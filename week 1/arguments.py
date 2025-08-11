# if n is odd,print Weird
# if n is even and in a inclusive range of 2 to 5,Print Not Weird
# if n is even and in a inclusive range of 6 to 20,print Weird
# if n is even and greater than 20,print Not Weird

def Check_Weird(n):
    if n % 2 !=0:
        return "Weird"
    elif 2 <= n <= 5:
        return "Not Weird"
    elif 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"
    print(Check_Weird(n))