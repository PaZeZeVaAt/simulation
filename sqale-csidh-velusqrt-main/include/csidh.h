#ifndef _CSIDH_H_
#define _CSIDH_H_

#include "isog.h"

#define KEYFILEPLUS "keyplus.txt"
#define KEYFILEMINUS "keyminus.txt"
#define KEYPLUS 88
#define KEYMINUS 99

extern uint16_t li;
extern uint16_t num_of_attempts;
extern bool attack_done;

typedef unsigned char byte;

typedef int8_t priv[N];	// secret keys corresponds with integer vectors of dimension N
typedef fp pub;		// public keys corresponds with affine Montgomery curve coefficients

void strategy_evaluation(proj B, int8_t e[], proj const *P, proj const A, uint8_t const j, int8_t m[]);	// strategy evaluation
void gae(fp b, int8_t const v[], fp const a);								// group action evaluation

void skgen(priv sk);					// secret key generation
void pkgen(pub pk, priv const sk);			// public key generation
void keygen(pub pk, priv sk);				// key generation (both secret and public keys are generated)
bool derive(pub ss, pub const pk, priv const sk);	// secret sharing derivation

void sk_print(priv const a, char *c);
void pk_print(pub const a, char *c);

// static unsigned long long bytes_to_ull(const unsigned char *in, unsigned int inlen)
// {
//     unsigned long long retval = 0;
//     unsigned int i;

//     for (i = 0; i < inlen; i++) {
//         retval |= ((unsigned long long)in[i]) << (8*(inlen - 1 - i));
//     }
//     return retval;
// }


// static void ull_to_bytes(unsigned char *out, unsigned int outlen,
//                   unsigned long long in)
// {
//     int i;

//     /* Iterate over out in decreasing order, for big-endianness. */
//     for (i = outlen - 1; i >= 0; i--) {
//         out[i] = in & 0xff;
//         in = in >> 8;
//     }
// }

void ToFile(const char * filename, const char * mode, byte * a, size_t len);

void FromFile(const char * filename, byte * a, size_t len);


// ----------------------------------------------------
// ----------------------------------------------------

// decision bit b has to be either 0 or 1
static inline void cmov(int8_t *r, const int8_t a, uint32_t b)
{
        uint32_t t;
        b = -b;                 //  Now b is either 0 or 0xffffffff
        t = (*r ^ a) & b;
        *r ^= t;
}

// check if a and b are equal in constant time
static inline uint32_t isequal(uint32_t a, uint32_t b)
{
        //size_t i;
        uint32_t r = 0;
        unsigned char *ta = (unsigned char *)&a;
        unsigned char *tb = (unsigned char *)&b;
        r = (ta[0] ^ tb[0]) | (ta[1] ^ tb[1]) | (ta[2] ^ tb[2]) |  (ta[3] ^ tb[3]);
        r = (-r);
        r = r >> 31;
        return (uint32_t)(1-r);
}

// get priv[pos] in constant time
static inline uint32_t lookup(size_t pos, int8_t const priv[])
{
        int b;
        int8_t r = priv[0];
        for(size_t i = 1; i < N; i++)
        {
                b = isequal(i, pos);
                cmov(&r, priv[i], b);
        }
        return r;
}

// constant-time comparison: 1 if x < y, 0 otherwise.
static inline int32_t issmaller(int32_t x, int32_t y)
{
        int32_t xy = x ^ y;
        int32_t c = x - y;
        c ^= xy & (c ^ x);
        c = c >> 31;
        return 1 - (uint32_t)(1 + c);
}

// constant-time sign computation
static inline int8_t sign(int8_t const e)
{
        int b;
        int8_t r = 0;

        // Is e a negative integer?
        b = issmaller(e, 0);
        cmov(&r, -1, b);

        // Is e a positive integer?
        b = issmaller(0, e);
        cmov(&r, 1, b);

        return r;       // Now, r has the sign of e
}

// priv[pos] is updated in constant-time with the value in e
static inline void update(size_t pos, int8_t const e, int8_t priv[])
{
        int b;
        for(size_t i = 0; i < N; i++)
        {
                b = isequal(i, pos);
                cmov(&priv[i], e, b);
        }
}

#endif

