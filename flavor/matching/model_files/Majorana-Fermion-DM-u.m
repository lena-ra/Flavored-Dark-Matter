(* ::Package:: *)

(* ::Title:: *)
(*Flavored Majorana fermion Dark Matter coupled to the right-handed up-type quark singlet*)


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
DefineCoupling[\[Lambda]\[Psi]\[Chi],
	Indices       -> {Flavor,Flavor},
	SelfConjugate -> False,
	NiceForm      -> "\!\(\*SubscriptBox[\(\[Lambda]\), \(\[Psi]\[Chi]\)]\)"
];


(* ::Text:: *)
(*Define fields*)


(* define DM field *)
DefineField[\[Chi],Fermion,
	SelfConjugate -> True,
	Indices       -> {Flavor},
	Charges       -> {},
	Mass          -> {Heavy,M\[Chi],{Flavor}},
	NiceForm      -> {"\[Chi]","\!\(\*SubscriptBox[\(M\), \(\[Chi]\)]\)"}
];
(* define the mediator *)
DefineField[\[Phi],Scalar,
	SelfConjugate -> False,
	Indices       -> {SU3c[fund]},
	Charges       -> {U1Y[2/3]},
	Mass          -> {Heavy,M\[Phi]},
	NiceForm      -> {"\[Phi]","\!\(\*SubscriptBox[\(M\), \(\[Phi]\)]\)"}
];


(* ::Text:: *)
(*Write Lagrangian*)


Module[{DMLag,p,r,i,a},
	DMLag = FreeLag[\[Chi],\[Phi]] + 
		\[Lambda]H\[Phi]1[] Bar[H[i]]*H[i]*Bar[\[Phi][a]]*\[Phi][a] + 
		PlusHc[\[Lambda]\[Psi]\[Chi][p,r]*Bar[u[a,p]]**\[Chi][r]*\[Phi][a]];

	DMLag//RelabelIndices
]
