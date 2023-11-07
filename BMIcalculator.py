
#height should be in metres, weight in kilograms

class Bmi():
    def __init__(self, height:float, weight:float):
        assert height > 0, f"Height must be a float greater than 0"
        assert weight >0, f"Weight must be a float greater than 0"

        self.height = height
        self.weight = weight

    def weightStatus(self):
        bmi = float(self.weight)/float((self.height)**2)
        print(f"Your BMI is {round(bmi,2)}")
        if bmi < 18.5:
            print("You are Underweight.")
        elif 18.5<bmi<=24.5:
            print("You have a healthy weight range. ")
        elif 24.5<bmi<=29.9:
            print("You are Overweight. ")
        else:
            print("You are obese. ")

Felix = Bmi(1.68, 59).weightStatus()

