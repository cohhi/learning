"""
根据描述, 将类的三要素提取出来
一只黄颜色的狗狗叫大黄
看见生人汪汪叫
看见熟人摇尾巴



类的三要素:
    类名:狗子  (dog)
    属性:颜色 (yellow)
    功能: bark
    方法:摇尾巴
"""


class Dog:
    # 定义大黄
    def __init__(self, name, color, newpeople, oldPeople):
        self.name = name
        self.color = color
        self.newPeople = newpeople
        self.odPeople = oldPeople
        print("名字:{}\t颜色:{}\t陌生人:{}\t熟人:{}\t".format(name, color, newpeople, oldPeople))


dog = Dog("大黄", "yellow", "汪汪汪", "摇尾巴")

"""
小明 今年18岁,身高1.75,每天早上跑完步,会去吃东西
小美 今年17岁, 身高1.65,小美不跑步,小美喜欢吃东西

类的三要素:
    类名:人
    属性:年龄,身高,姓名
    方法:跑步,吃东西
"""


class people:
    # 定义人对象
    def __init__(self, name, age, height, run, eat):
        self.name = name
        self.age = age
        self.height = height
        self.run = run
        self.eat = eat
        print("姓名:{}\t年龄:{}\t身高:{}\t是否跑步:{}\t{}".format(name, age, height, run, eat))


xiaoMing = people("小明", 18, 1.75, "每天早上跑步", "会去吃东西")
xiaoMei = people("小美", 17, 1.65, "小美不跑步", "喜欢吃东西")

