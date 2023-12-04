class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
def count(head):
    curr=head
    if head is None:
        return 
    count=0
    while curr!=None:
        count+=1
        curr=curr.next
    return count
        
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
print("Count of nodes",count(head))