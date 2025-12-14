class Card:
  def __init__(self, rank, suit, face_up = False):
      self.rank = rank
      self.suit = suit
      self.face_up = face_up

  def flip_card_face(self):
      self.face_up = True

  def show_card(self):
      if self.face_up == True:
          card = self.rank, self.suit
          print( f"{card}")
          return card

class Deck:
  def __init__(self):
      self.deck = []
    
  def create_deck(self, meaning, suit):
      for i in suit:
        for j in meaning:
         self.deck.append(Card(i,j))
      return self.deck

  def shuffle_deck(self):
      random.shuffle(self.deck)

class Pile:
  def __init__(self):
      self.pile = []

  def push(self, card):
      self.pile.append(card)

  def pop_cards(self):
     return self.pile.pop()


class Table:
  def __init__(self):
      self.table_1 = []
      self.table_2 = []
      self.table_3 = []
      self.table_4 = []

  def check_card(self, table):
      if len(table) > 0:
          top_card = table[-1]
          print(f"The top card of {table} is {top_card}")
          return top_card
      else:
          print(f"The {table} if empty. No cards to show")
    
class Game:
  def __init__(self):
    self.deck = Deck()
    meaning = ['6', '7', '8', '9', '10', 'B', 'Д', 'К', 'Т']
    suit = ['♥', '♦', '♣', '♠']
    self.deck.create_deck(meaning, suit)
    self.deck.shuffle_deck()
    self.table = Table()
    self.table.check_card(self.table.table_1)

    self.piles = []
    for i in range(7):
          self.piles.append(Pile())
    
    for i in range(7):
          for j in range(i+1):
              card = self.deck.deck.pop()   
              self.piles[i].pile.append(card)
    
