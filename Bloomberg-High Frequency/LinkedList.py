def AddTwoNumber(l1, l2):

    if not l1 and not l2:
        return None

    ans = Node()
    carr, val = divmod((l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
    ans.val = val
    
    if carr > 0:
        if l1.next:
            l1.next.val += 1
        else:
            l1.next = Node(carr)
    
    ans.next = AddTwoNumber((l1.next if l1 else None), (l2.next if l2 else None))
    return ans


def MergeTwoSortedList(l1, l2):
    if not l1 or not l2:
        return l1 or l2

    if l1.val < l2.val:
        l1.next = MergeTwoSortedList(l1.next, l2)
        return l1
    else:
        l2.next = MergeTwoSortedList(l1, l2.next)
        return l2


def ReverseLinkedList(head):
    if not head:
        return head

    ans = Node(head.val)
    node = head
    while node.next:
        node = node.next
        tmp = Node(node.val)
        tmp.next = ans
        ans = tmp
    return ans


def ReverseLinkedListII(head, m, n):
    if m == n:
        return head
    if not head:
        return head

    curr = head
    prev = None

    i = 0
    while curr and i < m-1:
        prev = curr
        curr = curr.next
        i += 1
    
    first = prev
    last = curr

    i = 0
    nextNode = None
    while curr and i < n-m+1:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
        i += 1

    if first:
        first.next = prev
    else:
        head = prev
    last.next = curr
    return head


def AddTwoNumberII(l1, l2):
    if not l1 or not l2:
        return l1 or l2

    def getValues(node):
        valueList = []
        while node:
            valueList.append(node.val)
            node = node.next
        return valueList
    
    l1List = getValues(l1)
    l2List = getValues(l2)
    carr, val = divmod(l1.pop() + l2.pop(), 10)
    ans = Node(val)
    while len(l1List) or len(l2List):

        val = carr
        if len(l1List) > 0:
            val += l1List.pop()
        if len(l2List) > 0:
            val += l2List.pop()
        carr, val = divmod(val, 10)

        curr = Node(val)
        curr.next = ans
        ans = curr
        
    if carr:
        curr = Node(1)
        curr.next = ans
        ans = curr
    return ans


visited = {}
def DeepcopyListWithRandomPointer(head):
    if not head:
        return None

    if head.val in visited:
        return visited[head.val]
    
    node = Node(head.val)
    visited[head.val] = node

    node.next = DeepcopyListWithRandomPointer(head.next)
    node.random = DeepcopyListWithRandomPointer(head.random)
    return node


