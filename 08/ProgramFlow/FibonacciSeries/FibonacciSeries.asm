// writing:C_PUSH argument 1
@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_POP pointer 1
@SP
M=M-1
A=M
D=M
@R4
M=D
// writing:C_PUSH constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_POP that 0
@0
D=A
@THAT
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// writing:C_PUSH constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_POP that 1
@1
D=A
@THAT
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// writing:C_PUSH argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
// writing:C_POP argument 0
@0
D=A
@ARG
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// writing label: MAIN_LOOP_START
(MAIN_LOOP_STAR)

// writing:C_PUSH argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing if-goto: COMPUTE_ELEMENT
@SP
A=M-1
D=M
@SP
M=M-1
@COMPUTE_ELEMENT
D;JNE
// writing goto: END_PROGRAM
@END_PROGRAM
// writing label: COMPUTE_ELEMENT
(COMPUTE_ELEMEN)

// writing:C_PUSH that 0
@0
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH that 1
@1
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M+D
@SP
M=M+1
// writing:C_POP that 2
@2
D=A
@THAT
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// writing:C_PUSH pointer 1
@R4
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M+D
@SP
M=M+1
// writing:C_POP pointer 1
@SP
M=M-1
A=M
D=M
@R4
M=D
// writing:C_PUSH argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
// writing:C_POP argument 0
@0
D=A
@ARG
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// writing goto: MAIN_LOOP_START
@MAIN_LOOP_START
// writing label: END_PROGRAM

(END_PROGRAM)

