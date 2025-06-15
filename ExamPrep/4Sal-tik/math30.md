30. Užrašykite ivykio pilnosios tikimybes formulę ivykio A tikimybei, kai galimos dvi hipotezes
H1 ir H2. Tegu P (A|H1) > P (A|H2). Irodykite, kad P (A) > P (A|H2).

P(A) = P(H1) * P(A|H1) + P(H2) * P(A|H2)
P(A) = P(A \cap H1) + P(A \cap H2)

P(A) = P(H1) * P(A|H1) + P(H2) * P(A|H2) > P(A|H2)
P(H1) * P(A|H1) > P(A|H2) - P(H2) * P(A|H2)
P(H1) * P(A|H1) > P(A|H2) * (1 - P(H2))

if 1 - P(H2) = P(H1), then: 

P(H1) * P(A|H1) > P(A|H2) * P(H1)
P(A) = P(A|H1) > P(A|H2)