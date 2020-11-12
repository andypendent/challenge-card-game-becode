"""
Create a class called `Symbol` with two attributes:
- `color` which is a string.
- `icon` which is a string: [♥, ♦, ♣, ♠]
"""

class Symbol:
    def __init__ (self, color: str, icon: str):
        
        if color not in ["black", "red"]:
            raise ValueError (color)    
        self.color = color

        if icon not in ["♥", "♦", "♣", "♠"]: 
            raise ValueError (icon)   
        self.icon = icon
 
    def __str__ (self):
        return f"{self.color} {self.icon}"
    
""""
create a class `Card` that **inherits** from `Symbol` and add an attribute:
- `value` which is a string. *(it can be 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K')*
"""

class Card (Symbol):
    def __init__ (self, color: str , icon: str, value: str):
        
        super().__init__(color, icon)
        
        if value not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
            raise ValueError (value)
        self.value = value

    def __str__ (self):
        return f"{self.color} {self.icon} {self.value}"

"""
A = Card ("red","♦","2")
print (A)
"""