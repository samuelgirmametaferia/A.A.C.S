import pandas as pd
from sklearn.cluster import KMeans
import sqlite3

conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    date TEXT,
    category TEXT,
    amount REAL
)
''')

def analyze_spending():
    expenses = pd.read_sql_query("SELECT * FROM expenses", conn)
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(expenses[['amount']])
    expenses['cluster'] = kmeans.labels_
    return expenses

def suggest_budget():
    expenses = analyze_spending()
    cluster_means = expenses.groupby('cluster')['amount'].mean()
    for cluster, mean_amount in cluster_means.items():
        print(f"Cluster {cluster}: Average spending = ${mean_amount:.2f}")

    # Implement further budget suggestions based on cluster analysis

suggest_budget()
conn.close()