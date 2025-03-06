# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:43:07



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

RelSqm11 = Parameter(name = 'RelSqm11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSqm11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 1 ])

RelSqm12 = Parameter(name = 'RelSqm12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSqm12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 2 ])

RelSqm13 = Parameter(name = 'RelSqm13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSqm13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 3 ])

RelSqm21 = Parameter(name = 'RelSqm21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSqm21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 4 ])

RelSqm22 = Parameter(name = 'RelSqm22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSqm22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

RelSqm23 = Parameter(name = 'RelSqm23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSqm23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

RelSqm31 = Parameter(name = 'RelSqm31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSqm31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 7 ])

RelSqm32 = Parameter(name = 'RelSqm32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSqm32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 8 ])

RelSqm33 = Parameter(name = 'RelSqm33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSqm33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

ImlSqm11 = Parameter(name = 'ImlSqm11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSqm11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 10 ])

ImlSqm12 = Parameter(name = 'ImlSqm12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSqm12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

ImlSqm13 = Parameter(name = 'ImlSqm13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSqm13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

ImlSqm21 = Parameter(name = 'ImlSqm21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSqm21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

ImlSqm22 = Parameter(name = 'ImlSqm22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSqm22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

ImlSqm23 = Parameter(name = 'ImlSqm23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSqm23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ImlSqm31 = Parameter(name = 'ImlSqm31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSqm31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

ImlSqm32 = Parameter(name = 'ImlSqm32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSqm32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

ImlSqm33 = Parameter(name = 'ImlSqm33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSqm33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 18 ])

lamHSq1 = Parameter(name = 'lamHSq1',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{lamHSq1}',
                    lhablock = 'FRBlock',
                    lhacode = [ 19 ])

lamHSq2 = Parameter(name = 'lamHSq2',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{lamHSq2}',
                    lhablock = 'FRBlock',
                    lhacode = [ 20 ])

lam2Sq = Parameter(name = 'lam2Sq',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lam2Sq}',
                   lhablock = 'FRBlock',
                   lhacode = [ 21 ])

mYSq = Parameter(name = 'mYSq',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{mYSq}',
                 lhablock = 'FRBlock',
                 lhacode = [ 22 ])

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

WYSqu = Parameter(name = 'WYSqu',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WYSqu}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000008 ])

WYSqd = Parameter(name = 'WYSqd',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WYSqd}',
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

RelSqm1x1 = Parameter(name = 'RelSqm1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSqm11',
                      texname = '\\text{RelSqm1x1}')

RelSqm1x2 = Parameter(name = 'RelSqm1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSqm12',
                      texname = '\\text{RelSqm1x2}')

RelSqm1x3 = Parameter(name = 'RelSqm1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSqm13',
                      texname = '\\text{RelSqm1x3}')

RelSqm2x1 = Parameter(name = 'RelSqm2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSqm21',
                      texname = '\\text{RelSqm2x1}')

RelSqm2x2 = Parameter(name = 'RelSqm2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSqm22',
                      texname = '\\text{RelSqm2x2}')

RelSqm2x3 = Parameter(name = 'RelSqm2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSqm23',
                      texname = '\\text{RelSqm2x3}')

RelSqm3x1 = Parameter(name = 'RelSqm3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSqm31',
                      texname = '\\text{RelSqm3x1}')

RelSqm3x2 = Parameter(name = 'RelSqm3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSqm32',
                      texname = '\\text{RelSqm3x2}')

RelSqm3x3 = Parameter(name = 'RelSqm3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSqm33',
                      texname = '\\text{RelSqm3x3}')

ImlSqm1x1 = Parameter(name = 'ImlSqm1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSqm11',
                      texname = '\\text{ImlSqm1x1}')

ImlSqm1x2 = Parameter(name = 'ImlSqm1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSqm12',
                      texname = '\\text{ImlSqm1x2}')

ImlSqm1x3 = Parameter(name = 'ImlSqm1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSqm13',
                      texname = '\\text{ImlSqm1x3}')

ImlSqm2x1 = Parameter(name = 'ImlSqm2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSqm21',
                      texname = '\\text{ImlSqm2x1}')

ImlSqm2x2 = Parameter(name = 'ImlSqm2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSqm22',
                      texname = '\\text{ImlSqm2x2}')

ImlSqm2x3 = Parameter(name = 'ImlSqm2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSqm23',
                      texname = '\\text{ImlSqm2x3}')

ImlSqm3x1 = Parameter(name = 'ImlSqm3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSqm31',
                      texname = '\\text{ImlSqm3x1}')

ImlSqm3x2 = Parameter(name = 'ImlSqm3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSqm32',
                      texname = '\\text{ImlSqm3x2}')

ImlSqm3x3 = Parameter(name = 'ImlSqm3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSqm33',
                      texname = '\\text{ImlSqm3x3}')

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

MYSqd = Parameter(name = 'MYSqd',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sqrt(mYSq**2 + ((lamHSq1 + lamHSq2)*vev**2)/2.)',
                  texname = '\\text{MYSqd}')

MYSqu = Parameter(name = 'MYSqu',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sqrt(mYSq**2 + (lamHSq1*vev**2)/2.)',
                  texname = '\\text{MYSqu}')

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

