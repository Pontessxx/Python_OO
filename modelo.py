class Filme:#primeira classe
    def __init__(self, nome, ano, duracao) -> None:
        self.nome = nome.title()
        self.ano = ano
        self.duaracao =duracao
        self.like = 0

    def dar_like(self):
        self.like += 1

class Serie: #manipulação de dados
    def __init__(self, nome, ano, temporadas) -> None: 
        self.nome = nome.title()
        self.ano = ano
        self.temporadas =temporadas
        self.like = 0

    def dar_like(self):
        self.like += 1

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'Nome {vingadores.nome} - Ano: {vingadores.ano} -Temp: {vingadores.duaracao} -Like:{vingadores.like}')

atlanta = Serie('atlanta',2018, 2)
atlanta.dar_like()
print(f'Nome {atlanta.nome} - Ano: {atlanta.ano} -Temp: {atlanta.temporadas} -Like: {atlanta.like}')

