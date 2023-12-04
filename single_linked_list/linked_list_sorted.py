class Node:
    def __init__(self, data):
        self.data = data
        self.next=None


def sorted_list(head):
    curr=head
    if head==None:
        return
    while curr.next!=None:
        if curr.data<=curr.next.data:
            curr=curr.next
        else:
            return False
    return True

        
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
l=[1,2,3,9,5]
for i in l:
    head=add_data_to_end(head,i)
print_list(head)
if sorted_list(head):
    print("sorted")
else:
    print("Not sorted")