# attributes / properties

# behaviors / methods

# my_lambdata/polos.py


class Polo():
    def __init__(self, color, size, price, style='normal fit'):
        self.color = color
        self.size = size
        self.price = price
        self.style = style

    def fold(self):
        print(f'folding the {self.size.upper()} {self.color.upper()} polo')

if __name__ == "__main__":

    polo = Polo('blue', 'large', 99.99)
    print(polo.color, polo.size, polo.price)
    polo.fold()

    polo2 = Polo(color='Yellow', size='Small', price=69.99)
    print(polo2.color, polo2.size, polo2.price)
    polo2.fold()

    polo3 = Polo(color='Green', size='Medium', price=79.99, style='Fit Cut')
    print(polo3.color, polo3.size, polo3.price)
    polo3.fold()
