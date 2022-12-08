"""
需求：
求0-100之间所有能被3整除的数字的累加和
"""

numbers = 0

for i in range(0, 100 + 1):
    if i % 3 == 0:
        numbers += i

print("0-100之间所有能被3整除的数字的累加:{}".format(numbers))