import pygame, sys
from sys import exit
import random
import button
pygame.init()
screen = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()
game_active = False
player_score = pygame.font.Font(None, 50)
playing_cards = {"ace of clubs" : "image/aceofclubs.png", "ace of dimonds" : "image/aceofdimonds.png", 
"ace of hearts" : "image/aceofhearts.png", "ace of spades" : "image/aceofspades.png",
"eight of clubs" : "image/eightofclubs.png", "eight of dimonds" : "image/eightofdimonds.png", 
"eight of hearts" : "image/eightofhearts.png", "eight of spades" : "image/eightofspades.png", 
"five of clubs" : "image/fiveofclubs.png", "five of dimonds" : "image/fiveofdimonds.png",
"five of hearts" : "image/fiveofhearts.png", "five of spades" : "image/fiveofspades.png",
"four of clubs" : "image/fourofclubs.png", "four of dimonds" : "image/fourofdimonds.png",
"four of hearts" : "image/fourofhearts.png", "four of spades" : "image/fourofspades.png",
"jack of clubs" : "image/jackofclubs.png", "jack of dimonds" : "image/jackofdimonds.png",
"jack of hearts" : "image/jackofhearts.png", "jack of spades" : "image/jackofspades.png",
"king of clubs" : "image/kingofclubs.png", "king of dimonds" : "image/kingofdimonds.png",
"king of hearts" : "image/kingofhearts.png", "king of spades" : "image/kingofspades.png",
"nine of clubs" : "image/nineofclubs.png", "nine of dimonds" : "image/nineofdimonds.png",
"nine of hearts" : "image/nineofhearts.png", "nine of spades" : "image/nineofspades.png",
"queen of clubs" : "image/queenofclubs.png", "queen of dimonds" : "image/queenofdimonds.png",
"queen of hearts" : "image/queenofhearts.png", "queen of spades" : "image/queenofspades.png",
"seven of clubs" : "image/sevenofclubs.png", "seven of dimonds" : "image/sevenofdimonds.png",
"seven of hearts" : "image/sevenofhearts.png", "seven of spades" : "image/sevenofspades.png",
"six of clubs" : "image/sixofclubs.png", "six of dimonds" : "image/sixofdimonds.png",
"six of hearts" : "image/sixofhearts.png", "six of spades" : "image/sixofspades.png",
"ten of clubs" : "image/tenofclubs.png", "ten of dimonds" : "image/tenofdimonds.png",
"ten of hearts" : "image/tenofhearts.png", "ten of spades" : "image/tenofspades.png",
"three of clubs" : "image/threeofclubs.png", "three of dimonds" : "image/threeofdimonds.png",
"three of hearts" : "image/threeofhearts.png", "three of spades" : "image/threeofspades.png",
"two of clubs" : "image/twoofclubs.png", "two of dimonds" : "image/twoofdimonds.png",
"two of hearts" : "image/twoofhearts.png", "two of spades" : "image/twoofspades.png"}


    
   
cards = {"ace of clubs" : 11, "ace of dimonds" : 11, "ace of hearts" : 11, "ace of spades" : 11,
"eight of clubs" : 8, "eight of dimonds" : 8, "eight of hearts" : 8, "eight of spades" : 8, 
"five of clubs" : 5, "five of dimonds" : 5,"five of hearts" : 5, "five of spades" : 5,
"four of clubs" : 4, "four of dimonds" : 4,"four of hearts" : 4, "four of spades" : 4,
"jack of clubs" : 10, "jack of dimonds" : 10,"jack of hearts" : 10, "jack of spades" : 10,
"king of clubs" : 10, "king of dimonds" : 10,"king of hearts" : 10, "king of spades" : 10,
"nine of clubs" : 9, "nine of dimonds" : 9,"nine of hearts" : 9, "nine of spades" : 9,
"queen of clubs" : 10, "queen of dimonds" : 10,"queen of hearts" : 10, "queen of spades" : 10,
"seven of clubs" : 7, "seven of dimonds" : 7,"seven of hearts" : 7, "seven of spades" : 7,
"six of clubs" : 6, "six of dimonds" : 6,"six of hearts" : 6, "six of spades" : 6,
"ten of clubs" : 10, "ten of dimonds" : 10,"ten of hearts" : 10, "ten of spades" : 10,
"three of clubs" : 3, "three of dimonds" : 3,"three of hearts" : 3, "three of spades" : 3,
"two of clubs" : 2, "two of dimonds" : 2,"two of hearts" : 2, "two of spades" : 2}



p_v = 0
dealer_value = 0
player_cards_in_hand = []
dealer_cards_in_hand = []
new_deck = cards.copy()
list_hits = 2
d_list_hits = 2
player_img = []
dealer_img = []
p_ace = []
d_ace = []
    
            
    
def p_deal_cards():
    # Player cards
    
    player_card = random.sample(new_deck.keys(), k=1)
    player_cards_in_hand.append(player_card)
    del new_deck[player_cards_in_hand[0][0]]
    player_card = random.sample(new_deck.keys(), k=1)
    player_cards_in_hand.append(player_card)
    del new_deck[player_cards_in_hand[1][0]]
    card_img = playing_cards[player_cards_in_hand[0][0]]
    card_img2 = playing_cards[player_cards_in_hand[1][0]]
    p_v += cards[player_cards_in_hand[0][0]]
    player_img.append(card_img)
    player_img.append(card_img2)
    p_v += cards[player_cards_in_hand[1][0]]
    return 
    # Dealer cards
    # dealer_card = random.sample(new_deck.keys(), k=1)
    # dealer_cards_in_hand.append(dealer_card)
    # del new_deck[dealer_cards_in_hand[0][0]]
    # dealer_card = random.sample(new_deck.keys(), k=1)
    # dealer_cards_in_hand.append(dealer_card)
    # del new_deck[dealer_cards_in_hand[1][0]]
    # d_card_img = playing_cards[dealer_cards_in_hand[0][0]]
    # d_card_img2 = playing_cards[dealer_cards_in_hand[1][0]]
    # dealer_value += cards[dealer_cards_in_hand[0][0]]
    # dealer_value += cards[dealer_cards_in_hand[1][0]]
    # dealer_img.append(d_card_img)
    # dealer_img.append(d_card_img2)
    # current_points()
    # return 

