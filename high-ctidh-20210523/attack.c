#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "fp.h"
#include "primes.h"
#include "csidh.h"
#include "cpucycles.h"

// Bob's secret key
private_key B = {{1, -5, -3, 0, -6, -6, 4, 0, -1, -1, 2, 4, 4, 4, -1, -2, 3, 2, -2, -1, -1, -2, 6, 0, -1, 1, 0, 10, 4, -2, -2, -2, -2, 1, 4, 2, 2, -3, 0, 1, 0, 4, 0, 0, -7, 1, 0, 1, 0, -1, 1, 8, 0, 0, 0, 2, -2, 1, -5, 2, -2, -1, -1, -1, 0, 1, 2, 0, -1, -2, 0, 0, 0, 0}};

void ToFile(const char * filename, const char * mode, byte * a, size_t len)
{
    FILE *f = fopen(filename, mode);
    if (f == NULL)
    {
        fprintf(stderr, "Error opening file!\n");
        exit(EXIT_FAILURE);
    }
    for (size_t i = 0; i < len; i++)
    {
        fwrite(&a[i], 1, 1, f);
    }
    fclose(f);
}

void FromFile(const char * filename, byte * a, size_t len)
{

    FILE *fOut = fopen(filename, "rb");

    if (fOut == NULL)
    {
        fprintf(stderr, "Error opening file!\n");
        exit(EXIT_FAILURE);
    }

    for (size_t i = 0; i < len; i++)
    {
        fread(&a[i], 1, 1, fOut);
    }


    fclose(fOut);
}

void print_priv(private_key pk)
{
    printf("pk = [");
    for (int n = 0; n < primes_num; n++)
    {
        if(n != primes_num - 1)
        {
            printf("%d, ", pk.e[n]);
        } else {
            printf("%d", pk.e[n]);
        }
            

    }
    printf("]\n");
}

#define KEYS 65

private_key priv_bob[KEYS];
public_key pub_bob[KEYS];
private_key priv_alice[KEYS];
public_key action_output[KEYS];

int main(int argc, char *argv[])
{

#ifdef KEYGEN

    if(argc < primes_num + 2)
    {
        printf ("Retry\n");
        return 1;
    }

    private_key sk = {0};

    public_key A;
    uint8_t type = 0;

    // type: plus or minus
    type = strtol(argv[1], NULL, 10);

    // secret key
    for (int i = 0; i < primes_num; i++)
    {
        // printf("%d,", i);
        sk.e[i] = strtol(argv[i + 2], NULL, 10);
    }    
        
    // key gen
    (void) csidh(&A, &base, &sk);

    // save to file
    byte *p = (byte *)&A.A.x.c[0];
    if (type == KEYPLUS)
    {
        ToFile(KEYFILEPLUS, "wb", p, sizeof(public_key));
    }
    else
    {
        ToFile(KEYFILEMINUS, "wb", p, sizeof(public_key));
    }

    return 0;
#else
    public_key A = {0}, ss = {0};
    uint8_t type = 0;

    if(argc != 3)
    {
        printf ("Retry\n");
        return 1;
    }

    // type: plus or minus
    type = strtol(argv[1], NULL, 10);

    // 1st param := which li to attack
    li = strtol(argv[2], NULL, 10);

    // get Alice's pub key
    byte p_out[256];
    if (type == KEYPLUS)
    {
        FromFile(KEYFILEPLUS, p_out, sizeof(public_key));
    }
    else
    {
        FromFile(KEYFILEMINUS, p_out, sizeof(public_key));
    }
    memcpy(A.A.x.c, p_out, sizeof(A));

    (void) csidh(&ss, &A, &B);

    return 0;
#endif


}
