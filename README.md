# leet-code

<details>
<summary><h4>Arrays & Hashing</h4></summary>
<ul>
<li><b><a href="https://leetcode.com/problems/contains-duplicate/">Contains Duplicate</a></b> <code>Add chars to HashSet while iterating. If already present, return True</code><br>
<a href="https://github.com/mithran77/leetcode-practice/blob/main/python/ArraysHashing/contains-duplicate.py">python</a> | 
<a href="https://github.com/mithran77/leetcode-practice/blob/main/golang/ArraysHashing/contains-duplicate.go">go</a>
</li>
<li><b><a href="https://leetcode.com/problems/valid-anagram/">Valid Anagram</a></b> <code>Create char_count HashMap for s, then subtract counts from HashMap while looping through t</code><br>
<a href="https://github.com/mithran77/leetcode-practice/blob/main/python/ArraysHashing/valid-anagram.py">python</a> |
<a href="https://github.com/mithran77/leetcode-practice/blob/main/golang/ArraysHashing/valid-anagram.go">go</a> 
</li>
<li><b><a href="https://leetcode.com/problems/two-sum/description/">Two Sum</a></b> <code>Use HashMap to store required number with index of computed number, If required value is found, return a list of correspomding indexes</code><br>
<a href="https://github.com/mithran77/leetcode-practice/blob/main/python/ArraysHashing/two-sum.py">python</a> |
<a href="https://github.com/mithran77/leetcode-practice/blob/main/golang/ArraysHashing/two-sum.go">go</a> 
</li>
<li><b><a href="https://leetcode.com/problems/group-anagrams/description/">Group Anagrams</a></b> <code>Use a HashMap with char_count[26] tuples as keys, appending words that match the count. Finally, return the HashMap's values.</code><br>
<a href="https://github.com/mithran77/leetcode-practice/blob/main/python/ArraysHashing/group-anagrams.py">python</a> |
<a href="https://github.com/mithran77/leetcode-practice/blob/main/golang/ArraysHashing/group-anagrams.go">go</a> 
</li>
<li><b><a href="https://leetcode.com/problems/top-k-frequent-elements/description/">Top K Frequent Elements</a></b> <code>First create a num_count dictionary, then an ordered map of counts with corresponding numbers (List[List]). Iterate in reverse, appending numbers to the result, and return when enough values are collected.</code><br>
<a href="https://github.com/mithran77/leetcode-practice/blob/main/python/ArraysHashing/top-k-frequent-elements.py">python</a> |
<a href="https://github.com/mithran77/leetcode-practice/blob/main/golang/ArraysHashing/top-k-frequent-elements.go">go</a> 
</li>
<li><b><a href="https://neetcode.io/problems/string-encode-and-decode">Encode and Decode Strings</a></b> <code>Use the format < len#word > for encoding. To decode, use two pointers and two while loops to read the length, then append the word slice to the result</code><br>
<a href="https://github.com/mithran77/leetcode-practice/blob/main/python/ArraysHashing/encode-and-decode-strings.py">python</a>
</li>
<li><b><a href="https://leetcode.com/problems/product-of-array-except-self/description/">Product of Array Except Self</a></b> <code>Initialize prod = 1. Loop L-R. First update ans array, ans[i] *= prod. Then update prod, prod *= nums[i], to use in the next iteration. Repeat the process R-L.</code><br>
<a href="https://github.com/mithran77/leetcode-practice/blob/main/python/ArraysHashing/product-of-array-except-self.py">python</a>
</li>
<li><b><a href="https://leetcode.com/problems/product-of-array-except-self/description/">Product of Array Except Self</a></b> <code>Initialize prod = 1. Loop L-R. First update ans array, ans[i] *= prod. Then update prod, prod *= nums[i], to use in the next iteration. Repeat the process R-L.</code><br>
<a href="https://github.com/mithran77/leetcode-practice/blob/main/python/ArraysHashing/product-of-array-except-self.py">python</a>
</li>
<li><b><a href="https://leetcode.com/problems/longest-consecutive-sequence/">Longest Consecutive Sequence</a></b> <code>Convert nums to a set. For each number, check if num-1 is present (indicating the start of a sequence). If yes, iteratively check until there are no more num+1 elements in the set. Then update the longest sequence length.</code><br>
<a href="https://github.com/mithran77/leetcode-practice/blob/main/python/ArraysHashing/product-of-array-except-self.py">python</a>
</li>
</ul>
</details>

<details>
<summary><h4>Two Pointers</h4></summary>
<ul>
<li><b><a href="https://leetcode.com/problems/valid-palindrome/description/">Valid Palindrome</a></b> <code>Add chars to HashSet while iterating. If already present, return True</code><br>
<a href="python/TwoPointer/valid-palindrome.py">python</a> | 
<a href="golang/TwoPointer/valid-palindrome.go">go</a>
</li>
</ul>
</details>

<details>
<summary><h4>Sliding Window</h4></summary>
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