/*

    572. Subtree of Another Tree

    Given the roots of two binary trees root and subRoot, return true if there
    is a subtree of root with the same structure and node values of subRoot and
    false otherwise.

    A subtree of a binary tree tree is a tree that consists of a node in tree
    and all of this node's descendants. The tree tree could also be considered
    as a subtree of itself.

    Example 1:
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

    Example 2:
    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false

    Constraints:

    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -104 <= root.val <= 104
    -104 <= subRoot.val <= 104

*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
    if subRoot == nil {
        return true
    }
    var dfs func(r *TreeNode, sr *TreeNode) bool
    dfs = func(r *TreeNode, sr *TreeNode) bool {
        if r == nil {
            return false
        } 
        if isSameTree(r, sr) {
            return true
        }

        return dfs(r.Left, sr) ||
            dfs(r.Right, sr)
    }
    return dfs(root, subRoot)
}

func isSameTree(t1 *TreeNode, t2 *TreeNode) bool {
    if t1 == nil && t2 == nil {
        return true
    }
    if t1 == nil || t2 == nil {
        return false
    }
    if t1.Val != t2.Val {
        return false
    }
    return isSameTree(t1.Left, t2.Left) &&
        isSameTree(t1.Right, t2.Right)
}

