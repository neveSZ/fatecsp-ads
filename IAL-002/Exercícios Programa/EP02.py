'''
+-----------------------------------------------------------------------------+
| Instituição   :  Faculdade de Tecnologia de São Paulo                       |
| Departamento  :  Tecnologia da Informação                                   |
| Curso         :  Análise e Desenvolvimento de Sistemas                      |
| Disciplina    :  IAL-002                                                    |
| Turno         :  Vespertino                                                 |
| Aluno         :  Victor Neves Silva                                         |
| Matrícula     :  18203756                                                   |
+-----------------------------------------------------------------------------+
| Programa      :  EP02.py - Intercalação de vetores                          |
| Linguagem     :  Python 3                                                   |
| Compilador    :  CPython (3.6.2)                                            |
+-----------------------------------------------------------------------------+
'''


def intercala(a, b, c, m, n):
    cont_a = 0
    cont_b = 0
    cont_c = 0
    while cont_a < m or cont_b < n:
        if cont_a == m:
            c[cont_c] = b[cont_b]
            cont_b += 1
        elif cont_b == n:
            c[cont_c] = a[cont_a]
            cont_a += 1
        else:
            if a[cont_a] < b[cont_b]:
                c[cont_c] = a[cont_a]
                cont_a = cont_a+1
            elif b[cont_b] < a[cont_a]:
                c[cont_c] = b[cont_b]
                cont_b += 1
            else:
                c[cont_c] = a[cont_a]
                cont_a += 1
                cont_b += 1
        cont_c += 1
    return cont_c  # quantidade de elementos inseridos no vetor c


def ordenacao(vetor, tamanho):
    for i in range(tamanho-1):
        for cont in range(i+1, tamanho):
            if vetor[i] > vetor[cont]:
                aux = vetor[cont]
                vetor[cont] = vetor[i]
                vetor[i] = aux


def repetido(vetor, indice_final, variavel):
    for i in range(indice_final):
        if vetor[i] == variavel:
            return True
    return False


def ler_vetor(vetor, tamanho):
    for i in range(tamanho):
        while(True):
            temp = int(input("%d: " % i))
            if repetido(vetor, i, temp):
                print("Elemento repetido")
            else:
                vetor[i] = temp
                break


def exibir_vetor(vetor, tamanho):
    print("[", end="")
    for i in range(tamanho):
        print(vetor[i], end=" ")
    print("]")


# 1. Ler m e um vetor de inteiros com m elementos nao repetidos
m = int(input("m: "))
a = [0]*m
ler_vetor(a, m)

# 2. Ler n e um vetor de inteiros com n elementos nao repetidos
n = int(input("n: "))
b = [0]*n
ler_vetor(b, n)

# 3. Exibir os vetores lidos
print("a = ", end="")
exibir_vetor(a, m)
print("b = ", end="")
exibir_vetor(b, n)

# 4. Ordenar cada vetor, chamando a funcao ordenacao
ordenacao(a, m)
ordenacao(b, n)

# 5. Exibir os vetores apos a ordenacao
print("a = ", end="")
exibir_vetor(a, m)
print("b = ", end="")
exibir_vetor(b, n)

# 6. Chamar a funcao de intercalacao passando os cinco parametros
c = [0]*(m+n)  # Inicializar c para passar de parametro
limite_c = intercala(a, b, c, m, n)  # ultimo indice util do vetor c

# 7. Exibir o terceiro vetor com o resultado da intercalacao
print("c = ", end="")
exibir_vetor(c, limite_c)
