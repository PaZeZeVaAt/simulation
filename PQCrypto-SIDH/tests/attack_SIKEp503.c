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
#include "../src/P503/P503_api.h"
#include "../src/P503/P503_internal.h"

#define SCHEME_NAME    "SIKEp503"

#define crypto_kem_keypair            crypto_kem_keypair_SIKEp503
#define crypto_kem_enc                crypto_kem_enc_SIKEp503
#define crypto_kem_dec                crypto_kem_dec_SIKEp503
#define crypto_kem_dec_leak           crypto_kem_dec_leak_SIKEp503

#include "attack_sike.c"