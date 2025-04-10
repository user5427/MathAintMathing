# Kovariacija tarp išsiųstų ir gautų vienetų
# Let me solve for the covariance between X (number of ones sent) and Y (number of ones received).

# Given information:
# Karlsonas sends '11' when in good mood (probability q = 0.76)
# Otherwise he sends '01' (probability 1-q = 0.24)
# Each bit has probability p = 0.02 of being flipped during transmission
# X = number of ones in sent message
# Y = number of ones in received message
# Step 1: Find possible values and probabilities for X
# X = 2 when sending '11', P(X=2) = q = 0.76
# X = 1 when sending '01', P(X=1) = 1-q = 0.24
# Step 2: Calculate conditional probabilities for Y given X
# For X = 2 (sending '11'):

# Y = 2: Both bits remain 1, P(Y=2|X=2) = (1-p)² = 0.98² = 0.9604
# Y = 1: One bit flips, P(Y=1|X=2) = 2p(1-p) = 2×0.02×0.98 = 0.0392
# Y = 0: Both bits flip, P(Y=0|X=2) = p² = 0.02² = 0.0004
# For X = 1 (sending '01'):

# Y = 2: 0-bit flips to 1, P(Y=2|X=1) = p(1-p) = 0.0196
# Y = 1: Either both bits stay same OR both flip, P(Y=1|X=1) = (1-p)²+p² = 0.9608
# Y = 0: 1-bit flips to 0, P(Y=0|X=1) = (1-p)p = 0.0196
# Step 3: Calculate joint probabilities P(X=x, Y=y)
# P(X=2, Y=2) = 0.76 × 0.9604 = 0.729904
# P(X=2, Y=1) = 0.76 × 0.0392 = 0.029792
# P(X=2, Y=0) = 0.76 × 0.0004 = 0.000304
# P(X=1, Y=2) = 0.24 × 0.0196 = 0.004704
# P(X=1, Y=1) = 0.24 × 0.9608 = 0.230592
# P(X=1, Y=0) = 0.24 × 0.0196 = 0.004704
# Step 4: Calculate expected values
# E[X] = 2×0.76 + 1×0.24 = 1.76
# E[Y] = 2×0.734608 + 1×0.260384 + 0×0.005008 = 1.7296
# E[XY] = 2×2×0.729904 + 2×1×0.029792 + 1×2×0.004704 + 1×1×0.230592 = 3.2192
# Step 5: Calculate covariance
# Cov(X,Y) = E[XY] - E[X]E[Y] = 3.2192 - 1.76×1.7296 = 0.175104

# Therefore, the covariance between X and Y is 0.175104.