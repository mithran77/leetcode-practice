/*
# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the
# longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
*/

func longestConsecutive(nums []int) int {
    set := make(map[int]struct{})
    var max_seq int

    for _,n := range nums{
        set[n] = struct{}{}
    }

    for n := range set {
        if _, exists := set[n-1]; !exists {
            seq_len := 1
            for {
                if _, exists := set[n+seq_len]; !exists {
                    break
                }
                seq_len++
            }
            if seq_len > max_seq {
                max_seq = seq_len
            }
        }
    }

    return max_seq
}

func main() {
    fmt.Println(longestConsecutive([]int{100,4,200,1,3,2}))
    fmt.Println(longestConsecutive([]int{0,3,7,2,5,8,4,6,0,1}))
    fmt.Println(longestConsecutive([]int{1,0,1,2}))
}


