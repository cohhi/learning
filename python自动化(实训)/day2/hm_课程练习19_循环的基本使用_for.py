"""
需求：
打印hello字符串的每一个字符
"""

steam_404 = "hello"
length = len(steam_404)
# 使用切片
print(steam_404[0:length])

# 使用循环
for i in range(0, length):
    print(steam_404[i], end=" ")
