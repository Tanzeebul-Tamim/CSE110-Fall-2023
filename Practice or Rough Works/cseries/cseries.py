def find_factorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

def find_m(e, v):
        m = 1
        while True:
            lhs = v ** (2 * m)
            rhs = e * find_factorial(2 * m)

            if (lhs <= rhs):
                break
            m += 1
        return m

def find_term(v, m):
     term = float(( v ** (2 * m) / find_factorial(2 * m) ) * (-1) ** m)
     return term
     
     

v = float(input("Enter a real number v between 0 and 6.28, inclusive: "))

if 0 <= v <= 6.28:
    e = float(input("Enter a small positive real number e << 1: "))
    if 0 < e < 1:
        m = find_m(e, v)
        w = 1

        for i in range(1, m + 1):
             w += (find_term(v, i))
        
        print(f"w : {w}")
    else:
         print("Invalid input for variable 'e'!")
else:
    print("Invalid input for variable 'v'!")
