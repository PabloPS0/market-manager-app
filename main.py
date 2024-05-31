class Product:
    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price
    def display_info(self):
        print(f'Nome: {self.name}, Código: {self.code}, Preço: R${self.price:.2f}')
    def add_data(self):
        self.data = input("Insira a data de fabricação (DD/MM/YYYY): ")
        print(f'Data de fabricação: {self.data}')

data()