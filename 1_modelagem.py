class Pessoas:
    possui_olho = True
    possui_boca = True
    raca = "Ser humano"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome()} Está logando no sistema')

    @classmethod
    def andar(cls):
        cls.possui_boca = False
        return None

    @staticmethod
    def e_adulto(idade):
        if idade > 18:
            return True
        return False
    

#p1 = Pessoas("Caio Sampaio", 21)
#p2 = Pessoas('Marcos Sampaio', 45)

print(Pessoas.e_adulto(21))







