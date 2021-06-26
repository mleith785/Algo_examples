import unittest

class Node:
    def __init__(self, name):
        #pointers to child nodes, set empty first
        self.children = []
        #set the payload of the node
        self.name = name

    def addChild(self, name):
        #add a child onto the graph left to right
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        #We visited this node, add it to our array that we did the visit
        array.append(self.name)
        #recursively call each child with depth first search
        for i in self.children:
            i.depthFirstSearch(array)
        return array

    def breadthFirstSearch(self, array):
        # First we hold the root node
        queue = [self]

        # Check if the queue is empty
        while len(queue) > 0:
            # Take a node off of the queue
            # 1st time is parent
            current_node = queue.pop(0)
            # Append this nodes data/name to our return value
            array.append(current_node.name)
            # now add the children of current node onto queue

            for child_node in current_node.children:
                queue.append(child_node)
        # there are no more children BFS is done, return the order
        return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.depthFirstSearch([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])
        self.assertEqual(graph.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])

if __name__ == '__main__':
    unittest.main()


