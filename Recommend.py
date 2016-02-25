#__author__ = 'jixuebin'
# Recommend Movie
# 给用户推荐item
def GetRecommendation(user, train, W, K, r):
	rank = dict()
	interacted_items = train[user]  # 用户产生行为的item
	for i in interacted_items:
		for j, wij in sorted(W[i].items(), key=lambda x: x[1], reverse=True)[0:K]:  # 取与物品i最相似的K个物品
			if j in interacted_items:  # 过滤掉已经产生行为的物品
				continue
			if j not in rank:
				rank[j] = wij * r[user][i]
			else:
				rank[j] += wij * r[user][i]  # 计算用户u对推荐物品j的感兴趣程度，物品i和物品j的相似度*用户u对物品i的感兴趣程度
	return rank
