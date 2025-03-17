# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Fri 14 Mar 2025 16:53:03



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

lamSdRe11 = Parameter(name = 'lamSdRe11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdRe11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 1 ])

lamSdRe12 = Parameter(name = 'lamSdRe12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdRe12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 2 ])

lamSdRe13 = Parameter(name = 'lamSdRe13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdRe13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 3 ])

lamSdRe21 = Parameter(name = 'lamSdRe21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdRe21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 4 ])

lamSdRe22 = Parameter(name = 'lamSdRe22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdRe22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 5 ])

lamSdRe23 = Parameter(name = 'lamSdRe23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdRe23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 6 ])

lamSdRe31 = Parameter(name = 'lamSdRe31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdRe31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 7 ])

lamSdRe32 = Parameter(name = 'lamSdRe32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdRe32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 8 ])

lamSdRe33 = Parameter(name = 'lamSdRe33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdRe33}',
                      lhablock = 'FRBlock',
                      lhacode = [ 9 ])

lamSdIm11 = Parameter(name = 'lamSdIm11',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdIm11}',
                      lhablock = 'FRBlock',
                      lhacode = [ 10 ])

lamSdIm12 = Parameter(name = 'lamSdIm12',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdIm12}',
                      lhablock = 'FRBlock',
                      lhacode = [ 11 ])

lamSdIm13 = Parameter(name = 'lamSdIm13',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdIm13}',
                      lhablock = 'FRBlock',
                      lhacode = [ 12 ])

lamSdIm21 = Parameter(name = 'lamSdIm21',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdIm21}',
                      lhablock = 'FRBlock',
                      lhacode = [ 13 ])

lamSdIm22 = Parameter(name = 'lamSdIm22',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdIm22}',
                      lhablock = 'FRBlock',
                      lhacode = [ 14 ])

lamSdIm23 = Parameter(name = 'lamSdIm23',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdIm23}',
                      lhablock = 'FRBlock',
                      lhacode = [ 15 ])

lamSdIm31 = Parameter(name = 'lamSdIm31',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdIm31}',
                      lhablock = 'FRBlock',
                      lhacode = [ 16 ])

lamSdIm32 = Parameter(name = 'lamSdIm32',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdIm32}',
                      lhablock = 'FRBlock',
                      lhacode = [ 17 ])

lamSdIm33 = Parameter(name = 'lamSdIm33',
                      nature = 'external',
                      type = 'real',
                      value = 1,
                      texname = '\\text{lamSdIm33}',
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

MYFd = Parameter(name = 'MYFd',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{MYFd}',
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

WYFd = Parameter(name = 'WYFd',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WYFd}',
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

lamSdRe1x1 = Parameter(name = 'lamSdRe1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdRe11',
                       texname = '\\text{lamSdRe1x1}')

lamSdRe1x2 = Parameter(name = 'lamSdRe1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdRe12',
                       texname = '\\text{lamSdRe1x2}')

lamSdRe1x3 = Parameter(name = 'lamSdRe1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdRe13',
                       texname = '\\text{lamSdRe1x3}')

lamSdRe2x1 = Parameter(name = 'lamSdRe2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdRe21',
                       texname = '\\text{lamSdRe2x1}')

lamSdRe2x2 = Parameter(name = 'lamSdRe2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdRe22',
                       texname = '\\text{lamSdRe2x2}')

lamSdRe2x3 = Parameter(name = 'lamSdRe2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdRe23',
                       texname = '\\text{lamSdRe2x3}')

lamSdRe3x1 = Parameter(name = 'lamSdRe3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdRe31',
                       texname = '\\text{lamSdRe3x1}')

lamSdRe3x2 = Parameter(name = 'lamSdRe3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdRe32',
                       texname = '\\text{lamSdRe3x2}')

lamSdRe3x3 = Parameter(name = 'lamSdRe3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdRe33',
                       texname = '\\text{lamSdRe3x3}')

lamSdIm1x1 = Parameter(name = 'lamSdIm1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdIm11',
                       texname = '\\text{lamSdIm1x1}')

lamSdIm1x2 = Parameter(name = 'lamSdIm1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdIm12',
                       texname = '\\text{lamSdIm1x2}')

lamSdIm1x3 = Parameter(name = 'lamSdIm1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdIm13',
                       texname = '\\text{lamSdIm1x3}')

lamSdIm2x1 = Parameter(name = 'lamSdIm2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdIm21',
                       texname = '\\text{lamSdIm2x1}')

lamSdIm2x2 = Parameter(name = 'lamSdIm2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdIm22',
                       texname = '\\text{lamSdIm2x2}')

lamSdIm2x3 = Parameter(name = 'lamSdIm2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdIm23',
                       texname = '\\text{lamSdIm2x3}')

lamSdIm3x1 = Parameter(name = 'lamSdIm3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdIm31',
                       texname = '\\text{lamSdIm3x1}')

lamSdIm3x2 = Parameter(name = 'lamSdIm3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdIm32',
                       texname = '\\text{lamSdIm3x2}')

lamSdIm3x3 = Parameter(name = 'lamSdIm3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'lamSdIm33',
                       texname = '\\text{lamSdIm3x3}')

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

