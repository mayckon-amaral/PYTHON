
class Produto():
    def __init__(self,id,nome,tipo,valor): #construtor
        #atributos
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.valor = valor
    def toString(self):     # saida para string
        return f'{self.id}{self.nome}{self.tipo}{self.valor}'

p1 = Produto(1,' televisão',' eleto ', 1000)
p2 = Produto(2,' microondas',' eletro ', 500)
print(p1.toString())
print(p2.toString())
