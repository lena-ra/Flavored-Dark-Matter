# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:48:34



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

RelFqs11 = Parameter(name = 'RelFqs11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqs11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 1 ])

RelFqs12 = Parameter(name = 'RelFqs12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqs12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 2 ])

RelFqs13 = Parameter(name = 'RelFqs13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqs13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 3 ])

RelFqs21 = Parameter(name = 'RelFqs21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqs21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 4 ])

RelFqs22 = Parameter(name = 'RelFqs22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqs22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

RelFqs23 = Parameter(name = 'RelFqs23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqs23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

RelFqs31 = Parameter(name = 'RelFqs31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqs31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 7 ])

RelFqs32 = Parameter(name = 'RelFqs32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqs32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 8 ])

RelFqs33 = Parameter(name = 'RelFqs33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFqs33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

ImlFqs11 = Parameter(name = 'ImlFqs11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqs11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 10 ])

ImlFqs12 = Parameter(name = 'ImlFqs12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqs12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

ImlFqs13 = Parameter(name = 'ImlFqs13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqs13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

ImlFqs21 = Parameter(name = 'ImlFqs21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqs21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

ImlFqs22 = Parameter(name = 'ImlFqs22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqs22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

ImlFqs23 = Parameter(name = 'ImlFqs23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqs23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ImlFqs31 = Parameter(name = 'ImlFqs31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqs31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

ImlFqs32 = Parameter(name = 'ImlFqs32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqs32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

ImlFqs33 = Parameter(name = 'ImlFqs33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFqs33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 18 ])

RelHXs11 = Parameter(name = 'RelHXs11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelHXs11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 19 ])

RelHXs12 = Parameter(name = 'RelHXs12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelHXs12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 20 ])

RelHXs13 = Parameter(name = 'RelHXs13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelHXs13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 21 ])

RelHXs22 = Parameter(name = 'RelHXs22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelHXs22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 22 ])

RelHXs23 = Parameter(name = 'RelHXs23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelHXs23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 23 ])

RelHXs33 = Parameter(name = 'RelHXs33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelHXs33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 24 ])

ImlHXs12 = Parameter(name = 'ImlHXs12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlHXs12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 25 ])

ImlHXs13 = Parameter(name = 'ImlHXs13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlHXs13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 26 ])

ImlHXs23 = Parameter(name = 'ImlHXs23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlHXs23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 27 ])

lam2Xs = Parameter(name = 'lam2Xs',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lam2Xs}',
                   lhablock = 'FRBlock',
                   lhacode = [ 28 ])

mXs1 = Parameter(name = 'mXs1',
                 nature = 'external',
                 type = 'real',
                 value = 300,
                 texname = '\\text{mXs1}',
                 lhablock = 'FRBlock',
                 lhacode = [ 29 ])

mXs2 = Parameter(name = 'mXs2',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{mXs2}',
                 lhablock = 'FRBlock',
                 lhacode = [ 30 ])

mXs3 = Parameter(name = 'mXs3',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{mXs3}',
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

wXs1 = Parameter(name = 'wXs1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXs1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000005 ])

wXs2 = Parameter(name = 'wXs2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXs2}',
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

RelFqs1x1 = Parameter(name = 'RelFqs1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqs11',
                      texname = '\\text{RelFqs1x1}')

RelFqs1x2 = Parameter(name = 'RelFqs1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqs12',
                      texname = '\\text{RelFqs1x2}')

RelFqs1x3 = Parameter(name = 'RelFqs1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqs13',
                      texname = '\\text{RelFqs1x3}')

RelFqs2x1 = Parameter(name = 'RelFqs2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqs21',
                      texname = '\\text{RelFqs2x1}')

RelFqs2x2 = Parameter(name = 'RelFqs2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqs22',
                      texname = '\\text{RelFqs2x2}')

RelFqs2x3 = Parameter(name = 'RelFqs2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqs23',
                      texname = '\\text{RelFqs2x3}')

RelFqs3x1 = Parameter(name = 'RelFqs3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqs31',
                      texname = '\\text{RelFqs3x1}')

RelFqs3x2 = Parameter(name = 'RelFqs3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqs32',
                      texname = '\\text{RelFqs3x2}')

RelFqs3x3 = Parameter(name = 'RelFqs3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFqs33',
                      texname = '\\text{RelFqs3x3}')

ImlFqs1x1 = Parameter(name = 'ImlFqs1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqs11',
                      texname = '\\text{ImlFqs1x1}')

ImlFqs1x2 = Parameter(name = 'ImlFqs1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqs12',
                      texname = '\\text{ImlFqs1x2}')

ImlFqs1x3 = Parameter(name = 'ImlFqs1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqs13',
                      texname = '\\text{ImlFqs1x3}')

ImlFqs2x1 = Parameter(name = 'ImlFqs2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqs21',
                      texname = '\\text{ImlFqs2x1}')

ImlFqs2x2 = Parameter(name = 'ImlFqs2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqs22',
                      texname = '\\text{ImlFqs2x2}')

ImlFqs2x3 = Parameter(name = 'ImlFqs2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqs23',
                      texname = '\\text{ImlFqs2x3}')

ImlFqs3x1 = Parameter(name = 'ImlFqs3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqs31',
                      texname = '\\text{ImlFqs3x1}')

ImlFqs3x2 = Parameter(name = 'ImlFqs3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqs32',
                      texname = '\\text{ImlFqs3x2}')

ImlFqs3x3 = Parameter(name = 'ImlFqs3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFqs33',
                      texname = '\\text{ImlFqs3x3}')

RelHXs1x1 = Parameter(name = 'RelHXs1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXs11',
                      texname = '\\text{RelHXs1x1}')

RelHXs1x2 = Parameter(name = 'RelHXs1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXs12',
                      texname = '\\text{RelHXs1x2}')

RelHXs1x3 = Parameter(name = 'RelHXs1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXs13',
                      texname = '\\text{RelHXs1x3}')

RelHXs2x1 = Parameter(name = 'RelHXs2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXs12',
                      texname = '\\text{RelHXs2x1}')

RelHXs2x2 = Parameter(name = 'RelHXs2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXs22',
                      texname = '\\text{RelHXs2x2}')

RelHXs2x3 = Parameter(name = 'RelHXs2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXs23',
                      texname = '\\text{RelHXs2x3}')

RelHXs3x1 = Parameter(name = 'RelHXs3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXs13',
                      texname = '\\text{RelHXs3x1}')

RelHXs3x2 = Parameter(name = 'RelHXs3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXs23',
                      texname = '\\text{RelHXs3x2}')

RelHXs3x3 = Parameter(name = 'RelHXs3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelHXs33',
                      texname = '\\text{RelHXs3x3}')

ImlHXs1x1 = Parameter(name = 'ImlHXs1x1',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{ImlHXs1x1}')

ImlHXs1x2 = Parameter(name = 'ImlHXs1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlHXs12',
                      texname = '\\text{ImlHXs1x2}')

ImlHXs1x3 = Parameter(name = 'ImlHXs1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlHXs13',
                      texname = '\\text{ImlHXs1x3}')

ImlHXs2x1 = Parameter(name = 'ImlHXs2x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-ImlHXs12',
                      texname = '\\text{ImlHXs2x1}')

ImlHXs2x2 = Parameter(name = 'ImlHXs2x2',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{ImlHXs2x2}')

ImlHXs2x3 = Parameter(name = 'ImlHXs2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlHXs23',
                      texname = '\\text{ImlHXs2x3}')

ImlHXs3x1 = Parameter(name = 'ImlHXs3x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-ImlHXs13',
                      texname = '\\text{ImlHXs3x1}')

ImlHXs3x2 = Parameter(name = 'ImlHXs3x2',
                      nature = 'internal',
                      type = 'real',
                      value = '-ImlHXs23',
                      texname = '\\text{ImlHXs3x2}')

ImlHXs3x3 = Parameter(name = 'ImlHXs3x3',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{ImlHXs3x3}')

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

MXs1 = Parameter(name = 'MXs1',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(mXs1**2 + (lamHXs1*vev**2)/2.)',
                 texname = '\\text{MXs1}')

MXs2 = Parameter(name = 'MXs2',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(mXs2**2 + (lamHXs2*vev**2)/2.)',
                 texname = '\\text{MXs2}')

MXs3 = Parameter(name = 'MXs3',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(mXs3**2 + (lamHXs3*vev**2)/2.)',
                 texname = '\\text{MXs3}')

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

