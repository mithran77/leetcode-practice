package main

import "fmt"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

// func reverseList(head *ListNode) *ListNode {

// }

func main() {
	var prev ListNode
	head := ListNode{1, nil}
	for _, v := range []int{2, 3, 4, 5} {
		prev.Next = &ListNode{v, nil}
	}

	fmt.Println(reverseList())
}
