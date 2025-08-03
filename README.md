# 📈 Linear Regression Practical Implementation

This repository contains a hands-on implementation of **Linear Regression** using Python and `scikit-learn`. The goal is to predict salaries based on years of experience from a real-world dataset. The project includes data preprocessing, model training, evaluation, and visualization of results.

## 👩‍💻 Author
**Sidra Saqlain**  
Bachelor of Science in Data Science  
Sir Syed University of Engineering and Technology (SSUET), Karachi

---

## 📁 Dataset Used
- **File**: `Salary_Data.csv`  
- **Features**:
  - `YearsExperience`: Independent variable
  - `Salary`: Dependent variable

---

## 📌 Workflow

1. **Importing Required Libraries**  
2. **Reading and Exploring the Dataset**  
3. **Checking for Null Values & Correlation**  
4. **Feature Scaling using StandardScaler**  
5. **Splitting Dataset into Training and Testing Sets**  
6. **Model Training using Linear Regression**  
7. **Model Evaluation:**
   - Mean Squared Error (MSE)
   - R² Score  
8. **Visualization:**
   - Actual vs Predicted Salaries
   - Residuals Distribution

---

## 🧪 Model Performance

- **Mean Squared Error (MSE)**: `37784662.47`
- **R² Score**: `0.9414`

📊 **Interpretation**: The model explains over 94% of the variance in the salary data, indicating a strong linear relationship between experience and salary.

---

## 📉 Visualizations

- 📍 Scatter Plot (Actual vs Predicted)
- 📍 Residual Distribution using Seaborn KDE

---

## 🔧 Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📦 How to Run

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# Run the Jupyter notebook
jupyter notebook
