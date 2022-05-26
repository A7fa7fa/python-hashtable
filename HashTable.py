
class HashTable:
    '''This is a Custome Hashtable.
    Stores key value pairs as tupple in array by hashing value to index.
    if hash returns the same hash from simple hashing. values are chained'''

    def __init__(self, size = 100) -> None:
        '''Creates new HashTable. default size 100'''
        self.MAX = size
        self.arr = [[] for i in range(self.MAX)]

    def getEntrys(self) -> list[list]:
        '''returns list'''
        result = []
        for element in self.arr:
            if element:
                for tup in element:
                    result.append(tup)
        return result

    def getSimpleHash(self, key) -> int:
        '''simple hashing funxtion. generates integer Hash from key'''
        checksum = 0
        for char in key:
            checksum += ord(char)
            return checksum % self.MAX

    def add(self, key, value):
        '''adds value as tupple(key, value) at index of integer hash of key.
        if there is already a tupple with different key at array position, new tupple is chained'''
        hashInt = self.getSimpleHash(key)

        # if list at hash index is empty just append key value as tupple and return 
        if not self.arr[hashInt]:
            self.arr[hashInt].append((key, value))
            return

        found = False
        for idx, element in enumerate(self.arr[hashInt]):
            if len(element) == 2 and element[0] == key:
                self.arr[hashInt][idx] = (key, value)
                found = True
                break
            if not found:
                self.arr[hashInt].append((key, value))

    def __setitem__(self, key, value):
        '''allows use of default python operator hashtable["key"] = value '''
        self.add(key, value)

    def get(self, key):
        '''return value of key.'''
        hashInt = self.getSimpleHash(key)
        for element in self.arr[hashInt]:
            if len(element) == 2 and element[0] == key:
                return element[1]
        return None

    def __getitem__(self, key):
        '''allows use of default python operator hashtable["key"]'''
        return self.get(key)

    def deleteItem(self, key):
        '''deletes value from hashtable'''
        hashInt = self.getSimpleHash(key)

        for idx, element in enumerate(self.arr[hashInt]):
            if len(element) == 2 and element[0] == key:
                del self.arr[hashInt][idx]
                break

    def __delitem__(self, key):
        '''allows use of default python operator del hashtable["key"]'''
        self.deleteItem(key)
