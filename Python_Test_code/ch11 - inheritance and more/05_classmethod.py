# class Cars:
#     a=100

#     def model(self):
#         print(f"totall number of cars: {self.a}")
# x = Cars()
# x.a=200
# x.model()




class Cars:
    a=100
    @classmethod
    def model(cls):
        print(f"totall number of cars: {cls.a}")
x = Cars()
x.a=200
x.model()
