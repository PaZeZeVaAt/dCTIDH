#ifndef _CTIDH_API_H_
#define _CTIDH_API_H_

#include "../common/namespace.h"
#include "../common/primes.h"
#include "ctidh.h"
#if defined AVX2
    #include "../common/fp/avx2/fp-avx2.h"
#elif defined GMP
    #include "../common/fp/gmp/fp-gmp.h"
#elif defined KARATSUBA
    #include "../common/fp/karatsuba/fp-karatsuba.h"
#else
    #include "../common/fp/mulx/fp.h"
#endif

extern const size_t NSAPI(pk_size);
extern const size_t NSAPI(sk_size);
extern const size_t NSAPI(ss_size);

#define internal_keygen NS(keygen)
void internal_keygen(public_key* pk, private_key* sk);			// key generation (both secret and public keys are generated)
#define internal_derive NS(derive)
bool internal_derive(fp* ss, public_key* const pk, private_key* const sk);	// secret sharing derivation
#define init_keys NS(init_keys)
void init_keys(public_key** pk, int8_t** sk);
#define skgen NS(skgen)
void skgen(int8_t* sk);					// secret key generation
#define pkgen NS(pkgen)
void pkgen(public_key* pk, int8_t* const sk);			// public key generation
#define free_keys NS(free_keys)
void free_keys(public_key** pk, int8_t** sk);

#endif
