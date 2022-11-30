# Patient Zero & Patient Six: Zero-Value and Correlation Attacks on CSIDH and SIKE

This repository contains auxiliary material for the paper ["Patient Zero & Patient Six: Zero-Value and Correlation Attacks on CSIDH and SIKE"](https://eprint.iacr.org/2022/904) which was accepted to [SAC 2022](https://www.sac2022.ca/).

# Overview

This archive contains the following:

- `PQCrypto-SIDH` contains the simulation and the modified SIKE implementation from [here](https://github.com/microsoft/PQCrypto-SIDH). Furthermore, it uses an adapted version of the [backtracking](https://github.com/FaultyIsogenies/faulty-isogeny-code/blob/main/sidh_attack.c#L278) code from the [Faulty Isogenies](https://github.com/FaultyIsogenies/faulty-isogeny-code) repository.
- `high-ctidh-20210523` contains the simulation script `simulation_CTIDH.py` and a slightly modified CTIDH implementation from [here](http://ctidh.isogeny.org/software.html).
- `sqale-csidh-velusqrt-main` contains the simulation script `simulation_SQALE.py` and a slightly modified SQALE implementation from [here](https://github.com/JJChiDguez/sqale-csidh-velusqrt).

# Practical Evaluation

## Attack SIKEp434, SIKEp503, SIKEp610, SIKEp751
1. ```cd PQCrypto-SIDH```
2. build all SIKE versions: ```make attack``` 
3. start simulation: e.g. ```./sike434/attack_SIKE``` for attacking SIKEp434

## Attack CTIDH-511
1. ```cd high-ctidh-20210523```
2. build CSIDH-511: ```make attackHW511``` for collecting HW and ```make attackKG511``` for KeyGen
3. start simulation: ```python simulation_CTIDH.py```

## Attack SQALE-2048
1. ```cd sqale-csidh-velusqrt-main```
2. build SQALE-2048: ```make attack BITS=2048 STYLE=df``` for collecting HW and ```make attack BITS=2048 STYLE=wd2``` for KeyGen.
3. start simulation: ```python simulation_SQALE.py```.
4. build SQALE-2048 with countermeasures: set in file ```simulation_SQALE.py``` the global value ```WITH_CM = True```, ```make cm BITS=2048 STYLE=df``` for collecting HW with countermeasures, and restart ```python simulation_SQALE.py```.



# Licenses

Code in this repository that does not indicate otherwise is placed in the public domain.

For the third party code see their licenses:


- [SIKE](https://github.com/microsoft/PQCrypto-SIDH): [https://github.com/microsoft/PQCrypto-SIDH/blob/master/LICENSE](https://github.com/microsoft/PQCrypto-SIDH/blob/master/LICENSE)
- [CTIDH](http://ctidh.isogeny.org/): [http://ctidh.isogeny.org/high-ctidh-20210523/AUTHORS.md.html](http://ctidh.isogeny.org/high-ctidh-20210523/AUTHORS.md.html)
- [SQALE](https://github.com/JJChiDguez/sqale-csidh-velusqrt): [https://github.com/JJChiDguez/sqale-csidh-velusqrt/blob/main/LICENSE](https://github.com/JJChiDguez/sqale-csidh-velusqrt/blob/main/LICENSE)
