# leet-code

<details>
<summary><h4>Arrays & Hashing</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/contains-duplicate/" target="_blank">Contains Duplicate</a></b> <code>Add chars to HashSet while iterating. If already present, return True</code><br>
<a href="python/ArraysHashing/contains-duplicate.py">python</a> | 
<a href="golang/ArraysHashing/contains-duplicate.go">go</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/valid-anagram/" target="_blank">Valid Anagram</a></b> <code>If lengths of s and t are not same, return False. Use counter(HashMap) to track character frequencies by incrementing for characters in s and decrementing for those in t. if any counts are not zero, return False; otherwise, return True</code><br>
<a href="python/ArraysHashing/valid-anagram.py">python</a> |
<a href="golang/ArraysHashing/valid-anagram.go">go</a> 
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/two-sum/" target="_blank">Two Sum</a></b> <code>Store difference between the target and each number (target - num) in a HashMap with the current index as value. If the required value is already in the HashMap, return a list of indices of the pair that is found</code><br>
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
<li><b>🟥 <a href="https://leetcode.com/problems/minimum-window-substring/" target="_blank">Minimum Window Substring</a></b> <code>Use 2 HashMaps to track char counts in s and t, and initialize have to 0. Loop through s, updating window counts and incrementing have when (window[c] == count_t[c]). Loop while (have == len(count_t)), if current window is smaller than ans_len, update ans and ans_len. Slide l right, adjusting window[s[l]] & have if window count goes below count_t. Return ans</code><br>
<a href="python/SlidingWindow/minimum-window-substring.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/sliding-window-maximum/" target="_blank">Sliding Window Maximum</a></b> <code></code><br>
<a href="python/SlidingWindow/sliding-window-maximum.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Stack</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/valid-parentheses/" target="_blank">Valid Parentheses</a></b> <code>Use a HashMap {')': '('}. Iterate through the string: append open brackets to stack. For closing brackets, return False if the stack is empty or there's a mismatch with stack.pop(). At the end, return whether the stack is empty</code><br>
<a href="python/Stack/valid-parentheses.py">python</a> | 
<a href="golang/Stack/valid-parentheses.go">go</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/min-stack/" target="_blank">Min Stack</a></b> <code>Use 2 stacks: one for values and one to keep track of the minimum value so far (min_stack). During each insert, push the current minimum onto min_stack.</code><br>
<a href="python/Stack/min-stack.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/evaluate-reverse-polish-notation/" target="_blank">Evaluate Reverse Polish Notation</a></b> <code>Use a stack to store operands. When an operator is encountered, pop the last two operands, perform the operation in the correct order, and push the result back onto the stack. At the end, return the last value in the stack</code><br>
<a href="python/Stack/evaluate-reverse-polish-notation.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/generate-parentheses/" target="_blank">Generate Parentheses</a></b> <code>Use stack to store braces while generating valid combinations. Define dfs to recursively explore paths, skipping invalid paths based on counts of open & close brackets. Append stack content to the results when both counts equal n. If (o_cnt < n), add opening bracket, call dfs, then backtrack. If (c_cnt < o_cnt), add closing bracket, call dfs, then backtrack again. Return ans finally</code><br>
<a href="python/Stack/generate-parentheses.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/daily-temperatures/" target="_blank">Daily Temperatures</a></b> <code>Initialize ans array with 0's. Iterate through temperatures, while using a monotonically decreasing stack to store element index. While (temperature[i] > temperature[stack[top]]), pop from stack and update ans[stack_index] with difference between indices.</code><br>
<a href="python/Stack/daily-temperatures.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/car-fleet/" target="_blank">Car Fleet</a></b> <code>Sort (position, speed) pairs by position in ascending order. Iterate through pairs in reverse. For each car, calculate time to reach target; if this time <= the time at top of the stack, it joins the same fleet. Otherwise, add it to the stack. Finally, return the stack’s length as number of fleets</code><br>
<a href="python/Stack/car-fleet.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/largest-rectangle-in-histogram/" target="_blank">Largest Rectangle In Histogram</a></b> <code></code><br>
<a href="">python</a>
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
<li><b>🟧 <a href="https://leetcode.com/problems/search-a-2d-matrix/" target="_blank">Search a 2D Matrix</a></b> <code>Use binary search to find row, where the target may lie based on row boundaries. If the target isn’t within any of the row ranges, return False. Otherwise, set the row to the last calculated midpoint and perform a binary search within that row for the target</code><br>
<a href="python/BinarySearch/search-a-2d-matrix.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/koko-eating-bananas/" target="_blank">Koko Eating Bananas</a></b> <code>Use binary search between 1 and max(piles) to find the minimum eating speed. If a solution meets the hours constraint 
ℎ
h, try smaller speeds to minimize further. Return the last speed that satisfies the condition</code><br>
<a href="python/BinarySearch/koko-eating-bananas.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/" target="_blank">Find Minimum in Rotated Sorted Array</a></b> <code>Initialize l and r to the start and end. Update ans, as min(ans, nums[mid]). If nums[mid] > nums[r], move window right; otherwise, move window left. Return min(nums[l], ans)</code><br>
<a href="python/BinarySearch/find-minimum-in-rotated-sorted-array.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/" target="_blank">Search in Rotated Sorted Array</a></b> <code>Use 3 pointers l, r, mid. mid will be apart of either left sorted or right sorted portions. If target is in range of sorted portion then search it, otherwise search other half</code><br>
<a href="python/BinarySearch/search-in-rotated-sorted-array.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/time-based-key-value-store/" target="_blank">Time Based Key Value Store</a></b> <code></code><br>
<a href="">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/median-of-two-sorted-arrays/" target="_blank">Median of Two Sorted Arrays</a></b> <code></code><br>
<a href="">python</a>
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
<li><b>🟩 <a href="https://leetcode.com/problems/linked-list-cycle/" target="_blank">Linked List Cycle</a></b> <code>Initialize f & s pointers to head. Iterate while f and f.next exist, moving f by 2 and s by 1. If they are equal, return True; otherwise, return False</code><br>
<a href="python/LinkedList/linked-list-cycle.py">python</a> | 
<a href="golang/LinkedList/linked-list-cycle.go">go</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/reorder-list/" target="_blank">Reorder List</a></b> <code>Move the s pointer to the center of the list while ensuring f.next exists. Set s.next as the start of the second half, then set s.next to None to end the first half. Reverse the second list, then use 2 temp variables to merge both halves.</code><br>
<a href="python/LinkedList/reorder-list.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/" target="_blank">Remove Nth Node From End of List</a></b> <code>Create a dummy node pointing to head and assign it to l. Assign r to head and move r forward n times. Then, move both pointers until r reaches the end. Set l.next.next to l.next and return dummy.next</code><br>
<a href="python/LinkedList/remove-nth-node-from-end-of-list.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank">Merge k Sorted Lists</a></b> <code>Create mergeLists() to merge two lists. While len(lists) > 1, run an inner loop to merge two lists at a time, append the result to mergedLists, and assign mergedLists to lists. Finally, return lists[0]</code><br>
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
<li><b>🟧 <a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/" target="_blank">Lowest Common Ancestor of a Binary Search Tree</a></b> <code>While True: if root.val > p and q, move left. If root.val < p and q, move right. Otherwise, if root lies between p and q or equals p or q, return root</code><br>
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
<li><b>🟥 <a href="https://leetcode.com/problems/serialize-and-deserialize-binary-tree/" target="_blank">Serialize And Deserialize Binary Tree</a></b> <code>Use the same traversal for encoding and decoding. For encoding, if a node is None, add 'N' to res; otherwise, add str(node.val). For decoding, split the string by ','; if 'N', return None, otherwise return TreeNode(val) while incrementing self.i. Finally, return the root.</code><br>
<a href="python/Trees/serialize-and-deserialize-binary-tree.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Heap / Priority Queue</h4></summary>
</details>

