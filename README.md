# E-Commerce Customer Churn Prediction System

## Problem
Customer acquisition costs 5-7x more than retention. This system identifies at-risk customers before they leave, enabling targeted retention campaigns that reduce churn by 15-20%.

# Dataset

Source: Kaggle E-Commerce Dataset
Size: 22,000 transactions, 17 features
Target: churn_90d - Will customer churn within 90 days?


Key Features: Session duration, customer rating, purchase history, delivery time, payment method, device type


# Clone repository

```bash
git clone https://github.com/codeWhizperer/Capstone-project.git
cd Capstone-project
```

# Build and run
```bash
docker build -t churn-predictor .
docker run -d -p 9696:9696 churn-predictor
```

# Test

```bash
curl http://localhost:9696/predict
```

# Install dependencies

```bash
pipenv install
pipenv shell
```

# Start service
```bash
python predict.py
```

# Test
```bash
python predict-test.py
```


## API Usage

### Request
```bash
 {
    'Age':32,
    'Gender': 'Male',
    'City': 'Istanbul',
    'Device_Type': 'Mobile',
    'Payment_Method': 'Credit Card',
    'Product_Category': 'Electronics',
    'Is_Returning_Customer': 'False',
    'Unit_Price': 804.06,
    'Quantity': 1,
    'Total_Amount': 574.78,
    'Session_Duration_Minutes': 8,
    'Pages_Viewed': 10,
    'Customer_Rating': 4,
    'Delivery_Time_Days':  1,
    'Discount_Amount': 229.28
}
```

### Response

```bash
{
  "churn_probability": float,
  "churn_probability": bool,
}
```


## 📁 Project Structure
```bash
├── data/                           # Dataset files
├── notebooks/
│   └── project.ipynb              # EDA & experimentation
├── train.py                       # Model training
├── predict.py                     # Flask API
├── predict-test.py                # Tests
├── model_C=10.bin                 # Trained model
├── Dockerfile                     # Container config
├── Pipfile / Pipfile.lock         # Dependencies
└── README.md
```

## Tech Stack

Python 3.12 | XGBoost | Pandas | Flask | Docker | Pipenv
