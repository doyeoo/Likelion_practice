class Profile:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

    def intro(self):
        print("%s %d세이고 %s입니다."%(self.name, self.age, self.gender))

jjang=Profile('짱구는',5,'남자')
dora=Profile('도라에몽은',14,'남자')
conan=Profile('코난은',8,'남자')
choco=Profile('쇼콜라는',15,'여자')
amu=Profile('아무는',12,'여자')
young=Profile('가영은',16,'여자')

jjang.intro()
dora.intro()
conan.intro()
choco.intro()
amu.intro()
young.intro()
