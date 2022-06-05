#ifndef CSIDH_H
#define CSIDH_H

#include "uintbig.h"
#include "fp.h"
#include "mont.h"
#include "primes.h"
#include "csidh_namespace.h"

#define KEYFILEPLUS "keyplus.txt"
#define KEYFILEMINUS "keyminus.txt"
#define KEYPLUS 88
#define KEYMINUS 99

extern uint16_t li;
extern uint16_t num_of_attempts;
extern bool attack_done;

typedef unsigned char byte;


extern long long csidh_stattried[primes_batches];
extern long long csidh_statsucceeded[primes_batches];

typedef struct private_key {
    int8_t e[primes_num];
} private_key;

typedef struct public_key {
    fp A; /* Montgomery coefficient: represents y^2 = x^3 + Ax^2 + x */
} public_key;

extern const public_key base;

void csidh_private(private_key *priv);

bool csidh(public_key *out, public_key const *in, private_key const *priv);

int validate_cutofforder_v2(uintbig *order,const fp *P,const fp *A);
bool validate(public_key const *in);

void action(public_key *out, public_key const *in, private_key const *priv);

#endif
