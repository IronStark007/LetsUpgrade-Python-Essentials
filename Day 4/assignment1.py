print("Hello")
for num in range(1042000, 702648265):
    l = len(str(num))
    s = 0
    i = num
    while i > 0:
        no = i % 10
        s += no ** l
        i //= 10
    if num == s:
        print("The first armstrong number is",num)
        break
    else:
    	continue
print("Thank You.")
