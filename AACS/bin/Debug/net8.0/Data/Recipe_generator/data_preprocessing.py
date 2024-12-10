import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv('recipes.csv')
ingredients = data['ingredients'].values
dietary_restrictions = data['dietary_restrictions'].values
labels = data['recipe_id'].values

encoder = OneHotEncoder(handle_unknown='ignore')
encoded_restrictions = encoder.fit_transform(dietary_restrictions.reshape(-1, 1)).toarray()

X_train, X_test, y_train, y_test = train_test_split(encoded_restrictions, labels, test_size=0.2)