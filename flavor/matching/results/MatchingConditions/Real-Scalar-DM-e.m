(* Created with the Wolfram Language : www.wolfram.com *)
{Coupling[gL, {}, 0] -> Coupling[gL, {}, 0], 
 Coupling[gs, {}, 0] -> Coupling[gs, {}, 0], 
 Coupling[gY, {}, 0] -> Coupling[cB2, {}, 0], 
 Coupling[Yd, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[Yd, {Index[i1, Flavor], Index[i2, Flavor]}, 0], 
 Coupling[Ye, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[cHle, {Index[i1, Flavor], Index[i2, Flavor]}, 0], 
 Coupling[Yu, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[Yu, {Index[i1, Flavor], Index[i2, Flavor]}, 0], 
 Coupling[\[Lambda], {}, 0] -> -2*Coupling[cH4, {}, 0] - 
   (2*hbar*Coupling[cB2, {}, 0]^4*Coupling[CH2, {}, 2])/
    (15*Coupling[M\[Phi], {}, 0]^2) + 4*hbar*Coupling[CH2, {}, 2]*
    Coupling[\[Lambda]H\[Chi], {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]^
     2*LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], 
      Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 1, 0}] - 
   4*hbar*Coupling[CH2, {}, 2]*Coupling[\[Lambda]H\[Chi], 
      {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]^2*
    LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], 
      Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {3, 1, -1}], 
 Coupling[\[Mu]2, {}, 2] -> Coupling[CH2, {}, 2], 
 Coupling[cllHH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cdB, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cdd, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (-2*hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(135*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cdG, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cdH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cdW, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[ceB, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]*
     Coupling[cHle, {Index[i1, Flavor], Index[d$$2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {3, 1, -1}])/4 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]*
     Coupling[cHle, {Index[i1, Flavor], Index[d$$2, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {4, 1, -2}])/4, 
 Coupling[ced, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  (-4*hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (45*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/6 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {4, 1, -2}])/18, 
 Coupling[cee, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/15*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
       Index[i4, Flavor]]*Delta[Index[i2, Flavor], Index[i3, Flavor]])/
     Coupling[M\[Phi], {}, 0]^2 - (hbar*Coupling[cB2, {}, 0]^4*
     Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
      Index[i4, Flavor]])/(15*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/8 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/8 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/8 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/8 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {4, 1, -2}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {4, 1, -2}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {4, 1, -2}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {4, 1, -2}])/24 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Bar[Coupling[\[Lambda]\[Psi]\[Chi], 
       {Index[i4, Flavor], Index[d$$2, Flavor]}, 0]]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i3, Flavor], Index[d$$1, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 1, 1, -1}])/
    16 + (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Bar[Coupling[\[Lambda]\[Psi]\[Chi], 
       {Index[i4, Flavor], Index[d$$2, Flavor]}, 0]]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i3, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 1, 1, -1}])/
    16 - (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Bar[Coupling[\[Lambda]\[Psi]\[Chi], 
       {Index[i4, Flavor], Index[d$$1, Flavor]}, 0]]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[i3, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 1, 1, -1}])/8, 
 Coupling[ceH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/2*(hbar*Bar[Coupling[cHle, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 
       0]]*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
        Index[d$$3, Flavor]}, 0]]*Coupling[cHle, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$4, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$4, Flavor], Index[d$$3, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$3, Flavor]}, 
        0]}, {2, 1, 0}]) + 
   hbar*Bar[Coupling[cHle, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]]*
    Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
       Index[d$$3, Flavor]}, 0]]*Coupling[cHle, {Index[d$$1, Flavor], 
      Index[i2, Flavor]}, 0]*Coupling[cHle, {Index[i1, Flavor], 
      Index[d$$4, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
     {Index[d$$4, Flavor], Index[d$$3, Flavor]}, 0]*
    LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$3, Flavor]}, 
       0]}, {3, 1, -1}] - 
   (hbar*Bar[Coupling[cHle, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
        Index[d$$3, Flavor]}, 0]]*Coupling[cHle, {Index[d$$1, Flavor], 
       Index[i2, Flavor]}, 0]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$4, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$4, Flavor], Index[d$$3, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$3, Flavor]}, 
        0]}, {4, 1, -2}])/2 - 
   hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
       Index[d$$1, Flavor]}, 0]]*Coupling[cHle, {Index[i1, Flavor], 
      Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]H\[Chi], 
     {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
    Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
      Index[d$$3, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
      Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Chi], 
       {Index[d$$3, Flavor]}, 0]}, {1, 1, 1, 0}] + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]H\[Chi], 
      {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
       Index[d$$3, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], Coupling[M\[Chi], 
        {Index[d$$3, Flavor]}, 0]}, {2, 1, 1, -1}])/2 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]H\[Chi], 
      {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
       Index[d$$3, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], 
        {Index[d$$3, Flavor]}, 0]}, {2, 1, 1, -1}])/2 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]H\[Chi], 
      {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$2, Flavor], 
       Index[d$$3, Flavor]}, 0]*LF[{Coupling[M\[Chi], {Index[d$$3, Flavor]}, 
        0], Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], 
        {Index[d$$1, Flavor]}, 0]}, {2, 1, 1, -1}])/2, 
 Coupling[ceu, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  (8*hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (45*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/3 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {4, 1, -2}])/9, 
 Coupling[ceW, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cG, {}, 0] -> 0, Coupling[cGt, {}, 0] -> 0, 
 Coupling[cH, {}, 0] -> (-4*hbar*Coupling[\[Lambda]H\[Chi], 
     {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]*
    Coupling[\[Lambda]H\[Chi], {Index[d$$1, Flavor], Index[d$$3, Flavor]}, 0]*
    Coupling[\[Lambda]H\[Chi], {Index[d$$2, Flavor], Index[d$$3, Flavor]}, 0]*
    LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], 
      Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0], Coupling[M\[Chi], 
       {Index[d$$3, Flavor]}, 0]}, {1, 1, 1, 0}])/3, 
 Coupling[cHB, {}, 0] -> 0, Coupling[cHBox, {}, 0] -> 
  -1/30*(hbar*Coupling[cB2, {}, 0]^4)/Coupling[M\[Phi], {}, 0]^2 + 
   hbar*Coupling[\[Lambda]H\[Chi], {Index[d$$1, Flavor], 
       Index[d$$2, Flavor]}, 0]^2*
    LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], 
      Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 1, 0}] - 
   hbar*Coupling[\[Lambda]H\[Chi], {Index[d$$1, Flavor], 
       Index[d$$2, Flavor]}, 0]^2*
    LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], 
      Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {3, 1, -1}], 
 Coupling[cHBt, {}, 0] -> 0, 
 Coupling[cHd, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (2*hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]])/
   (45*Coupling[M\[Phi], {}, 0]^2), Coupling[cHD, {}, 0] -> 
  (-2*hbar*Coupling[cB2, {}, 0]^4)/(15*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cHe, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (2*hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]])/
    (15*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {3, 1, -1}])/4 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i1, Flavor], 
       Index[d$$1, Flavor]}, 0]*LF[{Coupling[M\[Phi], {}, 0], 
       Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]}, {4, 1, -2}])/12, 
 Coupling[cHG, {}, 0] -> 0, Coupling[cHGt, {}, 0] -> 0, 
 Coupling[cHl1, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]])/
    (15*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[cHle, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$3, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$3, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0]}, {2, 1, 0}])/4 - 
   (hbar*Bar[Coupling[cHle, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$3, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$3, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0]}, {3, 1, -1}])/2 + 
   (hbar*Bar[Coupling[cHle, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$3, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$3, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0]}, {4, 1, -2}])/4, 
 Coupling[cHl3, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Bar[Coupling[cHle, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$3, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$3, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0]}, {2, 1, 0}])/4 - 
   (hbar*Bar[Coupling[cHle, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$3, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$3, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0]}, {3, 1, -1}])/2 + 
   (hbar*Bar[Coupling[cHle, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]]*
     Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[d$$1, Flavor], 
        Index[d$$2, Flavor]}, 0]]*Coupling[cHle, {Index[i1, Flavor], 
       Index[d$$3, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$3, Flavor], Index[d$$2, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$2, Flavor]}, 
        0]}, {4, 1, -2}])/4, 
 Coupling[cHq1, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  -1/45*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]])/Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cHq3, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cHu, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (-4*hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
     Index[i2, Flavor]])/(45*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cHud, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cHW, {}, 0] -> 0, Coupling[cHWB, {}, 0] -> 0, 
 Coupling[cHWt, {}, 0] -> 0, Coupling[cHWtB, {}, 0] -> 0, 
 Coupling[cld, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (-2*hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(45*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cle, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  (-2*hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (15*Coupling[M\[Phi], {}, 0]^2) - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/4 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {4, 1, -2}])/12, 
 Coupling[cledq, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[clequ1, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[clequ3, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cll, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/30*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    Coupling[M\[Phi], {}, 0]^2, 
 Coupling[clq1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(45*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[clq3, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[clu, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (4*hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(45*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cqd1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (2*hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(135*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cqd8, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cqe, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  (2*hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    (45*Coupling[M\[Phi], {}, 0]^2) + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {3, 1, -1}])/12 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i4, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[cB2, {}, 0]^2*
     Coupling[\[Lambda]\[Psi]\[Chi], {Index[i3, Flavor], 
       Index[d$$1, Flavor]}, 0]*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {4, 1, -2}])/36, 
 Coupling[cqq1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/270*(hbar*Coupling[cB2, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]])/
    Coupling[M\[Phi], {}, 0]^2, 
 Coupling[cqq3, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cqu1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (-4*hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(135*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cqu8, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cquqd1, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cquqd8, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cuB, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cud1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (8*hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(135*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cud8, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 0, 
 Coupling[cuG, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cuH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cuu, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (-8*hbar*Coupling[cB2, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]])/(135*Coupling[M\[Phi], {}, 0]^2), 
 Coupling[cuW, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 0, 
 Coupling[cW, {}, 0] -> 0, Coupling[cWt, {}, 0] -> 0, 
 Coupling[CH2, {}, 2] -> -(hbar*Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]^2*
     Coupling[\[Lambda]H\[Chi], {Index[d$$1, Flavor], Index[d$$1, Flavor]}, 
      0]) + Coupling[\[Mu]2, {}, 2] - 
   hbar*Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]^2*
    Coupling[\[Lambda]H\[Chi], {Index[d$$1, Flavor], Index[d$$1, Flavor]}, 0]*
    Log[\[Mu]bar2/Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0]^2], 
 Coupling[cHle, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[Ye, {Index[i1, Flavor], Index[i2, Flavor]}, 0] + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[Ye, {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$2, Flavor], Index[d$$1, Flavor]}, 0])/8 - 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[Ye, {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$2, Flavor], Index[d$$1, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {1, 1, 0}])/2 + 
   (hbar*Bar[Coupling[\[Lambda]\[Psi]\[Chi], {Index[i2, Flavor], 
        Index[d$$1, Flavor]}, 0]]*Coupling[Ye, {Index[i1, Flavor], 
       Index[d$$2, Flavor]}, 0]*Coupling[\[Lambda]\[Psi]\[Chi], 
      {Index[d$$2, Flavor], Index[d$$1, Flavor]}, 0]*
     LF[{Coupling[M\[Phi], {}, 0], Coupling[M\[Chi], {Index[d$$1, Flavor]}, 
        0]}, {2, 1, -1}])/4, Coupling[cH4, {}, 0] -> 
  -1/15*(hbar*Coupling[CH2, {}, 2]*Coupling[gY, {}, 0]^4)/
     Coupling[M\[Phi], {}, 0]^2 - Coupling[\[Lambda], {}, 0]/2 + 
   hbar*Coupling[\[Lambda]H\[Chi], {Index[d$$1, Flavor], 
       Index[d$$2, Flavor]}, 0]^2*
    LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], 
      Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {1, 1, 0}] + 
   2*hbar*Coupling[CH2, {}, 2]*Coupling[\[Lambda]H\[Chi], 
      {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]^2*
    LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], 
      Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {2, 1, 0}] - 
   2*hbar*Coupling[CH2, {}, 2]*Coupling[\[Lambda]H\[Chi], 
      {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]^2*
    LF[{Coupling[M\[Chi], {Index[d$$1, Flavor]}, 0], 
      Coupling[M\[Chi], {Index[d$$2, Flavor]}, 0]}, {3, 1, -1}], 
 Coupling[cB2, {}, 0] -> Coupling[gY, {}, 0] - 
   (2*hbar*Coupling[gY, {}, 0]^3*Log[\[Mu]bar2/Coupling[M\[Phi], {}, 0]^2])/3}
