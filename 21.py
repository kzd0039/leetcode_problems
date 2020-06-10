class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1,l2):
    result = ListNode(0)
    point1 = l1
    point2 = l2
    point3 = result
    
    while  point1 and  point2:
        if point1.val < point2.val:
            point3.next = point1
            point1 = point1.next
        else:
            point3.next = point2
            point2 = point2.next
        point3 = point3.next

    if point1:
        point3.next = point1

    if point2:
        point3.next = point2

    return result.next

def main():
    root1 = ListNode(0)
    point1 = root1
    root2 = ListNode(0)
    point2 = root2
    lists1 = [1,2,4]
    lists2 = [1,3,4]
    for i in range(len(lists1)):
        point1.next = ListNode(lists1[i])
        point1 = point1.next
        point2.next = ListNode(lists2[i])
        point2 = point2.next

    ans = mergeTwoLists(root1.next,root2.next)
    while ans:
        print(ans.val)
        ans = ans.next

if __name__ == '__main__':
    main()