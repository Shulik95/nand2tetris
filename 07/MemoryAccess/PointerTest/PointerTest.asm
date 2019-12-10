// writing:C_PUSH constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_POP pointer 0
@SP
M=M-1
A=M
D=M
@R3
M=D
// writing:C_PUSH constant 3040
@3040
D=A
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
// writing:C_PUSH constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_POP this 2
@2
D=A
@THIS
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
// writing:C_PUSH constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_POP that 6
@6
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
// writing:C_PUSH pointer 0
@R3
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH pointer 1
@R4
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
// writing:C_PUSH this 2
@2
D=A
@THIS
A=D+M
D=M
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
// writing:C_PUSH that 6
@6
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
