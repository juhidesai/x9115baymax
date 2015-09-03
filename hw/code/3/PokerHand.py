"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

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
        if hand.has_straightflush():
            self.label = "Straight Flush"
            return
        
        if hand.has_fourofakind():
            self.label = "4 of a kind"
            return
        
        if hand.has_fullhouse():
            self.label = "full house"
            return
        
        if hand.has_flush():
            self.label = "Flush"
            return
        
        if hand.has_straight():
            self.label = "Straight"
            return
        
        if hand.has_threeofakind():
            self.label = "3 of a kind"
            return
        
        if hand.has_twopair():
            self.label = "2 pair"
            return
        
        if hand.has_pair():
            self.label = "measley pair"
            return
        
        
        

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        cards_test = []
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
        print ''
        

