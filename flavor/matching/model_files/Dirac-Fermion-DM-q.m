(* ::Package:: *)

(* ::Title:: *)
(*Flavored Dirac fermion Dark Matter coupled to the left-handed quark doublet*)


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
	Indices       -> {SU3c[fund],SU2L[fund]},
	Charges       -> {U1Y[1/6]},
	Mass          -> {Heavy,M\[Phi]},
	NiceForm      -> {"\[Phi]","\!\(\*SubscriptBox[\(M\), \(\[Phi]\)]\)"}
];


(* ::Text:: *)
(*Write Lagrangian*)


Module[{DMLag,p,r,i,j,a},
	DMLag = FreeLag[\[Chi],\[Phi]] + 
		\[Lambda]H\[Phi]1[] Bar[H[i]]*H[i]*Bar[\[Phi][a,j]]*\[Phi][a,j] + 
		\[Lambda]H\[Phi]2[] Bar[H[i]]*H[j]*Bar[\[Phi][a,j]]*\[Phi][a,i] + 
		PlusHc[\[Lambda]\[Psi]\[Chi][p,r]*Bar[q[a,i,p]]**\[Chi][r]*\[Phi][a,i]];

	DMLag//RelabelIndices
]
