class FileNode:
    def __init__(self, name, *children):
        self.name = name
        self.children = []
        for c in children:
            self.children += [c]


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input_rows = input.split("\n")
        zero_dir = []
        last_dir = []
        for i in input_rows:
            strip_i = i.strip('\t')
            level = len(i) - len(strip_i)
            file_node = FileNode(strip_i)
            if len(last_dir) <= level:
                last_dir += [file_node]
            last_dir[level] = file_node
            if level != 0:
                last_dir[level - 1].children += [file_node]
            if level == 0:
                zero_dir += [file_node]

        def helper(file_node):
            if len(file_node.children) == 0:
                if len(file_node.name.split('.')) >= 2:
                    return len(file_node.name)
                else:
                    return 0
            max_children = 0
            for c in file_node.children:
                max_children = max(helper(c), max_children)
            if max_children == 0:
                return 0
            return len(file_node.name) + 1 + max_children

        max_dir = 0
        for z in zero_dir:
            max_dir = max(max_dir, helper(z))
        return max_dir


