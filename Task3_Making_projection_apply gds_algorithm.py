from py2neo import Graph

# Neo4j veritabanı bağlantısı
graph = Graph("bolt://localhost:7687", auth=("neo4j", "04629859"))

# Graf oluşturma sorgusu
graph.run("""
CALL gds.graph.project(
  'myGraph',
  'User',
  { FOLLOWS: { type: 'FOLLOWS', orientation: 'UNDIRECTED' } }
);
""")

print("Graph created successfully.")
