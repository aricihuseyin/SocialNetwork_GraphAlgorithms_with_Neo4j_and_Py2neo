from py2neo import Graph

# Neo4j veritabanı bağlantısı
graph = Graph("bolt://localhost:7687", auth=("neo4j", "04629859"))

# Betweenness Centrality sorgusu
betweenness_centrality_query = """
CALL gds.betweenness.stream('myGraph')
YIELD nodeId, score
WITH gds.util.asNode(nodeId) AS user, score
RETURN user.name AS userName, score
ORDER BY score DESC
LIMIT 20
"""

result = graph.run(betweenness_centrality_query).data()

# Sonucu yazdır
if result:
    for row in result:
        print(f"User: {row['userName']}, Betweenness Centrality Score: {row['score']}")
else:
    print("No results found.")
