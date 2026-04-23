import sys
from graph import Graph
from dsatur import DSatur

ESTADOS = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF",
    "ES", "GO", "MA", "MG", "MS", "MT", "PA",
    "PB", "PE", "PI", "PR", "RJ", "RN", "RO",
    "RR", "RS", "SC", "SE", "SP", "TO"
]

def main():
    if len(sys.argv) < 2:
        print("Uso: python src/main.py dados/brasil.txt")
        return

    caminho = sys.argv[1]

    # leitura do grafo (formato algs4)
    with open(caminho, "r") as f:
        V = int(f.readline())
        E = int(f.readline())

        g = Graph(V)

        for _ in range(E):
            v, w = f.readline().split()
            g.add_edge(v, w)

    print("=== GRAFO ===")
    print(g)

    ds = DSatur(g)
    cores = ds.color_graph()

    print("\n=== ORDEM DE COLORAÇÃO ===")
    for i, v in enumerate(ds.order, 1):
        print(f"{i}. {ESTADOS[v]}")

    print("\n=== CORES ===")
    for i, c in enumerate(cores):
        print(f"{ESTADOS[i]} -> Cor {c}")

    print("\nTotal de cores:", ds.total_colors())

    print("\nColoração válida?", ds.is_valid_coloring())


if __name__ == "__main__":
    main()