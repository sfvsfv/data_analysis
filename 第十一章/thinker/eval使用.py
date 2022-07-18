# coding=gbk
"""
作者：川川
@时间  : 2022/3/18 18:28
"""

# res1 = eval('3 * 5')
# res2 = eval('7+8+(2*3)')
# print(res1, res2)
#
# a = input()
# b = eval(a)
# print(b)

import parser
def test_compile_expr():
    st = parser.expr('2 + 3')
    code = parser.compilest(st)
    print(code)
test_compile_expr()