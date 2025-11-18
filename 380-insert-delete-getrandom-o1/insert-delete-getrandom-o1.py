class RandomizedSet:
    def __init__(self):
        self.list = []
        self.var = {}

    def insert(self, val: int) -> bool:
        if val in self.var:
            return False
        
        self.var[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.var:
            return False
        
        idx_to_remove = self.var[val]
        last_element = self.list[-1]

        self.list[idx_to_remove] = last_element
        self.var[last_element] = idx_to_remove

        self.list.pop()
        del self.var[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()