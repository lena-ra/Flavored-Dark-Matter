# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:22:14



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

RelFec11 = Parameter(name = 'RelFec11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFec11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 1 ])

RelFec12 = Parameter(name = 'RelFec12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFec12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 2 ])

RelFec13 = Parameter(name = 'RelFec13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFec13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 3 ])

RelFec21 = Parameter(name = 'RelFec21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFec21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 4 ])

RelFec22 = Parameter(name = 'RelFec22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFec22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

RelFec23 = Parameter(name = 'RelFec23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFec23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

RelFec31 = Parameter(name = 'RelFec31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFec31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 7 ])

RelFec32 = Parameter(name = 'RelFec32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFec32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 8 ])

RelFec33 = Parameter(name = 'RelFec33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelFec33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

ImlFec11 = Parameter(name = 'ImlFec11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFec11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 10 ])

ImlFec12 = Parameter(name = 'ImlFec12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFec12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

ImlFec13 = Parameter(name = 'ImlFec13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFec13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

ImlFec21 = Parameter(name = 'ImlFec21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFec21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

ImlFec22 = Parameter(name = 'ImlFec22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFec22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

ImlFec23 = Parameter(name = 'ImlFec23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFec23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ImlFec31 = Parameter(name = 'ImlFec31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFec31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

ImlFec32 = Parameter(name = 'ImlFec32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFec32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

ImlFec33 = Parameter(name = 'ImlFec33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlFec33}',
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

MYFe = Parameter(name = 'MYFe',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{MYFe}',
                 lhablock = 'MASS',
                 lhacode = [ 9000008 ])

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

WYFe = Parameter(name = 'WYFe',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WYFe}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000008 ])

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

RelFec1x1 = Parameter(name = 'RelFec1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFec11',
                      texname = '\\text{RelFec1x1}')

RelFec1x2 = Parameter(name = 'RelFec1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFec12',
                      texname = '\\text{RelFec1x2}')

RelFec1x3 = Parameter(name = 'RelFec1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFec13',
                      texname = '\\text{RelFec1x3}')

RelFec2x1 = Parameter(name = 'RelFec2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFec21',
                      texname = '\\text{RelFec2x1}')

RelFec2x2 = Parameter(name = 'RelFec2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFec22',
                      texname = '\\text{RelFec2x2}')

RelFec2x3 = Parameter(name = 'RelFec2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFec23',
                      texname = '\\text{RelFec2x3}')

RelFec3x1 = Parameter(name = 'RelFec3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFec31',
                      texname = '\\text{RelFec3x1}')

RelFec3x2 = Parameter(name = 'RelFec3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFec32',
                      texname = '\\text{RelFec3x2}')

RelFec3x3 = Parameter(name = 'RelFec3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelFec33',
                      texname = '\\text{RelFec3x3}')

ImlFec1x1 = Parameter(name = 'ImlFec1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFec11',
                      texname = '\\text{ImlFec1x1}')

ImlFec1x2 = Parameter(name = 'ImlFec1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFec12',
                      texname = '\\text{ImlFec1x2}')

ImlFec1x3 = Parameter(name = 'ImlFec1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFec13',
                      texname = '\\text{ImlFec1x3}')

ImlFec2x1 = Parameter(name = 'ImlFec2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFec21',
                      texname = '\\text{ImlFec2x1}')

ImlFec2x2 = Parameter(name = 'ImlFec2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFec22',
                      texname = '\\text{ImlFec2x2}')

ImlFec2x3 = Parameter(name = 'ImlFec2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFec23',
                      texname = '\\text{ImlFec2x3}')

ImlFec3x1 = Parameter(name = 'ImlFec3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFec31',
                      texname = '\\text{ImlFec3x1}')

ImlFec3x2 = Parameter(name = 'ImlFec3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFec32',
                      texname = '\\text{ImlFec3x2}')

ImlFec3x3 = Parameter(name = 'ImlFec3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlFec33',
                      texname = '\\text{ImlFec3x3}')

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

