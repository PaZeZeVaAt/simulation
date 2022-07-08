
#ifndef SIDH_ATTACK_PARTS_H
#define SIDH_ATTACK_PARTS_H

typedef struct { f2elm_t X; f2elm_t Y; f2elm_t Z; } point_full_proj;  // Point representation in full projective XYZ Montgomery coordinates 
typedef point_full_proj point_full_proj_t[1];
// int SAMPLES = 0;


void to_montA(f2elm_t A, f2elm_t const a, f2elm_t const b);

void print_montA(f2elm_t const a, f2elm_t const b);

unsigned int is_f2elm_zero(const f2elm_t x);

void fp2pow(const f2elm_t a, const felm_t exp, f2elm_t c);

int fp2_issquare(const f2elm_t a, f2elm_t b);

unsigned int isinfinity(const point_proj_t P);

unsigned int isequal_proj(const point_proj_t P, const point_proj_t Q);

void toAffine(const f2elm_t A, const point_proj_t P, point_full_proj_t R);

// static void getDiffPoint(const f2elm_t A, const point_full_proj_t R, const point_full_proj_t S, point_proj_t D);

int bits_test(f2elm_t const a, f2elm_t const b);

void Backtracking(unsigned char* PublicKeyA, const unsigned char *GuessedKeyB, const unsigned int iteration, const unsigned int swap);

int EphemeralSecretAgreement_B_extended_leak(const unsigned char* PrivateKeyB, const unsigned char* PublicKeyA, unsigned char* SharedSecretB, unsigned int sike, const unsigned int iteration, int* bitseq);

int NextBit(unsigned char* GuessedKeyB, const unsigned char* sk, const unsigned int iteration);

int LastBit(unsigned char* GuessedKeyB, const unsigned char* PublicKeyB);

#endif