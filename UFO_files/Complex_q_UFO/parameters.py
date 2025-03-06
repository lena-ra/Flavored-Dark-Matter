# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:25:15



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

RelFqc11 = Parameter(name = 'RelFqc11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqc11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 1 ])

RelFqc12 = Parameter(name = 'RelFqc12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqc12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 2 ])

RelFqc13 = Parameter(name = 'RelFqc13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqc13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 3 ])

RelFqc21 = Parameter(name = 'RelFqc21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqc21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 4 ])

RelFqc22 = Parameter(name = 'RelFqc22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqc22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

RelFqc23 = Parameter(name = 'RelFqc23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqc23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

RelFqc31 = Parameter(name = 'RelFqc31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqc31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 7 ])

RelFqc32 = Parameter(name = 'RelFqc32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqc32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 8 ])

RelFqc33 = Parameter(name = 'RelFqc33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqc33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

ImlFqc11 = Parameter(name = 'ImlFqc11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqc11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 10 ])

ImlFqc12 = Parameter(name = 'ImlFqc12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqc12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

ImlFqc13 = Parameter(name = 'ImlFqc13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqc13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

ImlFqc21 = Parameter(name = 'ImlFqc21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqc21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

ImlFqc22 = Parameter(name = 'ImlFqc22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqc22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

ImlFqc23 = Parameter(name = 'ImlFqc23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqc23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ImlFqc31 = Parameter(name = 'ImlFqc31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqc31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

ImlFqc32 = Parameter(name = 'ImlFqc32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqc32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

ImlFqc33 = Parameter(name = 'ImlFqc33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqc33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 18 ])

RelHXc11 = Parameter(name = 'RelHXc11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelHXc11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 19 ])

RelHXc12 = Parameter(name = 'RelHXc12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelHXc12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 20 ])

RelHXc13 = Parameter(name = 'RelHXc13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelHXc13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 21 ])

RelHXc22 = Parameter(name = 'RelHXc22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelHXc22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 22 ])

RelHXc23 = Parameter(name = 'RelHXc23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelHXc23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 23 ])

RelHXc33 = Parameter(name = 'RelHXc33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelHXc33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 24 ])

ImlHXc12 = Parameter(name = 'ImlHXc12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlHXc12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 25 ])

ImlHXc13 = Parameter(name = 'ImlHXc13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlHXc13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 26 ])

ImlHXc23 = Parameter(name = 'ImlHXc23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlHXc23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 27 ])

lam2Xc = Parameter(name = 'lam2Xc',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lam2Xc}',
                   lhablock = 'FRBlock',
                   lhacode = [ 28 ])

mXc1 = Parameter(name = 'mXc1',
                 nature = 'external',
                 type = 'real',
                 value = 300,
                 texname = '\\text{mXc1}',
                 lhablock = 'FRBlock',
                 lhacode = [ 29 ])

mXc2 = Parameter(name = 'mXc2',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{mXc2}',
                 lhablock = 'FRBlock',
                 lhacode = [ 30 ])

mXc3 = Parameter(name = 'mXc3',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{mXc3}',
                 lhablock = 'FRBlock',
                 lhacode = [ 31 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MYFqu = Parameter(name = 'MYFqu',
                  nature = 'external',
                  type = 'real',
                  value = 500,
                  texname = '\\text{MYFqu}',
                  lhablock = 'MASS',
                  lhacode = [ 9000008 ])

MYFqd = Parameter(name = 'MYFqd',
                  nature = 'external',
                  type = 'real',
                  value = 500,
                  texname = '\\text{MYFqd}',
                  lhablock = 'MASS',
                  lhacode = [ 9000009 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

wXc1 = Parameter(name = 'wXc1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXc1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000005 ])

wXc2 = Parameter(name = 'wXc2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXc2}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000006 ])

WYFqu = Parameter(name = 'WYFqu',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WYFqu}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000008 ])

WYFqd = Parameter(name = 'WYFqd',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WYFqd}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000009 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

RelFqc1x1 = Parameter(name = 'RelFqc1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqc11',
                      texname = '\\text{RelFqc1x1}')

RelFqc1x2 = Parameter(name = 'RelFqc1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqc12',
                      texname = '\\text{RelFqc1x2}')

RelFqc1x3 = Parameter(name = 'RelFqc1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqc13',
                      texname = '\\text{RelFqc1x3}')

RelFqc2x1 = Parameter(name = 'RelFqc2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqc21',
                      texname = '\\text{RelFqc2x1}')

RelFqc2x2 = Parameter(name = 'RelFqc2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqc22',
                      texname = '\\text{RelFqc2x2}')

RelFqc2x3 = Parameter(name = 'RelFqc2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqc23',
                      texname = '\\text{RelFqc2x3}')

RelFqc3x1 = Parameter(name = 'RelFqc3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqc31',
                      texname = '\\text{RelFqc3x1}')

RelFqc3x2 = Parameter(name = 'RelFqc3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqc32',
                      texname = '\\text{RelFqc3x2}')

RelFqc3x3 = Parameter(name = 'RelFqc3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqc33',
                      texname = '\\text{RelFqc3x3}')

ImlFqc1x1 = Parameter(name = 'ImlFqc1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqc11',
                      texname = '\\text{ImlFqc1x1}')

ImlFqc1x2 = Parameter(name = 'ImlFqc1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqc12',
                      texname = '\\text{ImlFqc1x2}')

ImlFqc1x3 = Parameter(name = 'ImlFqc1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqc13',
                      texname = '\\text{ImlFqc1x3}')

ImlFqc2x1 = Parameter(name = 'ImlFqc2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqc21',
                      texname = '\\text{ImlFqc2x1}')

ImlFqc2x2 = Parameter(name = 'ImlFqc2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqc22',
                      texname = '\\text{ImlFqc2x2}')

ImlFqc2x3 = Parameter(name = 'ImlFqc2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqc23',
                      texname = '\\text{ImlFqc2x3}')

ImlFqc3x1 = Parameter(name = 'ImlFqc3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqc31',
                      texname = '\\text{ImlFqc3x1}')

ImlFqc3x2 = Parameter(name = 'ImlFqc3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqc32',
                      texname = '\\text{ImlFqc3x2}')

ImlFqc3x3 = Parameter(name = 'ImlFqc3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqc33',
                      texname = '\\text{ImlFqc3x3}')

RelHXc1x1 = Parameter(name = 'RelHXc1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXc11',
                      texname = '\\text{RelHXc1x1}')

RelHXc1x2 = Parameter(name = 'RelHXc1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXc12',
                      texname = '\\text{RelHXc1x2}')

RelHXc1x3 = Parameter(name = 'RelHXc1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXc13',
                      texname = '\\text{RelHXc1x3}')

RelHXc2x1 = Parameter(name = 'RelHXc2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXc12',
                      texname = '\\text{RelHXc2x1}')

RelHXc2x2 = Parameter(name = 'RelHXc2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXc22',
                      texname = '\\text{RelHXc2x2}')

RelHXc2x3 = Parameter(name = 'RelHXc2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXc23',
                      texname = '\\text{RelHXc2x3}')

RelHXc3x1 = Parameter(name = 'RelHXc3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXc13',
                      texname = '\\text{RelHXc3x1}')

RelHXc3x2 = Parameter(name = 'RelHXc3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXc23',
                      texname = '\\text{RelHXc3x2}')

RelHXc3x3 = Parameter(name = 'RelHXc3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXc33',
                      texname = '\\text{RelHXc3x3}')

ImlHXc1x1 = Parameter(name = 'ImlHXc1x1',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{ImlHXc1x1}')

ImlHXc1x2 = Parameter(name = 'ImlHXc1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlHXc12',
                      texname = '\\text{ImlHXc1x2}')

ImlHXc1x3 = Parameter(name = 'ImlHXc1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlHXc13',
                      texname = '\\text{ImlHXc1x3}')

ImlHXc2x1 = Parameter(name = 'ImlHXc2x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-ImlHXc12',
                      texname = '\\text{ImlHXc2x1}')

ImlHXc2x2 = Parameter(name = 'ImlHXc2x2',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{ImlHXc2x2}')

ImlHXc2x3 = Parameter(name = 'ImlHXc2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlHXc23',
                      texname = '\\text{ImlHXc2x3}')

ImlHXc3x1 = Parameter(name = 'ImlHXc3x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-ImlHXc13',
                      texname = '\\text{ImlHXc3x1}')

ImlHXc3x2 = Parameter(name = 'ImlHXc3x2',
                      nature = 'internal',
                      type = 'real',
                      value = '-ImlHXc23',
                      texname = '\\text{ImlHXc3x2}')

ImlHXc3x3 = Parameter(name = 'ImlHXc3x3',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{ImlHXc3x3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

MXc1 = Parameter(name = 'MXc1',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(mXc1**2 + (lamHXc1*vev**2)/2.)',
                 texname = '\\text{MXc1}')

MXc2 = Parameter(name = 'MXc2',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(mXc2**2 + (lamHXc2*vev**2)/2.)',
                 texname = '\\text{MXc2}')

MXc3 = Parameter(name = 'MXc3',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(mXc3**2 + (lamHXc3*vev**2)/2.)',
                 texname = '\\text{MXc3}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

