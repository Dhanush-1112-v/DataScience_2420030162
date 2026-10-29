import numpy as np 
from sklearn.linear_model import LinearRegression, LogisticRegression,logisticRegression
#linear regression
print("........Linear Regression........")
x=line=np.array([[1000],[1200],[1500],[1800],[2000]])
#dependent variable
y=np.array([50,55,65,80,90])
#create linear regression model
linear_model=LinearRegression()
#train the model
linear_model.fit(x,y)
#predict the value of y for a new house
new_house_size=np.array([[1700]])
predicted_price=linear_model.predict(new_house_size)
print("traning house sizes:")
print(x.flatten())
print("traning house sizes:")
print(y)
print("\npredicted price for 1700 sq ft house is: ",predicted_price[0] )
# logistic regression
print("\n........Logistic Regression........")
#independent variable
x_logistic=np.array([[40],[50],[60],[70],[80]])
#dependent variable
y_logistic=np.array([0,0,0,1,1])
#create logistic regression model
logistic_model=LogisticRegression()
#train the model
logistic_model.fit(x_logistic,y_logistic)
#predict wheather customer purchases
test_price=np.array([[75]])
purchase_prediction=logistic_model.predict(test_price)
print("traning house sizes:")
print(x_logistic.flatten())
print("traning house sizes:")
print(y_logistic)
print("\ntest house size: ",test_price[0][0])
print("\npredicted purchase decision (0=No, 1=Yes): ",purchase_prediction[0])
print("\npredection probability: ",logistic_model.predict_proba(test_price)[0])
