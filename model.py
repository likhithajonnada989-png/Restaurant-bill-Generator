import pandas as pd
from sklearn.neighbors import NearestNeighbors
from data import orders

# Get all unique items
all_items = list(set(item for order in orders for item in order))

# Convert orders to binary matrix
def create_matrix(orders, items):
    matrix = []
    for order in orders:
        row = [1 if item in order else 0 for item in items]
        matrix.append(row)
    return pd.DataFrame(matrix, columns=items)

df = create_matrix(orders, all_items)

# Train model
model = NearestNeighbors(metric='cosine')
model.fit(df)

# Recommendation function
def predict_order(selected_items):
    if not selected_items:
        return []

    input_vec = [1 if item in selected_items else 0 for item in all_items]

    distances, indices = model.kneighbors([input_vec], n_neighbors=2)

    nearest_order = df.iloc[indices[0][1]]

    recommendations = [
        item for item in all_items
        if nearest_order[item] == 1 and item not in selected_items
    ]

    return recommendations