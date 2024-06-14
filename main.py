class Product:
    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price

    def display_info(self):
        print(f'Nome: {self.name}, Código: {self.code}, Preço: R${self.price:.2f}')

# Lista para armazenar produtos
products = []

add = input(f'Você quer adicionar um produto?(s/n) ').strip().upper()

while add == 'S':
    name = input('Nome do produto: ')
    code = input('Código do produto: ')
    price = float(input('Preço do produto:R$ '))

    product = Product(name, code, price)
    products.append(product) # Adiciona o produto a lista

    add = input(f'Você quer adicionar outro produto?(s/n) ').strip().upper()

for product in products:
    product.display_info() # Mostra informações de todos os produtos