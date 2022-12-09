def message(num1, num2):  # 添加参数
    total = 0
    for i in range(num1, num2 + 1):
        total += i

    return total


print(message(1, 100))
print(message(50, 60))
print(message(1, 10))
