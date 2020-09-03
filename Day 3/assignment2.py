print("Welcome")
for i in range(1, 200):
        if (i == 1):
            continue
        prime = 1
        for num in range(2, i // 2 + 1):
            if (i % num == 0):
                prime = 0
                break
        if (prime == 1): 
            print(i, end = ",")
print("\nAll the above are prime numbers\nThank You!!!")
