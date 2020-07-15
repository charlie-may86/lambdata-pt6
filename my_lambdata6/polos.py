# attributes / properties

# behaviors / methods

# my_lambdata/polos.py

# This is a class
class Polo():
    def __init__(self, color, size, price, style='normal fit'):
        # These are attributes
        self.color = color
        self.size = size
        self.price = price
        self.style = style

    # This a method
    def fold(self):
        print(f'folding the {self.size.upper()} {self.color.upper()} polo')

if __name__ == "__main__":

    # This is an instance of the Polo class
    polo = Polo('blue', 'large', 99.99)
    print(polo.color, polo.size, polo.price)
    # Applying a method to the polo class
    polo.fold()

    polo2 = Polo(color='Yellow', size='Small', price=69.99)
    print(polo2.color, polo2.size, polo2.price)
    polo2.fold()

    polo3 = Polo(color='Green', size='Medium', price=79.99, style='Fit Cut')
    print(polo3.color, polo3.size, polo3.price)
    polo3.fold()
