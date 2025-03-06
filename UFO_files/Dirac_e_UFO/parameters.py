# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:29:42



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

RelSed11 = Parameter(name = 'RelSed11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSed11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 1 ])

RelSed12 = Parameter(name = 'RelSed12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSed12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 2 ])

RelSed13 = Parameter(name = 'RelSed13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSed13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 3 ])

RelSed21 = Parameter(name = 'RelSed21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSed21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 4 ])

RelSed22 = Parameter(name = 'RelSed22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSed22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

RelSed23 = Parameter(name = 'RelSed23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSed23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

RelSed31 = Parameter(name = 'RelSed31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSed31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 7 ])

RelSed32 = Parameter(name = 'RelSed32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSed32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 8 ])

RelSed33 = Parameter(name = 'RelSed33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSed33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

ImlSed11 = Parameter(name = 'ImlSed11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSed11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 10 ])

ImlSed12 = Parameter(name = 'ImlSed12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSed12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

ImlSed13 = Parameter(name = 'ImlSed13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSed13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

ImlSed21 = Parameter(name = 'ImlSed21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSed21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

ImlSed22 = Parameter(name = 'ImlSed22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSed22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

ImlSed23 = Parameter(name = 'ImlSed23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSed23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ImlSed31 = Parameter(name = 'ImlSed31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSed31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

ImlSed32 = Parameter(name = 'ImlSed32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSed32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

ImlSed33 = Parameter(name = 'ImlSed33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSed33}',
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

RelSed1x1 = Parameter(name = 'RelSed1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSed11',
                      texname = '\\text{RelSed1x1}')

RelSed1x2 = Parameter(name = 'RelSed1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSed12',
                      texname = '\\text{RelSed1x2}')

RelSed1x3 = Parameter(name = 'RelSed1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSed13',
                      texname = '\\text{RelSed1x3}')

RelSed2x1 = Parameter(name = 'RelSed2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSed21',
                      texname = '\\text{RelSed2x1}')

RelSed2x2 = Parameter(name = 'RelSed2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSed22',
                      texname = '\\text{RelSed2x2}')

RelSed2x3 = Parameter(name = 'RelSed2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSed23',
                      texname = '\\text{RelSed2x3}')

RelSed3x1 = Parameter(name = 'RelSed3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSed31',
                      texname = '\\text{RelSed3x1}')

RelSed3x2 = Parameter(name = 'RelSed3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSed32',
                      texname = '\\text{RelSed3x2}')

RelSed3x3 = Parameter(name = 'RelSed3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSed33',
                      texname = '\\text{RelSed3x3}')

ImlSed1x1 = Parameter(name = 'ImlSed1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSed11',
                      texname = '\\text{ImlSed1x1}')

ImlSed1x2 = Parameter(name = 'ImlSed1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSed12',
                      texname = '\\text{ImlSed1x2}')

ImlSed1x3 = Parameter(name = 'ImlSed1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSed13',
                      texname = '\\text{ImlSed1x3}')

ImlSed2x1 = Parameter(name = 'ImlSed2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSed21',
                      texname = '\\text{ImlSed2x1}')

ImlSed2x2 = Parameter(name = 'ImlSed2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSed22',
                      texname = '\\text{ImlSed2x2}')

ImlSed2x3 = Parameter(name = 'ImlSed2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSed23',
                      texname = '\\text{ImlSed2x3}')

ImlSed3x1 = Parameter(name = 'ImlSed3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSed31',
                      texname = '\\text{ImlSed3x1}')

ImlSed3x2 = Parameter(name = 'ImlSed3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSed32',
                      texname = '\\text{ImlSed3x2}')

ImlSed3x3 = Parameter(name = 'ImlSed3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSed33',
                      texname = '\\text{ImlSed3x3}')

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

