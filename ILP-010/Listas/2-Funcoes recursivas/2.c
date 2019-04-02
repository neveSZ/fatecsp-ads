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

// d) Receber um numero inteiro n (n >= 0) e determinar a sua quantidade de
// digitos.
int digitos(int n) {
  if (n < 10)
    return 1;
  return digitos(n / 10) + 1;
}

// e) Dado um numero inteiro n (n >= 0), exibir seus digitos separados um por
// um.
void separaDigitos(int n) {
  if (n < 10)
    printf("%d", n);
  else {
    separaDigitos(n / 10);
    printf("%d ", n % 10);
  }
}

// f) Dado um numero inteiro n (n >= 0), exibir seus digitos invertidos.
void inverteDigitos(int n) {
  if (n < 10)
    printf("%d", n);
  else {
    printf("%d", n % 10);
    inverteDigitos(n / 10);
  }
}

// g) Receber um inteiro n (n >= 0), em base decimal, e exibir o correspondente
// em base binaria.
void converteBinario(int n) {
  if (n < 2)
    printf("%d", n);
  else {
    converteBinario(n / 2);
    printf("%d", n % 2);
  }
}

// h) Receber um numero inteiro n (n >= 0) em base decimal, e exibir o
// correspondente em base octal.
void converteOctal(int n) {
  if (n < 8)
    printf("%d", n);
  else {
    converteOctal(n / 8);
    printf("%d", n % 8);
  }
}

// k) Receber um inteiro n n(n >= 1) e devolver a soma dos n primeiros termos da
// serie: 1+(1/2)+(1/3)+(1/4)+(1/5)+..+(1/n).
float somatorio(int n) {
  if (n == 1)
    return 1.00;
  return somatorio(n - 1) + (1.00 / n);
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