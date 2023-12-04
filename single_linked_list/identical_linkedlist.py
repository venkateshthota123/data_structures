class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

def identical_linked_list(head1,head2):
    if head1==None or head2==None:
        return
    curr1=head1
    curr2=head2
    count1=0
    count2=0
    while curr1!=None:
        count1+=1
        curr1=curr1.next
    while curr2!=None:
        count2+=1
        curr2=curr2.next
    if count1==count2:
        while curr1!=None and curr2!=None:
            if curr1.data ==curr2.data :
                curr1=curr1.next
                curr2=curr2.next
            else:
                return False
        return True
    else:
        return False




        
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
l2=[1,2,3,4]
for i in l2:
    head2=add_data_to_end(head2,i)
print_list(head1)
print_list(head2)

print(identical_linked_list(head1,head2))
