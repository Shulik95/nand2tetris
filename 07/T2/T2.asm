// writing:C_PUSH constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: eq
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@JUMP0
M=-1
D;JEQ
@NJUMP0
M=0
0;JMP
(JUMP0)
(NJUMP0)
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: lt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@JUMP1
M=-1
D;JLT
@NJUMP1
M=0
0;JMP
(JUMP1)
(NJUMP1)
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: gt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@JUMP2
M=-1
D;JGT
@NJUMP2
M=0
0;JMP
(JUMP2)
(NJUMP2)
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 56
@56
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 53
@53
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
// writing:C_PUSH constant 112
@112
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
// writing arithmetic: neg
@SP
M=M-1
A=M
D=M
D=-D
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: and
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D&M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: or
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D|M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 100
@100
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_POP static 8
@SP
M=M-1
A=M
D=M
@T2.8
M=D
// writing:C_PUSH static 8
@T2.8
D=M
@SP
A=M
M=D
@SP
M=M+1
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
// writing:C_PUSH constant 3038
@3038
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
// writing:C_PUSH constant 15
@15
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
// writing:C_PUSH constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: eq
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@JUMP3
M=-1
D;JEQ
@NJUMP3
M=0
0;JMP
(JUMP3)
(NJUMP3)
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: lt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@JUMP4
M=-1
D;JLT
@NJUMP4
M=0
0;JMP
(JUMP4)
(NJUMP4)
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: gt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@JUMP5
M=-1
D;JGT
@NJUMP5
M=0
0;JMP
(JUMP5)
(NJUMP5)
D=M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 56
@56
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 53
@53
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
// writing:C_PUSH constant 112
@112
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
// writing arithmetic: neg
@SP
M=M-1
A=M
D=M
D=-D
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: and
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D&M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing arithmetic: or
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D|M
@SP
A=M
M=D
@SP
M=M+1
// writing:C_PUSH constant 100
@100
D=A
@SP
A=M
M=D
@SP
M=M+1
// writing:C_POP static 8
@SP
M=M-1
A=M
D=M
@T2.8
M=D
// writing:C_PUSH static 8
@T2.8
D=M
@SP
A=M
M=D
@SP
M=M+1
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
// writing:C_PUSH constant 3038
@3038
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
// writing:C_PUSH constant 15
@15
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
