int resto(int p, int q){
//Recebe: dois inteiros p e q (p >= 0  e q > 0).
//Retorna: o resto da divisao inteira de p por q.
//Obs: nao usar operador de resto.
  while(p>=q)
    p-=q;
  return p;
}
