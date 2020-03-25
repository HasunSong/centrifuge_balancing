# %%
import math

error = 0.000001


def is_balanced(list):
    x, y = 0, 0
    n = len(list)
    for i in range(n):
        if list[i] == '1':
            theta = i / n * 2 * math.pi
            x += math.cos(theta)
            y += math.sin(theta)
    if abs(x) < error and abs(y) < error:
        return True
    else:
        return False


# %%
def sum_string(temp_list):
    s = 0
    for i in range(len(temp_list)):
        s += int(temp_list[i])
    return s


# %%
def check_num(n):
    result = [0] * (n + 1)
    for i in range(2 ** n):
        loc_list = list(bin(i)[2:].zfill(n))
        if is_balanced(loc_list):
            result[sum_string(loc_list)] = True
    return [i for i, x in enumerate(result) if x == 0]

# %%
N=20
for n in range(1,N+1):
    print(f"{n} : {check_num(n)}")

"""
결론: 6의 배수만 된다.
pf) 일단 6의 배수가 되는 걸 보이자.
for N,
마주보는 쌍 N/2개 존재
for n=2k,(1<=k<=N/2)
k개의 쌍을 넣으면 된다.
for n=2k+1,
일단 3개를 정삼각형으로 넣는다.
이 3개가 원래 있던 N/2개의 쌍 중 3개를 먹는다.
나머지 2k-2 개를 k-1개의 쌍으로 나눈다.
이 k-1개의 쌍을 남은 N/2 - 1 개의 쌍들에 나눠넣는다.
근거: k-1<=N/2-1

이제 6의 배수가 아니면 안 되는 것을 보이자.
2의 배수가 아니면 2가 안 된다.
3의 배수가 아니면 3이 안 된다.
따라서 6의 배수가 아니면 안 된다.

증명 끝

"""