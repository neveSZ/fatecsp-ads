// 3. Defina as seguintes macros usando as proprias macros construidas no
// exercicio anterior:

// c) TO_LOWER(ch): Resulta a letra minuscula, caso ch seja uma letra maiuscula.
#define maiuscula(ch) ch > 64 && ch < 91 ? 1 : 0
#define TO_LOWER(ch) (maiuscula(ch)) ? ch + 32 : ch