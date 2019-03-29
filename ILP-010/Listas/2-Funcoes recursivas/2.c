// 2. Desenvolver as funcoes abaixo utilizando recursao, ou seja, serao funcoes
// recursivas.

// a) Receber dois numeros inteiros p e q (p >= 0 e q > 0) e devolver o
// resultado da divisao inteira de p por q.
int divisaoInteira(int p, int q) {
  if (p < q)
    return 0;
  return divisaoInteira(p - q, q) + 1;
}

// b) Receber dois numeros inteiros a e b (a >= 0 e b >= 0) e devolver o
// resultado do produto de a por b.
int multiplicacao(int a, int b) {
  if (b == 0)
    return 0;
  return a + multiplicacao(a, b - 1);
}

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