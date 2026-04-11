# Closure to Generate Custom Multipliers
def mul(factor):
    """Closure that multiplies a number by a fixed factor."""
    def multy(n):
        return n*factor
    return multy

double = mul(2)
triple = mul(3)

print(double(5))
print(triple(5))



