// DO NOT EDIT! generated by ./autogen

#if defined AVX2
    #include "avx2/fp-avx2.h"
#elif defined KARATSUBA
    #include "karatsuba/fp-karatsuba.h"
#else
    #include "mulx/fp.h"
#endif

// 256 mults, 2041 squarings
bool fp_issquare(fp x)
{
  fp origx;
  fp_copy(origx,x);
  fp r0;
  fp_copy(r0,x);
  fp r1;
  fp_sqr(r1,r0);
  fp r2;
  fp_mul(r2,r0,r1);
  fp r3;
  fp_mul(r3,r1,r2);
  fp r4;
  fp_mul(r4,r1,r3);
  fp r5;
  fp_mul(r5,r1,r4);
  fp r6;
  fp_mul(r6,r1,r5);
  fp r7;
  fp_mul(r7,r1,r6);
  fp r8;
  fp_mul(r8,r1,r7);
  fp r9;
  fp_mul(r9,r1,r8);
  fp r10;
  fp_mul(r10,r1,r9);
  fp r11;
  fp_mul(r11,r1,r10);
  fp r12;
  fp_mul(r12,r1,r11);
  fp r13;
  fp_mul(r13,r1,r12);
  fp r14;
  fp_mul(r14,r1,r13);
  fp r15;
  fp_mul(r15,r1,r14);
  fp r16;
  fp_mul(r16,r1,r15);
  fp r17;
  fp_mul(r17,r1,r16);
  fp r18;
  fp_mul(r18,r1,r17);
  fp r19;
  fp_mul(r19,r1,r18);
  fp r20;
  fp_mul(r20,r1,r19);
  fp r21;
  fp_mul(r21,r1,r20);
  fp r22;
  fp_mul(r22,r1,r21);
  fp r23;
  fp_mul(r23,r1,r22);
  fp r24;
  fp_mul(r24,r1,r23);
  fp r25;
  fp_mul(r25,r1,r24);
  fp r26;
  fp_mul(r26,r1,r25);
  fp r27;
  fp_mul(r27,r1,r26);
  fp r28;
  fp_mul(r28,r1,r27);
  fp r29;
  fp_mul(r29,r1,r28);
  fp r30;
  fp_mul(r30,r1,r29);
  fp r31;
  fp_mul(r31,r1,r30);
  fp r32;
  fp_mul(r32,r1,r31);
  fp r33;
  fp_mul(r33,r1,r32);
  fp_mul(r1,r1,r33);
  fp_sqr(r33,r29);
  fp_sq1_rep(r33,5);
  fp_mul(r33,r33,r26);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r1);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r26);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r0);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r14);
  fp_sq1_rep(r33,11);
  fp_mul(r33,r33,r6);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r27);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r19);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r20);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r26);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r8);
  fp_sq1_rep(r33,9);
  fp_mul(r33,r33,r25);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r16);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r12);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r13);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r30);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r9);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r22);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r3);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r3);
  fp_sq1_rep(r33,10);
  fp_mul(r33,r33,r13);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r19);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r19);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r6);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r5);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r27);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r17);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r14);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r17);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r15);
  fp_sq1_rep(r33,9);
  fp_mul(r33,r33,r28);
  fp_sq1_rep(r33,10);
  fp_mul(r33,r33,r24);
  fp_sq1_rep(r33,11);
  fp_mul(r33,r33,r18);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r25);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r10);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r5);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r7);
  fp_sq1_rep(r33,9);
  fp_mul(r33,r33,r7);
  fp_sq1_rep(r33,9);
  fp_mul(r33,r33,r30);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r10);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r29);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r21);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r11);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r23);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r6);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r21);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r16);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r15);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r6);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r26);
  fp_sq1_rep(r33,11);
  fp_mul(r33,r33,r27);
  fp_sq1_rep(r33,9);
  fp_mul(r33,r33,r30);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r12);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r18);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r31);
  fp_sq1_rep(r33,9);
  fp_mul(r33,r33,r19);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r31);
  fp_sq1_rep(r33,10);
  fp_mul(r33,r33,r16);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r20);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r3);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r6);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r24);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r6);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r29);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r12);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r8);
  fp_sq1_rep(r33,12);
  fp_mul(r33,r33,r1);
  fp_sq1_rep(r33,9);
  fp_mul(r33,r33,r5);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r15);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r26);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r30);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r13);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r24);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r29);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r13);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r29);
  fp_sq1_rep(r33,9);
  fp_mul(r33,r33,r26);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r19);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r17);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r28);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r23);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r6);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r23);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r32);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r31);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r22);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r3);
  fp_sq1_rep(r33,9);
  fp_mul(r33,r33,r20);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r20);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r4);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r0);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r19);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r32);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r16);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r8);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r11);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r9);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r4);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r20);
  fp_sq1_rep(r33,10);
  fp_mul(r33,r33,r3);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r31);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r9);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r8);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r6);
  fp_sq1_rep(r33,11);
  fp_mul(r33,r33,r16);
  fp_sq1_rep(r33,10);
  fp_mul(r33,r33,r31);
  fp_sq1_rep(r33,9);
  fp_mul(r33,r33,r5);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r18);
  fp_sq1_rep(r33,8);
  fp_mul(r33,r33,r31);
  fp_sq1_rep(r33,7);
  fp_mul(r33,r33,r26);
  fp_sq1_rep(r33,10);
  fp_mul(r33,r33,r1);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r11);
  fp_sq1_rep(r33,6);
  fp_mul(r33,r33,r17);
  fp_sq1_rep(r33,7);
  fp_mul(r6,r6,r33);
  fp_sq1_rep(r6,7);
  fp_mul(r6,r6,r28);
  fp_sq1_rep(r6,7);
  fp_mul(r6,r6,r10);
  fp_sq1_rep(r6,6);
  fp_mul(r6,r6,r24);
  fp_sq1_rep(r6,9);
  fp_mul(r6,r6,r4);
  fp_sq1_rep(r6,7);
  fp_mul(r6,r6,r29);
  fp_sq1_rep(r6,6);
  fp_mul(r6,r6,r26);
  fp_sq1_rep(r6,8);
  fp_mul(r6,r6,r9);
  fp_sq1_rep(r6,6);
  fp_mul(r6,r6,r15);
  fp_sq1_rep(r6,8);
  fp_mul(r1,r1,r6);
  fp_sq1_rep(r1,9);
  fp_mul(r1,r1,r16);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r30);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r21);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r21);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r5);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r31);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r18);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r5);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r4);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r32);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r23);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r23);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r7);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r7);
  fp_sq1_rep(r1,9);
  fp_mul(r1,r1,r11);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r5);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r3);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r9);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r32);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r3);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r27);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r11);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r20);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r15);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r30);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r20);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r0);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r27);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r5);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r9);
  fp_sq1_rep(r1,10);
  fp_mul(r1,r1,r19);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r14);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r24);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r8);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r3);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r13);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r22);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r13);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r5);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r27);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r28);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r11);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r2);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r26);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r5);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r32);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r2);
  fp_sq1_rep(r1,11);
  fp_mul(r1,r1,r18);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r14);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r23);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r22);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r3);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r18);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r8);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r2);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r18);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r31);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r14);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r9);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r27);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r12);
  fp_sq1_rep(r1,13);
  fp_mul(r1,r1,r10);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r22);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r23);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r13);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r3);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r13);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r28);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r17);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r19);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r32);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r15);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r10);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r9);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r31);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r21);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r3);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r27);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r13);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r20);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r25);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r20);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r28);
  fp_sq1_rep(r1,10);
  fp_mul(r1,r1,r11);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r27);
  fp_sq1_rep(r1,8);
  fp_mul(r1,r1,r17);
  fp_sq1_rep(r1,7);
  fp_mul(r1,r1,r13);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r5);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r31);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r21);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r13);
  fp_sq1_rep(r1,6);
  fp_mul(r1,r1,r4);
  fp_sq1_rep(r1,10);
  fp_mul(r1,r1,r19);
  fp_sq1_rep(r1,7);
  fp_mul(r0,r0,r1);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r27);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r19);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r14);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r17);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r18);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r31);
  fp_sq1_rep(r0,448);
  fp_copy(x,r0);
  fp check;
  fp_sqr(check,x);
  return fp_isequal(check,origx);
}
