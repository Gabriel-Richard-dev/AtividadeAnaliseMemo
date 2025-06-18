import random as rand;

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
    cortes[n] = n  # corte total, sem dividir

    for i in range(1, n):
        # lucro se cortar na posição i
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

def printAlgoritimoMemoizado(P, n):
    lucro_max, cortes = barras_memo(P, n)
    cortes_otimos = reconstruir_cortes(cortes, n)

    print(f"Lucro máximo: {lucro_max}")
    print(f"Cortes ótimos: {cortes_otimos}")

def printAlgoritimoSimples(P, n):    
    valor_maximo, cortes = corta_haste_bottom_up_completo(P, n)
    print("Valor máximo:", valor_maximo)

    print("Cortes ótimos:", end=" ")
    while n > 0:
        print(cortes[n], end=" ")
        n -= cortes[n]
   


# printAlgoritimoMemoizado(p,n)
# printAlgoritimoSimples(p,n)

def iniciarVetor():
    n = rand.randint(10,10000)
    P = []

    while len(P) < n + 1:
        valor = rand.randint(1, 400)
        if valor not in P:
            P.append(valor)
    P.sort()
    P[0] = 0

    print('\nVetor P ordenado e sem repetição:')
    for i in P:
        print(i)
    print('')

    printAlgoritimoSimples(P, n)
    printAlgoritimoMemoizado(P, n)

iniciarVetor()