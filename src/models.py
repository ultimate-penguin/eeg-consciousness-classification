import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import roc_curve,roc_auc_score
def scale(X_train,X_test):
  scaler = StandardScaler()
  X_train_scaled=scaler.fit_transform(X_train)
  X_test_scaled=scaler.transform(X_test)
  return  X_train_scaled,X_test_scaled


def train_feature(model,X_train,X_test,y_train,y_test):
  fig, ax = plt.subplots(figsize=(8, 3))

  model.fit(X_train,y_train)

  y_pred = model.predict(X_test)


  print('Classification report')
  print(classification_report(y_test, y_pred))


  cm = confusion_matrix(y_test, y_pred)
  display = ConfusionMatrixDisplay(confusion_matrix=cm)
  display.plot(ax=ax)
  ax.set_title('Confusion Matrix')

  plt.tight_layout()
  plt.show()


def auc(model,X_test,y_test):
  y_prob = model.predict_proba(X_test)[:,1]
  fpr,tpr,th = roc_curve(y_test,y_prob)
  plt.plot(fpr,tpr)
  plt.show()
  auc_score = roc_auc_score(y_test, y_prob)
  return print(f"ROC AUC Score: {auc_score:.4f}")



def shap_plot(model,X_train,X_test,X_train_unscaled):
  explainer =shap.KernelExplainer(model.predict,shap.kmeans(X_train,10))
  shap_values =explainer.shap_values(X_test)
  return shap.summary_plot(shap_values,X_test,feature_names=X_train_unscaled.columns)
