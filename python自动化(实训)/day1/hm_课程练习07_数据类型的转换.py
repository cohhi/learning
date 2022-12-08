# 需求1: 定义两个变量num1和num2, 值分别是10和20, 将num1和num2相加之后进行打印

num1 = 10
num2 = 20
print(num1 + num2)

# 需求2: 定义两个变量str1和str2, 值分别是'10'和'20',将str1和str2相加之后进行打印

str1 = '10'
str2 = '20'
print(str1 + str2)

# 需求3: 怎么样可以在需求2的代码上, 达到和需求1同样的效果?

str1 = '10'
str2 = '20'

str1 = int(str1)
str2 = int(str2)
print(str1 + str2)
