# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:23:29



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

RelFlc11 = Parameter(name = 'RelFlc11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFlc11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 1 ])

RelFlc12 = Parameter(name = 'RelFlc12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFlc12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 2 ])

RelFlc13 = Parameter(name = 'RelFlc13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFlc13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 3 ])

RelFlc21 = Parameter(name = 'RelFlc21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFlc21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 4 ])

RelFlc22 = Parameter(name = 'RelFlc22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFlc22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

RelFlc23 = Parameter(name = 'RelFlc23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFlc23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

RelFlc31 = Parameter(name = 'RelFlc31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFlc31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 7 ])

RelFlc32 = Parameter(name = 'RelFlc32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFlc32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 8 ])

RelFlc33 = Parameter(name = 'RelFlc33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFlc33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

ImlFlc11 = Parameter(name = 'ImlFlc11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFlc11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 10 ])

ImlFlc12 = Parameter(name = 'ImlFlc12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFlc12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

ImlFlc13 = Parameter(name = 'ImlFlc13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFlc13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

ImlFlc21 = Parameter(name = 'ImlFlc21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFlc21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

ImlFlc22 = Parameter(name = 'ImlFlc22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFlc22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

ImlFlc23 = Parameter(name = 'ImlFlc23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFlc23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ImlFlc31 = Parameter(name = 'ImlFlc31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFlc31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

ImlFlc32 = Parameter(name = 'ImlFlc32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFlc32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

ImlFlc33 = Parameter(name = 'ImlFlc33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFlc33}',
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

MYFle = Parameter(name = 'MYFle',
                  nature = 'external',
                  type = 'real',
                  value = 500,
                  texname = '\\text{MYFle}',
                  lhablock = 'MASS',
                  lhacode = [ 9000008 ])

MYFlv = Parameter(name = 'MYFlv',
                  nature = 'external',
                  type = 'real',
                  value = 500,
                  texname = '\\text{MYFlv}',
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

WYFle = Parameter(name = 'WYFle',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WYFle}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000008 ])

WYFlv = Parameter(name = 'WYFlv',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WYFlv}',
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

RelFlc1x1 = Parameter(name = 'RelFlc1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFlc11',
                      texname = '\\text{RelFlc1x1}')

RelFlc1x2 = Parameter(name = 'RelFlc1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFlc12',
                      texname = '\\text{RelFlc1x2}')

RelFlc1x3 = Parameter(name = 'RelFlc1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFlc13',
                      texname = '\\text{RelFlc1x3}')

RelFlc2x1 = Parameter(name = 'RelFlc2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFlc21',
                      texname = '\\text{RelFlc2x1}')

RelFlc2x2 = Parameter(name = 'RelFlc2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFlc22',
                      texname = '\\text{RelFlc2x2}')

RelFlc2x3 = Parameter(name = 'RelFlc2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFlc23',
                      texname = '\\text{RelFlc2x3}')

RelFlc3x1 = Parameter(name = 'RelFlc3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFlc31',
                      texname = '\\text{RelFlc3x1}')

RelFlc3x2 = Parameter(name = 'RelFlc3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFlc32',
                      texname = '\\text{RelFlc3x2}')

RelFlc3x3 = Parameter(name = 'RelFlc3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFlc33',
                      texname = '\\text{RelFlc3x3}')

ImlFlc1x1 = Parameter(name = 'ImlFlc1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFlc11',
                      texname = '\\text{ImlFlc1x1}')

ImlFlc1x2 = Parameter(name = 'ImlFlc1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFlc12',
                      texname = '\\text{ImlFlc1x2}')

ImlFlc1x3 = Parameter(name = 'ImlFlc1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFlc13',
                      texname = '\\text{ImlFlc1x3}')

ImlFlc2x1 = Parameter(name = 'ImlFlc2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFlc21',
                      texname = '\\text{ImlFlc2x1}')

ImlFlc2x2 = Parameter(name = 'ImlFlc2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFlc22',
                      texname = '\\text{ImlFlc2x2}')

ImlFlc2x3 = Parameter(name = 'ImlFlc2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFlc23',
                      texname = '\\text{ImlFlc2x3}')

ImlFlc3x1 = Parameter(name = 'ImlFlc3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFlc31',
                      texname = '\\text{ImlFlc3x1}')

ImlFlc3x2 = Parameter(name = 'ImlFlc3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFlc32',
                      texname = '\\text{ImlFlc3x2}')

ImlFlc3x3 = Parameter(name = 'ImlFlc3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFlc33',
                      texname = '\\text{ImlFlc3x3}')

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

