/*
+-----------------------------------------------------------------------------+
| Instituição   :  Faculdade de Tecnologia de São Paulo                       |
| Departamento  :  Tecnologia da Informação                                   |
| Curso         :  Análise e Desenvolvimento de Sistemas                      |
| Disciplina    :  ILP-010                                                    |
| Turno         :  Tarde                                                      |
| Aluno         :  Victor Neves Silva/Kevin Nicolas Bueno Quintino            |
| Matrícula     :  18203756/18212423                                          |
+-----------------------------------------------------------------------------+
| Programa      :  EP02.c  - Abreviação de Nomes                              |
| Linguagem     :  ANSI C                                                     |
| Compilador    :  Pelles C (8.00.60)                                         |
+-----------------------------------------------------------------------------+
*/
#include <stdio.h>

void abrevia(char nome[]);

int main(void) {
  char nome[41];
  gets(nome);
  abrevia(nome);
  puts(nome);
  return 0;
}

void abrevia(char nome[]) {
  int i, maiusculaAnterior = 0;
  for (i = 1; nome[i] != '\0'; i++) {
    // Verificar se eh espaco seguido de maiuscula
    if (nome[i] == ' ' && nome[++i] > 64 && nome[i] < 91) {
      // Verificar se ja teve maiuscula
      if (maiusculaAnterior) {
        // Colocar ponto apos a letra maiuscula
        int aux = maiusculaAnterior + 1;
        nome[aux++] = '.';

        // Achar o espaco que vem apos a abreviacao
        int espaco = aux;
        while (nome[espaco] != ' ')
          espaco++;

        // Remover as letras apos o ponto(movendo os sobrenomes)
        for (aux; nome[aux] != '\0'; aux++, espaco++)
          nome[aux] = nome[espaco];

        i -= espaco - aux; // Atualizar o indice
        nome[aux] = '\0';  // Mudar o final da string
      }
      // Guardar o indice quando ocorrer espaco seguido de maiuscula
      maiusculaAnterior = i;
    }
  }
}