<details>
<summary><h4>Backtracking</h4></summary>
<ul>
<li><b>🟧 <a href="https://leetcode.com/problems/combination-sum/" target="_blank">Combination Sum</a></b> <code>Define dfs(i, cur, total). Base cases: if target == total, append cur.copy() to res and return. If idx >= len(nums) or total > target, return. Append nums[i] to cur, add to total, then call dfs(). After, pop() from cur, subtract nums[i] from total, increment i, and call dfs() again. Finally, return res</code><br>
<a href="python/Backtracking/combination-sum/combination-sum.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/word-search/" target="_blank">Word Search</a></b> <code>Define dfs(r, c, i). If i == len(word), return True. If r or c are out of bounds, characters don't match, or the cell is already in the path, return False. If the current cell matches word[i], add it to the path, and recursively check neighboring cells recording result. backtrack by removing the cell from the path and return result</code><br>
<a href="python/Backtracking/word-search.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Tries</h4></summary>
</details>

<details>
<summary><h4>Graphs</h4></summary>
<ul>
<li><b>🟧 <a href="https://leetcode.com/problems/number-of-islands/" target="_blank">Number of Islands</a></b> <code>Define dfs(r, c) with BC: return if r or c are out of bounds, if grid[r][c] is not "1", or if (r, c) is in the visited set. If conditions are met, add (r, c) to visited and perform dfs on its four neighbors. Use a nested loop for r and c, and if grid[r][c] is "1" and not in visited, increment the islands and call dfs(r, c)</code><br>
<a href="python/Graphs/number-of-islands.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/clone-graph/" target="_blank">Clone Graph</a></b> <code>Create a HashMap to track visited nodes. Define dfs(node) with a BC: if node is already visited, return its corresponding value from the HashMap. Otherwise, create a copy with node.val & map it in the HashMap. Then iterate through node's neighbors, appending the result of dfs(neighbor) to copy's neighbors. Finally, return the copy</code><br>
<a href="python/Graphs/clone-graph.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/pacific-atlantic-water-flow/" target="_blank">Pacific Atlantic Water Flow</a></b> <code>Define dfs(r, c, pre_height) with BC: return if current cell (r, c) is out of bounds, has (height < pre_height), or already in visited. Use 2 HashSets to track cells reachable from the pac and atl oceans. Loop through cols to add nodes reachable from the first and last row to the Pacific and Atlantic sets. Similarly, loop through rows to add nodes reachable from the first and last column. Finally, loop through the grid(r & c) and add cells that reach both oceans to the result, and return it.</code><br>
<a href="python/Graphs/pacific-atlantic-water-flow.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/course-schedule/" target="_blank">Course Schedule</a></b> <code>Create adjacency list for directed graph. Define dfs(c) with BCs: if course already visited, return False; if course has no dependencies, return True. For each course, Add it to visited, check its dependencies with dfs(). If any dfs() call fails, return False. After processing, remove course from visited, empty adj[c] and return True. If dfs() fails for any course, return False; otherwise, return True.</code><br>
<a href="python/Graphs/course-schedule.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/graph-valid-tree/" target="_blank">Graph Valid Tree</a></b> <code>Create an adjacency list for each node using a HashMap (undirected graph). Use a set to track visited nodes. Define dfs(i, prev) with BC: if node already visited, return False. For each node, iterate through its neighbors, skipping previous node. If any check fails, return False, otherwise finally True. Return dfs(0, -1) and (len(visited) == n)</code><br>
<a href="python/Graphs/graph-valid-tree.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/" target="_blank">Number of Connected Components In An Undirected Graph</a></b> <code>Use Union-Find with parent and rank arrays. Define findRootParent(v) to get the absolute root parent of a node. Define union(v1, v2) to merge two nodes by their root parents. If they share the same parent, return 0; otherwise, merge them and return 1. Initialize res to the number of nodes, and for each edge, decrement res by the result of union(e1, e2)</code><br>
<a href="python/Graphs/number-of-connected-components-in-an-undirected-graph.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/minimize-malware-spread/" target="_blank">Minimize Malware Spread</a></b> <code>https://github.com/doocs/leetcode/blob/main/solution/0900-0999/0924.Minimize%20Malware%20Spread/README_EN.md</code><br>
<a href="python/Graphs/minimize-malware-spread.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Advanced Graphs</h4></summary>
</details>

