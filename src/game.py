import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Kőr", "Káró", "Pikk", "Treff"]
        ranks = [
            "Két",
            "Három",
            "Négy",
            "Öt",
            "Hat",
            "Hét",
            "Nyolc",
            "Kilenc",
            "Tíz",
            "Jumbó",
            "Dáma",
            "Király",
            "Ász",
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
            elif card.rank in ["Jumbó", "Dáma", "Király"]:
                self.value += 10
            else:
                hasAce = True
                self.value += 11
        if hasAce and self.value > 21:
            self.value -= 10

    def display(self):
        for card in self.cards:
            print(card)
        print(f"Összérték: {self.value}")


class Game:
    def __init__(self):
        self.deck = Deck()
        self.playerHand = Hand()
        self.dealerHand = Hand()

    def startGame(self):
        print("Üdvözöllek a játékban!")
        self.playerHand.addCard(self.deck.dealCard())
        self.playerHand.addCard(self.deck.dealCard())
        self.dealerHand.addCard(self.deck.dealCard())
        self.dealerHand.addCard(self.deck.dealCard())

        self.playerTurn()

    def playerTurn(self):
        while True:
            print("\nA lapjaid:")
            self.playerHand.display()
            choice = input("Kérsz egy új lapot vagy tovább? (k/t): ").lower()
            if choice == "k":
                self.playerHand.addCard(self.deck.dealCard())
                if self.playerHand.value > 21:
                    print("Túllépted a 21-et! Vesztettél.")
                    self.endGame()
            elif choice == "t":
                self.dealerTurn()
                break
            else:
                print(
                    "Érvénytelen válasz. Kérlek válassz 'k'-t a lapkéréssel vagy 't'-t hogy tovább lépj."
                )

    def dealerTurn(self):
        print("\nAz osztó lapjai:")
        self.dealerHand.display()
        while self.dealerHand.value < 17:
            self.dealerHand.addCard(self.deck.dealCard())
        if self.dealerHand.value > 21 or self.dealerHand.value < self.playerHand.value:
            print("Nyertél!")
        elif self.dealerHand.value > self.playerHand.value:
            print("Az osztó nyert!")
        else:
            print("Döntetlen!")
        self.endGame()

    def endGame(self):
        playAgain = input("\nSzeretnél egy új meccset játszani? (i/n): ").lower()
        if playAgain == "i":
            self.deck = Deck()
            self.playerHand = Hand()
            self.dealerHand = Hand()
            self.startGame()
        else:
            print("Köszönöm, hogy játszottál!")


if __name__ == "__main__":
    game = Game()
    game.startGame()
