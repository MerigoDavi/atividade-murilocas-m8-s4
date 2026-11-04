import networkx as nx
import matplotlib as mp
mp.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

#DO
destino = 6
origem = 0

#RA
D6 = 3
D5 = 2
D4 = 1
D3 = 0
D2 = 1
D1 = 4

#pesos
w1 = 10 + (D6 % 5)
print(w1)
w2 = 15 + (D5 % 7) 
w3 = 8 + (D4 % 4)
w4 = 12 + (D3 % 6)
w5 = 14 + (D2 % 5)
w6 = 9 + (D1 % 6)
w7 = 7 + ((D5 + D6) % 5)
w8 = 11 + ((D4 + D5) % 6)
w9 = 6 + ((D3 + D4) % 4)
w10 = 16 + ((D2 + D3) % 7)
w11 = 18 + ((D1 + D2) % 8)
w12 = 9 + ((D5 + D1) % 5)
w13 = 20 + (D6 % 4)

#Verificar pq é bom
print(w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13)

#Valida se é positivo
assert min(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13) >= 0, "tem peso negativo nessa bomba"

#Cria o grafo
G = nx.Graph()
G.add_nodes_from([0,1,2,3,4,5,6,7])
G.add_weighted_edges_from([(0, 1, w1), (0,2,w2), (1,2,w3), (1,3,w4), (2,4,w5), (2,5,w6), (3,4,w7), (3,6,w8), (4,5,w9), (4,7,w10), (5,7,w11), (6,7,w12), (1,4,w13)])

#Gera a visualização do grafo
fig = plt.figure()
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, ax=fig.add_subplot(), with_labels=True, node_color="lightblue")
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"))
fig.savefig("graph.png")

#Matrix
nodes = sorted(G.nodes())
A = nx.to_numpy_array(G, nodelist=nodes, weight="weight", dtype=int).astype(object)
A[A == 0] = None
print("Matriz de adjacência:")
print("x" + "|".join(f"{n:>3}" for n in nodes))
for n, linha in zip(nodes, A):
    print(f"{n:>3}" + "|".join(f"{'-' if v is None else v:>3}" for v in linha))
simetria = np.array_equal(A, A.transpose())
print("Matriz simétrica:", simetria)

#Dijkstra
distances = nx.single_source_dijkstra_path_length(G, source=origem)
print("Distâncias de 0 até cada vértice:", distances)

#Rota e custo
rota = nx.dijkstra_path(G, origem, destino)
custo = nx.dijkstra_path_length(G, origem, destino)
print("Rota ótima:", rota, "custo =", custo)

#Prim
mst = nx.minimum_spanning_tree(G, algorithm="prim")
print("ramais da MST:", sorted(mst.edges(data="weight")))
print("custo MST:", mst.size(weight="weight"))