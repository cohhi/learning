height = 175
money = 15000
# 女生1相亲标准:身高大于等于180,并且月薪大于等于10000
# 女生2相亲标准:身高大于等于180,或者月薪大于等于10000

# 问 height和money的值满足哪位女生的相亲标准


if height >= 180:
    print("身高大于180")
elif height < 180:
    print("身高小于180")

if money >= 10000:
    print("月薪大于10000")
elif money < 10000:
    print("月薪小于10000")
print("-----------------------我是分割线------------------------")
if height >= 180 and money >= 10000:
    print("满足女生1")
elif height >= 180 or money >= 10000:
    print("满足女生2")
else:
    print("单身贵族🐕")
