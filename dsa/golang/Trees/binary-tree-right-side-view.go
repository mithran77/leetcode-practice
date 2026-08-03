/*

    199. Binary Tree Right Side View

    Given the root of a binary tree, imagine yourself
    standing on the right side of it, return the values
    of the nodes you can see ordered from top to bottom.

    Example 1:
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]

    Example 2:
    Input: root = [1,null,3]
    Output: [1,3]

    Example 3:
    Input: root = []
    Output: []

    Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rightSideView(root *TreeNode) []int {
    rightView := []int{}

    q := []*TreeNode{root}

    for len(q) > 0 {
        qLen := len(q)
        right := 0
        found := false

        for range qLen {
            node := q[0]
            q = q[1:]
            if node != nil {
                right = node.Val
                found = true
                q = append(q, node.Left)
                q = append(q, node.Right)
            }
        }

        if found {
            rightView = append(rightView, right)
        }

    }

    return rightView
}