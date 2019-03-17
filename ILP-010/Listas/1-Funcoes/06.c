int maior(int a[], int tam) {
  // Recebe: o endereco do vetor a e o seu tamanho tam (tam > 0).
  // Retorna: o valor do maior elemento de a.
  int i, maior = a[tam - 1];
  for (i = 0; i < tam - 1; i++) {
    if (a[i] > maior)
      maior = a[i];
  }
  return maior;
}
