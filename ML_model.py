import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

train_df = pd.read_csv("/content/sample_data/california_housing_train.csv")
test_df = pd.read_csv("/content/sample_data/california_housing_test.csv")


features = ['housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income']
target = 'median_house_value'

X_train = train_df[features]
y_train = train_df[target]
X_test = test_df[features]
y_test = test_df[target]

X_train['total_bedrooms'].fillna(X_train['total_bedrooms'].mean(), inplace=True)
X_test['total_bedrooms'].fillna(X_test['total_bedrooms'].mean(), inplace=True)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

feature_importance = pd.DataFrame({'Feature': features, 'Coefficient': model.coef_})
feature_importance = feature_importance.sort_values(by='Coefficient', ascending=False)
plt.figure(figsize=(10, 4))
sns.barplot(x='Coefficient', y='Feature', data=feature_importance)
plt.title("Feature Importance")
plt.show()

print(train_df.head())
print(train_df.info())
print(train_df.describe())



print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
