// writing function: Sys.init
(NestedCall.Sys.init)
// writing:C_PUSH constant 4000
@4000
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
// writing:C_PUSH constant 5000
@5000
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
//writing call: Sys.main
@NestedCall.Sys.main$RETURN1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@NestedCall.Sys.main
0;JMP
(NestedCall.Sys.main$RETURN1)
// writing:C_POP temp 1
@SP
M=M-1
A=M
D=M
@R6
M=D
// writing label: LOOP
(LOOP)
// writing goto: LOOP
@LOOP
0;JMP
// writing function: Sys.main
(NestedCall.Sys.main)
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
@R0
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 4001
@4001
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
// writing:C_PUSH constant 5001
@5001
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
// writing:C_PUSH constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_POP local 1
@1
D=A
@LCL
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
// writing:C_PUSH constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_POP local 2
@2
D=A
@LCL
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
// writing:C_PUSH constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_POP local 3
@3
D=A
@LCL
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
// writing:C_PUSH constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
//writing call: Sys.add12
@NestedCall.Sys.add12$RETURN2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@NestedCall.Sys.add12
0;JMP
(NestedCall.Sys.add12$RETURN2)
// writing:C_POP temp 0
@SP
M=M-1
A=M
D=M
@R5
M=D
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
// writing:C_PUSH local 2
@2
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH local 3
@3
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH local 4
@4
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
// writing return: return
//# endframe = LCL
@LCL
D=M
@ENDFRAME2
M=D
//#  # retaddr = *(endframe-5)
@5
D=D-A
A=D
D=M
@RETURN2
M=D
//# *ARG = pop()
@0
D=A
@ARG
D=M+D
@R14
M=D
@SP
M=M-1
A=M
D=M
@R14
A=M
M=D
//# sp = arg + 1
@ARG
D=M
@SP
M=D+1
@ENDFRAME2
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@ENDFRAME2
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@ENDFRAME2
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@ENDFRAME2
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@RETURN2
A=M
0;JMP
// writing function: Sys.add12
(NestedCall.Sys.add12)
// writing:C_PUSH constant 4002
@4002
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
// writing:C_PUSH constant 5002
@5002
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
// writing:C_PUSH constant 12
@12
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
// writing return: return
//# endframe = LCL
@LCL
D=M
@ENDFRAME2
M=D
//#  # retaddr = *(endframe-5)
@5
D=D-A
A=D
D=M
@RETURN2
M=D
//# *ARG = pop()
@0
D=A
@ARG
D=M+D
@R14
M=D
@SP
M=M-1
A=M
D=M
@R14
A=M
M=D
//# sp = arg + 1
@ARG
D=M
@SP
M=D+1
@ENDFRAME2
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@ENDFRAME2
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@ENDFRAME2
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@ENDFRAME2
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@RETURN2
A=M
0;JMP
