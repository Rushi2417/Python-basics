class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head = None:
            print("LL is empty")
            return
        itr = self.head
        ll = ''
        while itr:
            if itr.next:
                ll = ll + str(itr.data) + "--> "
            else:
                str(itr.data)
        print(ll)

    def getlenth(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insertAtBegin(self, data):
        node = Node(data, self.head)
        self.head = node

