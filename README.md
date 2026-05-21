# Campus Placement Predictor 🎓

An end-to-end Machine Learning web application that predicts whether a college student will get placed based on two key features: **CGPA** and **IQ**. 

The core predictive engine uses a **Logistic Regression** classification model trained on student data, with feature normalization handled seamlessly across the pipeline.

## 🚀 Features
* **Machine Learning Driven:** Leverages a trained Scikit-Learn classification model (`model.pkl`).
* **Feature Pipeline Preservation:** Integrates a serialized `StandardScaler` configuration (`scaler.pkl`) to ensure live user inputs match the exact mathematical distribution of the training data.
* **Interactive UI:** A lightweight, responsive dashboard built completely in Python using Streamlit.

## 🛠️ Tech Stack
* **Language:** Python 3.14
* **ML Libraries:** Scikit-Learn, NumPy
* **Web Framework:** Streamlit
* **Data Processing:** Jupyter Notebook (`project.ipynb`)

## 📐 Machine Learning Pipeline
1. **Data Preprocessing:** Handled feature variance using `StandardScaler` to normalize raw metrics.
2. **Model Training:** Fit a Logistic Regression classifier to optimize the decision boundary separating placed and unplaced student data clusters.
3. **Serialization:** Saved both the trained model weights and the feature scale configuration using `pickle` for low-latency inference in production.

## 💻 Local Installation

1. Clone the repository:
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
cd "Mechine Learning"
