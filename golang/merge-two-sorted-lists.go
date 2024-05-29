package main

// https://medium.com/@jaydevchauhan2000/implementing-single-linked-list-in-golang-d6634ebb39cf

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

type LinkedList struct {
	head *ListNode
}

func (ll *LinkedList) append(data int) {
	newNode := &ListNode{Val: data, Next: nil}

	if ll.head == nil {
		ll.head = newNode
		return
	}

	current := ll.head
	for current.Next != nil {
		current = current.Next
	}

	current.Next = newNode
}

func (ll *LinkedList) prepend(data int) {
	if ll.head == nil {
		ll.head = &ListNode{Val: data, Next: nil}
		return
	}
	newNode := &ListNode{Val: data, Next: ll.head}
	ll.head = newNode
}

func (ll *LinkedList) insertAfterValue(value, data int) {
	// if ll.head == nil {
	// 	ll.head = &ListNode{Val: data, Next: nil}
	// 	return
	// }
	curr := ll.head
	for curr.Next != nil {
		if curr.Val == value {
			newNode := &ListNode{Val: data, Next: curr.Next}
			curr.Next = newNode
			return
		}
		curr = curr.Next
	}
	fmt.Printf("Cannot insert node, after value %d doesn't exist", value)
	fmt.Println()
}

func (ll LinkedList) display() {
	curr := ll.head
	for curr != nil {
		fmt.Printf("%d ->", curr.Val)
		curr = curr.Next
	}
	fmt.Println("nil")
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	result := &ListNode{}
	curr := result

	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			curr.Next = list1
			list1 = list1.Next
		} else {
			curr.Next = list2
			list2 = list2.Next
		}
		curr = curr.Next
	}
	if list1 == nil {
		curr.Next = list2
	}
	if list2 == nil {
		curr.Next = list1
	}
	return result.Next
}

func main() {
	ll := LinkedList{}
	for _, v := range []int{1, 2, 3, 4, 5} {
		ll.append(v)
	}
	ll.display()
}
