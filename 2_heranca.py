class Pessoa:

    
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Estou falando')

class Cliente(Pessoa):
    

    def comprar(self):
        print('Estou comprando')

class Vendedor(Pessoa):


    def vender(self):
        print('Estou vendendo')





v1 = Vendedor()

v1.andar()
v1.falar()
v1.vender()
v1.comprar()