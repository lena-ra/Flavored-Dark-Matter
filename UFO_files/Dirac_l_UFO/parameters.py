# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:32:27



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

RelSld11 = Parameter(name = 'RelSld11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSld11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 1 ])

RelSld12 = Parameter(name = 'RelSld12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSld12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 2 ])

RelSld13 = Parameter(name = 'RelSld13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSld13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 3 ])

RelSld21 = Parameter(name = 'RelSld21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSld21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 4 ])

RelSld22 = Parameter(name = 'RelSld22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSld22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 5 ])

RelSld23 = Parameter(name = 'RelSld23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSld23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 6 ])

RelSld31 = Parameter(name = 'RelSld31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSld31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 7 ])

RelSld32 = Parameter(name = 'RelSld32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSld32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 8 ])

RelSld33 = Parameter(name = 'RelSld33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{RelSld33}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

ImlSld11 = Parameter(name = 'ImlSld11',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSld11}',
                     lhablock = 'FRBlock',
                     lhacode = [ 10 ])

ImlSld12 = Parameter(name = 'ImlSld12',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSld12}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

ImlSld13 = Parameter(name = 'ImlSld13',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSld13}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

ImlSld21 = Parameter(name = 'ImlSld21',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSld21}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

ImlSld22 = Parameter(name = 'ImlSld22',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSld22}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

ImlSld23 = Parameter(name = 'ImlSld23',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSld23}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

ImlSld31 = Parameter(name = 'ImlSld31',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSld31}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

ImlSld32 = Parameter(name = 'ImlSld32',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSld32}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

ImlSld33 = Parameter(name = 'ImlSld33',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{ImlSld33}',
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

RelSld1x1 = Parameter(name = 'RelSld1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSld11',
                      texname = '\\text{RelSld1x1}')

RelSld1x2 = Parameter(name = 'RelSld1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSld12',
                      texname = '\\text{RelSld1x2}')

RelSld1x3 = Parameter(name = 'RelSld1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSld13',
                      texname = '\\text{RelSld1x3}')

RelSld2x1 = Parameter(name = 'RelSld2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSld21',
                      texname = '\\text{RelSld2x1}')

RelSld2x2 = Parameter(name = 'RelSld2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSld22',
                      texname = '\\text{RelSld2x2}')

RelSld2x3 = Parameter(name = 'RelSld2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSld23',
                      texname = '\\text{RelSld2x3}')

RelSld3x1 = Parameter(name = 'RelSld3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSld31',
                      texname = '\\text{RelSld3x1}')

RelSld3x2 = Parameter(name = 'RelSld3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSld32',
                      texname = '\\text{RelSld3x2}')

RelSld3x3 = Parameter(name = 'RelSld3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'RelSld33',
                      texname = '\\text{RelSld3x3}')

ImlSld1x1 = Parameter(name = 'ImlSld1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSld11',
                      texname = '\\text{ImlSld1x1}')

ImlSld1x2 = Parameter(name = 'ImlSld1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSld12',
                      texname = '\\text{ImlSld1x2}')

ImlSld1x3 = Parameter(name = 'ImlSld1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSld13',
                      texname = '\\text{ImlSld1x3}')

ImlSld2x1 = Parameter(name = 'ImlSld2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSld21',
                      texname = '\\text{ImlSld2x1}')

ImlSld2x2 = Parameter(name = 'ImlSld2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSld22',
                      texname = '\\text{ImlSld2x2}')

ImlSld2x3 = Parameter(name = 'ImlSld2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSld23',
                      texname = '\\text{ImlSld2x3}')

ImlSld3x1 = Parameter(name = 'ImlSld3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSld31',
                      texname = '\\text{ImlSld3x1}')

ImlSld3x2 = Parameter(name = 'ImlSld3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSld32',
                      texname = '\\text{ImlSld3x2}')

ImlSld3x3 = Parameter(name = 'ImlSld3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'ImlSld33',
                      texname = '\\text{ImlSld3x3}')

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

