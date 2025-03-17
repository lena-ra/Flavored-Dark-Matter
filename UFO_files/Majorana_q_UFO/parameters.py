# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Mon 17 Mar 2025 09:50:29



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

lamMqRe11 = Parameter(name = 'lamMqRe11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqRe11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 1 ])

lamMqRe12 = Parameter(name = 'lamMqRe12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqRe12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 2 ])

lamMqRe13 = Parameter(name = 'lamMqRe13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqRe13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 3 ])

lamMqRe21 = Parameter(name = 'lamMqRe21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqRe21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 4 ])

lamMqRe22 = Parameter(name = 'lamMqRe22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqRe22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 5 ])

lamMqRe23 = Parameter(name = 'lamMqRe23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqRe23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 6 ])

lamMqRe31 = Parameter(name = 'lamMqRe31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqRe31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 7 ])

lamMqRe32 = Parameter(name = 'lamMqRe32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqRe32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 8 ])

lamMqRe33 = Parameter(name = 'lamMqRe33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqRe33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 9 ])

lamMqIm11 = Parameter(name = 'lamMqIm11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqIm11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 10 ])

lamMqIm12 = Parameter(name = 'lamMqIm12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqIm12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 11 ])

lamMqIm13 = Parameter(name = 'lamMqIm13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqIm13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 12 ])

lamMqIm21 = Parameter(name = 'lamMqIm21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqIm21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 13 ])

lamMqIm22 = Parameter(name = 'lamMqIm22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqIm22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 14 ])

lamMqIm23 = Parameter(name = 'lamMqIm23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqIm23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 15 ])

lamMqIm31 = Parameter(name = 'lamMqIm31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqIm31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 16 ])

lamMqIm32 = Parameter(name = 'lamMqIm32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqIm32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 17 ])

lamMqIm33 = Parameter(name = 'lamMqIm33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMqIm33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 18 ])

lamYHq1 = Parameter(name = 'lamYHq1',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{lamYHq1}',
                    lhablock = 'FRBlock',
                    lhacode = [ 19 ])

lamYHq2 = Parameter(name = 'lamYHq2',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{lamYHq2}',
                    lhablock = 'FRBlock',
                    lhacode = [ 20 ])

lam2Yq = Parameter(name = 'lam2Yq',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lam2Yq}',
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

MYSqu = Parameter(name = 'MYSqu',
                  nature = 'external',
                  type = 'real',
                  value = 500,
                  texname = '\\text{MYSqu}',
                  lhablock = 'MASS',
                  lhacode = [ 9000008 ])

MYSqd = Parameter(name = 'MYSqd',
                  nature = 'external',
                  type = 'real',
                  value = 500,
                  texname = '\\text{MYSqd}',
                  lhablock = 'MASS',
                  lhacode = [ 9000009 ])

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

lamMqRe1x1 = Parameter(name = 'lamMqRe1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqRe11',
                       texname = '\\text{lamMqRe1x1}')

lamMqRe1x2 = Parameter(name = 'lamMqRe1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqRe12',
                       texname = '\\text{lamMqRe1x2}')

lamMqRe1x3 = Parameter(name = 'lamMqRe1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqRe13',
                       texname = '\\text{lamMqRe1x3}')

lamMqRe2x1 = Parameter(name = 'lamMqRe2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqRe21',
                       texname = '\\text{lamMqRe2x1}')

lamMqRe2x2 = Parameter(name = 'lamMqRe2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqRe22',
                       texname = '\\text{lamMqRe2x2}')

lamMqRe2x3 = Parameter(name = 'lamMqRe2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqRe23',
                       texname = '\\text{lamMqRe2x3}')

lamMqRe3x1 = Parameter(name = 'lamMqRe3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqRe31',
                       texname = '\\text{lamMqRe3x1}')

lamMqRe3x2 = Parameter(name = 'lamMqRe3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqRe32',
                       texname = '\\text{lamMqRe3x2}')

lamMqRe3x3 = Parameter(name = 'lamMqRe3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqRe33',
                       texname = '\\text{lamMqRe3x3}')

lamMqIm1x1 = Parameter(name = 'lamMqIm1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqIm11',
                       texname = '\\text{lamMqIm1x1}')

lamMqIm1x2 = Parameter(name = 'lamMqIm1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqIm12',
                       texname = '\\text{lamMqIm1x2}')

lamMqIm1x3 = Parameter(name = 'lamMqIm1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqIm13',
                       texname = '\\text{lamMqIm1x3}')

lamMqIm2x1 = Parameter(name = 'lamMqIm2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqIm21',
                       texname = '\\text{lamMqIm2x1}')

lamMqIm2x2 = Parameter(name = 'lamMqIm2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqIm22',
                       texname = '\\text{lamMqIm2x2}')

lamMqIm2x3 = Parameter(name = 'lamMqIm2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqIm23',
                       texname = '\\text{lamMqIm2x3}')

lamMqIm3x1 = Parameter(name = 'lamMqIm3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqIm31',
                       texname = '\\text{lamMqIm3x1}')

lamMqIm3x2 = Parameter(name = 'lamMqIm3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqIm32',
                       texname = '\\text{lamMqIm3x2}')

lamMqIm3x3 = Parameter(name = 'lamMqIm3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMqIm33',
                       texname = '\\text{lamMqIm3x3}')

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

