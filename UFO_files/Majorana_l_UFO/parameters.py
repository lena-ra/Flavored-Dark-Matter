# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:41:14



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

RelSlm11 = Parameter(name = 'RelSlm11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSlm11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 1 ])

RelSlm12 = Parameter(name = 'RelSlm12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSlm12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 2 ])

RelSlm13 = Parameter(name = 'RelSlm13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSlm13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 3 ])

RelSlm21 = Parameter(name = 'RelSlm21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSlm21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 4 ])

RelSlm22 = Parameter(name = 'RelSlm22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSlm22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

RelSlm23 = Parameter(name = 'RelSlm23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSlm23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

RelSlm31 = Parameter(name = 'RelSlm31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSlm31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 7 ])

RelSlm32 = Parameter(name = 'RelSlm32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSlm32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 8 ])

RelSlm33 = Parameter(name = 'RelSlm33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSlm33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

ImlSlm11 = Parameter(name = 'ImlSlm11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSlm11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 10 ])

ImlSlm12 = Parameter(name = 'ImlSlm12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSlm12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

ImlSlm13 = Parameter(name = 'ImlSlm13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSlm13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

ImlSlm21 = Parameter(name = 'ImlSlm21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSlm21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

ImlSlm22 = Parameter(name = 'ImlSlm22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSlm22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

ImlSlm23 = Parameter(name = 'ImlSlm23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSlm23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ImlSlm31 = Parameter(name = 'ImlSlm31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSlm31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

ImlSlm32 = Parameter(name = 'ImlSlm32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSlm32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

ImlSlm33 = Parameter(name = 'ImlSlm33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSlm33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 18 ])

lamHSl1 = Parameter(name = 'lamHSl1',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{lamHSl1}',
                    lhablock = 'FRBlock',
                    lhacode = [ 19 ])

lamHSl2 = Parameter(name = 'lamHSl2',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{lamHSl2}',
                    lhablock = 'FRBlock',
                    lhacode = [ 20 ])

lamHSl3 = Parameter(name = 'lamHSl3',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{lamHSl3}',
                    lhablock = 'FRBlock',
                    lhacode = [ 21 ])

lam2Sl = Parameter(name = 'lam2Sl',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lam2Sl}',
                   lhablock = 'FRBlock',
                   lhacode = [ 22 ])

mYSl = Parameter(name = 'mYSl',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{mYSl}',
                 lhablock = 'FRBlock',
                 lhacode = [ 23 ])

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

WYSle = Parameter(name = 'WYSle',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WYSle}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000008 ])

WYSlvR = Parameter(name = 'WYSlvR',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{WYSlvR}',
                   lhablock = 'DECAY',
                   lhacode = [ 9000009 ])

WYSlvI = Parameter(name = 'WYSlvI',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{WYSlvI}',
                   lhablock = 'DECAY',
                   lhacode = [ 9000010 ])

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

RelSlm1x1 = Parameter(name = 'RelSlm1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSlm11',
                      texname = '\\text{RelSlm1x1}')

RelSlm1x2 = Parameter(name = 'RelSlm1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSlm12',
                      texname = '\\text{RelSlm1x2}')

RelSlm1x3 = Parameter(name = 'RelSlm1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSlm13',
                      texname = '\\text{RelSlm1x3}')

RelSlm2x1 = Parameter(name = 'RelSlm2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSlm21',
                      texname = '\\text{RelSlm2x1}')

RelSlm2x2 = Parameter(name = 'RelSlm2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSlm22',
                      texname = '\\text{RelSlm2x2}')

RelSlm2x3 = Parameter(name = 'RelSlm2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSlm23',
                      texname = '\\text{RelSlm2x3}')

RelSlm3x1 = Parameter(name = 'RelSlm3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSlm31',
                      texname = '\\text{RelSlm3x1}')

RelSlm3x2 = Parameter(name = 'RelSlm3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSlm32',
                      texname = '\\text{RelSlm3x2}')

RelSlm3x3 = Parameter(name = 'RelSlm3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSlm33',
                      texname = '\\text{RelSlm3x3}')

ImlSlm1x1 = Parameter(name = 'ImlSlm1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSlm11',
                      texname = '\\text{ImlSlm1x1}')

ImlSlm1x2 = Parameter(name = 'ImlSlm1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSlm12',
                      texname = '\\text{ImlSlm1x2}')

ImlSlm1x3 = Parameter(name = 'ImlSlm1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSlm13',
                      texname = '\\text{ImlSlm1x3}')

ImlSlm2x1 = Parameter(name = 'ImlSlm2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSlm21',
                      texname = '\\text{ImlSlm2x1}')

ImlSlm2x2 = Parameter(name = 'ImlSlm2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSlm22',
                      texname = '\\text{ImlSlm2x2}')

ImlSlm2x3 = Parameter(name = 'ImlSlm2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSlm23',
                      texname = '\\text{ImlSlm2x3}')

ImlSlm3x1 = Parameter(name = 'ImlSlm3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSlm31',
                      texname = '\\text{ImlSlm3x1}')

ImlSlm3x2 = Parameter(name = 'ImlSlm3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSlm32',
                      texname = '\\text{ImlSlm3x2}')

ImlSlm3x3 = Parameter(name = 'ImlSlm3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSlm33',
                      texname = '\\text{ImlSlm3x3}')

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

MYSle = Parameter(name = 'MYSle',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sqrt(mYSl**2 + ((lamHSl1 + lamHSl2)*vev**2)/2.)',
                  texname = '\\text{MYSle}')

MYSlvI = Parameter(name = 'MYSlvI',
                   nature = 'internal',
                   type = 'real',
                   value = 'cmath.sqrt(mYSl**2 + ((lamHSl1 - lamHSl3)*vev**2)/2.)',
                   texname = '\\text{MYSlvI}')

MYSlvR = Parameter(name = 'MYSlvR',
                   nature = 'internal',
                   type = 'real',
                   value = 'cmath.sqrt(mYSl**2 + ((lamHSl1 + lamHSl3)*vev**2)/2.)',
                   texname = '\\text{MYSlvR}')

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

