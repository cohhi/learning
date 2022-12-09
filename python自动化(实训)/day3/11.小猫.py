"""
需求：小猫 爱 吃鱼，小猫 要 喝水
使用上述需求, 将类定义出来
通过这个类,创建两只猫对象, 让这两只猫对象完成吃鱼和喝水的事情
思考, 这两个猫对象是同一个东西吗

student:不是
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat_food(self):
        print("吃鱼中...")

    def drink(self):
        print("喝水中...")


cat1 = Cat("小花", 2)
cat2 = Cat("大肥", 3)
cat3 = Cat("小飞", 5)

print(cat1.name)
print(cat1.age)
