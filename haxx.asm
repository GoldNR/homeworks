format PE GUI 4.0 DLL
entry DllMain

include 'C:\Users\rowel\AppData\Local\FASM\INCLUDE\WIN32A.INC'

section '.text' code readable executable

proc DllMain hinstDLL, fdwReason, lpvReserved
    cmp [fdwReason], 1          ; DLL_PROCESS_ATTACH
    jne .done

    mov eax, 0x0F423F		; 999999
    mov dword [0x00C0F188], eax

.done:
    ret
endp
