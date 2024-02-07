package main

import "fmt"

func maxProfit(prices []int) int {
	l, r, maxP := 0, 1, 0

	for r < len(prices) {

		if prices[r] < prices[l] {
			l = r
		}
		if (prices[r] - prices[l]) > maxP {
			maxP = prices[r] - prices[l]
		}
		r++
	}
	return maxP
}

func main() {
	fmt.Println(maxProfit([]int{7, 1, 5, 3, 6, 4}))
}
