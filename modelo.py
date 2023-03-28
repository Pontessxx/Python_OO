class programa:
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

    def __str__(self):
        return f'{self._nome} - {self.ano}: {self._likes}'

class Filme(programa):#classe filha
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
      return f'{self._nome} - {self.ano} - {self.duracao} min: {self._likes}'

class Serie(programa):#classe filha
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temp: {self._likes}'

class Playlist:#list é um bult-in
    def __init__(self, nome, programas):
       self.nome = nome
       self._programas = programas
    @property
    def listagem(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('toto mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016,2)

vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]#lista
playtist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playtist_fim_de_semana.listagem)}')#onjeto que verifica o tamanho

for programa in playtist_fim_de_semana.listagem:
    print(programa)

print(f'Está ou não esta? {demolidor in playtist_fim_de_semana}')