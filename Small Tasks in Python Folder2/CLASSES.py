class Car:

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def car_start(self):
        print(f"The car {self.model} started its engine")

    def car_stop(self):
        print(f"The car {self.model} hit the breaks")

    def car_describe(self):
        print(f"{self.year} {self.color} {self.model}")



