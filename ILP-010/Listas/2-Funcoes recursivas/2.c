// 2. Desenvolver as funcoes abaixo utilizando recursao, ou seja, serao funcoes
// recursivas.

// c) Receber um numero real b (b > 0) e um numero inteiro n (n >= 0) e devolver
// o resultado de b elevado a n.
float potencia(float b, int n) {
  if (n == 0)
    return 1;
  return b * potencia(b, n - 1);
}
