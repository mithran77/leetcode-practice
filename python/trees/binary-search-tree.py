class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val) -> bool:
        new_node = Node(val)
        # Is empty
        if self.root is None:
            self.root = new_node
            return True

        tmp = self.root

        while True:
            # No duplicates
            if tmp.val == new_node.val:
                return False
            # Left
            if new_node.val < tmp.val:
                if tmp.left is None:
                    tmp.left = new_node
                    return True
                tmp = tmp.left
            # Right
            else:
                if tmp.right is None:
                    tmp.right = new_node
                    return True
                tmp = tmp.right

    def r_insert(self, val):
        if self.root is None:
            self.root = Node(val)
        self.__r_insert(self.root, val)

    def __r_insert(self, curr_node, val):
        if curr_node is None:
            curr_node = Node(val)
        if val < curr_node.val:
            curr_node.left = self.__r_insert(curr_node.left, val)
        if val > curr_node.val:
            curr_node.right = self.__r_insert(curr_node.right, val)
        return curr_node

    def contains(self, val) -> bool:
        tmp = self.root
        while tmp is not None:
            # Left
            if val < tmp.val:
                tmp = tmp.left
            # Right
            elif val > tmp.val:
                tmp = tmp.right
            # Match
            else:
                return True

        return False

    def min_value(self, current_node):
        while (current_node.left is not None):
            current_node = current_node.left
        return current_node.value

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    def __delete_node(self, current_node, value):
        # Not found
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        # Value Found
        else:
            # 4 Cases
            # Leaf
            if current_node.left is None and current_node.right is None:
                return None
            # Left None
            elif current_node.left is None:
                return current_node.right
            # Right None
            elif current_node.right is None:
                return current_node.left
            # Left and right exist
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

if __name__ == "__main__":
    t = BinarySearchTree()
    t.r_insert(47)
    t.r_insert(21)
    t.r_insert(76)
    t.r_insert(18)
    t.r_insert(27)
    t.r_insert(52)
    t.r_insert(82)
    print(t.contains(27))
    print(t.contains(20))


'''
RT

t.r_insert(47) Non Recursive

t.r_insert(21)
    __r_insert(Root(47), 21)
    __r_insert(None, 21)

t.r_insert(76)
    __r_insert(Root(47), 76)
    __r_insert(None, 76)

t.r_insert(18)
    __r_insert(Root(47), 18)
    __r_insert(Node(21), 18)
    __r_insert(None, 18)

t.r_insert(27)
    __r_insert(Root(47), 27)
    __r_insert(Node(21), 27)
    __r_insert(None, 27)

t.r_insert(52)
    __r_insert(Root(47), 52)
    __r_insert(Node(76), 52)
    __r_insert(None, 52)

t.r_insert(82)
    __r_insert(Node(47), 82)
    __r_insert(Node(76), 82)
    __r_insert(None, 82)

'''