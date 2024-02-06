
def minimunChange(coins):
	sortedCoins = sorted(coins)
	coinsAmount = len(sortedCoins)
	changes = [0]
	for i in range(coinsAmount):
		changesLength = len(changes)
		for t in range(changesLength):
			lastElementIndex = len(changes) -1
			validateRepeated = changes[t] + sortedCoins[i] in changes
			validateChange = changes[lastElementIndex] - changes[lastElementIndex - 1] <= 1
			if validateRepeated == False and validateChange == True:
				changes.append(changes[t] + sortedCoins[i])
			elif validateChange == False:
				return changes[lastElementIndex - 1] + 1
	return max(changes) + 1

#coins = [1, 1, 1, 1, 1] # {1, 2, 3, 4, 5} -> 6
#coins = [1, 2, 4, 7, 9] # {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16} -> 8
#coins = [5, 7, 1, 1, 2, 3, 22] # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41} -> 20
coins =  [1, 5, 1, 1, 1, 10, 15, 20, 100]
result = minimunChange(coins)
print('Minimun change that cannot be given')
print('Coins: ', coins, ' -> ', result)