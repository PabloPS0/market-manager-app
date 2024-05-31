class Product:
    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price
    def display_info(self):
        print(f'Nome: {self.name}, Código: {self.code}, Preço: R${self.price:.2f}')