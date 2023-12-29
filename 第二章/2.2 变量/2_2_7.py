"""
作者：川川
时间：2023年12月29日
"""
# 用户输入输出
name = input('请输入你的名字：')
print(name)



# 从用户界面分别输入姓和名
f_name, l_name = input('请分别输入性和名字（空格分开）:').split()
print('性为：', f_name)
print('名为：', l_name)