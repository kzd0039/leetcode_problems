class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    num = 1
    tem = head
    while tem.next != None:
        tem = tem.next
        num += 1
    if num ==1:
        return None
    
    if num == n:
        dummy.next = dummy.next.next
        return dummy.next
    
    count = 1
    tem = head
    while count < num - n:
        tem =  tem.next
        count += 1
        
    if tem.next.next:
        tem.next = tem.next.next
    else:
        tem.next = None
    
    return dummy.next

def main():
    root = ListNode(0)
    point = root
    lists = [1,2,3,4,5]
    for num in lists:
        point.next = ListNode(num)
        point = point.next
    n = 2
    ans = removeNthFromEnd(root.next,n)
    while ans:
        print(ans.val)
        ans = ans.next

if __name__ == '__main__':
    main()