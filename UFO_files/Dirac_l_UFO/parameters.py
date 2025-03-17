# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Fri 14 Mar 2025 17:33:19



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

lamDlRe11 = Parameter(name = 'lamDlRe11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlRe11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 1 ])

lamDlRe12 = Parameter(name = 'lamDlRe12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlRe12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 2 ])

lamDlRe13 = Parameter(name = 'lamDlRe13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlRe13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 3 ])

lamDlRe21 = Parameter(name = 'lamDlRe21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlRe21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 4 ])

lamDlRe22 = Parameter(name = 'lamDlRe22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlRe22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 5 ])

lamDlRe23 = Parameter(name = 'lamDlRe23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlRe23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 6 ])

lamDlRe31 = Parameter(name = 'lamDlRe31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlRe31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 7 ])

lamDlRe32 = Parameter(name = 'lamDlRe32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlRe32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 8 ])

lamDlRe33 = Parameter(name = 'lamDlRe33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlRe33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 9 ])

lamDlIm11 = Parameter(name = 'lamDlIm11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlIm11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 10 ])

lamDlIm12 = Parameter(name = 'lamDlIm12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlIm12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 11 ])

lamDlIm13 = Parameter(name = 'lamDlIm13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlIm13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 12 ])

lamDlIm21 = Parameter(name = 'lamDlIm21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlIm21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 13 ])

lamDlIm22 = Parameter(name = 'lamDlIm22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlIm22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 14 ])

lamDlIm23 = Parameter(name = 'lamDlIm23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlIm23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 15 ])

lamDlIm31 = Parameter(name = 'lamDlIm31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlIm31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 16 ])

lamDlIm32 = Parameter(name = 'lamDlIm32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlIm32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 17 ])

lamDlIm33 = Parameter(name = 'lamDlIm33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamDlIm33}',
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

MXD1 = Parameter(name = 'MXD1',
                 nature = 'external',
                 type = 'real',
                 value = 300,
                 texname = '\\text{MXD1}',
                 lhablock = 'MASS',
                 lhacode = [ 9000005 ])

MXD2 = Parameter(name = 'MXD2',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{MXD2}',
                 lhablock = 'MASS',
                 lhacode = [ 9000006 ])

MXD3 = Parameter(name = 'MXD3',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{MXD3}',
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

wXD1 = Parameter(name = 'wXD1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXD1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000005 ])

wXD2 = Parameter(name = 'wXD2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXD2}',
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

lamDlRe1x1 = Parameter(name = 'lamDlRe1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlRe11',
                       texname = '\\text{lamDlRe1x1}')

lamDlRe1x2 = Parameter(name = 'lamDlRe1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlRe12',
                       texname = '\\text{lamDlRe1x2}')

lamDlRe1x3 = Parameter(name = 'lamDlRe1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlRe13',
                       texname = '\\text{lamDlRe1x3}')

lamDlRe2x1 = Parameter(name = 'lamDlRe2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlRe21',
                       texname = '\\text{lamDlRe2x1}')

lamDlRe2x2 = Parameter(name = 'lamDlRe2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlRe22',
                       texname = '\\text{lamDlRe2x2}')

lamDlRe2x3 = Parameter(name = 'lamDlRe2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlRe23',
                       texname = '\\text{lamDlRe2x3}')

lamDlRe3x1 = Parameter(name = 'lamDlRe3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlRe31',
                       texname = '\\text{lamDlRe3x1}')

lamDlRe3x2 = Parameter(name = 'lamDlRe3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlRe32',
                       texname = '\\text{lamDlRe3x2}')

lamDlRe3x3 = Parameter(name = 'lamDlRe3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlRe33',
                       texname = '\\text{lamDlRe3x3}')

lamDlIm1x1 = Parameter(name = 'lamDlIm1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlIm11',
                       texname = '\\text{lamDlIm1x1}')

lamDlIm1x2 = Parameter(name = 'lamDlIm1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlIm12',
                       texname = '\\text{lamDlIm1x2}')

lamDlIm1x3 = Parameter(name = 'lamDlIm1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlIm13',
                       texname = '\\text{lamDlIm1x3}')

lamDlIm2x1 = Parameter(name = 'lamDlIm2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlIm21',
                       texname = '\\text{lamDlIm2x1}')

lamDlIm2x2 = Parameter(name = 'lamDlIm2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlIm22',
                       texname = '\\text{lamDlIm2x2}')

lamDlIm2x3 = Parameter(name = 'lamDlIm2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlIm23',
                       texname = '\\text{lamDlIm2x3}')

lamDlIm3x1 = Parameter(name = 'lamDlIm3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlIm31',
                       texname = '\\text{lamDlIm3x1}')

lamDlIm3x2 = Parameter(name = 'lamDlIm3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlIm32',
                       texname = '\\text{lamDlIm3x2}')

lamDlIm3x3 = Parameter(name = 'lamDlIm3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamDlIm33',
                       texname = '\\text{lamDlIm3x3}')

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

