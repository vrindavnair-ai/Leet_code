from collections import deque
class MyStack:

    def __init__(self):
        #queue object
        self.q = deque()

    def push(self, x: int) -> None:
        #adding new element
        self.q.append(x)

        #rotating the queue. '_' beacause the iterator is not used inside the loop
        #q = [1, 2, 3] -> popleft → 1 → append → [2, 3, 1] -> popleft → 2 → append → [3, 1, 2]
        for _ in range(len(self.q)-1):
            x = self.q.popleft()
            self.q.append(x)
        

    def pop(self) -> int:
        #last element is at the front after rotation
        return self.q.popleft()
        

    def top(self) -> int:
        #front element is at 0 index
        return self.q[0]

    def empty(self) -> bool:
        #to check if it is empty
        return len(self.q) ==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
"""["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]
Only the last 3 functions returns elements. that's why others are null
"""