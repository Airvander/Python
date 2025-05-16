#isValidPassword.py

from JonathanChuaWeiCong_solution import isValidPassword

# Test cases
print(isValidPassword("Abcdefghi1@"))    # True
print(isValidPassword("Abc1@"))          # False (less than 10 characters)
print(isValidPassword("ABCDEF123!"))     # False (no lowercase)
print(isValidPassword("abcde123!"))      # False (no uppercase)
print(isValidPassword("Abcdefghi123"))   # False (no special character)
print(isValidPassword("Abcdefghi123!!")) # True
print(isValidPassword("1A@"))            # False (less than 10 characters)
print(isValidPassword("a1@"))            # False (no uppercase)
print(isValidPassword("A1@"))            # False (no lowercase)
print(isValidPassword("aA1@"))           # False (less than 10 characters)
print(isValidPassword("!@#"))            # False (less than 10 characters)
print(isValidPassword("aA1@bC2#dE3!"))   # True

