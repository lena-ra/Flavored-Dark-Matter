# Flavored-Dark-Matter

This repository includes FeynRules, UFO, and CalcHEP model files for 20 different flavored dark matter models in the respective folders. The models are specified by the dark matter particle type (real or complex scalar, Dirac or Majorana fermion) and the SM fermion that the particles couple to. The SM fermions are:

- Right-handed up-type quarks (u)
- Right-handed down-type quarks (d)
- Left-handed quark doublet (q)
- Right-handed leptons (e)
- Left-handed lepton doublet (l)

Different dark matter models can be combined by loading two or more FeynRules model files and adding the respective Lagrangians to produce the UFO or CalcHEP file of this model.

All masses for the dark matter and mediator particles are expected to be given after EWSB. The couplings between the DM field, the mediator and the SM fermions is split into the real and imaginary part (indicated by Re and Im at the end of the variable name). 