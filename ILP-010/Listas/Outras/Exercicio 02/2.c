#include <stdio.h>
/*b) Crie um programa que receba um inteiro n(n>0) e exiba a soma dos
divisores de n.
EXemplo: n=10 -> soma=1+2+5+10=18
*/
int main(void)
{
  int n, soma, i;
  printf("n: ");
  scanf("%d", &n);
  soma = n;
  for(i = n/2; i > 0 ;i--)
  {
    if(n%i == 0)
    {
      soma += i;
    }
  }
  printf("%d", soma);
  return 0;
}
