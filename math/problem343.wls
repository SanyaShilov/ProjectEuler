#!/usr/bin/env wolframscript
(*::Package:: *)

n = 1;
S = 0;
While[n <= 2 * 10^6,
	num = n*n - n + 1;
	fm = FactorInteger[num];
	m = Max[fm[[{-1}, 1]]];
	fmn = FactorInteger[n + 1];
	mn = Max[fmn[[{-1}, 1]]];
	S += Max[m, mn] - 1;
	n += 1;
];
S

