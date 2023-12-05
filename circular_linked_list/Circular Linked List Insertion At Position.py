#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def insertatfirst(head,data):
    temp=Node(data)
    temp.next=head.next
    head.next=temp
    head.data,temp.data=temp.data,head.data
    return head

def insertAtPosition(head,pos,data):
    temp=Node(data)
    if pos==1:
        head=insertatfirst(head,data)
        return head
    else:
        curr=head
        for i in range(pos-2):
            curr=curr.next
        temp.next=curr.next
        curr.next=temp
    return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def displayList(head):
    t=head
    while t.next!=head:
        print(t.data,end=' ')
        t=t.next
    print(t.data,end=' ')


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        pos,data=[int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        #making circular
        tail.next=ll.head

        insertAtPosition(ll.head,pos,data)
        displayList(ll.head)
        print()
# } Driver Code Ends