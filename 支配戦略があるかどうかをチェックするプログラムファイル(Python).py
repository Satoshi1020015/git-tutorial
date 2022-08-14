# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

Row = 2 # 行数
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

Row = 2 # 行数
Col = 2 # 列数

# プレーヤー1の利得
payoff1 = [
    [3,0],
    [4,1],
]

# プレーヤー2の利得
payoff2 = [
    [3,4],
    [0,1]
]

print()
print('ゲームの利得')
for i in range(Row):
    print('戦略',i+1,' ', end="")
    for j in range(Col):
        print('(',payoff1[i][j],',',payoff2[i][j],') ',end="")
    print()

# プレーヤー1に支配戦略があるかどうか
d_index1 = [0]*Row
for j in range(Col):
    tmp_val = -9999 # 仮の利得の値
    tmp_i = -1 # 仮の支配戦略のインデックス
    for i in range(Row):
        if payoff1[i][j] > tmp_val: # 戦略iの利得の方が大きければ
            tmp_i = i # インデックスを入れ替える
            tmp_val = payoff1[i][j] # 利得最大値を入れ替える
    d_index1[j] = tmp_i # 利得最大の戦略のインデックスを保存

d_tmp = d_index1[0]
judge = -1
for j in range(Col):
    if d_index1[j] == d_tmp:
        d_tmp = d_index1[j]
        judge = 1
    else:
        judge = 0

print()
if judge == 1:
    print('プレーヤー1にとって、戦略',d_index1[0]+1,'は支配戦略.')
else:
    print('支配戦略は存在しない.')