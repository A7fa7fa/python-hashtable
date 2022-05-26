
from HashTable import HashTable


def run ():
    hTable = HashTable(size = 10)

    hTable.add("first entry", 1256)
    hTable["second entry"] = 222
    print(hTable["1234"])
    print(hTable.getEntrys())

if __name__ == "__main__":

    run()
