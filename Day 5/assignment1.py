"""
Name:Ansari Mohammed Ali Nasim
Date:09/09/2020
Purpose-Python Essentials-Batch 7 Day 5 Assignment 1
"""


def matchwords(sen1, sen2):
    for i in sen1:
        for j in sen2:
            if len(sen2) >= 0 and j == i:
                sen2.pop(0)
                sen1.remove(i)
            else:
                break
    return sen2


if __name__ == '__main__':
    Listy = [1, 5, 6, 4, 1, 2, 3, 5]
    # Listy = [1, 5, 6, 5, 1, 2, 3, 6]
    sublist = [1, 1, 5]
    if len(matchwords(Listy, sublist)) == 0:
        print('It\'s a Match')
    else:
        print('It\'s Gone')
