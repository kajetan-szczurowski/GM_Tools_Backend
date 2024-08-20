import uuid

def make_node(label: str, description: str):
        new_id = uuid.uuid4().hex
        return {
            "label": label,
            "description": description,
            'id': new_id
        }

class AdjacencyList:
    def __init__(self, first_node = None):
        self.list = {}
        if first_node is not None:
            self.insert_node(first_node)

    def insert_node(self, node):
        if node['id'] in self.list:
            return
        
        new_node = {"content": node, "edges": []}
        self.list[node['id']] = new_node

    def insert_edge(self, node1, node2):
        if node1['id'] not in self.list or node2['id'] not in self.list:
            return
        
        if node2['id'] not in self.list[node1['id']]['edges']:
            self.list[node1['id']]['edges'].append(node2['id'])

        if node1['id'] not in self.list[node2['id']]['edges']:
            self.list[node2['id']]['edges'].append(node1['id'])

    def node_edges_to_string(self, node):
        result = ''
        # print(self.list[node]['edges'])
        # exit()
        for edge in self.list[node]['edges']:
            print(edge)
            result += f'{self.list[edge]['content']['label']}, '
        return result

    def __str__(self):
        result = ''
        for node in self.list:
            # result += f'{self.list[node]['content']['label']} => \n'
            result += f'{self.list[node]['content']['label']} => {self.node_edges_to_string(node)} \n'

        
        return result
    

if __name__ == '__main__':
    test_node = make_node('jestem nodem', 'i moja praca to przekazywanie informacji')
    test_node2 = make_node('jestem nodem2137', 'lul')
    test_graph = AdjacencyList(test_node)
    test_graph.insert_node(test_node2)
    test_graph.insert_edge(test_node, test_node2)
    print(test_graph)