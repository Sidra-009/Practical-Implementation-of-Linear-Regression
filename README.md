# 📊 Linear Regression Practical Implementation

This project demonstrates a practical implementation of **Linear Regression** using the California Housing dataset from scikit-learn. The goal is to predict housing prices 🏠 based on various features through a supervised machine learning approach 🤖.

## 📚 Dataset

- The dataset used is the **California Housing dataset**, which includes features like median income 💰, house age 🕰️, average rooms 🛏️, population 👥, and more.
- Data is loaded using `fetch_california_housing` from scikit-learn and converted into a pandas DataFrame 🐼 for easier manipulation.

## ⚙️ Workflow

1. **Data Preparation**  
   - Features (`X`) and target (`y`) variables are extracted from the dataset.
   - The dataset is split into training and testing sets (70% train 🚂, 30% test 🎯).

2. **Feature Scaling**  
   - Features are standardized using `StandardScaler` 📏 to improve model performance.

3. **Model Training**  
   - A Linear Regression model 🧮 is trained on the scaled training data.

4. **Model Evaluation**  
   - Cross-validation with 10 folds 🔄 is performed to evaluate Mean Squared Error (MSE).
   - Predictions are made on the test set 🔍.
   - Residuals are visualized using a KDE plot 📈.
   - The model’s performance is assessed using the R² score 🎯.

## 🚀 Usage

- Clone the repository 📥.
- Run the Jupyter notebook or Python script 🐍 to execute the workflow.
- Modify and extend the project by experimenting with feature engineering 🛠️ or different regression models.

## 🛠️ Dependencies

- Python 3.x 🐍
- numpy 🔢
- pandas 🐼
- matplotlib 📊
- seaborn 🌊
- scikit-learn 🤖

You can install the dependencies using:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
