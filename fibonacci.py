#!/usr/bin/env python3


def fibonacci(f: object) -> object:
    """

    :type i: int
    :rtype: int
    :param f:
    :return: int
    """
    # recursive implementation of fibonacci numbers
    if f <= 1:
        return f
    else:
        return fibonacci(f - 1) + fibonacci(f - 2)


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """
    # returns the last 8 digits of the integer,
    # first convert the int to string and take the last 8 characters and convert into Int
    return int(str(some_int)[-8:])


def optimized_fibonacci(f):

    if f <= 1:
        return f
    else:
        # store the first two values, we just take the previous values and add them thru the loop
        # at the end we return the final value
        opt_fib = [0, 1]
        for i in range(2, f + 1):
            opt_fib.append(opt_fib[i - 1] + opt_fib[i - 2])
        return opt_fib[i]
        # at this point we have the fibonacci number f at the i th position in the list


# raise NotImplementedError()


class SummableSequence(object):
    def __init__(self, *initial):
        # Assign the initial values, can be generalized as well
        self.args = initial

    # raise NotImplementedError()

    def __call__(self, f):
        global next_sum

        # if the input number is higher than 3 we will loop thru to add the numbes
        # ex: 5 + 7 + 11 = 23, next number in the series is 5 +7 +11 +23 = 46
        # next number is 92 , 184 etc, we just multiply the numbers
        prev_sum = sum(self.args)
        for i in range(len(self.args), f + 1):
            next_sum = prev_sum * 2
            prev_sum = next_sum
        return next_sum


if __name__ == "__main__":
    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)

    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))

    ss = SummableSequence(0, 1)
    print("new_seq(5)[-8:]:", last_8(ss(5)))
    print("new_seq(10)[-8:]:", last_8(ss(10)))
