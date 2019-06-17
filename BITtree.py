# i が与えられたとき a1~aiまでの和を計算する( O(log n) )
def bitsum(bit,i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i&(-i)
    return s
    
# i と x が与えられたとき ai += x とする ( O(log n) )
def bitadd(bit,i,x):
    while i <= n:
        bit[i] += x
        i += i&(-i)
    return bit
    
#################################
import math
n = int(input())
a = list(map(int,input().split()))

#bitの構築
n_ = int(math.log2(n)) + 1
bit = [0] * (2**n_)
bit.append(0)

################################
ass = 0
for j in range(n):
    ass += j-bitsum(bit,a[j])
    #bitsum(bit,a[j]): j-1番目までの中でa[j]以下のもの
    bit = bitadd(bit,a[j],1)
print(ass)  