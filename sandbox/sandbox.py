#Place for messing with code while developement
from assets import make_node, AdjacencyList

room_types = ['pit', 'torture_room', 'crypt', 'wine cellar', 'treasure room']

test_node = make_node('jestem nodem', 'i moja praca to przekazywanie informacji')
test_node2 = make_node('jestem nodem2137', 'lul')
test_graph = AdjacencyList(test_node)
test_graph.insert_node(test_node2)
test_graph.insert_edge(test_node, test_node2)
print(test_graph)
