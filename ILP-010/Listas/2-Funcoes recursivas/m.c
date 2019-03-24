int esquerdaPar(int n) {
  // Receber um numero inteiro n e exibir 'sim', caso o digito mais a esquerda
  // seja par, ou 'nao', caso contrario. Use os operadores de divisao e resto.
  if (n < 10) {
    if (n % 2 == 0)
      printf("sim");
    else
      printf("nao");
  } else
    esquerdaPar(n / 10);
}
