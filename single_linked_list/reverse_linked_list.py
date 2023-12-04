class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

def reverse_linkedlist(head):
    if head==None:
        return head
    elif head.next==None:
        return head
    curr=head
    prev=None
    while curr!=None:
        next_1=curr.next
        curr.next=prev
        prev=curr
        curr=next_1
    return prev


        
def add_data_to_end(head,data):
    temp= Node(data)
    curr=head
    if curr==None:
        return temp
    else:
        while curr.next!=None:
            curr=curr.next
        curr.next=temp
    return head
def print_list(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()
# Testing the function
head=None
l=[1,2,3,4,5]
for i in l:
    head=add_data_to_end(head,i)
print_list(head)
head=reverse_linkedlist(head)
print_list(head)