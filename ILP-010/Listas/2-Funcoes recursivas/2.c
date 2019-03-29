// 2. Desenvolver as funcoes abaixo utilizando recursao, ou seja, serao funcoes
// recursivas.

// c) Receber um numero real b (b > 0) e um numero inteiro n (n >= 0) e devolver
// o resultado de b elevado a n.
float potencia(float b, int n) {
  if (n == 0)
    return 1;
  return b * potencia(b, n - 1);
}

// m) Receber um numero inteiro n e exibir 'sim', caso o digito mais a esquerda
// seja par, ou 'nao', caso contrario. Use os operadores de divisao e resto.
void esquerdaPar(int n) {
  if (n < 10) {
    if (n % 2 == 0)
      printf("sim");
    else
      printf("nao");
  } else
    esquerdaPar(n / 10);
}