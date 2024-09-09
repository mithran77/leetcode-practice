package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

type LinkedList struct {
	Head *ListNode
}

func (ll *LinkedList) Append(num int) {
	newNode := &ListNode{Val: num, Next: nil}
	if ll.Head == nil {
		ll.Head = newNode
		return
	}
	curr := ll.Head
	for curr.Next != nil {
		curr = curr.Next
	}
	curr.Next = newNode
}

func (ll *LinkedList) Prepend(num int) {
	newNode := &ListNode{Val: num, Next: ll.Head}
	if ll.Head == nil {
		ll.Head = newNode
	}
	newNode.Next = ll.Head
	ll.Head = newNode
}

func (ll *LinkedList) Display() {
	curr := ll.Head
	for curr != nil {
		fmt.Printf("%d ->", curr.Val)
		curr = curr.Next
	}
	fmt.Println("nil")
}

func hasCycle(head *ListNode) bool {
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if fast == slow {
			return true
		}
	}
	return false
}

func main() {
	ll := &LinkedList{}
	for _, v := range []int{3, 2, 0, -4} {
		ll.Append(v)
	}
	// for _, v := range []int{1, 2} {
	// 	ll.Prepend(v)
	// }
	ll.Display()
	fmt.Println(hasCycle(ll.Head))
}
