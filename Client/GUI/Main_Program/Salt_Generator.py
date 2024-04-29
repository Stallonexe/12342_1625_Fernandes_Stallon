import random
from Algorithms.mergesort import *

class Pool:
    def __init__(self):
        self.salt_pool = []
        self.sorted_salt_pool = []
        self.salt_dict = {}


        self.UpdateDictionary()

    def ConvertHextoDecimal(self, Hexadecimal):
        decimal = int(Hexadecimal,16)
        return decimal

    def SavePool(self):
        with open("pool.txt", "w") as file:
            for salt in self.sorted_salt_pool:
                file.write(f"{salt}\n")
        file.close()

    def ImportPool(self):
        with open("pool.txt", "r") as file:
            for line in file:
                line = str(line.strip('\n'))
                if line not in self.salt_pool:
                     self.salt_pool.append(line)

    def UpdateDictionary(self):
        self.ImportPool()
        for salt in self.salt_pool:
            decimal = self.ConvertHextoDecimal(str(salt))
            self.salt_dict[str(salt)] = int(decimal)
        self.SortPool()
        self.SavePool()

    def FindKeyByValue(self, target_value):
        for key, value in self.salt_dict.items():
            if value == target_value:
                return key
        return None # Return None is the value is not in the dictionary

    def GetValuesList(self):
        values = []
        for key, value in self.salt_dict.items():
            values.append(value)
        return values

    def SortPool(self):
        sorted_pool = MergeSort(self.GetValuesList())
        print(sorted_pool)
        for value in sorted_pool:
            salt = self.FindKeyByValue(value)
            if salt not in self.sorted_salt_pool:
                self.sorted_salt_pool.append(salt)

pool = Pool()

def BinarySearch(array, target, low, high):
    if low <= high:
        mid_point = (low + high) // 2  # index of the middle value

        if array[mid_point] == target:  # Returns True, when target has been found
            return True

        elif array[mid_point] < target:  # if target is larger: look at the right side of the array.
            BinarySearch(array, target, mid_point + 1, high)

        elif array[mid_point] > target:  # if target is lower: look at the left side of the array.
            BinarySearch(array, target, low, mid_point - 1)

        else:
            return False

def gen_hex():
    # temp stores hex in the array
    hex_array = []
    for i in range(4):
        #generate random decimal value
        random_value = random.randrange(0,15,1)

        #convert decimal to hexadecimal
        hex_code = hex(random_value)[2:]
        hex_array.append(hex_code)

    #Convert array into a string
    hex_string = ''.join(hex_array)

    check = BinarySearch(pool.sorted_salt_pool, hex_string, 0, len(pool.sorted_salt_pool) - 1)

    if check is True:
        gen_hex()
    else:
        pool.sorted_salt_pool.append(hex_string)
        pool.UpdateDictionary()




pool = Pool()

#gen_hex()

#print(pool.salt_pool)

#print(pool.sorted_salt_pool)

