"""
3人团队在餐厅吃饭，公司能够报销300元，超出的部分三人平摊
输入吃饭金额，得出每个人应该掏的钱的金额。
"""

money = int(input("please enter money"))

if money <= 300:
    print("可以报销")
elif money > 300:
    temp = money - 300
    print("每人应平摊{}元".format(temp / 3))
