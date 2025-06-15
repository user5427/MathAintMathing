14. Atliekami penki polinominės schemos bandymai, kiekviename bandyme galimos trys
baigtys, pirmųjų dviejų baigčių tikimybės p1 = 0,2, p2 = 0,3 bandymų serijoje gauti sėkmių skaičiai
S1, S2, S3. Užrašykite reiškinį tikimybei P (S1 = 2, S2 ⩽ 2) apskaičiuoti.

P(S1 = 2, S2 ≤ 2) = P(S1 = 2, S2 = 0) + P(S1 = 2, S2 = 1) + P(S1 = 2, S2 = 2)

S3 = 5 - S1 - S2
p3 = 1 - p1 - p2 = 0,5

ir tada daug skaičiuojame
P(S1 = 2, S2 = 0) = n! / (k! * l! * (n - k - l)!) * p1^k * p2^l * p3^(n - k - l)
P(S1 = 2, S2 = 1) = n! / (k! * l! * (n - k - l)!) * p1^k * p2^l * p3^(n - k - l)
P(S1 = 2, S2 = 2) = n! / (k! * l! * (n - k - l)!) * p1^k * p2^l * p3^(n - k - l)
n = 5
k = 2
l = 0, 1, 2
p1 = 0.2
p2 = 0.3
p3 = 1 - p1 - p2 = 0.5
P(S1 = 2, S2 = 0) = (5! / (2! * 0! * 3!)) * (0.2^2) * (0.3^0) * (0.5^3) = x
P(S1 = 2, S2 = 1) = (5! / (2! * 1! * 2!)) * (0.2^2) * (0.3^1) * (0.5^2) = y
P(S1 = 2, S2 = 2) = (5! / (2! * 2! * 1!)) * (0.2^2) * (0.3^2) * (0.5^1) = z
P(S1 = 2, S2 ≤ 2) = x + y + z