#!/usr/bin/env wolframscript
(*::Package:: *)

S = 0; p = 5; q = 7;
While[p < 10^6,
	S += ChineseRemainder[{0, p}, {q, 10^(Floor[Log[10, p]] + 1)}];
	p = q;
	q = NextPrime[q];
]
