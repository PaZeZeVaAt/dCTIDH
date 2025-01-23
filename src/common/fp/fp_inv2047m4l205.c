// DO NOT EDIT! generated by ./autogen

#if defined AVX2
    #include "avx2/fp-avx2.h"
#elif defined KARATSUBA
    #include "karatsuba/fp-karatsuba.h"
#else
    #include "mulx/fp.h"
#endif
// 325 mults, 2040 squarings
void fp_inv(fp x)
{
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
  fp r34;
  fp_mul(r34,r1,r33);
  fp r35;
  fp_mul(r35,r1,r34);
  fp r36;
  fp_mul(r36,r1,r35);
  fp r37;
  fp_mul(r37,r1,r36);
  fp r38;
  fp_mul(r38,r1,r37);
  fp r39;
  fp_mul(r39,r1,r38);
  fp r40;
  fp_mul(r40,r1,r39);
  fp r41;
  fp_mul(r41,r1,r40);
  fp r42;
  fp_mul(r42,r1,r41);
  fp r43;
  fp_mul(r43,r1,r42);
  fp r44;
  fp_mul(r44,r1,r43);
  fp r45;
  fp_mul(r45,r1,r44);
  fp r46;
  fp_mul(r46,r1,r45);
  fp r47;
  fp_mul(r47,r1,r46);
  fp r48;
  fp_mul(r48,r1,r47);
  fp_mul(r1,r1,r48);
  fp r49;
  fp_mul(r49,r48,r1);
  fp_sq1(&r49);
  fp_mul(r49,r49,r6);
  fp_sq1_rep(r49,7);
  fp_mul(r49,r49,r11);
  fp_sq1_rep(r49,9);
  fp_mul(r49,r49,r29);
  fp_sq1_rep(r49,8);
  fp_mul(r49,r49,r19);
  fp_sq1_rep(r49,13);
  fp_mul(r49,r49,r48);
  fp_sq1_rep(r49,7);
  fp_mul(r49,r49,r23);
  fp_sq1_rep(r49,8);
  fp_mul(r49,r49,r41);
  fp_sq1_rep(r49,13);
  fp_mul(r49,r49,r15);
  fp_sq1_rep(r49,6);
  fp_mul(r49,r49,r28);
  fp_sq1_rep(r49,7);
  fp_mul(r49,r49,r0);
  fp_sq1_rep(r49,8);
  fp_mul(r49,r49,r10);
  fp_sq1_rep(r49,6);
  fp_mul(r49,r49,r32);
  fp_sq1_rep(r49,8);
  fp_mul(r49,r49,r44);
  fp_sq1_rep(r49,8);
  fp_mul(r49,r49,r33);
  fp_sq1_rep(r49,8);
  fp_mul(r49,r49,r32);
  fp_sq1_rep(r49,10);
  fp_mul(r49,r49,r32);
  fp_sq1_rep(r49,9);
  fp_mul(r49,r49,r42);
  fp_sq1_rep(r49,9);
  fp_mul(r49,r49,r10);
  fp_sq1_rep(r49,7);
  fp_mul(r49,r49,r43);
  fp_sq1_rep(r49,12);
  fp_mul(r49,r49,r30);
  fp_sq1_rep(r49,8);
  fp_mul(r49,r49,r24);
  fp_sq1_rep(r49,8);
  fp_mul(r49,r49,r19);
  fp_sq1_rep(r49,8);
  fp_mul(r49,r49,r45);
  fp_sq1_rep(r49,9);
  fp_mul(r42,r42,r49);
  fp_sq1_rep(r42,8);
  fp_mul(r42,r42,r40);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r22);
  fp_sq1_rep(r42,6);
  fp_mul(r42,r42,r31);
  fp_sq1_rep(r42,8);
  fp_mul(r42,r42,r25);
  fp_sq1_rep(r42,9);
  fp_mul(r42,r42,r13);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r24);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r47);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r8);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r14);
  fp_sq1_rep(r42,6);
  fp_mul(r42,r42,r26);
  fp_sq1_rep(r42,11);
  fp_mul(r42,r42,r27);
  fp_sq1_rep(r42,6);
  fp_mul(r42,r42,r24);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r20);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r37);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r40);
  fp_sq1_rep(r42,12);
  fp_mul(r42,r42,r47);
  fp_sq1_rep(r42,6);
  fp_mul(r42,r42,r23);
  fp_sq1_rep(r42,8);
  fp_mul(r42,r42,r33);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r16);
  fp_sq1_rep(r42,8);
  fp_mul(r42,r42,r24);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r4);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r19);
  fp_sq1_rep(r42,9);
  fp_mul(r42,r42,r21);
  fp_sq1_rep(r42,11);
  fp_mul(r42,r42,r41);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r1);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r28);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r38);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r10);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r7);
  fp_sq1_rep(r42,8);
  fp_mul(r42,r42,r22);
  fp_sq1_rep(r42,8);
  fp_mul(r42,r42,r39);
  fp_sq1_rep(r42,8);
  fp_mul(r42,r42,r46);
  fp_sq1_rep(r42,9);
  fp_mul(r42,r42,r39);
  fp_sq1_rep(r42,15);
  fp_mul(r42,r42,r37);
  fp_sq1_rep(r42,11);
  fp_mul(r42,r42,r19);
  fp_sq1_rep(r42,8);
  fp_mul(r42,r42,r38);
  fp_sq1_rep(r42,6);
  fp_mul(r42,r42,r28);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r32);
  fp_sq1_rep(r42,8);
  fp_mul(r42,r42,r12);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r18);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r22);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r25);
  fp_sq1_rep(r42,8);
  fp_mul(r42,r42,r48);
  fp_sq1_rep(r42,7);
  fp_mul(r42,r42,r39);
  fp_sq1_rep(r42,8);
  fp_mul(r8,r8,r42);
  fp_sq1_rep(r8,6);
  fp_mul(r8,r8,r30);
  fp_sq1_rep(r8,8);
  fp_mul(r8,r8,r33);
  fp_sq1_rep(r8,7);
  fp_mul(r8,r8,r6);
  fp_sq1_rep(r8,8);
  fp_mul(r8,r8,r37);
  fp_sq1_rep(r8,7);
  fp_mul(r8,r8,r9);
  fp_sq1_rep(r8,9);
  fp_mul(r8,r8,r29);
  fp_sq1_rep(r8,7);
  fp_mul(r8,r8,r36);
  fp_sq1_rep(r8,7);
  fp_mul(r8,r8,r1);
  fp_sq1_rep(r8,9);
  fp_mul(r8,r8,r30);
  fp_sq1_rep(r8,6);
  fp_mul(r8,r8,r28);
  fp_sq1_rep(r8,10);
  fp_mul(r8,r8,r10);
  fp_sq1_rep(r8,7);
  fp_mul(r8,r8,r31);
  fp_sq1_rep(r8,8);
  fp_mul(r8,r8,r40);
  fp_sq1_rep(r8,7);
  fp_mul(r8,r8,r47);
  fp_sq1_rep(r8,6);
  fp_mul(r8,r8,r29);
  fp_sq1_rep(r8,7);
  fp_mul(r8,r8,r39);
  fp_sq1_rep(r8,6);
  fp_mul(r8,r8,r22);
  fp_sq1_rep(r8,9);
  fp_mul(r8,r8,r37);
  fp_sq1_rep(r8,6);
  fp_mul(r8,r8,r24);
  fp_sq1_rep(r8,9);
  fp_mul(r8,r8,r21);
  fp_sq1_rep(r8,9);
  fp_mul(r8,r8,r44);
  fp_sq1_rep(r8,6);
  fp_mul(r8,r8,r24);
  fp_sq1_rep(r8,7);
  fp_mul(r8,r8,r29);
  fp_sq1_rep(r8,8);
  fp_mul(r8,r8,r31);
  fp_sq1_rep(r8,9);
  fp_mul(r0,r0,r8);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r13);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r17);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r9);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r38);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r48);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r22);
  fp_sq1_rep(r0,11);
  fp_mul(r0,r0,r21);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r30);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r29);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r19);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r28);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r30);
  fp_sq1_rep(r0,9);
  fp_mul(r0,r0,r30);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r43);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r18);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r41);
  fp_sq1_rep(r0,9);
  fp_mul(r0,r0,r40);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r24);
  fp_sq1_rep(r0,11);
  fp_mul(r0,r0,r6);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r38);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r26);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r17);
  fp_sq1_rep(r0,13);
  fp_mul(r0,r0,r4);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r13);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r6);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r40);
  fp_sq1_rep(r0,10);
  fp_mul(r0,r0,r20);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r18);
  fp_sq1_rep(r0,9);
  fp_mul(r0,r0,r17);
  fp_sq1_rep(r0,10);
  fp_mul(r0,r0,r4);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r7);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r9);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r44);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r24);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,9);
  fp_mul(r0,r0,r33);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r27);
  fp_sq1_rep(r0,10);
  fp_mul(r0,r0,r41);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r19);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r9);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r39);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r16);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,9);
  fp_mul(r0,r0,r40);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r19);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r3);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r22);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r36);
  fp_sq1_rep(r0,12);
  fp_mul(r0,r0,r17);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r40);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r22);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r10);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r15);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r23);
  fp_sq1_rep(r0,9);
  fp_mul(r0,r0,r10);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r27);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r29);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r37);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r24);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r33);
  fp_sq1_rep(r0,11);
  fp_mul(r0,r0,r20);
  fp_sq1_rep(r0,9);
  fp_mul(r0,r0,r34);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r9);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r40);
  fp_sq1_rep(r0,9);
  fp_mul(r0,r0,r19);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r2);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r29);
  fp_sq1_rep(r0,9);
  fp_mul(r0,r0,r43);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r19);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r23);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r26);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r11);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r18);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r40);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r24);
  fp_sq1_rep(r0,10);
  fp_mul(r0,r0,r45);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r48);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r5);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r9);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r3);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r35);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r28);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r34);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r25);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r21);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r23);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r20);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r30);
  fp_sq1_rep(r0,10);
  fp_mul(r0,r0,r29);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r28);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r43);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r27);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r45);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r27);
  fp_sq1_rep(r0,11);
  fp_mul(r0,r0,r16);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r20);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r22);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r18);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r23);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r47);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r6);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r1);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r30);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r27);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r14);
  fp_sq1_rep(r0,10);
  fp_mul(r0,r0,r5);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,9);
  fp_mul(r0,r0,r12);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r20);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r4);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r19);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r18);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r22);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r35);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,10);
  fp_mul(r0,r0,r18);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r41);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r26);
  fp_sq1_rep(r0,10);
  fp_mul(r0,r0,r30);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r33);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r36);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r19);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r33);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r3);
  fp_sq1_rep(r0,9);
  fp_mul(r0,r0,r41);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r33);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r10);
  fp_sq1_rep(r0,9);
  fp_mul(r0,r0,r21);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r43);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r1);
  fp_sq1_rep(r0,11);
  fp_mul(r0,r0,r18);
  fp_sq1_rep(r0,8);
  fp_mul(r0,r0,r23);
  fp_sq1_rep(r0,7);
  fp_mul(r0,r0,r48);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r32);
  fp_sq1_rep(r0,6);
  fp_mul(r0,r0,r31);
  fp_copy(x,r0);
}
