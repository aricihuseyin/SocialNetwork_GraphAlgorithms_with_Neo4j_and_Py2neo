from py2neo import Graph

# Neo4j veritabanı bağlantısı
graph = Graph("bolt://localhost:7687", auth=("neo4j", "04629859"))

# Degree Centrality sorgusu
degree_centrality_query = """
CALL gds.degree.stream('myGraph')
YIELD nodeId, score
WITH gds.util.asNode(nodeId) AS user, score
RETURN user.name AS userName, score
ORDER BY score DESC
LIMIT 20
"""

result = graph.run(degree_centrality_query).data()

# Sonucu yazdır
if result:
    for row in result:
        print(f"User: {row['userName']}, Degree Centrality Score: {row['score']}")
else:
    print("No results found.")
