#!/usr/bin/env wolframscript
(*::Package:: *)

n = 1; S = 0;
While[n <= 50000000,
	If[PrimeQ[2*n^2-1], S += 1];
	n += 1;
]
S
