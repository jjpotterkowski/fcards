from __future__ import print_function
import random
import csv
import os

# Re-seed random number generator
random.seed()


class Deck():
    
    def __init__(self, first_side='front'):
        self.num_cards = 0
        assert first_side in ['front', 'back', 'random', 'f', 'b', 'r']
        if first_side in ['front', 'f']:
            self.first_side = 'front'
        elif first_side in ['back', 'b']:
            self.first_side = 'back'
        else: self.first_side = 'random'
        self.cards = []
    
    def add_cards(self, deck_list):
        for deck in deck_list:
            deck_file = os.path.join('decks', deck+'.csv')
            card_data = read_from_csv(deck_file)
            for card_num in range(len(card_data['front'])):
                CARD = {'front':card_data['front'][card_num],
                        'back':card_data['back'][card_num],
                        'more':card_data['more'][card_num]}
                self.cards.append(CARD)

    def draw_cards(self, num_cards):
        if num_cards == 0:
            num_cards = len(self.cards)
        cards_copy = list(self.cards)
        card_num = 1
        while (card_num <= num_cards) and (len(cards_copy) > 0):
            drawn_card_num = random.randint(0, len(cards_copy)-1)
            drawn_card = cards_copy.pop(drawn_card_num)
            print("")
            print(str(card_num) + ".")
            self.show_card(drawn_card)
            card_num = card_num + 1
        print("")

    def show_card(self, card):
        random_bool = random.randint(0, 1)
        if (self.first_side == 'front') or (
                (self.first_side == 'random') and random_bool):
            side_order = ['front', 'back', 'more']
        elif (self.first_side == 'back') or (
                (self.first_side == 'random') and not random_bool):
            side_order = ['back', 'front', 'more']
        input(card[side_order[0]])
        input(card[side_order[1]])
        if card[side_order[2]] != "":
            input(card[side_order[2]])


def read_from_csv(file_name):
    with open(file_name, encoding='utf-8') as csv_file:
        CSVREADER = csv.reader(csv_file)
        DATA = {}
        row_num = 0
        for row in CSVREADER:
            if row_num == 0:
                num_cols = len(row)
                col_headers = row
                for col in range(0, num_cols):
                    DATA[col_headers[col]] = []
            else:
                for col in range(0, num_cols):
                    DATA[col_headers[col]].append(row[col])
            row_num = row_num + 1
    return DATA


if __name__ == '__main__':
    DECK = Deck()
    DECK.add_cards(deck_list=['test_deck'])
    DECK.draw_cards(0)
