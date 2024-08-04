from modules.time_module import sleep
import modules.list_util as lu
class Product:
    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price

    def display_info(self):
        print(f'Nome: {self.name}, Código: {self.code}, Preço: R${self.price:.2f}')

class Menu:
    def __init__(self):
        self.products = [] # Array
    
    def add_product(self):
        name = input('Nome do produto: ')
        code = input('Código do produto: ')
        price = float(input('Preço do produto: R$ '))

        product = Product(name, code, price)
        self.products.append(product) # Adiciona produto a lista
        print('Produto adicionado com sucesso!\n')

    def remove_product(self):
        code = input('Código do produto a ser removido: ')
        for product in self.products:
            if product.code == code:
                product.display_info()
                confirm = input('Você deseja realmente deletar esse produto?[s/n] ')
                if confirm.lower() == 's':
                    sleep(3)
                    self.products.remove(product)
                    print('Produto removido com sucesso!\n')
                    print('Sistema atualizado:')
                    product.display_info()
                    print('\n')
                elif confirm.lower == 'n':
                    sleep(3)
                    print('Operação cancelada.\n')
                else:
                    sleep(3)
                    print('Opção inválida.\n')

    def search_product(self):
        code = input('Código: ')
        for product in self.products:
            if product.code == code:
                print('Buscando produto...')
                sleep(3)
                print('Produto encontrado.\n')
                product.display_info()
                return
        print('Produto não encontrado.\n')

    def display_products(self):
        if not self.products:
            print('Não há produtos cadastrados.\n')
        else:
            for product in self.products: # Percorre a lista de produtos(products)
                product.display_info() # Mostra informações de cada produto
            print()

    def show_menu(self):
        print("Selecione uma opção:")
        print("1 - Adicionar Novo Produto")
        print("2 - Exibir Todos os Produtos")
        print("3 - Pesquisar Produto")
        print("4 - Deletar produto")
        print("5 - Sair")
        return input('Opção: ')

    def main(self):
        while True:
            option = self.show_menu()
            if option == '1':
                self.add_product()
            elif option == '2':
                self.display_products()
            elif option == '3':
                self.search_product()
            elif option == '4':
                self.remove_product()
            elif option == '5':
                print('Saindo do programa...')
                sleep(3)
                break
            else:
                print('Opção inválida. Tente novamente.\n')

if __name__ == "__main__":
    menu = Menu()
    menu.main()