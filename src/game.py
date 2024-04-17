import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = [
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)

    def dealCard(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def addCard(self, card):
        self.cards.append(card)
        self.calculateValue()

    def calculateValue(self):
        self.value = 0
        hasAce = False
        for card in self.cards:
            if card.rank.isdigit():
                self.value += int(card.rank)
            elif card.rank in ["Jack", "Queen", "King"]:
                self.value += 10
            else:
                hasAce = True
                self.value += 11
        if hasAce and self.value > 21:
            self.value -= 10

    def display(self):
        for card in self.cards:
            print(card)
        print(f"Total Value: {self.value}")


class Game:
    def __init__(self):
        self.deck = Deck()
        self.playerHand = Hand()
        self.dealerHand = Hand()

    def startGame(self):
        print("Welcome to Blackjack!")
        self.playerHand.addCard(self.deck.dealCard())
        self.playerHand.addCard(self.deck.dealCard())
        self.dealerHand.addCard(self.deck.dealCard())
        self.dealerHand.addCard(self.deck.dealCard())

        self.playerTurn()

    def playerTurn(self):
        while True:
            print("\nYour Hand:")
            self.playerHand.display()
            choice = input("Do you want to hit or stand? (h/s): ").lower()
            if choice == "h":
                self.playerHand.addCard(self.deck.dealCard())
                if self.playerHand.value > 21:
                    print("Busted! You lose.")
                    self.endGame()
            elif choice == "s":
                self.dealerTurn()
                break
            else:
                print("Invalid choice. Please enter 'h' to hit or 's' to stand.")

    def dealerTurn(self):
        print("\nDealer's Hand:")
        self.dealerHand.display()
        while self.dealerHand.value < 17:
            self.dealerHand.addCard(self.deck.dealCard())
        if self.dealerHand.value > 21 or self.dealerHand.value < self.playerHand.value:
            print("You win!")
        elif self.dealerHand.value > self.playerHand.value:
            print("Dealer wins!")
        else:
            print("It's a tie!")
        self.endGame()

    def endGame(self):
        playAgain = input("\nDo you want to play again? (y/n): ").lower()
        if playAgain == "y":
            self.deck = Deck()
            self.playerHand = Hand()
            self.dealerHand = Hand()
            self.startGame()
        else:
            print("Thanks for playing!")


if __name__ == "__main__":
    game = Game()
    game.startGame()
