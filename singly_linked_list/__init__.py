class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next: Node or None = None
        self.prev: Node or None = None


class LinkedList:
    def __init__(self):
        self.head: Node or None = None
        self.tail: Node or None = None
        self.length = 0

    def __len__(self):
        return self.length

    def add_to_tail(self, key: int) -> Node:
        new_node = Node(key)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return new_node
        self.tail.next = new_node
        new_node.next = None
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return self.tail

    def remove_tail(self) -> int or None:
        if not self.head and not self.tail:
            return None
        if self.tail is self.head:
            old_tail: Node = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return old_tail.value
        old_tail: Node = self.tail
        self.tail = old_tail.prev
        self.tail.next = None
        self.length -= 1
        return old_tail.value

    def add_to_head(self, key: int) -> Node:
        new_node = Node(key)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return new_node
        self.head.prev = new_node
        new_node.prev = None
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self.head

    def remove_head(self) -> int or None:
        if not self.head and not self.tail:
            return None
        if self.head is self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return old_head.value
        old_head = self.head
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        return old_head.value

    def contains(self, key: int) -> bool:
        if self.head is not None or self.tail is not None:
            curr_node = self.head
            if curr_node.value == key:
                return True
            while self.tail is not curr_node:
                curr_node = curr_node.next
                if curr_node.value == key:
                    return True
        return False

    def get_max(self) -> int or None:
        # Initialize max_value to zero
        max_value = 0
        # Check to ensure there are nodes within the list
        if self.head is not None or self.tail is not None:
            curr_node = self.head
            # While the next not is not None
            while curr_node.next is not None:
                # Check the value against max_value
                if curr_node.value > max_value:
                    # If greater assign ne max_value
                    max_value = curr_node.value
                # Regardless of check move the curr_node forward
                curr_node = curr_node.next
            # This handles single items within the list
            if curr_node.value > max_value:
                # Assign the new max_value
                max_value = curr_node.value
        # If the max_value has not changed return None
        if max_value == 0:
            return None
        # If the max value has changed return the max_value
        return max_value
