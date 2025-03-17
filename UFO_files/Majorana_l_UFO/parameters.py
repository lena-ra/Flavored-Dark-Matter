# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Mon 17 Mar 2025 09:54:16



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

lamMlRe11 = Parameter(name = 'lamMlRe11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlRe11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 1 ])

lamMlRe12 = Parameter(name = 'lamMlRe12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlRe12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 2 ])

lamMlRe13 = Parameter(name = 'lamMlRe13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlRe13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 3 ])

lamMlRe21 = Parameter(name = 'lamMlRe21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlRe21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 4 ])

lamMlRe22 = Parameter(name = 'lamMlRe22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlRe22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 5 ])

lamMlRe23 = Parameter(name = 'lamMlRe23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlRe23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 6 ])

lamMlRe31 = Parameter(name = 'lamMlRe31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlRe31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 7 ])

lamMlRe32 = Parameter(name = 'lamMlRe32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlRe32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 8 ])

lamMlRe33 = Parameter(name = 'lamMlRe33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlRe33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 9 ])

lamMlIm11 = Parameter(name = 'lamMlIm11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlIm11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 10 ])

lamMlIm12 = Parameter(name = 'lamMlIm12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlIm12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 11 ])

lamMlIm13 = Parameter(name = 'lamMlIm13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlIm13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 12 ])

lamMlIm21 = Parameter(name = 'lamMlIm21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlIm21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 13 ])

lamMlIm22 = Parameter(name = 'lamMlIm22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlIm22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 14 ])

lamMlIm23 = Parameter(name = 'lamMlIm23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlIm23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 15 ])

lamMlIm31 = Parameter(name = 'lamMlIm31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlIm31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 16 ])

lamMlIm32 = Parameter(name = 'lamMlIm32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlIm32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 17 ])

lamMlIm33 = Parameter(name = 'lamMlIm33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMlIm33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 18 ])

lamYHl1 = Parameter(name = 'lamYHl1',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{lamYHl1}',
                    lhablock = 'FRBlock',
                    lhacode = [ 19 ])

lamYHl2 = Parameter(name = 'lamYHl2',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{lamYHl2}',
                    lhablock = 'FRBlock',
                    lhacode = [ 20 ])

lamYHl3 = Parameter(name = 'lamYHl3',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{lamYHl3}',
                    lhablock = 'FRBlock',
                    lhacode = [ 21 ])

lam2Yl = Parameter(name = 'lam2Yl',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lam2Yl}',
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

MXM1 = Parameter(name = 'MXM1',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{MXM1}',
                 lhablock = 'MASS',
                 lhacode = [ 9000005 ])

MXM2 = Parameter(name = 'MXM2',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{MXM2}',
                 lhablock = 'MASS',
                 lhacode = [ 9000006 ])

MXM3 = Parameter(name = 'MXM3',
                 nature = 'external',
                 type = 'real',
                 value = 300,
                 texname = '\\text{MXM3}',
                 lhablock = 'MASS',
                 lhacode = [ 9000007 ])

MYSle = Parameter(name = 'MYSle',
                  nature = 'external',
                  type = 'real',
                  value = 500,
                  texname = '\\text{MYSle}',
                  lhablock = 'MASS',
                  lhacode = [ 9000008 ])

MYSlvR = Parameter(name = 'MYSlvR',
                   nature = 'external',
                   type = 'real',
                   value = 500,
                   texname = '\\text{MYSlvR}',
                   lhablock = 'MASS',
                   lhacode = [ 9000009 ])

MYSlvI = Parameter(name = 'MYSlvI',
                   nature = 'external',
                   type = 'real',
                   value = 500,
                   texname = '\\text{MYSlvI}',
                   lhablock = 'MASS',
                   lhacode = [ 9000010 ])

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

wXM1 = Parameter(name = 'wXM1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXM1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000005 ])

wXM2 = Parameter(name = 'wXM2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXM2}',
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

lamMlRe1x1 = Parameter(name = 'lamMlRe1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlRe11',
                       texname = '\\text{lamMlRe1x1}')

lamMlRe1x2 = Parameter(name = 'lamMlRe1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlRe12',
                       texname = '\\text{lamMlRe1x2}')

lamMlRe1x3 = Parameter(name = 'lamMlRe1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlRe13',
                       texname = '\\text{lamMlRe1x3}')

lamMlRe2x1 = Parameter(name = 'lamMlRe2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlRe21',
                       texname = '\\text{lamMlRe2x1}')

lamMlRe2x2 = Parameter(name = 'lamMlRe2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlRe22',
                       texname = '\\text{lamMlRe2x2}')

lamMlRe2x3 = Parameter(name = 'lamMlRe2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlRe23',
                       texname = '\\text{lamMlRe2x3}')

lamMlRe3x1 = Parameter(name = 'lamMlRe3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlRe31',
                       texname = '\\text{lamMlRe3x1}')

lamMlRe3x2 = Parameter(name = 'lamMlRe3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlRe32',
                       texname = '\\text{lamMlRe3x2}')

lamMlRe3x3 = Parameter(name = 'lamMlRe3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlRe33',
                       texname = '\\text{lamMlRe3x3}')

lamMlIm1x1 = Parameter(name = 'lamMlIm1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlIm11',
                       texname = '\\text{lamMlIm1x1}')

lamMlIm1x2 = Parameter(name = 'lamMlIm1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlIm12',
                       texname = '\\text{lamMlIm1x2}')

lamMlIm1x3 = Parameter(name = 'lamMlIm1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlIm13',
                       texname = '\\text{lamMlIm1x3}')

lamMlIm2x1 = Parameter(name = 'lamMlIm2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlIm21',
                       texname = '\\text{lamMlIm2x1}')

lamMlIm2x2 = Parameter(name = 'lamMlIm2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlIm22',
                       texname = '\\text{lamMlIm2x2}')

lamMlIm2x3 = Parameter(name = 'lamMlIm2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlIm23',
                       texname = '\\text{lamMlIm2x3}')

lamMlIm3x1 = Parameter(name = 'lamMlIm3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlIm31',
                       texname = '\\text{lamMlIm3x1}')

lamMlIm3x2 = Parameter(name = 'lamMlIm3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlIm32',
                       texname = '\\text{lamMlIm3x2}')

lamMlIm3x3 = Parameter(name = 'lamMlIm3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMlIm33',
                       texname = '\\text{lamMlIm3x3}')

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

