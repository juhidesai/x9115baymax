"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""


from __future__ import division
from Card import *

class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            
    def rank_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
            
    def has_pair(self):
        """ pair """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False
        
    def has_twopair(self):
        """ two pair """
        self.rank_hist()
        count=0
        for val in self.ranks.values():
            if val >= 2:
                count+=1
            if count == 2:
                return True
        return False
        
    def has_threeofakind(self):
        """ three of a kind """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False
    
    def has_fourofakind(self):
        """ four of a kind """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False
        
    def has_straight(self):
        # self.rank_hist()
        sorted_ranks = []
        # print self.cards[0].rank
        for card in self.cards:
            sorted_ranks.append(card.rank)
        #sorted_ranks = [1,8,9,10,11,12,13]
        sorted_ranks.sort()
        special_case = [1]
        no_of_cards = len(self.cards)
        for num in range(no_of_cards-1):
            special_case.append(13-num)
        special_case.sort()
        #print "Special case is ",special_case
        if sorted_ranks == special_case:
            return True
        for i in range(len(sorted_ranks)-1):
            if sorted_ranks[i+1] - sorted_ranks[i] != 1:
                return False
        # print sorted_ranks
        return True
    
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
        
    def has_fullhouse(self):
        """ Full house """
        self.rank_hist()
        count3 = 0
        count2 = 0
        for val in self.ranks.values():
            if val >= 3:
                count3+=1
            elif val >=2:
                count2+=1
        if count3 >=1 and count2 >=1:
            return True
        return False
        
    def has_straightflush(self):
        return self.has_straight() and self.has_flush()
        
    def classify(self):
        if self.has_straightflush():
            self.label = "Straight flush"
            #print "Straight Flush : True"
            return
        #print "Straight Flush : False"
        
        if self.has_fourofakind():
            self.label = "4 of a kind"
            #print "4 of a kind : True"
            return
        #print "4 of a kind : False"
        
        if self.has_fullhouse():
            self.label = "Full house"
            #print "Full house : True"
            return
        #print "Full house : False"
        
        if self.has_flush():
            self.label = "Flush"
            #print " Flush : True"
            return
        #print "Flush : False"
        
        if self.has_straight():
            self.label = "Straight"
            #print "Straight : True"
            return
        #print "Straight : False"
        
        if self.has_threeofakind():
            self.label = "3 of a kind"
            #print "Three of a kind : True"
            return
        #print "Three of a kind : False"
        
        if self.has_twopair():
            self.label = "2 pair"
            #print "Two pair : True"
            return
        #print "Two pair : False"
        
        if self.has_pair():
            self.label = "Pair"
            #print "Pair : True"
            return
        #print "Pair : False"
        
        self.label = "None"

def update_classification(label):
     occurences[label] = occurences.get(label,0) + 1
     
def print_classification(n):
    print "No of hands :",no_of_hands
    print "Iterations :",iterations
    print "Classification is :"
    print '{0: <20}{1: <10}{2: <8}'.format("Label","Count","Probability")
    #print "Label\t\t\tCount\tProbability"
    for key in occurences:
        print '{0: <20}{1: < 10}{2: .4f}'.format(key,occurences[key],occurences[key]/(n*iterations))
        #print key,"%s\t\t\t",occurences[key],"\t%.2f"%(occurences[key]/(n*10))
     
def count_classifications(n):
    #deck = Deck()
    #hand = PokerHand()
    # for number in range(n):
    for i in range(n):
        # print 'i is ',i
        deck.shuffle()
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        #print hand
        hand.classify()
        #print hand.label
        #print ''
        update_classification(hand.label)
        #print_classification()
        #print ''
    #print_classification(n)
    
def initialize_occurences():
    occurences["Straight flush"] = 0
    occurences["4 of a kind "] = 0
    occurences["Full house"] = 0
    occurences["Flush"] = 0
    occurences["Straight"] = 0
    occurences["3 of a kind"] = 0
    occurences["2 pair"] = 0
    occurences["Pair"] = 0
    occurences["None"] = 0
    

if __name__ == '__main__':
    # make a deck
    occurences = {}
    iterations = 80000
    no_of_hands = 7
    for j in range(iterations):
        deck = Deck()
        #deck.shuffle()
        count_classifications(no_of_hands)
        
    print_classification(no_of_hands)
    # deal the cards and classify the hands
    for i in []:
    #for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        #cards_test = []
        ## Test for straightflush
        #for i in range(7):
        #    cards_test.append(Card(0,i+3))
        #hand.cards = cards_test
        print hand
        #print hand.has_flush()
        # print hand.has_twopair()
        #print hand.has_threeofakind()
        # print hand.has_straight()
        # print hand.has_fullhouse()
        #print hand.has_fourofakind()
        # print hand.has_straightflush()
        hand.classify()
        print hand.label
        update_classification(hand.label)
        print ''
    #print_classification()
        
    
        

