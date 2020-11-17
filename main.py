# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import self as self

from HashTable_Chaining import HashTable_Chaining
from HashTable_LinearProbing import HashTable_LinearProbing
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    randomlength = random.randint(1, 100)
    hash_table_Chaining = [[] for _ in range(10)]
    hash_table_LinearProbing = [[] for _ in range(10)]

    for i in range(0, randomlength):
        HashTable_Chaining.insert(hash_table_Chaining, i, 'Italy')
        HashTable_LinearProbing.insert(hash_table_LinearProbing, i, 'Nepal')

    print("Hash Table With Chaining -> ")
    print(hash_table_Chaining)
    print("Numero di collisioni:",HashTable_Chaining.get_chaning_count(hash_table_Chaining))

    print("Hash Table With Linear Probing -> ")
    print(hash_table_LinearProbing)
    print("Numero di elementi persi causa overflow:", HashTable_LinearProbing.getOverflow_Count(hash_table_LinearProbing))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
