class Filme:#primeira classe
    def __init__(self, nome, ano, duracao, like) -> None:
        self.nome = nome
        self.ano =ano
        self.duaracao =duracao
        self.like = like

class Serie: #manipulação de dados
     def __init__(self, nome, ano, temporadas, like) -> None: 
        self.nome = nome
        self.ano =ano
        self.temporadas =temporadas
        self.like = like 

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'Nome {vingadores.nome} - Ano: {vingadores.ano} -Temp: {vingadores.duaracao}')

atlanta = Serie('atlanta',2018, 2)
print(f'Nome {atlanta.nome} - Ano: {atlanta.ano} -Temp: {atlanta.temporadas}')

