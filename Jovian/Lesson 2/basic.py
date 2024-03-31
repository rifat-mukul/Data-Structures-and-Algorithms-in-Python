class TreeNode:
    def __init__(self,key) -> None:
        self.key = key
        self.left = None
        self.right = None

node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)
# print(type(node0))
# print(node0)
node0.left = node1
node0.right = node2
print(node0.left.key if node0.left else None) #left key
print(node0.right.key if node0.right else None) #right key