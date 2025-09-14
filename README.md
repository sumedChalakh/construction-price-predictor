# Construction Material Price Predictor

# Overview
This project predicts future prices of construction materials (like cement, steel, sand) using Machine Learning.

# Project Structure
- `data/` → dataset files
- `notebooks/` → Jupyter notebooks
- `src/` → Python scripts
- `results/` → model results & graphs

# Tech Stack
- Python, Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook

# Workflow
1. Data collection & cleaning
2. Exploratory Data Analysis (EDA)
3. Machine Learning models (Linear Regression, Random Forest, etc.)
4. Model evaluation (R², MAE, RMSE)


# Results

Predictions and evaluation metrics for construction material prices:

| Material | R² Score | MAE   | RMSE  | Plot |
|----------|----------|-------|-------|------|
| Cement   | -1.95    | 262.60 | 330.41 | ![Cement](results/Cement_price_prediction.png) |
| Steel    | -2.08    | 561.29 | 728.00 | ![Steel](results/Steel_price_prediction.png) |
| Sand     | -8.07    | 774.32 | 848.20 | ![Sand](results/Sand_price_prediction.png) |
| Bricks   | -3.33    | 234.06 | 299.39 | ![Bricks](results/Bricks_price_prediction.png) |
| Wood     | -12.55   | 566.65 | 672.28 | ![Wood](results/Wood_price_prediction.png) |



