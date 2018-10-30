import sys
""" 
The general algorithm:
    1) make a tree
    2) calculate the total lengths of paths from root to each leaf
    3) find longest path
    4) recurse again from root, this time for each edge you find,
       add enough weight such that the leaf with the max path that has
       a path containing that edge will have the same max path as the
       longest path you found previously.
    5) return
(just an implementation problem I believe)
"""

class Node:
    def __init__(self, v):
        self.l = None
        self.r = None
        self.v = v

    def add(self, node):
        if self.l == None:
            self.l = node
        elif self.r == None:
            self.r = node
    
    def can_add(self):
        return self.l == None or self.r == None
    
    def print_node(self):
        sys.stdout.write("{} {}\n".format(self.v, self.w))

class Tree:
    def __init__(self, num_nodes, edges):
        self.root = None
        self.edges = {}
        if num_nodes > 0:
            self.root = Node(1)
            queue = [self.root]
            nodes = list(range(2, num_nodes + 1))
            while len(nodes) != 0:
                parent = queue.pop(0)
                edges = []
                if e
                while parent.can_add():
                    child = Node(nodes.pop(0))
                    queue.append(child)
                    parent.add(child)
            
            p_node = 1
            for in edges:
                self.edges[p_node] = 

    def print_tree(self):
        self.root.print_node()
        queue = [self.root]
        while len(queue) != 0:
            node = queue.pop(0)
            if node.l != None:
                queue.append(node.l)
                node.l.print_node()
            if node.r != None:
                queue.append(node.r)
                node.r.print_node()

def get_tree(nodes):
    tree = Tree(Node(*nodes[0]))
    queue = [tree.root]
    unadded_nodes = nodes[1:]
    while len(unadded_nodes) != 0:
        parent = queue.pop(0)
        while parent.can_add():
            child = Node(*unadded_nodes.pop(0))
            parent.add(child)
            queue.append(child)
    return tree

def get_tc(filename):
    with open(filename) as fl:
        return fl.read()

def run(filename):
    tc = get_tc(filename).split("\n")[:-1]
    header = tc[0]
    num_nodes = int(tc[1])
    nodes = [ [int(n) for n in v.strip().split(" ")] for v in tc[2:] ]
    
    tree = get_tree(nodes)
    sys.stdout.write(header + "\n")
    sys.stdout.write(tc[1] + "\n")
    for s, e in nodes:
        sys.stdout.write("{} {}\n".format(s, e))

if __name__ == "__main__":
    f1 = "input1.txt"
    f2 = "input2.txt"
    run(f2)
