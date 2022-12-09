"""
需求：
1. 定义动物类，动物有姓名和年龄属性，具有 吃 睡 玩耍 的行为
2. 定义狗类，狗类具有动物类的所有属性和方法，并且具有 叫 的特殊行为
"""


# 动物类
class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃")

    def sleep(self):
        print("睡觉")

    def play(self):
        print("玩耍")


class Dog(animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dark(self):
        print("汪汪汪")


print("动物")
animal1 = animal("小花", 3)
print(animal1.name)
print(animal1.age)
animal1.eat()
animal1.sleep()
animal1.play()
print("\n")

dog1 = Dog("小黑", 5)
dog1.eat()
dog1.sleep()
dog1.play()
dog1.dark()
