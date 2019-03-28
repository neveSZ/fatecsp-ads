float potencia(float b, int n) {
  // Receber um numero real b (b > 0) e um numero inteiro n (n >= 0) e devolver
  // o resultado de b elevado a n.
  if (n == 0)
    return 1;
  return b * potencia(b, n - 1);
}
