class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

def join_linked_list(head1,head2):
    curr=head1
    while curr.next!=None:
        curr=curr.next
    curr.next=head2
    return head1




        
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
head1=None
head2=None
l1=[1,2,3,4,5]
for i in l1:
    head1=add_data_to_end(head1,i)
l2=[6,7,8,9,10]
for i in l2:
    head2=add_data_to_end(head2,i)
print_list(head1)
print_list(head2)

head3=join_linked_list(head1,head2)
print_list(head3)