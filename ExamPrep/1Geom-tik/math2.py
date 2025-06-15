# 2. Bandymo baigčiu aibė Ω – kvadratas. Jo viduje yra skritulys, kurio spindulys lygus 2. At-
# sitiktinai renkant kvadrato tašką, tikimybė pataikyti  i skrituli lygi 0,25. Koks kvadrato kraštinės
# ilgis?

r = 2  # Radius of the circle
prob = 0.25  # Probability of hitting the circle

# Area of the circle
circle_area = 3.14 * r ** 2
# Area of the square based on the probability
square_area = circle_area / prob
# Length of the square's side
square_side = square_area ** 0.5
print("Length of the square's side: ", square_side)