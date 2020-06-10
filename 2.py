class ListNode(object):
     def __init__(self, x=None):
        self.val = x
        self.next = None

         

def main():
    l1=ListNode(2)
    l1.next=ListNode(4)
    l1.next.next=ListNode(3)
    l2=ListNode(5)
    l2.next=ListNode(6)
    l2.next.next=ListNode(4)


if __name__=='__main__':
    main()
