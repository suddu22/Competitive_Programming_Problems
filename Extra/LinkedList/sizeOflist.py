import sys


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def size(self):
        n = 0
        current = self.head
        while current:
            n += 1
            current = current.get_next()
        return n

    def search(self, target):
        current = self.head
        if not current:
            raise ValueError("List is empty")
        found = False
        while current and not found:
            if current.get_data() == target:
                found = True
            else:
                current = current.get_next()

        if current is None:
            raise ValueError("Data not found in list")

        return current

    def delete(self, target):
        current = self.head
        if not current:
            raise ValueError("List is empty")

        found = False
        previous = None
        while current and not found:
            if current.get_data() == target:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError("Data not found in list")

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def findMin(self):
        current = self.head
        current_min = current.get_data()
        while current:
            current = current.get_next()
            if current.get_data() < current_min:
                current_min = current.get_data()

        return current_min

    def rotateRight(self, k):
        head = self.head
        if not head or not head.next_node or k == 0:
            return head

        n = self.size()
        k = k % n
        if k == 0:
            return head

        tmp = Node(0)
        tmp.set_next(head)
        current = head

        for i in range(k):
            current = current.get_next()

        while current and current.get_next():
            head = head.get_next()
            current = current.get_next()

        new_head = head.get_next()
        current.set_next(tmp.get_next())
        head.set_next(None)

        self.head = new_head

    def getMidPoint(self):
        slow = self.head
        fast = self.head.get_next()

        while fast and fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
        return slow.get_next()

    def printList(self):
        current = self.head
        while current:
            if (current.get_next() is None):
                sys.stdout.write(str(current.get_data()) + "\n")
            else:
                sys.stdout.write(str(current.get_data()) + " --> ")
            current = current.get_next()

    def removeDuplicate(self):

        current = self.head
        prev = None

        unique = set()

        while current:
            if current.get_data() in unique:
                if prev:
                    prev.set_next(current.get_next())
                else:
                    prev = current.get_next()
                    self.head = prev
            else:
                unique.add(current.get_data())
            prev = current
            current = current.get_next()

    def kthLast(self, k):

        current = self.head

        n = self.size()
        if n < k:
            return -1

        kth = n - k
        while kth > 0:
            current = current.get_next()
            kth -= 1

        return current.get_data()

    def kthLastNoSize(self, k):

        p1 = self.head
        p2 = self.head

        for i in range(k):
            if not p1:
                return None
            p1 = p1.get_next()

        while p1:
            p1 = p1.get_next()
            p2 = p2.get_next()

        return p2.get_data()

    def deleteMiddle(self, n):
        if not n or not n.get_next():
            return False

        p1 = n.get_next()
        n.set_next(p1)

        return True

    def partition(self, x):
        head = self.head
        tail = self.head

        node = self.head
        while node:
            next_node = node.get_next()
            if node.get_data() < x:
                node.set_next(head)
                head = node
            else:
                tail.set_next(node)
                tail = node

            node = next_node
        tail.set_next(None)

        self.head = head

    def reverse(self):

        current = self.head
        last = None
        while current:
            nxt = current.get_next()
            current.set_next(last)
            last = current
            current = nxt

        self.head = last

    def isPalindrome(self):
        fast = self.head
        slow = self.head

        stack = []

        while fast and fast.get_next():
            stack.append(slow.get_data())
            slow = slow.get_next()
            fast = fast.get_next().get_next()

        if fast is not None:
            slow = slow.get_next()

        while slow:
            pop = stack.pop()

            if pop != slow.get_data():
                return False

            slow = slow.get_next()

        return True




def size(head):
    n = 0
    current = head
    while current:
        n += 1
        current = current.get_next()
    return n

def getIntersectionNode(headA, headB):
    a_size = size(headA)
    b_size = size(headB)

    if a_size > b_size:
        for i in range(a_size - b_size):
            headA = headA.get_next()
    else:
        for i in range(b_size - a_size):
            headB = headB.get_next()

    while headA and headB:
        if headA.get_data() == headB.get_data():
            return headA

        headA = headA.get_next()
        headB = headB.get_next()

    return None

def reorderList(head):
    if not head or not head.next:
        return

    # Find mid
    slow = head
    fast = head.get_next()
    while fast and fast.get_next():
        slow = slow.get_next()
        fast = fast.get_next().get_next()

        # Revserse 2nd half
        cur = slow.get_next()
        slow.set_next(None)
        pre = None

        while cur:
            tmp = cur.get_next()
            cur.set_next(tmp)
            pre = cur
            cur = tmp
        tail = pre







linkedList = LinkedList()
linkedList.insert(1)
linkedList.insert(2)
linkedList.insert(3)
linkedList.insert(4)
linkedList.insert(6)
linkedList.insert(3)
linkedList.insert(2)
linkedList.insert(1)
linkedList.printList()
print linkedList.isPalindrome()
linkedList.printList()
