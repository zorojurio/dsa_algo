

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def breadth_first_search(self, start_vertex, end_vertex):
        queue = [[start_vertex]]
        while queue:
            path = queue.pop(0)
            node = path[-1]  # get the last node from the path
            if node == end_vertex:  # if the last node is the end
                return path
            for adjacent in self.gdict.get(node, []):  # if it is not the end node -> loop adjacent_vertices
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


if __name__ == '__main__':
    # customDict = {"a": ["b", "c"],
    #               "b": ["d", "g"],
    #               "c": ["d", "e"],
    #               "d": ["f"],
    #               "e": ["f"],
    #               "g": ["f"]
    #               }

    customDict = {"a": ["b", "c"],
                  "b": ["d", ],
                  "c": ["d", "e"],
                  "e": ["f"],
                  "f": ["g"]
                  }
    g = Graph(customDict)
    print(g.breadth_first_search("a", "g"))