// DO NOT EDIT! generated by ./autogen

#ifndef primes_h
#define primes_h

#include "primes_namespace.h"

#if BITS == 512
#define primes_num 74
#define two_cofactor 2
#define primes_batches 14
#define primes_maxbatchboundplussize 26
#elif BITS == 2048
#define primes_num 226
#define two_cofactor 64
#define primes_batches 25
#define primes_maxbatchboundplussize 15
#else
#error BITS must be 512 or 2048
#endif

extern const long long primes[primes_num];
extern const long long primes_dac[primes_num];
extern const long long primes_daclen[primes_num];
extern const long long primes_batchsize[primes_batches];
extern const long long primes_batchstart[primes_batches];
extern const long long primes_batchstop[primes_batches];
extern const long long primes_batchbound[primes_batches];
extern const long long primes_batchmaxdaclen[primes_batches];

#endif
