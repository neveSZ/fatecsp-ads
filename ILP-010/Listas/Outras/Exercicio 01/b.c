#include <stdio.h>
/*b) Crie um programa que receba a quantidade de sabonetes que um mercado
 * comprou de uma fabrica e exiba o total de sabonetes recebidos, sabendo que a
 * cada 100 sabonetes ganha-se 5 sabonetes de brinde. obs: sem if e sem lacos*/
int main(void) {
  int qtd, brinde;
  printf("Quantidade de sabonetes comprados: ");
  scanf("%d", &qtd);
  brinde = qtd / 100 * 5;
  printf("Total de sabonetes recebidos = %d", qtd + brinde);
  return 0;
}
