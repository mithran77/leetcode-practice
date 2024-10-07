# leet-code

<details>
<summary><h4>Arrays & Hashing</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/contains-duplicate/" target="_blank">Contains Duplicate</a></b> <code>Add chars to HashSet while iterating. If already present, return True</code><br>
<a href="python/ArraysHashing/contains-duplicate.py">python</a> | 
<a href="golang/ArraysHashing/contains-duplicate.go">go</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/valid-anagram/" target="_blank">Valid Anagram</a></b> <code>Create char_count HashMap for s, then subtract counts from HashMap while looping through t</code><br>
<a href="python/ArraysHashing/valid-anagram.py">python</a> |
<a href="golang/ArraysHashing/valid-anagram.go">go</a> 
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/two-sum/" target="_blank">Two Sum</a></b> <code>Use HashMap to store required number with index of computed number, If required value is found, return a list of correspomding indexes</code><br>
<a href="python/ArraysHashing/two-sum.py">python</a> |
<a href="golang/ArraysHashing/two-sum.go">go</a> 
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/group-anagrams/" target="_blank">Group Anagrams</a></b> <code>Use a HashMap with char_count[26] tuples as keys, appending words that match the count. Finally, return the HashMap's values.</code><br>
<a href="python/ArraysHashing/group-anagrams.py">python</a> |
<a href="golang/ArraysHashing/group-anagrams.go">go</a> 
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/top-k-frequent-elements/" target="_blank">Top K Frequent Elements</a></b> <code>First create a num_count HashMap, from which create an ordered map of counts with corresponding numbers (List[List]). Iterate in reverse, appending numbers to the result, and return when enough values are collected.</code><br>
<a href="python/ArraysHashing/top-k-frequent-elements.py">python</a> |
<a href="golang/ArraysHashing/top-k-frequent-elements.go">go</a> 
</li>
<li><b>🟧 <a href="https://neetcode.io/problems/string-encode-and-decode" target="_blank">Encode and Decode Strings</a></b> <code>Use the format < len#word > for encoding. To decode, use two pointers and two while loops to read the length, then append the word slice to the result</code><br>
<a href="python/ArraysHashing/encode-and-decode-strings.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/product-of-array-except-self/" target="_blank">Product of Array Except Self</a></b> <code>Initialize prod = 1. Loop L-R. First update ans array, ans[i] *= prod. Then update prod, prod *= nums[i], to use in the next iteration. Repeat the process R-L.</code><br>
<a href="python/ArraysHashing/product-of-array-except-self.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-consecutive-sequence/" target="_blank">Longest Consecutive Sequence</a></b> <code>Convert nums to a set. For each number, check if num-1 is present (indicating the start of a sequence). If yes, iteratively check until there are no more num+1 elements in the set. Then update the longest sequence length.</code><br>
<a href="python/ArraysHashing/longest-consecutive-sequence.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Two Pointers</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/valid-palindrome/" target="_blank">Valid Palindrome</a></b> <code>Iterate with L & R pointers, skip invalid characters with ASCII range checks, compare in lowercase, finally return True if no mismatches found</code><br>
<a href="python/TwoPointer/valid-palindrome.py">python</a> | 
<a href="golang/TwoPointer/valid-palindrome.go">go</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/container-with-most-water/" target="_blank">Container With Most Water</a></b> <code>Iterate with L & R pointers, calculate the current area and update max_area if larger, then move pointer with the lower height</code><br>
<a href="python/TwoPointer/container-with-most-water.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/" target="_blank">Two Sum II</a></b> <code>Iterate with L & R pointers, adjust pointers based on cur_sum relative to target, and return indices if they match</code><br>
<a href="python/TwoPointer/two-sum-ii-input-array-is-sorted.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/3sum/" target="_blank">3Sum</a></b> <code>Sort the array and iterate through nums, skipping duplicates. For each nums[i], set target = -nums[i] and iterate using L & R pointers to find pairs that sum to the target. Add indices on a match, and skip duplicates for L followed by R pointers</code><br>
<a href="python/TwoPointer/3sum.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Sliding Window</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/" target="_blank">Best Time to Buy and Sell Stock</a></b> <code>Set buy to prices[0], iterate through prices calculating profit, and update if larger</code><br>
<a href="python/SlidingWindow/best-time-to-buy-and-sell-stock.py">python</a> | 
<a href="golang/SlidingWindow/best-time-to-buy-and-sell-stock.go">go</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/" target="_blank">Longest Substring Without Repeating Characters</a></b> <code>Initialize L pointer to 0. Iterate over s, adding characters to a charSet. If duplicate is found, remove characters from left until duplicate is gone. Continuously update longest substring and return it at end</code><br>
<a href="python/SlidingWindow/longest-substring-without-repeating-characters.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-repeating-character-replacement/" target="_blank">Longest Repeating Character Replacement</a></b> <code>Set L = 0 and iterate R through s, tracking the max frequency of any character by comparing against the current character count. Adjust L & char frequencies in window while the count of other characters exceeds k using maxf. Continuously update longest substring with repetitions and return it at end</code><br>
<a href="python/SlidingWindow/longest-repeating-character-replacement.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/minimum-window-substring/" target="_blank">Minimum Window Substring</a></b> <code></code><br>
<a href="#">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Stack</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/valid-parentheses/" target="_blank">Valid Parentheses</a></b> <code>Use a HashMap {')': '('}. Iterate through the string: append open brackets (not in the HashMap) to a stack. For closing brackets, return False if the stack is empty or there's a mismatch. Pop from the stack and continue. At the end, return whether the stack is empty</code><br>
<a href="python/Stack/valid-parentheses.py">python</a> | 
<a href="golang/Stack/valid-parentheses.go">go</a>
</li>
</ul>
</details>

