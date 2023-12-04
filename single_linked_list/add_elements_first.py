class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

def add_data_to_first(head,data):
    temp= Node(data)
    curr=head
    if head==None:
        return temp
    else:
        temp.next=head
    return temp
    
def print_list(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
# Testing the function
head=None
l=[1,2,3,4,5]
for i in l:
    head=add_data_to_first(head,i)
print_list(head)
