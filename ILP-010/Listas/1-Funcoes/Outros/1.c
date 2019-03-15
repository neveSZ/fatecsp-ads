#include <stdio.h>
/*1) Crie um programa que receba um numero natural n (1<=n<=7) e exiba o correspondente
do dia da semana. Adote domingo como o 1o dia da semana(use switch)*/
int main(void)
{
  int n;
  printf("n: ");
  scanf("%d", &n);
  switch (n)
  {
    case 1: {
      printf("Domingo");
      break;
    }
    case 2: {
      printf("Segunda-feira");
      break;
    }
    case 3: {
      printf("Terca-feira");
      break;
    }
    case 4: {
      printf("Quarta-feira");
      break;
    }
    case 5: {
      printf("Quinta-feira");
      break;
    }
    case 6: {
      printf("Sexta-feira");
      break;
    }
    case 7: {
      printf("Sabado");
      break;
    }
    default: {
      printf("Nao reconhecido");
      break;
      }
  }
  return 0;
}
