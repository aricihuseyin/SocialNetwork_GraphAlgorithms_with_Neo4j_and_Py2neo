import pandas as pd
from py2neo import Graph, Node

# Read the Excel file with the adjacency matrix
file_path = 'socialnetwork.xlsx'  # Excel dosyanızın yolunu belirtin
df = pd.read_excel(file_path, index_col=0)

# Reset the index to create numerical indices
df = df.reset_index()

# Connect to the Neo4j database
uri = "bolt://localhost:7687"  # Neo4j sunucu bilgilerinize göre güncelleyin
username = "neo4j"
password = "04629859"
graph = Graph(uri, auth=(username, password))

# Create nodes and relationships
for i, row in df.iterrows():
    user1 = row['index']
    cleaned_user1 = ''.join(e for e in user1 if e.isalnum())

    # Create user node
    user_node = Node("User", name=cleaned_user1)
    graph.create(user_node)

    # Create relationships for follows
    for j, follows in enumerate(row[1:]):
        if follows == 1:
            user2 = df.columns[j + 1]
            cleaned_user2 = ''.join(e for e in user2 if e.isalnum())

            # Create FOLLOWS relationship
            query = (
                f"MATCH (u1:User {{name: '{cleaned_user1}'}}), "
                f"(u2:User {{name: '{cleaned_user2}'}}) "
                "CREATE (u1)-[:FOLLOWS]->(u2)"
            )
            graph.run(query)

print("Social media graph loaded into Neo4j.")
