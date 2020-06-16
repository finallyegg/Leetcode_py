# Design

class RandomizedSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.store:
            return False
        self.list.append(val)
        self.store[val] = len(self.list)-1
        return True
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.store: # swap val with end
            idx = self.store[val]
            end = self.list[-1]
            
            self.list[idx] = end
            self.store[end] = idx
            
            # remove end
            self.list.pop()
            
            # remove val in store
            del self.store[val]
            
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.list[random.randint(0,len(self.list)-1)]
            


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()