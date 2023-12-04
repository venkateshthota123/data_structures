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
def add_to_pos(head,data,pos):
    curr=head
    temp=Node(data)
    if head==None:
        head=temp
    elif pos==1:
        temp.next=head
        return temp
    else:
        for i in range(pos-2):
            curr=curr.next
        temp.next=curr.next
        curr.next=temp
    return head
def print_list(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
# Testing the function
head=None
l=[1,2,3,4,5]
for i in l:
    head=add_data_to_end(head,i)
head=add_to_pos(head,6,3)
print_list(head)


