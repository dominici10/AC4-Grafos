def arvoreGeradora(D, A):
    import numpy as np
    # L = (D - A)
    L = np.array(D) - np.array(A)
    L = np.delete(L,0,0)
    L = np.delete(L,0,1)
    return round(np.linalg.det(L))

graus = [  
    [3,0,0,0],
    [0,2,0,0],
    [0,0,2,0],
    [0,0,0,3]
]

adj = [  
    [0,1,1,1],
    [1,0,0,1],
    [1,0,0,1],
    [1,1,1,0]
]


print("Quantidade de arvores possíveis:")
print(arvoreGeradora(graus, adj))
