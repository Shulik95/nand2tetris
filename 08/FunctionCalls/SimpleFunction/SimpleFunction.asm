// writing function: SimpleFunction.test
(SimpleFunction.SimpleFunction.test)
@R0
D=A
@SP
A=M
M=D
@SP
M=M+1
@R0
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH local 1
@1
D=A
@LCL
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
// writing arithmetic: not
@SP
M=M-1
A=M
D=M
D=!D
@SP
A=M
M=D
@SP
M=M+1
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
// writing return: return
//endframe = LCL
@LCL
D=M
@ENDFRAME0
M=D
// retaddr = *(endframe-5)
@5
D=D-A
//saving endframe-5 in R15
@R15
M=D
// continue retaddr = *(endframe-5)
A=D
D=M
@RETURN0
M=D
// *ARG = pop()
@SP
M=M-1
A=M
D=M
@ARG
M=D
//sp = arg + 1
D=M
@SP
M=D+1
//LCL = *(endframe-4)
@R15
M=M+1
A=M
D=M
@LCL
M=D
//ARG = *(endframe-3)
@R15
M=M+1
A=M
D=M
@ARG
M=D
//This = *(endframe-2)
@R15
M=M+1
A=M
D=M
@THIS
M=D
//That = *(endframe-1)
@R15
M=M+1
A=M
D=M
@THAT
M=D
//writing reutrn go-to
@RETURN0
A=M
0;JMP
