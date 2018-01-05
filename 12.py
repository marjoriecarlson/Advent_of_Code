#!/usr/bin/python

class Node(object):
    def __init__(self, nodeIndex, children):
        self.nodeIndex = nodeIndex
        self.children = children

    def __str__(self):
        return str(self.nodeIndex) + ' ' + str(self.children)

class Tree(object):
    def __init__(self):
        self.nodes = []
        
    def add(self, nodeIndex, children):
        self.nodes.append(Node(nodeIndex, children))

    def getNode(self, nodeIndex):
        return self.nodes[nodeIndex]

    # visit the node's children if they haven't already been;
    # add them to the visited list; recurse to visit THEIR children
    def dfs(self, nodeIndex, visited):
        for childIndex in self.nodes[nodeIndex].children:
            if childIndex not in visited:
                visited.append(childIndex)
                self.dfs(childIndex, visited)
        return visited

    # the connected subgraph a node is in is all the ones you
    # can reach through DFS from it.
    def getConnectedSubgraphSize(self, nodeIndex):
        visited = self.dfs(nodeIndex, [nodeIndex])
        return len(visited)

    def countSubgraphs(self):
        subgraphs = 0
        visited = []  # will track ALL nodes seen

        # iterate through nodes. If not yet seen, they're in a new
        # subgraph; increment subgraphs and add all the nodes
        # in that tree's subgraph to 'visited'
        for nodeIndex in range(len(self.nodes)):
            if nodeIndex not in visited:
                subgraphs += 1
                visited.extend(self.dfs(nodeIndex, [nodeIndex]))
        return subgraphs
                
                          
    def __str__(self):
        string = ""
        for node in self.nodes:
            string += str(node) + '\n'
        return string[:-1]

input = open('input/11.txt','r')
lines = input.readlines()

tree = Tree()
for line in lines:
    info = line.rstrip('\n ').split(' <-> ')
    nodeNum = info[0]
    children = info[1].split(',')
    for i in range(len(children)):
        children[i] = int(children[i])
    tree.add(nodeNum, children)

# solution to part A: how many nodes are connected to 0?    
print tree.getConnectedSubgraphSize(0), "nodes connected to 0"
# solution to part B: how many disconnected subgraphs are there?
print tree.countSubgraphs(), "subgraphs in this network"
