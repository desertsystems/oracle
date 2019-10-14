from enum import Enum, unique

@unique
class Number(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    eleven = 11
    twelve = 12
    thirteen = 13
    fourteen = 14
    fifteen = 15
    sixteen = 16
    seventeen = 17
    eighteen = 18
    nineteen = 19
    twenty = 20
    thirty = 30
    forty = 40
    fifty = 50
    sixty = 60
    seventy = 70
    eighty = 80
    ninety = 90
    hundred = 100
    thousand = 1000
    million = 1000000
    billion = 1000000000
    trillion = 1000000000000
    quadrillion = 1000000000000000
    quintillion = 1000000000000000000
    sextillion = 1000000000000000000000


class NumberUtil:
    def __init__(this, number):
        this.number = number # input number
        this.output = ""     # output words


    # parser for input number
    def parse(this):
        groups = this.numberToGroups(this.number)
        groupCategory = this.getGroupCatogory(groups)
        
        # new process groups
        for i, (group, category) in enumerate(zip(groups,groupCategory)):
            this.process(group)
            number = this.groupToInt(group)
            
            if i < len(groups)-1 and number > 0: 
                this.output += category+" "
                this.checkGrammar(i, groups)

        # output result
        print(this.output)
        

    # process 0 to 999
    def process(this, group):
        number = this.groupToInt(group)

        # process 0 to 21
        if number < 21:
            if number != 0:
                this.output += Number(number).name+" "
        
        else: # process 21 to 99
            if len(group) == 2:
                this.output += Number(group[0]*10).name+" "

                if(group[1] != 0): 
                    this.output += Number(group[1]).name+" "
            
            else: # process 100 to 999
                if group[0] != 0:
                    this.output += Number(group[0]).name+" "
                    this.output += Number(100).name+" "

                if number != (100*group[0]):
                    if number != 0:
                        this.checkGrammarMistake(group)

                    del group[0]
                    this.process(group)


    # converts group array to whole number
    def groupToInt(this, group):
        return int(''.join(str(x) for x in group))


    # convert a number into groups of 3 digits from right to left
    def numberToGroups(this, number):
        # iterate number string to char array
        digits = list(int(x) for x in str(number))
        digits.reverse()

        # divide digits into groups of 3 from
        groups = [digits[i:i + 3] for i in range(0, len(digits), 3)]
        groups.reverse()

        # reorder each group to original sequence
        for group in groups: group.reverse()
        
        return groups


    # assigns catogories for each group
    def getGroupCatogory(this, groups):
        category = []
        for i, group in enumerate(reversed(groups)):
            # 10^(i*3)... 
            # if i=1: 10^3 >> thousand
            # if i=2: 10^6 >> million
            # if i=3: 10^9 >> billion ...
            category.insert(i, Number(10**(i*3)).name)

        category.reverse()
        return category


    # checks grammar inbetween groups
    def checkGrammar(this, current, groups):
        if current < len(groups)-1:
            nextNumber = this.groupToInt(groups[current+1])

            if nextNumber < 100 and nextNumber != 0:
                this.output += "and "

            if nextNumber == 0:
                this.checkGrammar(current+1, groups)


    # checks grammar in current group
    def checkGrammarMistake(this, group):
        if len(group) == 3: 
            if this.output[-4:] != "and ":
                this.output += "and "



# commanline interface for testing
q = False
inputType = 'number'
bang = '!'

while not q:
    number = input('Input a '+inputType+' and press Enter (0 to quit): ')

    try:
        util = NumberUtil(int(number))
        util.parse()

        if int(number) == 0: q = True
        inputType = 'number'

    except ValueError:
        inputType = "NUMBER"+bang
        bang = bang+'!'
