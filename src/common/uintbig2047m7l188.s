/* DO NOT EDIT! generated by ./autogen */

.intel_syntax noprefix

#include "uintbig_namespace.h"

.section .rodata

.global secsidh_internal_2047m7l188_uintbig_1
secsidh_internal_2047m7l188_uintbig_1:
    .quad 1, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0

.global secsidh_internal_2047m7l188_uintbig_1_ctidh
secsidh_internal_2047m7l188_uintbig_1_ctidh:
    .quad 1, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0

.global secsidh_internal_2047m7l188_uintbig_p
secsidh_internal_2047m7l188_uintbig_p:
    .quad 0xffffffffffffffff, 0xffffffffffffffff, 0xffffffffffffffff, 0xffffffffffffffff
    .quad 0xffffffffffffffff, 0xffffffffffffffff, 0xffffffffffffffff, 0x384a0754ada123f3
    .quad 0xb7057521324fb4b2, 0x4d17aa4175667633, 0xad1914cb78495fba, 0x1c6f4d88b55c0275
    .quad 0xfc18236edac1633c, 0xacc896bb8a819992, 0x51222129bbcf0a64, 0xbf0ad4ace3bdce07
    .quad 0x3ff6da1a685448a8, 0x61fee929097b1848, 0x6dc9de0773988ba8, 0x7a09467acc435611
    .quad 0x3ce02fa223c2c0f8, 0xf387032fe7c7aa44, 0x84ded2d6ffeab144, 0x7d8c979cb272334a
    .quad 0xf17c971e086093a6, 0xd1fa253d07e714b2, 0x974bee85e60d4765, 0xc9341a3b27cd22b6
    .quad 0x2da13a370bc11b14, 0x628a0ca54a584b54, 0x53e678c5f5d9768d, 0x739a199813602f59

.global secsidh_internal_2047m7l188_uintbig_four_sqrt_p
secsidh_internal_2047m7l188_uintbig_four_sqrt_p:
    .quad 0x9908a7eb0d1d84c1, 0x1121506b8e274f88, 0xa38464265a350cc0, 0xe0a013552b5d9191
    .quad 0x8bc7ab79bc0ae60d, 0x7be6e95925d2bfd6, 0x9748257f91b34006, 0x7d2902997ec00b78
    .quad 0x33fe388711feeb9b, 0x6b1ccc66f500fe74, 0xb337eb5eec6cdaa9, 0x9ca1f8f90aa13079
    .quad 0x59fcdce8bc2636f8, 0xe2017acfb89d0695, 0xc2f23d93a08c111b, 0xb01e0ffec86d6bb2
    .quad 2, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0
    .quad 0, 0, 0, 0

.section .text

.global secsidh_internal_2047m7l188_uintbig_set
secsidh_internal_2047m7l188_uintbig_set:
    cld
    mov rax, rsi
    stosq
    xor rax, rax
    mov rcx, 31
    rep stosq
    ret


.global secsidh_internal_2047m7l188_uintbig_bit
secsidh_internal_2047m7l188_uintbig_bit:
    mov rcx, rsi
    and rcx, 0x3f
    shr rsi, 6
    mov rax, [rdi + 8*rsi]
    shr rax, cl
    and rax, 1
    ret


.global secsidh_internal_2047m7l188_uintbig_add
secsidh_internal_2047m7l188_uintbig_add:
    mov rax, [rsi +  0]
    add rax, [rdx +  0]
    mov [rdi +  0], rax
    .set k, 1
    .rept 31
        mov rax, [rsi + 8*k]
        adc rax, [rdx + 8*k]
        mov [rdi + 8*k], rax
        .set k, k+1
    .endr
    setc al
    movzx rax, al
    ret

