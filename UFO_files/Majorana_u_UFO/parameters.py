# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Mon 17 Mar 2025 09:51:31



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

lamMuRe11 = Parameter(name = 'lamMuRe11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuRe11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 1 ])

lamMuRe12 = Parameter(name = 'lamMuRe12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuRe12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 2 ])

lamMuRe13 = Parameter(name = 'lamMuRe13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuRe13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 3 ])

lamMuRe21 = Parameter(name = 'lamMuRe21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuRe21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 4 ])

lamMuRe22 = Parameter(name = 'lamMuRe22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuRe22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 5 ])

lamMuRe23 = Parameter(name = 'lamMuRe23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuRe23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 6 ])

lamMuRe31 = Parameter(name = 'lamMuRe31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuRe31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 7 ])

lamMuRe32 = Parameter(name = 'lamMuRe32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuRe32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 8 ])

lamMuRe33 = Parameter(name = 'lamMuRe33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuRe33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 9 ])

lamMuIm11 = Parameter(name = 'lamMuIm11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuIm11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 10 ])

lamMuIm12 = Parameter(name = 'lamMuIm12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuIm12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 11 ])

lamMuIm13 = Parameter(name = 'lamMuIm13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuIm13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 12 ])

lamMuIm21 = Parameter(name = 'lamMuIm21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuIm21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 13 ])

lamMuIm22 = Parameter(name = 'lamMuIm22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuIm22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 14 ])

lamMuIm23 = Parameter(name = 'lamMuIm23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuIm23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 15 ])

lamMuIm31 = Parameter(name = 'lamMuIm31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuIm31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 16 ])

lamMuIm32 = Parameter(name = 'lamMuIm32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuIm32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 17 ])

lamMuIm33 = Parameter(name = 'lamMuIm33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamMuIm33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 18 ])

lamYHu = Parameter(name = 'lamYHu',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lamYHu}',
                   lhablock = 'FRBlock',
                   lhacode = [ 19 ])

lam2Yu = Parameter(name = 'lam2Yu',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{lam2Yu}',
                   lhablock = 'FRBlock',
                   lhacode = [ 20 ])

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

MYSu = Parameter(name = 'MYSu',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{MYSu}',
                 lhablock = 'MASS',
                 lhacode = [ 9000008 ])

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

lamMuRe1x1 = Parameter(name = 'lamMuRe1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuRe11',
                       texname = '\\text{lamMuRe1x1}')

lamMuRe1x2 = Parameter(name = 'lamMuRe1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuRe12',
                       texname = '\\text{lamMuRe1x2}')

lamMuRe1x3 = Parameter(name = 'lamMuRe1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuRe13',
                       texname = '\\text{lamMuRe1x3}')

lamMuRe2x1 = Parameter(name = 'lamMuRe2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuRe21',
                       texname = '\\text{lamMuRe2x1}')

lamMuRe2x2 = Parameter(name = 'lamMuRe2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuRe22',
                       texname = '\\text{lamMuRe2x2}')

lamMuRe2x3 = Parameter(name = 'lamMuRe2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuRe23',
                       texname = '\\text{lamMuRe2x3}')

lamMuRe3x1 = Parameter(name = 'lamMuRe3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuRe31',
                       texname = '\\text{lamMuRe3x1}')

lamMuRe3x2 = Parameter(name = 'lamMuRe3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuRe32',
                       texname = '\\text{lamMuRe3x2}')

lamMuRe3x3 = Parameter(name = 'lamMuRe3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuRe33',
                       texname = '\\text{lamMuRe3x3}')

lamMuIm1x1 = Parameter(name = 'lamMuIm1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuIm11',
                       texname = '\\text{lamMuIm1x1}')

lamMuIm1x2 = Parameter(name = 'lamMuIm1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuIm12',
                       texname = '\\text{lamMuIm1x2}')

lamMuIm1x3 = Parameter(name = 'lamMuIm1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuIm13',
                       texname = '\\text{lamMuIm1x3}')

lamMuIm2x1 = Parameter(name = 'lamMuIm2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuIm21',
                       texname = '\\text{lamMuIm2x1}')

lamMuIm2x2 = Parameter(name = 'lamMuIm2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuIm22',
                       texname = '\\text{lamMuIm2x2}')

lamMuIm2x3 = Parameter(name = 'lamMuIm2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuIm23',
                       texname = '\\text{lamMuIm2x3}')

lamMuIm3x1 = Parameter(name = 'lamMuIm3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuIm31',
                       texname = '\\text{lamMuIm3x1}')

lamMuIm3x2 = Parameter(name = 'lamMuIm3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuIm32',
                       texname = '\\text{lamMuIm3x2}')

lamMuIm3x3 = Parameter(name = 'lamMuIm3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamMuIm33',
                       texname = '\\text{lamMuIm3x3}')

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

