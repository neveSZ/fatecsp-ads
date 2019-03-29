// 1. Simule as funcoes recursivas a seguir:

// a) Quantas chamadas recursivas para n = 15?
void imp(int n) {
  if (n > 0) {
    imp(n / 3);
    printf("%d", 2 * n);
    imp(n / 3);
  }
}
// R: 14 chamadas recursivas
// Saida: 2102302102

// b) Simule para n = 5 e a[]={2, 7, -9, 5, 6}.
int maximo(int a[], int n) {
  if (n == 1)
    return a[0];
  else {
    int aux = maximo(a, n - 1);
    if (aux > a[n - 1])
      return aux;
    else
      return a[n - 1];
  }
}
// Retorno: 7