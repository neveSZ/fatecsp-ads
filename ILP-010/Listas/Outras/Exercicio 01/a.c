#include <stdio.h>
/*a) Crie um programa que leia a base e a altura de um triangulo(valores reais) e
exiba sua area com duas casas decimais.*/
int main(void)
{
  float base, altura, area;
  printf("Base: ");
  scanf("%f", &base);
  printf("Altura: ");
  scanf("%f", &altura);
  area = base*altura/2;
  printf("Area = %.2f", area);
  return 0;
}
