"""
需求：
1. 定义动物类，动物有姓名和年龄属性，具有吃和睡的行为
2. 定义猫类，猫类具有动物类的所有属性和方法，并且具有抓老鼠的特殊行为
3. 定义狗类，狗类具有动物类的所有属性和方法，并且具有看门的特殊行为
4. 定义哮天犬类，哮天犬类具有狗类的所有属性和方法，并且具有飞的特殊行为
"""


class animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃")

    def sleep(self):
        print("睡")


class Cat(animal):

    def mouse(self):
        print("抓老鼠")


class Dog(animal):

    def door(self):
        print("看门")


# 定义哮天犬
# 继承狗类
class ScreamerDog(Dog):

    def fly(self):
        print("起飞咯")


ScreamerDog1 = ScreamerDog("哮天犬", 100)
print(ScreamerDog1.name)
print(ScreamerDog1.age)
ScreamerDog1.door()
ScreamerDog1.sleep()
ScreamerDog1.fly()
