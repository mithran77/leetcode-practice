/*

    110. Balanced Binary Tree

    Given a binary tree, determine if it is height-balanced.

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: true

    Example 2:
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

    Example 3:
    Input: root = []
    Output: true


    Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104

*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {
    balanced := true

    var rMaxDepth func(n *TreeNode) int 
    rMaxDepth = func(n *TreeNode) int {
        // BC
        if n == nil {
            return 0
        }
        // RC
        lh := rMaxDepth(n.Left)
        rh := rMaxDepth(n.Right)
        if abs(lh-rh) > 1 {
            balanced = false
        }

        return 1 + max(lh, rh)
    }
    rMaxDepth(root)
    return balanced
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}