<details>
<summary><h4>1-D Dynamic Programming</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/climbing-stairs/" target="_blank">Climbing Stairs</a></b> <code>Use bottom-up DP. Initialize f and s to 1. Iterate (n - 1) times, updating f as- sum of f + s and setting s to old value of f. Finally return f</code><br>
<a href="python/DynamicProgramming1D/climbing-stairs.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/house-robber/" target="_blank">House Robber</a></b> <code>Use 2 pointers f and s initialized to 0. Loop through nums, calculate take as (n + s) and not_take as f. Update s to current f and f to the max(take, not_take). Finally, return f</code><br>
<a href="python/DynamicProgramming1D/house-robber/house-robber.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/house-robber-ii/" target="_blank">House Robber II</a></b> <code>Define function rob1(). If nums size is 1, return nums[0]. Otherwise, return maximum of rob1(nums[1:]) and rob1(nums[:len(nums)-1])</code><br>
<a href="python/DynamicProgramming1D/house-robber-ii.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-palindromic-substring/" target="_blank">Longest Palindromic Substring</a></b> <code>Initialize res as "" and res_len as 0. Loop through the string, checking for odd-length (l, r = i, i) and even-length (l, r = i, i+1) palindromes. Update res and res_len whenever a longer palindrome is found. Finally, return res</code><br>
<a href="python/DynamicProgramming1D/longest-palindromic-substring.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/palindromic-substrings/" target="_blank">Palindromic Substrings</a></b> <code>Initialize count to 0. Loop through the string, checking for odd-length (l, r = i, i) and even-length (l, r = i, i+1) palindromes using expand-from-center algorithm. Increment count for each palindrome found, and return total count at the end</code><br>
<a href="python/DynamicProgramming1D/palindromic-substrings.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/decode-ways/" target="_blank">Decode Ways</a></b> <code>BCs: If s is '' or starts with '0', return 0. If s length is 1, return 1. Initialize upto_prev and upto_cur to 1. Loop from 1 to len(s). Convert s[i] and (s[i-1] + s[i]) to 0-based integers. If cur > 0, add upto_cur to val. If prev forms a number between 10 and 26, add upto_prev to val. Update upto_prev to upto_cur and upto_cur to val. Finally, return upto_cur</code><br>
<a href="python/DynamicProgramming1D/decode-ways.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/coin-change/" target="_blank">Coin Change</a></b> <code>Use tabulation to create a DP array of size amount + 1, initialized to amount + 1. For each amount from 1 to amount, loop through each coin and update dp[a] to the minimum of dp[a] and 1 + dp[a - c]. Return dp[amount] if it's updated, otherwise return -1.</code><br>
<a href="python/DynamicProgramming1D/coin-change.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/maximum-product-subarray/" target="_blank">Maximum Product Subarray</a></b> <code>Initialize cur_max and cur_min to 1 & res to nums[0]. Loop through nums, updating cur_max as the maximum and cur_min as the minimum of (n * cur_max, n * cur_min, n) for each n. Update res as the maximum of res and cur_max. Return res</code><br>
<a href="python/DynamicProgramming1D/maximum-product-subarray.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/word-break/" target="_blank">Word Break</a></b> <code>Initialize DP array with False and set the last element to True. Loop through the string in reverse, checking each substring against the list of words. If a match is found, update the DP array at the current index to dp[i + len(w)] and break the inner loop. Finally, return the value of dp[0]</code><br>
<a href="python/DynamicProgramming1D/word-break.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-increasing-subsequence/" target="_blank">Longest Increasing Subsequence</a></b> <code>Declare a dp array initialized to 1 for each element in nums. Loop through nums in reverse, for each element, loop again from i + 1 to len(nums). If nums[i] < nums[j], update dp[i] to max(dp[i], 1 + dp[j]). Finally, return the maximum value in dp</code><br>
<a href="python/DynamicProgramming1D/longest-increasing-subsequence.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>2-D Dynamic Programming</h4></summary>
</details>

