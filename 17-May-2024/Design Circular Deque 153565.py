# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.k=k
        self.qu=[]
        l=0
        r=0
        

    def insertFront(self, value: int) -> bool:
        if !self.isFull():
            self.qu.insert(0,value)

        l-=1
        
            

        

    def insertLast(self, value: int) -> bool:
        if len(self.qu)<k:
            self.qu.append(value)
        

    def deleteFront(self) -> bool:
        if len(self.qu)>0:
            self.qu.pop(0)
        

    def deleteLast(self) -> bool:
        if len(self.qu)>0:
            self.qu.pop(0)
        

    def getFront(self) -> int:
        self.qu[0]
        

    def getRear(self) -> int:
        self.qu[-1]
        

    def isEmpty(self) -> bool:
        return len(self.qu)==0
        

    def isFull(self) -> bool:
        return len(self.qu)==self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()