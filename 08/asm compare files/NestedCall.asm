
@256
D=A
@SP
M=D

@Sys.init.return.0
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

@SP
D=M
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Sys.init
0;JMP

(Sys.init.return.0)

(Sys.init)

@4000
D=A


@SP
A=M
M=D
@SP
M=M+1

@0
D=A
@3
D=A+D
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

@5000
D=A


@SP
A=M
M=D
@SP
M=M+1

@1
D=A
@3
D=A+D
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

@Sys.main.return.1
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

@SP
D=M
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Sys.main
0;JMP

(Sys.main.return.1)

@1
D=A
@5
D=A+D
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

(Sys.Sys.init.LOOP)

@Sys.Sys.init.LOOP
0;JMP

(Sys.main)

@0
D=A

@SP
A=M
M=D
@SP
M=M+1


@0
D=A

@SP
A=M
M=D
@SP
M=M+1


@0
D=A

@SP
A=M
M=D
@SP
M=M+1


@0
D=A

@SP
A=M
M=D
@SP
M=M+1


@0
D=A

@SP
A=M
M=D
@SP
M=M+1

@4001
D=A


@SP
A=M
M=D
@SP
M=M+1

@0
D=A
@3
D=A+D
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

@5001
D=A


@SP
A=M
M=D
@SP
M=M+1

@1
D=A
@3
D=A+D
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

@200
D=A


@SP
A=M
M=D
@SP
M=M+1

@1
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

@40
D=A


@SP
A=M
M=D
@SP
M=M+1

@2
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

@6
D=A


@SP
A=M
M=D
@SP
M=M+1

@3
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

@123
D=A


@SP
A=M
M=D
@SP
M=M+1

@Sys.add12.return.2
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

@SP
D=M
@6
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D

@Sys.add12
0;JMP

(Sys.add12.return.2)

@0
D=A
@5
D=A+D
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
@LCL
A=M+D
D=M


@SP
A=M
M=D
@SP
M=M+1

@1
D=A
@LCL
A=M+D
D=M


@SP
A=M
M=D
@SP
M=M+1

@2
D=A
@LCL
A=M+D
D=M


@SP
A=M
M=D
@SP
M=M+1

@3
D=A
@LCL
A=M+D
D=M


@SP
A=M
M=D
@SP
M=M+1

@4
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

@LCL
D=M
@FRAME
M=D
@5
D=D-A
A=D
D=M
@RET
M=D  

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

@ARG
D=M+1
@SP
M=D

@FRAME
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D 


@FRAME
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D 


@FRAME
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D 


@FRAME
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D 

@RET
A=M
0;JMP

(Sys.add12)

@4002
D=A


@SP
A=M
M=D
@SP
M=M+1

@0
D=A
@3
D=A+D
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

@5002
D=A


@SP
A=M
M=D
@SP
M=M+1

@1
D=A
@3
D=A+D
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

@12
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
M=M+D
@SP
M=M+1

@LCL
D=M
@FRAME
M=D
@5
D=D-A
A=D
D=M
@RET
M=D  

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

@ARG
D=M+1
@SP
M=D

@FRAME
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D 


@FRAME
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D 


@FRAME
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D 


@FRAME
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D 

@RET
A=M
0;JMP
