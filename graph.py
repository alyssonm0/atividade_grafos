# -*- coding: utf-8 -*-
import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.M = [[0 for _ in range(n)] for _ in range(n)]
        self.L = [[] for _ in range(n)]

    def print(self):
        print("Número de Vértices:", self.num_vertices)
        print("Matriz de Adjacência:")
        for row in self.M:
            print(row)
        print("Lista de Adjacência:")
        for i, adj in enumerate(self.L):
            print(f"{i}: {adj}")
    
    # DFS recursivo para contagem de componentes conectados
    def num_comp(self):
        pred = self.dfs_recursive()
        num = 0
        for v in range(self.num_vertices):
            # Se pred[v] é -1, significa que v foi o primeiro vértice de um componente
            if pred[v] == -1:
                num += 1
        return num
    
    def dfs_recursive(self):
        pred = [-1 for _ in range(self.num_vertices)]
        visited = [False for _ in range(self.num_vertices)]
        for v in range(self.num_vertices):
            if not visited[v]:
                self._dfs_rec(v, visited, pred)
        return pred
        
    def _dfs_rec(self, v, visited, pred):
        print("Visitando vértice (recursivo):", v)
        visited[v] = True
        for u in self.L[v]:
            if not visited[u]:
                pred[u] = v
                self._dfs_rec(u, visited, pred)

    # Busca em Largura (BFS) a partir de um vértice fonte
    def bfs(self, source):
        visited = [False for _ in range(self.num_vertices)]
        pred = [-1 for _ in range(self.num_vertices)]
        dist = [-1 for _ in range(self.num_vertices)]
        q = queue.Queue()
        q.put(source)
        visited[source] = True
        dist[source] = 0
        
        while not q.empty():
            v = q.get()
            print("Visitando vértice (BFS):", v)
            for u in self.L[v]:
                if not visited[u]:
                    q.put(u)
                    visited[u] = True
                    dist[u] = dist[v] + 1
                    pred[u] = v
        return dist, pred
    
    # Função para imprimir o caminho entre dois vértices utilizando o resultado do BFS
    def print_bfs_path(self, s, t):
        dist, pred = self.bfs(s)
        if pred[t] == -1 and s != t:
            print(f"Não há caminho entre os vértices {s} e {t}.")
            return
        # Reconstruir o caminho de t até s usando o vetor de predecessores
        path = []
        current = t
        while current != -1:
            path.append(current)
            if current == s:
                break
            current = pred[current]
        path.reverse()
        print("Caminho BFS de", s, "para", t, ":", " -> ".join(map(str, path)))
    
    # DFS iterativa utilizando pilha para eliminar a recursão
    def dfs_iterative(self, start):
        visited = [False for _ in range(self.num_vertices)]
        pred = [-1 for _ in range(self.num_vertices)]
        stack = []
        stack.append(start)
        while stack:
            v = stack.pop()
            if not visited[v]:
                print("Visitando vértice (iterativo DFS):", v)
                visited[v] = True
                # Adiciona os vizinhos em ordem reversa para manter a ordem similar à recursiva
                for u in reversed(self.L[v]):
                    if not visited[u]:
                        stack.append(u)
                        if pred[u] == -1:
                            pred[u] = v
        return pred
