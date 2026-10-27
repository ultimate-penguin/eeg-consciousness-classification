# EEG-based Classification of Awake and Propofol Sedated States using Information-Theoretic and Spectral Features 


## 📌 Project Overview
Loss of consciousness under anesthesia is associated with changes in neural dynamics.Conventional EEG biomarkers rely primarily on spectral power, while Integrated Information Theory (IIT) motivates the use of information-theoretic measures describing integration and complexity. This project compares EEG spectral features with several IIT-inspired proxy measures for distinguishing awake and sedated states.

## 📊 Dataset
* **Source:** OpenNeuro ds005620 [A repeated awakening study exploring the capacity of complexity measures to capture dreaming during propofol sedation]
* **citation:**  Imad J. Bajwa1, Andre S. Nilsen1, René Skukies1,3, Arnfinn Aamodt1, Gernot Ernst2, Johan F. Storm1, and Bjørn E. Juel1,2 (2024). A repeated awakening study exploring the capacity of complexity measures to capture dreaming during propofol sedation. OpenNeuro. [Dataset] doi: doi:10.18112/openneuro.ds005620.v1.0.0
* **License:** The source code in this repository is licensed under the MIT License.
  The underlying dataset and processed data are derived from [ OpenNeuro ds005620] and are licensed under CC BY-4.0.

______________________________________

## 🛠️ Project Pipeline
Raw EEG

↓

Preprocessing

↓

Feature Extraction

↓

Statistical Analysis

↓

Machine Learning

↓

SHAP Interpretation
________________________________________
Features\
Spectral\
•	Delta\
•	Theta\
•	Alpha\
•	Beta\
Information-theoretic\
•	Mean pairwise mutual information (MI)\
•	O-information (o-info)\
•	Lempel–Ziv complexity (complexity)
________________________________________
Models
•	Logistic Regression\
•	Random Forest\
•	SVM\
•	KNN\
**These models are used to train on spectral features only. Since SVM and Random Forest yeild the best results, only they are selected to train the other feature sets**
________________________________________
Results

Feature Set			Accuracy\
Spectral			78%\
IIT proxies			71%\
Spectral + MI			80%\
Spectral + Complexity		79%\
Spectral + O-information	78%\
Spectral + All IIT		79%
________________________________________
## 🚀 Key Findings

•	Spectral EEG features provided the strongest standalone classification performance.\
•	All information-theoretic features showed statistically significant differences between awake and sedated conditions.\
•	Mean pairwise mutual information consistently improved classification when combined with spectral features.\
•	Lempel–Ziv complexity decreased during sedation, consistent with previous anesthesia studies.\
•	Pairwise mutual information increased during sedation, suggesting stronger statistical dependence between EEG channels.\
•	O-information also increased during sedation, indicating a possible shift toward more redundancy-dominated interactions.
________________________________________
##    Scientific interpretation

Integrated Information Theory proposes that conscious states are characterized by richer and more integrated information processing. Since direct computation of integrated information (Φ) is computationally infeasible for EEG, this study evaluated several information-theoretic proxy measures.
The results indicate that these proxies are sensitive to changes between awake and propofol-sedated EEG. Among the evaluated measures, mean pairwise mutual information provided the greatest complementary information beyond conventional spectral features, whereas complexity and O-information showed significant state differences but limited improvement in classification performance.
These findings are consistent with the broader literature reporting reduced EEG complexity during anesthesia and increased statistical dependence among cortical signals during propofol sedation. However, because the evaluated measures are proxies rather than direct estimates of Φ, the results should be interpreted as being consistent with, rather than direct validation of, Integrated Information Theory.
________________________________________
##Limitations

•	Pairwise mutual information is not equivalent to integrated information (Φ).\
•	O-information remains an emerging measure with limited validation in anesthesia.\
•	Results are specific to propofol sedation.\
•	Feature extraction was performed on fixed EEG windows.

________________________________________
Future Work

•	Deep learning on raw EEG\
•	Functional connectivity networks\
•	Exact Φ approximations
________________________________________

## 📁 Repository Structure
```text
eeg-consciousness-classification/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── data/
│   ├── README.txt
│   └── download_data.py
|   |__awake.csv/sedate.csv
│
├── notebooks/
│   ├── 01_data_overview.ipynb
│   ├── 02_dataset_preparation.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_models_training.ipynb
│   
│
├── src/
│   ├── prepare_data.py
│   ├── analysis.py
│   ├── models.py
│
├── results/
│   ├── individual_eeg/   # single subject eeg visualization and data
│   └── eda_result/       # feature distribution, correlation,t-test result
|   |__ model_result/      # classification reports, roc curve, confusion matrix, shap summary plot
│    
│
└── docs/project_summary.pdf

```

## 💻 Getting Started

### Prerequisites
Ensure you have Python installed locally.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ultimate-penguin/eeg-consciousness-classification.git
   cd eeg-consciousness-classification
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## References


## 👤 Author
* **Ultimate Penguin** - [Github]( https://github.com/ultimate-penguin)
