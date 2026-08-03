/*
    102. Binary Tree Level Order Traversal

    Given the root of a binary tree, return the level
    order traversal of its nodes' values. (i.e., from
    left to right, level by level).


    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Example 2:
    Input: root = [1]
    Output: [[1]]

    Example 3:
    Input: root = []
    Output: []
    

    Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func levelOrder(root *TreeNode) [][]int {
    var traversal [][]int
    q := []*TreeNode{root}
    
    for len(q) > 0 {
        qLen := len(q)
        level := []int{}

        for range qLen {
            node := q[0]
            q = q[1:]

            if node != nil {
                level = append(level, node.Val)
                q = append(q, node.Left)
                q = append(q, node.Right)
            }
        }

        if len(level) > 0 {
            traversal = append(traversal, level)
        }

    }
    return traversal
}
