# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:27:47



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

RelSdd11 = Parameter(name = 'RelSdd11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdd11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 1 ])

RelSdd12 = Parameter(name = 'RelSdd12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdd12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 2 ])

RelSdd13 = Parameter(name = 'RelSdd13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdd13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 3 ])

RelSdd21 = Parameter(name = 'RelSdd21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdd21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 4 ])

RelSdd22 = Parameter(name = 'RelSdd22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdd22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

RelSdd23 = Parameter(name = 'RelSdd23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdd23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

RelSdd31 = Parameter(name = 'RelSdd31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdd31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 7 ])

RelSdd32 = Parameter(name = 'RelSdd32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdd32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 8 ])

RelSdd33 = Parameter(name = 'RelSdd33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdd33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

ImlSdd11 = Parameter(name = 'ImlSdd11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdd11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 10 ])

ImlSdd12 = Parameter(name = 'ImlSdd12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdd12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

ImlSdd13 = Parameter(name = 'ImlSdd13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdd13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

ImlSdd21 = Parameter(name = 'ImlSdd21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdd21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

ImlSdd22 = Parameter(name = 'ImlSdd22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdd22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

ImlSdd23 = Parameter(name = 'ImlSdd23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdd23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ImlSdd31 = Parameter(name = 'ImlSdd31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdd31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

ImlSdd32 = Parameter(name = 'ImlSdd32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdd32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

ImlSdd33 = Parameter(name = 'ImlSdd33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdd33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 18 ])

lamHSd = Parameter(name = 'lamHSd',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lamHSd}',
                   lhablock = 'FRBlock',
                   lhacode = [ 19 ])

lam2Sd = Parameter(name = 'lam2Sd',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lam2Sd}',
                   lhablock = 'FRBlock',
                   lhacode = [ 20 ])

mYSd = Parameter(name = 'mYSd',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{mYSd}',
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

MXd1 = Parameter(name = 'MXd1',
                 nature = 'external',
                 type = 'real',
                 value = 300,
                 texname = '\\text{MXd1}',
                 lhablock = 'MASS',
                 lhacode = [ 9000005 ])

MXd2 = Parameter(name = 'MXd2',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{MXd2}',
                 lhablock = 'MASS',
                 lhacode = [ 9000006 ])

MXd3 = Parameter(name = 'MXd3',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{MXd3}',
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

wXd1 = Parameter(name = 'wXd1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXd1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000005 ])

wXd2 = Parameter(name = 'wXd2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXd2}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000006 ])

WYSd = Parameter(name = 'WYSd',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WYSd}',
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

RelSdd1x1 = Parameter(name = 'RelSdd1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdd11',
                      texname = '\\text{RelSdd1x1}')

RelSdd1x2 = Parameter(name = 'RelSdd1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdd12',
                      texname = '\\text{RelSdd1x2}')

RelSdd1x3 = Parameter(name = 'RelSdd1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdd13',
                      texname = '\\text{RelSdd1x3}')

RelSdd2x1 = Parameter(name = 'RelSdd2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdd21',
                      texname = '\\text{RelSdd2x1}')

RelSdd2x2 = Parameter(name = 'RelSdd2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdd22',
                      texname = '\\text{RelSdd2x2}')

RelSdd2x3 = Parameter(name = 'RelSdd2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdd23',
                      texname = '\\text{RelSdd2x3}')

RelSdd3x1 = Parameter(name = 'RelSdd3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdd31',
                      texname = '\\text{RelSdd3x1}')

RelSdd3x2 = Parameter(name = 'RelSdd3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdd32',
                      texname = '\\text{RelSdd3x2}')

RelSdd3x3 = Parameter(name = 'RelSdd3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdd33',
                      texname = '\\text{RelSdd3x3}')

ImlSdd1x1 = Parameter(name = 'ImlSdd1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdd11',
                      texname = '\\text{ImlSdd1x1}')

ImlSdd1x2 = Parameter(name = 'ImlSdd1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdd12',
                      texname = '\\text{ImlSdd1x2}')

ImlSdd1x3 = Parameter(name = 'ImlSdd1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdd13',
                      texname = '\\text{ImlSdd1x3}')

ImlSdd2x1 = Parameter(name = 'ImlSdd2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdd21',
                      texname = '\\text{ImlSdd2x1}')

ImlSdd2x2 = Parameter(name = 'ImlSdd2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdd22',
                      texname = '\\text{ImlSdd2x2}')

ImlSdd2x3 = Parameter(name = 'ImlSdd2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdd23',
                      texname = '\\text{ImlSdd2x3}')

ImlSdd3x1 = Parameter(name = 'ImlSdd3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdd31',
                      texname = '\\text{ImlSdd3x1}')

ImlSdd3x2 = Parameter(name = 'ImlSdd3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdd32',
                      texname = '\\text{ImlSdd3x2}')

ImlSdd3x3 = Parameter(name = 'ImlSdd3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdd33',
                      texname = '\\text{ImlSdd3x3}')

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

MYSd = Parameter(name = 'MYSd',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(mYSd**2 + (lamHSd*vev**2)/2.)',
                 texname = '\\text{MYSd}')

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

