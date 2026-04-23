class DSatur:
    def __init__(self, graph):
        self.graph = graph
        self.colors = [-1] * graph.V
        self.order = []

    def degree(self, v):
        grau = 0
        for _ in self.graph.adj[v]:
            grau += 1
        return grau

    def saturation_degree(self, v):
        cores_vizinhos = set()

        for vizinho in self.graph.adj[v]:
            if self.colors[vizinho] != -1:
                cores_vizinhos.add(self.colors[vizinho])

        return len(cores_vizinhos)

    def smallest_available_color(self, v):
        cores_usadas = set()

        for vizinho in self.graph.adj[v]:
            if self.colors[vizinho] != -1:
                cores_usadas.add(self.colors[vizinho])

        cor = 1
        while cor in cores_usadas:
            cor += 1

        return cor

    def choose_vertex(self, nao_coloridos):
        return max(
            nao_coloridos,
            key=lambda v: (
                self.saturation_degree(v),
                self.degree(v)
            )
        )

    def color_graph(self):
        nao_coloridos = set(range(self.graph.V))

        primeiro = max(nao_coloridos, key=lambda v: self.degree(v))

        self.colors[primeiro] = 1
        self.order.append(primeiro)
        nao_coloridos.remove(primeiro)

        while nao_coloridos:
            v = self.choose_vertex(nao_coloridos)
            cor = self.smallest_available_color(v)

            self.colors[v] = cor
            self.order.append(v)
            nao_coloridos.remove(v)

        return self.colors

    def total_colors(self):
        return max(self.colors)

    def is_valid_coloring(self):
        for v in range(self.graph.V):
            for w in self.graph.adj[v]:
                if self.colors[v] == self.colors[w]:
                    return False

        return True