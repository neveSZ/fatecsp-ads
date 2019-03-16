int busca(int a[], int tam, int x){
//Recebe: o endereco do vetor a, o seu tamanho tam (tam > 0) e um inteiro x.
//Retorna: 1 se x estiver em a, ou 0 caso contrario.
  int i;
  for(i=0; i<tam; i++){
    if(a[i]==x)
      return 1;
  }
  return 0;
}