<details>
<summary><h4>Binary Search</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/binary-search/" target="_blank">Binary Search</a></b> <code>Use 3 pointers: l, r & mid. Compare the mid value with the target and either move the window left/right or return the index if found.</code><br>
<a href="python/BinarySearch/binary-search.py">python</a> | 
<a href="golang/BinarySearch/binary-search.go">go</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/" target="_blank">Find Minimum in Rotated Sorted Array</a></b> <code>Initialize l and r to the start and end. If nums[mid] > nums[r], move window right; otherwise, move window left, including mid. l and r will converge on smallest value, which you return at end</code><br>
<a href="python/BinarySearch/find-minimum-in-rotated-sorted-array.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/" target="_blank">Search in Rotated Sorted Array</a></b> <code>At most two sorted halfs, mid will be apart of left sorted or right sorted, if target is in range of sorted portion then search it, otherwise search other half</code><br>
<a href="python/BinarySearch/search-in-rotated-sorted-array.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Linked List</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank">Reverse Linked List</a></b> <code>Initialize prev, cur = None, head. Iterate through the list, updating prev and cur. At the end, return prev as the new head</code><br>
<a href="python/LinkedList/reverse-linked-list.py">python</a> | 
<a href="golang/LinkedList/reverse-linked-list.go">go</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/merge-two-sorted-lists/" target="_blank">Merge Two Sorted Lists</a></b> <code>Create an empty node cur with a pointer res. Iterate while both list1 and list2 are not None, adding the node with the lower value to cur. Then if either list is None, append the other list. Finally, return res.next</code><br>
<a href="python/LinkedList/merge-two-sorted-lists.py">python</a> | 
<a href="golang/LinkedList/merge-two-sorted-lists.go">go</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/linked-list-cycle/" target="_blank">Linked List Cycle</a></b> <code>Initialize F & S pointers to head. Iterate while F and F.next exist, moving F by 2 and S by 1. If they are equal, return True; otherwise, return False</code><br>
<a href="python/LinkedList/linked-list-cycle.py">python</a> | 
<a href="golang/LinkedList/linked-list-cycle.go">go</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/reorder-list/" target="_blank">Reorder List</a></b> <code>Move the s pointer to the center of the list while ensuring f.next exists. Set s.next as the start of the second half, then set s.next to None to end the first half. Reverse the second list, then use two temp variables to merge both halves.</code><br>
<a href="python/LinkedList/reorder-list.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/" target="_blank">Remove Nth Node From End of List</a></b> <code>Create a dummy node pointing to head and assign it to s. Assign f to head and move f forward n times. Then, move both pointers until f reaches the end. Set s.next.next to s.next and return head</code><br>
<a href="python/LinkedList/remove-nth-node-from-end-of-list.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank">Merge k Sorted Lists</a></b> <code></code><br>
<a href="python/LinkedList/merge-k-sorted-lists.py">python</a>
</ul>
</details>

