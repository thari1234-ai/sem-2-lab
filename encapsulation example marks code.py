class Stu:
    def __init__(self):
        self.__marks=0
    def set_marks(self,m):
        self.__marks=m
    def get_marks(self):
        return self.__marks
s=Stu()
s.set_marks(86)
print(s.get_marks())
        
    