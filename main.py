import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

run_data = pd.read_csv('run_data.csv')
lr = LinearRegression()

x = run_data[['length', 'segment', 'direction']]
y = run_data['run_time_in_seconds']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(mse)


