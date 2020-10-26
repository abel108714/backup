import os

def getUesrIndex(UesrName):
    file1 = open('data\\UserData.txt', 'r') 
    Lines = file1.readlines() 
    count = 0
    for line in Lines: 
        if UesrName == line.strip().split(',')[1]:
            return count
        else:
            count+=1
            
def getUesrID(UesrName):
    file1 = open('data\\UserData.txt', 'r') 
    Lines = file1.readlines() 
    count = 0
    index = getUesrIndex(UesrName)
    for line in Lines: 
        if count == index:
            return line.strip().split(',')[0]
        else:
            count+=1


print(getUesrIndex('立修'))
print(getUesrIndex('陳'))
print(getUesrID('立修'))
print(getUesrID('陳'))


class Student:
    def __init__(self, id=1, name='george', sex='boy'):
        self.id = id
        self.name = name
        self.sex = sex
    def getID(self,id):
        return self.id
    def getName(self, id):
        return self.name
    def getSex(self, id):
        return self.sex
    def getObjAdd(self,id):
        return self 



if __name__ == '__main__':
    s = Student(1, 'Peter')
    s2 = Student(2, 'kate', 'girl')
    s3 = Student()
    print(s.id, s.name, s.sex)
    print(s2.id, s2.name, s2.sex)
    print(s3.id, s3.name, s3.sex)
    print(s3.getID(1))
    print(s3.getName(1))
    print(s3.getSex(1))
    print(s3.getObjAdd(1))

class Animal:
    def __init__(self, name):
        self.name = name
    def who(self):
        return self.name

a = Animal("dog")
print(a.who())

