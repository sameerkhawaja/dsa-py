from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init(self):
        # insert a dummy node
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        cur = self.head
        while cur and index > -1:
            if index == 0:
                return cur.val
            cur = cur.next
            index -= 1
        return -1

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val)
        if not self.head:
            self.head = new_head
        else:
            new_head.next = self.head
        self.head = new_head

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        if not self.tail:
            self.head = new_tail
        else:
            self.tail.next = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        cur = self.head
        prev = ListNode(-1)
        while cur and index > -1:
            if index == 0:
                prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
            index -= 1
        return False

    def getValues(self) -> List[int]:
        result = []
        if not self.head:
            return result
        cur = self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result


def test_linked_list():
    # Test case 1: Initialization and getValues
    ll = LinkedList()
    assert ll.getValues() == [], "Test case 1 failed"

    # Test case 2: Insert head and getValues
    ll.insertHead(1)
    assert ll.getValues() == [1], "Test case 2 failed"
    ll.insertHead(2)
    assert ll.getValues() == [2, 1], "Test case 2 failed"

    # Test case 3: Insert tail and getValues
    ll.insertTail(3)
    assert ll.getValues() == [2, 1, 3], "Test case 3 failed"
    ll.insertTail(4)
    assert ll.getValues() == [2, 1, 3, 4], "Test case 3 failed"

    # Test case 4: Get value at index
    assert ll.get(0) == 2, "Test case 4 failed"
    assert ll.get(1) == 1, "Test case 4 failed"
    assert ll.get(2) == 3, "Test case 4 failed"
    assert ll.get(3) == 4, "Test case 4 failed"
    assert ll.get(4) == -1, "Test case 4 failed"  # Index out of bounds

    # Test case 5: Remove and getValues
    assert ll.remove(1) == True, "Test case 5 failed"  # Remove value at index 1
    assert ll.getValues() == [2, 3, 4], "Test case 5 failed"
    assert ll.remove(0) == True, "Test case 5 failed"  # Remove value at index 0
    assert ll.getValues() == [3, 4], "Test case 5 failed"
    assert ll.remove(1) == True, "Test case 5 failed"  # Remove value at index 1
    assert ll.getValues() == [3], "Test case 5 failed"
    assert ll.remove(0) == True, "Test case 5 failed"  # Remove last remaining element
    assert ll.getValues() == [], "Test case 5 failed"
    assert ll.remove(0) == False, "Test case 5 failed"  # Remove from empty list

    print("All LinkedList tests passed")


# Uncomment the following line to run the tests
test_linked_list()
