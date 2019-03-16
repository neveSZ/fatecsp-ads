int copia_string(char dest[], char fonte[]){
//Recebe: o endereco da string dest e o endereco da string fonte.
//Retorna: a quantidade de caracteres copiados de fonte para dest.
  int i;
  for(i=0; dest[i]!='\0'; i++){
    dest[i]=fonte[i];
  }
  return i;
}
