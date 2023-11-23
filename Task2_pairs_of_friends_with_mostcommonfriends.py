from py2neo import Graph, Node

# Neo4j veritabanı bağlantısı
graph = Graph("bolt://localhost:7687", auth=("neo4j", "04629859"))

# Sorguyu tanımla
query = """
MATCH (u1:User)-[:FOLLOWS]->(u2:User)-[:FOLLOWS]->(u3:User),
      (u2)-[:FOLLOWS]->(u1:User)-[:FOLLOWS]->(u3)
WHERE u1 <> u2 AND u1 <> u3 AND u2 <> u3
WITH u1, u2, COLLECT(DISTINCT u3) AS mutualFriends, SIZE(COLLECT(DISTINCT u3)) AS mutualFriendsCount
WHERE mutualFriendsCount > 0
WITH u1, u2, mutualFriendsCount, mutualFriends
ORDER BY mutualFriendsCount DESC
LIMIT 10
RETURN u1.name AS user1, u2.name AS user2, mutualFriendsCount, [friend IN mutualFriends | friend.name] AS mutualFriends;
"""

# Sorguyu çalıştır ve sonuçları al
result = graph.run(query)

# Sonuçları ekrana yazdır
for record in result:
    user1 = record["user1"]
    user2 = record["user2"]
    count = record["mutualFriendsCount"]
    friends = record["mutualFriends"]

    # İstediğiniz çıktı formatını oluştur
    print(f"[{user1}, {user2}]\t\t\t\t{count}\t\t\t\t{friends}")
