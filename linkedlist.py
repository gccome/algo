class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse(head):
    if head is None or head.next is None:
        return head

    pre = None
    reverse_head = None
    current = head

    while current:
        reverse_head = current
        tmp = current.next
        current.next = pre
        pre = current
        current = tmp

    return reverse_head


def check_circle(head):
    slow = head
    fast = head
    loop = False

    if head is None:
        return False

    while slow.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop = True
            break

    if loop:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    return False


def merge_sorted_lists(l1, l2):
    if l1 is None:
        return l1
    if l2 is None:
        return l1

    head = ListNode(0)  # New head
    current = head
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1 is None:
        current.next = l2
    elif l2 is None:
        current.next = l1

    return head.next


def remove_last_kth(head, k):
    slow = head
    fast = head
    i = 0
    while i != k:
        fast = fast.next
        i += 1
    if fast is None:
        return head.next
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head


def find_middle_node(head):
    if head is None:
        return None
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


if __name__ == '__main__':
    # reverse
    # head = ListNode(1)
    # p1 = ListNode(2)
    # p2 = ListNode(3)
    # p3 = ListNode(4)
    # head.next = p1
    # p1.next = p2
    # p2.next = p3
    #
    # p = reverse(head)
    #
    # while p:
    #     print(p.val)
    #     p = p.next

    # check loop
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    print(check_circle(node1).val)
