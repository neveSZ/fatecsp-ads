int ocorrencia(char s[], char ch){
//Recebe: o endereco de uma string s.
//Retorna: o numero de ocorrencias de ch em s.
  int i, cont = 0;
  for(i=0; s[i]!='\0'; i++){
    if(s[i]==ch)
      cont++;
  }
  return cont;
}