
@0
D=A


@SP
A=M
M=D
@SP
M=M+1

@0
D=A
@LCL
D=M+D
@13
M=D


@SP
A=M-1
D=M
@SP
M=M-1
@R13
A=M
M=D

(BasicLoop..LOOP_START)

@0
D=A
@ARG
A=M+D
D=M


@SP
A=M
M=D
@SP
M=M+1

@0
D=A
@LCL
A=M+D
D=M


@SP
A=M
M=D
@SP
M=M+1

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

@0
D=A
@LCL
D=M+D
@13
M=D


@SP
A=M-1
D=M
@SP
M=M-1
@R13
A=M
M=D

@0
D=A
@ARG
A=M+D
D=M


@SP
A=M
M=D
@SP
M=M+1

@1
D=A


@SP
A=M
M=D
@SP
M=M+1

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

@0
D=A
@ARG
D=M+D
@13
M=D


@SP
A=M-1
D=M
@SP
M=M-1
@R13
A=M
M=D

@0
D=A
@ARG
A=M+D
D=M


@SP
A=M
M=D
@SP
M=M+1

@SP
A=M-1
D=M
@SP
M=M-1
@BasicLoop..LOOP_START
D;JNE

@0
D=A
@LCL
A=M+D
D=M


@SP
A=M
M=D
@SP
M=M+1
