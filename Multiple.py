class Father:
    def money(self):
        print("Father has money")
class Mother:
    def care(self):
        print("Mother gives care")
class Child(Father, Mother):
    def son(self):
        print("son study")
c = Child()
c.money()
c.care()
c.son()
