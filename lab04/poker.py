# -*- coding: utf-8 -*-
#gruppe: Jørn Utheim-Olsen

import random

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, numdecks=1, deck=mydeck):
	random.shuffle(deck)
	for s in range(numdecks - 1):
		deck = deck + mydeck
	return [deck[n*i:n*(i+1)] for i in range(numhands)]

pranks = ["high card", "Pair", "Two Pair", "Three of a kind", "Straight", \
	"Flush", "Full house", "Four of a kind", "Straight flush"]

def poker(hands):
	#List of the winning hands: poker([hand,...]) => [hand,...]

	return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
	#Returns the list of all cards that is equal to the max of the iterable.
	result, maxcal = [], None
	key = key or (lambda x: x)
	for x in iterable:
		xval = key(x)
		if not result or xval > maxval:
			result, maxval = [x], xval
		elif xval == maxval:
			result.append(x)
	if len(result) == 1:
		result = result[0]
	return result


def hand_rank(hand):
	#Returns the value of the cards that indicate the ranking of a hand.
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):
		return (8, max(ranks))
	elif kind(4, ranks):
		return (7, kind(4, ranks), kind(1, ranks))
	elif kind(3, ranks) and kind(2, ranks):
		return (6, kind(3, ranks), kind(2, ranks))
	elif flush(hand):
		return (5, ranks)
	elif straight(ranks):
		return (4, max(ranks))
	elif kind(3, ranks):
		return (3, kind(3, ranks), ranks)
	elif two_pair(ranks):
		return (2, two_pair(ranks), ranks)
	elif kind(2, ranks):
		return (1, kind(2, ranks), ranks)
	else:
		return (0, ranks)

def card_ranks(hand):
	#Returns a list of the different ranks, sorted with highest first.
	ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
	ranks.sort(reverse = True)
	return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def flush(hand):
	checkflush = [s for r, s in hand]
	return checkflush.count(checkflush[1]) == 5

def straight(ranks):
	#Returns True if the ordered ranks form a 5-card straight.
	return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
	#Returns the first rank in game that has exactly one of a kin hand.
	#if there a none of one of a kind i the hand in game the returns message is None.
	for r in ranks:
		if ranks.count(r) == n: return r
	return None



def two_pair(ranks):
	#If two pair, it returns the two ranks as a tuple: (highest, lowest); otherwhise None.
	pairlist = ()
	for r in ranks:
		if ranks.count(r) == 2: pairlist = pairlist +(r, )
	set(pairlist)
	pairlist = tuple(set(pairlist))
	if len(pairlist) == 2:
		return pairlist
	else:
		return None

def test():
	#A test case to test the different hand results in the game
	sf = "6C 7C 8C 9C TC".split() # Straight Flush
	sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
	sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House
	fl = "AH KH JH 6H TH".split() # Flush
	st = "AH KC QD JD TS".split() # Straight
	tk = "2H 2C 2D AC TD".split() # Three of kind
	tp = "TD 9H TH 7C 9S".split() # Two Pair
	op = "TD TC AD KD QD".split() # One Pair
	hq = "2D 3D 4C 5H 7H".split() # High card
	al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
	tp1 = "7H 7D 9C 3C 9S".split() #Two Pair
	sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
	fkranks = card_ranks(fk)
	tpranks = card_ranks(tp)
	op1 = "KH 7C 5S KS 2S".split() # One pair
	tp2 = "TH 3S 2H 3D TC".split() # Two pair
	tk1 = "TH JD JH 8C JC".split() # Three of kind
	hq1 = "TH 9D 5C 3H 2C".split() # High card
	fk3 = "TC TS TH 2C TD".split() # Four of a Kind
	f3 = "2C 4C 6C 7C TC".split() # Flush
	s3 = "3C 4D 5H 6D 7H".split() # Straight
	assert poker([fk3, f3, s3]) == fk3 
	assert hand_rank(f3) == (5, [10, 7, 6, 4, 2])
	assert flush(f3) == True
	assert straight(card_ranks(s3)) == True
	assert straight(card_ranks(f3)) == False 
	assert hand_rank(tp1) == (2, (9, 7), [9, 9, 7, 7, 3])
	assert kind(1, tpranks) == 7 
	assert card_ranks(fk) == [9, 9, 9, 9, 7]
	assert flush(fl) == True
	assert straight(card_ranks(tp)) == False
	assert hand_rank(tk) == (3, 2, [14, 10, 2, 2, 2])
	assert kind(5, tpranks) == None
	assert poker([sf1] + 50*[fl]) == sf1
	assert hand_rank(sf1) == (8, 10)
	assert straight(card_ranks(al)) == True
	print 'test passed, god job'
	return 'God job :)'
	assert card_ranks(fh) == [10, 10, 10, 7, 7]
test()
