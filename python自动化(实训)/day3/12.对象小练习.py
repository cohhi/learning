"""
需求:
小明体重 75 公斤
小明爱跑步, 每次跑步都会减肥0.5公斤
小明爱吃东西, 每次吃东西都会增加1公斤

将上述需求用面向对象的代码实现出来

"""


class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def eat(self):
        print("吃东西...")
        self.height += 1

    def run(self):
        print("跑步")
        self.height -= 0.5


ikun = Person("小明", 75)
# 定义小明,并出传入参数
ikun.eat()
# 吃东西 +1
ikun.run()
# 跑步 -0.5
print(ikun.height)
# 体重
