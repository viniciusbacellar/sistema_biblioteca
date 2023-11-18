from Livro import Livro
from Biblioteca import Biblioteca

def menu():
    print("\nMenu:")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Listar Livros por Autor")
    print("4. Listar Livros por Gênero")
    print("5. Salvar Dados")
    print("6. Carregar Dados")
    print("0. Sair")

if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = input("Ano de publicação do livro: ")
            genero = input("Gênero do livro: ")

            livro = Livro(titulo, autor, ano, genero)
            biblioteca.cadastrar_livro(livro)

        elif opcao == "2":
            titulo = input("Digite o título do livro para consultar: ")
            resultado = biblioteca.consultar_livro(titulo)
            print(resultado)

        elif opcao == "3":
            autor = input("Digite o nome do autor para listar os livros: ")
            resultado = biblioteca.listar_livros_por_autor(autor)
            print(resultado)

        elif opcao == "4":
            genero = input("Digite o gênero para listar os livros: ")
            resultado = biblioteca.listar_livros_por_genero(genero)
            print(resultado)

        elif opcao == "5":
            nome_arquivo = input("Digite o nome do arquivo para salvar os dados: ")
            biblioteca.salvar_dados(nome_arquivo + ".json")

        elif opcao == "6":
            nome_arquivo = input("Digite o nome do arquivo para carregar os dados: ")
            biblioteca.carregar_dados(nome_arquivo + ".json")

        elif opcao == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")