import string

def verify(isbn):
    """
    Validates the provided isbn string using the checksum described by the ISBN-10 format

    ISBN-10 format is composed of 9 digits [x1, ... , x9] (possible values 0-9) and a check character x10 
      (either digit or X, representing value 10).
    A valid ISBN obeys the formula:
      sum(x[n]*i) mod 11 == 0 for n=[1,2,...,10] and i=[10, 9,...,1]
    """
    x = []

    for character in isbn:
        if character in string.digits:
            x.append(int(character))
        # only accept X as a digit if it's the check digit, in position 10
        if character == 'X':
            if len(x) == 9:
                x.append(10)
            else:
                # found an X out of position
                return False

    if len(x) != 10:
        # too many digits
        return False

    if sum( val*(10-n) for n, val in enumerate(x)) % 11 == 0:
        return True
    else:
        return False

verify([3-598-21508-8])        