import glob
import re
import mne
from sklearn.feature_selection import mutual_info_regression
import antropy as ant
import numpy as np
from hoi.metrics import Oinfo
import pandas as pd
def get_file_paths(root,task,extra_sedate_path):
  if task == 'awake':
    awake_vhdr_paths = glob.glob(f'{root}/**/*_task-awake_acq-EC_eeg.vhdr', recursive=True)
    
    print(f"Found {len(awake_vhdr_paths)} awake .vhdr files:")
    awake_vhdr_paths.sort(key=get_subject_id)
    return awake_vhdr_paths
    
  elif task == 'sedated':
    if 'awake' in extra_sedate_path:
      return print('error:choose extra path from sedate task')
      

    sedate_vhdr_paths = glob.glob(f'{root}/**/*_task-sed_acq-rest_run-1*.vhdr', recursive=True)
    sedate_vhdr_paths.append(extra_sedate_path)
    print(f"Found {len(sedate_vhdr_paths)} sedated .vhdr files:")
    sedate_vhdr_paths.sort(key=get_subject_id)
    return sedate_vhdr_paths
    
    
   

  else:
    return print('invalid task, valid task names include awake and sedated')



def get_subject_id(path):
    match = re.search(r'sub-(\d+)', path)
    if match:
        return int(match.group(1))
    return -1 # Return -1 or handle error if no subject ID is found



def preprocess_eeg(path):
  data=mne.io.read_raw_brainvision(path, preload=True, verbose=True)
  data_processed = data.copy().set_eeg_reference(ref_channels="average") 
  data_filtered = data_processed.copy().filter(l_freq=0.1, h_freq=40)
  return data_filtered


def spectral_bands(eeg_data,ch):
  alpha=eeg_data.copy().pick(picks=ch).filter(l_freq=8,h_freq=12)
  beta=eeg_data.copy().pick(picks=ch).filter(l_freq=12,h_freq=30)
  theta=eeg_data.copy().pick(picks=ch).filter(l_freq=4,h_freq=8)
  delta=eeg_data.copy().pick(picks=ch).filter(l_freq=1,h_freq=4)
  return alpha,beta,theta,delta



def epoch(clean_data,alpha,beta,theta,delta,window_size,step_size,ch):
  eeg_data=clean_data.copy().pick(picks=ch).get_data()
  alpha_data = alpha.get_data()
  beta_data = beta.get_data()
  theta_data = theta.get_data()
  delta_data = delta.get_data()
  eeg_windows=[]
  alpha_windows=[]
  beta_windows=[]
  theta_windows=[]
  delta_windows=[]
# Slide across the data
  for start in range(0, eeg_data.shape[1] - window_size, step_size):
    end = start + window_size
    window_data1 = eeg_data[:,start:end]  
    eeg_windows.append(window_data1)
    window_data2 = alpha_data[:,start:end]  
    alpha_windows.append(window_data2)
    window_data3 = beta_data[:,start:end]  
    beta_windows.append(window_data3)
    window_data4 = theta_data[:,start:end]  
    theta_windows.append(window_data4)
    window_data5 = delta_data[:,start:end]  
    delta_windows.append(window_data5)
  return eeg_windows,alpha_windows,beta_windows,theta_windows,delta_windows



def lzc_feature(eeg):

    complexity = []

    for ch in eeg:

        # convert continuous EEG into binary sequence
        median = np.median(ch)

        binary = (ch > median).astype(int)

        lzc = ant.lziv_complexity(
            binary,
            normalize=True
        )

        complexity.append(lzc)

    return np.mean(complexity)



def mutual_information(eeg):
    """
    eeg:
        numpy array
        shape = (channels, samples)

    returns:
        average pairwise mutual information
    """

    n_channels = eeg.shape[0]

    MI_values = []

    for i in range(n_channels):
        for j in range(i+1, n_channels):

            x = eeg[i]
            y = eeg[j]

            mi = mutual_info_regression(
                x.reshape(-1,1),
                y
            )[0]

            MI_values.append(mi)

    return np.mean(MI_values)



def compute_o(eeg):

# 2. Extract the non-continuous data points
  sampled_data =eeg.T # Shape: (200, 6)

# 3. Compute O-information 
  model = Oinfo(sampled_data)
  oi_value = model.fit(minsize=6, maxsize=6)
  return oi_value



def feature_extraction(eeg_windows,alpha_windows,beta_windows,theta_windows,delta_windows,task,path):
  alpha_list=[]
  beta_list=[]
  theta_list=[]
  delta_list=[]
  o_info_list=[]
  MI_list=[]
  complex_list=[]
  label=[]
  sub_id=[]
  for i,chunk in enumerate(eeg_windows):
    if i ==100:
      break
    LZC_feature = lzc_feature(chunk)
    MI_feature = mutual_information(chunk)
    o_info=compute_o(chunk)[0][0]
    alpha_value=alpha_windows[i].mean(axis=1).mean(axis=0)
    beta_value=beta_windows[i].mean(axis=1).mean(axis=0)
    theta_value=theta_windows[i].mean(axis=1).mean(axis=0)
    delta_value=delta_windows[i].mean(axis=1).mean(axis=0)
    alpha_list.append(alpha_value)
    beta_list.append(beta_value)
    theta_list.append(theta_value)
    delta_list.append(delta_value)
    o_info_list.append(o_info)
    MI_list.append(MI_feature)
    complex_list.append(LZC_feature)
    label.append(task)
    sub_id.append(get_subject_id(path))
    print(f'window:{i}')
  print('done')
  return alpha_list,beta_list,theta_list,delta_list,o_info_list,MI_list,complex_list,label,sub_id



def get_dataset(list_of_path,task,task_df,ch,window_size,step_size):
  for path in list_of_path:
    clean_data=preprocess_eeg(path)
    
    alpha,beta,theta,delta=spectral_bands(clean_data)
    
    eeg_windows,alpha_windows,beta_windows,theta_windows,delta_windows=epoch(clean_data,alpha,beta,theta,delta,window_size,step_size)
    
    alpha_list,beta_list,theta_list,delta_list,o_info_list,MI_list,complex_list,label,sub_id=feature_extraction(eeg_windows,alpha_windows,beta_windows,theta_windows,delta_windows,task,path)

    df=pd.DataFrame({'subject':sub_id,'alpha':alpha_list,'beta':beta_list,'theta':theta_list,'delta':delta_list,'o-info':o_info_list,'MI':MI_list,'complexity':complex_list,'label':label})
    task_df = pd.concat([task_df, df], ignore_index=True)
    print(f'subject:{get_subject_id(path)}')
    return task_df
