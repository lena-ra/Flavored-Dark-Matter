(* ::Package:: *)

(* ::Title:: *)
(*Flavored real scalar Dark Matter coupled to the right-handed charged lepton singlet*)


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
	SelfConjugate -> True,
	Indices       -> {Flavor},
	Charges       -> {},
	Mass          -> {Heavy,M\[Chi],{Flavor}},
	NiceForm      -> {"\[Chi]","\!\(\*SubscriptBox[\(M\), \(\[Chi]\)]\)"}
];

(* define the mediator *)
DefineField[\[Phi],Fermion,
	SelfConjugate -> False,
	Indices       -> {},
	Charges       -> {U1Y[-1]},
	Mass          -> {Heavy,M\[Phi]},
	NiceForm      -> {"\[Phi]","\!\(\*SubscriptBox[\(M\), \(\[Phi]\)]\)"}
];


(* ::Text:: *)
(*Write Lagrangian*)


Module[{DMLag,p,r,i,a},
	DMLag = FreeLag[\[Chi],\[Phi]] + 
		\[Lambda]H\[Chi][p,r] Bar[H[i]]*H[i]*\[Chi][p]*\[Chi][r] + 
		PlusHc[\[Lambda]\[Psi]\[Chi][p,r]*Bar[e[p]]**\[Phi][]*\[Chi][r]];

	DMLag//RelabelIndices
]
