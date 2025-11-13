(* Created with the Wolfram Language : www.wolfram.com *)
{Coupling[gL, {}, 0] -> Coupling[cW2, {}, 0], 
 Coupling[gs, {}, 0] -> Coupling[cG2, {}, 0], 
 Coupling[gY, {}, 0] -> Coupling[cB2, {}, 0], 
 Coupling[Yd, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[cHqd, {Index[i1, Flavor], Index[i2, Flavor]}, 0], 
 Coupling[Ye, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[Ye, {Index[i1, Flavor], Index[i2, Flavor]}, 0], 
 Coupling[Yu, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[cHqu, {Index[i1, Flavor], Index[i2, Flavor]}, 0], 
 Coupling[\[Lambda], {}, 0] -> -2*Coupling[cH4, {}, 0] - 
   (hbar*Coupling[cB2, {}, 0]^4*Coupling[CH2, {}, 2])/
    (360*Coupling[M\[Phi], {}, 0]^2) - 
   (3*hbar*Coupling[CH2, {}, 2]*Coupling[cW2, {}, 0]^4)/
    (40*Coupling[M\[Phi], {}, 0]^2) - 
   (2*hbar*Coupling[CH2, {}, 2]*Coupling[\[Lambda]H\[Phi]1, {}, 0]^2)/
    Coupling[M\[Phi], {}, 0]^2 - (2*hbar*Coupling[CH2, {}, 2]*
     Coupling[\[Lambda]H\[Phi]1, {}, 0]*Coupling[\[Lambda]H\[Phi]2, {}, 0])/
    Coupling[M\[Phi], {}, 0]^2, Coupling[\[Mu]2, {}, 2] -> 
  Coupling[CH2, {}, 2], 
 Coupling[cllHH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cdB, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cB2, {}, 0]*
     Coupling[cHqd, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {2, 1, 0}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cB2, {}, 0]*
     Coupling[cHqd, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {3, 1, -1}])/12 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cB2, {}, 0]*
     Coupling[cHqd, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {4, 1, -2}])/24, 
 Coupling[cdd, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/120*(hbar*Coupling[cG2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i4, Flavor]]*Delta[Index[i2, Flavor], Index[i3, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cB2, {}, 0]^4*
     Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
      Index[i4, Flavor]])/(3240*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Coupling[cG2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (360*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cdG, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cG2, {}, 0]*
     Coupling[cHqd, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {2, 1, 0}])/4 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cG2, {}, 0]*
     Coupling[cHqd, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {3, 1, -1}])/2 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cG2, {}, 0]*
     Coupling[cHqd, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {4, 1, -2}])/4, 
 Coupling[cdH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/80*(hbar*Coupling[cHqd, {Index[i1, Flavor], Index[i2, Flavor]}, 0]*
      Coupling[cW2, {}, 0]^4)/Coupling[M\[Phi], {}, 0]^2 + 
   (hbar*Coupling[cHqd, {Index[i1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/(4*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 1, 0}])/2 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]H\[Phi]2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 1, 0}])/2 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 2, -1}])/4 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]H\[Phi]2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 2, -1}])/4 - 
   (hbar*Bar[Coupling[cHqd, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$3, Flavor], 
        Index[d$$4, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$3, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cHqd, {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$4, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$4, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/2 + 
   hbar*Bar[Coupling[cHqd, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]]*
    Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$3, Flavor], 
       Index[d$$4, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$3, Flavor], 
      Index[i2, Flavor]}, 0]*Coupling[cHqd, {Index[i1, Flavor], 
      Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
     {Index[d$$1, Flavor], Index[d$$4, Flavor]}, 0]*
    LF[{Coupling[M\[Chi], {Index[d$$4, Flavor]}, 0], 
      Coupling[M\[Phi], {}, 0]}, {3, 1, -1}] - 
   (hbar*Bar[Coupling[cHqd, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$3, Flavor], 
        Index[d$$4, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$3, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cHqd, {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$4, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$4, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/2, 
 Coupling[cdW, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cW2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {2, 1, 0}])/8 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cW2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {3, 1, -1}])/4 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cW2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {4, 1, -2}])/8, 
 Coupling[ceB, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[ced, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/540*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cee, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/720*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i4, Flavor]]*Delta[Index[i2, Flavor], Index[i3, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cB2, {}, 0]^4*
     Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
      Index[i4, Flavor]])/(720*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[ceH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/80*(hbar*Coupling[cW2, {}, 0]^4*Coupling[Ye, {Index[i1, Flavor], 
        Index[i2, Flavor]}, 0])/Coupling[M\[Phi], {}, 0]^2 + 
   (hbar*Coupling[Ye, {Index[i1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/(4*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[ceu, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(270*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[ceW, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cG, {}, 0] -> (hbar*Coupling[cG2, {}, 0]^3)/
   (180*Coupling[M\[Phi], {}, 0]^2), Coupling[cGt, {}, 0] -> 0, 
 Coupling[cH, {}, 0] -> (hbar*Coupling[cH4, {}, 0]*Coupling[cW2, {}, 0]^4)/
    (20*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]^3)/Coupling[M\[Phi], {}, 0]^2 + 
   (3*hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]^2*Coupling[\[Lambda]H\[Phi]2, 
      {}, 0])/(2*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Coupling[cH4, {}, 0]*Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/
    Coupling[M\[Phi], {}, 0]^2 + (3*hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/(2*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Coupling[\[Lambda]H\[Phi]2, {}, 0]^3)/
    (2*Coupling[M\[Phi], {}, 0]^2), Coupling[cHB, {}, 0] -> 
  -1/72*(hbar*Coupling[cB2, {}, 0]^2*Coupling[\[Lambda]H\[Phi]1, {}, 0])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]H\[Phi]2, {}, 0])/(144*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cHBox, {}, 0] -> 
  -1/1440*(hbar*Coupling[cB2, {}, 0]^4)/Coupling[M\[Phi], {}, 0]^2 - 
   (3*hbar*Coupling[cW2, {}, 0]^4)/(160*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]^2)/
    (2*Coupling[M\[Phi], {}, 0]^2) - (hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0])/(2*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cHBt, {}, 0] -> 0, 
 Coupling[cHd, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]])/
    (1080*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Bar[Coupling[cHqd, {Index[d$$1, Flavor], Index[i1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
        Index[d$$3, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$2, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/2 + 
   hbar*Bar[Coupling[cHqd, {Index[d$$1, Flavor], Index[i1, Flavor]}, 0]]*
    Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
       Index[d$$3, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$2, Flavor], 
      Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
     {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
    LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 0], 
      Coupling[M\[Phi], {}, 0]}, {3, 1, -1}] - 
   (hbar*Bar[Coupling[cHqd, {Index[d$$1, Flavor], Index[i1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
        Index[d$$3, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$2, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/2, Coupling[cHD, {}, 0] -> 
  -1/360*(hbar*Coupling[cB2, {}, 0]^4)/Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/
    (2*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cHe, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]])/
   (360*Coupling[M\[Phi], {}, 0]^2), Coupling[cHG, {}, 0] -> 
  -1/12*(hbar*Coupling[cG2, {}, 0]^2*Coupling[\[Lambda]H\[Phi]1, {}, 0])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]H\[Phi]2, {}, 0])/(24*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cHGt, {}, 0] -> 0, 
 Coupling[cHl1, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]])/
   (720*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cHl3, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/80*(hbar*Coupling[cW2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]])/Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cHq1, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/2160*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i2, Flavor]])/Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {2, 1, 0}])/36 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {2, 2, -1}])/72 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {3, 1, -1}])/72 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {2, 1, 0}])/72 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {3, 1, -1}])/36 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {4, 1, -2}])/72, 
 Coupling[cHq3, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/80*(hbar*Coupling[cW2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i2, Flavor]])/Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {2, 1, 0}])/12 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {2, 2, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {3, 1, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {2, 1, 0}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {3, 1, -1}])/12 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {4, 1, -2}])/24, 
 Coupling[cHu, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/540*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i2, Flavor]])/Coupling[M\[Phi], {}, 0]^2 + 
   (hbar*Bar[Coupling[cHqu, {Index[d$$1, Flavor], Index[i1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
        Index[d$$3, Flavor]}, 0]]*Coupling[cHqu, {Index[d$$2, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/2 - 
   hbar*Bar[Coupling[cHqu, {Index[d$$1, Flavor], Index[i1, Flavor]}, 0]]*
    Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
       Index[d$$3, Flavor]}, 0]]*Coupling[cHqu, {Index[d$$2, Flavor], 
      Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
     {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
    LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 0], 
      Coupling[M\[Phi], {}, 0]}, {3, 1, -1}] + 
   (hbar*Bar[Coupling[cHqu, {Index[d$$1, Flavor], Index[i1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
        Index[d$$3, Flavor]}, 0]]*Coupling[cHqu, {Index[d$$2, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/2, 
 Coupling[cHud, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -(hbar*Bar[Coupling[cHqu, {Index[d$$1, Flavor], Index[i1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
        Index[d$$3, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$2, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}]) + 
   2*hbar*Bar[Coupling[cHqu, {Index[d$$1, Flavor], Index[i1, Flavor]}, 0]]*
    Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
       Index[d$$3, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$2, Flavor], 
      Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
     {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
    LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 0], 
      Coupling[M\[Phi], {}, 0]}, {3, 1, -1}] - 
   hbar*Bar[Coupling[cHqu, {Index[d$$1, Flavor], Index[i1, Flavor]}, 0]]*
    Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
       Index[d$$3, Flavor]}, 0]]*Coupling[cHqd, {Index[d$$2, Flavor], 
      Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
     {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
    LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 0], 
      Coupling[M\[Phi], {}, 0]}, {4, 1, -2}], 
 Coupling[cHW, {}, 0] -> 
  -1/8*(hbar*Coupling[cW2, {}, 0]^2*Coupling[\[Lambda]H\[Phi]1, {}, 0])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]H\[Phi]2, {}, 0])/(16*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cHWB, {}, 0] -> 
  -1/24*(hbar*Coupling[cB2, {}, 0]*Coupling[cW2, {}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0])/Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cHWt, {}, 0] -> 0, Coupling[cHWtB, {}, 0] -> 0, 
 Coupling[cld, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/1080*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cle, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/360*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cledq, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[clequ1, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[clequ3, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cll, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/80*(hbar*Coupling[cW2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i4, Flavor]]*Delta[Index[i2, Flavor], Index[i3, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cB2, {}, 0]^4*
     Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
      Index[i4, Flavor]])/(1440*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Coupling[cW2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (160*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[clq1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  (hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (2160*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/36 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/72 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/72 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/72 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/36 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/72, 
 Coupling[clq3, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/80*(hbar*Coupling[cW2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/12 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/12 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/24, 
 Coupling[clu, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(540*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cqd1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  (hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (3240*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/54 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/108 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/108 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/108 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/54 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/108, 
 Coupling[cqd8, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/30*(hbar*Coupling[cG2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/3 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/6 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/6 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/6 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/3 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/6, 
 Coupling[cqe, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  (hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (1080*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/18 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/36 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/36 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/36 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/18 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/36, 
 Coupling[cqq1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/240*(hbar*Coupling[cG2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i4, Flavor]]*Delta[Index[i2, Flavor], Index[i3, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cB2, {}, 0]^4*
     Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
      Index[i4, Flavor]])/(12960*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Coupling[cG2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (360*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/216 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/36 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/216 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/36 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/432 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/72 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/432 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/72 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/432 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/72 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/432 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/72 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/432 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/72 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/432 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/72 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/216 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/36 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/216 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/36 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/432 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/72 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/432 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/72 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Bar[Coupling[\[Lambda]\[Psi]\[Chi], 
       {Index[i4, Flavor], Index[d$$2, Flavor]}, 0]]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i3, Flavor], Index[d$$1, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 1, 1, -1}])/8 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Bar[Coupling[\[Lambda]\[Psi]\[Chi], 
       {Index[i4, Flavor], Index[d$$1, Flavor]}, 0]]*
     Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]*Coupling[M\[Chi], 
      {Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i1, Flavor], Index[d$$2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Chi], 
        {Index[d$$2, Flavor]}, 0]}, {2, 1, 1, 0}])/4, 
 Coupling[cqq3, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/240*(hbar*Coupling[cG2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i4, Flavor]]*Delta[Index[i2, Flavor], Index[i3, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cW2, {}, 0]^4*
     Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
      Index[i4, Flavor]])/(160*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/48 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/48, 
 Coupling[cqu1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/1620*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/27 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/54 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/54 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/54 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/27 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/54, 
 Coupling[cqu8, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/30*(hbar*Coupling[cG2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/3 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/6 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/6 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/6 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/3 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cG2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/6, 
 Coupling[cquqd1, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cquqd8, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cuB, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cB2, {}, 0]*
     Coupling[cHqu, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {2, 1, 0}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cB2, {}, 0]*
     Coupling[cHqu, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {3, 1, -1}])/12 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cB2, {}, 0]*
     Coupling[cHqu, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {4, 1, -2}])/24, 
 Coupling[cud1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(810*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cud8, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/30*(hbar*Coupling[cG2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cuG, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cG2, {}, 0]*
     Coupling[cHqu, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {2, 1, 0}])/4 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cG2, {}, 0]*
     Coupling[cHqu, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {3, 1, -1}])/2 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cG2, {}, 0]*
     Coupling[cHqu, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {4, 1, -2}])/4, 
 Coupling[cuH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/80*(hbar*Coupling[cHqu, {Index[i1, Flavor], Index[i2, Flavor]}, 0]*
      Coupling[cW2, {}, 0]^4)/Coupling[M\[Phi], {}, 0]^2 + 
   (hbar*Coupling[cHqu, {Index[i1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/(4*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHqu, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 1, 0}])/2 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHqu, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 2, -1}])/4 - 
   (hbar*Bar[Coupling[cHqu, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$3, Flavor], 
        Index[d$$4, Flavor]}, 0]]*Coupling[cHqu, {Index[d$$3, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cHqu, {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$4, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$4, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/2 + 
   hbar*Bar[Coupling[cHqu, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]]*
    Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$3, Flavor], 
       Index[d$$4, Flavor]}, 0]]*Coupling[cHqu, {Index[d$$3, Flavor], 
      Index[i2, Flavor]}, 0]*Coupling[cHqu, {Index[i1, Flavor], 
      Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
     {Index[d$$1, Flavor], Index[d$$4, Flavor]}, 0]*
    LF[{Coupling[M\[Chi], {Index[d$$4, Flavor]}, 0], 
      Coupling[M\[Phi], {}, 0]}, {3, 1, -1}] - 
   (hbar*Bar[Coupling[cHqu, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$3, Flavor], 
        Index[d$$4, Flavor]}, 0]]*Coupling[cHqu, {Index[d$$3, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cHqu, {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$4, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$4, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/2, 
 Coupling[cuu, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/120*(hbar*Coupling[cG2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i4, Flavor]]*Delta[Index[i2, Flavor], Index[i3, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cB2, {}, 0]^4*
     Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
      Index[i4, Flavor]])/(810*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Coupling[cG2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (360*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cuW, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHqu, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cW2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {2, 1, 0}])/8 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHqu, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cW2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {3, 1, -1}])/4 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHqu, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cW2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {4, 1, -2}])/8, 
 Coupling[cW, {}, 0] -> (hbar*Coupling[cW2, {}, 0]^3)/
   (120*Coupling[M\[Phi], {}, 0]^2), Coupling[cWt, {}, 0] -> 0, 
 Coupling[CH2, {}, 2] -> -6*hbar*Coupling[M\[Phi], {}, 0]^2*
    Coupling[\[Lambda]H\[Phi]1, {}, 0] - 3*hbar*Coupling[M\[Phi], {}, 0]^2*
    Coupling[\[Lambda]H\[Phi]2, {}, 0] + Coupling[\[Mu]2, {}, 2] - 
   6*hbar*Coupling[M\[Phi], {}, 0]^2*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
    Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2] - 
   3*hbar*Coupling[M\[Phi], {}, 0]^2*Coupling[\[Lambda]H\[Phi]2, {}, 0]*
    Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2], 
 Coupling[cHqd, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[Yd, {Index[i1, Flavor], Index[i2, Flavor]}, 0] + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[Yd, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i1, Flavor], Index[d$$2, Flavor]}, 0])/8 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[Yd, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i1, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0]}, {1, 1, 0}])/2 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[Yd, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i1, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, -1}])/4, 
 Coupling[cHqu, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[Yu, {Index[i1, Flavor], Index[i2, Flavor]}, 0] + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[Yu, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i1, Flavor], Index[d$$2, Flavor]}, 0])/8 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[Yu, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i1, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0]}, {1, 1, 0}])/2 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[Yu, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i1, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, -1}])/4, Coupling[cW2, {}, 0] -> 
  Coupling[gL, {}, 0] - (hbar*Coupling[gL, {}, 0]^3*
     Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2])/4, 
 Coupling[cG2, {}, 0] -> Coupling[gs, {}, 0] - 
   (hbar*Coupling[gs, {}, 0]^3*Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2])/6, 
 Coupling[cB2, {}, 0] -> Coupling[gY, {}, 0] - 
   (hbar*Coupling[gY, {}, 0]^3*Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2])/36, 
 Coupling[cH4, {}, 0] -> 
  -1/80*(hbar*Coupling[CH2, {}, 2]*Coupling[gL, {}, 0]^4)/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[CH2, {}, 2]*
     Coupling[gY, {}, 0]^4)/(720*Coupling[M\[Phi], {}, 0]^2) - 
   Coupling[\[Lambda], {}, 0]/2 - (hbar*Coupling[CH2, {}, 2]*
     Coupling[\[Lambda]H\[Phi]1, {}, 0]^2)/Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Coupling[CH2, {}, 2]*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0])/Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Coupling[CH2, {}, 2]*Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/
    (2*Coupling[M\[Phi], {}, 0]^2) + 
   3*hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]^2*
    Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2] + 
   3*hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]*Coupling[\[Lambda]H\[Phi]2, {}, 
     0]*Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2] + 
   (3*hbar*Coupling[\[Lambda]H\[Phi]2, {}, 0]^2*
     Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2])/2}
