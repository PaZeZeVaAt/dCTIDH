#!/usr/bin/env sage -python


# how to call
# sage -python AsmMultCodegenerator.py  > fp9216.s

from sage.all import *
import math

sefOfLimbs = set()
printOut = 0
prime = 0
fullLength = 0
output = ""

def Print_mult_dyn(plimbs):
    if(plimbs%2==0):
        # .global mult_32x32
        S = ".macro mult_" + str(plimbs) + "x" + str(plimbs) + "\n"
        # mult_32x32:
        # S = S + "mult_" + str(plimbs) + "x" + str(plimbs) + ":\n"
        S = S + "push    r14\n"
        # S = S + "xor     eax, eax\n"
        # mov     ecx, 34
        # S = S + "mov     ecx, " + str(plimbs + 2) + "\n"
        S = S + "push    r13\n"
        # lea     r13, [rsi+128]
        S = S + "lea     r13, [rsi+" + str(4*plimbs)  + "]\n"
        S = S + "push    r12\n"
        S = S + "mov     r12, rdx\n"
        S = S + "mov     rdx, r13\n"
        S = S + "push    rbp\n"
        # lea     r14, [r12+128]
        S = S + "lea     r14, [r12+" + str(4*plimbs)  + "]\n"
        S = S + "mov     rbp, rsi\n"
        S = S + "push    rbx\n"
        S = S + "mov     rbx, rdi\n"
        # sub     rsp, 544
        S = S + "sub     rsp, " + str(((plimbs//2)+1)*32) + "\n"
        # S = S + "mov     rdi, rsp\n"
        # S = S + "rep stosq\n"
        # lea     rdi, [rsp+272]
        # S = S + "lea     rdi, [rsp+" + str((((plimbs//2)+1)*32)//2) + "]\n"
        # mov     ecx, 34
        # S = S + "mov     ecx, " + str(plimbs + 2) + "\n"
        # S = S + "rep stosq\n"
        S = S + "mov     rdi, rsp\n"
        # call    add_16x16        
        S = S + "add_" + str(plimbs//2) + "x" +  str(plimbs//2) + "\n"
        S = S + "mov     rdx, r14\n"
        S = S + "mov     rsi, r12\n"
        # S = S + "xor     eax, eax\n"
        # lea     rdi, [rsp+136]
        S = S + "lea     rdi, [rsp+" + str((((plimbs//2)+1)*32)//4) + "]\n"
        # call    add_16x16
        S = S + "add_" + str(plimbs//2) + "x" +  str(plimbs//2) + "\n"
        S = S + "mov     rdx, r12\n"
        S = S + "mov     rsi, rbp\n"
        S = S + "mov     rdi, rbx\n"
        # call    mult_16x16
        S = S + "mult_" + str(plimbs//2) + "x" +  str(plimbs//2) + "\n"
        # lea     r12, [rbx+256]
        S = S + "lea     r12, [rbx+" + str(plimbs*8)  + "]\n"
        S = S + "mov     rdx, rsp\n"
        # lea     rsi, [rsp+136]
        S = S + "lea     rsi, [rsp+" + str((((plimbs//2)+1)*32)//4) + "]\n"
        # lea     rdi, [rsp+272]
        S = S + "lea     rdi, [rsp+" + str((((plimbs//2)+1)*32)//2) + "]\n"
        # call    mult_17x17
        S = S + "mult_" + str(plimbs//2 + 1) + "x" +  str(plimbs//2 + 1) + "\n"
        S = S + "mov     rdx, r14\n"
        S = S + "mov     rsi, r13\n"
        S = S + "mov     rdi, r12\n"
        # call    mult_16x16
        S = S + "mult_" + str(plimbs//2) + "x" +  str(plimbs//2) + "\n"    
        S = S + "mov     rdx, r12\n"
        S = S + "mov     rsi, rbx\n"
        # S = S + "xor     eax, eax\n"
        # lea     rdi, [rsp+272]
        S = S + "lea     rdi, [rsp+" + str((((plimbs//2)+1)*32)//2) + "]\n"
        # call    sub_d_34x32_woc
        S = S + "sub_d_" +  str(plimbs + 2) + "x" + str(plimbs) + "_woc\n"
        # lea     rdi, [rbx+128]
        S = S + "lea     rdi, [rbx+" + str(4*plimbs)  + "]\n"

        S = S + "lea     rdx, [rsp+" + str((((plimbs//2)+1)*32)//2) + "]\n"
        # S = S + "xor     eax, eax\n"
        S = S + "mov     rsi, rdi\n"
        # call    add_34x33
        S = S + "add_" +  str(plimbs + 2) + "x" + str(plimbs + 1) + "\n"
        # add     rsp, 544
        S = S + "add     rsp, " + str(((plimbs//2)+1)*32) + "\n"
        S = S + "pop     rbx\n"
        S = S + "pop     rbp\n"
        S = S + "pop     r12\n"
        S = S + "pop     r13\n"
        S = S + "pop     r14\n"
        S = S + ".endm\n\n"
    else:
        # .global mult_32x32
        S = ".macro mult_" + str(plimbs) + "x" + str(plimbs) + "\n"
        # mult_32x32:
        # S = S + "mult_" + str(plimbs) + "x" + str(plimbs) + ":\n"
        S = S + "push    r14\n"
        # S = S + "xor     eax, eax\n"
        # mov     ecx, 34
        # S = S + "mov     ecx, " + str(plimbs + 1) + "\n"
        S = S + "push    r13\n"
        # lea     r13, [rsi+128]
        S = S + "lea     r13, [rsi+" + str(4*(plimbs-1))  + "]\n"
        S = S + "push    r12\n"
        S = S + "mov     r12, rdx\n"
        S = S + "mov     rdx, rsi\n"
        S = S + "push    rbp\n"
        # lea     r14, [r12+128]
        S = S + "lea     r14, [r12+" + str(4*(plimbs-1))  + "]\n"
        S = S + "mov     rbp, rsi\n"
        S = S + "mov     rsi, r13\n"
        S = S + "push    rbx\n"
        S = S + "mov     rbx, rdi\n"
        # sub     rsp, 544
        S = S + "sub     rsp, " + str(((plimbs//2)+2)*32) + "\n"
        # S = S + "mov     rdi, rsp\n"
        # S = S + "rep stosq\n"
        # lea     rdi, [rsp+272]
        # S = S + "lea     rdi, [rsp+" + str((((plimbs//2)+1)*32)//2) + "]\n"
        # mov     ecx, 34
        # S = S + "mov     ecx, " + str(plimbs + 1) + "\n"
        # S = S + "rep stosq\n"
        S = S + "mov     rdi, rsp\n"
        # call    add_16x16
        S = S + "add_" + str(plimbs//2 + 1) + "x" +  str(plimbs//2) + "\n"
        S = S + "mov     rdx, r12\n"
        S = S + "mov     rsi, r14\n"        
        # lea     rdi, [rsp+136]
        S = S + "lea     rdi, [rsp+" + str((((plimbs//2)+2)*32)//4) + "]\n"       
        # S = S + "xor     eax, eax\n"         
        # call    add_16x16
        S = S + "add_" + str(plimbs//2 + 1) + "x" +  str(plimbs//2) + "\n"
        S = S + "mov     rdx, r12\n"
        S = S + "mov     rsi, rbp\n"
        S = S + "mov     rdi, rbx\n"
        # S = S + "xor     eax, eax\n"        
        # lea     r12, [rbx+256]
        S = S + "lea     rbp, [rbx+" + str((plimbs -1) *8)  + "]\n"
        # call    mult_16x16
        S = S + "mult_" + str(plimbs//2) + "x" +  str(plimbs//2) + "\n"
        S = S + "mov     rdx, rsp\n"
        # lea     rsi, [rsp+136]
        S = S + "lea     rsi, [rsp+" + str((((plimbs//2)+2)*32)//4) + "]\n"
        # S = S + "xor     eax, eax\n"
        # lea     rdi, [rsp+272]
        S = S + "lea     rdi, [rsp+" + str((((plimbs//2)+2)*32)//2) + "]\n"
        # call    mult_17x17
        S = S + "mult_" + str(plimbs//2 + 2) + "x" +  str(plimbs//2 + 2) + "\n"
        S = S + "mov     rdx, r14\n"
        S = S + "mov     rsi, r13\n"
        S = S + "mov     rdi, rbp\n"
        # S = S + "xor     eax, eax\n"
        # call    mult_16x16
        S = S + "mult_" + str(plimbs//2 + 1) + "x" +  str(plimbs//2 + 1) + "\n"
        S = S + "mov     rsi, rbx\n"
        S = S + "mov     rdx, rbp\n"
        # S = S + "xor     eax, eax\n"
        # lea     rdi, [rsp+272]
        S = S + "lea     rdi, [rsp+" + str((((plimbs//2)+2)*32)//2) + "]\n"
        # call    sub_d_34x32_woc
        S = S + "_sub_d_" +  str(plimbs + 3) + "x" + str(plimbs + 1) + "_woc\n"
        # lea     rdi, [rbx+128]
        S = S + "lea     rdi, [rbx+" + str(4*(plimbs-1))  + "]\n"

        S = S + "lea     rdx, [rsp+" + str((((plimbs//2)+2)*32)//2) + "]\n"
        # S = S + "xor     eax, eax\n"
        S = S + "mov     rsi, rdi\n"
        # call    add_34x33
        S = S + "add_" +  str(plimbs + 2) + "x" + str(plimbs + 1) + "\n"

        # add     rsp, 544
        S = S + "add     rsp, " + str(((plimbs//2)+2)*32) + "\n"
        S = S + "pop     rbx\n"
        S = S + "pop     rbp\n"
        S = S + "pop     r12\n"
        S = S + "pop     r13\n"
        S = S + "pop     r14\n"
        S = S + ".endm\n\n"        
    # print(S)
    # return 0
    return S

def rotate(l, x):
    return l[-x:] + l[:-x]

def push():
    # S = "# -------------------\n"
    S = "# push\n"
    # S = S + "    push rbx\n    push rbp\n    push rdi\n    push rsi\n    push r12\n    push r13\n    push r14\n    push r15\n\n"
    S = S + "    push rbx\n    push rbp\n    push rsi\n    push r12\n    push r13\n    push r14\n    push r15\n\n"    
    # S = S + "    push rdx\n    push rdi\n    push rsi\n\n"    
    return S

def pop():
    # S = "# -------------------\n"
    S = "# pop\n"    
    # S = S + "    pop r15\n    pop r14\n    pop r13\n    pop r12\n    pop rsi\n    pop rdi\n    pop rbp\n    pop rbx\n\n"
    S = S + "    pop r15\n    pop r14\n    pop r13\n    pop r12\n    pop rsi\n    pop rbp\n    pop rbx\n\n"    
    # S = S + "    pop rsi\n    pop rdi\n    pop rdx\n\n"    
    return S


def PrintMont4kWordRedc(plimbs):
    global prime
    S = ""
    S = S + "push r14\n"
    S = S + "push r8\n"    
    S = S + "sub rsp, 2*pbytes+8\n"
    S = S + "mov r14, secsidh_internal_4095m27l262_redc_alpha@GOTPCREL[rip]\n"

    S = S + "xor rax, rax\n"  
    S = S + "xor r8, r8\n"
    S = S + "xor rcx, rcx\n"    
    S = S + "xor rbx, rbx\n" 
    # S = S + "mov [rsp + 8*" + str(2*plimbs) + "], rax\n"       

#   FIRST ITERATION ++++++++++++++++++++++++++++++++

    S = S + "########################## mul\n"
    S = S + "mov rdx, [rsi]\n"
    # S = S + "mulx rcx, rax, [r14]\n"
    # S = S + "add r8, rax\n"
    
    # S = S + "add rax, rdx\n"
    S = S + "mov rax, [rsi + 8]\n"
    S = S + "mov [rsp], rax\n\n"    

    # S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
    # S = S + "mov rax, [rsi + 8*" + str(1 + 1) + "]\n"
    # # S = S + "adox rcx, rax\n"
    # S = S + "mov [rsp + 8*" + str(1) + "], rax\n\n"       

    
    for k in range(1,plimbs):
        if(k<=25):
            # S = S + "mov rbx, r8\n"
            S = S + "mov rax, [rsi + 8*" + str(k + 1) + "]\n"
            S = S + "mov [rsp + 8*" + str(k) + "], rax\n\n"    
        else:
            if(k==plimbs-1):
                # S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                S = S + "mov rbx, r8\n"
                S = S + "adcx rcx, [rsi + 8*" + str(k + 1) + "]\n"
                S = S + "adox rcx, r8\n"
                S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"       
            else:
                if(k&1):
                    S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                    S = S + "adcx rcx, [rsi + 8*" + str(k + 1) + "]\n"
                    S = S + "adox rcx, rax\n"
                    S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"                
                else:

                    S = S + "mulx rcx, rax, [r14 + 8*" + str(k) + "]\n"
                    S = S + "adcx rbx, [rsi + 8*" + str(k + 1) + "]\n"
                    S = S + "adox rbx, rax\n"
                    S = S + "mov [rsp + 8*" + str(k) + "], rbx\n\n"

    S = S + "######### carry\n"
    # S = S + "mov r11, [rsp + 8*" + str(plimbs) + "]\n"
    # S = S + "mov r11, 0\n"    
    # S = S + "xor r8, r8\n"
    S = S + "adox rbx, [rsi + 8*" + str(plimbs+1) + "]\n"
    S = S + "adcx rbx, r8\n"
    S = S + "mov [rsp + 8*" + str(plimbs) + "], rbx\n\n"

    # S = S + "mov rax, 0\n" 
    for k in range(plimbs + 1,2*plimbs):
        S = S + "mov r11, r8\n" 
        S = S + "adc r11, [rsi + 8*" + str(k + 1) + "]\n"
        # S = S + "adcx r11, r8\n"
        S = S + "mov [rsp + 8*" + str(k) + "], r11\n\n"


#   LOOP ++++++++++++++++++++++++++++++++

    for j in range(1,plimbs-1):


        S = S + "########################## mul\n"
        S = S + "xor rax, rax\n" 
        S = S + "xor rcx, rcx\n"    
        S = S + "xor rbx, rbx\n"         
        S = S + "mov rdx, [rsp]\n"
        # S = S + "mulx rcx, rax, [r14]\n"
        # S = S + "add r8, rax\n"
        
        # S = S + "add rax, rdx\n"
        # S = S + "adcx rax, [rsp + 8]\n"
        # S = S + "mov [rsp], rax\n\n"   

        S = S + "mov rax, [rsp + 8]\n"
        S = S + "mov [rsp], rax\n\n"    

   

        for k in range(1,plimbs):
            if(k<=25):
                # S = S + "mov rbx, r8\n"
                S = S + "mov rax, [rsp + 8*" + str(k + 1) + "]\n"
                S = S + "mov [rsp + 8*" + str(k) + "], rax\n\n"   
            else:            
                if(k==plimbs-1):
                    # S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                    S = S + "mov rbx, r8\n"
                    S = S + "adcx rcx, [rsp + 8*" + str(k + 1) + "]\n"
                    S = S + "adox rcx, r8\n"
                    S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"
                else:             
                    if(k&1):
                        # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                        # S = S + "xor r8, r8\n"
                        # S = S + "mov r11, 0\n"
                        S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                        S = S + "adcx rcx, [rsp + 8*" + str(k+1) + "]\n"
                        S = S + "adox rcx, rax\n"
                        S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"                
                    else:
                        # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                        # S = S + "xor r8, r8\n"
                        # S = S + "mov r11, 0\n"
                        S = S + "mulx rcx, rax, [r14 + 8*" + str(k) + "]\n"
                        S = S + "adcx rbx, [rsp + 8*" + str(k+1) + "]\n"
                        S = S + "adox rbx, rax\n"
                        S = S + "mov [rsp + 8*" + str(k) + "], rbx\n\n"
                # S = S + "adox r11, rax\n"
                # S = S + "adox [rsp + 8*" + str(j) + "], rax\n\n"


        S = S + "######### carry\n"
        # S = S + "mov r11, [rsp + 8*" + str(plimbs) + "]\n"
        # S = S + "mov r11, 0\n"    
        # S = S + "xor r8, r8\n"
        S = S + "adox rbx, [rsp + 8*" + str(plimbs+1) + "]\n"
        S = S + "adcx rbx, r8\n"
        S = S + "mov [rsp + 8*" + str(plimbs) + "], rbx\n\n"

        # S = S + "mov rax, 0\n" 
        for k in range(plimbs+1,2*plimbs-j):
            S = S + "mov r11, r8\n" 
            S = S + "adc r11, [rsp + 8*" + str(k + 1) + "]\n"
            # S = S + "adcx r11, r8\n"
            S = S + "mov [rsp + 8*" + str(k) + "], r11\n\n"

# #   LAST ITERATION ++++++++++++++++++++++++++++++++

    j = plimbs-1

    S = S + "########################## mul\n"
    S = S + "xor rax, rax\n"  
    S = S + "xor rcx, rcx\n"    
    S = S + "xor rbx, rbx\n"       
    S = S + "mov rdx, [rsp]\n"
    # S = S + "mulx rcx, rax, [r14]\n"
    # S = S + "add r8, rax\n"
    
    # S = S + "add rax, rdx\n"
    # S = S + "adcx rax, [rsp + 8]\n"
    # S = S + "mov [rdi], rax\n\n"   

    S = S + "mov rax, [rsp + 8]\n"
    S = S + "mov [rdi], rax\n\n"    


    for k in range(1,plimbs):
        if(k<=25):
            # S = S + "mov rbx, r8\n"
            S = S + "mov rax, [rsp + 8*" + str(k + 1) + "]\n"
            S = S + "mov [rdi + 8*" + str(k) + "], rax\n\n"   
        else:             
            if(k==plimbs-1):
                # S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                S = S + "mov rbx, r8\n"
                S = S + "adcx rcx, [rsp + 8*" + str(k + 1) + "]\n"
                S = S + "adox rcx, r8\n"
                S = S + "mov [rdi + 8*" + str(k) + "], rcx\n\n"
            else:         
                if(k&1):
                    # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                    # S = S + "xor r8, r8\n"
                    # S = S + "mov r11, 0\n"
                    S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                    S = S + "adcx rcx, [rsp + 8*" + str(k+1) + "]\n"
                    S = S + "adox rcx, rax\n"
                    S = S + "mov [rdi + 8*" + str(k) + "], rcx\n\n"                
                else:
                    # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                    # S = S + "xor r8, r8\n"
                    # S = S + "mov r11, 0\n"
                    S = S + "mulx rcx, rax, [r14 + 8*" + str(k) + "]\n"
                    S = S + "adcx rbx, [rsp + 8*" + str(k+1) + "]\n"
                    S = S + "adox rbx, rax\n"
                    S = S + "mov [rdi + 8*" + str(k) + "], rbx\n\n"
                # S = S + "adox r11, rax\n"
                # S = S + "adox [rsp + 8*" + str(j) + "], rax\n\n"


    # S = S + "######### carry\n"
    # # S = S + "mov r11, [rsp + 8*" + str(plimbs) + "]\n"
    # S = S + "mov r11, 0\n"    
    # # S = S + "xor r8, r8\n"
    # S = S + "adox rbx, [rsp + 8*" + str(plimbs+1) + "]\n"
    # S = S + "adcx rbx, r11\n"
    # S = S + "mov [rdi + 8*" + str(plimbs) + "], rbx\n\n"


    S = S + "########################## done\n"
    S = S + "add rsp, 2*pbytes+8\n"
    S = S + "pop r8\n"     
    S = S + "pop r14\n"

    S = S + "jmp .reduce_once\n"

    return S



def PrintMont2kWordRedc(plimbs, cofactor, f_prefix):
    cofactor2 = cofactor//64
    global prime

    if((cofactor2-1)<1):
        S = ""

        S = S + "\n.global " + f_prefix + "fp_word_redc\n" + f_prefix + "fp_word_redc:\n"

        S = S + "push r14\n"
        S = S + "push r8\n"    
        S = S + "sub rsp, 2*pbytes+8\n"
        S = S + "mov r14, " + f_prefix + "redc_alpha@GOTPCREL[rip]\n"

        S = S + "xor rax, rax\n"  
        S = S + "xor r8, r8\n"
        # S = S + "mov [rsp + 8*" + str(2*plimbs) + "], rax\n"       

    #   FIRST ITERATION ++++++++++++++++++++++++++++++++

        S = S + "########################## mul\n"
        S = S + "mov rdx, [rsi]\n"
        S = S + "mulx rcx, rax, [r14]\n"
        # S = S + "add r8, rax\n"
        
        # S = S + "add rax, rdx\n"
        S = S + "adcx rax, [rsi + 8]\n"
        S = S + "mov [rsp], rax\n\n"    

        for k in range(1,plimbs):
            if(k==plimbs-1):
                # S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                S = S + "mov rbx, r8\n"
                S = S + "adcx rcx, [rsi + 8*" + str(k + 1) + "]\n"
                S = S + "adox rcx, r8\n"
                S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"       
            else:
                if(k&1):
                    S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                    S = S + "adcx rcx, [rsi + 8*" + str(k + 1) + "]\n"
                    S = S + "adox rcx, rax\n"
                    S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"                
                else:

                    S = S + "mulx rcx, rax, [r14 + 8*" + str(k) + "]\n"
                    S = S + "adcx rbx, [rsi + 8*" + str(k + 1) + "]\n"
                    S = S + "adox rbx, rax\n"
                    S = S + "mov [rsp + 8*" + str(k) + "], rbx\n\n"

        S = S + "######### carry\n"
        # S = S + "mov r11, [rsp + 8*" + str(plimbs) + "]\n"
        # S = S + "mov r11, 0\n"    
        # S = S + "xor r8, r8\n"
        S = S + "adox rbx, [rsi + 8*" + str(plimbs+1) + "]\n"
        S = S + "adcx rbx, r8\n"
        S = S + "mov [rsp + 8*" + str(plimbs) + "], rbx\n\n"

        # S = S + "mov rax, 0\n" 
        for k in range(plimbs + 1,2*plimbs):
            S = S + "mov r11, r8\n" 
            S = S + "adc r11, [rsi + 8*" + str(k + 1) + "]\n"
            # S = S + "adcx r11, r8\n"
            S = S + "mov [rsp + 8*" + str(k) + "], r11\n\n"


    #   LOOP ++++++++++++++++++++++++++++++++

        for j in range(1,plimbs-1):


            S = S + "########################## mul\n"
            S = S + "xor rax, rax\n"  
            S = S + "mov rdx, [rsp]\n"
            S = S + "mulx rcx, rax, [r14]\n"
            # S = S + "add r8, rax\n"
            
            # S = S + "add rax, rdx\n"
            S = S + "adcx rax, [rsp + 8]\n"
            S = S + "mov [rsp], rax\n\n"   

    

            for k in range(1,plimbs):
                if(k==plimbs-1):
                    # S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                    S = S + "mov rbx, r8\n"
                    S = S + "adcx rcx, [rsp + 8*" + str(k + 1) + "]\n"
                    S = S + "adox rcx, r8\n"
                    S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"
                else:             
                    if(k&1):
                        # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                        # S = S + "xor r8, r8\n"
                        # S = S + "mov r11, 0\n"
                        S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                        S = S + "adcx rcx, [rsp + 8*" + str(k+1) + "]\n"
                        S = S + "adox rcx, rax\n"
                        S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"                
                    else:
                        # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                        # S = S + "xor r8, r8\n"
                        # S = S + "mov r11, 0\n"
                        S = S + "mulx rcx, rax, [r14 + 8*" + str(k) + "]\n"
                        S = S + "adcx rbx, [rsp + 8*" + str(k+1) + "]\n"
                        S = S + "adox rbx, rax\n"
                        S = S + "mov [rsp + 8*" + str(k) + "], rbx\n\n"
                # S = S + "adox r11, rax\n"
                # S = S + "adox [rsp + 8*" + str(j) + "], rax\n\n"


            S = S + "######### carry\n"
            # S = S + "mov r11, [rsp + 8*" + str(plimbs) + "]\n"
            # S = S + "mov r11, 0\n"    
            # S = S + "xor r8, r8\n"
            S = S + "adox rbx, [rsp + 8*" + str(plimbs+1) + "]\n"
            S = S + "adcx rbx, r8\n"
            S = S + "mov [rsp + 8*" + str(plimbs) + "], rbx\n\n"

            # S = S + "mov rax, 0\n" 
            for k in range(plimbs+1,2*plimbs-j):
                S = S + "mov r11, r8\n" 
                S = S + "adc r11, [rsp + 8*" + str(k + 1) + "]\n"
                # S = S + "adcx r11, r8\n"
                S = S + "mov [rsp + 8*" + str(k) + "], r11\n\n"

    # #   LAST ITERATION ++++++++++++++++++++++++++++++++

        j = plimbs-1

        S = S + "########################## mul\n"
        S = S + "xor rax, rax\n"  
        S = S + "mov rdx, [rsp]\n"
        S = S + "mulx rcx, rax, [r14]\n"
        # S = S + "add r8, rax\n"
        
        # S = S + "add rax, rdx\n"
        S = S + "adcx rax, [rsp + 8]\n"
        S = S + "mov [rdi], rax\n\n"   



        for k in range(1,plimbs):
            if(k==plimbs-1):
                # S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                S = S + "mov rbx, r8\n"
                S = S + "adcx rcx, [rsp + 8*" + str(k + 1) + "]\n"
                S = S + "adox rcx, r8\n"
                S = S + "mov [rdi + 8*" + str(k) + "], rcx\n\n"
            else:         
                if(k&1):
                    # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                    # S = S + "xor r8, r8\n"
                    # S = S + "mov r11, 0\n"
                    S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                    S = S + "adcx rcx, [rsp + 8*" + str(k+1) + "]\n"
                    S = S + "adox rcx, rax\n"
                    S = S + "mov [rdi + 8*" + str(k) + "], rcx\n\n"                
                else:
                    # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                    # S = S + "xor r8, r8\n"
                    # S = S + "mov r11, 0\n"
                    S = S + "mulx rcx, rax, [r14 + 8*" + str(k) + "]\n"
                    S = S + "adcx rbx, [rsp + 8*" + str(k+1) + "]\n"
                    S = S + "adox rbx, rax\n"
                    S = S + "mov [rdi + 8*" + str(k) + "], rbx\n\n"
                # S = S + "adox r11, rax\n"
                # S = S + "adox [rsp + 8*" + str(j) + "], rax\n\n"


        # S = S + "######### carry\n"
        # # S = S + "mov r11, [rsp + 8*" + str(plimbs) + "]\n"
        # S = S + "mov r11, 0\n"    
        # # S = S + "xor r8, r8\n"
        # S = S + "adox rbx, [rsp + 8*" + str(plimbs+1) + "]\n"
        # S = S + "adcx rbx, r11\n"
        # S = S + "mov [rdi + 8*" + str(plimbs) + "], rbx\n\n"


        S = S + "########################## done\n"
        S = S + "add rsp, 2*pbytes+8\n"
        S = S + "pop r8\n"     
        S = S + "pop r14\n"

        S = S + "jmp .reduce_once\n"

    else:


        S = ""

        S = S + "\n.global " + f_prefix + "fp_word_redc\n" + f_prefix + "fp_word_redc:\n"

        S = S + "push r14\n"
        S = S + "push r8\n"    
        S = S + "sub rsp, 2*pbytes+8\n"
        S = S + "mov r14, " + f_prefix + "redc_alpha@GOTPCREL[rip]\n"

        S = S + "xor rax, rax\n"  
        S = S + "xor r8, r8\n"
        S = S + "xor rcx, rcx\n"    
        S = S + "xor rbx, rbx\n"     
        # S = S + "mov [rsp + 8*" + str(2*plimbs) + "], rax\n"       

    #   FIRST ITERATION ++++++++++++++++++++++++++++++++

        S = S + "########################## mul\n"
        S = S + "mov rdx, [rsi]\n"
        # S = S + "mulx rcx, rax, [r14]\n"
        # S = S + "add r8, rax\n"
        
        # S = S + "add rax, rdx\n"
        # S = S + "adcx rax, [rsi + 8]\n"
        
        S = S + "mov rax, [rsi + 8]\n"
        S = S + "mov [rsp], rax\n\n"    

        for k in range(1,plimbs):
            if(k<cofactor2-1):
                # S = S + "mov rbx, r8\n"
                S = S + "mov rax, [rsi + 8*" + str(k + 1) + "]\n"
                S = S + "mov [rsp + 8*" + str(k) + "], rax\n\n"   
            else:           
                if(k==plimbs-1):
                    # S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                    S = S + "mov rbx, r8\n"
                    S = S + "adcx rcx, [rsi + 8*" + str(k + 1) + "]\n"
                    S = S + "adox rcx, r8\n"
                    S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"       
                else:
                    if(k&1):
                        S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                        S = S + "adcx rcx, [rsi + 8*" + str(k + 1) + "]\n"
                        S = S + "adox rcx, rax\n"
                        S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"                
                    else:

                        S = S + "mulx rcx, rax, [r14 + 8*" + str(k) + "]\n"
                        S = S + "adcx rbx, [rsi + 8*" + str(k + 1) + "]\n"
                        S = S + "adox rbx, rax\n"
                        S = S + "mov [rsp + 8*" + str(k) + "], rbx\n\n"

        S = S + "######### carry\n"
        # S = S + "mov r11, [rsp + 8*" + str(plimbs) + "]\n"
        # S = S + "mov r11, 0\n"    
        # S = S + "xor r8, r8\n"
        S = S + "adox rbx, [rsi + 8*" + str(plimbs+1) + "]\n"
        S = S + "adcx rbx, r8\n"
        S = S + "mov [rsp + 8*" + str(plimbs) + "], rbx\n\n"

        # S = S + "mov rax, 0\n" 
        for k in range(plimbs + 1,2*plimbs):
            S = S + "mov r11, r8\n" 
            S = S + "adc r11, [rsi + 8*" + str(k + 1) + "]\n"
            # S = S + "adcx r11, r8\n"
            S = S + "mov [rsp + 8*" + str(k) + "], r11\n\n"


    #   LOOP ++++++++++++++++++++++++++++++++

        for j in range(1,plimbs-1):


            S = S + "########################## mul\n"
            S = S + "xor rax, rax\n"  
            S = S + "xor rcx, rcx\n"    
            S = S + "xor rbx, rbx\n"          
            S = S + "mov rdx, [rsp]\n"

            # S = S + "adcx rax, [rsp + 8]\n"
            S = S + "mov rax, [rsp + 8]\n"
            S = S + "mov [rsp], rax\n\n"   

    

            for k in range(1,plimbs):
                if(k<cofactor2-1):
                    # S = S + "mov rbx, r8\n"
                    S = S + "mov rax, [rsp + 8*" + str(k + 1) + "]\n"
                    S = S + "mov [rsp + 8*" + str(k) + "], rax\n\n"   
                else:             
                    if(k==plimbs-1):
                        # S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                        S = S + "mov rbx, r8\n"
                        S = S + "adcx rcx, [rsp + 8*" + str(k + 1) + "]\n"
                        S = S + "adox rcx, r8\n"
                        S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"
                    else:             
                        if(k&1):
                            # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                            # S = S + "xor r8, r8\n"
                            # S = S + "mov r11, 0\n"
                            S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                            S = S + "adcx rcx, [rsp + 8*" + str(k+1) + "]\n"
                            S = S + "adox rcx, rax\n"
                            S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"                
                        else:
                            # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                            # S = S + "xor r8, r8\n"
                            # S = S + "mov r11, 0\n"
                            S = S + "mulx rcx, rax, [r14 + 8*" + str(k) + "]\n"
                            S = S + "adcx rbx, [rsp + 8*" + str(k+1) + "]\n"
                            S = S + "adox rbx, rax\n"
                            S = S + "mov [rsp + 8*" + str(k) + "], rbx\n\n"
                    # S = S + "adox r11, rax\n"
                    # S = S + "adox [rsp + 8*" + str(j) + "], rax\n\n"


            S = S + "######### carry\n"
            # S = S + "mov r11, [rsp + 8*" + str(plimbs) + "]\n"
            # S = S + "mov r11, 0\n"    
            # S = S + "xor r8, r8\n"
            S = S + "adox rbx, [rsp + 8*" + str(plimbs+1) + "]\n"
            S = S + "adcx rbx, r8\n"
            S = S + "mov [rsp + 8*" + str(plimbs) + "], rbx\n\n"

            # S = S + "mov rax, 0\n" 
            for k in range(plimbs+1,2*plimbs-j):
                S = S + "mov r11, r8\n" 
                S = S + "adc r11, [rsp + 8*" + str(k + 1) + "]\n"
                # S = S + "adcx r11, r8\n"
                S = S + "mov [rsp + 8*" + str(k) + "], r11\n\n"

    # #   LAST ITERATION ++++++++++++++++++++++++++++++++

        j = plimbs-1

        S = S + "##########################last mul\n"
        S = S + "xor rax, rax\n"  
        S = S + "xor rcx, rcx\n"    
        S = S + "xor rbx, rbx\n"    
        S = S + "mov rdx, [rsp]\n"
        # S = S + "mulx rcx, rax, [r14]\n"

        # S = S + "adcx rax, [rsp + 8]\n"
        S = S + "mov rax, [rsp + 8]\n"
        S = S + "mov [rdi], rax\n\n"   



        for k in range(1,plimbs):
            if(k<cofactor2-1):
                # S = S + "mov rbx, r8\n"
                S = S + "mov rax, [rsp + 8*" + str(k + 1) + "]\n"
                S = S + "mov [rdi + 8*" + str(k) + "], rax\n\n"    
            else: 
                if(k==plimbs-1):
                    # S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                    S = S + "mov rbx, r8\n"
                    S = S + "adcx rcx, [rsp + 8*" + str(k + 1) + "]\n"
                    S = S + "adox rcx, r8\n"
                    S = S + "mov [rdi + 8*" + str(k) + "], rcx\n\n"
                else:         
                    if(k&1):
                        # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                        # S = S + "xor r8, r8\n"
                        # S = S + "mov r11, 0\n"
                        S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                        S = S + "adcx rcx, [rsp + 8*" + str(k+1) + "]\n"
                        S = S + "adox rcx, rax\n"
                        S = S + "mov [rdi + 8*" + str(k) + "], rcx\n\n"                
                    else:
                        # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                        # S = S + "xor r8, r8\n"
                        # S = S + "mov r11, 0\n"
                        S = S + "mulx rcx, rax, [r14 + 8*" + str(k) + "]\n"
                        S = S + "adcx rbx, [rsp + 8*" + str(k+1) + "]\n"
                        S = S + "adox rbx, rax\n"
                        S = S + "mov [rdi + 8*" + str(k) + "], rbx\n\n"
                    # S = S + "adox r11, rax\n"
                    # S = S + "adox [rsp + 8*" + str(j) + "], rax\n\n"


        # S = S + "######### carry\n"
        # # S = S + "mov r11, [rsp + 8*" + str(plimbs) + "]\n"
        # S = S + "mov r11, 0\n"    
        # # S = S + "xor r8, r8\n"
        # S = S + "adox rbx, [rsp + 8*" + str(plimbs+1) + "]\n"
        # S = S + "adcx rbx, r11\n"
        # S = S + "mov [rdi + 8*" + str(plimbs) + "], rbx\n\n"


        S = S + "########################## done\n"
        S = S + "add rsp, 2*pbytes+8\n"
        S = S + "pop r8\n"     
        S = S + "pop r14\n"

        S = S + "jmp .reduce_once\n"

    return S



def PrintMontRedc(plimbs):
    global prime
    S = ""
    S = S + "push r14\n"
    S = S + "sub rsp, 2*pbytes+8\n"
    S = S + "mov r14, secsidh_internal_"+ str(prime) +"_p@GOTPCREL[rip]\n"

    S = S + "xor rax, rax\n"  
    S = S + "mov [rsp + 8*" + str(2*plimbs) + "], rax\n"       

#   FIRST ITERATION ++++++++++++++++++++++++++++++++

    S = S + "########################## mul\n"
    S = S + "mov rdx, [rsi]\n"
    S = S + "mulx rcx, rax, [r14]\n"
    # S = S + "add r8, rax\n"
    
    # S = S + "add rax, rdx\n"
    S = S + "adcx rax, rdx\n"
    S = S + "mov [rsp], rax\n\n"    

    for k in range(1,plimbs):
        if(k&1):
            # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
            # S = S + "xor r8, r8\n"
            # S = S + "mov r11, 0\n"
            S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
            S = S + "adcx rcx, [rsi + 8*" + str(k) + "]\n"
            S = S + "adox rcx, rax\n"
            S = S + "mov [rsp + 8*" + str(k) + "], rcx\n\n"                
        else:
            # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
            # S = S + "xor r8, r8\n"
            # S = S + "mov r11, 0\n"
            S = S + "mulx rcx, rax, [r14 + 8*" + str(k) + "]\n"
            S = S + "adcx rbx, [rsi + 8*" + str(k) + "]\n"
            S = S + "adox rbx, rax\n"
            S = S + "mov [rsp + 8*" + str(k) + "], rbx\n\n"
        # S = S + "adox r11, rax\n"
        # S = S + "adox [rsp + 8*" + str(j) + "], rax\n\n"


    S = S + "######### carry\n"
    # S = S + "mov r11, [rsp + 8*" + str(plimbs) + "]\n"
    S = S + "mov r11, 0\n"    
    # S = S + "xor r8, r8\n"
    S = S + "adox rbx, [rsi + 8*" + str(plimbs) + "]\n"
    S = S + "adcx rbx, r11\n"
    S = S + "mov [rsp + 8*" + str(plimbs) + "], rbx\n\n"

    S = S + "mov rax, 0\n" 
    for k in range(plimbs+1,2*plimbs+1):
        S = S + "mov r11, 0\n" 
        S = S + "adox r11, [rsi + 8*" + str(k) + "]\n"
        S = S + "adcx r11, rax\n"
        S = S + "mov [rsp + 8*" + str(k) + "], r11\n\n"

#   LOOP ++++++++++++++++++++++++++++++++

    for j in range(1,plimbs-1):

        # S = S + "mov r11, [rsp]\n"

        S = S + "########################## mul\n"
        S = S + "xor rax, rax\n"  
        S = S + "mov rdx, [rsp + 8*" + str(j) + "]\n"
        S = S + "mulx rcx, rax, [r14]\n"
        # S = S + "add r8, rax\n"
        
        # S = S + "add rax, rdx\n"
        S = S + "adcx rax, rdx\n"
        S = S + "mov [rsp + 8*" + str(j) + "], rax\n\n"    

        for k in range(1,plimbs):
            if(k&1):
                # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                # S = S + "xor r8, r8\n"
                # S = S + "mov r11, 0\n"
                S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
                S = S + "adcx rcx, [rsp + 8*" + str(j+k) + "]\n"
                S = S + "adox rcx, rax\n"
                S = S + "mov [rsp + 8*" + str(j+k) + "], rcx\n\n"                
            else:
                # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
                # S = S + "xor r8, r8\n"
                # S = S + "mov r11, 0\n"
                S = S + "mulx rcx, rax, [r14 + 8*" + str(k) + "]\n"
                S = S + "adcx rbx, [rsp + 8*" + str(j+k) + "]\n"
                S = S + "adox rbx, rax\n"
                S = S + "mov [rsp + 8*" + str(j+k) + "], rbx\n\n"
            # S = S + "adox r11, rax\n"
            # S = S + "adox [rsp + 8*" + str(j) + "], rax\n\n"


        S = S + "######### carry\n"
        # S = S + "mov r11, [rsp + 8*" + str(plimbs) + "]\n"
        S = S + "mov r11, 0\n"    
        # S = S + "xor r8, r8\n"
        S = S + "adox rbx, [rsp + 8*" + str(plimbs+j) + "]\n"
        S = S + "adcx rbx, r11\n"
        S = S + "mov [rsp + 8*" + str(plimbs+j) + "], rbx\n\n"

        S = S + "mov rax, 0\n" 
        for k in range(plimbs+1+j,2*plimbs+1):
            S = S + "mov r11, 0\n" 
            S = S + "adox r11, [rsp + 8*" + str(k) + "]\n"
            S = S + "adcx r11, rax\n"
            S = S + "mov [rsp + 8*" + str(k) + "], r11\n\n"

#   LAST ITERATION ++++++++++++++++++++++++++++++++

    j = plimbs-1

    S = S + "########################## mul\n"
    S = S + "xor rax, rax\n"  
    S = S + "mov rdx, [rsp + 8*" + str(j) + "]\n"
    S = S + "mulx rcx, rax, [r14]\n"
    # S = S + "add r8, rax\n"
    
    # S = S + "add rax, rdx\n"
    S = S + "adcx rax, rdx\n"
    S = S + "mov [rsp + 8*" + str(j) + "], rax\n\n"    

    for k in range(1,plimbs):
        if(k&1):
            # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
            # S = S + "xor r8, r8\n"
            # S = S + "mov r11, 0\n"
            S = S + "mulx rbx, rax, [r14 + 8*" + str(k) + "]\n"
            S = S + "adcx rcx, [rsp + 8*" + str(j+k) + "]\n"
            S = S + "adox rcx, rax\n"
            S = S + "mov [rdi + 8*" + str(k-1) + "], rcx\n\n"                
        else:
            # S = S + "mov r11, [rsp + 8*" + str(k) + "]\n"
            # S = S + "xor r8, r8\n"
            # S = S + "mov r11, 0\n"
            S = S + "mulx rcx, rax, [r14 + 8*" + str(k) + "]\n"
            S = S + "adcx rbx, [rsp + 8*" + str(j+k) + "]\n"
            S = S + "adox rbx, rax\n"
            S = S + "mov [rdi + 8*" + str(k-1) + "], rbx\n\n"
        # S = S + "adox r11, rax\n"
        # S = S + "adox [rsp + 8*" + str(j) + "], rax\n\n"

    S = S + "mov r11, 0\n"    
    # # S = S + "xor r8, r8\n"
    S = S + "adox rbx, [rsp + 8*" + str(plimbs+j) + "]\n"
    S = S + "adcx rbx, r11\n"
    S = S + "mov [rdi + 8*" + str(plimbs-1) + "], rbx\n\n"   


    S = S + "########################## done\n"
    S = S + "add rsp, 2*pbytes+8\n"
    S = S + "pop r14\n"

    S = S + "jmp .reduce_once\n"

    return S



def PrintMult(plimbs):


    # registers reserved rdi, rsi, rdx
    # rax, rbx = rcx, r8
    registers = ["rcx", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    if(plimbs > len(registers)):
        print("ERROR: Index out range")
        exit()
    state = registers[:plimbs]
    #state = registers

    S = ""
    # S = ".intel_syntax noprefix\n\n"
    # S = S + ".section .rodata\n\n"
    # S = S + ".section .text\n\n"

    S = S + ".macro mult_"+ str(plimbs) + "x" + str(plimbs) + "\n"
    # S = S + "mult_"+ str(plimbs) + "x" + str(plimbs) + ":\n"
    
    S = S + push()
    
    S = S + "# intro \n"
    
    
    S = S + "    mov rbp, rdx\n"

    S = S + "    mov rdx, [rbp]\n"
    S = S + "    mulx " + state[len(state)-1] + ", rcx, [rsi + 0*8]\n"
    S = S + "    mov [rdi + 0*8], rcx\n"
    for j in range(1,plimbs):
        if(j == plimbs-1):
            S = S + "    mulx " + state[len(state)-1-(1*j)] + ", rax, [rsi + " + str(j) + "*8]\n"
            S = S + "    adc " + state[len(state)-(1*j)] + ", rax\n"            
            S = S + "    adc " + state[len(state)-1-(1*j)] + ", 0\n"
        elif(j == 1):
            S = S + "    mulx " + state[len(state)-1-(1*j)] + ", rax, [rsi + " + str(j) + "*8]\n"
            S = S + "    add " + state[len(state)-(1*j)] + ", rax\n"
        else:
            S = S + "    mulx " + state[len(state)-1-(1*j)] + ", rax, [rsi + " + str(j) + "*8]\n"
            S = S + "    adc " + state[len(state)-(1*j)] + ", rax\n"



    for i in range(1,plimbs):
        S = S + "# loop i = " + str(i) + "\n"
        S = S + "    mov rdx, [rbp + " + str(i) + "*8]\n"

        for j in range(0,plimbs):
            S = S + "    mulx rbx, rax, [rsi + " + str(j) + "*8]\n"
            if(j == 0):
                S = S + "    adcx " + state[len(state)-1] + ", rax\n"
                S = S + "    adox " + state[len(state)-2] + ", rbx\n"
                S = S + "    mov [rdi + " + str(i) + "*8], " + state[len(state)-1] + "\n"
                #S = S + "    sub " + state[len(state)-1] + ", " + state[len(state)-1] + "\n"
                S = S + "    mov " + state[len(state)-1] + ", 0\n"
            elif(j == plimbs-1):
                S = S + "    adcx " + state[len(state)-2-(1*(j-1))] + ", rax\n"
                S = S + "    adox " + state[len(state)-1] + ", rbx\n"
                S = S + "    adc " + state[len(state)-1] + ", 0\n"
            else:
                S = S + "    adcx " + state[len(state)-2-(1*(j-1))] + ", rax\n"
                S = S + "    adox " + state[len(state)-2-(1*j)] + ", rbx\n"
        state = rotate(state, 1)
    
    S = S + "# outro\n"
    for j in range(0,plimbs):
        S = S + "    mov [rdi + " + str(plimbs + j) + "*8], " + state[len(state)-1-(1*j)] + "\n"

    S = S + pop()

    S = S + ".endm\n\n"

    # print(S)
    return S

    # return 0

def PrintAdd(plimbs):

    S = ""
    # S = ".intel_syntax noprefix\n\n"
    # S = S + ".section .rodata\n\n"
    # S = S + ".section .text\n\n"
    S = S + ".macro add_"+ str(plimbs) + "x" + str(plimbs) + "\n"

    # S = S + "add_"+ str(plimbs) + "x" + str(plimbs) + ":\n"
    S = S + "# intro\n"
    S = S + "    xor r8, r8\n"    
    S = S + "    mov rax, [rsi + 0]\n    add rax, [rdx + 0]\n"
    S = S + "    mov [rdi + 0], rax\n"
    S = S + "# loop\n"
    S = S + "    .set k, 1\n"

    S = S + "    .rept " + str(plimbs-1) + "\n"

    S = S + "        mov rax, [rsi + 8*k]\n        adc rax, [rdx + 8*k]\n"
    S = S + "        mov [rdi + 8*k], rax\n        .set k, k+1\n    .endr\n"
    S = S + "# outro\n"
    # S = S + "    mov rax, [rdi + " + str(plimbs) + "*8]\n"
    S = S + "    adc r8, 0\n"
    S = S + "    mov [rdi + " + str(plimbs) + "*8], r8\n"
    # S = S + "    setc al\n    movzx rax, al\n    ret\n\n"
    S = S + ".endm\n\n"

    # print(S)
    # return 0
    return S

#
# add function for "oddly" combinations like ADD_17x16, ADD_9x8
#
def PrintAddOdd(plimbs):

    S = ""
    # S = ".intel_syntax noprefix\n\n"
    # S = S + ".section .rodata\n\n"
    # S = S + ".section .text\n\n"
    S = S + ".macro add_"+ str(plimbs + 1) + "x" + str(plimbs) + "\n"

    # S = S + "add_"+ str(plimbs + 1) + "x" + str(plimbs) + ":\n"
    S = S + "# intro\n"
    S = S + "    xor r8, r8\n"
    S = S + "    mov rax, [rsi + 0]\n    add rax, [rdx + 0]\n"
    S = S + "    mov [rdi + 0], rax\n"
    S = S + "# loop\n"
    S = S + "    .set k, 1\n"

    S = S + "    .rept " + str(plimbs-1) + "\n"

    S = S + "        mov rax, [rsi + 8*k]\n        adc rax, [rdx + 8*k]\n"
    S = S + "        mov [rdi + 8*k], rax\n        .set k, k+1\n    .endr\n"
    S = S + "# outro\n"
    S = S + "    mov rax, [rsi + 8*" + str(plimbs) + "]\n"
    S = S + "    adc rax, 0\n"   
    S = S + "    mov [rdi + 8*" + str(plimbs) + "], rax\n"
    S = S + "    adc r8, 0\n"   
    S = S + "    mov [rdi + 8*" + str(plimbs + 1) + "], r8\n"   
    #  
    # S = S + "    setc al\n    movzx rax, al\n    ret\n\n"
    S = S + ".endm\n\n"


    # print(S)
    return S
    # return 0

def PrintAddAtEnd(plimbs):

    S = ""

    S = S + ".macro add_"+ str(plimbs + 1) + "x" + str(plimbs) + "\n"

    S = S + "# intro\n"
    S = S + "    mov rax, [rsi + 0]\n    add rax, [rdx + 0]\n"
    S = S + "    mov [rdi + 0], rax\n"
    S = S + "# loop\n"
    S = S + "    .set k, 1\n"

    S = S + "    .rept " + str(plimbs) + "\n"

    S = S + "        mov rax, [rsi + 8*k]\n        adc rax, [rdx + 8*k]\n"
    S = S + "        mov [rdi + 8*k], rax\n        .set k, k+1\n    .endr\n"
    S = S + "# outro\n"
    # for i in range(plimbs+1, plimbs+4):
    for i in range(plimbs+1, plimbs+1+2):    
        S = S + "    mov rax, [rsi + 8*" + str(i)  + "]\n"
        S = S + "    adc rax, 0\n"   
        S = S + "    mov [rdi + 8*" + str(i)  + "], rax\n"

    S = S + ".endm\n\n"


    # print(S)

    return S
    # return 0


def PrintAddOddAtEnd(plimbs):

    S = ""

    S = S + ".macro add_"+ str(plimbs + 1) + "x" + str(plimbs) + "\n"

    S = S + "# intro\n"
    S = S + "    mov rax, [rsi + 0]\n    add rax, [rdx + 0]\n"
    S = S + "    mov [rdi + 0], rax\n"
    S = S + "# loop\n"
    S = S + "    .set k, 1\n"

    S = S + "    .rept " + str(plimbs+1) + "\n"

    S = S + "        mov rax, [rsi + 8*k]\n        adc rax, [rdx + 8*k]\n"
    S = S + "        mov [rdi + 8*k], rax\n        .set k, k+1\n    .endr\n"
    S = S + "# outro\n"

    for i in range(plimbs+2, (plimbs+2+3)):
        S = S + "    mov rax, [rsi + 8*" + str(i)  + "]\n"
        S = S + "    adc rax, 0\n"   
        S = S + "    mov [rdi + 8*" + str(i)  + "], rax\n"

    S = S + ".endm\n\n"


    # print(S)
    return S
    # return 0    

def PrintSubOdd(plimbs):

    
    registers = ["rax", "rbx", "rcx", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    
    S = ""

    plimbs += 1
    limbs_counter = plimbs

    S = S + "# odd intro\n"
    S = S + "    mov rax, [rdi]\n"
    S = S + "    sub rax, [rsi]\n"
    S = S + "    mov [rdi], rax\n"    


    S = S + "# loop\n"
    for i in range(1, plimbs - 1):
        S = S + "    mov rax, [rdi + " + str(i) + "*8]\n"
        S = S + "    sbb rax, [rsi + " + str(i) + "*8]\n"
        S = S + "    mov [rdi + " + str(i) + "*8], rax\n"

    # outro
    S = S + "# outro\n"
    S = S + "    mov rax, [rdi + " + str(plimbs - 1) + "*8]\n"
    S = S + "    sbb rax, 0\n"
    S = S + "    mov [rdi + " + str(plimbs - 1) + "*8], rax\n"
    S = S + "    mov rax, [rdi + " + str(plimbs) + "*8]\n"
    S = S + "    sbb rax, 0\n"
    S = S + "    mov [rdi + " + str(plimbs) + "*8], rax\n"    

    S = S + "# 2nd subtraction ---------\n"

    S = S + "# odd intro\n"
    S = S + "    mov rax, [rdi]\n"
    S = S + "    sub rax, [rdx]\n"
    S = S + "    mov [rdi], rax\n"    


    S = S + "# loop\n"
    for i in range(1, plimbs - 1):
        S = S + "    mov rax, [rdi + " + str(i) + "*8]\n"
        S = S + "    sbb rax, [rdx + " + str(i) + "*8]\n"
        S = S + "    mov [rdi + " + str(i) + "*8], rax\n"

    # outro
    S = S + "# outro\n"
    S = S + "    mov rax, [rdi + " + str(plimbs - 1) + "*8]\n"
    S = S + "    sbb rax, 0\n"
    S = S + "    mov [rdi + " + str(plimbs - 1) + "*8], rax\n"
    S = S + "    mov rax, [rdi + " + str(plimbs) + "*8]\n"
    S = S + "    sbb rax, 0\n"
    S = S + "    mov [rdi + " + str(plimbs) + "*8], rax\n"   

    S = ".macro sub_d_"+ str(plimbs + 1) + "x" + str(plimbs - 1) + "_woc\n" + S 
    # S = S + pop()

    S = S + ".endm\n\n"


    return S
    # print(S)
    # return 0

def PrintSub(plimbs):
    
    registers = ["rax", "rbx", "rcx", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    
    S = ""

    plimbs += 1
    limbs_counter = plimbs

    S = ".macro _sub_d_"+ str(plimbs + 2) + "x" + str(plimbs) + "_woc\n"

    S = S + "# intro\n"
    S = S + "    mov rax, [rdi]\n"
    S = S + "    sub rax, [rsi]\n"
    S = S + "    mov [rdi], rax\n"    


    S = S + "# loop\n"
    for i in range(1, plimbs-2):
        S = S + "    mov rax, [rdi + " + str(i) + "*8]\n"
        S = S + "    sbb rax, [rsi + " + str(i) + "*8]\n"
        S = S + "    mov [rdi + " + str(i) + "*8], rax\n"

    S = S + "# outro\n"
    S = S + "    mov rax, [rdi + " + str(plimbs-2) + "*8]\n"
    S = S + "    sbb rax, 0\n"
    S = S + "    mov [rdi + " + str(plimbs-2) + "*8], rax\n"
    S = S + "    mov rax, [rdi + " + str(plimbs-1) + "*8]\n"
    S = S + "    sbb rax, 0\n"
    S = S + "    mov [rdi + " + str(plimbs-1) + "*8], rax\n"       
    S = S + "    mov rax, [rdi + " + str(plimbs) + "*8]\n"
    S = S + "    sbb rax, 0\n"
    S = S + "    mov [rdi + " + str(plimbs) + "*8], rax\n"
    S = S + "    mov rax, [rdi + " + str(plimbs+1) + "*8]\n"
    S = S + "    sbb rax, 0\n"
    S = S + "    mov [rdi + " + str(plimbs+1) + "*8], rax\n"

    S = S + "# 2nd subtraction ---------\n"


    S = S + "# intro\n"
    S = S + "    mov rax, [rdi]\n"
    S = S + "    sub rax, [rdx]\n"
    S = S + "    mov [rdi], rax\n"    


    S = S + "# loop\n"
    for i in range(1, plimbs):
        S = S + "    mov rax, [rdi + " + str(i) + "*8]\n"
        S = S + "    sbb rax, [rdx + " + str(i) + "*8]\n"
        S = S + "    mov [rdi + " + str(i) + "*8], rax\n"

    S = S + "# outro\n"
    S = S + "    mov rax, [rdi + " + str(plimbs) + "*8]\n"
    S = S + "    sbb rax, 0\n"
    S = S + "    mov [rdi + " + str(plimbs) + "*8], rax\n"

    S = S + "    mov rax, [rdi + " + str(plimbs + 1) + "*8]\n"
    S = S + "    sbb rax, 0\n"
    S = S + "    mov [rdi + " + str(plimbs + 1) + "*8], rax\n"    

    S = S + ".endm\n\n"

    return S

    # print(S)
    # return 0    

#////////////////////////////////////////
def Print_Assembly(plimbs):
    global sefOfLimbs
    global printOut
    global output
    # global functions
    breakout = 9
    if(printOut):
        while 1 :
            if plimbs > breakout :
                print("++++++++++++++++++++++++++")
                output = output + "++++++++++++++++++++++++++"
                if(plimbs not in sefOfLimbs):
                    sefOfLimbs.add(plimbs)

                    if(plimbs%2!=1):
                        output = output + "add_" + str(plimbs//2) + "x" + str(plimbs//2) + "\n"
                        # print("add_" + str(plimbs//2) + "x" + str(plimbs//2))


                        output = output + "sub_d_" + str(plimbs + 2) + "x" + str(plimbs) + "_woc"  + "\n"
                        # print("sub_d_" + str(plimbs + 2) + "x" + str(plimbs) + "_woc")

                        output = output + "add_" + str(plimbs + 2) + "x" + str(plimbs + 1)  + "\n"
                        # print("add_" + str(plimbs + 2) + "x" + str(plimbs + 1))
                        if(plimbs > 9):
                        #     print("mult_"+ str(plimbs//2) + "x" + str(plimbs//2))
                        #     print("mult_"+ str(plimbs//2+1) + "x" + str(plimbs//2+1))
                        # else:
                            Print_Assembly(plimbs//2)
                            Print_Assembly(plimbs//2+1)
                    else:
                        output = output + "add_"+ str(plimbs//2 + 1) + "x" + str(plimbs//2)  + "\n"
                        # print("add_"+ str(plimbs//2 + 1) + "x" + str(plimbs//2))            

                        output = output + "sub_d_"+ str(plimbs + 3) + "x" + str(plimbs + 1) + "_woc"  + "\n"
                        # print("sub_d_"+ str(plimbs + 3) + "x" + str(plimbs + 1) + "_woc")
                        
                        output = output + "add_"+ str(plimbs + 2) + "x" + str(plimbs + 1)  + "\n"
                        # print("add_"+ str(plimbs + 2) + "x" + str(plimbs + 1))
                        if(plimbs > 9):
                        #     print("mult_"+ str(plimbs//2) + "x" + str(plimbs//2))
                        #     print("mult_"+ str(plimbs//2+1) + "x" + str(plimbs//2+1))
                        # else:
                            Print_Assembly(plimbs//2)
                            Print_Assembly(plimbs//2+2)
                            Print_Assembly(plimbs//2+1)                    
                    # plimbs = plimbs // 2

                    output = output + ">mult_"+ str(plimbs) + "x" + str(plimbs)  + "\n"
                    # print(">mult_"+ str(plimbs) + "x" + str(plimbs))

                else:
                    plimbs = 0
                    break
            else:
                if plimbs <= breakout:
                    if(plimbs not in sefOfLimbs):
                        sefOfLimbs.add(plimbs)
                        output = output + "mult_"+ str(plimbs) + "x" + str(plimbs)  + "\n"
                        # print("mult_"+ str(plimbs) + "x" + str(plimbs))
                    if(plimbs+1 not in sefOfLimbs):                    
                        if(plimbs+1 <= 9):
                            sefOfLimbs.add(plimbs+1)
                            output = output + "mult_"+ str(plimbs+1) + "x" + str(plimbs+1)  + "\n"
                            # print("mult_"+ str(plimbs+1) + "x" + str(plimbs+1))
                    # PrintMult(plimbs+1)
                break
    else:
        while 1 :
            if plimbs > breakout:
                if(plimbs not in sefOfLimbs):
                    sefOfLimbs.add(plimbs)

                    if(plimbs%2!=1):
                        output = output + PrintAdd(plimbs//2)
                        output = output + PrintSubOdd(plimbs)
                        output = output + PrintAddAtEnd(plimbs+1)
                        # PrintAddOddAtEnd(plimbs+1)
                        # if(plimbs > breakout):
                        Print_Assembly(plimbs//2)
                        Print_Assembly(plimbs//2+1)
                    else:
                        output = output + PrintAddOdd(plimbs//2)
                        output = output + PrintSub(plimbs)
                        # PrintAddOdd(plimbs+1)
                        output = output + PrintAddOddAtEnd(plimbs+1)
                        
                        # if(plimbs > breakout):
                        Print_Assembly(plimbs//2)
                        Print_Assembly(plimbs//2+2)
                        Print_Assembly(plimbs//2+1)    

                    # functions["mult_" + str(plimbs) + "x" + str(plimbs)]()              
                    output = output + Print_mult_dyn(plimbs)
                    # print("# ------------------" + str(plimbs) + "x" + str(plimbs))

                else:
                    plimbs = 0
                    break
            else:
                if plimbs <= breakout:
                    if(plimbs not in sefOfLimbs):
                        sefOfLimbs.add(plimbs)
                        output = output + PrintMult(plimbs)
                    if(plimbs+1 not in sefOfLimbs):                    
                        if(plimbs+1 <= breakout):
                            sefOfLimbs.add(plimbs+1)                        
                            output = output + PrintMult(plimbs+1)
                break

    return output

#//+++++++++++++++ Main ++++++++++++++++++//

def main(argv):
    global printOut
    global prime

    #PrintMult(32)

    return Print_Assembly(32)

    # print(PrintMont4kWordRedc(64))    
    # S = ""
    # print(S)
    exit(0)
    if(len(argv) < 2):
        print(
            "\nplease specify the prime and type of execution [1 = only printing functions out, 0 = print full assembly\n")
        sys.exit()
    else:
        printOut = int(argv[1])
        prime = argv[0]
        length = 0

        if(prime=="2047k221"):
            length = 2048

        elif(prime=="4095k256"):
            length = 4096

        elif(prime=="5119k234"):
            length = 5120
  
        elif(prime=="6143k256"):
            length = 6144
                             
        elif(prime=="8191k332"):
            length = 8192

        elif(prime=="9215k384"):
            length = 9216
                               
        else:
            print("\nError : no prime available for this input\n")
            sys.exit()                 


        S = ".intel_syntax noprefix\n\n"
        S = S + ".section .rodata\n\n"
        S = S + ".section .text\n\n"

        print(S)

        plimbs = length//64

        Print_Assembly(plimbs)

        S = ".global fp_mult_"+ str(plimbs) + "x" + str(plimbs) + "\n"
        S = S + "fp_mult_"+ str(plimbs) + "x" + str(plimbs) + ":\n"
        S = S + "    mult_"+ str(plimbs) + "x" + str(plimbs) + "\n"
        S = S + "    ret\n"

        print(S)

        # S = "\n.global fp_mont_redc_a\n"
        # S = S + "fp_mont_redc_a:\n"
        # print(S)
        # print(PrintMontRedc(plimbs))

        print("\n")

if __name__ == "__main__":
    main(sys.argv[1:])
