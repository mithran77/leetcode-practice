# DSA

<details>
<summary><h4>Arrays & Hashing</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/contains-duplicate/" target="_blank">Contains Duplicate</a></b> <code>Add chars to HashSet while iterating. If already present, return True</code><br>
<a href="dsa/python/ArraysAndHashing/contains-duplicate.py">python</a> | 
<a href="golang/ArraysAndHashing/contains-duplicate.go">go</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/valid-anagram/" target="_blank">Valid Anagram</a></b> <code>If lengths of s and t are not same, return False. Use counter(HashMap) to track character frequencies by incrementing for characters in s and decrementing for those in t. if any counts are not zero, return False; otherwise, return True</code><br>
<a href="dsa/python/ArraysAndHashing/valid-anagram.py">python</a> |
<a href="golang/ArraysAndHashing/valid-anagram.go">go</a> 
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/two-sum/" target="_blank">Two Sum</a></b> <code>Store difference between the target and each number (target - num) in a HashMap with the current index as value. If the required value is already in the HashMap, return a list of indices of the pair that is found</code><br>
<a href="dsa/python/ArraysAndHashing/two-sum.py">python</a> |
<a href="golang/ArraysAndHashing/two-sum.go">go</a> 
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/group-anagrams/" target="_blank">Group Anagrams</a></b> <code>Use a HashMap with char_count[26] tuples as keys, appending words that match the count. Finally, return the HashMap's values.</code><br>
<a href="dsa/python/ArraysAndHashing/group-anagrams.py">python</a> |
<a href="golang/ArraysAndHashing/group-anagrams.go">go</a> 
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/top-k-frequent-elements/" target="_blank">Top K Frequent Elements</a></b> <code>First create a num_count HashMap, from which create an ordered map of counts with corresponding numbers (List[List]). Iterate in reverse, appending numbers to the result, and return when enough values are collected.</code><br>
<a href="dsa/python/ArraysAndHashing/top-k-frequent-elements.py">python</a> |
<a href="golang/ArraysAndHashing/top-k-frequent-elements.go">go</a> 
</li>
<li><b>🟧 <a href="https://neetcode.io/problems/string-encode-and-decode" target="_blank">Encode and Decode Strings</a></b> <code>Use the format < len#word > for encoding. To decode, use two pointers and two while loops to read the length, then append the word slice to the result</code><br>
<a href="dsa/python/ArraysAndHashing/encode-and-decode-strings.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/product-of-array-except-self/" target="_blank">Product of Array Except Self</a></b> <code>Initialize prod = 1. Loop L-R. First update ans array, ans[i] *= prod. Then update prod, prod *= nums[i], to use in the next iteration. Repeat the process R-L.</code><br>
<a href="dsa/python/ArraysAndHashing/product-of-array-except-self.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/valid-sudoku/" target="_blank">Valid Sudoku</a></b> <code>Create 3 HashMaps of hash sets for- rows, cols & squares. For squares, use tuple (i // 3, j // 3) as the key. If duplicate in any of the 3 hashsets return False, otherwise add to all 3 maps. Return True at the end</code><br>
<a href="dsa/python/ArraysAndHashing/valid-sudoku.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-consecutive-sequence/" target="_blank">Longest Consecutive Sequence</a></b> <code>Convert nums to a set. For each number, check if num-1 is present (indicating the start of a sequence). If yes, iteratively check until there are no more num+1 elements in the set. Then update the longest sequence length.</code><br>
<a href="dsa/python/ArraysAndHashing/longest-consecutive-sequence.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Two Pointers</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/valid-palindrome/" target="_blank">Valid Palindrome</a></b> <code>Iterate with L & R pointers, skip invalid characters with ASCII range checks, compare in lowercase, finally return True if no mismatches found</code><br>
<a href="dsa/python/TwoPointer/valid-palindrome.py">python</a> | 
<a href="golang/TwoPointer/valid-palindrome.go">go</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/" target="_blank">Two Sum II Input Array Is Sorted</a></b> <code>Iterate with L & R pointers, adjust pointers based on cur_sum relative to target, and return indices if they match</code><br>
<a href="dsa/python/TwoPointer/two-sum-ii-input-array-is-sorted.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/container-with-most-water/" target="_blank">Container With Most Water</a></b> <code>Iterate with L & R pointers, calculate the current area and update max_area if larger, then move pointer with the lower height</code><br>
<a href="dsa/python/TwoPointer/container-with-most-water.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/3sum/" target="_blank">3Sum</a></b> <code>Sort the array and iterate through nums, skipping duplicates. For each nums[i], set target = -nums[i] and iterate using L & R pointers to find pairs that sum to the target. Add indices on a match, and skip duplicates for L followed by R pointers</code><br>
<a href="dsa/python/TwoPointer/3sum.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank">Trapping Rain Water</a></b> <code>Create left_max and right_max arrays(based on height[i-1]). Iterate len(height), calculating running sum of trapped_water(min(left_max, right_max) - height). Return trapped_water</code><br>
<a href="dsa/python/TwoPointer/trapping-rain-water.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Sliding Window</h4></summary>
<blockquote>
<a href="https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175088/C++-Maximum-Sliding-Window-Cheatsheet-Template/">Template</a>
</blockquote>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/" target="_blank">Best Time to Buy and Sell Stock</a></b> <code>Set buy to prices[0], iterate through prices calculating profit, and update if larger</code><br>
<a href="dsa/python/SlidingWindow/best-time-to-buy-and-sell-stock.py">python</a> | 
<a href="golang/SlidingWindow/best-time-to-buy-and-sell-stock.go">go</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/" target="_blank">Longest Substring Without Repeating Characters</a></b> <code>Initialize L pointer to 0. Iterate over s, adding characters to a charSet. If duplicate is found, remove characters from left until duplicate is gone. Continuously update longest substring and return it at end</code><br>
<a href="dsa/python/SlidingWindow/longest-substring-without-repeating-characters.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/frequency-of-the-most-frequent-element/" target="_blank">Frequency of the Most Frequent Element</a></b> <code>Sort the array(This helps in making numbers equal efficiently). Use sliding window, Expand the window by adding elements from the right, Check if we can make all numbers in the window equal using at most k operations, If not possible, shrink the window from the left. Keep track of the largest valid window. We try to make multiple numbers equal to the largest number in the current window while keeping the operations within the allowed limit k</code><br>
<a href="dsa/python/SlidingWindow/frequency-of-the-most-frequent-element.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/" target="_blank">Longest Subarray of 1's After Deleting One Element</a></b> <code></code><br>
<a href="dsa/python/SlidingWindow/longest-subarray-of-1s-after-deleting-one-element.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-repeating-character-replacement/" target="_blank">Longest Repeating Character Replacement</a></b> <code>Set L = 0 and iterate R through s, tracking the max frequency of any character by comparing against the current character count. Adjust L & char frequencies in window while the count of other characters exceeds k using maxf. Continuously update longest substring with repetitions and return it at end</code><br>
<a href="dsa/python/SlidingWindow/longest-repeating-character-replacement.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/permutation-in-string/" target="_blank">Permutation In String</a></b> <code>Calculate char_count of s1. For each char in s2, if it exists in s1: create char_count of s2, with len(s1). If char_count's are same return True. Otherwise return False finally</code><br>
<a href="dsa/python/SlidingWindow/permutation-in-string.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/minimum-window-substring/" target="_blank">Minimum Window Substring</a></b> <code>Use 2 variables called have & need & 2 HashMaps to track char counts in s and t, and initialize have to 0. Loop through s, updating window counts and incrementing have when (window[c] == count_t[c]). Loop while (have == len(count_t)), if current window is smaller than ans_len, update res and ans_len. Slide l right, adjusting window[s[l]] & have if window count goes below count_t. Return res</code><br>
<a href="dsa/python/SlidingWindow/minimum-window-substring.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/sliding-window-maximum/" target="_blank">Sliding Window Maximum</a></b> <code></code><br>
<a href="dsa/python/SlidingWindow/sliding-window-maximum.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Stack</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/valid-parentheses/" target="_blank">Valid Parentheses</a></b> <code>Use a HashMap {')': '('}. Iterate through the string: append open brackets to stack. For closing brackets, return False if the stack is empty or there's a mismatch with stack.pop(). At the end, return whether the stack is empty</code><br>
<a href="dsa/python/Stack/valid-parentheses.py">python</a> | 
<a href="golang/Stack/valid-parentheses.go">go</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/min-stack/" target="_blank">Min Stack</a></b> <code>Use 2 stacks: one for values and one to keep track of the minimum value so far (min_stack). During each insert, push the current minimum onto min_stack.</code><br>
<a href="dsa/python/Stack/min-stack.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/evaluate-reverse-polish-notation/" target="_blank">Evaluate Reverse Polish Notation</a></b> <code>Use a stack to store operands. When an operator is encountered, pop the last two operands, perform the operation in the correct order, and push the result back onto the stack. At the end, return the last value in the stack</code><br>
<a href="dsa/python/Stack/evaluate-reverse-polish-notation.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/generate-parentheses/" target="_blank">Generate Parentheses</a></b> <code>Use stack to store braces while generating valid combinations. Define dfs to recursively explore paths, skipping invalid paths based on counts of open & close brackets. Append stack content to the results when both counts equal n. If (o_cnt < n), add opening bracket, call dfs, then backtrack. If (c_cnt < o_cnt), add closing bracket, call dfs, then backtrack again. Return ans finally</code><br>
<a href="dsa/python/Stack/generate-parentheses.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/daily-temperatures/" target="_blank">Daily Temperatures</a></b> <code>Initialize ans array with 0's. Iterate through temperatures, while using a monotonically decreasing stack to store element index. While (temperature[i] > temperature[stack[top]]), pop from stack and update ans[stack_index] with difference between indices.</code><br>
<a href="dsa/python/Stack/daily-temperatures.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/car-fleet/" target="_blank">Car Fleet</a></b> <code>Sort (position, speed) pairs by position in ascending order. Iterate through pairs in reverse. For each car, calculate time to reach target; if this time <= the time at top of the stack, it joins the same fleet. Otherwise, add it to the stack. Finally, return the stack’s length as number of fleets</code><br>
<a href="dsa/python/Stack/car-fleet.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/largest-rectangle-in-histogram/" target="_blank">Largest Rectangle In Histogram</a></b> <code>Maintain a monotonically increasing stack (start, height). Iterate through heights, when a smaller element is found, pop all taller elements from the stack, processing their contribution to max_area and mark the start index of the current element as the last popped pushing current element onto the stack. Run an additional loop for remaining elements in the stack, calculating their heights wrt len(heights), updating max_area. Finally return max_area</code><br>
<a href="dsa/python/Stack/largest-rectangle-in-histogram.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Binary Search</h4></summary>
<blockquote>
<a href="https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems">Template</a>
</blockquote>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/binary-search/" target="_blank">Binary Search</a></b> <code>Use 3 pointers: l, r & mid. Compare the mid value with the target and either move the window left/right or return the index if found.</code><br>
<a href="dsa/python/BinarySearch/binary-search.py">python</a> | 
<a href="golang/BinarySearch/binary-search.go">go</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/first-bad-version/" target="_blank">First Bad Version</a></b> <code></code><br>
<a href="dsa/python/BinarySearch/first-bad-version.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/sqrtx/" target="_blank">Sqrt(x)</a></b> <code></code><br>
<a href="dsa/python/BinarySearch/first-bad-version.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/sqrtx/" target="_blank">Sqrt(x)</a></b> <code></code><br>
<a href="dsa/python/BinarySearch/first-bad-version.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/search-a-2d-matrix/" target="_blank">Search a 2D Matrix</a></b> <code>Use binary search to find row, where the target may lie based on row boundaries. If the target isn’t within any of the row ranges, return False. Otherwise, set the row to the last calculated midpoint and perform a binary search within that row for the target</code><br>
<a href="dsa/python/BinarySearch/search-a-2d-matrix.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/koko-eating-bananas/" target="_blank">Koko Eating Bananas</a></b> <code>Use binary search between 1 and max(piles) to find the minimum eating speed. If a solution meets the hours constraint ℎ, try smaller speeds to minimize further. Return the last speed that satisfies the condition</code><br>
<a href="dsa/python/BinarySearch/koko-eating-bananas.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/" target="_blank">Find Minimum in Rotated Sorted Array</a></b> <code>Initialize l and r to the start and end. Update ans, as min(ans, nums[mid]). If nums[mid] > nums[r], move window right; otherwise, move window left. Return min(nums[l], ans)</code><br>
<a href="dsa/python/BinarySearch/find-minimum-in-rotated-sorted-array.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/" target="_blank">Search in Rotated Sorted Array</a></b> <code>Use 3 pointers l, r, mid. mid will be apart of either left sorted or right sorted portions. If target is in range of sorted portion then search it, otherwise search other half</code><br>
<a href="dsa/python/BinarySearch/search-in-rotated-sorted-array.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/time-based-key-value-store/" target="_blank">Time Based Key Value Store</a></b> <code>Use a HashMap to store each key's list of [value, timestamp] pairs. For set, append the pair; for get, use binary search to find the most recent value with a timestamp ≤ the query using the concept of a running result that contains the most recent value found so far. Return it at the end</code><br>
<a href="dsa/python/BinarySearch/time-based-key-value-store.py">python</a>
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
<a href="dsa/python/LinkedList/reverse-linked-list/reverse-linked-list.py">python</a> | 
<a href="golang/LinkedList/reverse-linked-list.go">go</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/merge-two-sorted-lists/" target="_blank">Merge Two Sorted Lists</a></b> <code>Create an empty node cur with a pointer res. Iterate while both list1 and list2 are not None, adding the node with the lower value to cur. Then if either list is None, append the other list. Finally, return res.next</code><br>
<a href="dsa/python/LinkedList/merge-two-sorted-lists/merge-two-sorted-lists.py">python</a> | 
<a href="golang/LinkedList/merge-two-sorted-lists.go">go</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/linked-list-cycle/" target="_blank">Linked List Cycle</a></b> <code>Initialize f & s pointers to head. Iterate while f and f.next exist, moving f by 2 and s by 1. If they are equal, return True; otherwise, return False</code><br>
<a href="dsa/python/LinkedList/linked-list-cycle.py">python</a> | 
<a href="golang/LinkedList/linked-list-cycle.go">go</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/middle-of-the-linked-list/" target="_blank">Middle of the Linked List</a></b> <code>Use s & f pointing to head. Use loop condition, f and f.next. Run them like tortoise & hare. Return s</code><br>
<a href="dsa/python/LinkedList/middle-of-the-linked-list.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/palindrome-linked-list/" target="_blank">Palindrome Linked List</a></b> <code>Go to left center. Reverse 2nd half. Compare both from beginning (No need to compare remaining element as it will be middle)</code><br>
<a href="dsa/python/LinkedList/palindrome-linked-list.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/reorder-list/" target="_blank">Reorder List</a></b> <code>Move the s pointer to the center of the list while ensuring f.next exists. Set s.next as the start of the second half, then set s.next to None to end the first half. Reverse the second list, then use 2 temp variables to merge both halves.</code><br>
<a href="dsa/python/LinkedList/reorder-list.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/" target="_blank">Remove Nth Node From End of List</a></b> <code>Create a dummy node pointing to head and assign it to l. Assign r to head and move r forward n times. Then, move both pointers until r reaches the end. Set l.next.next to l.next and return dummy.next</code><br>
<a href="dsa/python/LinkedList/remove-nth-node-from-end-of-list.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/copy-list-with-random-pointer/" target="_blank">Copy List with Random Pointer</a></b> <code>First, create a map to store the deep copies of each node. Traverse the original linked list, creating deep copies of all nodes. Then, traverse it again to set the next and random pointers for the copied nodes using the map. Finally, return the deep copy of the head node from the map</code><br>
<a href="dsa/python/LinkedList/copy-list-with-random-pointer.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/add-two-numbers/" target="_blank">Add Two Numbers</a></b> <code>Traverse both input lists using a dummy node and maintain a carry. For each node, sum values and carry, add the remainder to the result list. Continue until both lists are exhausted, handling any leftover carry by adding an extra node. Return dummy.next as the final result</code><br>
<a href="dsa/python/LinkedList/add-two-numbers.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/lru-cache/" target="_blank">LRU Cache</a></b> <code>Utilize a HashMap for quick value access and a doubly linked list (DLL) to track the order of usage. The DLL has two dummy nodes marking the LRU (left) and MRU (right). For put operations, the DLL functions like a queue, while get operations involve moving nodes to the MRU side, introducing extra complexity</code><br>
<a href="dsa/python/LinkedList/lru-cache.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank">Merge k Sorted Lists</a></b> <code>Create mergeLists() to merge two lists. While len(lists) > 1, run an inner loop to merge two lists at a time, append the result to mergedLists, and assign mergedLists to lists. Finally, return lists[0]</code><br>
<a href="dsa/python/LinkedList/merge-k-sorted-lists.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/reverse-nodes-in-k-group/" target="_blank">Reverse Nodes in k-Group</a></b> <code>Use slow (s) and fast (f) pointers to traverse the list with an index counter i. When i is a multiple of k, disconnect f and move it forward. Reverse the sublist from s to f and connect it to the previous tail. Update prev_tail and start the next group from s. After traversal, connect any remaining nodes and return the modified list starting from dummy.next</code><br>
<a href="dsa/python/LinkedList/reverse-nodes-in-k-group.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Trees</h4></summary>
<blockquote>
<a href="https://leetcode.com/discuss/study-guide/1820334/Become-Master-in-Tree">Refresher</a>
</blockquote>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/binary-tree-preorder-traversal/" target="_blank">Binary Tree Preorder Traversal</a></b> <code></code><br>
<a href="dsa/python/Trees/binary-tree-preorder-traversal.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/binary-tree-inorder-traversal/" target="_blank"></a></b> <code>Binary Tree Inorder Traversal</code><br>
<a href="dsa/python/Trees/binary-tree-inorder-traversal.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/invert-binary-tree/" target="_blank">Invert Binary Tree</a></b> <code>Traverse via dfs(). If node exists, replace left and right. Call dfs(left), then dfs(right)</code><br>
<a href="dsa/python/Trees/invert-binary-tree.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/" target="_blank">Maximum Depth of Binary Tree</a></b> <code>Use recursive DFS with a leaf case returning 0. At each step, return 1 + the max height of the left and right subtrees</code><br>
<a href="dsa/python/Trees/maximum-depth-of-binary-tree.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/diameter-of-binary-tree/" target="_blank">Diameter of Binary Tree</a></b> <code>Use a maxHeight function, while before returning the height, maintain the calculate the diameter (l_height+r_height) and update max_diameter. Finally return max_diameter</code><br>
<a href="dsa/python/Trees/diameter-of-binary-tree.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/diameter-of-binary-tree/" target="_blank">Balanced Binary Tree</a></b> <code>Perform post order dfs, return -1 if subtree is not balanced. </code><br>
<a href="dsa/python/Trees/balanced-binary-tree.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/same-tree/" target="_blank">Same Tree</a></b> <code>For base cases, return True if both nodes are None. If either is None or values don’t match, return False. In the recursive case, return fn(left) and fn(right)</code><br>
<a href="dsa/python/Trees/same-tree.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/subtree-of-another-tree/" target="_blank">Subtree of Another Tree</a></b> <code>Create a separate fn isSameTree() and perform BFS on the root. At each node, if isSameTree(node, subTree) return True. Finally if no same trees were found, return False</code><br>
<a href="dsa/python/Trees/subtree-of-another-tree.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree" target="_blank">Lowest Common Ancestor of a Binary Tree</a></b> <code>Use an instance variable to store state. in the recursive function basecase, return False if node is None. Perform a post order dfs, use 3 flags to account for the 3 cases(parent of nodes, not parent and node parent of another). cur(if current node is p or q), left & right(if node is present in respective subtrees). If either 2 flags are true set self.lca. Return left or right or cur</code><br>
<a href="dsa/python/Trees/lowest-common-ancestor-of-a-binary-tree.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/" target="_blank">Lowest Common Ancestor of a Binary Search Tree</a></b> <code>While True: if root.val > p and q, move left. If root.val < p and q, move right. Otherwise, if root lies between p and q or equals p or q, return root</code><br>
<a href="dsa/python/Trees/lowest-common-ancestor.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/binary-tree-level-order-traversal/" target="_blank">Binary Tree Level Order Traversal</a></b> <code>Add root to a Q. While the Q is not empty, initialize a level array. Run an inner loop for len(Q), adding node.val to level and left & right children back to the Q. If level is not empty, add it to res. Finally, return res</code><br>
<a href="dsa/python/Trees/binary-tree-level-order-traversal.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/binary-tree-level-order-traversal/" target="_blank">Binary Tree Right Side View</a></b> <code></code><br>
<a href="dsa/python/Trees/binary-tree-right-side-view.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/count-good-nodes-in-binary-tree/" target="_blank">Count Good Nodes in Binary Tree</a></b> <code></code><br>
<a href="dsa/python/Trees/count-good-nodes-in-binary-tree.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/validate-binary-search-tree/" target="_blank">Validate Binary Search Tree</a></b> <code>Define valid() with node, left, and right values. If node is None, return True. If node.val is not between left and right, return False. Recursively return valid(node.left, left, node.val) and valid(node.right, node.val, right)</code><br>
<a href="dsa/python/Trees/validate-binary-search-tree.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/kth-smallest-element-in-a-bst/" target="_blank">Kth Smallest Element in a BST</a></b> <code>Use a single pointer and a stack. Iterate while stack or pointer are not empty. Push cur.left to the stack, until cur.left is None. Pop from the stack, decrement k, and check if k == 0 to return the node's value. Otherwise, set cur to cur.right and continue</code><br>
<a href="dsa/python/Trees/kth-smallest-element-in-a-bst.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/" target="_blank">Construct Binary Tree from Preorder and Inorder Traversal</a></b> <code>If either traversal is empty, return None. The 1st element in preorder is the root. Use inorder to find the root's index (mid). In inorder, elements left of mid are the left subtree, and elements right of mid are the right subtree. Recursively build subtrees.</code><br>
<a href="dsa/python/Trees/construct-binary-tree-from-preorder-and-inorder-traversal.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/binary-tree-maximum-path-sum/" target="_blank">Binary Tree Maximum Path Sum</a></b> <code>Perform a postorder traversal to calculate the path sum, of the max height of the left(l) and right(r) subtrees, treating negative values as 0. For each node, update the max_path_sum if (n.val + l + r) exceeds the current maximum. Return the path sum contribution of node as (n.val + max(l, r)). Finally, return max_path_sum</code><br>
<a href="dsa/python/Trees/binary-tree-maximum-path-sum.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/serialize-and-deserialize-binary-tree/" target="_blank">Serialize And Deserialize Binary Tree</a></b> <code>Use the same traversal for encoding and decoding. For encoding, if a node is None, add 'N' to res; otherwise, add str(node.val). For decoding, split the string by ','; if 'N', return None, otherwise return TreeNode(val) while incrementing self.i. Finally, return the root.</code><br>
<a href="dsa/python/Trees/serialize-and-deserialize-binary-tree.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Heap / Priority Queue</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/kth-largest-element-in-a-stream/" target="_blank">Kth Largest Element in a Stream</a></b> <code>Heapify nums to a min_heap and reduce the size to k. In add(), push element to heap, if len(min_heap) > k: pop and return min_heap[0]</code><br>
<a href="dsa/python/Heap-PriorityQueue/kth-largest-element-in-a-stream.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/last-stone-weight/" target="_blank">Last Stone Weight</a></b> <code>Use a max-heap to repeatedly extract the two largest stones, smash them, and push the remaining stone back into the heap if any. Return the last stone in the heap or 0 if the heap is empty.</code><br>
<a href="dsa/python/Heap-PriorityQueue/last-stone-weight.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/k-closest-points-to-origin/" target="_blank">K Closest Points to Origin</a></b> <code>Use a min-heap to store vertices sorted by Euclidean distance. Repeatedly pop elements from the heap until the k-th smallest is reached, and then return it.</code><br>
<a href="dsa/python/Heap-PriorityQueue/k-closest-points-to-origin.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/kth-largest-element-in-an-array/" target="_blank">Kth Largest Element in an Array</a></b> <code>Use a max-heap and heapify the array. Keep popping elements until we reach the kth largest, then return it</code><br>
<a href="dsa/python/Heap-PriorityQueue/kth-largest-element-in-an-array.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/task-scheduler/" target="_blank">Task Schedule</a></b> <code>Maintain 2 queues(free_q & idling_q). Construct free_q as a max_heap based on frequency. Simulate seconds while iterating, until both queues are empty. Each tick, consume a task from the free_q and move the remainder of the task to the idling_q [count, time+n]. If idling time is up, popleft from the idling q and add remaining tasks to the free_q. Finally return ticks</code><br>
<a href="dsa/python/Heap-PriorityQueue/task-scheduler.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/design-twitter/" target="_blank">Design Twitter</a></b> <code>Create a singly linked list class Tweet, with id, timestamp and next pointer. In class Twitter, create 2 dictionaries, following{uid: [follow_id]} and tweets{uid: Tweethead}, Initialize an incrementing timestamp to 0, to store last_modified to tweets when added. In postTweet, add timestamp as last_modified. For follow() and unfollow() add and discard from following dict. For getNewsFeed(), first create a max_heap based on last_modified for tweets for all following and user itself. To generate feed while heap is not empty and len(feed) < FEED_SIZE, pop from heap append to feed and add the tweet's next back to the heap. Finally return feed</code><br>
<a href="dsa/python/Heap-PriorityQueue/design-twitter/design-twitter.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/find-median-from-data-stream/" target="_blank">Find Median From Data Stream</a></b> <code>Use 2 arrays as min & max heaps. For addNum(), Follow a 2 step process. First Insert, if num < max_heap[0]: push into max_heap otherwise push to min_heap. Then rebalance, if len of either heap is greater than the other by 1. For findMedian(), For the odd len case, return the top of the longer heap. For even case, get the top values by peaking, and return (v1+v2)/2</code><br>
<a href="dsa/python/Heap-PriorityQueue/find-median-from-data-stream.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Backtracking</h4></summary>
<blockquote>
<a href="https://leetcode.com/problems/subsets/solutions/27281/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning/">Template</a>
</blockquote>
<ul>
<li><b>🟧 <a href="https://leetcode.com/problems/subsets/" target="_blank">Subsets</a></b> <code>Implement a dfs() method that takes an iterator and uses the pick-and-no-pick algorithm to explore subsets. At each step, include the current element & skip it. Add the current subset to the result list when the iterator reaches the end of nums</code><br>
<a href="dsa/python/Backtracking/subsets.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/combination-sum/" target="_blank">Combination Sum</a></b> <code>Define dfs(i, cur, total). Base cases: if target == total, append cur.copy() to res and return. If idx >= len(nums) or total > target, return. Append nums[i] to cur, add to total, then call dfs(). After, pop() from cur, subtract nums[i] from total, increment i, and call dfs() again. Finally, return res</code><br>
<a href="dsa/python/Backtracking/combination-sum/combination-sum.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/combination-sum-ii/" target="_blank">Combination Sum II</a></b> <code>Sort the array to handle duplicates efficiently, then use backtracking to explore combinations while maintaining a running total. Append valid combinations when the total matches the target and terminate early if it exceeds the target. Skip duplicate elements during iteration to avoid redundant results</code><br>
<a href="dsa/python/Backtracking/combination-sum/combination-sum-ii.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/permutations/" target="_blank">Permutations</a></b> <code>Define backtrack(cur), with BC: if len(cur) == len(nums), add it to res and return. Otherwise loop through nums, if n is not in cur add it, and recursively call backtrack with the new cur, then pop the element and continue the iteration. Return res at the end</code><br>
<a href="dsa/python/Backtracking/permutations.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/subsets-ii/" target="_blank">Subsets II</a></b> <code>Sort input array to group duplicates, then use backtracking to generate subsets by either including the current element (pick) or skipping it (no-pick); before making no-pick recursive call, ensure duplicates are skipped by advancing the index to the next unique value, thereby avoiding duplicates</code><br>
<a href="dsa/python/Backtracking/subsets-ii.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/word-search/" target="_blank">Word Search</a></b> <code>Define dfs(r, c, i). If i == len(word), return True. If r or c are out of bounds, characters don't match, or the cell is already in the path, return False. If the current cell matches word[i], add it to the path, and recursively check neighboring cells recording result. backtrack by removing the cell from the path and return result</code><br>
<a href="dsa/python/Backtracking/word-search.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/palindrome-partitioning/" target="_blank">Palindrome Partitioning</a></b> <code></code><br>
<a href="dsa/python/Backtracking/palindrome-partitioning.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/" target="_blank">Letter Combinations of a Phone Number</a></b> <code>Create a map of numbers to a list of letters. Use a param start to backtrack() that increments each recursive call and tracks the idx of digits. BCs- len(path) == len(digits), add to res and return. start >= len(digits), return. Guard the backtrack call by a condition that checks if len(digits) > 0. Return combinations collected.</code><br>
<a href="dsa/python/Backtracking/letter-combinations-of-a-phone-number.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/n-queens/" target="_blank">N Queens</a></b> <code>Create a fn that validates a (row, col) against already placed queens. Create another fn, that attempts to place queens on the board, if the (r,c) is a valid placement, place a queen, and recurse to attempt to place on the next row. BC: when len of placed queens reaches board size, save a copy of the board. Finally return placed queens.</code><br>
<a href="dsa/python/Backtracking/n-queens.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Tries</h4></summary>
<ul>
<li><b>🟧 <a href="https://leetcode.com/problems/implement-trie-prefix-tree/" target="_blank">Implement Trie Prefix Tree</a></b> <code>Use a TrieNode with a children HashMap and a boolean end_of_word set to False. For insert, traverse the Trie from the root, creating a new TrieNode for each letter in the word if it doesn't already exist in children, and move to the node. After processing all letters, mark end_of_word as True. For search, traverse from the root, checking if each letter exists in children. If any letter is missing, return False; otherwise, continue to the next node. After processing all letters, return whether end_of_word is True for the final node. For startsWith: Follow the same logic as Search(), but finally return True irrespective if we reached an end_of_word or not.</code><br>
<a href="dsa/python/Tries/implement-trie-prefix-tree.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/design-add-and-search-words-data-structure/" target="_blank">Design Add and Search Words Data Structure</a></b> <code>In the AddWord method, the process remains identical to the insert method in a Trie. For search, a recursive approach is used: if the current character is not '.', check if it exists in the current node's children and continue the search(return False if not present). If the character is '.', recursively explore all children nodes, returning True if any branch leads to a match. If no valid path exists, return False</code><br>
<a href="dsa/python/Tries/design-add-and-search-words-data-structure.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/word-search-ii/" target="_blank">Word Search II</a></b> <code>Insert words into a Trie, then traverse the board recursively, exploring neighbors to match characters with Trie nodes. Terminate on mismatches and backtrack by marking and unmarking visited cells. Trie traversal handles mismatches, so explicit backtracking on the Trie isn’t needed</code><br>
<a href="dsa/python/Tries/word-search-ii.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/design-in-memory-file-system/" target="_blank">Design In-Memory File System</a></b> <code></code><br>
<a href="dsa/python/Tries/design-in-memory-file-system.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Graphs</h4></summary>
<ul>
<li><b>🟧 <a href="https://leetcode.com/problems/number-of-islands/" target="_blank">Number of Islands</a></b> <code>Define dfs(r, c) with BC: return if r or c are out of bounds, if grid[r][c] is not "1", or if (r, c) is in the visited set. If conditions are met, add (r, c) to visited and perform dfs on its four neighbors. Use a nested loop for r and c, and if grid[r][c] is "1" and not in visited, increment the islands and call dfs(r, c)</code><br>
<a href="dsa/python/Graphs/number-of-islands.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/max-area-of-island/" target="_blank">Max Area of Island</a></b> <code>Define dfs(r, c) with BC: return 0 if r or c are out of bounds, or if (r, c) is in the visited set. If conditions are met, add (r, c) to visited and return (1 + sum of dfs on each of its four neighbors). Use a nested loop for r and c, and maintain a running max_area updated with the result of each dfs call. Return max_area at the end</code><br>
<a href="dsa/python/Graphs/max-area-of-island.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/clone-graph/" target="_blank">Clone Graph</a></b> <code>Create a HashMap to track visited nodes. Define dfs(node) with a BC: if node is already visited, return its corresponding value from the HashMap. Otherwise, create a copy with node.val & map it in the HashMap. Then iterate through node's neighbors, appending the result of dfs(neighbor) to copy's neighbors. Finally, return the copy</code><br>
<a href="dsa/python/Graphs/clone-graph.py">python</a>
</li>
<li><b>🟧 <a href="https://neetcode.io/problems/islands-and-treasure" target="_blank">Islands and Treasure</a></b> <code>Loop across the grid till we find a treasure. Maintain running minimums for all non (-1 & 0) neighbours. Use a visited set to avoid revisits in each backtrack. and avoid traversing if we find another 0. Return the grid modified in place at the end</code><br>
<a href="dsa/python/Graphs/walls-and-gates.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/rotting-oranges/" target="_blank">Rotting Oranges</a></b> <code>Iterate through cells in the grid to collect 2's in a q and maintain a count of 1's(fresh). Execture BFS on 2's and change neighbours with 1->2, and updating fresh. Gate BFS while, with fresh > 0 for a potential early exit. And finally return minutes if no ones remain otherwise -1</code><br>
<a href="dsa/python/Graphs/rotting-oranges.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/pacific-atlantic-water-flow/" target="_blank">Pacific Atlantic Water Flow</a></b> <code>Define dfs(r, c, pre_height) with BC: return if current cell (r, c) is out of bounds, has (height < pre_height), or already in visited. Use 2 HashSets to track cells reachable from the pac and atl oceans. Loop through cols to add nodes reachable from the first and last row to the Pacific and Atlantic sets. Similarly, loop through rows to add nodes reachable from the first and last column. Finally, loop through the grid(r & c) and add cells that reach both oceans to the result, and return it.</code><br>
<a href="dsa/python/Graphs/pacific-atlantic-water-flow.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/surrounded-regions/" target="_blank">Surrounded Regions</a></b> <code>Run dfs from edges of board marking all reachable O's as T's. Iterate through board, changing all O's to X's followed by all T's to O's</code><br>
<a href="dsa/python/Graphs/surrounded-regions.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/course-schedule/" target="_blank">Course Schedule</a></b> <code>Create adjacency list for directed graph. Define dfs(c) with BCs: if course already visited, return False; if course has no dependencies, return True. For each course, Add it to visited, check its dependencies with dfs(). If any dfs() call fails, return False. After processing, remove course from visited, empty adj[c] and return True. If dfs() fails for any course, return False; otherwise, return True.</code><br>
<a href="dsa/python/Graphs/course-schedule.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/course-schedule-ii/" target="_blank">Course Schedule II</a></b> <code>Similar to original problem, Maintain a cycle set, that works similar to the visit set. After we remove from the cycle set, add to visit set & res, for the True base condition, check if course exists in visit set instead of whether pre_reqs are empty. Return [], if dfs failed, otherwise return res</code><br>
<a href="dsa/python/Graphs/course-schedule-ii.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/graph-valid-tree/" target="_blank">Graph Valid Tree</a></b> <code>Create an adjacency list for each node using a HashMap (undirected graph). Use a set to track visited nodes. Define dfs(i, prev) with BC: if node already visited, return False. For each node, iterate through its neighbors, skipping previous node. If any check fails, return False, otherwise finally True. Return dfs(0, -1) and (len(visited) == n)</code><br>
<a href="dsa/python/Graphs/graph-valid-tree.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/" target="_blank">Create adjacency list for each vertex and a visited list for each n ([False] * n), For each vertex, if not visited, run dfs and increase component count. Finally return components.</code><br>
<a href="dsa/python/Graphs/number-of-connected-components-in-an-undirected-graph.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/redundant-connection/" target="_blank">Redundant Connection</a></b> <code></code><br>
<a href="dsa/python/Graphs/redundant-connection.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/word-ladder/" target="_blank">Word Ladder</a></b> <code>Add beginning word to wordList & Create adjancy List {pattern: [word]}. Perform BFS, returning res if there is a match, otherwise add all unvisited neighbors of the word to the q incrementing res with each level of breadth. Finally return 0 if word not found</code><br>
<a href="dsa/python/Graphs/word-ladder.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/minimize-malware-spread/" target="_blank">Minimize Malware Spread</a></b> <code>https://github.com/doocs/leetcode/blob/main/solution/0900-0999/0924.Minimize%20Malware%20Spread/README_EN.md</code><br>
<a href="dsa/python/Graphs/minimize-malware-spread.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Advanced Graphs</h4></summary>
<ul>
<li><b>🟧 <a href="https://leetcode.com/problems/network-delay-time/" target="_blank">Network Delay Time</a></b> <code>Use Djikstra's algo. Sort neighbours by weight in min_heap. Maintain a max running time, that indicates the min path till the end. If visited contains all nodes return max_time, else -1</code><br>
<a href="dsa/python/AdvancedGraphs/network-delay-time.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/reconstruct-itinerary/" target="_blank">Reconstruct Itinerary</a></b> <code></code><br>
<a href="">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/min-cost-to-connect-all-points/" target="_blank">Min Cost to Connect All Points</a></b> <code>Use Prim's algo. Create adjacency list for bidirectional weighted graph[md, idx]. Iterate while len(visit) < len(points). pop from min_ heap, skip if already visited, and add neighbours to min_heap. Finally return min cost</code><br>
<a href="dsa/python/AdvancedGraphs/min-cost-to-connect-all-points.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/swim-in-rising-water/" target="_blank">Swim in Rising Water</a></b> <code>Use BFS with a min_heap. Use (time, (r, c)) as ds on heap. Maintain a running max for times popped from heap. If (r, c) in visited, continue. If (r, c) is end, return max_time. Otherwise add valid neighbours.</code><br>
<a href="dsa/python/AdvancedGraphs/swim-in-rising-water.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/alien-dictionary/" target="_blank">Alien Dictionary</a></b> <code></code><br>
<a href="">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/cheapest-flights-within-k-stops/" target="_blank">Cheapest Flights Within K Stops</a></b> <code>Use Djikstra's algo. But add a parameter num_stops also to be tracked in the heap, Allow revisiting of node if num_stops is less, that existing value. Return cost, if dest is reached. Otherwise -1</code><br>
<a href="dsa/python/AdvancedGraphs/cheapest-flights-within-k-stops.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>1-D Dynamic Programming</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/climbing-stairs/" target="_blank">Climbing Stairs</a></b> <code>Model this after fibonacci series starting with 1, 1. Use the fibonacci recurrance relation.</code><br>
<a href="dsa/python/1D-DynamicProgramming/climbing-stairs.py">python</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/min-cost-climbing-stairs/" target="_blank">Min Cost Climbing Stairs</a></b> <code>Similar to climbing stairs, but we need to account for cost at individual stair as well. For the final result, we return the min(len-1, len-2).</code><br>
<a href="dsa/python/1D-DynamicProgramming/min-cost-climbing-stairs.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/house-robber/" target="_blank">House Robber</a></b> <code>The base cases here should be 0, when idx < 0 and nums[house] when idx = 0. Reccurance relation starts from 1, and is the max(rRob(i-1), rRob(i-2) + nums[i])</code><br>
<a href="dsa/python/1D-DynamicProgramming/house-robber/house-robber.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/house-robber-ii/" target="_blank">House Robber II</a></b> <code>Similar to house robber 1, but here we return the max(without_first_house, without_last_house)</code><br>
<a href="dsa/python/1D-DynamicProgramming/house-robber-ii.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-palindromic-substring/" target="_blank">Longest Palindromic Substring</a></b> <code>Initialize res as "" and res_len as 0. Loop through the string, checking for odd-length (l, r = i, i) and even-length (l, r = i, i+1) palindromes. Update res and res_len whenever a longer palindrome is found. Finally, return res</code><br>
<a href="dsa/python/1D-DynamicProgramming/longest-palindromic-substring.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/palindromic-substrings/" target="_blank">Palindromic Substrings</a></b> <code>Initialize count to 0. Loop through the string, checking for odd-length (l, r = i, i) and even-length (l, r = i, i+1) palindromes using expand-from-center algorithm. Increment count for each palindrome found, and return total count at the end</code><br>
<a href="dsa/python/1D-DynamicProgramming/palindromic-substrings.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/decode-ways/" target="_blank">Decode Ways</a></b> <code>BCs: If s is '' or starts with '0', return 0. If s length is 1, return 1. Initialize upto_prev and upto_cur to 1. Loop from 1 to len(s). Convert s[i] and (s[i-1] + s[i]) to 0-based integers. If cur > 0, add upto_cur to val. If prev forms a number between 10 and 26, add upto_prev to val. Update upto_prev to upto_cur and upto_cur to val. Finally, return upto_cur</code><br>
<a href="dsa/python/1D-DynamicProgramming/decode-ways.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/coin-change/" target="_blank">Coin Change</a></b> <code>Use tabulation to create a DP array of size amount + 1, initialized to amount + 1. For each amount from 1 to amount, loop through each coin and update dp[a] to the minimum of dp[a] and 1 + dp[a - c]. Return dp[amount] if it's updated, otherwise return -1.</code><br>
<a href="dsa/python/1D-DynamicProgramming/coin-change.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/maximum-product-subarray/" target="_blank">Maximum Product Subarray</a></b> <code>Initialize cur_max and cur_min to 1 & res to nums[0]. Loop through nums, updating cur_max as the maximum and cur_min as the minimum of (n * cur_max, n * cur_min, n) for each n. Update res as the maximum of res and cur_max. Return res</code><br>
<a href="dsa/python/1D-DynamicProgramming/maximum-product-subarray.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/word-break/" target="_blank">Word Break</a></b> <code>Initialize DP array with False and set the last element to True. Loop through the string in reverse, checking each substring against the list of words. If a match is found, update the DP array at the current index to dp[i + len(w)] and break the inner loop. Finally, return the value of dp[0]</code><br>
<a href="dsa/python/1D-DynamicProgramming/word-break.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-increasing-subsequence/" target="_blank">Longest Increasing Subsequence</a></b> <code>Declare a dp array initialized to 1 for each element in nums. Loop through nums in reverse, for each element, loop again from i + 1 to len(nums). If nums[i] < nums[j], update dp[i] to max(dp[i], 1 + dp[j]). Finally, return the maximum value in dp</code><br>
<a href="dsa/python/1D-DynamicProgramming/longest-increasing-subsequence.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>2-D Dynamic Programming</h4></summary>
<ul>
<li><b>🟧 <a href="https://leetcode.com/problems/unique-paths/" target="_blank">Unique Paths</a></b> <code></code><br>
<a href="dsa/python/Greedy/maximum-subarray.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-common-subsequence/" target="_blank">Longest Common Subsequence</a></b> <code>Start from the ends of both strings, and make the way to the start. If either indices goes out of bounds(-1), return 0. If characters match, return 1 + f(i-1, j-1), otherwise return max(f(i, j-1), f(i-1, j)).</code><br>
<a href="dsa/python/2D-DynamicProgramming/longest-common-subsequence.py">python</a>
</li>
<li><b>🟧 <a href="https://www.geeksforgeeks.org/problems/longest-common-substring1452/1" target="_blank">Longest Common Substring</a></b> <code>Start from the ends of both strings, and make the way to the start. If either indices goes out of bounds(-1), return 0. If characters match, return 1 + f(i-1, j-1), otherwise return 0.</code><br>
<a href="dsa/python/2D-DynamicProgramming/longest-common-substring1452.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Greedy</h4></summary>
<ul>
<li><b>🟧 <a href="https://leetcode.com/problems/maximum-subarray/" target="_blank">Maximum Subarray</a></b> <code>Initialize max to nums[0] and cur to 0. Iterate through nums, if (cur < 0), reset cur to 0, add num to cur and maintain the running max. Return max at the end</code><br>
<a href="dsa/python/Greedy/maximum-subarray.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/jump-game/" target="_blank">Jump Game</a></b> <code>Intialize goalpost to last index. Iterate through nums in reverse, for each i, check if (i + nums[i]) >= goalpost, if so move goalpost to i. Finally return goalpost == 0</code><br>
<a href="dsa/python/Greedy/jump-game.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/jump-game-ii/" target="_blank">Jump Game II</a></b> <code>Use Breadth-First Search (BFS) with a visited set for optimization. Add indexes within the jump range to the queue. When the last index is popped from the queue, return the current height (level in BFS).</code><br>
<a href="dsa/python/Greedy/jump-game-ii.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/gas-station/" target="_blank">Gas Station</a></b> <code>Check if sum(gas) < sum(cost) and return -1. Otherwise loop through gas mainitaining a running_total of remaining_gas. If it becomes < 0, reset running_total and set res to i + 1</code><br>
<a href="dsa/python/Greedy/gas-station.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/hand-of-straights/description/" target="_blank">Hand of Straights</a></b> <code>Create a counter for, and sort hand. For each n in hand, if n has a count in counter, we try to create a hand by iterating size of hand and decrementing count from counter. If counter does not have a particular value, we return False. Otherwise return True.</code><br>
<a href="dsa/python/Greedy/hand-of-straights.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/merge-triplets-to-form-target-triplet/" target="_blank">Merge Triplets to Form Target Triplet</a></b> <code>Create a res set, to hold the indexes of matched values from target. Iterate through triplets, and discard any, that have values > target. For the others, if we find a matching value, add its index to res. Finally return len(res) == 3</code><br>
<a href="dsa/python/Greedy/hand-of-straights.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/partition-labels/" target="_blank">Partition Labels</a></b> <code>Create a hashmap of last indexes of each character in s. Iterate through s, maintaining a running max of the highest last index in the window of crossed characters, if i == max_index, append i to res. Return res at the end</code><br>
<a href="dsa/python/Greedy/partition-labels.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/valid-parenthesis-string/" target="_blank">Valid Parenthesis String</a></b> <code></code><br>
<a href="dsa/python/Greedy/partition-labels.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Intervals</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/meeting-rooms/" target="_blank">Meeting Rooms</a></b> <code>Sort intervals by start time. Iterate from [1..len(intervals)], if (interval[i-1].end > interval[i].start) return False. Otherwise True</code><br>
<a href="dsa/python/Intervals/meeting-rooms.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/meeting-rooms-ii/" target="_blank">Meeting Rooms II</a></b> <code>Create 2 arrays of sorted start and end times, Iterate while s < len(intervals). if start[s] < end[e], increment count and s. else increment e and decrement count. Update rooms at the end of each iteration. Finally return rooms</code><br>
<a href="dsa/python/Intervals/meeting-rooms-ii.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/insert-interval/" target="_blank">Insert Interval</a></b> <code>Sort intervals. Add intervals to res, that end before newInterval starts(intervals[i][1] < newInterval[0]). Then, merge newInterval to reflect all overlapping intervals(intervals[i][0] <= newInterval[1]). Then, add any remaining intervals. Return res</code><br>
<a href="dsa/python/Intervals/insert-interval.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/merge-intervals/" target="_blank">Merge Intervals</a></b> <code>Sort intervals based on starts. Create result array with 1st element of interval. Iterate through intervals from index 1, if the end of last interval in res is >= start of current interval, then update the end of the interval in res to max(end of current, end of res[-1]), otherwise add current to res. Return res finally</code><br>
<a href="dsa/python/Intervals/merge-intervals.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/non-overlapping-intervals/" target="_blank">Non Overlapping Intervals</a></b> <code></code><br>
<a href="dsa/python/Intervals/non-overlapping-intervals.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/minimum-interval-to-include-each-query/" target="_blank">Minimum Interval to Include Each Query</a></b> <code></code><br>
<a href="">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/number-of-flowers-in-full-bloom/" target="_blank">Number of Flowers in Full Bloom</a></b> <code>Create arrays with (people, idx), start and end times. Heapify the start and end arrays. Loop through a sorted array of people, increment the count while start_time <= p, and decrement it when end_time < p. Assign count to res[i], then return the final res</code><br>
<a href="dsa/python/Intervals/number-of-flowers-in-full-bloom.py">python</a>
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