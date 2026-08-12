num = int(input("Enter digit No: "))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Total Digits:",count)
