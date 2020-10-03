

def f_n_plus_2(f_n, f_n_plus_one):
    return f_n + f_n_plus_one

eps = 0.0001

sum = 0
f1 = 3
f2 = 5
while (1/(f1*f_n_plus_2(f1, f2)) >= eps):
    new_elem = f_n_plus_2(f1, f2)
    sum += 1/(f1*new_elem)
    f1 = f2
    f2 = new_elem
print(sum)