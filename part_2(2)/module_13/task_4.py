class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0:
            return None
        current_node = self.head
        for _ in range(index):
            if current_node.next:
                current_node = current_node.next
            else:
                return None
        return current_node.data

    def remove(self, index):
        if index < 0 or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current_node = self.head
        for _ in range(index - 1):
            if current_node.next:
                current_node = current_node.next
            else:
                return
        if current_node.next:
            current_node.next = current_node.next.next

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __repr__(self):
        return '[' + ' '.join(str(data) for data in self) + ']'


my_list = LinkedList()
for num in range(10):
    my_list.append(num)

print('Текущий список:', my_list)
print('Получение 5 элемента:', my_list.get(4))
print('Удаление 9 элемента.')
my_list.remove(9)
print('Текущий список:', my_list)
