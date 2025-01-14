import numpy as np
import matplotlib.pyplot as plt
import heapq


class GrafoDijkstra:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz_adjacencia = np.full((num_vertices, num_vertices), np.inf)
        np.fill_diagonal(self.matriz_adjacencia, 0)

    def adicionar_aresta(self, u, v, peso):
        self.matriz_adjacencia[u][v] = peso
        self.matriz_adjacencia[v][u] = peso  # Para grafos não direcionados

    def dijkstra(self, origem):
        distancias = np.full(self.num_vertices, np.inf)
        distancias[origem] = 0
        visitados = [False] * self.num_vertices
        fila_prioridade = [(0, origem)]  # (distância, nó)

        while fila_prioridade:
            distancia_atual, u = heapq.heappop(fila_prioridade)

            if visitados[u]:
                continue
            visitados[u] = True

            for v in range(self.num_vertices):
                peso = self.matriz_adjacencia[u][v]
                if peso != np.inf and not visitados[v]:
                    nova_distancia = distancia_atual + peso
                    if nova_distancia < distancias[v]:
                        distancias[v] = nova_distancia
                        heapq.heappush(fila_prioridade, (nova_distancia, v))

        return distancias

    def plotar_grafo(self, caminho=None):
        plt.figure(figsize=(8, 8))
        coordenadas = np.random.rand(self.num_vertices, 2) * 10
        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if self.matriz_adjacencia[i][j] < np.inf:
                    plt.plot(
                        [coordenadas[i][0], coordenadas[j][0]],
                        [coordenadas[i][1], coordenadas[j][1]],
                        "gray",
                        linestyle="dotted",
                    )

        # Destacar os caminhos
        if caminho:
            for i in range(len(caminho) - 1):
                u, v = caminho[i], caminho[i + 1]
                plt.plot(
                    [coordenadas[u][0], coordenadas[v][0]],
                    [coordenadas[u][1], coordenadas[v][1]],
                    "red",
                    linewidth=2,
                )

        # Adicionar nós
        for i, (x, y) in enumerate(coordenadas):
            plt.scatter(x, y, c="blue")
            plt.text(x, y, f" {i}", fontsize=12, color="black")

        plt.title("Grafo com Algoritmo de Dijkstra")
        plt.show()


# Teste do algoritmo
def main():
    num_vertices = 6
    grafo = GrafoDijkstra(num_vertices)

    # Adicionar arestas (u, v, peso)
    grafo.adicionar_aresta(0, 1, 7)
    grafo.adicionar_aresta(0, 2, 9)
    grafo.adicionar_aresta(0, 5, 14)
    grafo.adicionar_aresta(1, 2, 10)
    grafo.adicionar_aresta(1, 3, 15)
    grafo.adicionar_aresta(2, 3, 11)
    grafo.adicionar_aresta(2, 5, 2)
    grafo.adicionar_aresta(3, 4, 6)
    grafo.adicionar_aresta(4, 5, 9)

    origem = 0
    distancias = grafo.dijkstra(origem)

    print(f"Distâncias a partir do nó {origem}: {distancias}")

    # Plotar o grafo com o caminho mais curto até um nó específico
    grafo.plotar_grafo()

if __name__ == "__main__":
    main()
