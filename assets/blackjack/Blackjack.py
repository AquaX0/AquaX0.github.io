import random

Ace = int(input("the value of ace [1/11] : "))
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
def card_value(card, player=False):
    """Returns the value of a card and handles Ace value selection."""
    if card in ['Jack', 'Queen', 'King', 'J', 'Q', 'K']:
        return 10
    elif card in ['Ace', 'A']:
        return Ace
    else:
        return int(card)

def print_results(player, dealer, player_score, dealer_score):
    print(f"Dealer's cards: {dealer}, score: {dealer_score}")
    print(f"Your cards: {player}, score: {player_score}")
    
    if player_score > 21:
        print("You busted! Dealer wins.")
    elif dealer_score > 21:
        print("Dealer busted! Player wins.")
    elif player_score > dealer_score:
        print("Player wins!")
    elif dealer_score > player_score:
        print("Dealer wins!")
    else:
        print("It's a tie.")

while True:
    player = [random.choice(cards), random.choice(cards)]
    dealer = [random.choice(cards), random.choice(cards)]
    player_score = sum(card_value(card, player) for card in player)
    dealer_score = sum(card_value(card, dealer) for card in dealer)
    print(f"Your cards: {player}, score: {player_score}")
    print(f"Dealer's face-up card: {dealer[0]}")
    if player_score == 21 and len(player) == 2:
        print_results(player, dealer, player_score, dealer_score)
        option = input("Continue [y/n]: ").lower()
        if option == "y":
            print("\nNew round starting...\n")
            continue
        else:
            break
    while True:
        if player_score > 21: 
            print_results(player, dealer, player_score, dealer_score)
            break
        choice = input("Hit or Stand: ").lower()
        if choice == "hit":
            new_card = random.choice(cards)
            player.append(new_card)
            player_score = sum(card_value(card, player) for card in player)
            print(f"\nYour cards: {player}, score: {player_score}\n")
            if player_score == 21: 
                print_results(player, dealer, player_score, dealer_score)
                break
        elif choice == "stand":
            break
        else:
            print("Invalid choice. Please try again.")
    if player_score > 21:
        option = input("Continue [y/n]: ").lower()
        if option == "y":
            print("\nNew round starting...\n")
            continue
        else:
            break
    while dealer_score < 17:
        new_card = random.choice(cards)
        dealer.append(new_card)
        dealer_score += card_value(new_card, dealer)
    print_results(player, dealer, player_score, dealer_score)
    option = str(input("Continue [y/n] : ").lower())
    if option == "y":
        print("\nNew round starting\n")
    else:
        break