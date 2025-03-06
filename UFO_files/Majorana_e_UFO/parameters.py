# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:39:24



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

RelSem11 = Parameter(name = 'RelSem11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSem11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 1 ])

RelSem12 = Parameter(name = 'RelSem12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSem12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 2 ])

RelSem13 = Parameter(name = 'RelSem13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSem13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 3 ])

RelSem21 = Parameter(name = 'RelSem21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSem21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 4 ])

RelSem22 = Parameter(name = 'RelSem22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSem22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

RelSem23 = Parameter(name = 'RelSem23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSem23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

RelSem31 = Parameter(name = 'RelSem31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSem31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 7 ])

RelSem32 = Parameter(name = 'RelSem32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSem32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 8 ])

RelSem33 = Parameter(name = 'RelSem33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSem33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

ImlSem11 = Parameter(name = 'ImlSem11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSem11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 10 ])

ImlSem12 = Parameter(name = 'ImlSem12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSem12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

ImlSem13 = Parameter(name = 'ImlSem13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSem13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

ImlSem21 = Parameter(name = 'ImlSem21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSem21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

ImlSem22 = Parameter(name = 'ImlSem22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSem22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

ImlSem23 = Parameter(name = 'ImlSem23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSem23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ImlSem31 = Parameter(name = 'ImlSem31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSem31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

ImlSem32 = Parameter(name = 'ImlSem32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSem32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

ImlSem33 = Parameter(name = 'ImlSem33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSem33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 18 ])

lamHSe = Parameter(name = 'lamHSe',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lamHSe}',
                   lhablock = 'FRBlock',
                   lhacode = [ 19 ])

lam2Se = Parameter(name = 'lam2Se',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lam2Se}',
                   lhablock = 'FRBlock',
                   lhacode = [ 20 ])

mYSe = Parameter(name = 'mYSe',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{mYSe}',
                 lhablock = 'FRBlock',
                 lhacode = [ 21 ])

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

MXm1 = Parameter(name = 'MXm1',
                 nature = 'external',
                 type = 'real',
                 value = 300,
                 texname = '\\text{MXm1}',
                 lhablock = 'MASS',
                 lhacode = [ 9000005 ])

MXm2 = Parameter(name = 'MXm2',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{MXm2}',
                 lhablock = 'MASS',
                 lhacode = [ 9000006 ])

MXm3 = Parameter(name = 'MXm3',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{MXm3}',
                 lhablock = 'MASS',
                 lhacode = [ 9000007 ])

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

wXm1 = Parameter(name = 'wXm1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXm1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000005 ])

wXm2 = Parameter(name = 'wXm2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXm2}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000006 ])

WYSe = Parameter(name = 'WYSe',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WYSe}',
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

RelSem1x1 = Parameter(name = 'RelSem1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSem11',
                      texname = '\\text{RelSem1x1}')

RelSem1x2 = Parameter(name = 'RelSem1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSem12',
                      texname = '\\text{RelSem1x2}')

RelSem1x3 = Parameter(name = 'RelSem1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSem13',
                      texname = '\\text{RelSem1x3}')

RelSem2x1 = Parameter(name = 'RelSem2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSem21',
                      texname = '\\text{RelSem2x1}')

RelSem2x2 = Parameter(name = 'RelSem2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSem22',
                      texname = '\\text{RelSem2x2}')

RelSem2x3 = Parameter(name = 'RelSem2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSem23',
                      texname = '\\text{RelSem2x3}')

RelSem3x1 = Parameter(name = 'RelSem3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSem31',
                      texname = '\\text{RelSem3x1}')

RelSem3x2 = Parameter(name = 'RelSem3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSem32',
                      texname = '\\text{RelSem3x2}')

RelSem3x3 = Parameter(name = 'RelSem3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSem33',
                      texname = '\\text{RelSem3x3}')

ImlSem1x1 = Parameter(name = 'ImlSem1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSem11',
                      texname = '\\text{ImlSem1x1}')

ImlSem1x2 = Parameter(name = 'ImlSem1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSem12',
                      texname = '\\text{ImlSem1x2}')

ImlSem1x3 = Parameter(name = 'ImlSem1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSem13',
                      texname = '\\text{ImlSem1x3}')

ImlSem2x1 = Parameter(name = 'ImlSem2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSem21',
                      texname = '\\text{ImlSem2x1}')

ImlSem2x2 = Parameter(name = 'ImlSem2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSem22',
                      texname = '\\text{ImlSem2x2}')

ImlSem2x3 = Parameter(name = 'ImlSem2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSem23',
                      texname = '\\text{ImlSem2x3}')

ImlSem3x1 = Parameter(name = 'ImlSem3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSem31',
                      texname = '\\text{ImlSem3x1}')

ImlSem3x2 = Parameter(name = 'ImlSem3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSem32',
                      texname = '\\text{ImlSem3x2}')

ImlSem3x3 = Parameter(name = 'ImlSem3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSem33',
                      texname = '\\text{ImlSem3x3}')

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

MYSe = Parameter(name = 'MYSe',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(mYSe**2 + (lamHSe*vev**2)/2.)',
                 texname = '\\text{MYSe}')

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

