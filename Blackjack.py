import random
import time
import os

class Blackjack:
    def __init__(self):
        self.reset_game()  # Initialize deck, hand, and house
        random.shuffle(self.deck)

    def reset_game(self, delay=False):
        # Create a standard deck: Ace (1), numbers 2-10, and face cards as 10 (each repeated 4 times)
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        self.hand = 0
        self.house = 0
        if delay:
            time.sleep(1)

    def draw(self, current_total):
        if not self.deck:
            raise ValueError("The deck is empty. Cannot draw a card.")
        card = random.choice(self.deck)
        self.deck.remove(card)
        # Ace handling: if card is Ace, choose 11 if it doesn't cause a bust
        if card == 1:
            return 11 if current_total + 11 <= 21 else 1
        return card

    def hit(self):
        # Draw a card using the current player's hand total for Ace logic
        card = self.draw(self.hand)
        self.hand += card
        return card

    def house_hit(self):
        # Draw a card using the house's current hand total for Ace logic
        card = self.draw(self.house)
        self.house += card
        return card


def play_round(game):
    game.reset_game()
    
    # Player draws two cards
    game.hand += game.draw(game.hand)
    game.hand += game.draw(game.hand)
    print(f"Your hand: {game.hand}")

    # Dealer (house) draws two cards
    house_card1 = game.house_hit()  # visible
    house_card2 = game.house_hit()  # hole card, hidden for now
    print(f"House's visible card: {house_card1}")
    # We do NOT show house_card2 yet in a real Blackjack scenario.

    # Player's turn
    while game.hand < 21:
        choice = input("\nHit or stand? (h/s): ").lower()
        if choice == 'h':
            new_card = game.hit()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"You drew {new_card}.\nYour hand: {game.hand}\n")
            if game.hand > 21:
                print("Bust! You lose.")
                return
        elif choice == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Invalid input. Enter 'h' to hit or 's' to stand.")


    print(f"\nHouse's total is now: {game.house}")

    # Dealer draws until total >= 17
    while game.house < game.hand:
        new_card = game.house_hit()
        time.sleep(2)
        print(f"House draws {new_card}. House's hand: {game.house}")

    # Compare hands
    if game.house > 21:
        print(f"House busts! You win. | Your hand: {game.hand} || House's hand: {game.house}")
    elif game.house == game.hand:
        print(f"It's a tie! | Your hand: {game.hand} || House's hand: {game.house}")
    elif game.house > game.hand:
        print(f"House wins! | Your hand: {game.hand} || House's hand: {game.house}")
    else:
        print(f"You win! | Your hand: {game.hand} || House's hand: {game.house}")



# Game loop
game = Blackjack()
while True:
    play_round(game)
    exit_choice = input("\nPlay again? (y/n): ").lower()
    if exit_choice == 'n':
        print("Thanks for playing!")
        exit_choice = False
        break
    elif exit_choice == 'y':
        exit_choice = True
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for better visibility