class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

def remove_duplicates(head):
    curr=head
    if head is None:
        return
    while curr!=None and curr.next!=None:
        if curr.data==curr.next.data:
            curr.next=curr.next.next
        else:
            curr=curr.next
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
l=[1,2,3,3,4,5,5]
for i in l:
    head=add_data_to_end(head,i)
print_list(head)
head=remove_duplicates(head)
print_list(head)