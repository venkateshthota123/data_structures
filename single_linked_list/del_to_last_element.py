class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

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
def del_to_last(head):
    curr=head
    if head == None:
        return 
    else:
        while curr.next.next!=None:
            curr=curr.next
        curr.next=curr.next.next
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
del_to_last(head)
print_list(head)