<details>
<summary><h4>Trees</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/invert-binary-tree/" target="_blank">Invert Binary Tree</a></b> <code>Traverse via dfs(). If node exists, replace left and right. Call dfs(left), then dfs(right)</code><br>
<a href="python/Trees/invert-binary-tree.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/" target="_blank">Maximum Depth of Binary Tree</a></b> <code>Use recursive DFS with a leaf case returning 0. At each step, return 1 + the max height of the left and right subtrees</code><br>
<a href="python/Trees/maximum-depth-of-binary-tree.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/same-tree/" target="_blank">Same Tree</a></b> <code>For base cases, return True if both nodes are None. If either is None or values don’t match, return False. In the recursive case, return fn(left) and fn(right)</code><br>
<a href="python/Trees/same-tree.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/subtree-of-another-tree/" target="_blank">Subtree of Another Tree</a></b> <code>Create a separate fn isSameTree() and perform BFS on the root. At each node, if isSameTree(node, subTree) return True. Finally if no same trees were found, return False</code><br>
<a href="python/Trees/subtree-of-another-tree.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/" target="_blank">Lowest Common Ancestor of a Binary Search Tree</a></b> <code>If node.val > p & q, move to node.left. if node.val < p & q, move right.</code><br>
<a href="python/Trees/lowest-common-ancestor.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/binary-tree-level-order-traversal/" target="_blank">Binary Tree Level Order Traversal</a></b> <code>Add root to a Q. While the Q is not empty, initialize a level array. Run an inner loop for len(Q), adding node.val to level and left & right children back to the Q. If level is not empty, add it to res. Finally, return res</code><br>
<a href="python/Trees/binary-tree-level-order-traversal.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/validate-binary-search-tree/" target="_blank">Validate Binary Search Tree</a></b> <code>Define valid() with node, left, and right values. If node is None, return True. If node.val is not between left and right, return False. Recursively return valid(node.left, left, node.val) and valid(node.right, node.val, right)</code><br>
<a href="python/Trees/validate-binary-search-tree.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/kth-smallest-element-in-a-bst/" target="_blank">Kth Smallest Element in a BST</a></b> <code>Use a single pointer and a stack. Iterate while stack or pointer are not empty. Push cur.left to the stack, until cur.left is None. Pop from the stack, decrement k, and check if k == 0 to return the node's value. Otherwise, set cur to cur.right and continue</code><br>
<a href="python/Trees/kth-smallest-element-in-a-bst.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/" target="_blank">Construct Binary Tree from Preorder and Inorder Traversal</a></b> <code>If either traversal is empty, return None. The 1st element in preorder is the root. Use inorder to find the root's index (mid). In inorder, elements left of mid are the left subtree, and elements right of mid are the right subtree. Recursively build subtrees.</code><br>
<a href="python/Trees/construct-binary-tree-from-preorder-and-inorder-traversal.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/serialize-and-deserialize-binary-tree/" target="_blank">Serialize And Deserialize Binary Tree</a></b> <code>Use the same traversal for encoding and decoding. For encoding, if a node is None, add 'N' to res; otherwise, add str(node.val). For decoding, split the string by ','; if 'N', return None, otherwise return TreeNode(val) while incrementing i. Finally, return the root.</code><br>
<a href="python/Trees/serialize-and-deserialize-binary-tree.py">python</a>
</ul>
</details>

<details>
<summary><h4>Heap / Priority Queue</h4></summary>
</details>

<details>
<summary><h4>Backtracking</h4></summary>
</details>

<details>
<summary><h4>Tries</h4></summary>
</details>

<details>
<summary><h4>Graphs</h4></summary>
</details>

<details>
<summary><h4>Advanced Graphs</h4></summary>
</details>

<details>
<summary><h4>1-D Dynamic Programming</h4></summary>
</details>

<details>
<summary><h4>2-D Dynamic Programming</h4></summary>
</details>

<details>
<summary><h4>Greedy</h4></summary>
</details>

<details>
<summary><h4>Intervals</h4></summary>
</details>

<details>
<summary><h4>Math & Geometry</h4></summary>
</details>

<details>
<summary><h4>Bit Manipulation</h4></summary>
</details>



<h4>Profile: <a href="https://leetcode.com/u/mithran77/">mithran77</a></h4>