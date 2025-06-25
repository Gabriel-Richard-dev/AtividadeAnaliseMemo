import random as rand
import time
import matplotlib.pyplot as plt

def corta_haste_bottom_up_completo(p, n):
    r = [0] * (n + 1)  
    d = [0] * (n + 1) 

    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                d[j] = i
        r[j] = q

    return r[n], d


def barras_memo(P, n, memo=None, cortes=None):
    if memo is None:
        memo = [-1] * (n + 1)
    if cortes is None:
        cortes = [-1] * (n + 1)

    if memo[n] >= 0:
        return memo[n], cortes

    if n == 0:
        memo[0] = 0
        return 0, cortes

    l = P[n] if n < len(P) else float('-inf')
    cortes[n] = n  

    for i in range(1, n):
        lcandidat, _ = barras_memo(P, n - i, memo, cortes)
        lcandidat += P[i]
        if lcandidat > l:
            l = lcandidat
            cortes[n] = i

    memo[n] = l
    return l, cortes

def reconstruir_cortes(cortes, n):
    resultado = []
    while n > 0:
        resultado.append(cortes[n])
        n -= cortes[n]
    return resultado

def comparar_tempos_e_graficar():
    tamanhos = list(range(5, 35, 5))  
    tempos_bottom_up = []
    tempos_memoizado = []

    for n in tamanhos:
        base = rand.randint(10, 20)
        P = [0]
        valor = 0
        while len(P) < n + 1:
            valor += base
            if valor not in P:
                P.append(valor)
        P.sort()

        inicio = time.time()
        corta_haste_bottom_up_completo(P, n)
        fim = time.time()
        tempos_bottom_up.append(fim - inicio)

        inicio = time.time()
        barras_memo(P, n)
        fim = time.time()
        tempos_memoizado.append(fim - inicio)

    plt.plot(tamanhos, tempos_bottom_up, marker='o', label='Bottom-Up (sem memoização)')
    plt.plot(tamanhos, tempos_memoizado, marker='x', label='Top-Down Memoizado')
    plt.xlabel('Tamanho da haste (n)')
    plt.ylabel('Tempo de execução (s)')
    plt.title('Comparação de Desempenho: Bottom-Up vs Memoização')
    plt.legend()
    plt.grid(True)
    plt.show()

comparar_tempos_e_graficar()
