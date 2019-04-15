// 2. Defina as seguintes macros (utilize o operador ternario):

// a) Resulta 1 se x for par ou 0 caso contrario;
#define par(x) x % 2 == 0 ? 1 : 0

// b) Resulta 1 se x for impar ou 0 caso contrario;
#define impar(x) x % 2 == 0 ? 0 : 1

// c) Resulta 1 se ch for uma letra maiuscula ou 0 caso contrario;
#define maiuscula(ch) ch > 64 && ch < 91 ? 1 : 0
