# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:44:03



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

RelSum11 = Parameter(name = 'RelSum11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSum11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 1 ])

RelSum12 = Parameter(name = 'RelSum12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSum12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 2 ])

RelSum13 = Parameter(name = 'RelSum13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSum13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 3 ])

RelSum21 = Parameter(name = 'RelSum21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSum21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 4 ])

RelSum22 = Parameter(name = 'RelSum22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSum22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

RelSum23 = Parameter(name = 'RelSum23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSum23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

RelSum31 = Parameter(name = 'RelSum31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSum31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 7 ])

RelSum32 = Parameter(name = 'RelSum32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSum32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 8 ])

RelSum33 = Parameter(name = 'RelSum33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSum33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

ImlSum11 = Parameter(name = 'ImlSum11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSum11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 10 ])

ImlSum12 = Parameter(name = 'ImlSum12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSum12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

ImlSum13 = Parameter(name = 'ImlSum13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSum13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

ImlSum21 = Parameter(name = 'ImlSum21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSum21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

ImlSum22 = Parameter(name = 'ImlSum22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSum22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

ImlSum23 = Parameter(name = 'ImlSum23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSum23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ImlSum31 = Parameter(name = 'ImlSum31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSum31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

ImlSum32 = Parameter(name = 'ImlSum32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSum32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

ImlSum33 = Parameter(name = 'ImlSum33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSum33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 18 ])

lamHSu = Parameter(name = 'lamHSu',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lamHSu}',
                   lhablock = 'FRBlock',
                   lhacode = [ 19 ])

lam2Su = Parameter(name = 'lam2Su',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lam2Su}',
                   lhablock = 'FRBlock',
                   lhacode = [ 20 ])

mYSu = Parameter(name = 'mYSu',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{mYSu}',
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

WYSu = Parameter(name = 'WYSu',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WYSu}',
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

RelSum1x1 = Parameter(name = 'RelSum1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSum11',
                      texname = '\\text{RelSum1x1}')

RelSum1x2 = Parameter(name = 'RelSum1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSum12',
                      texname = '\\text{RelSum1x2}')

RelSum1x3 = Parameter(name = 'RelSum1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSum13',
                      texname = '\\text{RelSum1x3}')

RelSum2x1 = Parameter(name = 'RelSum2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSum21',
                      texname = '\\text{RelSum2x1}')

RelSum2x2 = Parameter(name = 'RelSum2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSum22',
                      texname = '\\text{RelSum2x2}')

RelSum2x3 = Parameter(name = 'RelSum2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSum23',
                      texname = '\\text{RelSum2x3}')

RelSum3x1 = Parameter(name = 'RelSum3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSum31',
                      texname = '\\text{RelSum3x1}')

RelSum3x2 = Parameter(name = 'RelSum3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSum32',
                      texname = '\\text{RelSum3x2}')

RelSum3x3 = Parameter(name = 'RelSum3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSum33',
                      texname = '\\text{RelSum3x3}')

ImlSum1x1 = Parameter(name = 'ImlSum1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSum11',
                      texname = '\\text{ImlSum1x1}')

ImlSum1x2 = Parameter(name = 'ImlSum1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSum12',
                      texname = '\\text{ImlSum1x2}')

ImlSum1x3 = Parameter(name = 'ImlSum1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSum13',
                      texname = '\\text{ImlSum1x3}')

ImlSum2x1 = Parameter(name = 'ImlSum2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSum21',
                      texname = '\\text{ImlSum2x1}')

ImlSum2x2 = Parameter(name = 'ImlSum2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSum22',
                      texname = '\\text{ImlSum2x2}')

ImlSum2x3 = Parameter(name = 'ImlSum2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSum23',
                      texname = '\\text{ImlSum2x3}')

ImlSum3x1 = Parameter(name = 'ImlSum3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSum31',
                      texname = '\\text{ImlSum3x1}')

ImlSum3x2 = Parameter(name = 'ImlSum3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSum32',
                      texname = '\\text{ImlSum3x2}')

ImlSum3x3 = Parameter(name = 'ImlSum3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSum33',
                      texname = '\\text{ImlSum3x3}')

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

MYSu = Parameter(name = 'MYSu',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(mYSu**2 + (lamHSu*vev**2)/2.)',
                 texname = '\\text{MYSu}')

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

