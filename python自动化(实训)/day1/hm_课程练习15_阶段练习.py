# author:steam-404
"""
录入用户信息
需求：
1. 提示用户输入用户姓名，并保存到变量中
2. 提示用户输入用户年龄，保存到变量中，并转换成整数
3. 提示用户输入用户身高，保存到变量中，并转换成浮点数
4. 在控制台输出用户姓名、年龄、身高对应变量的数据类型
5. 按照以下格式输出用户信息：“姓名:xxx 年龄:xxx 身高:xxx”
6. 在控制台输出该用户5年之后的年龄，格式：“张三 5 年之后的年龄是 25岁”
"""

name = input("请输入姓名")
age = input("请输入年龄")
age = int(age)
height = input("请输入身高")
height = float(height)

print(f"姓名:{name}\t年龄:{age}\t身高:{height}\t")
print(f"5年后:姓名:{name}\t年龄:{age + 5}\t身高:{height}\t")

# format方法
print("姓名:{}\t年龄:{}\t身高:{}\t".format(name, age, height))
print("5年后:姓名:{}\t年龄:{}\t身高:{}\t".format(name, age+5, height))
