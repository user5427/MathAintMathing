x = [8.9, 6.9, 2.2, 8.6, 4.3, 8.5, 3.4, 7.8, 8.8, 7.1, 9.7, 9.4, 7.8]

q = [1/4, 1/2, 3/4]


def findVq(x, q):
    y = x.copy()
    y.sort()
    
    val = len(y) * q
    
    
    if val != int(val):
        return y[int(val)]
    else:
        return (y[int(val)-1] + y[int(val)]) / 2
    
vqs = [findVq(x, q) for q in q]
print(vqs)
        
# avg = sum(x) / len(x)
# print(avg)

# dispersion = sum([(i - avg) ** 2 for i in x]) / (len(x) - 1)
# # print(f"{dispersion} not squared")
# print(dispersion ** 0.5)
