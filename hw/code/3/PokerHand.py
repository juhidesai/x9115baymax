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
        """ two pair """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False
        
    def has_straight(self):
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


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        #print hand.has_flush()
        # print hand.has_twopair()
        print hand.has_threeofakind()
        print ''

