import sys
import math
import random

import solver_greedy

from common import print_tour, read_input


# 2点間の距離を求める関数
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# 合計距離を計算する関数
def get_score(n, cities, tour):
    score = 0
    for i in range(n):
        score += distance(cities[tour[i]], cities[tour[i+1]])
    return score

# 焼きなまし法によって答えを求める関数
def solve(cities):
    n = len(cities)
    # 初期解生成
    # tour = [ i % n for i in range(n + 1) ]
    # 初期解生成: 貪欲法
    tour = solver_greedy.solve(cities)
    tour.append(tour[0])
    #print(tour)
    current_score = get_score(n, cities, tour)
	# 焼きなまし法
    NUM_LOOPS = 40000
    for t in range(NUM_LOOPS):
        # 反転させる区間 [L, R] を選ぶ
        l = random.randint(1, n - 1) 
        r = random.randint(1, n - 1) 
        if l > r:
            l, r = r, l
		# tour[l:r]を逆順にしたときの合計距離を求める
        new_score = current_score
        new_score -= distance(cities[tour[l-1]], cities[tour[l]])
        new_score -= distance(cities[tour[r]], cities[tour[r+1]])
        new_score += distance(cities[tour[l-1]], cities[tour[r]])
        new_score += distance(cities[tour[l]], cities[tour[r+1]])
        # T: 温度
        T = 30 - 28 * (t / NUM_LOOPS)
        probability = math.exp(min((current_score - new_score) / T, 0))
        if random.random() < probability:
			# 解が改善した場合
            tour[l:r+1] = reversed(tour[l:r+1])
            current_score = new_score
    return tour

if __name__ == '__main__':
    assert len(sys.argv) > 1
    # 焼きなまし法
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
