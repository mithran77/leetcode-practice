import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        def traverse(root: TreeNode, level: int) -> str:
            if not root:
                return ''
            prefix = '  ' * level
            return f'{prefix}({root.val})\n' + traverse(root.left, level + 1) + traverse(root.right, level + 1)
        return str.rstrip(traverse(self, 0))


def build_complete_tree(arr: list[int], i: int, n: int) -> TreeNode | None:
    """
    >>> arr = [1, 2, 3]
    >>> build_complete_tree(arr, 0, len(arr))
    (1)
      (2)
      (3)
    """
    root = None
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = build_complete_tree(arr, 2 * i + 1, n)
        root.right = build_complete_tree(arr, 2 * i + 2, n)
    return root


def build_tree(arr: list[int]) -> TreeNode | None:
    """
    >>> arr = [1, 2, 3, None, 4, None, None, 5, 6, None, 7]
    >>> build_tree(arr)
    (1)
      (2)
        (4)
          (5)
            (7)
          (6)
      (3)
    """
    if len(arr) == 0:
        return None

    nodes = []

    val = arr.pop(0)
    root = TreeNode(val)
    nodes.append(root)

    while len(arr) > 0:
        curr = nodes.pop(0)

        left_val = arr.pop(0)
        if left_val is not None:
            curr.left = TreeNode(left_val)
            nodes.append(curr.left)

        if len(arr) > 0:
            right_val = arr.pop(0)
            if right_val is not None:
                curr.right = TreeNode(right_val)
                nodes.append(curr.right)

    return root

def printLevelOrder(root: TreeNode):

    # Base Case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    queue = []
    res = []

    # Enqueue Root and initialize height
    queue.append(root)

    while(len(queue) > 0):

        # Print front of queue and
        # remove it from queue
        # print(queue[0].val, end=" ")
        res.append(queue[0].val)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

    print(res)

def iterativeInOrderTraversal(root: TreeNode) -> list[int]:
    in_order = []
    st = collections.deque()
    st.append(root)

    while True:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            if not st:
                break
            node = st.pop()
            in_order.append(node.val)
            node = node.right

    return in_order

def iterativePreOrderTraversal(root: TreeNode) -> list[int]:
    pre_order = []
    st = collections.deque()
    st.append(root)

    while st:
        node = st.pop()
        if node is not None:
            pre_order.append(node.val)
            st.append(node.right)
            st.append(node.left)

    return pre_order

def iterativePostOrderTraversal(root: TreeNode | None) -> list[int]:
    post_order = []
    st1 = collections.deque()
    st2 = collections.deque()
    if root is None:
        return post_order

    st1.append(root)
    while st1:
        node = st1.pop()
        st2.append(node)
        if node.left is not None:
            st1.append(node.left)
        if node.right is not None:
            st1.append(node.right)

    while st2:
        post_order.append(st2.pop().val)

    return post_order

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    root = build_tree([1, 2, 7, 3, 4, None, None, None, None, 5, 6])
    print(iterativePreOrderTraversal(root))
