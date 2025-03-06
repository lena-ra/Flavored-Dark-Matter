# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.0 for Mac OS X ARM (64-bit) (December 3, 2021)
# Date: Thu 6 Mar 2025 15:32:27


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-0.5*ee**2/cw',
                order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = 'ee**2/(2.*cw)',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-G',
                 order = {'QCD':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-2*complex(0,1)*lam',
                 order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-4*complex(0,1)*lam',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '2*complex(0,1)*lam2Sl',
                 order = {'NP':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '4*complex(0,1)*lam2Sl',
                 order = {'NP':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '6*complex(0,1)*lam2Sl',
                 order = {'NP':1})

GC_19 = Coupling(name = 'GC_19',
                 value = 'complex(0,1)*lamHSl1',
                 order = {'NP':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'complex(0,1)*lamHSl1 + complex(0,1)*lamHSl2',
                 order = {'NP':1})

GC_21 = Coupling(name = 'GC_21',
                 value = 'lamHSl2/2. - lamHSl3/2.',
                 order = {'NP':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-0.5*(complex(0,1)*lamHSl2) - (complex(0,1)*lamHSl3)/2.',
                 order = {'NP':1})

GC_23 = Coupling(name = 'GC_23',
                 value = 'complex(0,1)*lamHSl1 - complex(0,1)*lamHSl3',
                 order = {'NP':1})

GC_24 = Coupling(name = 'GC_24',
                 value = 'complex(0,1)*lamHSl1 + complex(0,1)*lamHSl3',
                 order = {'NP':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-0.5*lamHSl2 + lamHSl3/2.',
                 order = {'NP':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(complex(0,1)*lamHSl3)',
                 order = {'NP':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '-2*complex(0,1)*lamHSl3',
                 order = {'NP':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '-ImlSld1x1 + complex(0,1)*RelSld1x1',
                 order = {'NP':1})

GC_29 = Coupling(name = 'GC_29',
                 value = 'ImlSld1x1 + complex(0,1)*RelSld1x1',
                 order = {'NP':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-((complex(0,1)*ImlSld1x1)/cmath.sqrt(2)) - RelSld1x1/cmath.sqrt(2)',
                 order = {'NP':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '-(ImlSld1x1/cmath.sqrt(2)) + (complex(0,1)*RelSld1x1)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_32 = Coupling(name = 'GC_32',
                 value = 'ImlSld1x1/cmath.sqrt(2) + (complex(0,1)*RelSld1x1)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '-((complex(0,1)*ImlSld1x1)/cmath.sqrt(2)) + RelSld1x1/cmath.sqrt(2)',
                 order = {'NP':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '-ImlSld1x2 + complex(0,1)*RelSld1x2',
                 order = {'NP':1})

GC_35 = Coupling(name = 'GC_35',
                 value = 'ImlSld1x2 + complex(0,1)*RelSld1x2',
                 order = {'NP':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-((complex(0,1)*ImlSld1x2)/cmath.sqrt(2)) - RelSld1x2/cmath.sqrt(2)',
                 order = {'NP':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '-(ImlSld1x2/cmath.sqrt(2)) + (complex(0,1)*RelSld1x2)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_38 = Coupling(name = 'GC_38',
                 value = 'ImlSld1x2/cmath.sqrt(2) + (complex(0,1)*RelSld1x2)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-((complex(0,1)*ImlSld1x2)/cmath.sqrt(2)) + RelSld1x2/cmath.sqrt(2)',
                 order = {'NP':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-ImlSld1x3 + complex(0,1)*RelSld1x3',
                 order = {'NP':1})

GC_41 = Coupling(name = 'GC_41',
                 value = 'ImlSld1x3 + complex(0,1)*RelSld1x3',
                 order = {'NP':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-((complex(0,1)*ImlSld1x3)/cmath.sqrt(2)) - RelSld1x3/cmath.sqrt(2)',
                 order = {'NP':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-(ImlSld1x3/cmath.sqrt(2)) + (complex(0,1)*RelSld1x3)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_44 = Coupling(name = 'GC_44',
                 value = 'ImlSld1x3/cmath.sqrt(2) + (complex(0,1)*RelSld1x3)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-((complex(0,1)*ImlSld1x3)/cmath.sqrt(2)) + RelSld1x3/cmath.sqrt(2)',
                 order = {'NP':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-ImlSld2x1 + complex(0,1)*RelSld2x1',
                 order = {'NP':1})

GC_47 = Coupling(name = 'GC_47',
                 value = 'ImlSld2x1 + complex(0,1)*RelSld2x1',
                 order = {'NP':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((complex(0,1)*ImlSld2x1)/cmath.sqrt(2)) - RelSld2x1/cmath.sqrt(2)',
                 order = {'NP':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(ImlSld2x1/cmath.sqrt(2)) + (complex(0,1)*RelSld2x1)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_50 = Coupling(name = 'GC_50',
                 value = 'ImlSld2x1/cmath.sqrt(2) + (complex(0,1)*RelSld2x1)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-((complex(0,1)*ImlSld2x1)/cmath.sqrt(2)) + RelSld2x1/cmath.sqrt(2)',
                 order = {'NP':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-ImlSld2x2 + complex(0,1)*RelSld2x2',
                 order = {'NP':1})

GC_53 = Coupling(name = 'GC_53',
                 value = 'ImlSld2x2 + complex(0,1)*RelSld2x2',
                 order = {'NP':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-((complex(0,1)*ImlSld2x2)/cmath.sqrt(2)) - RelSld2x2/cmath.sqrt(2)',
                 order = {'NP':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '-(ImlSld2x2/cmath.sqrt(2)) + (complex(0,1)*RelSld2x2)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_56 = Coupling(name = 'GC_56',
                 value = 'ImlSld2x2/cmath.sqrt(2) + (complex(0,1)*RelSld2x2)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-((complex(0,1)*ImlSld2x2)/cmath.sqrt(2)) + RelSld2x2/cmath.sqrt(2)',
                 order = {'NP':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-ImlSld2x3 + complex(0,1)*RelSld2x3',
                 order = {'NP':1})

GC_59 = Coupling(name = 'GC_59',
                 value = 'ImlSld2x3 + complex(0,1)*RelSld2x3',
                 order = {'NP':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-((complex(0,1)*ImlSld2x3)/cmath.sqrt(2)) - RelSld2x3/cmath.sqrt(2)',
                 order = {'NP':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(ImlSld2x3/cmath.sqrt(2)) + (complex(0,1)*RelSld2x3)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_62 = Coupling(name = 'GC_62',
                 value = 'ImlSld2x3/cmath.sqrt(2) + (complex(0,1)*RelSld2x3)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-((complex(0,1)*ImlSld2x3)/cmath.sqrt(2)) + RelSld2x3/cmath.sqrt(2)',
                 order = {'NP':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-ImlSld3x1 + complex(0,1)*RelSld3x1',
                 order = {'NP':1})

GC_65 = Coupling(name = 'GC_65',
                 value = 'ImlSld3x1 + complex(0,1)*RelSld3x1',
                 order = {'NP':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-((complex(0,1)*ImlSld3x1)/cmath.sqrt(2)) - RelSld3x1/cmath.sqrt(2)',
                 order = {'NP':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(ImlSld3x1/cmath.sqrt(2)) + (complex(0,1)*RelSld3x1)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_68 = Coupling(name = 'GC_68',
                 value = 'ImlSld3x1/cmath.sqrt(2) + (complex(0,1)*RelSld3x1)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-((complex(0,1)*ImlSld3x1)/cmath.sqrt(2)) + RelSld3x1/cmath.sqrt(2)',
                 order = {'NP':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-ImlSld3x2 + complex(0,1)*RelSld3x2',
                 order = {'NP':1})

GC_71 = Coupling(name = 'GC_71',
                 value = 'ImlSld3x2 + complex(0,1)*RelSld3x2',
                 order = {'NP':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '-((complex(0,1)*ImlSld3x2)/cmath.sqrt(2)) - RelSld3x2/cmath.sqrt(2)',
                 order = {'NP':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-(ImlSld3x2/cmath.sqrt(2)) + (complex(0,1)*RelSld3x2)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_74 = Coupling(name = 'GC_74',
                 value = 'ImlSld3x2/cmath.sqrt(2) + (complex(0,1)*RelSld3x2)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-((complex(0,1)*ImlSld3x2)/cmath.sqrt(2)) + RelSld3x2/cmath.sqrt(2)',
                 order = {'NP':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-ImlSld3x3 + complex(0,1)*RelSld3x3',
                 order = {'NP':1})

GC_77 = Coupling(name = 'GC_77',
                 value = 'ImlSld3x3 + complex(0,1)*RelSld3x3',
                 order = {'NP':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-((complex(0,1)*ImlSld3x3)/cmath.sqrt(2)) - RelSld3x3/cmath.sqrt(2)',
                 order = {'NP':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-(ImlSld3x3/cmath.sqrt(2)) + (complex(0,1)*RelSld3x3)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_80 = Coupling(name = 'GC_80',
                 value = 'ImlSld3x3/cmath.sqrt(2) + (complex(0,1)*RelSld3x3)/cmath.sqrt(2)',
                 order = {'NP':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '-((complex(0,1)*ImlSld3x3)/cmath.sqrt(2)) + RelSld3x3/cmath.sqrt(2)',
                 order = {'NP':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '-0.5*ee/sw',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-0.5*(ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '-0.5*ee**2/sw',
                  order = {'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = '-0.5*(ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = 'ee**2/(2.*sw)',
                  order = {'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '(ee*complex(0,1)*sw)/(3.*cw)',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(ee*complex(0,1)*sw)/cw',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-0.5*(cw*ee)/sw - (ee*sw)/(2.*cw)',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '(cw*ee)/(2.*sw) + (ee*sw)/(2.*cw)',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                  order = {'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_117 = Coupling(name = 'GC_117',
                  value = '-0.5*(ee**2*vev)/cw',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '(ee**2*vev)/(2.*cw)',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-2*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-6*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-(complex(0,1)*lamHSl3*vev)',
                  order = {'NP':1,'QED':-1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-0.25*(ee**2*vev)/sw**2',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '-0.25*(ee**2*complex(0,1)*vev)/sw**2',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '(ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '-0.5*(ee**2*vev)/sw',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = 'complex(0,1)*lamHSl1*vev + complex(0,1)*lamHSl2*vev',
                  order = {'NP':1,'QED':-1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(lamHSl2*vev)/2. - (lamHSl3*vev)/2.',
                  order = {'NP':1,'QED':-1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-0.5*(complex(0,1)*lamHSl2*vev) - (complex(0,1)*lamHSl3*vev)/2.',
                  order = {'NP':1,'QED':-1})

GC_131 = Coupling(name = 'GC_131',
                  value = 'complex(0,1)*lamHSl1*vev - complex(0,1)*lamHSl3*vev',
                  order = {'NP':1,'QED':-1})

GC_132 = Coupling(name = 'GC_132',
                  value = 'complex(0,1)*lamHSl1*vev + complex(0,1)*lamHSl3*vev',
                  order = {'NP':1,'QED':-1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-0.5*(lamHSl2*vev) + (lamHSl3*vev)/2.',
                  order = {'NP':1,'QED':-1})

GC_134 = Coupling(name = 'GC_134',
                  value = '-0.25*(ee**2*vev)/cw - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '-0.25*(ee**2*vev)/cw + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-0.5*(ee**2*complex(0,1)*vev) - (cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '-(yb/cmath.sqrt(2))',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '-(CKM1x3*yb)',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-(CKM2x3*yb)',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '-(CKM3x3*yb)',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '-(yc/cmath.sqrt(2))',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = 'yc/cmath.sqrt(2)',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = 'CKM2x1*yc',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = 'CKM2x2*yc',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = 'CKM2x3*yc',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '-(ydo/cmath.sqrt(2))',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-(CKM1x1*ydo)',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '-(CKM2x1*ydo)',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '-(CKM3x1*ydo)',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '-ye',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = 'ye',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '-(ye/cmath.sqrt(2))',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '-ym',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = 'ym',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-(ym/cmath.sqrt(2))',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '-(ys/cmath.sqrt(2))',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '-(CKM1x2*ys)',
                  order = {'QED':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-(CKM2x2*ys)',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '-(CKM3x2*ys)',
                  order = {'QED':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-(yt/cmath.sqrt(2))',
                  order = {'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_171 = Coupling(name = 'GC_171',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_172 = Coupling(name = 'GC_172',
                  value = 'CKM3x1*yt',
                  order = {'QED':1})

GC_173 = Coupling(name = 'GC_173',
                  value = 'CKM3x2*yt',
                  order = {'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = 'CKM3x3*yt',
                  order = {'QED':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-ytau',
                  order = {'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = 'ytau',
                  order = {'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '-(yup/cmath.sqrt(2))',
                  order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = 'yup/cmath.sqrt(2)',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = 'CKM1x1*yup',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = 'CKM1x2*yup',
                  order = {'QED':1})

GC_184 = Coupling(name = 'GC_184',
                  value = 'CKM1x3*yup',
                  order = {'QED':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_186 = Coupling(name = 'GC_186',
                  value = 'ydo*complexconjugate(CKM1x1)',
                  order = {'QED':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '-(yup*complexconjugate(CKM1x1))',
                  order = {'QED':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_189 = Coupling(name = 'GC_189',
                  value = 'ys*complexconjugate(CKM1x2)',
                  order = {'QED':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '-(yup*complexconjugate(CKM1x2))',
                  order = {'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = 'yb*complexconjugate(CKM1x3)',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '-(yup*complexconjugate(CKM1x3))',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-(yc*complexconjugate(CKM2x1))',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = 'ydo*complexconjugate(CKM2x1)',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '-(yc*complexconjugate(CKM2x2))',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = 'ys*complexconjugate(CKM2x2)',
                  order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = 'yb*complexconjugate(CKM2x3)',
                  order = {'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '-(yc*complexconjugate(CKM2x3))',
                  order = {'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = 'ydo*complexconjugate(CKM3x1)',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '-(yt*complexconjugate(CKM3x1))',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = 'ys*complexconjugate(CKM3x2)',
                  order = {'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '-(yt*complexconjugate(CKM3x2))',
                  order = {'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_210 = Coupling(name = 'GC_210',
                  value = 'yb*complexconjugate(CKM3x3)',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '-(yt*complexconjugate(CKM3x3))',
                  order = {'QED':1})

