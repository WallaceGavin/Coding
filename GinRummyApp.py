#!/usr/bin/env python3

#Gin Rummy Application
#Be able to generate a 52 card deck and shuffle to two players
#Give logic and allow picking of options
#BONUS: allow the program to learn from mistakes - a little ML

import io
import base64
import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#def combinations(n, k):
#	combinations = math.factorial(n) // (math.factorial(k) * (n - math.factorial(k))
#	return combinations

#conditional probabilities = n! / (k!(n-k!)

cards_in_deck = 52
number_suits = 4
selection_options = 1

ranks = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

def generate_deck():
	deck = []
	for suit in suits:
		for rank in ranks:
			deck.append(f'{rank} of {suit}')
	return deck 

#shuffle the using Fisher-Yates for shuffling an infinite # while random is Mersenne Twister method (not cryptographically secure)
def shuffle_deck(deck):
	#shuffle deck 7 times (min of 4 but 7 is ideal in a casino realm
	random.shuffle(deck)
	random.shuffle(deck)
	random.shuffle(deck)
	random.shuffle(deck)
	random.shuffle(deck)
	random.shuffle(deck)
	random.shuffle(deck)
	return deck 

#deal the cards to players
def deal_cards(deck, num_cards):
	return [deck.pop() for _ in range(num_cards)]

#simplified setup
def simple():
	deck = generate_deck()
	print(f"Initial Box Order Deck: \n{deck}\n")
	
	shuffled_deck = shuffle_deck(deck)
	print(f"Shuffled deck (Shuffled 7 times): \n{shuffled_deck}\n")
	
	print(f"Gutter card is {shuffled_deck[0]}")
	
	first = shuffled_deck[1],shuffled_deck[3],shuffled_deck[5],shuffled_deck[7],shuffled_deck[9],shuffled_deck[11],shuffled_deck[13],shuffled_deck[15],shuffled_deck[17],shuffled_deck[19]
	second = shuffled_deck[2],shuffled_deck[4],shuffled_deck[6],shuffled_deck[8],shuffled_deck[10],shuffled_deck[12],shuffled_deck[14],shuffled_deck[16],shuffled_deck[18],shuffled_deck[20]
	print(first)
	print(second)
	
print(simple())