# -*- coding: utf-8 -*-
from graph import Graph

# Lista de arquivos permitidos
ALLOWED_FILES = ["pcv4.txt", "pcv10.txt", "pcv50.txt", "pcv177.txt"]

def load_from(fileName):
    with open(fileName, 'r', encoding='utf-8') as f:
        n = int(f.readline())
        g = Graph(n)
        l = 0
        for line in f:
            line = line.strip()
            numeros = line.split("\t")
            c = 0
            for i in numeros:
                if c == n:
                    break
                num = int(i)
                g.M[l][c] = num
                if num != 0:
                    g.L[l].append(c)
                c += 1
            l += 1
    return g

def choose_file():
    print("Escolha um arquivo entre as opções:")
    for idx, filename in enumerate(ALLOWED_FILES):
        print(f"{idx+1}. {filename}")
    escolha = input("Digite o número correspondente ao arquivo desejado: ")
    try:
        escolha = int(escolha)
        if escolha < 1 or escolha > len(ALLOWED_FILES):
            print("Opção inválida. Encerrando...")
            exit(1)
    except ValueError:
        print("Entrada inválida. Encerrando...")
        exit(1)
    return ALLOWED_FILES[escolha - 1]

def show_menu():
    print("\nMenu de Ações:")
    print(" 1 - Imprimir a representação do grafo")
    print(" 2 - Mostrar número de componentes conectados")
    print(" 3 - Caminho BFS entre dois vértices")
    print(" 4 - DFS iterativa a partir de um vértice")
    print(" 5 - Encerrar")
    acao = input("Digite o número da ação desejada: ")
    return acao

def main():
    selected_file = choose_file()
    print("\nArquivo selecionado:", selected_file)
    
    try:
        g = load_from(selected_file)
    except Exception as e:
        print(f"Erro ao carregar o arquivo {selected_file}: {e}")
        exit(1)
    
    while True:
        acao = show_menu()
        if acao == "1":
            g.print()
        elif acao == "2":
            num_components = g.num_comp()
            print("\nNúmero de Componentes:", num_components)
        elif acao == "3":
            try:
                s = int(input("Digite o vértice de origem (s): "))
                t = int(input("Digite o vértice destino (t): "))
            except ValueError:
                print("Entrada inválida para vértices.")
                continue
            print(f"\nCaminho BFS entre os vértices {s} e {t}:")
            g.print_bfs_path(s, t)
        elif acao == "4":
            try:
                start = int(input("Digite o vértice de início para DFS iterativa: "))
            except ValueError:
                print("Entrada inválida para vértice.")
                continue
            print(f"\nDFS Iterativa a partir do vértice {start}:")
            g.dfs_iterative(start)
        elif acao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
