39. Tegu X1, X2 yra nepriklausomi atsitiktiniai dydžiai, X1 ∼ P (2), X2 ∼ P (3); Y1 = X_1^2, Y2 = X_2^2.
Kaip apskaičiuoti tikimybę P (Y1 = 1, Y2 > 3) ?

P (Y1 = 1, Y2 > 3) = P(Y1 = 1) * P(Y2 > 3)

P(Y2 > 3) = 1 - P(Y2 ≤ 3)

P(Y2 ≤ 3) = P(X2 = 0) + P(X2 = 1) // this is because X2^2 > 3, X2 > sqrt(3), so X2 must be 2,3,4,...
P(X2 = 0) = (3^0 * e^(-3)) / 0! = e^(-3)
P(X2 = 1) = (3^1 * e^(-3)) / 1! = 3 * e^(-3)
P(Y2 ≤ 3) = P(X2 = 0) + P(X2 = 1)
P(Y2 ≤ 3) = e^(-3) + 3 * e^(-3) = 4 * e^(-3)
P(Y2 > 3) = 1 - P(Y2 ≤ 3)
P(Y2 > 3) = 1 - 4 * e^(-3)
P(Y1 = 1) = P(X1 = 1) = (2^1 * e^(-2)) / 1! = 2 * e^(-2)
P(Y1 = 1, Y2 > 3) = P(Y1 = 1) * P(Y2 > 3)
P(Y1 = 1, Y2 > 3) = (2 * e^(-2)) * (1 - 4 * e^(-3))
P(Y1 = 1, Y2 > 3) = 2 * e^(-2) * (1 - 4 * e^(-3))
P(Y1​=1,Y2​>3)=2e−2(1−4e−3)≈0.2166.