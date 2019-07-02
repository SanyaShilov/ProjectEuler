#!/usr/bin/env wolframscript
(*::Package:: *)

Clear[calc];
calc[n_]:= calc[n] = Module[{r, nn},
	If[n < 2, Return[1]];
	If[BitAnd[n, 1] == 1, Return[calc[BitShiftRight[n]]]];
	r = 0;
	nn = n;
	While[BitAnd[nn, 1] == 0,
		nn = BitShiftRight[nn];
		r += 1;
	];
	nn = BitShiftRight[nn];
	Return[calc[nn] + r * calc[BitShiftLeft[nn]]];
	]
	
f[r_, i_Integer]:= First@Cases[r /. C[1] -> i, _Integer]
	
a = 3;
b = 2;
c = 1;
d = 1;
k = 7;
z = 3;
Clear[n];
r = Reduce[{Mod[3 + 2*n, 7] == 0, Mod[1 + 1*n, 3] == 0, (3 + 2*n}, n, Integers];
r
n2 = f[r, 0];
n2



