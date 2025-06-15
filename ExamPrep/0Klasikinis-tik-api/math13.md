13. Parduotuves lentynoje - 15 stikliniu vazu, 6 iš ju nežymiai įskilę.
    Kokia tikimybe, kad nusipirkęs 5 vazas pirkejas gaus bent 3 įskilusias?

[]: # 
[]: # Pirmiausia apskaičiuojame bendrą galimų derinių skaičių, kaip renkamės 5 vaza iš 15:
[]: # C(15, 5) = 3003
[]: # 
[]: # Tada apskaičiuojame derinius, kai gauname bent 3 įskilusias vazas:
[]: # 
[]: # 1. 3 įskilusios ir 2 sveikos:
[]: # C(6, 3) * C(9, 2) = 20 * 36 = 720
[]: # 
[]: # 2. 4 įskilusios ir 1 sveika:
[]: # C(6, 4) * C(9, 1) = 15 * 9 = 135
[]: # 
[]: # 3. Visos 5 įskilusios:
[]: # C(6, 5) = 6
[]: # 
[]: # Dabar sudedame visus galimus atvejus:
[]: # Total = 720 + 135 + 6 = 861
[]: # 
[]: # Galiausiai apskaičiuojame tikimybę:
[]: # P = Total / C(15, 5) = 861 / 3003 ≈ 0.286
