from py2neo import Graph

# Neo4j veritabanı bağlantısı
graph = Graph("bolt://localhost:7687", auth=("neo4j", "04629859"))

# En kısa yol sorgusu
query = """
CALL gds.allShortestPaths.stream('myGraph')
YIELD sourceNodeId, targetNodeId, distance
WITH sourceNodeId, targetNodeId, distance
WHERE gds.util.isFinite(distance) = true
WITH gds.util.asNode(sourceNodeId) AS source, gds.util.asNode(targetNodeId) AS target, distance WHERE source <> target

RETURN source.name AS source, target.name AS target, distance
ORDER BY distance DESC, source ASC, target ASC
LIMIT 10
"""

result = graph.run(query).data()

# Sonucu yazdır
if result:
    for row in result:
        print(f"Source: {row['source']}, Target: {row['target']}, Distance: {row['distance']}")
else:
    print("No paths found.")
