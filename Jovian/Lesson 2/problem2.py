# implement a binary tree using python and show its usage
# with some example

class TreeNode:
    def __init__(self,key) -> None:
        self.key = key
        self.left = None
        self.right = None
    # @staticmethod
    def parse_tuple(data):
        print(data)
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)

        return node
    
data = ((1,3,None), 2,((None, 3,4),(6,7,8)))
print(TreeNode.parse_tuple(data))

# chatgpt version
# class TreeNode:
#     def __init__(self, key) -> None:
#         self.key = key
#         self.left = None
#         self.right = None

#     @staticmethod
#     def parse_tuple(data):
#         if isinstance(data, tuple) and len(data) == 3:
#             node = TreeNode(data[1])
#             node.left = TreeNode.parse_tuple(data[0])  # Corrected reference to the static method
#             node.right = TreeNode.parse_tuple(data[2])  # Corrected reference to the static method
#         elif data is None:
#             node = None
#         else:
#             node = TreeNode(data)

#         return node

# data = ((1, 3, None), 2, ((None, 3, 4), (6, 7, 8)))
# root = TreeNode.parse_tuple(data)


