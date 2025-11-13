(* ::Package:: *)

(* ::Title:: *)
(*Flavored complex scalar Dark Matter coupled to the left-handed lepton doublet*)


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


DefineCoupling[\[Lambda]H\[Chi], 
	Indices       -> {Flavor,Flavor},
	SelfConjugate -> True,
	Symmetries    -> {SymmetricIndices[1,2]},
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
DefineField[\[Chi],Scalar,
	SelfConjugate -> False,
	Indices       -> {Flavor},
	Charges       -> {},
	Mass          -> {Heavy,M\[Chi],{Flavor}},
	NiceForm      -> {"\[Chi]","\!\(\*SubscriptBox[\(M\), \(\[Chi]\)]\)"}
];
(* define the mediator *)
DefineField[\[Phi],Fermion,
	SelfConjugate -> False,
	Indices       -> {SU2L[fund]},
	Charges       -> {U1Y[-1/2]},
	Mass          -> {Heavy,M\[Phi]},
	NiceForm      -> {"\[Phi]","\!\(\*SubscriptBox[\(M\), \(\[Phi]\)]\)"}
];


(* ::Text:: *)
(*Write Lagrangian*)


Module[{DMLag,p,r,i,a},
	DMLag = FreeLag[\[Chi],\[Phi]] + 
		\[Lambda]H\[Chi][p,r] Bar[H[i]]*H[i]*Bar[\[Chi][p]]*\[Chi][r] + 
		PlusHc[\[Lambda]\[Psi]\[Chi][p,r]*Bar[l[i,p]]**\[Phi][i]*\[Chi][r]];

	DMLag//RelabelIndices
]
