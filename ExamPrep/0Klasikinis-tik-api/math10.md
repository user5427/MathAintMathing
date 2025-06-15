10. Bandymas - dalelės kelione iš plokštumos taško (0; 0) i plokštumos tašką (6; 4). Iš taško
(x; y) dalele vienu žingsniu gali patekti i tašką (x + 1; y) arba (x; y + 1). Kiek yra tokio bandymo
baigčiu (keliu)?

6 i 1 žingsniais reikia pereiti 6 horizontalius ir 4 vertikalius žingsnius, t.y. iš viso 10 žingsnių.

Baigčių skaičius yra lygus visų galimų žingsnių kombinacijų skaičiui, kuriose yra 6 horizontalių ir 4 vertikalių žingsnių. Tai galima apskaičiuoti naudojant kombinatoriką:
\[
C(10, 6) = \frac{10!}{6! \cdot 4!} = \frac{10 \cdot 9 \cdot 8 \cdot 7}{4 \cdot 3 \cdot 2 \cdot 1} = 210
\]