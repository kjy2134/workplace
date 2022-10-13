class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack :
    def __init__(self):
        self.head = None

    def push(self,data):
        if self.head is None: #stack이 비어있을 때
            self.head = node(data)

        else:
            new_node= node(data) #stack이 비어있지 않을  ##new_node는 node클래스의 객체로 node클래스의 data값을 저장
            new_node.next = self.head #node클래스의 next값에  앞서 저정된 node클래스 data값을 할당
            self.head = new_node #stack의 head값에 나중에 들어온 node클래스의 data를 저장
        
    def pop(self):
        if self.head is None: #stack이 비어있을 때
            return None

        else :#stack에 데이터가 있을떄
            popped = (self.head).data #head에 저장된 node클래스의 data를 할당. data는 나중에 들어온 값이 할당되어있고, 이를 따로 저장해둠
            self.head = self.head.next  #먼저 들어온 data를 head변수에 저장
            return popped #나중 값을 return.  

s = stack()

s.push("a") #["a"] , s.head = "a"
s.push("b") #["a","b"] , s.data = "b", s.next = "a" : next에 나중값이 할당 됨
s.push("c") #["a","b","c"]
s.push("d") #.
s.push("e") #.
s.push("f") #.

print(s.pop()) #가장 나중에 들어온 데이터가 가장 먼저 나옴 후입선출