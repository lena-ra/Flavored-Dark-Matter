(* ::Package:: *)

(* ::Title:: *)
(*Flavored Dirac fermion Dark Matter coupled to the left-handed lepton doublet*)


(* ::Subtitle:: *)
(*Model file created by:*)
(*Felix Wilsch (felix.wilsch@physik.rwth-aachen.de)*)
(*on: August 21, 2025*)


(* ::Subtitle:: *)
(*Please cite: *)
(*Belfatto, Blanke, Heisig, Kr\[ADoubleDot]mer, Rathmann, and Wilsch [arXiv:2510.XXXXX]*)


ParentModel["SM"]


(* ::Text:: *)
(*Define couplings*)


DefineCoupling[\[Lambda]H\[Phi]1, 
	SelfConjugate -> True,
	NiceForm      -> "\!\(\*SubscriptBox[\(\[Lambda]\), \(H\[Chi]\)]\)"
];
DefineCoupling[\[Lambda]H\[Phi]2, 
	SelfConjugate -> True,
	NiceForm      -> "\!\(\*SubscriptBox[\(\[Lambda]\), \(H\[Chi]\)]\)"
];
DefineCoupling[\[Lambda]H\[Phi]3, 
	SelfConjugate -> False,
	NiceForm      -> "\!\(\*SubscriptBox[\(\[Lambda]\), \(H\[Chi]\)]\)"
];
DefineCoupling[\[Lambda]\[Psi]\[Chi],
	Indices       -> {Flavor,Flavor},
	SelfConjugate -> False,
	NiceForm      -> "\!\(\*SubscriptBox[\(\[Lambda]\), \(\[Psi]\[Chi]\)]\)"
];


(* ::Text:: *)
(*Define fields*)


(* define DM field *)
DefineField[\[Chi],Fermion,
	SelfConjugate -> False,
	Indices       -> {Flavor},
	Charges       -> {},
	Mass          -> {Heavy,M\[Chi],{Flavor}},
	NiceForm      -> {"\[Chi]","\!\(\*SubscriptBox[\(M\), \(\[Chi]\)]\)"}
];
(* define the mediator *)
DefineField[\[Phi],Scalar,
	SelfConjugate -> False,
	Indices       -> {SU2L[fund]},
	Charges       -> {U1Y[-1/2]},
	Mass          -> {Heavy,M\[Phi]},
	NiceForm      -> {"\[Phi]","\!\(\*SubscriptBox[\(M\), \(\[Phi]\)]\)"}
];


(* ::Text:: *)
(*Write Lagrangian*)


Module[{DMLag,p,r,i,j,n,m,a},
	DMLag = FreeLag[\[Chi],\[Phi]] + 
		\[Lambda]H\[Phi]1[] Bar[H[i]]*H[i]*Bar[\[Phi][j]]*\[Phi][j] + 
		\[Lambda]H\[Phi]2[] Bar[H[i]]*H[j]*Bar[\[Phi][j]]*\[Phi][i] + 
		PlusHc[1/2*\[Lambda]H\[Phi]3[] H[i]*H[n]*\[Phi][j]*\[Phi][m]*Bar@CG[eps[SU2L],{i,j}]*Bar@CG[eps[SU2L],{n,m}]] +
		PlusHc[\[Lambda]\[Psi]\[Chi][p,r]*Bar[l[i,p]]**\[Chi][r]*\[Phi][i]];

	DMLag//RelabelIndices
]
