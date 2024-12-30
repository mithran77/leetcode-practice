// https://www.educative.io/answers/singly-linked-list-in-go
package main

import "fmt"

type Node struct {
	data int
	next *Node
}

type LinkedList struct {
	head *Node
}

func NewSinglyLinkedList() *LinkedList {
	return &LinkedList{}
}

func (ll *LinkedList) Append(data int) {
	newNode := &Node{data: data, next: nil}

	if ll.head == nil {
		ll.head = newNode
		return
	}

	current := ll.head
	for current.next != nil {
		current = current.next
	}
	current.next = newNode
}

func (ll *LinkedList) Display() {
	current := ll.head
	for current != nil {
		fmt.Printf("%d ->", current.data)
		current = current.next
	}
	fmt.Println("nil")
}

func main() {
	ll := NewSinglyLinkedList()
	// Add elements to the linked list
	for _, v := range []int{1, 2, 3, 4, 5} {
		ll.Append(v)
	}

	// ll.Append(10)
	// ll.Append(20)
	// ll.Append(30)

	// Display the linked list
	fmt.Println("Linked List:")
	ll.Display()
}
