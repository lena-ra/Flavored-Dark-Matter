# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Fri 14 Mar 2025 16:54:29



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

lamSeRe11 = Parameter(name = 'lamSeRe11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeRe11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 1 ])

lamSeRe12 = Parameter(name = 'lamSeRe12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeRe12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 2 ])

lamSeRe13 = Parameter(name = 'lamSeRe13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeRe13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 3 ])

lamSeRe21 = Parameter(name = 'lamSeRe21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeRe21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 4 ])

lamSeRe22 = Parameter(name = 'lamSeRe22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeRe22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 5 ])

lamSeRe23 = Parameter(name = 'lamSeRe23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeRe23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 6 ])

lamSeRe31 = Parameter(name = 'lamSeRe31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeRe31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 7 ])

lamSeRe32 = Parameter(name = 'lamSeRe32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeRe32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 8 ])

lamSeRe33 = Parameter(name = 'lamSeRe33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeRe33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 9 ])

lamSeIm11 = Parameter(name = 'lamSeIm11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeIm11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 10 ])

lamSeIm12 = Parameter(name = 'lamSeIm12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeIm12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 11 ])

lamSeIm13 = Parameter(name = 'lamSeIm13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeIm13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 12 ])

lamSeIm21 = Parameter(name = 'lamSeIm21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeIm21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 13 ])

lamSeIm22 = Parameter(name = 'lamSeIm22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeIm22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 14 ])

lamSeIm23 = Parameter(name = 'lamSeIm23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeIm23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 15 ])

lamSeIm31 = Parameter(name = 'lamSeIm31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeIm31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 16 ])

lamSeIm32 = Parameter(name = 'lamSeIm32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeIm32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 17 ])

lamSeIm33 = Parameter(name = 'lamSeIm33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSeIm33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 18 ])

lamSHRe11 = Parameter(name = 'lamSHRe11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSHRe11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 19 ])

lamSHRe12 = Parameter(name = 'lamSHRe12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSHRe12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 20 ])

lamSHRe13 = Parameter(name = 'lamSHRe13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSHRe13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 21 ])

lamSHRe22 = Parameter(name = 'lamSHRe22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSHRe22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 22 ])

lamSHRe23 = Parameter(name = 'lamSHRe23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSHRe23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 23 ])

lamSHRe33 = Parameter(name = 'lamSHRe33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSHRe33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 24 ])

lamSHIm12 = Parameter(name = 'lamSHIm12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSHIm12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 25 ])

lamSHIm13 = Parameter(name = 'lamSHIm13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSHIm13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 26 ])

lamSHIm23 = Parameter(name = 'lamSHIm23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSHIm23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 27 ])

lam2S = Parameter(name = 'lam2S',
                  nature = 'external',
                  type = 'real',
                  value = 0.1,
                  texname = '\\text{lam2S}',
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

MXS1 = Parameter(name = 'MXS1',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{MXS1}',
                 lhablock = 'MASS',
                 lhacode = [ 9000005 ])

MXS2 = Parameter(name = 'MXS2',
                 nature = 'external',
                 type = 'real',
                 value = 200,
                 texname = '\\text{MXS2}',
                 lhablock = 'MASS',
                 lhacode = [ 9000006 ])

MXS3 = Parameter(name = 'MXS3',
                 nature = 'external',
                 type = 'real',
                 value = 300,
                 texname = '\\text{MXS3}',
                 lhablock = 'MASS',
                 lhacode = [ 9000007 ])

MYFe = Parameter(name = 'MYFe',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{MYFe}',
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

wXS1 = Parameter(name = 'wXS1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXS1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000005 ])

wXS2 = Parameter(name = 'wXS2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{wXS2}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000006 ])

WYFe = Parameter(name = 'WYFe',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WYFe}',
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

lamSeRe1x1 = Parameter(name = 'lamSeRe1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeRe11',
                       texname = '\\text{lamSeRe1x1}')

lamSeRe1x2 = Parameter(name = 'lamSeRe1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeRe12',
                       texname = '\\text{lamSeRe1x2}')

lamSeRe1x3 = Parameter(name = 'lamSeRe1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeRe13',
                       texname = '\\text{lamSeRe1x3}')

lamSeRe2x1 = Parameter(name = 'lamSeRe2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeRe21',
                       texname = '\\text{lamSeRe2x1}')

lamSeRe2x2 = Parameter(name = 'lamSeRe2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeRe22',
                       texname = '\\text{lamSeRe2x2}')

lamSeRe2x3 = Parameter(name = 'lamSeRe2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeRe23',
                       texname = '\\text{lamSeRe2x3}')

lamSeRe3x1 = Parameter(name = 'lamSeRe3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeRe31',
                       texname = '\\text{lamSeRe3x1}')

lamSeRe3x2 = Parameter(name = 'lamSeRe3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeRe32',
                       texname = '\\text{lamSeRe3x2}')

lamSeRe3x3 = Parameter(name = 'lamSeRe3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeRe33',
                       texname = '\\text{lamSeRe3x3}')

lamSeIm1x1 = Parameter(name = 'lamSeIm1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeIm11',
                       texname = '\\text{lamSeIm1x1}')

lamSeIm1x2 = Parameter(name = 'lamSeIm1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeIm12',
                       texname = '\\text{lamSeIm1x2}')

lamSeIm1x3 = Parameter(name = 'lamSeIm1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeIm13',
                       texname = '\\text{lamSeIm1x3}')

lamSeIm2x1 = Parameter(name = 'lamSeIm2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeIm21',
                       texname = '\\text{lamSeIm2x1}')

lamSeIm2x2 = Parameter(name = 'lamSeIm2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeIm22',
                       texname = '\\text{lamSeIm2x2}')

lamSeIm2x3 = Parameter(name = 'lamSeIm2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeIm23',
                       texname = '\\text{lamSeIm2x3}')

lamSeIm3x1 = Parameter(name = 'lamSeIm3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeIm31',
                       texname = '\\text{lamSeIm3x1}')

lamSeIm3x2 = Parameter(name = 'lamSeIm3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeIm32',
                       texname = '\\text{lamSeIm3x2}')

lamSeIm3x3 = Parameter(name = 'lamSeIm3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSeIm33',
                       texname = '\\text{lamSeIm3x3}')

lamSHRe1x1 = Parameter(name = 'lamSHRe1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSHRe11',
                       texname = '\\text{lamSHRe1x1}')

lamSHRe1x2 = Parameter(name = 'lamSHRe1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSHRe12',
                       texname = '\\text{lamSHRe1x2}')

lamSHRe1x3 = Parameter(name = 'lamSHRe1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSHRe13',
                       texname = '\\text{lamSHRe1x3}')

lamSHRe2x1 = Parameter(name = 'lamSHRe2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSHRe12',
                       texname = '\\text{lamSHRe2x1}')

lamSHRe2x2 = Parameter(name = 'lamSHRe2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSHRe22',
                       texname = '\\text{lamSHRe2x2}')

lamSHRe2x3 = Parameter(name = 'lamSHRe2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSHRe23',
                       texname = '\\text{lamSHRe2x3}')

lamSHRe3x1 = Parameter(name = 'lamSHRe3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSHRe13',
                       texname = '\\text{lamSHRe3x1}')

lamSHRe3x2 = Parameter(name = 'lamSHRe3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSHRe23',
                       texname = '\\text{lamSHRe3x2}')

lamSHRe3x3 = Parameter(name = 'lamSHRe3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSHRe33',
                       texname = '\\text{lamSHRe3x3}')

lamSHIm1x1 = Parameter(name = 'lamSHIm1x1',
                       nature = 'internal',
                       type = 'real',
                       value = '0',
                       texname = '\\text{lamSHIm1x1}')

lamSHIm1x2 = Parameter(name = 'lamSHIm1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSHIm12',
                       texname = '\\text{lamSHIm1x2}')

lamSHIm1x3 = Parameter(name = 'lamSHIm1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSHIm13',
                       texname = '\\text{lamSHIm1x3}')

lamSHIm2x1 = Parameter(name = 'lamSHIm2x1',
                       nature = 'internal',
                       type = 'real',
                       value = '-lamSHIm12',
                       texname = '\\text{lamSHIm2x1}')

lamSHIm2x2 = Parameter(name = 'lamSHIm2x2',
                       nature = 'internal',
                       type = 'real',
                       value = '0',
                       texname = '\\text{lamSHIm2x2}')

lamSHIm2x3 = Parameter(name = 'lamSHIm2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSHIm23',
                       texname = '\\text{lamSHIm2x3}')

lamSHIm3x1 = Parameter(name = 'lamSHIm3x1',
                       nature = 'internal',
                       type = 'real',
                       value = '-lamSHIm13',
                       texname = '\\text{lamSHIm3x1}')

lamSHIm3x2 = Parameter(name = 'lamSHIm3x2',
                       nature = 'internal',
                       type = 'real',
                       value = '-lamSHIm23',
                       texname = '\\text{lamSHIm3x2}')

lamSHIm3x3 = Parameter(name = 'lamSHIm3x3',
                       nature = 'internal',
                       type = 'real',
                       value = '0',
                       texname = '\\text{lamSHIm3x3}')

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

