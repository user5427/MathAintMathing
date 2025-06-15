11. Paaiškinkite, kokie atsitiktiniai dydžiai pasiskirstę pagal Studento desni su n laisves
laipsniu. Nubrežkite tokiu dydžiu tankio grafiko eskizą.


11. Paaiškinimas: Studento (t) skirstinys su n laisvės laipsnių
🔹 Kas yra Studento skirstinys?

Studento (dar vadinamas t-skirstiniu) skirstinys naudojamas tada, kai:

    Atliekame hipotezių tikrinimą, ypač kai imties dydis mažas (dažnai n < 30),

    Populiacijos standartinis nuokrypis nežinomas, todėl jį pakeičiame imties standartiniu nuokrypiu.

Šis skirstinys priklauso nuo n laisvės laipsnių – tai dažniausiai imties dydis minus vienas (n = m – 1, kur m – imties dydis).
🔹 Atsitiktiniai dydžiai, pasiskirstę pagal Studento skirstinį

Tarkime:

    X1,X2,…,XnX1​,X2​,…,Xn​ – nepriklausomi ir normaliai pasiskirstę dydžiai su nežinoma dispersija,

    Tuomet imties vidurkis XˉXˉ ir standartinis nuokrypis SS naudojami sudarant šį dydį:

T=Xˉ−μS/n
T=S/n
​Xˉ−μ​

Šis atsitiktinis dydis TT pasiskirstęs pagal t-skirstinį su n – 1 laisvės laipsniu.

Arba bendriau:
T=ZV/n∼tn
T=V/n
​Z​∼tn​

Kur:

    Z∼N(0,1)Z∼N(0,1),

    V∼χn2V∼χn2​ – chi kvadrato pasiskirstymas su nn laisvės laipsnių,

    ZZ ir VV yra nepriklausomi.

🔹 Studento t-skirstinio savybės

    Simetriškas apie nulį,

    Turi storesnes uodegas nei normalusis skirstinys (didesnė tikimybė ekstremaliems rezultatams),

    Kai n→∞n→∞, t-skirstinys artėja prie standartinio normalaus skirstinio N(0,1)N(0,1).

🔹 Tankio funkcijos eskizas

Čia pateikiamas eskizinis tankio grafikas t-skirstiniui su skirtingais laisvės laipsniais:

Tankio funkcijos grafiko forma (rankiniu būdu):

            |
          * |        t(1)
         *  |
        *   |
       *    |          t(5)
     **     |
   **       |
 **         |                     t(30)
*-----------|-------------------------
      -3   0    3      t ašis
https://www.geeksforgeeks.org/students-t-distribution-in-statistics/

    t(1) – storesnės uodegos, smailesnis,

    t(30) – labai artimas normaliam skirstiniui.