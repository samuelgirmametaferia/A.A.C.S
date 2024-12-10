from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv("food_waste_data.csv")
X = data.drop("waste", axis=1)
y = data["waste"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy}")