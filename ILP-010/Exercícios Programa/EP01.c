/*
+-----------------------------------------------------------------------------+
| Instituição   :  Faculdade de Tecnologia de São Paulo                       |
| Departamento  :  Tecnologia da Informação                                   |
| Curso         :  Análise e Desenvolvimento de Sistemas                      |
| Disciplina    :  ILP-010                                                    |
| Turno         :  Tarde                                                      |
| Aluno         :  Victor Neves Silva                                         |
| Matrícula     :  18203756                                                   |
+-----------------------------------------------------------------------------+
| Programa      :  EP01.c  - Codificação e decodificação de mensagens         |
| Linguagem     :  ANSI C                                                     |
| Compilador    :  Pelles C (8.00.60)                                         |
+-----------------------------------------------------------------------------+
*/
#include <stdio.h>

void codifica(char msg[], char cod[]);
void decodifica(char cod[], char msg[]);
int decimalValue(int codChar);
int charValue(int codChar);

int main(void) {
  int opcao;
  char msg[50], cod[100];
  puts("Digite 1 para codificar ou 2 para decodificar");
  scanf(" %d", &opcao);
  getchar(); // Nao guarda o \n
  switch (opcao) {
  case 1:
    puts("mensagem: ");
    gets(msg);
    codifica(msg, cod);
    puts(cod);
    break;
  case 2:
    puts("codigo: ");
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

void codifica(char msg[], char cod[]) {
  int i, cont = 0;
  for (i = 0; msg[i] != '\0'; i++) {
    cod[cont++] = charValue(msg[i] / 10); // Guarda algarismo de dezena
    cod[cont++] = charValue(msg[i] % 10); // Guarda algarismo de unidade
  }
  cod[cont] = '\0';
}

void decodifica(char cod[], char msg[]) {
  int i, cont = 0;
  for (i = 0; cod[i] != '\0'; i += 2) {
    msg[cont] = decimalValue(cod[i]) * 10 +
                decimalValue(cod[i + 1]); // Une os dois algarismos
    cont++;
  }
  msg[cont] = '\0';
}

int decimalValue(int charValue) {
  // Caractere para decimal. Ex: o char '7' eh 55 em decimal
  return charValue - 48;
}

int charValue(int decimalValue) {
  // Decimal para caractere. Ex: o decimal 55 eh o char '7'
  return decimalValue + 48;
}