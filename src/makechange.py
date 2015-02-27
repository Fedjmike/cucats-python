#Needs:
#- recursion
#- list comprehensions, with if
#- list slices, [1:]

def also(coin, ways):
	return [rest + [coin] for rest in ways]

def makechange(amount, coins):
	#Deal with the trivial case of making zero
	if amount == 0:
		return [[]]

	else:
		ways = []
	
		#Get rid of the coins that are too large
		coins = [coin for coin in coins if coin <= amount]
		
		for coin in coins:
			ways += also(coin, makechange(amount-coin, coins))
			
			#Exclude this coin from any more solutions
			coins = coins[1:]
		
		return ways
		

#Order of coins doesn't matter
#It just changes which ways are found first	
print makechange(25, [5, 10, 20, 50, 100])