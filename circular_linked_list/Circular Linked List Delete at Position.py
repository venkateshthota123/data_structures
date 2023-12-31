#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def delete_first(head):
    curr=head
    while curr.next!=head:
        curr=curr.next
    curr.next=curr.next.next
    return head.next
def deleteAtPosition(head,pos):
    if head==None:
        return 
    if pos==1:
        head=delete_first(head)
        return head
    else:
        curr=head
        for i in range(pos-2):
            curr=curr.next
        curr.next=curr.next.next
    return head



#{ 
 # Driver Code Starts
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
        pos=int(input())

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        #making circular
        tail.next=ll.head

        resHead=deleteAtPosition(ll.head,pos)
        displayList(resHead)
        print()
# } Driver Code Ends