import json
from Livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = {}

    def cadastrar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def consultar_livro(self, titulo):
        if titulo in self.livros:
            return str(self.livros[titulo])
        else:
            return "Livro não encontrado."

    def listar_livros_por_autor(self, autor):
        livros_autor = [livro for livro in self.livros.values() if livro.autor == autor]
        if livros_autor:
            return [str(livro) for livro in livros_autor]
        else:
            return "Nenhum livro encontrado para esse autor."

    def listar_livros_por_genero(self, genero):
        livros_genero = [livro for livro in self.livros.values() if livro.genero == genero]
        if livros_genero:
            return [str(livro) for livro in livros_genero]
        else:
            return "Nenhum livro encontrado para esse gênero."

    def salvar_dados(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            dados = {livro.titulo: (livro.autor, livro.ano, livro.genero) for livro in self.livros.values()}
            json.dump(dados, arquivo)

    def carregar_dados(self, nome_arquivo):
        livrosCarregados = []
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            for titulo, info in dados.items():
                autor, ano, genero = info
                livro = Livro(titulo, autor, ano, genero)
                livrosCarregados.append(livro)
                self.cadastrar_livro(livro)

            print()
            print("Livros Carregados:")
            for livro in livrosCarregados:
                print(livro)