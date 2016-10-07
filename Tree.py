class Node:
    def __init__(self, value, value1):
        self.left = None
        self.data = value
        self.label = value1
        self.right = None
        self.dict = {}


class Tree:
    def createNode(self, data, label):
        return Node(data, label)

    def insert(self, node, data, label):
        if node is None:
            return self.createNode(data, label)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data, label)
        elif data > node.data:
            node.right = self.insert(node.right, data, label)
        return node

    def search(self, node, data):
        if node is None or node.data == data:
            return node
        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def deleteNode(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else:
            if node.left is None and node.right is None:
                del node
            if node.left is None:
                temp = node.right
                del node
                return temp
            elif node.right is None:
                temp = node.left
                del node
                return temp
        return node

    def traverse(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverse(root.left)
            print root.data, root.label, len(root.dict)
            self.traverse(root.right)


if __name__ == "__main__":
    root = None
    tree = Tree()
    root = tree.insert(root, 1, 2)
    print root.label
    print "Traverse Inorder"
    tree.traverse(root)
