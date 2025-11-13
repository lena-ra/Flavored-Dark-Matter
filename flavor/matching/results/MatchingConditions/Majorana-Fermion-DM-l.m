(* Created with the Wolfram Language : www.wolfram.com *)
{Coupling[gL, {}, 0] -> Coupling[cW2, {}, 0], 
 Coupling[gs, {}, 0] -> Coupling[gs, {}, 0], 
 Coupling[gY, {}, 0] -> Coupling[cB2, {}, 0], 
 Coupling[Yd, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[Yd, {Index[i1, Flavor], Index[i2, Flavor]}, 0], 
 Coupling[Ye, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[cHle, {Index[i1, Flavor], Index[i2, Flavor]}, 0], 
 Coupling[Yu, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[Yu, {Index[i1, Flavor], Index[i2, Flavor]}, 0], 
 Coupling[\[Lambda], {}, 0] -> -2*Coupling[cH4, {}, 0] - 
   (hbar*Coupling[cB2, {}, 0]^4*Coupling[CH2, {}, 2])/
    (120*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Coupling[CH2, {}, 2]*Coupling[cW2, {}, 0]^4)/
    (40*Coupling[M\[Phi], {}, 0]^2) - 
   (2*hbar*Coupling[CH2, {}, 2]*Coupling[\[Lambda]H\[Phi]1, {}, 0]^2)/
    (3*Coupling[M\[Phi], {}, 0]^2) - 
   (2*hbar*Coupling[CH2, {}, 2]*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0])/(3*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]H\[Phi]3, {}, 0]]*Coupling[CH2, {}, 2]*
     Coupling[\[Lambda]H\[Phi]3, {}, 0])/(3*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[\[Mu]2, {}, 2] -> Coupling[CH2, {}, 2], 
 Coupling[cllHH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/2*(hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]]*Bar[Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]]*
    Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]*Coupling[\[Lambda]H\[Phi]3, 
     {}, 0]*LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], 
       {Index[d$$1, Flavor]}, 0]}, {2, 1, 0}]), 
 Coupling[cdB, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cdd, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/1080*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cdG, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cdH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/240*(hbar*Coupling[cW2, {}, 0]^4*Coupling[Yd, {Index[i1, Flavor], 
        Index[i2, Flavor]}, 0])/Coupling[M\[Phi], {}, 0]^2 + 
   (hbar*Coupling[Yd, {Index[i1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/(12*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]H\[Phi]3, {}, 0]]*
     Coupling[Yd, {Index[i1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]H\[Phi]3, {}, 0])/(12*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cdW, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[ceB, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/8*(hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cB2, {}, 0]*
     Coupling[cHle, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {2, 1, 0}]) + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cB2, {}, 0]*
     Coupling[cHle, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {3, 1, -1}])/4 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cB2, {}, 0]*
     Coupling[cHle, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {4, 1, -2}])/8, 
 Coupling[ced, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/180*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cee, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/240*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i4, Flavor]]*Delta[Index[i2, Flavor], Index[i3, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cB2, {}, 0]^4*
     Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
      Index[i4, Flavor]])/(240*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[ceH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/240*(hbar*Coupling[cHle, {Index[i1, Flavor], Index[i2, Flavor]}, 0]*
      Coupling[cW2, {}, 0]^4)/Coupling[M\[Phi], {}, 0]^2 + 
   (hbar*Coupling[cHle, {Index[i1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/(12*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]H\[Phi]3, {}, 0]]*
     Coupling[cHle, {Index[i1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]H\[Phi]3, {}, 0])/(12*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 1, 0}])/2 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]H\[Phi]2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 1, 0}])/2 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 2, -1}])/4 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]H\[Phi]2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 2, -1}])/4 - 
   (hbar*Bar[Coupling[cHle, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$3, Flavor], 
        Index[d$$4, Flavor]}, 0]]*Coupling[cHle, {Index[d$$3, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$4, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$4, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/2 + 
   hbar*Bar[Coupling[cHle, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]]*
    Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$3, Flavor], 
       Index[d$$4, Flavor]}, 0]]*Coupling[cHle, {Index[d$$3, Flavor], 
      Index[i2, Flavor]}, 0]*Coupling[cHle, {Index[i1, Flavor], 
      Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
     {Index[d$$1, Flavor], Index[d$$4, Flavor]}, 0]*
    LF[{Coupling[M\[Chi], {Index[d$$4, Flavor]}, 0], 
      Coupling[M\[Phi], {}, 0]}, {3, 1, -1}] - 
   (hbar*Bar[Coupling[cHle, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$3, Flavor], 
        Index[d$$4, Flavor]}, 0]]*Coupling[cHle, {Index[d$$3, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$4, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$4, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/2, 
 Coupling[ceu, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(90*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[ceW, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cW2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {2, 1, 0}])/8 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cW2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {3, 1, -1}])/4 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cW2, {}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {4, 1, -2}])/8, 
 Coupling[cG, {}, 0] -> 0, Coupling[cGt, {}, 0] -> 0, 
 Coupling[cH, {}, 0] -> (hbar*Coupling[cH4, {}, 0]*Coupling[cW2, {}, 0]^4)/
    (60*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]^3)/
    (3*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]^2*Coupling[\[Lambda]H\[Phi]2, {}, 
      0])/(2*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Coupling[cH4, {}, 0]*Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/
    (3*Coupling[M\[Phi], {}, 0]^2) + (hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/(2*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Coupling[\[Lambda]H\[Phi]2, {}, 0]^3)/
    (6*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Bar[Coupling[\[Lambda]H\[Phi]3, {}, 0]]*Coupling[cH4, {}, 0]*
     Coupling[\[Lambda]H\[Phi]3, {}, 0])/(3*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]H\[Phi]3, {}, 0]]*Coupling[\[Lambda]H\[Phi]1, 
      {}, 0]*Coupling[\[Lambda]H\[Phi]3, {}, 0])/
    (2*Coupling[M\[Phi], {}, 0]^2), Coupling[cHB, {}, 0] -> 
  -1/24*(hbar*Coupling[cB2, {}, 0]^2*Coupling[\[Lambda]H\[Phi]1, {}, 0])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]H\[Phi]2, {}, 0])/(48*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cHBox, {}, 0] -> 
  -1/480*(hbar*Coupling[cB2, {}, 0]^4)/Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Coupling[cW2, {}, 0]^4)/(160*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]^2)/
    (6*Coupling[M\[Phi], {}, 0]^2) - (hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0])/(6*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]H\[Phi]3, {}, 0]]*Coupling[\[Lambda]H\[Phi]3, 
      {}, 0])/(12*Coupling[M\[Phi], {}, 0]^2), Coupling[cHBt, {}, 0] -> 0, 
 Coupling[cHd, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]])/
   (360*Coupling[M\[Phi], {}, 0]^2), Coupling[cHD, {}, 0] -> 
  -1/120*(hbar*Coupling[cB2, {}, 0]^4)/Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/
    (6*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]H\[Phi]3, {}, 0]]*Coupling[\[Lambda]H\[Phi]3, 
      {}, 0])/(6*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cHe, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]])/
    (120*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Bar[Coupling[cHle, {Index[d$$1, Flavor], Index[i1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
        Index[d$$3, Flavor]}, 0]]*Coupling[cHle, {Index[d$$2, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/2 + 
   hbar*Bar[Coupling[cHle, {Index[d$$1, Flavor], Index[i1, Flavor]}, 0]]*
    Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
       Index[d$$3, Flavor]}, 0]]*Coupling[cHle, {Index[d$$2, Flavor], 
      Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
     {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
    LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 0], 
      Coupling[M\[Phi], {}, 0]}, {3, 1, -1}] - 
   (hbar*Bar[Coupling[cHle, {Index[d$$1, Flavor], Index[i1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
        Index[d$$3, Flavor]}, 0]]*Coupling[cHle, {Index[d$$2, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/2, Coupling[cHG, {}, 0] -> 0, 
 Coupling[cHGt, {}, 0] -> 0, 
 Coupling[cHl1, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]])/
    (240*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {2, 1, 0}])/12 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {2, 2, -1}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {3, 1, -1}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {2, 1, 0}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {3, 1, -1}])/12 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0]}, {4, 1, -2}])/24, 
 Coupling[cHl3, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/240*(hbar*Coupling[cW2, {}, 0]^4*Delta[Index[i1, Flavor], 
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
 Coupling[cHq1, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/720*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]])/Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cHq3, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/240*(hbar*Coupling[cW2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]])/Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cHu, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/180*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]])/Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cHud, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cHW, {}, 0] -> 
  -1/24*(hbar*Coupling[cW2, {}, 0]^2*Coupling[\[Lambda]H\[Phi]1, {}, 0])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]H\[Phi]2, {}, 0])/(48*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cHWB, {}, 0] -> (hbar*Coupling[cB2, {}, 0]*Coupling[cW2, {}, 0]*
    Coupling[\[Lambda]H\[Phi]2, {}, 0])/(24*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cHWt, {}, 0] -> 0, Coupling[cHWtB, {}, 0] -> 0, 
 Coupling[cld, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/360*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/18 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/36 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/36 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/36 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/18 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/36, 
 Coupling[cle, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/120*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/6 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/12 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/12 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/12 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/6 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/12, 
 Coupling[cledq, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[clequ1, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[clequ3, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cll, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/240*(hbar*Coupling[cW2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i4, Flavor]]*Delta[Index[i2, Flavor], Index[i3, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cB2, {}, 0]^4*
     Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
      Index[i4, Flavor]])/(480*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Coupling[cW2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (480*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/12 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/12 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/48 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/48 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/48 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/48 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/48 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/48 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/48 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/12 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/12 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/48 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/48 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/48 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/48 + 
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
 Coupling[clq1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  (hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (720*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/36 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/72 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/72 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/72 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/36 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/72, 
 Coupling[clq3, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/240*(hbar*Coupling[cW2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/12 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/24 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/12 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cW2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/24, 
 Coupling[clu, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  (hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (180*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, 0}])/9 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 2, -1}])/18 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/18 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, 0}])/18 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {3, 1, -1}])/9 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {4, 1, -2}])/18, 
 Coupling[cqd1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(1080*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cqd8, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cqe, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(360*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cqq1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/4320*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cqq3, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/480*(hbar*Coupling[cW2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cqu1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/540*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cqu8, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cquqd1, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cquqd8, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cuB, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cud1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(270*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cud8, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cuG, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cuH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/240*(hbar*Coupling[cW2, {}, 0]^4*Coupling[Yu, {Index[i1, Flavor], 
        Index[i2, Flavor]}, 0])/Coupling[M\[Phi], {}, 0]^2 + 
   (hbar*Coupling[Yu, {Index[i1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/(12*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]H\[Phi]3, {}, 0]]*
     Coupling[Yu, {Index[i1, Flavor], Index[i2, Flavor]}, 0]*
     Coupling[\[Lambda]H\[Phi]3, {}, 0])/(12*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cuu, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/270*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cuW, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cW, {}, 0] -> (hbar*Coupling[cW2, {}, 0]^3)/
   (360*Coupling[M\[Phi], {}, 0]^2), Coupling[cWt, {}, 0] -> 0, 
 Coupling[CH2, {}, 2] -> -2*hbar*Coupling[M\[Phi], {}, 0]^2*
    Coupling[\[Lambda]H\[Phi]1, {}, 0] - hbar*Coupling[M\[Phi], {}, 0]^2*
    Coupling[\[Lambda]H\[Phi]2, {}, 0] + Coupling[\[Mu]2, {}, 2] - 
   2*hbar*Coupling[M\[Phi], {}, 0]^2*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
    Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2] - 
   hbar*Coupling[M\[Phi], {}, 0]^2*Coupling[\[Lambda]H\[Phi]2, {}, 0]*
    Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2], 
 Coupling[cHle, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[Ye, {Index[i1, Flavor], Index[i2, Flavor]}, 0] + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[Ye, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i1, Flavor], Index[d$$2, Flavor]}, 0])/8 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[Ye, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i1, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0]}, {1, 1, 0}])/2 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[Ye, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i1, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0], Coupling[M\[Phi], {}, 
        0]}, {2, 1, -1}])/4, Coupling[cW2, {}, 0] -> 
  Coupling[gL, {}, 0] - (hbar*Coupling[gL, {}, 0]^3*
     Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2])/12, 
 Coupling[cB2, {}, 0] -> Coupling[gY, {}, 0] - 
   (hbar*Coupling[gY, {}, 0]^3*Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2])/12, 
 Coupling[cH4, {}, 0] -> 
  -1/240*(hbar*Coupling[CH2, {}, 2]*Coupling[gL, {}, 0]^4)/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[CH2, {}, 2]*
     Coupling[gY, {}, 0]^4)/(240*Coupling[M\[Phi], {}, 0]^2) - 
   Coupling[\[Lambda], {}, 0]/2 - (hbar*Coupling[CH2, {}, 2]*
     Coupling[\[Lambda]H\[Phi]1, {}, 0]^2)/(3*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Coupling[CH2, {}, 2]*Coupling[\[Lambda]H\[Phi]1, {}, 0]*
     Coupling[\[Lambda]H\[Phi]2, {}, 0])/(3*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Coupling[CH2, {}, 2]*Coupling[\[Lambda]H\[Phi]2, {}, 0]^2)/
    (6*Coupling[M\[Phi], {}, 0]^2) + hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]^
     2*Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2] + 
   hbar*Coupling[\[Lambda]H\[Phi]1, {}, 0]*Coupling[\[Lambda]H\[Phi]2, {}, 0]*
    Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2] + 
   (hbar*Coupling[\[Lambda]H\[Phi]2, {}, 0]^2*
     Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2])/2 + 
   (hbar*Bar[Coupling[\[Lambda]H\[Phi]3, {}, 0]]*Coupling[\[Lambda]H\[Phi]3, 
      {}, 0]*Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2])/2}
