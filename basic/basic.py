
class Basic:
    def user_input_integers(self):
        """
        Take in two numbers from user input and calculate the average
        """
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        avg = (num_1 + num_2) / 2
        print(f"The average is {avg}")

    def sum_num(self, specified_range=10):
        """
         Take in a range and calculate the sum of each number
         and the preceeding number in the range
        """
        for i in range(specified_range):
            if i < 1:
                continue
            sum = i + (i + 1)
            print(f"Current number: {i}, previous number: {i - 1}, sum: {sum}")

    def even_placed_chars(self, word):
        """
        Take in a string from the user and return only the strings
        that are placed in even placed positions
        """
        list = []
        for i, v in enumerate(word):
            if i % 2 == 0:
                list.append(v)
        return list

    def slice_string_with_diff(_, str, diff):
        """
          Takes in a string and a diff and removes thee first 0-n letters
          of the string
        """
        if diff > len(str):
            return None
        else:
            return str[diff:]

    def run_excercises(self):
        self.sum_num()
        self.user_input_integers()


if __name__ == "__main__":
    Basic().run_excercises()
