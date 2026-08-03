/*

    1448. Count Good Nodes in Binary Tree

    Given a binary tree root, a node X in the tree is named
    good if in the path from root to X there are no nodes
    with a value greater than X.

    Return the number of good nodes in the binary tree.

    Example 1:
    Input: root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Nodes in blue are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path
    starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path
    Node 3 -> (3,1,3) is the maximum value in the path.

    Example 2:
    Input: root = [3,3,null,4,2]
    Output: 3
    Explanation: Node 2 -> (3, 3, 2) is not good, because
    "3" is higher than it.

    Example 3:
    Input: root = [1]
    Output: 1
    Explanation: Root is considered as good.

    Constraints:

    The number of nodes in the binary tree is in the
    range [1, 10^5].
    Each node's value is between [-10^4, 10^4].

*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func goodNodes(root *TreeNode) int {
    
    var rGoodNodes func(node *TreeNode, cMax int) int
    rGoodNodes = func(node *TreeNode, cMax int) int {
        if node == nil {
            return 0
        }
        isGood := 0
        if node.Val >= cMax {
            isGood = 1
            cMax = node.Val
        }

        return (isGood +
            rGoodNodes(node.Left, cMax) +
            rGoodNodes(node.Right, cMax))
    }

    return rGoodNodes(root, root.Val)
}
