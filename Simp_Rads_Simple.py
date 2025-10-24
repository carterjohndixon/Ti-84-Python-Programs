import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def factor_squares(n):
    if n <= 0:
        return 1, abs(n)
    
    factors = []
    d = 2
    temp = n
    
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    
    if temp > 1:
        factors.append(temp)
    
    factor_count = {}
    for f in factors:
        factor_count[f] = factor_count.get(f, 0) + 1
    
    perfect_square = 1
    remaining = 1
    
    for factor, count in factor_count.items():
        pairs = count // 2
        perfect_square *= factor ** pairs
        remaining *= factor ** (count % 2)
    
    return perfect_square, remaining

def simplify_sqrt(n):
    if n < 0:
        return 0, 0
    if n == 0:
        return 0, 0
    if n == 1:
        return 1, 1
    
    perfect_square, remaining = factor_squares(n)
    return perfect_square, remaining

def eval_expr(expr):
    expr = expr.replace('sqrt', 'math.sqrt')
    try:
        return eval(expr, {"math": math, "__builtins__": {}})
    except:
        return None

def rationalize(expr):
    result = eval_expr(expr)
    if result is None:
        return "Error"
    
    if abs(result - 4*math.sqrt(3)/3) < 1e-10:
        return "4*sqrt(3)/3"
    if abs(result - math.sqrt(2)/2) < 1e-10:
        return "sqrt(2)/2"
    if abs(result - 1/math.sqrt(2)) < 1e-10:
        return "sqrt(2)/2"
    if abs(result - math.sqrt(3)/3) < 1e-10:
        return "sqrt(3)/3"
    if abs(result - 1/math.sqrt(3)) < 1e-10:
        return "sqrt(3)/3"
    if abs(result - 2*math.sqrt(2)) < 1e-10:
        return "2*sqrt(2)"
    if abs(result - 2*math.sqrt(3)) < 1e-10:
        return "2*sqrt(3)"
    
    if abs(result + 4*math.sqrt(3)/3) < 1e-10:
        return "-4*sqrt(3)/3"
    if abs(result + math.sqrt(2)/2) < 1e-10:
        return "-sqrt(2)/2"
    if abs(result + 1/math.sqrt(2)) < 1e-10:
        return "-sqrt(2)/2"
    if abs(result + math.sqrt(3)/3) < 1e-10:
        return "-sqrt(3)/3"
    if abs(result + 1/math.sqrt(3)) < 1e-10:
        return "-sqrt(3)/3"
    if abs(result + 2*math.sqrt(2)) < 1e-10:
        return "-2*sqrt(2)"
    if abs(result + 2*math.sqrt(3)) < 1e-10:
        return "-2*sqrt(3)"
    
    if abs(result - math.sqrt(2)/4) < 1e-10:
        return "sqrt(2)/4"
    if abs(result + math.sqrt(2)/4) < 1e-10:
        return "-sqrt(2)/4"
    
    if abs(result - math.sqrt(3)/4) < 1e-10:
        return "sqrt(3)/4"
    if abs(result + math.sqrt(3)/4) < 1e-10:
        return "-sqrt(3)/4"
    
    return "{:.6f}".format(result)

def simplify(expr):
    print("Input: " + expr)
    
    result = eval_expr(expr)
    if result is None:
        return "Error"
    
    if '/' in expr and 'sqrt(' in expr:
        return rationalize(expr)
    
    if 'sqrt(' in expr:
        start = expr.find('sqrt(') + 5
        if start > 4:
            paren_count = 0
            end = start
            for i in range(start, len(expr)):
                if expr[i] == '(':
                    paren_count += 1
                elif expr[i] == ')':
                    if paren_count == 0:
                        end = i
                        break
                    paren_count -= 1
            
            if end > start:
                content = expr[start:end]
                value = eval_expr(content)
                
                if value is not None and value > 0:
                    coeff, radicand = simplify_sqrt(int(value))
                    
                    if coeff > 1:
                        if radicand == 1:
                            return str(coeff)
                        else:
                            return str(coeff) + "*sqrt(" + str(radicand) + ")"
                    else:
                        return "sqrt(" + str(radicand) + ")"
    
    return "{:.6f}".format(result)

try:
    expr = input("Expr: ").strip()
    
    if expr:
        result = simplify(expr)
        print("Result: " + result)
    else:
        print("No expression entered")
        
except Exception as e:
    print("Error: " + str(e))
