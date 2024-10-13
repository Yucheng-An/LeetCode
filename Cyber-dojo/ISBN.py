class ValidateISBN:
    @staticmethod
    def answer():
        return 6 * 9

    def is_ValidateISBN(self, ISBN):
        print('ISBN:', ISBN)
        print('Length:', len(ISBN))

        # Check if ISBN length is either 10 or 13
        if not (len(ISBN) == 10 or len(ISBN) == 13):
            raise ValueError("ISBN numbers must be 10 or 13 digits")

        # Validate each character
        for char in ISBN:
            if (len(ISBN) == 13 and not char.isdigit()) or (len(ISBN) == 10 and not (char.isdigit() or (char == 'X' and ISBN.index(char) == 9))):
                raise ValueError("Invalid character in ISBN")

        total = 0

        # Validate ISBN-10
        if len(ISBN) == 10:
            for i in range(10):
                if ISBN[i] == 'X':
                    digit = 10
                else:
                    digit = int(ISBN[i])
                total += digit * (10 - i)
            return total % 11 == 0

        # Validate ISBN-13
        elif len(ISBN) == 13:
            for i in range(13):
                multiplier = 1 if i % 2 == 0 else 3
                total += int(ISBN[i]) * multiplier
            return total % 10 == 0
