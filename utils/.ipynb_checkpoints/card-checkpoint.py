"""
Create a class called `Symbol` with two attributes:
- `color` which is a string.
- `icon` which is a string: [♥, ♦, ♣, ♠]
"""

class Symbol:
    def __init__(self, color: str, icon:[str] = [♥, ♦, ♣, ♠]:
        self.color = color
        self.icon = icon
        
    def __str__ (self):
        return f"{self.color} {self.icon}"
    
A=Symbol('color','♥')
print (A)