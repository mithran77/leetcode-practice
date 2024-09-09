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

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode = nil
	curr := head
	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}
	return prev
}

func createLinkedList(nums []int) *ListNode {
	head := &ListNode{nums[0], nil}
	curr := head
	for _, v := range nums[1:] {
		curr.Next = &ListNode{v, nil}
		curr = curr.Next
	}
	return head
}

func printList(head *ListNode) {
	curr := head
	for curr != nil {
		fmt.Printf("%d -> ", curr.Val)
		curr = curr.Next
	}
	fmt.Println("nil")
}

func main() {
	head := createLinkedList([]int{1, 2, 3, 4, 5})
	// printList(head)
	printList(reverseList(head))
}
