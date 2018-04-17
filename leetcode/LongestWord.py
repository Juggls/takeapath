
class TrieRoot: 
    def __init__(self):
        self.children = {}

class Node:
    def __init__(self, parent, value, isWord):
        self.parent = parent
        self.value = value
        self.isWord = isWord
        self.children = {}

    def add_child(self, child):
        self.children[child.value] = child

    def get_next(self, next_letter):
        if next_letter in self.children:
            return self.children[next_letter]
        else:
            return None



    