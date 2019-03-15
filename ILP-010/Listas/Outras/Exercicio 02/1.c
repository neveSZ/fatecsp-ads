#include <stdio.h>
/*1) Crie um programa que receba um salario bruto e exiba uma mensagem indicando
se sera descontado o teto do INSS, o desconto do teto do INSS ocorre quando 11%
do salario bruto ultrapassa R$ 640,00.*/
int main(void)
{
  float salario;
  printf("Salario: ");
  scanf("%f", &salario);
  if(salario*0.11 > 640.00)
  {
    printf("Desconto do teto");
  }
  return 0;
}
