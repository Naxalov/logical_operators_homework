def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    ans1 = b>a and b<c 
    ans2 = b<a and b>c
    return ans1 or ans2

print(main(1,4,7))