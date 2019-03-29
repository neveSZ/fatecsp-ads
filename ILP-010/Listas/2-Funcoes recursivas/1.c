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
