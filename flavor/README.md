# Flavor analysis manual

The relevant code for the flavor analysis of the Dark Matter (DM) models can be found in the current directory `flavor`. It is divided into a section on matching the DM models onto the Standard Model Effective Field Theory (SMEFT) in `flavor/matching` and a section on extracting the flavor constraints in `flavor/likelihood`.



## From the DM model to the SMEFT

### Matching with `Matchete`

The matching of the DM models onto the SMEFT is performed at the new physics scale onto the SMEFT with the help of the Mathematica package `Matchete` \[[2212.04510](https://arxiv.org/abs/2212.04510)\]. The model files are stored in the directory `model_files` and the matching can be performed with the notebook `matching.nb`. The results are stored in the directory `results`, which contains three subdirectories:
- `MatchingConditions`: storing the matching conditions of the various models onto the Warsaw basis of the SMEFT in `Matchete` format; 
- `MatchingConditions-pdf`: storing the matching conditions of the various models onto the Warsaw basis of the SMEFT in a human readable PDF format; 
- `SMEFT-Lagrangians-pdf`: storing the SMEFT Lagrangian obtained after the matching of the various models in a human readable PDF format.

Notice that the matching can be performed once and for all and does not have to be repeated for every analysis. The matching results for all models are stored already in the directory `results`. For an analysis one does not have to run the matching again but can simply use the matching conditions provided in `results/MatchingConditions`. The notebook `matching.nb` is only provided for completeness.

*Notice that the matching of models with heavy flavored particles is supported in `Matchete` only from `v0.3.0` onwards, as is the updated model file format used here. However, the WCxf output (discussed below) requires [`v0.4.0`](https://gitlab.com/matchete/matchete/-/tags/v0.4.0).
The latest version of `Matchete` can be installed by evaluating in a Mathematica notebook:*
```
Import["https://gitlab.com/matchete/matchete/-/raw/master/install.m"]
``` 
*For more details see \[[2212.04510](https://arxiv.org/abs/2212.04510)\] and [https://gitlab.com/matchete/matchete](https://gitlab.com/matchete/matchete).*

### Numeric evaluation of matching conditions: `Matchete-WCxf` interface

To determine the flavor constraints on the DM models through parameter scan, the matching conditions have to be evaluated numerically for a given set of BSM parameter values. This is achieved in the notebook `WCxf.nb`, where a table containing values for various BSM parameters points is read in. Example tables can be found in the `*.dat` files in the directory `parameter_files`. These are then converted into the appropriate `JSON` format used by the `Matchete-WCxf` interface as in put. Examples can be found again in the `*.json` files in the directory `parameter_files`. Every parameter point is then passed through the matching conditions, to obtain the corresponding numerical values of the [Warsaw basis](https://arxiv.org/abs/1008.4884) Wilson coefficients. These coefficients are then exported again as a `JSON` file (one file per parameter point as determined by the format) to the directory `WCxf`, following the conventions and notation of the [WCxf format](https://arxiv.org/abs/1712.05298). This is achieved with the new `Matchete-WCxf` export interface created specifically for this project, which can, however, be also used for any other BSM theory that is matched with `Matchete`. As already mentioned, this feature is available since [`v0.4.0`](https://gitlab.com/matchete/matchete/-/tags/v0.4.0) of the `Matchete` code.

## Global likelihood with `smelli`

To determine the flavor constraints on the DM models, we adopt a global likelihood approach employing the python program `smelli` \[[1810.07698](https://arxiv.org/abs/1810.07698)\]. For more details see [https://smelli.github.io](https://smelli.github.io). `smelli` determines the global log likelihood ratio 

<picture>
  <source media="(prefers-color-scheme: dark)"
          srcset="https://latex.codecogs.com/svg.latex?\color{white}\Delta\mathcal{L}=\log\left(\frac{\mathcal{L}_\mathrm{BSM}}{\mathcal{L}_\mathrm{SM}}\right)">
  <img alt="Δℒ = log(L_BSM / L_SM)"
       src="https://latex.codecogs.com/svg.latex?\Delta\mathcal{L}=\log\left(\frac{\mathcal{L}_\mathrm{BSM}}{\mathcal{L}_\mathrm{SM}}\right)">
</picture>

for every parameter point.
Here, <picture><source media="(prefers-color-scheme: dark)" srcset="https://latex.codecogs.com/svg.latex?\color{white}\mathcal{L}_\mathrm{SM}"><img alt="ℒ_SM" src="https://latex.codecogs.com/svg.latex?\mathcal{L}_\mathrm{SM}"></picture> is the global Standard Model (SM) likelihood and <picture><source media="(prefers-color-scheme: dark)" srcset="https://latex.codecogs.com/svg.latex?\color{white}\mathcal{L}_\mathrm{BSM}"><img alt="ℒ_BSM" src="https://latex.codecogs.com/svg.latex?\mathcal{L}_\mathrm{BSM}"></picture> is the global likelihood of any Beyond SM (BSM) model such as the DM theories we consider here.
A wide range of flavor and electroweak precision observables can be included in this likelihood. The list of observables can be found in appendix D of \[[1810.07698](https://arxiv.org/abs/1810.07698)\] or an updated version on [GitHub](https://github.com/smelli/smelli/tree/master/smelli/data/yaml). These observables are computed with the `flavio` package \[[1810.08132](https://arxiv.org/abs/1810.08132)\]. As input `smelli` takes the numerical values all Wilson coefficients at each parameter point in the format of `WCxf` files, which we created before with `Matchete`. Employing the `Wilson` code \[[1804.05033](https://arxiv.org/abs/1804.05033)\], `smelli` then evolves the Wilson coefficients from the input/matching scale down to the electroweak scale using the Renormalization Group Equations (RGEs) of the SMEFT. Then the SMEFT is matched onto the Low Energy Effective Theory (LEFT), and subsequently the LEFT RGEs are used to further evolve all couplings down to the relevant experimental energy scales.

An example Jupyter notebook performing a `smelli` analysis can be found at `likelihood/smelli.ipynb`. It can be easily adapted for analyzing other BSM models. In principle only the variable `model_name` has to be changed to the name of the sub-directory (in `matching/WCxf/`) in which the WCxf files, which should be analyzed, are stored. The results, that is, the likelihoods and the table of observables for all variables, as well as an overview of the most relevant observables, is then exported to the directory `likelihood/model_name/`.

Alternatively, the directory `likelihoods/cluster/` provides python and shell scripts for performing a large analysis on a cluster using the Slurm Workload Manager. While the python scripts do not necessarily have to be modified, several paths in the shell script have to be set appropriately by the user. Afterwards, the job can be submitted executing the shell script by
`source sbatch_jobs.sh`. Notice that the scripts need to be marked as executable (`chmod +x sbatch_jobs.sh`).