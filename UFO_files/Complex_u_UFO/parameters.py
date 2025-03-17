# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Fri 14 Mar 2025 16:15:52



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

lamCuRe11 = Parameter(name = 'lamCuRe11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuRe11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 1 ])

lamCuRe12 = Parameter(name = 'lamCuRe12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuRe12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 2 ])

lamCuRe13 = Parameter(name = 'lamCuRe13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuRe13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 3 ])

lamCuRe21 = Parameter(name = 'lamCuRe21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuRe21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 4 ])

lamCuRe22 = Parameter(name = 'lamCuRe22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuRe22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 5 ])

lamCuRe23 = Parameter(name = 'lamCuRe23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuRe23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 6 ])

lamCuRe31 = Parameter(name = 'lamCuRe31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuRe31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 7 ])

lamCuRe32 = Parameter(name = 'lamCuRe32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuRe32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 8 ])

lamCuRe33 = Parameter(name = 'lamCuRe33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuRe33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 9 ])

lamCuIm11 = Parameter(name = 'lamCuIm11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuIm11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 10 ])

lamCuIm12 = Parameter(name = 'lamCuIm12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuIm12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 11 ])

lamCuIm13 = Parameter(name = 'lamCuIm13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuIm13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 12 ])

lamCuIm21 = Parameter(name = 'lamCuIm21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuIm21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 13 ])

lamCuIm22 = Parameter(name = 'lamCuIm22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuIm22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 14 ])

lamCuIm23 = Parameter(name = 'lamCuIm23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuIm23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 15 ])

lamCuIm31 = Parameter(name = 'lamCuIm31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuIm31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 16 ])

lamCuIm32 = Parameter(name = 'lamCuIm32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuIm32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 17 ])

lamCuIm33 = Parameter(name = 'lamCuIm33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCuIm33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 18 ])

lamCHRe11 = Parameter(name = 'lamCHRe11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCHRe11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 19 ])

lamCHRe12 = Parameter(name = 'lamCHRe12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCHRe12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 20 ])

lamCHRe13 = Parameter(name = 'lamCHRe13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCHRe13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 21 ])

lamCHRe22 = Parameter(name = 'lamCHRe22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCHRe22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 22 ])

lamCHRe23 = Parameter(name = 'lamCHRe23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCHRe23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 23 ])

lamCHRe33 = Parameter(name = 'lamCHRe33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCHRe33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 24 ])

lamCHIm12 = Parameter(name = 'lamCHIm12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCHIm12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 25 ])

lamCHIm13 = Parameter(name = 'lamCHIm13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCHIm13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 26 ])

lamCHIm23 = Parameter(name = 'lamCHIm23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamCHIm23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 27 ])

lam2C = Parameter(name = 'lam2C',
                  nature = 'external',
                  type = 'real',
                  value = 0.1,
                  texname = '\\text{lam2C}',
                  lhablock = 'FRBlock',
                  lhacode = [ 28 ])

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

MXC1 = Parameter(name = 'MXC1',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{MXC1}',
                 lhablock = 'MASS',
                 lhacode = [ 9000005 ])

MXC2 = Parameter(name = 'MXC2',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{MXC2}',
                 lhablock = 'MASS',
                 lhacode = [ 9000006 ])

MXC3 = Parameter(name = 'MXC3',
                 nature = 'external',
                 type = 'real',
                 value = 300,
                 texname = '\\text{MXC3}',
                 lhablock = 'MASS',
                 lhacode = [ 9000007 ])

MYFu = Parameter(name = 'MYFu',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{MYFu}',
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

wXC1 = Parameter(name = 'wXC1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXC1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000005 ])

wXC2 = Parameter(name = 'wXC2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXC2}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000006 ])

WYFu = Parameter(name = 'WYFu',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WYFu}',
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

lamCuRe1x1 = Parameter(name = 'lamCuRe1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuRe11',
                       texname = '\\text{lamCuRe1x1}')

lamCuRe1x2 = Parameter(name = 'lamCuRe1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuRe12',
                       texname = '\\text{lamCuRe1x2}')

lamCuRe1x3 = Parameter(name = 'lamCuRe1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuRe13',
                       texname = '\\text{lamCuRe1x3}')

lamCuRe2x1 = Parameter(name = 'lamCuRe2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuRe21',
                       texname = '\\text{lamCuRe2x1}')

lamCuRe2x2 = Parameter(name = 'lamCuRe2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuRe22',
                       texname = '\\text{lamCuRe2x2}')

lamCuRe2x3 = Parameter(name = 'lamCuRe2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuRe23',
                       texname = '\\text{lamCuRe2x3}')

lamCuRe3x1 = Parameter(name = 'lamCuRe3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuRe31',
                       texname = '\\text{lamCuRe3x1}')

lamCuRe3x2 = Parameter(name = 'lamCuRe3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuRe32',
                       texname = '\\text{lamCuRe3x2}')

lamCuRe3x3 = Parameter(name = 'lamCuRe3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuRe33',
                       texname = '\\text{lamCuRe3x3}')

lamCuIm1x1 = Parameter(name = 'lamCuIm1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuIm11',
                       texname = '\\text{lamCuIm1x1}')

lamCuIm1x2 = Parameter(name = 'lamCuIm1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuIm12',
                       texname = '\\text{lamCuIm1x2}')

lamCuIm1x3 = Parameter(name = 'lamCuIm1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuIm13',
                       texname = '\\text{lamCuIm1x3}')

lamCuIm2x1 = Parameter(name = 'lamCuIm2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuIm21',
                       texname = '\\text{lamCuIm2x1}')

lamCuIm2x2 = Parameter(name = 'lamCuIm2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuIm22',
                       texname = '\\text{lamCuIm2x2}')

lamCuIm2x3 = Parameter(name = 'lamCuIm2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuIm23',
                       texname = '\\text{lamCuIm2x3}')

lamCuIm3x1 = Parameter(name = 'lamCuIm3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuIm31',
                       texname = '\\text{lamCuIm3x1}')

lamCuIm3x2 = Parameter(name = 'lamCuIm3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuIm32',
                       texname = '\\text{lamCuIm3x2}')

lamCuIm3x3 = Parameter(name = 'lamCuIm3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCuIm33',
                       texname = '\\text{lamCuIm3x3}')

lamCHRe1x1 = Parameter(name = 'lamCHRe1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCHRe11',
                       texname = '\\text{lamCHRe1x1}')

lamCHRe1x2 = Parameter(name = 'lamCHRe1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCHRe12',
                       texname = '\\text{lamCHRe1x2}')

lamCHRe1x3 = Parameter(name = 'lamCHRe1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCHRe13',
                       texname = '\\text{lamCHRe1x3}')

lamCHRe2x1 = Parameter(name = 'lamCHRe2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCHRe12',
                       texname = '\\text{lamCHRe2x1}')

lamCHRe2x2 = Parameter(name = 'lamCHRe2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCHRe22',
                       texname = '\\text{lamCHRe2x2}')

lamCHRe2x3 = Parameter(name = 'lamCHRe2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCHRe23',
                       texname = '\\text{lamCHRe2x3}')

lamCHRe3x1 = Parameter(name = 'lamCHRe3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCHRe13',
                       texname = '\\text{lamCHRe3x1}')

lamCHRe3x2 = Parameter(name = 'lamCHRe3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCHRe23',
                       texname = '\\text{lamCHRe3x2}')

lamCHRe3x3 = Parameter(name = 'lamCHRe3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCHRe33',
                       texname = '\\text{lamCHRe3x3}')

lamCHIm1x1 = Parameter(name = 'lamCHIm1x1',
                       nature = 'internal',
                       type = 'real',
                       value = '0',
                       texname = '\\text{lamCHIm1x1}')

lamCHIm1x2 = Parameter(name = 'lamCHIm1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCHIm12',
                       texname = '\\text{lamCHIm1x2}')

lamCHIm1x3 = Parameter(name = 'lamCHIm1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCHIm13',
                       texname = '\\text{lamCHIm1x3}')

lamCHIm2x1 = Parameter(name = 'lamCHIm2x1',
                       nature = 'internal',
                       type = 'real',
                       value = '-lamCHIm12',
                       texname = '\\text{lamCHIm2x1}')

lamCHIm2x2 = Parameter(name = 'lamCHIm2x2',
                       nature = 'internal',
                       type = 'real',
                       value = '0',
                       texname = '\\text{lamCHIm2x2}')

lamCHIm2x3 = Parameter(name = 'lamCHIm2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamCHIm23',
                       texname = '\\text{lamCHIm2x3}')

lamCHIm3x1 = Parameter(name = 'lamCHIm3x1',
                       nature = 'internal',
                       type = 'real',
                       value = '-lamCHIm13',
                       texname = '\\text{lamCHIm3x1}')

lamCHIm3x2 = Parameter(name = 'lamCHIm3x2',
                       nature = 'internal',
                       type = 'real',
                       value = '-lamCHIm23',
                       texname = '\\text{lamCHIm3x2}')

lamCHIm3x3 = Parameter(name = 'lamCHIm3x3',
                       nature = 'internal',
                       type = 'real',
                       value = '0',
                       texname = '\\text{lamCHIm3x3}')

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

