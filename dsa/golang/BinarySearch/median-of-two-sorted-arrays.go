/*
	4. Median of Two Sorted Arrays

	Given two sorted arrays nums1 and nums2 of size m
    and n respectively, return the median of the two
    sorted arrays.

	The overall run time complexity should be O(log (m+n)).

	Example 1:
	Input: nums1 = [1,3], nums2 = [2]
	Output: 2.00000
	Explanation: merged array = [1,2,3] and median is 2.

	Example 2:
	Input: nums1 = [1,2], nums2 = [3,4]
	Output: 2.50000
	Explanation: merged array = [1,2,3,4] and median is
    (2 + 3) / 2 = 2.5.

	Constraints:
	nums1.length == m
	nums2.length == n
	0 <= m <= 1000
	0 <= n <= 1000
	1 <= m + n <= 2000
	-106 <= nums1[i], nums2[i] <= 106

*/

// Brute Force
// func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
//     merged := []int{}
//     a, b := nums1, nums2

//     i, j := 0, 0
//     for i < len(a) && j < len(b) {
//         if a[i] < b[j] {
//             merged = append(merged, a[i])
//             i++
//         } else {
//             merged = append(merged, b[j])
//             j++
//         }
//     }

//     if i < len(a) {
//         merged = append(merged, a[i:]...)
//     }

//     if j < len(b) {
//         merged = append(merged, b[j:]...)
//     }

//     mLen := len(merged)
//     var median float64
//     if mLen % 2 == 1 {
//         median = float64(merged[(mLen/2)])
//     } else {
//         m1, m2 := merged[(mLen/2)-1], merged[(mLen/2)]
//         median = float64(m1 + m2) / 2
//     }

//     return median
// }

// BF Optimized
// func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
//     merged := []int{}
//     a, b := nums1, nums2
//     full := len(nums1) + len(nums2)
//     half := full / 2

//     i, j := 0, 0
//     for len(merged) <= half {
//         if i < len(a) && (j >= len(b) || a[i] < b[j]) {
//             merged = append(merged, a[i])
//             i++
//         } else {
//             merged = append(merged, b[j])
//             j++
//         }
//     }

//     var median float64
//     if full % 2 == 1 {
//         median = float64(merged[(half)])
//     } else {
//         m1, m2 := merged[(half)-1], merged[(half)]
//         median = float64(m1 + m2) / 2
//     }

//     return median
// }


// func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
//     a, b := nums1, nums2
//     full := len(a) + len(b)
//     half := full / 2

//     for i := 0; i <= len(a) && i <= half; i++ {
//         j := half - i
//         if j < 0 || j > len(b) {
//             continue
//         }

//         aLeft, aRight := math.MinInt, math.MaxInt
//         if i > 0 {
//             aLeft = a[i-1]
//         }
//         if i < len(a) {
//             aRight = a[i]
//         }

//         bLeft, bRight := math.MinInt, math.MaxInt
//         if j > 0 {
//             bLeft = b[j-1]
//         }
//         if j < len(b) {
//             bRight = b[j]
//         }

//         if aLeft <= bRight && bLeft <= aRight {
//             if full%2 == 1 {
//                 return float64(min(aRight, bRight))
//             }
//             return float64(max(aLeft, bLeft)+min(aRight, bRight)) / 2
//         }
//     }

//     return 0
// }


func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    a, b := nums1, nums2
    if len(b) < len(a) {
        a, b = b, a
    }

    full := len(a) + len(b)
    half := full / 2

    l, r := -1, len(a) + 1
    for l + 1 != r {

        i := l + (r - l) / 2
        j := half - i

        aLeft, aRight := math.MinInt, math.MaxInt
        if i > 0 {
            aLeft = a[i-1]
        }
        if i < len(a) {
            aRight = a[i]
        }

        bLeft, bRight := math.MinInt, math.MaxInt
        if j > 0 {
            bLeft = b[j-1]
        }
        if j < len(b) {
            bRight = b[j]
        }

        if aLeft <= bRight && bLeft <= aRight {
            if full % 2 == 1 {
                return float64(min(aRight, bRight))
            }

            return float64(max(aLeft, bLeft) + min(aRight, bRight)) / 2

        } else if aLeft > bRight {
            r = i // too far right, pull i back
        } else {
            l = i // too far left, push i forward
        }
    }

    return 0
}

func main() {
	fmt.Println(findMedianSortedArrays([]int{1, 3}, []int{2}))
	fmt.Println(findMedianSortedArrays([]int{1, 2}, []int{3, 4}))
}