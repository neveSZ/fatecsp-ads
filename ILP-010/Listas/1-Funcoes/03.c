int potencia(float b, int e){
//Recebe: um real (b > 0.0) e um inteiro e (e >= 0).
//Retorna: a potencia de b elevado a e.
  int i;
  float pot=b;
  for(i=1; i<e; i++){
    pot*=b;
  }
  return pot;
}