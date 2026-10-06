class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:

    if not head or not head.next:
        return False

    lento = head
    rapido = head

    while rapido and rapido.next:
        lento = lento.next
        rapido = rapido.next.next

        if lento == rapido:
            return True
    return False
