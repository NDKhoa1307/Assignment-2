num = int(input().strip())

temp = 0
while num:
    if len(str(num)) == 1:
        temp += num % 10
        if len(str(temp)) == 1:
            print(temp)
            break
        else:
            num = temp
            temp = 0
    else:
        temp += num % 10
        num //= 10
