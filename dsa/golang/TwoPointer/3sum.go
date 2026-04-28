/*
# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and
# nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []


# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
*/

func threeSum(nums []int) [][]int {
    res := [][]int{}

    slices.Sort(nums)
    for i := range nums {
        if i > 0 && nums[i] == nums[i-1] {
            continue
        }

        l, r := i + 1, len(nums) - 1

        for l < r {
            sum := nums[i] + nums[l] + nums[r]
            if sum < 0 {
                l++
            } else if sum > 0 {
                r--
            } else {
                res = append(res, []int{nums[i], nums[l], nums[r]})
                l++
                r--

                for l < r && nums[l] == nums[l-1] {
                    l++
                }
                for l < r && nums[r] == nums[r+1] {
                    r--
                }
            }
        }
    }

    return res
}


func main() {
    fmt.Println(threeSum([]int{-1,0,1,2,-1,-4}))
    fmt.Println(threeSum([]int{0,1,1}))
    fmt.Println(threeSum([]int{0,0,0}))
}

