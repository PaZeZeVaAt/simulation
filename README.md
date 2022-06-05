# Patient Zero: Zero-Value Attacks on CSIDH and Variants

This repository contains auxiliary material for the paper "Patient Zero: Zero-Value Attacks on CSIDH and Variants".

# Overview

This archive contains the following:

- `high-ctidh-20210523` contains the simulation script `simulation_CTIDH.py` and a slightly modified CSIDH implementation from [here](http://ctidh.isogeny.org/software.html).
- `sqale-csidh-velusqrt-main` contains the simulation script `simulation_SQALE.py` and a slightly modified SQALE implementation from [here](https://github.com/JJChiDguez/sqale-csidh-velusqrt).

# Practical Evaluation

## Attack CTIDH-511
1. build CSIDH-511: ```make attackHW511``` for collecting HW and ```make attackKG511``` for KeyGen
2. start simulation: ```python simulation_CTIDH.py```

## Attack SQALE-2048
1. build SQALE-2048: ```make attack BITS=2048 STYLE=df``` for collecting HW and ```make attack BITS=2048 STYLE=wd2``` for KeyGen.
2. start simulation: ```python simulation_SQALE.py```.
3. build SQALE-2048 with countermeasures: set the global value ```WITH_CM = True```, ```make cm BITS=2048 STYLE=df``` for collecting HW with countermeasures, and restart ```python simulation_SQALE.py```.



# Licenses

Code in this repository that does not indicate otherwise is placed in the public domain.

For the third party code see their licenses:

- [CTIDH](http://ctidh.isogeny.org/): [http://ctidh.isogeny.org/high-ctidh-20210523/AUTHORS.md.html](http://ctidh.isogeny.org/high-ctidh-20210523/AUTHORS.md.html)
- [SQALE](https://github.com/JJChiDguez/sqale-csidh-velusqrt): [https://github.com/JJChiDguez/sqale-csidh-velusqrt/blob/main/LICENSE](https://github.com/JJChiDguez/sqale-csidh-velusqrt/blob/main/LICENSE)
