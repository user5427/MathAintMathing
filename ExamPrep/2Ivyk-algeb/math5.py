# 5. Bandymas – kelionė i paskaitą. Ivykis A reiškia, kad paveluosite, B – kad
# paveluos dėstytojas. Kokiais dar ivykiais reikia papildyti šią ivykiu porą,
# kad ivykiu sistema sudarytu σ-algebrą?


# Norint, kad įvykių sistema sudarytų σ-algebrą, ji turi tenkinti šias sąlygas:

#     Visos erdvės priklausymas: Visos imties erdvė Ω turi priklausyti σ-algebrai.

#     Uždarumas atžvilgiu papildinio: Jei įvykis priklauso σ-algebrai, tai ir jo papildinys turi priklausyti.

#     Uždarumas atžvilgiu skaičiuojamos jungties: Bet koks skaičiuojamas įvykių sąjunga turi priklausyti σ-algebrai.


# Šiuo metu σ-algebra turi tik šiuos du įvykius, tačiau ji nėra pilna. Kad
# sistema taptų σ-algebra, turime pridėti visus galimus šių įvykių derinius ir
# jų papildinius.



# Taigi, pilna σ-algebra turėtų būti sudaryta iš šių įvykių:

#     ∅ (tuščia aibė)

#     A (studentas paveluoja)

#     B (dėstytojas paveluoja)

#     A' (studentas nepaveluoja)

#     B' (dėstytojas nepaveluoja)

#     A ∪ B (studentas arba dėstytojas paveluoja, arba abu)

#     A ∩ B (studentas ir dėstytojas paveluoja)

#     (A ∪ B)' (nei studentas, nei dėstytojas paveluoja)

#     A' ∩ B (studentas nepaveluoja, bet dėstytojas paveluoja)

#     A ∩ B' (studentas paveluoja, bet dėstytojas nepaveluoja)

#     A' ∪ B (studentas nepaveluoja arba dėstytojas paveluoja, arba abu)

#     A ∪ B' (studentas paveluoja arba dėstytojas nepaveluoja, arba abu)

#     A' ∩ B' (nei studentas, nei dėstytojas paveluoja)

#     A' ∪ B' (studentas nepaveluoja arba dėstytojas nepaveluoja, arba abu)

#     A Δ B (simetrinis skirtumas: studentas arba dėstytojas paveluoja, bet ne abu)

#     Ω (visa imties erdvė)


# Tačiau daugeliu atvejų, kai turime tik du pagrindinius įvykius A ir B, minimali σ-algebra (generuota šių įvykių) bus sudaryta iš šių aibių:

#     ∅

#     A

#     B

#     A' ∩ B'

#     A ∪ B

#     A' ∩ B

#     A ∩ B'

#     Ω

# Taigi, norint užbaigti σ-algebra, reikia pridėti visus likusius galimus nesutaikomus įvykius ir jų derinius, kad būtų užtikrintas uždarymas visoms aibių operacijoms.
