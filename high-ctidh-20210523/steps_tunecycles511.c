#include "steps.h"

int steps_guess(long long *bs,long long *gs,long long l)
{
  /* l=3: bs=0 gs=0 bench=3591 baseline=3154 */
  /* l=5: bs=0 gs=0 bench=4351 baseline=4028 */
  /* l=7: bs=0 gs=0 bench=6175 baseline=5605 */
  /* l=11: bs=0 gs=0 bench=8607 baseline=8493 */
  /* l=13: bs=0 gs=0 bench=10013 baseline=9500 */
  /* l=17: bs=0 gs=0 bench=12312 baseline=12179 */
  /* l=19: bs=0 gs=0 bench=14288 baseline=13642 */
  /* l=23: bs=0 gs=0 bench=17005 baseline=17100 */
  /* l=29: bs=0 gs=0 bench=21337 baseline=21204 */
  /* l=31: bs=0 gs=0 bench=21774 baseline=21888 */
  /* l=37: bs=0 gs=0 bench=26657 baseline=26581 */
  /* l=41: bs=0 gs=0 bench=28594 baseline=29203 */
  /* l=43: bs=0 gs=0 bench=31027 baseline=29792 */
  /* l=47: bs=0 gs=0 bench=32642 baseline=32584 */
  /* l=53: bs=0 gs=0 bench=37924 baseline=36271 */
  /* l=59: bs=0 gs=0 bench=42427 baseline=42161 */
  /* l=61: bs=0 gs=0 bench=43681 baseline=43339 */
  /* l=67: bs=0 gs=0 bench=46778 baseline=45561 */
  /* l=71: bs=0 gs=0 bench=51395 baseline=50027 */
  /* l=73: bs=0 gs=0 bench=50882 baseline=51413 */
  /* l=79: bs=0 gs=0 bench=55214 baseline=53713 */
  /* l=83: bs=0 gs=0 bench=57608 baseline=56107 */
  /* l=89: bs=0 gs=0 bench=61674 baseline=62471 */
  /* l=97: bs=0 gs=0 bench=69369 baseline=65360 */
  /* l=101: bs=0 gs=0 bench=72181 baseline=72238 */
  /* l=103: bs=0 gs=0 bench=71440 baseline=73378 */
  /* l=107: bs=0 gs=0 bench=73720 baseline=75126 */
  /* l=109: bs=0 gs=0 bench=75696 baseline=73833 */
  /* l=113: bs=0 gs=0 bench=77824 baseline=75772 */
  /* l=127: bs=0 gs=0 bench=87248 baseline=85784 */
  /* l=131: bs=0 gs=0 bench=90136 baseline=87685 */
  /* l=137: bs=0 gs=0 bench=94012 baseline=91769 */
  /* l=139: bs=0 gs=0 bench=95361 baseline=96387 */
  /* l=149: bs=0 gs=0 bench=105602 baseline=99560 */
  if (l <= 149) { *bs = 0; *gs = 0; return 1; }
  /* l=151: bs=2 gs=1 bench=110029 baseline=101251 */
  if (l <= 151) { *bs = 2; *gs = 1; return 1; }
  /* l=157: bs=0 gs=0 bench=111340 baseline=105051 */
  /* l=163: bs=0 gs=0 bench=116109 baseline=108889 */
  /* l=167: bs=0 gs=0 bench=118731 baseline=113069 */
  /* l=173: bs=0 gs=0 bench=120042 baseline=120840 */
  /* l=179: bs=0 gs=0 bench=127490 baseline=124393 */
  /* l=181: bs=0 gs=0 bench=123747 baseline=125723 */
  /* l=191: bs=0 gs=0 bench=130435 baseline=132430 */
  /* l=193: bs=0 gs=0 bench=132012 baseline=128060 */
  /* l=197: bs=0 gs=0 bench=134482 baseline=136211 */
  /* l=199: bs=0 gs=0 bench=141189 baseline=133608 */
  /* l=211: bs=0 gs=0 bench=144856 baseline=141588 */
  if (l <= 211) { *bs = 0; *gs = 0; return 1; }
  /* l=223: bs=10 gs=5 bench=157548 baseline=148808 */
  if (l <= 223) { *bs = 10; *gs = 5; return 1; }
  /* l=227: bs=0 gs=0 bench=155667 baseline=157130 */
  /* l=229: bs=0 gs=0 bench=156465 baseline=153938 */
  /* l=233: bs=0 gs=0 bench=165585 baseline=160645 */
  /* l=239: bs=0 gs=0 bench=169784 baseline=165851 */
  /* l=241: bs=0 gs=0 bench=174059 baseline=165661 */
  /* l=251: bs=0 gs=0 bench=191368 baseline=180348 */
  if (l <= 251) { *bs = 0; *gs = 0; return 1; }
  /* l=257: bs=10 gs=6 bench=190380 baseline=204288 */
  /* l=263: bs=10 gs=6 bench=185649 baseline=189563 */
  /* l=269: bs=10 gs=6 bench=193667 baseline=203452 */
  /* l=271: bs=10 gs=6 bench=201343 baseline=195491 */
  if (l <= 271) { *bs = 10; *gs = 6; return 1; }
  /* l=277: bs=8 gs=4 bench=199690 baseline=200735 */
  if (l <= 277) { *bs = 8; *gs = 4; return 1; }
  /* l=281: bs=10 gs=7 bench=195947 baseline=199025 */
  /* l=283: bs=10 gs=7 bench=193685 baseline=196099 */
  /* l=293: bs=10 gs=7 bench=197144 baseline=205447 */
  if (l <= 293) { *bs = 10; *gs = 7; return 1; }
  /* l=307: bs=0 gs=0 bench=216847 baseline=210444 */
  if (l <= 307) { *bs = 0; *gs = 0; return 1; }
  /* l=311: bs=10 gs=7 bench=223117 baseline=245271 */
  if (l <= 311) { *bs = 10; *gs = 7; return 1; }
  /* l=313: bs=12 gs=6 bench=215783 baseline=226860 */
  /* l=317: bs=12 gs=6 bench=213313 baseline=217683 */
  if (l <= 317) { *bs = 12; *gs = 6; return 1; }
  /* l=331: bs=10 gs=8 bench=218652 baseline=227297 */
  if (l <= 331) { *bs = 10; *gs = 8; return 1; }
  /* l=337: bs=12 gs=7 bench=217379 baseline=226822 */
  /* l=347: bs=12 gs=7 bench=223573 baseline=247703 */
  /* l=349: bs=12 gs=7 bench=224162 baseline=234536 */
  if (l <= 349) { *bs = 12; *gs = 7; return 1; }
  /* l=353: bs=10 gs=8 bench=229824 baseline=243637 */
  if (l <= 353) { *bs = 10; *gs = 8; return 1; }
  /* l=359: bs=12 gs=7 bench=234840 baseline=246487 */
  /* l=367: bs=12 gs=7 bench=238241 baseline=251066 */
  /* l=373: bs=12 gs=7 bench=239761 baseline=257127 */
  if (l <= 373) { *bs = 12; *gs = 7; return 1; }
  /* l=587: bs=14 gs=10 bench=347263 baseline=394440 */
  if (l <= 587) { *bs = 14; *gs = 10; return 1; }
  return 0;
}
