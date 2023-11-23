from py2neo import Graph

# Neo4j veritabanı bağlantısı
graph = Graph("bolt://localhost:7687", auth=("neo4j", "04629859"))

# Louvain sorgusu
louvain_query = """
CALL gds.louvain.stream('myGraph')
YIELD nodeId, communityId
WITH gds.util.asNode(nodeId) AS user, communityId
RETURN user.name AS userName, communityId
ORDER BY communityId, userName
"""

result = graph.run(louvain_query).data()

# Sonucu yazdır
if result:
    current_community = None
    for row in result:
        if current_community != row['communityId']:
            print(f"\nCommunity {row['communityId']}:")
            current_community = row['communityId']
        print(f"  User: {row['userName']}")
else:
    print("No communities found.")
