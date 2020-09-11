"""
Name:Ansari Mohammed Ali Nasim
Date:11/09/2020
Purpose-Python Essentials-Batch 7 Day 8 Assignment 2
Program - Error handling of a file which is open in read only mode
"""


with open("translate.txt", "r") as f:
    print(f.read())
    try:
        f.write(input("Enter input to write\n"))
    except:
        print("Sorry, the file is open in \"READ ONLY MODE\"\n"
              "If you want to write something open file in \"WRITE OR READ AND WRTIE MODE\"")
    finally:
        print("Thank You!!!")
