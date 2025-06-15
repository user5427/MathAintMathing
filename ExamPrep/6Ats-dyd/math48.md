48. Atsitiktiniai dydžiai X1, X2, X3 yra nepriklausomi, X1 ∼ B(10; 0,7), X2 ∼ N (1; 3), E[X3] = 1.
Kam lygus vidurkis E[X1X2 + 3X1X3]?

E[X1X2 + 3X1X3] = E[X1X2] + E[3X1X3]
E[X1X2] = E[X1] * E[X2] // because X1 and X2 are independent
E[X1] = 10 * 0.7 = 7
E[X2] = 1 // because X2 is normally distributed with mean 1
E[X1X2] = 7 * 1 = 7
E[3X1X3] = 3 * E[X1] * E[X3] // because X1 and X3 are independent
E[X1X3] = E[X1] * E[X3] = 7 * 1 = 7
E[3X1X3] = 3 * 7 = 21
E[X1X2 + 3X1X3] = 7 + 21
E[X1X2 + 3X1X3] = 28.