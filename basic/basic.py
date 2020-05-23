
# exercises here https://pynative.com/python-basic-exercise-for-beginners/


class Basic:
    def user_input_integers(self):
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        avg = (num_1 + num_2) / 2
        print(f"The average is {avg}")

    def sum_num(self, specified_range=10):
        for i in range(specified_range):
            if i < 1:
                continue
            sum = i + (i + 1)
            print(f"Current number: {i}, previous number: {i - 1}, sum: {sum}")

    def even_placed_chars(self, word):
        list = []
        for i, v in enumerate(word):
            if i % 2 == 0:
                list.append(v)
        return list

    def slice_string_with_diff(_, str, diff):
        if diff > len(str):
            return None
        else:
            return str[diff:]

    def bool_on_start_end_equality(_, list):
        return list[0] == list[len(list) - 1]

    def is_divisible_by_five(cls, list):
        return [node for node in list if node % 5 == 0]

    def count_substring(self, str, sub):
        return str.count(sub)

    def number_palindrome(self, num):
        return str(num) == str(num)[::-1]

    def run_excercises(self):
        self.sum_num()
        self.user_input_integers()


if __name__ == "__main__":
    Basic().run_excercises()
