@256
D=A
@SP
M=D
@Sys.init$RETURN1
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
@Sys.init
0;JMP
(Sys.init$RETURN1)
// writing function: Class1.set
(Class1.set)
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
// writing:C_POP static 0
@SP
M=M-1
A=M
D=M
@Class1.0
M=D
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
// writing:C_POP static 1
@SP
M=M-1
A=M
D=M
@Class1.1
M=D
// writing:C_PUSH constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing return: return
//# endframe = LCL
@LCL
D=M
@ENDFRAME1
M=D
//#  # retaddr = *(endframe-5)
@5
D=D-A
A=D
D=M
@RETURN1
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
@ENDFRAME1
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@ENDFRAME1
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@ENDFRAME1
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@ENDFRAME1
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@RETURN1
A=M
0;JMP
// writing function: Class1.get
(Class1.get)
// writing:C_PUSH static 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH static 1
@Class1.1
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
//# endframe = LCL
@LCL
D=M
@ENDFRAME1
M=D
//#  # retaddr = *(endframe-5)
@5
D=D-A
A=D
D=M
@RETURN1
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
@ENDFRAME1
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@ENDFRAME1
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@ENDFRAME1
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@ENDFRAME1
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@RETURN1
A=M
0;JMP
// writing function: Class2.set
(Class2.set)
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
// writing:C_POP static 0
@SP
M=M-1
A=M
D=M
@Class2.0
M=D
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
// writing:C_POP static 1
@SP
M=M-1
A=M
D=M
@Class2.1
M=D
// writing:C_PUSH constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing return: return
//# endframe = LCL
@LCL
D=M
@ENDFRAME1
M=D
//#  # retaddr = *(endframe-5)
@5
D=D-A
A=D
D=M
@RETURN1
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
@ENDFRAME1
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@ENDFRAME1
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@ENDFRAME1
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@ENDFRAME1
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@RETURN1
A=M
0;JMP
// writing function: Class2.get
(Class2.get)
// writing:C_PUSH static 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH static 1
@Class2.1
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
//# endframe = LCL
@LCL
D=M
@ENDFRAME1
M=D
//#  # retaddr = *(endframe-5)
@5
D=D-A
A=D
D=M
@RETURN1
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
@ENDFRAME1
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@ENDFRAME1
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@ENDFRAME1
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@ENDFRAME1
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@RETURN1
A=M
0;JMP
// writing function: Sys.init
(Sys.init)
// writing:C_PUSH constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
//writing call: Class1.set
@Class1.set$RETURN2
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
@7
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(Class1.set$RETURN2)
// writing:C_POP temp 0
@SP
M=M-1
A=M
D=M
@R5
M=D
// writing:C_PUSH constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
//writing call: Class2.set
@Class2.set$RETURN3
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
@7
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(Class2.set$RETURN3)
// writing:C_POP temp 0
@SP
M=M-1
A=M
D=M
@R5
M=D
//writing call: Class1.get
@Class1.get$RETURN4
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
@Class1.get
0;JMP
(Class1.get$RETURN4)
//writing call: Class2.get
@Class2.get$RETURN5
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
@Class2.get
0;JMP
(Class2.get$RETURN5)
// writing label: WHILE
(WHILE)
// writing goto: WHILE

@WHILE

0;JMP
