# leet-code

<details>
<summary><h4>Arrays & Hashing</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/contains-duplicate/">Contains Duplicate</a></b> <code>Add chars to HashSet while iterating. If already present, return True</code><br>
<a href="python/ArraysHashing/contains-duplicate.py">python</a> | 
<a href="golang/ArraysHashing/contains-duplicate.go">go</a>
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/valid-anagram/">Valid Anagram</a></b> <code>Create char_count HashMap for s, then subtract counts from HashMap while looping through t</code><br>
<a href="python/ArraysHashing/valid-anagram.py">python</a> |
<a href="golang/ArraysHashing/valid-anagram.go">go</a> 
</li>
<li><b>🟩 <a href="https://leetcode.com/problems/two-sum/description/">Two Sum</a></b> <code>Use HashMap to store required number with index of computed number, If required value is found, return a list of correspomding indexes</code><br>
<a href="python/ArraysHashing/two-sum.py">python</a> |
<a href="golang/ArraysHashing/two-sum.go">go</a> 
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/group-anagrams/description/">Group Anagrams</a></b> <code>Use a HashMap with char_count[26] tuples as keys, appending words that match the count. Finally, return the HashMap's values.</code><br>
<a href="python/ArraysHashing/group-anagrams.py">python</a> |
<a href="golang/ArraysHashing/group-anagrams.go">go</a> 
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/top-k-frequent-elements/description/">Top K Frequent Elements</a></b> <code>First create a num_count dictionary, then an ordered map of counts with corresponding numbers (List[List]). Iterate in reverse, appending numbers to the result, and return when enough values are collected.</code><br>
<a href="python/ArraysHashing/top-k-frequent-elements.py">python</a> |
<a href="golang/ArraysHashing/top-k-frequent-elements.go">go</a> 
</li>
<li><b>🟧 <a href="https://neetcode.io/problems/string-encode-and-decode">Encode and Decode Strings</a></b> <code>Use the format < len#word > for encoding. To decode, use two pointers and two while loops to read the length, then append the word slice to the result</code><br>
<a href="python/ArraysHashing/encode-and-decode-strings.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/product-of-array-except-self/description/">Product of Array Except Self</a></b> <code>Initialize prod = 1. Loop L-R. First update ans array, ans[i] *= prod. Then update prod, prod *= nums[i], to use in the next iteration. Repeat the process R-L.</code><br>
<a href="python/ArraysHashing/product-of-array-except-self.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-consecutive-sequence/">Longest Consecutive Sequence</a></b> <code>Convert nums to a set. For each number, check if num-1 is present (indicating the start of a sequence). If yes, iteratively check until there are no more num+1 elements in the set. Then update the longest sequence length.</code><br>
<a href="python/ArraysHashing/product-of-array-except-self.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Two Pointers</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/valid-palindrome/description/">Valid Palindrome</a></b> <code>Iterate with L & R pointers, skip invalid characters with ASCII range checks, compare in lowercase, finally return True if no mismatches found</code><br>
<a href="python/TwoPointer/valid-palindrome.py">python</a> | 
<a href="golang/TwoPointer/valid-palindrome.go">go</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/">Two Sum II</a></b> <code>Iterate with L & R pointers, adjust pointers based on cur_sum relative to target, and return indices if they match</code><br>
<a href="python/TwoPointer/two-sum-ii-input-array-is-sorted.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/3sum/description/">3Sum</a></b> <code>Sort the array and iterate through nums, skipping duplicates. For each nums[i], set target = -nums[i] and iterate using L & R pointers to find pairs that sum to the target. Add indices on a match, and skip duplicates for L followed by R pointers</code><br>
<a href="python/TwoPointer/3sum.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/container-with-most-water/description/">Container With Most Water</a></b> <code>Iterate with L & R pointers, calculate the current area and update max_area if larger, then move pointer with the lower height</code><br>
<a href="python/TwoPointer/container-with-most-water.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Sliding Window</h4></summary>
<ul>
<li><b>🟩 <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/">Best Time to Buy and Sell Stock</a></b> <code>Set buy to prices[0], iterate through prices calculating profit, and update if larger</code><br>
<a href="python/SlidingWindow/best-time-to-buy-and-sell-stock.py">python</a> | 
<a href="golang/SlidingWindow/best-time-to-buy-and-sell-stock.go">go</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/description/">Longest Substring Without Repeating Characters</a></b> <code>Initialize L pointer to 0. Iterate over s, adding characters to a charSet. If duplicate is found, remove characters from left until duplicate is gone. Continuously update longest substring and return it at end</code><br>
<a href="python/SlidingWindow/longest-substring-without-repeating-characters.py">python</a>
</li>
<li><b>🟧 <a href="https://leetcode.com/problems/longest-repeating-character-replacement/description/">Longest Repeating Character Replacement</a></b> <code></code><br>
<a href="python/SlidingWindow/longest-repeating-character-replacement.py">python</a>
</li>
<li><b>🟥 <a href="https://leetcode.com/problems/minimum-window-substring/description/">Minimum Window Substring</a></b> <code></code><br>
<a href="#">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Stack</h4></summary>
</details>

<details>
<summary><h4>Binary Search</h4></summary>
</details>

<details>
<summary><h4>Linked List</h4></summary>
</details>

<details>
<summary><h4>Trees</h4></summary>
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