class BinaryLifting:
    def __init__(self, n, log, root=0):
        self.n = n
        self.log = log
        self.up = [[-1 for _ in range(log)] for _ in range(n)]
        self.depth = [0 for _ in range(n)]
        self.root = root

    def add_edge(self, parent, child):
        self.up[child][0] = parent
        self.depth[child] = self.depth[parent] + 1
        for i in range(1, self.log):
            if self.up[child][i-1] != -1:
                self.up[child][i] = self.up[self.up[child][i-1]][i-1]

    def ancestor(self, node, k):
        if self.depth[node] < k:
            return -1
        for i in range(self.log):
            if k & (1 << i):
                node = self.up[node][i]
                if node == -1:
                    break
        return node

    def lca(self, a, b):
        if self.depth[a] < self.depth[b]:
            a, b = b, a
        a = self.ancestor(a, self.depth[a] - self.depth[b])
        if a == b:
            return a
        for i in reversed(range(self.log)):
            if self.up[a][i] != self.up[b][i]:
                a = self.up[a][i]
                b = self.up[b][i]
        return self.up[a][0]

# Usage
n = 10  # number of nodes in the tree
log = 2  # maximum depth of the tree, typically log2(n)
tree = BinaryLifting(n, log)

# Add edges according to the tree structure
# for example: tree.add_edge(parent, child)

# Find k-th ancestor
# kth_ancestor = tree.ancestor(node, k)

# Find LCA of two nodes
# lca = tree.lca(node1, node2)
