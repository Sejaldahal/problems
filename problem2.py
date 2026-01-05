 # ADD two numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution (object):
    def addtwonumbers(self,l1,l2):
        dummy=ListNode(0)
        current=dummy
        carry =0
        while l1 or l2 or carry:
            val1 =l1.val if l1 else 0
            val2=l2.val if l2 else 0
            total=val1+val2+carry
            carry=total//10
            current.next=ListNode(total%10)
            current=current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next


def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

if __name__ == "__main__":
    l1_values = [2, 4, 3]
    l2_values = [5, 6, 4]
    l1 = build_linked_list(l1_values)
    l2 = build_linked_list(l2_values)
    result = Solution().addtwonumbers(l1, l2)
    
    # Print the result linked list
    while result:
        print(result.val, end=" -> " if result.next else "")
        result = result.next

''' In this code, initially two linkedlist l1 and l2 are created using the build_linked_list function.
Then the addtwonumbers method of the Solution class is called with l1 and l2 as arguments.
in build linked list function we create a dummy node which initally points to 0 and then we iterate for each value creting a newnodeand linking it to the current node for both linked lists.
in the addtwonumbers method we create a dummy node to help build the result linked list. We also maintain a carry variable to handle sums greater than 9.
We iterate through both linked listsuntil all nodes are checked and there is no carry left.
while l1,l2 or carry has values we take value else we keep it 0 and then find the sum and update carry for next iteration.
we create a newnode linking to current node.
iterate all nodes till l1,l2 and carry are empty.
return dummy.next which points to the head of the resultant linked list.
the output is in reverse order representing the sum of the two numbers.
'''