<details>
<summary><h4>Greedy</h4></summary>
</details>

<details>
<summary><h4>Intervals</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/meeting-rooms/" target="_blank">Meeting Rooms</a></b> <code></code><br>
<a href="python/Intervals/meeting-rooms.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/meeting-rooms-ii/" target="_blank">Meeting Rooms II</a></b> <code></code><br>
<a href="python/Intervals/meeting-rooms-ii.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/insert-interval/" target="_blank">Insert Interval</a></b> <code></code><br>
<a href="python/Intervals/insert-interval.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/merge-intervals/" target="_blank">Merge Intervals</a></b> <code></code><br>
<a href="python/Intervals/merge-intervals.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/non-overlapping-intervals/" target="_blank">Non Overlapping Intervals</a></b> <code></code><br>
<a href="python/Intervals/non-overlapping-intervals.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/minimum-interval-to-include-each-query/" target="_blank">Minimum Interval to Include Each Query</a></b> <code></code><br>
<a href="">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/number-of-flowers-in-full-bloom/" target="_blank">Number of Flowers in Full Bloom</a></b> <code>Create arrays with (people, idx), start and end times. Heapify the start and end arrays. Loop through a sorted array of people, increment the count while start_time <= p, and decrement it when end_time < p. Assign count to res[i], then return the final res</code><br>
<a href="python/Intervals/number-of-flowers-in-full-bloom.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Math & Geometry</h4></summary>
</details>

<details>
<summary><h4>Bit Manipulation</h4></summary>
</details>


<h4>Profile: <a href="https://leetcode.com/u/mithran77/">mithran77</a></h4>