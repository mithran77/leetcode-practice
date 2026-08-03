/*
	875. Koko Eating Bananas

	Koko loves to eat bananas. There are n piles of bananas, the ith pile has
	piles[i] bananas. The guards have gone and will come back in h hours.

	Koko can decide her bananas-per-hour eating speed of k. Each hour, she
	chooses some pile of bananas and eats k bananas from that pile.
	If the pile has less than k bananas, she eats all of them instead and will
	not eat any more bananas during this hour.

	Koko likes to eat slowly but still wants to finish eating all the bananas
	before the guards return.

	Return the minimum integer k such that she can eat all the bananas within
	h hours.

	Example 1:
	Input: piles = [3,6,7,11], h = 8
	Output: 4

	Example 2:
	Input: piles = [30,11,23,4,20], h = 5
	Output: 30

	Example 3:
	Input: piles = [30,11,23,4,20], h = 6
	Output: 23

	Constraints:
	1 <= piles.length <= 104
	piles.length <= h <= 109
	1 <= piles[i] <= 109

*/

// func minEatingSpeed(piles []int, h int) int {
//     l, r := 0, slices.Max(piles) + 1

//     for (l + 1) != r {
//         m := l + (r - l) / 2

//         time := 0
//         for _, p := range piles {
//             time += int(math.Ceil(float64(p) / float64(m)))
//         }

//         if time > h {
//             l = m
//         } else {
//             r = m
//         }
//     }

//     return r

// }


func minEatingSpeed(piles []int, h int) int {

    l, r := 0, slices.Max(piles) + 1

    for l + 1 != r {
        m := l + (r - l) / 2

        if canEat(m, piles, h) {
            r = m
        } else {
            l = m
        }
    }

    return r

}

func canEat(m int, piles []int, h int) bool {
    tick := 0
    for _, p := range piles {
        tick += p / m
        if p % m > 0 {
            tick++
        }
    }

    return tick <= h
}

func main() {
	fmt.Println(search([]int{3,6,7,11}, 8))
	fmt.Println(search([]int{30,11,23,4,20}, 5))
	fmt.Println(search([]int{30,11,23,4,20}, 6))
}
