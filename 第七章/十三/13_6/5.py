"""
作者：川川

@时间  : 2022/3/28 2:48
"""
filename = input("请输入文件名: ")
new = filename.split(".")
print("拓展格式为 : " + repr(new[-1]))
