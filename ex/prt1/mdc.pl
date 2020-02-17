mdc(A,A,MDC):-MDC is A.
mdc(A,B,MDC):- A>B, A1 is A-B, mdc(A1,B,MDC).
mdc(A,B,MDC):- B>A, B1=B-A, mdc(A,B1,MDC).