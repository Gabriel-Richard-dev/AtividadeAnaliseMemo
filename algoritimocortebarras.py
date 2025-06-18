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
   
p = [0, 1, 5, 8, 9]
n = 4

printAlgoritimoMemoizado(p,n)
printAlgoritimoSimples(p,n)