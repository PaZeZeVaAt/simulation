/********************************************************************************************
* SIDH: an efficient supersingular isogeny cryptography library
* Copyright (c) Microsoft Corporation
*
* Website: https://github.com/microsoft/PQCrypto-SIDH
* Released under MIT license
*
* Abstract: benchmarking/testing isogeny-based key encapsulation mechanism SIKEp434
*********************************************************************************************/ 

#include <stdio.h>
#include <string.h>
#include "test_extras.h"
#include "../src/P751/P751_api.h"
#include "../src/P751/P751_internal.h"

#define SCHEME_NAME    "SIKEp751"

#define crypto_kem_keypair            crypto_kem_keypair_SIKEp751
#define crypto_kem_enc                crypto_kem_enc_SIKEp751
#define crypto_kem_dec                crypto_kem_dec_SIKEp751
#define crypto_kem_dec_leak           crypto_kem_dec_leak_SIKEp751

#include "attack_sike.c"