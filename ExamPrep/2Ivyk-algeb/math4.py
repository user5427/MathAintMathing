# 4. Krepšininkas mes tris baudos metimus. Ivyki, kad i-asis metimas bus taiklus, pažymekime
# Ai , i = 1, 2, 3. Naudodamiesi šiu bei jiems priešingu ivykiu žymenimis išreikškite ivyki, kad taiklus
# bus tik vienas metimas.

# (A1 & ~A2 & ~A3) | (~A1 & A2 & ~A3) | (~A1 & ~A2 & A3)
# E = (A₁ ∩ A₂ᶜ ∩ A₃ᶜ) ∪ (A₁ᶜ ∩ A₂ ∩ A₃ᶜ) ∪ (A₁ᶜ ∩ A₂ᶜ ∩ A₃)