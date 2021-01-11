'''
Implementation for max heap.....same logic applies for min heap (change logic for small values)

for index i:
    left child = 2i+1
    right child = 2i+2
    root : (i-1)/2

For Input → 35 33 42 10 14 19 27 44 26 31

resultant => 44 42 35 33 31 19 27 10 26 14
'''

class MaxHeap:
    def __init__(self):
        self.max_heap_data = []

    def insert(self, data):
        self.max_heap_data.append(data)
        self.adjust()

    def adjust(self):
        if len(self.max_heap_data) > 1:
            index =len(self.max_heap_data)-1
            root_index = self.getRootindex(index)
            print('index is {} and root index is {}'.format(index, root_index))
            self.compare_and_swap(index, root_index)

    def getRootindex(self, index):
        if index == 0:
            return 0
        return int((index-1)/2)

    def compare_and_swap(self, child, root):
        if self.max_heap_data[root] > self.max_heap_data[child]:
            print('root is greater ..no need to to swap')
        else:
            print('root {} is less than child {}'.format(self.max_heap_data[root], self.max_heap_data[child]))
            self.max_heap_data[root], self.max_heap_data[child] = self.max_heap_data[child], self.max_heap_data[root]
            print('swapping done')
            new_root_index = self.getRootindex(root)
            if new_root_index == root :
                print('no need to adjust more as i am at 0th index')
            else:
                self.compare_and_swap(root, new_root_index)

    def display(self):
        print("Data in max heap list.........")
        for data in self.max_heap_data:
            print(data)


if __name__ == "__main__":
    MaxHeapObj = MaxHeap()
    while 1:
        print("_____Menu______")
        print("1. Insert")
        print("2. Display")
        print("0. Exit")

        data = input("Enter the choice :  ")
        if int(data) == 0:
            break
        if int(data) == 1:
            user_input = input('Enter the value for heap = ')
            MaxHeapObj.insert(int(user_input))
        if int(data) == 2:
            MaxHeapObj.display()



    
