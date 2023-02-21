import random
import pygame, sys

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and click conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


class Card:
    rank = ["two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace"]
    suit = ["clubs", "dimonds", "hearts", "spades"]
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{Card.rank[self.rank]} of {Card.suit[self.suit]}"

class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(13):
                self.deck.append(Card(suit, rank))
        self.shuffle()
    def __len__(self):
        return len(self.deck)
    
    def add_card(self, card):
        self.deck.append(card)

    def pop_card(self):
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)

class Hand(Deck):
    def __init__(self, label):
        self.deck = []
        self.label = label
        self.win_count = 0

    def __str__(self):
        return 

    def get_label(self):
        return self.label

    def get_win_count(self):
        return self.win_count

    def round_winner(self):
        self.win_count = self.win_count + 1



