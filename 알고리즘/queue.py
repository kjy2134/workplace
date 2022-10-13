


class node:
    def __init_(self,data):
        self.data = data
        self.next = None

#queue 만들기
class queue :
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isempty(self):
        if self.head in None:
            return True
        
        else:
            return False
        
    def enqueue(self,data):
        #queue가 비어있을 때

        if self.tail is None:
            self.head = self.tail = node(data)

        
        #queue가 비어있지 않을 때
        else:
            #새로운 node를 생성하여 뒤에 붙임
            self.tail.next = node(data)
            #tail 위치 조정
            self.tail = self.tail.next

    def dequeue(self):

        if self.head is None: #queue가 비어있음
            return None
        else :
            dequeue_data = self.head.data
            self.head - self.head.next
            return dequeue_data


q = queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue())
print(q.dequeue())