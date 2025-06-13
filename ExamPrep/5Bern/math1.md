1. Atliekama n (n ⩾ 5) Bernulio schemos bandymu, Sn yra gautu sekmiu skaičius. Kaip
užrašoma baigtis šioje Bernulio schemoje? Kiek palankiu baigčiu turi ivykis {Sn = 5}?

Bernulio schemoje su \(n\) bandymų (kur \(n \geq 5\)) ir sėkmės tikimybe \(p\), baigtis užrašoma kaip seka ilgio \(n\), kurioje kiekvienas elementas yra arba "sėkmė" (\(S\)), arba "nesėkmė" (\(N\)). Pavyzdžiui, viena iš galimų baigčių gali būti \(SNSNSS \dots SNSNSS\).

Įvykis \(\{S_n = 5\}\) reiškia, kad per \(n\) bandymų buvo lygiai 5 sėkmės. Palankių baigčių, kurios tenkina šią sąlygą, skaičius yra lygus derinių skaičiui, t.y. būdų, kuriais galima pasirinkti 5 sėkmingus bandymus iš \(n\) bandymų. Tai užrašoma kaip \(C(n, 5)\) arba \(\binom{n}{5}\).

Taigi, palankių baigčių skaičius yra:
\[
\binom{n}{5} = \frac{n!}{5!(n-5)!}
\]
