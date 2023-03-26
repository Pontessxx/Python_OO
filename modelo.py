class Programa:
    def __init__(self, nome, ano):
        self._nome= nome.title() #_Programa__nome => privado nao vai para classes filhas
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):#classe filha
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duarcao = duracao
        self._likes = 0

class Serie(Programa):#classe filha
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
print(vingadores.nome)

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')