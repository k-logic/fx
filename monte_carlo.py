from datetime import datetime, timedelta
import math
import matplotlib.pyplot as plt
import random
import matplotlib.pyplot as plt

# コイントスを行い　表なら勝ち　裏なら負け
# モンテカルロの方式に分解を組み合わせて行う。

# 整数を２分解
def calcDecomposition(n):
    x = math.floor(n/2)
    y = math.ceil(n/2)
    return [x, y]

# 先頭と末尾削除
def calcWinMonte(list):
    del list[0]
    del list[-1]
    if not list:
        list = [0, 1]
    if len(list) == 1:
        list = calcDecomposition(list[0])
    return list

# 末尾に追加
def addLossMonte(list):
    sum = list[-1] + list[0]
    list.append(sum)
    return list

#ベットロット
def entryLotBed(list):
    lot = list[-1] + list[0]
    return lot
    
# 表:１ 裏:0
def cointoss(threshold=1):
    # 0から1までのランダムな数を生成
    random_number = random.random()
    # 生成したランダムな数が指定した確率より小さいかどうかを確認
    return random_number < threshold

probability = 0.5
capital = 1000000
rate = 10000
lot = 1
num = 6000
R = []
T = []
S = []
list_monte = [0, 1]
win_rate = 0
loss_rate = 0
Profit = 0
drawdown = 0

for k in range(num):
    print(f'\n')
    print(f'{k+1}回目')
    print(f'Lot: {lot}')
    res = cointoss(probability)
    R.append(res)
    if(res):
    # 勝ち(表)
        rate_win = rate*lot
        Profit += rate_win
        win_rate += rate_win
        list_monte = calcWinMonte(list_monte)
        print(f'勝ち')
        T.append(lot)
        S.append(rate_win)
        print(f'利益: {rate_win} 円' )
    else:
    # 負け(裏)
        rate_loss = -rate*lot
        Profit += rate_loss
        loss_rate += rate_loss
        list_monte = addLossMonte(list_monte)
        print(f'負け')
        T.append(lot * -1)
        S.append(rate_loss)
        print(f'利益: {rate_loss} 円' )

    print(list_monte)
    lot = entryLotBed(list_monte)
    print(f'Lot: {lot}に変更')


#print(R)
#print(T)
#print(f'\n')
print(f'勝率=勝ち数: {sum(R)}')
print(f'勝率負け数: {num-sum(R)}')
print(f'勝率: {(sum(R)/num) * 100} %')
print(f'利益: {win_rate} 円')
print(f'損益: {loss_rate} 円')
print(f'合計: {Profit} 円')

cumulative_profits = [sum(S[:i+1]) for i in range(len(S))]
plt.plot(cumulative_profits)
plt.title('Cumulative Profits')
plt.xlabel('Trade Number')
plt.ylabel('Cumulative Profit')
plt.grid(True)
plt.show()





