import requests

host = 'churn-serving-envs.eba-7wwmcpex.eu-west-1.elasticbeanstalk.com'
url = f'http://{host}/predict'

customer = {
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

response = requests.post(url, json=customer)
data = response.json()

# Extract predicted values
churn = data.get('churn')
prob = data.get('churn_probability')

print(f"Churn prediction: {churn}")
print(f"Churn probability: {prob:.4f}")

if churn:
    print("The customer is likely to churn.")
else:
    print("The customer is likely to stay.")