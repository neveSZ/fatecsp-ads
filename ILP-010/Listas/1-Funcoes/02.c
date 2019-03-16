int fatorial(int n){
//Recebe: um inteiro n (n >= 0).
//Retorna: o fatorial de n.
  int i, fat=1;
  for(i=1; i<=n; i++){ 
    fat*=i;
  }
  return fat;
}