def current_points():
    global player_value
    aces = "ace of clubs ace of dimonds ace of hearts ace of spades"
    if player_value > 21: 
        for aceses in player_cards_in_hand:    
            if aceses[0] in aces:
                p_ace.append(aceses)
                if aceses not in " ".join(p_ace):
                    player_value = player_value - 10
                    
                else:
                    remove_cards()
                    return 
    return   
                        
            

    
def player_hits():
    global list_hits
    global player_value
    player_card = random.sample(new_deck.keys(), k=1)
    player_cards_in_hand.append(player_card)
    del new_deck[player_cards_in_hand[list_hits][0]]
    player_value = player_value + cards[player_cards_in_hand[list_hits][0]]
    card_img = playing_cards[player_cards_in_hand[list_hits][0]]
    list_hits += 1
    player_img.append(card_img)
    current_points()
    return card_img

def dealer_hits(self):
    dealer_card = random.sample(self.new_deck.keys(), k=1)
    self.dealer_cards_in_hand.append(dealer_card)
    del self.new_deck[self.dealer_cards_in_hand[self.d_list_hits][0]]
    self.dealer_value += self.played_deck.cards[self.dealer_cards_in_hand[self.d_list_hits][0]]
    self.d_list_hits += 1
    self.staying()
    return 
    
# def staying(self):
#     aces = "ace of clubs ace of dimonds ace of hearts ace of spades"
#     ace = 0
#     if self.player_value > 21: 
#         for aceses in self.player_cards_in_hand:    
#             if aceses[self.alist_indx] in aces:
#                 if self.player_value > 21 and ace > 0:
#                     self.player_value -= 10
                    
#                 else:
#                     self.remove_cards()
#                     return
                        
#         self.d_alist_indx += 1 
#     elif self.dealer_value < 21:
#         self.staying()
#             else:
                
#                 self.remove_cards()
#                 return
    
#     elif self.dealer_value < 17:
#         print("\nDealer Hits")
#         self.dealer_hits()
    
#     elif self.dealer_value >= 17:
#         if self.dealer_value > self.player_value:
#             print("\nYou Lose")
#             print(f"\nYour hand {self.player_cards_in_hand}, total {self.player_value}")
#             self.player_ply = False
#             self.dealer_ply = False
#             self.remove_cards()
#         elif self.dealer_value < self.player_value:
#             print("\n!!!! You Win !!!!")
#             print(f"\nYour hand {self.player_cards_in_hand}, total {self.player_value}")
#             self.player_ply = False
#             self.dealer_ply = False
#             self.remove_cards()
#         else:
#             print("\nIt's a Draw")
#             print(f"\nYour hand {self.player_cards_in_hand}, total {self.player_value}")
#             self.player_ply = False
#             self.dealer_ply = False
#             self.remove_cards()


def remove_cards(self):
    self.player_value = 0
    self.dealer_value = 0
    self.list_hits = 1
    self.d_list_hits = 1
    self.player_cards_in_hand.clear()
    self.dealer_cards_in_hand.clear() 
    self.new_deck.clear()
    self.new_deck = self.played_deck.cards.copy()

poker_table_surface = pygame.image.load('image/pokertable.png').convert_alpha()
start_button = pygame.image.load("image/startbutton.png").convert_alpha()
hit_button = pygame.image.load("image/hitbutton.png").convert_alpha()


p_score_surface = player_score.render(f'{p_v}', False, 'Black')
start_btn = button.Button(525, 275, start_button, 1)
ht_btn = button.Button(50, 375, hit_button, 1)
hb = pygame.USEREVENT + 1
pygame.time.set_timer(hb, 10)
show_image = False
show2_image = False
show3_image = False
show4_image = False
dealer_hide_card = True
pressed = 0
while True:
    
    
    
    if game_active == False:
        screen.fill("Blue")
        if start_btn.draw(screen):
            p_deal_cards()
            game_active = True
    
    if game_active:
           
        for event in pygame.event.get():
            screen.blit(poker_table_surface,(0,0))
            screen.blit((p_score_surface), (550,500))    
            screen.blit(pygame.image.load(player_img[0]), (500,300))
            screen.blit(pygame.image.load(player_img[1]), (650,300))
            # screen.blit(pygame.image.load(dealer_img[0]), (500,50))
            # if dealer_hide_card == False:
            #     screen.blit(pygame.image.load("image/backofcards.png"), (650,50))
            # else:
            #     screen.blit(pygame.image.load(dealer_img[1]), (650,50))
        
            if ht_btn.draw(screen):
                player_hits()
                show_image = True
                if pressed == 1:
                    show2_image = True
                    pressed += 1
                elif pressed == 2:
                    show3_image = True
                    pressed += 1
                elif pressed == 3:
                    show4_image = True
                    pressed += 1
                else:
                    pressed += 1
            if show_image:        
                screen.blit(pygame.image.load(player_img[2]), (200,300))
            
            if show2_image:
                screen.blit(pygame.image.load(player_img[3]), (350,300))
            if show3_image:
                screen.blit(pygame.image.load(player_img[4]), (800,300))
            if show4_image:
                screen.blit(pygame.image.load(player_img[5]), (950,300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
            exit()

    pygame.display.update()
    clock.tick(60)


