import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, r2_score

data = pd.read_csv('run_data.csv', nrows=200000)
target_column = 'run_time_in_seconds'
X = data.drop(columns=[target_column, 'trip_id', 'date', 'start_time', 'end_time'])
y = data[target_column]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

rmse = root_mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(rmse)
print(r2)

input_length = 2

input_features = pd.DataFrame([[0]*len(X.columns)], columns=X.columns)
input_features['length'] = input_length

predicted = model.predict(input_features)
print(f"Predicted run time for {input_length} kilometers is {predicted[0]} seconds")
