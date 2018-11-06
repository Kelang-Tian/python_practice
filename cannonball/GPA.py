
class Student:
    def __init__(self, name, hours, points):
        self.name = name
        self.hours = float(hours)
        self.points = float(points)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.points

    def gpa(self):
        return self.points/self.hours


def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)


def main():
    # open the input file for reading
    filename = input("Enter the name of file: ")
    infile = open(filename, 'r')

    best = makeStudent(infile.readline())

    for line in infile:
        s = makeStudent(line)
        if s.gpa() > best.gpa():
            best = s

    infile.seek(0)

    for line in infile:
        s = makeStudent(line)
        # if multiple students are tied for the best GPA
        if s.gpa() == best.gpa():
            # print information about the best student
            print("The best students is: ", s.getName())
            print("========hours======== ", s.getHours())
            print("=========GPA========= ", s.gpa())
            print()

    infile.close()


if __name__ == '__main__':
    main()