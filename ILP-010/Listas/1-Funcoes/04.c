int divide(int p, int q){
//Recebe: dois inteiros p e q (p >= 0  e q > 0).
//Retorna: o quociente da divisao inteira de p por q.
//Obs: nao usar operador de divisao.
  int quo;
  for(quo=0; p>=q; p-=q)
    quo++;
  return quo;
}