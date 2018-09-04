#coding=utf-8

"""
# A,B,C,D四个人，有三个人说了真话，一个说假话，谁是小偷？

A: 我不是小偷
B: C是小偷
C: 小偷肯定是D
D: C冤枉人
"""

def find_thief():
    people = ['A', 'B', 'C', 'D']
    real_cnt = 0
    
    for i in range(4):
        real_cnt = 1 if i != 0 else 0 
        real_cnt += 1 if i == 2 else 0
        real_cnt += 1 if i == 3 else 0
        real_cnt += 1 if i != 3 else 0
        if real_cnt == 3:
            print("小偷是: ", people[i])
            return
    print("no thief")
    
find_thief()

"""
多项式生成：
多项式系数符合杨辉三角规则，n阶某项系数由n-1阶相邻的系计算而得。
"""
def buildItem(n):
    items = [None]*(n+1)
    if n == 0:
        items[0] = {'c': 1, 'am': 0, 'bm': 0}
        return
    for i in range(1, n + 1):
        # 项数
        nc = i + 1
        items[nc - 1] = {'c': 1, 'am': 0, 'bm': i}
        for j in range(nc - 2, 0, -1):
            c = items[j]['c'] + items[j - 1]['c']
            items[j] = {'c': c, 'am': i - j, 'bm': j}
        items[0] = {'c': 1, 'am': i, 'bm': 0}
    print(items)
        
buildItem(3)