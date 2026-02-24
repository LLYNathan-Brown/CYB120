class entry:
    def __init__(self, data, dataName):
        self.data = data
        self.id = dataName

def printheader(dataList):
    for entry in dataList :
        print(f'{entry.id}: {entry.data}')

def printfooter(obj):
    #print('(c) www.petmon1754.com   ' & NameOfReport & '    Page 1 of 1')
    print(f'(c) www.petmon1754.com  {obj.data}  Page 1 of 1')

def getInput(data):
    raw = input(f'Please Enter {data}: ')
    if raw == '' :
        print(f'\n\'{data}\' cannot be empty!\n')
        getInput(data)
    return entry(raw, data)
    
#if Name = '' then Name = input("Enter Name: ")
#if Department = '' then Department =
#if Computer '' then Computer = input("Enter Computer: ")
#if DateAndTime = '' then DateAndTime = input("Enter Date and Time: ")
#if NameOfReport = '' then NameOfReport = input("Enter Name of report: ")
Name = getInput('Name')
Department = getInput('Department')
Computer = getInput('Computer')
DateAndTime = getInput('Date And Time')
NameOfReport = getInput('Report Name')

printheader([Name, Department, Computer, DateAndTime, NameOfReport])
print('\nReport goes here\n')
printfooter(NameOfReport)
