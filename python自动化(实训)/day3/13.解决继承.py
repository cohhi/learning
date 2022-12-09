"""
写一个动物类, 具备 吃 喝 跑 睡 四项能力
写一个狗类, 具备 吃 喝 跑 睡 叫 五项能力
写一个猫类, 具备 吃 喝 跑 睡 喵 五项能力

写完之后, 你会发现有一些啥问题
student:大量重复
"""


class animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


print("动物:")
animate1 = animal()
animate1.eat()
animate1.drink()
animate1.run()
animate1.sleep()
print("\n")


class Dog:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

    def dark(self):
        print("汪汪汪")


print("狗:")
dog1 = Dog()
dog1.eat()
dog1.drink()
dog1.run()
dog1.sleep()
dog1.dark()
print("\n")


class Cat:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

    def dark(self):
        print("喵喵喵")


print("猫")
cat1 = Cat()
cat1.eat()
cat1.drink()
cat1.run()
cat1.sleep()
cat1.dark()
