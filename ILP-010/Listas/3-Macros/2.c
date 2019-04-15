// 2. Defina as seguintes macros (utilize o operador ternario):

// a) Resulta 1 se x for par ou 0 caso contrario;
#define par(x) x % 2 == 0 ? 1 : 0

// b) Resulta 1 se x for impar ou 0 caso contrario;
#define impar(x) x % 2 == 0 ? 0 : 1

// c) Resulta 1 se ch for uma letra maiuscula ou 0 caso contrario;
#define maiuscula(ch) ch > 64 && ch < 91 ? 1 : 0

// d) Resulta 1 se ch for uma letra minuscula ou 0 caso contrario;
#define minuscula(ch) ch > 96 && ch < 123 ? 1 : 0

// e) Resulta 1 se ch for um digito hexadecimal ou 0 caso contrario;
#define hexa(ch) (ch > 64 && ch < 71) || (ch > 47 && ch < 58) ? 1 : 0

// f) Resulta 1 se ch for um digito decimal ou 0 caso contrario;
#define decimal(ch) ch > 47 && ch < 58 ? 1 : 0

// g) Resulta 1 se ch for uma letra ou 0 caso contrario;
#define letra(ch) (ch > 64 && ch < 91) || (ch > 96 && ch < 123) ? 1 : 0
