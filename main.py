
class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.node_height = 1
class AVL:
    def __init__(self, root=None):
        self.root = root

    def search(self, k):
        if self.root is None:
            return None
        else:
            if self.root.key == k:
                return self.root.value
            else:
                return self.__recursive_search(k, self.root)

    def __recursive_search(self, k, node):
        if node is None:
            return None
        else:
            if node.key == k:
                return node.value
            if node.key > k:
                return self.__recursive_search(k, node.left)
            elif node.key < k:
                return self.__recursive_search(k, node.right)

    def balance(self, node):
        if node is None:
            return 0
        else:
            return self.height_for_rotation(node.right) - self.height_for_rotation(node.left)

    def rotate_left(self, node):
        if node is None or node.right is None:
            return node

        y = node.right
        node_subtree = y.left

        y.left = node
        node.right = node_subtree

        # node.node_height = self.__recursive_height(node)
        # y.node_height = self.__recursive_height(node)
        node.node_height = max(self.height_for_rotation(node.left), self.height_for_rotation(node.right)) + 1
        y.node_height = max(self.height_for_rotation(y.left), self.height_for_rotation(y.right)) + 1
        return y
    def rotate_right(self, node):
        if node is None or node.left is None:
            return node

        x = node.left
        node_subtree = x.right

        x.right = node
        node.left = node_subtree


        node.node_height = max(self.height_for_rotation(node.left), self.height_for_rotation(node.right)) +1

        x.node_height = max(self.height_for_rotation(x.left), self.height_for_rotation(x.right)) + 1

        return x




    def insert(self, k, v):
        if self.root is None:
            self.root = Node(k, v)
        else:
            self.root = self.__recursive_insert(k, v, self.root)

    def __recursive_insert(self, k, v, node):

        if node is None:
            return Node(k, v)
        if k < node.key:
            node.left = self.__recursive_insert(k, v, node.left)
        elif k > node.key:
            node.right = self.__recursive_insert(k, v, node.right)
        else:
            node.value = v


        node.node_height = max(self.height_for_rotation(node.left), self.height_for_rotation(node.right)) + 1
        balance = self.balance(node)
        if balance == -2:
            if self.balance(node.left) <= 0:
                return self.rotate_right(node)
            if self.balance(node.left) > 0:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        if balance == 2:
            if self.balance(node.right) >= 0:
                return self.rotate_left(node)
            if self.balance(node.right) < 0:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        return node


    def delete(self,  k):
        if self.root is None:
            return None
        else:
            self.root = self.__recursive_delete(k, self.root)
    def __recursive_delete(self, k, node):
        if node is None:
            return None

        if node.key > k:
            node.left = self.__recursive_delete(k, node.left)
        elif node.key < k:
            node.right = self.__recursive_delete(k, node.right)
        else:
            if node.left is None and node.right is None:
                node = None
                return node
            elif node.left is None or node.right is None:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
            elif node.left is not None and node.right is not None:
                parent = node
                right_child = node.right
                while right_child.left is not None:
                    parent = right_child
                    right_child = right_child.left
                node.key = right_child.key
                node.value = right_child.value
                if parent.left == right_child:
                    parent.left = right_child.right
                else:
                    parent.right = right_child.right

        node.node_height = max(self.height_for_rotation(node.left), self.height_for_rotation(node.right)) + 1
        balance = self.balance(node)
        if balance == -2:
            if self.balance(node.left) <= 0:
                return self.rotate_right(node)
            if self.balance(node.left) > 0:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        if balance == 2:
            if self.balance(node.right) >= 0:
                return self.rotate_left(node)
            if self.balance(node.right) < 0:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        return node


    def print(self):
        self.__recursive_print(self.root)
        print()
    def __recursive_print(self, node):
        if node is not None:
            self.__recursive_print(node.left)
            print(f"{node.key}:{node.value}", end=',' )
            self.__recursive_print(node.right)

    def height(self):
        if self.root is None:
            return -1
        else:
            return self.__recursive_height(self.root)
    def __recursive_height(self, node):
        if node is None:
            return -1
        h_left = self.__recursive_height(node.left)

        h_right = self.__recursive_height(node.right)

        return max(h_left+1, h_right+1)

    def height_for_rotation(self, node):
        if node is None:
            return 0
        else:
            return node.node_height
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")
    def __print_tree(self, node, lvl):
        if node is not None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)

            self.__print_tree(node.left, lvl+5)

if __name__ == '__main__':
    drzewo = AVL()
    d = {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}
    for k, v in d.items():
        drzewo.insert(k, v)
    drzewo.print_tree()
    drzewo.print() #w formie klucz:wartość
    print(drzewo.search(10))
    drzewo.delete(50)
    drzewo.delete(52)
    drzewo.delete(11)
    drzewo.delete(57)
    drzewo.delete(1)
    drzewo.delete(12)
    drzewo.insert(3, 'AA')
    drzewo.insert(4, 'BB')
    drzewo.delete(7)
    drzewo.delete(8)
    drzewo.print_tree()
    drzewo.print()