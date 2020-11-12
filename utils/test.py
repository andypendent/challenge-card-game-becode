import random
card_icon = ["♥", "♦", "♣", "♠"]
card_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random_icon = random.choice (card_icon)
random_value = random.choice (card_value)
pick = random_icon, random_value
print (pick)