from py2neo import Graph

# Neo4j veritabanı bağlantısı
graph = Graph("bolt://localhost:7687", auth=("neo4j", "04629859"))

# Label Propagation sorgusu
label_propagation_query = """
CALL gds.labelPropagation.stream('myGraph')
YIELD nodeId, communityId
WITH gds.util.asNode(nodeId) AS user, communityId
RETURN user.name AS userName, communityId
ORDER BY communityId, userName
"""

result = graph.run(label_propagation_query).data()

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
