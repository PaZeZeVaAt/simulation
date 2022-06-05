#include <time.h>

#define _C_CODE_
#include "csidh.h"
#include "cycle.h"

// Bob's secret key
priv B = {-1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1};

uint16_t li, num_of_attempts;

// write byte string (key) to a file
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

// read byte string (key) from a file
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
        size_t read = fread(&a[i], 1, 1, fOut);
        if(read != sizeof(byte))
        {
            printf("Error reading file!\n");
            exit(EXIT_FAILURE);
        }
    }


    fclose(fOut);
}

int main(int argc, char *argv[])
{
#ifdef wd2

    if(argc < N + 2)
    {
        printf ("Retry\n");
        return 1;
    }

    priv sk = {0};
    pub A;
    uint8_t type = 0;

    // type: plus or minus
    type = strtol(argv[1], NULL, 10);

    // secret key
    for (int i = 2; i < argc; i++)
        sk[i - 2] = strtol(argv[i], NULL, 10);

    // gen key
    pkgen(A, sk);

    // save to file
    byte *p = (byte *)&A[0];
    if (type == KEYPLUS)
    {
        ToFile(KEYFILEPLUS, "wb", p, sizeof(pub));
    }
    else
    {
        ToFile(KEYFILEMINUS, "wb", p, sizeof(pub));
    }

#else

    if(argc < 3)
    {
        printf ("Retry\n");
        return 1;
    }

    pub A = {0}, ss = {0};

    uint8_t type = 0;

    // type: plus or minus
    type = strtol(argv[1], NULL, 10);

    // 1st param := which li to attack
    li = strtol(argv[2], NULL, 10);

    // get Alice's pub key
    byte p_out[256];
    if (type == KEYPLUS)
    {
        FromFile(KEYFILEPLUS, p_out, sizeof(pub));
    }
    else
    {
        FromFile(KEYFILEMINUS, p_out, sizeof(pub));
    }
    memcpy(A, p_out, sizeof(A));


    gae(ss, B, A);

    

#endif
    return 0;
}
