int menor_ind(int a[], int tam){
//Recebe: o endereco do vetor a e o seu tamanho tam (tam > 0).
//Retorna: o indice do menor elemento de a.
  int i, menor=tam-1;
  for(i=0; i<tam-1; i++){
    if(a[i]<a[menor])
      menor = i;
  }
  return menor;
}
