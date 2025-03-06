# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:37:53



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

RelSdm11 = Parameter(name = 'RelSdm11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdm11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 1 ])

RelSdm12 = Parameter(name = 'RelSdm12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdm12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 2 ])

RelSdm13 = Parameter(name = 'RelSdm13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdm13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 3 ])

RelSdm21 = Parameter(name = 'RelSdm21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdm21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 4 ])

RelSdm22 = Parameter(name = 'RelSdm22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdm22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

RelSdm23 = Parameter(name = 'RelSdm23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdm23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

RelSdm31 = Parameter(name = 'RelSdm31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdm31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 7 ])

RelSdm32 = Parameter(name = 'RelSdm32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdm32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 8 ])

RelSdm33 = Parameter(name = 'RelSdm33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSdm33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

ImlSdm11 = Parameter(name = 'ImlSdm11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdm11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 10 ])

ImlSdm12 = Parameter(name = 'ImlSdm12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdm12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

ImlSdm13 = Parameter(name = 'ImlSdm13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdm13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

ImlSdm21 = Parameter(name = 'ImlSdm21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdm21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

ImlSdm22 = Parameter(name = 'ImlSdm22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdm22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

ImlSdm23 = Parameter(name = 'ImlSdm23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdm23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ImlSdm31 = Parameter(name = 'ImlSdm31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdm31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

ImlSdm32 = Parameter(name = 'ImlSdm32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdm32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

ImlSdm33 = Parameter(name = 'ImlSdm33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSdm33}',
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

RelSdm1x1 = Parameter(name = 'RelSdm1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdm11',
                      texname = '\\text{RelSdm1x1}')

RelSdm1x2 = Parameter(name = 'RelSdm1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdm12',
                      texname = '\\text{RelSdm1x2}')

RelSdm1x3 = Parameter(name = 'RelSdm1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdm13',
                      texname = '\\text{RelSdm1x3}')

RelSdm2x1 = Parameter(name = 'RelSdm2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdm21',
                      texname = '\\text{RelSdm2x1}')

RelSdm2x2 = Parameter(name = 'RelSdm2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdm22',
                      texname = '\\text{RelSdm2x2}')

RelSdm2x3 = Parameter(name = 'RelSdm2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdm23',
                      texname = '\\text{RelSdm2x3}')

RelSdm3x1 = Parameter(name = 'RelSdm3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdm31',
                      texname = '\\text{RelSdm3x1}')

RelSdm3x2 = Parameter(name = 'RelSdm3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdm32',
                      texname = '\\text{RelSdm3x2}')

RelSdm3x3 = Parameter(name = 'RelSdm3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSdm33',
                      texname = '\\text{RelSdm3x3}')

ImlSdm1x1 = Parameter(name = 'ImlSdm1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdm11',
                      texname = '\\text{ImlSdm1x1}')

ImlSdm1x2 = Parameter(name = 'ImlSdm1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdm12',
                      texname = '\\text{ImlSdm1x2}')

ImlSdm1x3 = Parameter(name = 'ImlSdm1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdm13',
                      texname = '\\text{ImlSdm1x3}')

ImlSdm2x1 = Parameter(name = 'ImlSdm2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdm21',
                      texname = '\\text{ImlSdm2x1}')

ImlSdm2x2 = Parameter(name = 'ImlSdm2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdm22',
                      texname = '\\text{ImlSdm2x2}')

ImlSdm2x3 = Parameter(name = 'ImlSdm2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdm23',
                      texname = '\\text{ImlSdm2x3}')

ImlSdm3x1 = Parameter(name = 'ImlSdm3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdm31',
                      texname = '\\text{ImlSdm3x1}')

ImlSdm3x2 = Parameter(name = 'ImlSdm3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdm32',
                      texname = '\\text{ImlSdm3x2}')

ImlSdm3x3 = Parameter(name = 'ImlSdm3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSdm33',
                      texname = '\\text{ImlSdm3x3}')

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

