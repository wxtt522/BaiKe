import json

from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "123456"))


def add_friend(tx, name, friend_name):
    tx.run("MERGE (a:Person {name: $name}) "
           "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
           name=name, friend_name=friend_name)


def add_node(tx, category, relation, title):
    tx.run(
        "MERGE (a:Finance {category: $category}) ""MERGE (b:Entry {title: $title}) ""MERGE (a)-[:" + relation + "]-> (b)",
        category=category, title=title)


def add_node_more(tx, category1, category2, relation, title):
    tx.run(
        "MERGE (a:Finance {category: $category1}) " "MERGE (b:Finance {category: $category2}) " "MERGE (c:Entry {title: $title}) ""MERGE (a)-[:" + relation + "]-> (c)""MERGE (b)-[:" + relation + "]-> (c)",
        category1=category1, category2=category2, title=title)


def add_jinrong(tx, js):
    tx.run("MERGE (a:Finance {$jsx}) ", jsx=js)


def print_friends(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
                         "RETURN friend.name ORDER BY friend.name", name=name):
        print(record["friend.name"])


# with driver.session() as session:
#     session.write_transaction(add_friend, "Arthur", "Guinevere")
#     session.write_transaction(add_friend, "Arthur", "Lancelot")
#     session.write_transaction(add_friend, "Arthur", "Merlin")
#     session.read_transaction(print_friends, "Arthur")

with driver.session() as session:
    for line in open("baike_jingjixue.json", "r", encoding="utf8").readlines():
        dic = json.loads(line[:-2])
        print(json.dumps(dic, ensure_ascii=False))
        category2 = dic["category_2"]
        if category2:
            session.write_transaction(add_node_more, dic["category_1"], dic["category_2"], "开放分类", dic["title"])
        else:
            session.write_transaction(add_node, dic["category_1"], "开放分类", dic["title"])
