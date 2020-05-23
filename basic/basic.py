
class Basic:
    def user_input_integers(self):
        """
        Take in two numbers from user input and calculate the average
        """
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        avg = (num_1 + num_2) / 2
        print(f"The average is {avg}")

    def run_excercises(self):
        self.user_input_integers()


if __name__ == "__main__":
    Basic().run_excercises()
