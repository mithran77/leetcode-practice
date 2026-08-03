/*

    155. Min Stack

    Design a stack that supports push, pop, top, and
    retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto
    the stack.
    void pop() removes the element on the top of
    the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time
    complexity for each function.

    Example 1:

    Input
    ["MinStack","push","push","push","getMin",
    "pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2

    Constraints:

    -231 <= val <= 231 - 1
    Methods pop, top and getMin operations will always
    be called on non-empty stacks. At most 3 * 104
    calls will be made to push, pop, top, and getMin.

*/

type MinStack struct {  // S: O(2n) = O(n)
    values []int
    mins []int
}


func Constructor() MinStack {
    return MinStack{
        values: []int{},
        mins: []int{},
    }
}


func (ms *MinStack) Push(value int)  {  // T: O(1)
    ms.values = append(ms.values, value)
    minVal := value
    if len(ms.mins) > 0 {
        minVal = min(ms.mins[len(ms.mins)-1], value)
    }
    ms.mins = append(ms.mins, minVal)
}


func (ms *MinStack) Pop()  {    // T: O(1)
    sLen := len(ms.values)

    ms.values = ms.values[:sLen-1]
    ms.mins = ms.mins[:sLen-1]
}


func (ms *MinStack) Top() int { // T: O(1)
    return ms.values[len(ms.values)-1]
}


func (ms *MinStack) GetMin() int {  // T: O(1)
    return ms.mins[len(ms.mins)-1]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(value);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */