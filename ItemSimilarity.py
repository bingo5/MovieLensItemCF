#__author__ = 'jixuebin'

import math


def ItemSimilarity(train):
	# calculate co-users between items
	C = dict()
	N = dict()
	for user, item in train.items():
		for i in item:
			if i not in C:
				C[i] = dict()
			if i not in N:
				N[i] = 1
			else:
				N[i] += 1  # 记录喜欢物品i的用户数量
			for j in item:
				if i == j:
					continue
				if j not in C[i]:
					C[i][j] = 1
				else:
					C[i][j] += 1  # 记录同时喜欢物品i和物品j的用户数量

	# calculate final similarity Matrix,W
	W = dict()
	for i, related_item in C.items():
		if i not in W:
			W[i] = dict()
		for j, cij in related_item.items():
			W[i][j] = cij / math.sqrt(N[i] * N[j])
	return W


def ImprovedSimilarity(train):
	# calculate co-users between items
	C = dict()
	N = dict()
	for user, item in train.items():
		for i in item:
			if i not in C:
				C[i] = dict()
			if i not in N:
				N[i] = 1
			else:
				N[i] += 1  # 记录喜欢物品i的用户数量
			for j in item:
				if i == j:
					continue
				if j not in C[i]:
					C[i][j] = 1 / math.log(1 + len(item))  # 对活跃用户进行了一定的惩罚
				else:
					C[i][j] += 1 / math.log(1 + len(item))

	# calculate final similarity Matrix,W
	W = dict()
	for i, related_item in C.items():
		if i not in W:
			W[i] = dict()
		for j, cij in related_item.items():
			W[i][j] = cij / math.sqrt(N[i] * N[j])
	return W


# 相似度矩阵归一化
def SimilarityNormalization(W):
	W_Norm = dict()
	for i, related_item in W.items():
		if i not in W_Norm:
			W_Norm[i] = dict()
		maxw = max(related_item.values())
		for j, wij in related_item.items():
			W_Norm[i][j] = wij / maxw
	return W_Norm