.global secsidh_internal_2047m7l188_uintbig_sub
secsidh_internal_2047m7l188_uintbig_sub:
    mov rax, [rsi +  0]
    sub rax, [rdx +  0]
    mov [rdi +  0], rax
    .set k, 1
    .rept 31
        mov rax, [rsi + 8*k]
        sbb rax, [rdx + 8*k]
        mov [rdi + 8*k], rax
        .set k, k+1
    .endr
    setc al
    movzx rax, al
    ret


.global secsidh_internal_2047m7l188_uintbig_mul3_64
secsidh_internal_2047m7l188_uintbig_mul3_64:

    mulx r10, rax, [rsi +  0]
    mov [rdi +  0], rax

    mulx r11, rax, [rsi + 8]
    add  rax, r10
    mov [rdi + 8], rax

    mulx r10, rax, [rsi + 16]
    adcx rax, r11
    mov [rdi + 16], rax

    mulx r11, rax, [rsi + 24]
    adcx rax, r10
    mov [rdi + 24], rax

    mulx r10, rax, [rsi + 32]
    adcx rax, r11
    mov [rdi + 32], rax

    mulx r11, rax, [rsi + 40]
    adcx rax, r10
    mov [rdi + 40], rax

    mulx r10, rax, [rsi + 48]
    adcx rax, r11
    mov [rdi + 48], rax

    mulx r11, rax, [rsi + 56]
    adcx rax, r10
    mov [rdi + 56], rax

    mulx r10, rax, [rsi + 64]
    adcx rax, r11
    mov [rdi + 64], rax

    mulx r11, rax, [rsi + 72]
    adcx rax, r10
    mov [rdi + 72], rax

    mulx r10, rax, [rsi + 80]
    adcx rax, r11
    mov [rdi + 80], rax

    mulx r11, rax, [rsi + 88]
    adcx rax, r10
    mov [rdi + 88], rax

    mulx r10, rax, [rsi + 96]
    adcx rax, r11
    mov [rdi + 96], rax

    mulx r11, rax, [rsi + 104]
    adcx rax, r10
    mov [rdi + 104], rax

    mulx r10, rax, [rsi + 112]
    adcx rax, r11
    mov [rdi + 112], rax

    mulx r11, rax, [rsi + 120]
    adcx rax, r10
    mov [rdi + 120], rax

    mulx r10, rax, [rsi + 128]
    adcx rax, r11
    mov [rdi + 128], rax

    mulx r11, rax, [rsi + 136]
    adcx rax, r10
    mov [rdi + 136], rax

    mulx r10, rax, [rsi + 144]
    adcx rax, r11
    mov [rdi + 144], rax

    mulx r11, rax, [rsi + 152]
    adcx rax, r10
    mov [rdi + 152], rax

    mulx r10, rax, [rsi + 160]
    adcx rax, r11
    mov [rdi + 160], rax

    mulx r11, rax, [rsi + 168]
    adcx rax, r10
    mov [rdi + 168], rax

    mulx r10, rax, [rsi + 176]
    adcx rax, r11
    mov [rdi + 176], rax

    mulx r11, rax, [rsi + 184]
    adcx rax, r10
    mov [rdi + 184], rax

    mulx r10, rax, [rsi + 192]
    adcx rax, r11
    mov [rdi + 192], rax

    mulx r11, rax, [rsi + 200]
    adcx rax, r10
    mov [rdi + 200], rax

    mulx r10, rax, [rsi + 208]
    adcx rax, r11
    mov [rdi + 208], rax

    mulx r11, rax, [rsi + 216]
    adcx rax, r10
    mov [rdi + 216], rax

    mulx r10, rax, [rsi + 224]
    adcx rax, r11
    mov [rdi + 224], rax

    mulx r11, rax, [rsi + 232]
    adcx rax, r10
    mov [rdi + 232], rax

    mulx r10, rax, [rsi + 240]
    adcx rax, r11
    mov [rdi + 240], rax

    mulx r11, rax, [rsi + 248]
    adcx rax, r10
    mov [rdi + 248], rax

    ret
