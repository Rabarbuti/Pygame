from importlib_metadata import files


def lists_formation(complete_list):
    row_A = []
    row_B = []
    row_C = []

    partial_list = complete_list

    for i in range(0, 21, 3):
        row_A.append(partial_list[i])
    for j in range(1, 21, 3):
        row_B.append(partial_list[j])
    for k in range(2, 21, 3):
        row_C.append(partial_list[k])

    return row_A, row_B, row_C


def positioning(row_A, row_B, row_C, correct_column):
    choice = correct_column
    deck_of_cards = []

    if choice == "A":
        for i in row_B:
            deck_of_cards.append(i)
        for j in row_A:
            deck_of_cards.append(j)
        for k in row_C:
            deck_of_cards.append(k)
    if choice == "B":
        for i in row_A:
            deck_of_cards.append(i)
        for j in row_B:
            deck_of_cards.append(j)
        for k in row_C:
            deck_of_cards.append(k)
    if choice == "C":
        for i in row_B:
            deck_of_cards.append(i)
        for j in row_C:
            deck_of_cards.append(j)
        for k in row_A:
            deck_of_cards.append(k)

    return deck_of_cards


def colors():
    return {"white": (255, 255, 255),
            "dark_orange": (201, 90, 10),
            "light_orange": (245, 127, 10),
            "dark_purple": (110, 60, 128),
            "light_purple": (145, 17, 171),
            }

def cards():
    cards ={'10_of_clubs' : '10_of_clubs.png',
    '10_of_diamonds' : '10_of_diamonds.png',      
    '10_of_hearts' : '10_of_hearts.png',
    '10_of_spades' : '10_of_spades.png',
    '2_of_clubs' : '2_of_clubs.png',
    '2_of_diamonds' : '2_of_diamonds.png',        
    '2_of_hearts' : '2_of_hearts.png',
    '2_of_spades' : '2_of_spades.png',
    '3_of_clubs' : '3_of_clubs.png',
    '3_of_diamonds' : '3_of_diamonds.png',        
    '3_of_hearts' : '3_of_hearts.png',
    '3_of_spades' : '3_of_spades.png',
    '4_of_clubs' : '4_of_clubs.png',
    '4_of_diamonds' : '4_of_diamonds.png',        
    '4_of_hearts' : '4_of_hearts.png',
    '4_of_spades' : '4_of_spades.png',
    '5_of_clubs' : '5_of_clubs.png',
    '5_of_diamonds' : '5_of_diamonds.png',        
    '5_of_hearts' : '5_of_hearts.png',
    '5_of_spades' : '5_of_spades.png',
    '6_of_clubs' : '6_of_clubs.png',
    '6_of_diamonds' : '6_of_diamonds.png',        
    '6_of_hearts' : '6_of_hearts.png',
    '6_of_spades' : '6_of_spades.png',
    '7_of_clubs' : '7_of_clubs.png',
    '7_of_diamonds' : '7_of_diamonds.png',        
    '7_of_hearts' : '7_of_hearts.png',
    '7_of_spades' : '7_of_spades.png',
    '8_of_clubs' : '8_of_clubs.png',
    '8_of_diamonds' : '8_of_diamonds.png',        
    '8_of_hearts' : '8_of_hearts.png',
    '8_of_spades' : '8_of_spades.png',
    '9_of_clubs' : '9_of_clubs.png',
    '9_of_diamonds' : '9_of_diamonds.png',        
    '9_of_hearts' : '9_of_hearts.png',
    '9_of_spades' : '9_of_spades.png',
    'ace_of_clubs' : 'ace_of_clubs.png',
    'ace_of_diamonds' : 'ace_of_diamonds.png',    
    'ace_of_hearts' : 'ace_of_hearts.png',        
    'ace_of_spades' : 'ace_of_spades.png',        
    'jack_of_clubs' : 'jack_of_clubs.png',        
    'jack_of_diamonds' : 'jack_of_diamonds.png',  
    'jack_of_hearts' : 'jack_of_hearts.png',      
    'jack_of_spades' : 'jack_of_spades.png',      
    'king_of_clubs' : 'king_of_clubs.png',
    'king_of_diamonds' : 'king_of_diamonds.png',  
    'king_of_hearts' : 'king_of_hearts.png',      
    'king_of_spades' : 'king_of_spades.png',      
    'queen_of_clubs' : 'queen_of_clubs.png',      
    'queen_of_diamonds' : 'queen_of_diamonds.png',
    'queen_of_hearts' : 'queen_of_hearts.png',    
    'queen_of_spades' : 'queen_of_spades.png',
    }
    return cards
