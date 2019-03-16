int tam_string(char s[]){
//Recebe: o endereco de uma string s.
//Retorna: a quantidade de caracteres de s.
  int i;
  for(i=0; s[i]!='\0'; i++);
  return i;
}

