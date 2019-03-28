/*
+-----------------------------------------------------------------------------+
| Instituição   :  Faculdade de Tecnologia de São Paulo                       |
| Departamento  :  Tecnologia da Informação                                   |
| Curso         :  Análise e Desenvolvimento de Sistemas                      |
| Disciplina    :  ILP-010                                                    |
| Turno         :  Tarde                                                      |
| Aluno         :  Victor Neves Silva/Yago Machado Bareia                     |
| Matrícula     :  18203756/18110782                                          |
+-----------------------------------------------------------------------------+
| Programa      :  EP01.c  - Codificação e decodificação de mensagens         |
| Linguagem     :  ANSI C                                                     |
| Compilador    :  Pelles C (8.00.60)                                         |
+-----------------------------------------------------------------------------+
*/
#include <stdio.h>

void codifica(char msg[], char cod[]);
void decodifica(char cod[], char msg[]);

int main(void) {
  int opcao;
  char msg[51], cod[101];
  puts("Digite 1 para codificar ou 2 para decodificar");
  scanf("%d", &opcao);
  getchar(); // Nao guarda o \n
  switch (opcao) {
  case 1:
    puts("Digite a mensagem: ");
    gets(msg);
    codifica(msg, cod);
    puts(cod);
    break;
  case 2:
    puts("Digite o codigo: ");
    gets(cod);
    decodifica(cod, msg);
    puts(msg);
    break;
  default:
    puts("Opcao nao disponivel");
    break;
  }
  return 0;
}

int valorDecimal(int ascii) {
  // Recebe: um valor que representa um caractere numerico na tabela ASCII.
  // Retorna: um numero em base decimal.
  // Ex: recebe 55(valor ASCII do char '7') e retorna 7.
  return ascii - 48;
}

int valorAscii(int decimal) {
  // Recebe: um numero em base decimal.
  // Retorna: um valor que representa um caractere numerico na tabela ASCII.
  // Ex: recebe 7 e retorna 55(valor ASCII do char '7').
  return decimal + 48;
}

void codifica(char msg[], char cod[]) {
  int i, cont = 0;
  for (i = 0; msg[i] != '\0'; i++) {
    cod[cont++] = valorAscii(msg[i] / 10); // Guarda algarismo de dezena
    cod[cont++] = valorAscii(msg[i] % 10); // Guarda algarismo de unidade
  }
  cod[cont] = '\0'; // Final da string
}

void decodifica(char cod[], char msg[]) {
  int i, cont = 0;
  for (i = 0; cod[i] != '\0'; i += 2) {
    msg[cont] = valorDecimal(cod[i]) * 10 +
                valorDecimal(cod[i + 1]); // Une os dois algarismos
    cont++;
  }
  msg[cont] = '\0';
}
