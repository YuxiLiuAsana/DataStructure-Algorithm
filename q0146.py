class DoubleLinkedNode:
    def __init__(self, key, value, pre=None, post=None):
        self.key = key
        self.value = value
        self.pre = None
        self.post = None

    def __del__(self):
        self.pre = None
        self.post = None


class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.tail = None
        self.head = None
        self.len = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.map:
            return -1
        else:
            node = self.map[key]
            pre = node.pre
            post = node.post
            if post == None:
                return node.value
            if pre != None:
                pre.post = post
            else:
                self.head = post
                self.head.pre = None
            post.pre = pre
            self.tail.post = node
            node.pre = self.tail
            self.tail = node
            self.tail.post = None
            return node.value

    def put(self, key: int, value: int) -> None:
        if self.len == self.capacity and not key in self.map:
            if self.capacity == 1:
                del self.head
                self.head = None
                self.tail = None
                self.map = {}
            else:
                node = self.head
                del self.map[node.key]
                self.len -= 1
                self.head = self.head.post
                self.head.pre = None
                del node
        if key in self.map:
            self.map[key].value = value
            self.get(key)
        else:
            self.map[key] = DoubleLinkedNode(key, value)
            if self.head == None:
                self.head = self.map[key]
                self.tail = self.map[key]
            else:
                self.tail.post = self.map[key]
                self.map[key].pre = self.tail
                self.tail = self.tail.post
            self.len += 1
