from py2neo import Graph

# Neo4j veritabanı bağlantısı
graph = Graph("bolt://localhost:7687", auth=("neo4j", "04629859"))

# Louvain sorgusu ve toplulukları kullanıcı düğümlerine yazma
write_communities_query = """
CALL gds.louvain.stream('myGraph')
YIELD nodeId, communityId
WITH gds.util.asNode(nodeId) AS user, communityId
SET user.community = communityId
"""

graph.run(write_communities_query)
