class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

def insert_to_begin(head,data):
    temp=Node(data)
    temp.next=head
    return temp
def insert_to_end(head,data):
    temp=Node(data)
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=temp
    temp.next=None
    return head
def insert_to_pos(head,data,count):
    temp=Node(data)
    curr=head
    for i in range(count-2):
        curr=curr.next
    temp.next=curr.next
    curr.next=temp
    return head

def  insert_to_sorted(head,data):
    curr=head
    prev=head
    count=0
    c=0
    while prev!=None:
        c+=1
        prev=prev.next
    while curr!=None:
        if curr.data<data:
            curr=curr.next
            count+=1
    if c==count:
        insert_to_end(head,data)
    elif count==0:
       head= insert_to_begin(head,data)
    else:
        insert_to_pos(head,data,count)
    return head


        
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
head=insert_to_sorted(head,10)
print_list(head)
