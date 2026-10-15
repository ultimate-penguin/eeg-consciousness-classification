The EEG dataset is available from OpenNeuro:

https://openneuro.org/datasets/ds005620

This project only used data from task-awake_acq-EC and task-sed_acq-rest

Download the dataset and place it inside this folder.

## Authors
- Imad J. Bajwa
- Andre S. Nilsen
- René Skukies
- Arnfinn Aamodt
- Gernot Ernst
- Johan F. Storm
- Bjørn E. Juel

## Ethics Statement
Approved by the Regional Committees for Medical Research Ethics South East Norway (REK), ref. 2015/1520.

## License
This dataset is licensed under CC-BY-4.0.

## File Structure

The dataset is organized by subject, with each subject's EEG files stored in a dedicated directory. Below is the structure for the EEG data associated with a sample subject (sub-1016).

### Directory Structure
```
/Volumes/IMADS SSD/Anesthesia_conciousness_paper/project_BIDS/
└── sub-1016/
    └── eeg/
        ├── sub-1016_task-awake_acq-EC_channels.tsv
        ├── sub-1016_task-awake_acq-EC_eeg.eeg
        ├── sub-1016_task-awake_acq-EC_eeg.json
        ├── sub-1016_task-awake_acq-EC_eeg.vhdr
        ├── sub-1016_task-awake_acq-EC_eeg.vmrk
        ├── sub-1016_task-awake_acq-EC_events.json
        ├── sub-1016_task-awake_acq-EC_events.tsv
        ├── ...
```

### File Naming Convention
EEG files are named in the format:
`sub-<subject_id>_task-<task_name>_acq-<acquisition>_run-<run_number>.<extension>`

### Example Filenames
- `sub-1016_task-awake_acq-EC_channels.tsv`
- `sub-1016_task-sed_acq-rest_run-1_eeg.eeg`

### Filename Components
- **sub-<subject_id>**: Identifier for the subject (e.g., `sub-1016`).
- **task-<task_name>**: Indicates the task condition:
  - `awake`: Wakefulness
  - `sed`: Sedation condition
  - `sed2`: One-minute resting EEG recorded just before an awakening
- **acq-<acquisition>**: Type of acquisition:
  - `EC`: Eyes Closed (during wakefulness)
  - `EO`: Eyes Open (during wakefulness)
  - `tms`: Session with Transcranial Magnetic Stimulation
  - `rest`: Rest condition (during sedation)
- **run-<run_number>**: Specifies the run number for the data collection:
  - `run-1`, `run-2`, `run-3` (indicating different awakenings in sedation)
- **.<extension>**: File extension indicating the type of file (e.g., `.eeg`, `.vhdr`, `.vmrk`, etc.).

### File Types
- **.eeg**: Raw EEG data.
- **.vhdr**: BrainVision header file.
- **.vmrk**: BrainVision marker file.
- **_events.json / _events.tsv**: Event markers.
- **_channels.tsv / _eeg.json**: Channel information and metadata.


