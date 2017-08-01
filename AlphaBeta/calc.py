import random

# Generate a random number based on the given number of
# digits. Expected to have number between 1 to 10. Returns
# the number without overlapping digits

class alphaBeta:
    def __init__(self, digit):
        self.digit = digit
        self.targetNumber = self.generate(self.digit)
        print(self.targetNumber)

    def generate(self, digit_limit):
        my_number = random.randint(1, 9)
        digits = list(range(10))
        digits.pop(my_number)
        for i in range(digit_limit - 1):
            r_index = random.randint(0, 8 - i)
            r_digit = digits.pop(r_index)
            my_number = my_number * 10 + r_digit
        return my_number

    def check(self, guess):
        if self.targetNumber == guess:
            return [self.digit, 0]
        alpha = 0
        beta = 0
        for i in range(self.digit):
            result = self.num_in_digit(self.targetNumber, guess % 10, i)
            if result == 'alpha':
                alpha += 1
            elif result == 'beta':
                beta += 1
            guess //= 10
        return [alpha, beta]

    def num_in_digit(self, number, digit, place):
        counter = 0
        remainder = number % 10
        while remainder >= 0 and number > 0:
            if remainder == digit:
                if counter == place:
                    return 'alpha'
                else:
                    return 'beta'

            number = number // 10
            remainder = number % 10
            counter += 1
        return 'no'

    def guess(self, myGuess):
        won = 0
        response = self.check(myGuess)
        if response[0] == self.digit:
            won = 1
        else:
            print('Alpha: ' + str(response[0]))
            print('Beta: ' + str(response[1]))

        return [won, response[0], response[1]]