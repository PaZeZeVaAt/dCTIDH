// #include "crypto_declassify.h"
#include "elligator.h"

// #define fp_cswap fp_cswap_ctidh

void elligator(proj *plus,proj *minus,const proj *A)
{
  for (;;) {
    fp u;
    fp_random(&u);

    // long long reject = fp_iszero(&u);
    long long reject = fp_iszero(&u);    
    // crypto_declassify(&reject,sizeof reject);
    if (reject) continue; /* bad RNG outputs 0 */

    fp u2; fp_sq2(&u2,&u);
    fp D; fp_sub3(&D,&u2,&fp_1);

    // reject = fp_iszero(&D);
    reject = fp_iszero(&D);    
    // crypto_declassify(&reject,sizeof reject);
    if (reject) continue; /* bad RNG outputs +-1 */

    fp M; fp_mul3(&M,&A->x,&u2); /* M = u^2 A->x */
    fp T; fp_mul3(&T,&A->x,&M); /* T = u^2 A->x^2 */

    // long long control = fp_iszero(&A->x);
    long long control = fp_iszero(&A->x);
    fp P;
    fp_copy(P, A->x);
    fp_cmov(&P,&fp_1,control); /* P = 1 if A->x = 0 else A->x */
    fp_cmov(&M,&fp_1,control); /* M = 1 if A->x = 0 else u^2 A->x */
    fp_cmov(&T,&fp_1,control); /* T = 1 if A->x = 0 */

    fp_mul2(&D,&A->z); /* D = (u^2-1) A->z */

    fp D2; fp_sq2(&D2,&D); /* D2 = (u^2-1)^2 A->z^2 */

    fp_add2(&T,&D2); /* T = 1 + (u^2-1)^2 A->z^2 if A->x = 0, else u^2 A->x^2 + (u^2-1)^2 A->z^2 */
    fp_mul2(&T,&D);
    fp_mul2(&T,&P);
    /* T = (u^2-1)A->z(1+(u^2-1)^2 A->z^2) if A->x = 0 */
    /* else (u^2-1) A->z A->x(u^2 A->x^2 + (u^2-1)^2 A->z^2) */

    /* plus point will be P/D = 1/(u^2-1)A->z if A->x = 0 else A/(u^2-1) */
    /* and minus point will be -M/D = -1/(u^2-1)A->z if A->x = 0 else -u^2 A/(u^2-1) */
    /* unless they're flipped, which is determined by T */

    /* T = Az^4 (1-u^2)^4 ((P/D)^3+A(P/D)^2+(P/D)) */
    /* so T squareness says whether P/D is on curve */

    /* also says whether -M/D is not on curve: */
    /* in all cases -M/D = -P/D-A */
    /* so (-M/D)^3+A(-M/D)^2+(-M/D) = (-P/D-A)^3+A(-P/D-A)^2+(-P/D-A) */
    /* = ((P/D)^3+A(P/D)^2+(P/D)) (-1-AD/P) */
    /* and by construction -1-AD/P is a non-square */
    /* since it's -1 if A=0, else -u^2 */

    fp_copy(plus->x, P);
    fp_neg2(&minus->x,&M);



//   x0 = plus->x;
//   y0 = minus->x;

    // test x0, y0;
    // x0[0] = 1;
    // y0[0] = 2;

// fp_cswap(x0,y0,1-fp_sqrt(&T));
    fp_cswap(&plus->x,&minus->x,1-fp_sqrt(&T));

    // fp_cswap(x0, y0, 1);

    fp_copy(plus->z, D);
    fp_copy(minus->z, D);

    return;
  }
}
