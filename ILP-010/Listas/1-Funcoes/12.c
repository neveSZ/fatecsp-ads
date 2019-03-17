int copia_maiusculas(char dest[], char fonte[]) {
  // Recebe: o endereco da string dest e o endereco da string fonte.
  // Retorna: a quantidade de letras maiusculas copiadas de fonte para dest.
  int i, cont = 0;
  for (i = 0; dest[i] != '\0'; i++) {
    if (fonte[i] > 64 && fonte[i] < 91) {
      dest[cont] = fonte[i];
      cont++;
    }
  }
  return cont;
}