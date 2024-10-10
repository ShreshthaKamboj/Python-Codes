# Creating a Node which stores the data of the current node 
# and the pointer to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating a Linked List structure to implement Linked List Operations
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Method to append new node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    # Method to display the linked list   
    def display(self):
        current = self.head
        while current:
            print(current.data, end = "->")
            current = current.next
        print("None")
    
    # Method to reverse the current linled list 
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    # Method to find the middle element of the linked list
    def find_middle_element(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next
        return slow.data
    
    # Method to create a cycle 
    def create_cycle(self, pos):
        if pos == -1:
            return
        cycle_start = self.head
        last = self.head
        for i in range(pos):
            cycle_start = cycle_start.next
        while last.next:
            last =last.next
        last.next = cycle_start
    
    # Method to check for cycle in a linked list
    def check_cycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True
        return False
 
# Method to add two linked list    
def add_two_linkedlist(list1, list2):
    dummy = Node(0)
    p = list1
    q = list2
    current = dummy
    carry = 0
    while p is not None or q is not None:
        x = p.data if p is not None else 0
        y = q.data if q is not None else 0
        sum = carry + x + y
        carry = sum // 10
        current.next = Node(sum % 10)
        current = current.next
        if p is not None:
            p = p.next
        if q is not None:
            q = q.next
    if carry > 0:
        current.next = Node(carry)
    return dummy.next

# Method to Merge two sorted list
def merge_linkedlists(list1, list2):
    dummy = Node(0)
    p = list1
    q = list2
    current = dummy
    while p is not None and q is not None:
        if p.data <= q.data:
            current.next = p
            p = p.next
        else:
            current.next = q
            q = q.next
        current = current.next
    if p is not None:
        current.next = p
    if q is not None:
        current.next = q
    return dummy.next
 
list1 = LinkedList()
list1.append(2)
list1.append(4)
list1.append(6)
list1.display()
      
list2 = LinkedList()
list2.append(3)
list2.append(5)
list2.append(7)
list2.display()

result = add_two_linkedlist(list1.head, list2.head)
print("Result:")
res_list = LinkedList()
res_list.head = result
res_list.display()

merged = merge_linkedlists(list1.head, list2.head)
print("Merged:")
merged_list = LinkedList()
merged_list.head = merged
merged_list.display()

print("Middle Element is", list1.find_middle_element())

res_list.create_cycle(2)
if res_list.check_cycle():
    print("Cycle Detected!")
else:
    print("No Cycle Detected")
    