"""
需求：
计算0~100所有偶数的累加和结果
"""
numbers = 0

for i in range(0, 100 + 1):
    if i % 2 == 0:
        numbers += i

print("0~100所有偶数的累加和结果:{}".format(numbers))