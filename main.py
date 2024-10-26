from random import shuffle

def createDeck():
  Deck = []

  faceValues = ["A","J","Q","K"]
  for i in range(4):
    for card in range(2,11):
      Deck.append(str(card))

    for card in faceValues:
      Deck.append(card)

  shuffle(Deck)
  return Deck

class player:
  def __init__(self, hand = [], money = 100):
    self.hand = hand
    self.score = self.setScore()
    self.money = money
    self.bet = 0

  def __str__(self):   
    currentHand = "" 
    for card in self.hand:
      currentHand += str(card) + " "

    finalStatus = currentHand + "score: " + str(self.score)
    return finalStatus

  def setScore(self):
    self.score = 0
    faceCardsDict={"A":11,"J":10,"Q":10,"K":10,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}

    aceCounter = 0
    for card in self.hand:
      self.score += faceCardsDict[card]
      if card == "A":
        aceCounter += 1
      if self.score > 21 and aceCounter != 0:
        self.score -= 10
        aceCounter -= 1
      
    return self.score

  def hit(self, card):
    self.hand.append(card)
    self.score = self.setScore()

  def play(self,newHand):
    self.hand = newHand
    self.score = self.setScore()

  def betMoney(self,amount):
    self.money -= amount
    self.bet += amount

  def win(self,result):
    if result == True:
      if self.score == 21 and len(self.hand) == 2:
        self.money += 2.5*self.bet
      else:
        self.money += 2*self.bet
      self.bet = 0

    else:
      self.bet = 0

def printHouse(House):
  for card in range(len(House.hand)):
    if card == 0:
      print("X",end = " ")
    elif card == len(House.hand) - 1:
      print(House.hand[card])
    else:
      print(House.hand[card],end = " ")

cardDeck = createDeck()

firstHand = [cardDeck.pop(),cardDeck.pop()]
secondHand = [cardDeck.pop(),cardDeck.pop()]

Player1 = player(firstHand)
House = player(secondHand)

print(cardDeck)
betQuestion = int(input("How much would you like to bet? "))
if betQuestion > Player1.money:
  print("You don't have enough money to bet that much!")
elif betQuestion <= 0:
  print("You can't bet nothing!")
elif betQuestion <= Player1.money:
  Player1.betMoney(betQuestion)
  print("You bet",betQuestion,"dollars")
printHouse(House)
print(Player1)
x=0

while(True):
  action = input("Do you want another card?(y/n): ")
  if action == "y":
    Player1.hit(cardDeck.pop())
    print(Player1)
    
    if House.score < 17:
      House.hit(cardDeck.pop())
      printHouse(House)
    else:
      printHouse(House)

    if Player1.score > 21:
      print("You lose")
      x = False
      break
    elif Player1.score == 21:
      print("You win")
      x=True
      break
    elif House.score > 21:
      print("House bust")
      x=True
      break
    elif House.score == 21:
      print("House wins")
      x = False
      break
    else:
      continue
      
  else:
    break

print(House)
print("You have",Player1.money, "money left")