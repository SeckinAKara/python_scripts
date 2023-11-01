import math

class Calculator:

    class treeNode:
        def __init__(self, value, lchild, rchild):
            self.value, self.lchild, self.rchild = value, lchild, rchild



    def __init__(self):
        self.functDic = {'+':1, '-':1, '*':2, '/':2, '^':3, 'sqrt':4, 'exp':4,
                         'sin':4, 'cos':4, 'tan':4, 'ln':4, 'lg':4, 'mod':4}
        self.functs = ['tan', 'lg', 'cos', 'ln', 'mod', 'sin','sqrt', 'exp']        

    def getLines(self, expr):                
        #expr : input to calc
        #the function sets self.lines
        self.lines = expr.split(';')
        if len(self.lines) == 1 and "return" not in self.lines[0]:
            self.lines[0] = "return " + self.lines[0]
        for number, line in enumerate(self.lines):
            if "=" in line:
                temporary = line.split('=')
                if len(temporary) > 2 or temporary[0].strip() == '' or temporary[1].strip() == '':
                    print("Line error: invalid equals signs")
                    return "Line error: invalid equals signs"
                self.lines[number] = list(map(lambda x: x.strip(), temporary))
            elif 'return' in line:
                return_index = line.index('return')
                self.lines[number] = ['return', line[return_index+6:]]
        if len(self.lines) > 1:
            if 'return' not in self.lines[-1]:
                return "Error: Invalid return placement"

    def applyFunct(self, funct, operand1, operand2):
        if funct == '+':
            try:
                return operand1+operand2
            except:
                return "Operation Error"
        elif funct == '-':
            try:
                return operand1-operand2
            except:
                return "Operation Error"
        elif funct == '*':
            try:
                return operand1*operand2
            except:
                return "Operation Error"
        elif funct == '/':
            try:
                return operand1/operand2
            except:
                return "Operation Error"
        elif funct == '^':
            try:
                return operand1**operand2
            except:
                return "Operation Error"
        elif funct == 'sqrt':
            try:
                return math.sqrt(operand1)
            except:
                return "Operation Error"
        elif funct == 'exp':
            try:
                return math.exp(operand1)
            except:
                return "Operation Error"
        elif funct == 'sin':
            try:
                return math.sin(operand1)
            except:
                return "Operation Error"
        elif funct == 'cos':
            try:
                return math.cos(operand1)
            except:
                return "Operation Error"
        elif funct == 'tan':
            try:
                return math.tan(operand1)
            except:
                return "Operation Error"
        elif funct == 'ln':
            try:
                return math.log(operand1)
            except:
                return "Operation Error"
        elif funct == 'lg':
            try:
                return math.log(operand1)/math.log(2)
            except:
                return "Operation Error"
        elif funct == 'mod':
            try:
                return operand1 - operand2 * math.floor(operand1/operand2)
            except:
                return "Operation Error"
        else:
            return "Operation Error"


    def isNumber(self, expr):
        if not isinstance(expr, str):
            print("type mismatch error: isNumber")
            return False
        elif len(expr.strip()) == 0:
            return False
        expr = expr.strip()
        if expr[0] == '-':
            expr = expr[1:]
        expr = expr.strip()
        try:
            float(expr)
            return True
        except:
            return False

    def convertNum(self, x):
        if x[0] == '-':
            num = -1*float(x[1:].strip())
        else:
            num = float(x)
        return num


    def isVariable(self, expr):
        if not isinstance(expr, str):
            print("type mismatch error: isNumber")
            return False
        elif len(expr) == 0:
            return False
        
        expr = expr.strip()
        if expr == '':
            return False
        if not expr[0].isalpha():
            return False
        else:
            for i in expr[1:]:
                if not i.isalpha() and not i.isdecimal():
                    return False
            return True


    def mask(self, s):   
        nestLevel = 0
        masked = list(s)
        for i in range(len(s)):
            if s[i]==")":
                nestLevel -=1
            elif s[i]=="(":
                nestLevel += 1
            if nestLevel>0 and not s[i]=="(":  # Line A
                masked[i]=" "
        return "".join(masked)


    def getNextFunct(self, expr, pos):
        if len(expr)==0 or not isinstance(expr, str):
            print("type mismatch error: isNumber")
            return None, None, None
        
        oldPos = pos
        while pos < len(expr):
            if expr[pos] in self.functDic:
                oprPos = pos
                opr = expr[pos]
                if opr == '-' and pos == 0:
                    if expr[pos+1:].strip()[0] == '(' or expr[pos+1:].strip()[0].isalpha():
                        break
                    else:
                        pos += 1
                        continue
                else:
                    break
            elif expr[pos].isalpha():
                scanPos = pos
                while expr[scanPos].isalpha():
                    scanPos += 1
                    if scanPos >= len(expr):
                        break
                if expr[pos:scanPos] in self.functDic:
                    oprPos = pos
                    opr = expr[pos:scanPos]
                    break
            pos += 1
        if pos >= len(expr):
            oprPos = opr = None
        item = expr[oldPos:pos]
        if item == '' and opr == '-':
            return opr, oprPos, 0
        elif self.isNumber(item):
            return opr, oprPos, self.convertNum(item.strip())
        elif self.isVariable(item):
            return opr, oprPos, item.strip()
        else:
            return opr, oprPos, None

    def addStars(self, expr):
        if type(expr) != str:
            return "Error: Invalid expression"
        if len(expr.strip()) < 1:
            return "Error: Invalid expression"
        operators = ['+', '-', '*', '/', '^', ',']
        functs = ['tan', 'lg', 'cos', 'ln', 'mod', 'sin','sqrt', 'exp']
        pieces = []
        pos = 0
        add_pos = 1
        while pos < len(expr):
            if expr[pos] in operators:
                pieces.append(expr[pos].strip())
                pos += 1
            elif self.isNumber(expr[pos]):
                while self.isNumber(expr[pos:pos+add_pos+1]):
                    add_pos += 1
                    if pos+add_pos+1 > len(expr):
                        break
                pieces.append(expr[pos:pos+add_pos].strip())
                pos += add_pos
                add_pos = 1
            elif self.isVariable(expr[pos]):
                while self.isVariable(expr[pos:pos+add_pos+1]):
                    add_pos += 1
                    if pos+add_pos+1 > len(expr):
                        break
                pieces.append(expr[pos:pos+add_pos].strip())
                pos += add_pos
                add_pos = 1
            elif expr[pos] in ['(', ')']:
                pieces.append(expr[pos].strip())
                pos += 1
            else:
                pos += 1
        if len(pieces) < 2:
            return expr
        new_pieces = []
        for i in range(len(pieces)-1):
            if pieces[i] in operators or pieces[i] in functs:
                new_pieces.append(pieces[i])
                i += 1
            elif pieces[i] not in operators and pieces[i] != '(':
                if pieces[i+1] not in operators and pieces[i+1] != ')':
                    new_pieces.append(pieces[i])
                    new_pieces.append('*')
                else:
                    new_pieces.append(pieces[i])
                i += 1
            else:
                new_pieces.append(pieces[i])
                i += 1
        new_pieces.append(pieces[-1])
        new_expr = ' '.join(new_pieces)
        return new_expr   
            


    def constructTree(self, expr):
        expr = expr.strip()
        test = self.mask(expr)
        test = test.replace('(', '')
        test = test.replace(')', '')
        if test.strip() == '':
            expr = expr[1:-1]
            good = True
        else:
            good = False
        variables = []
        #print(expr)
        pos = 0
        if self.isNumber(expr):
            node = self.treeNode(self.convertNum(expr), None, None)
            return node
        elif self.isVariable(expr):
            if expr.strip() in self.varDic:
                value = self.varDic[expr.strip()]
                node = self.treeNode(float(value), None, None)
                return node
            else:
                return "Error: Variable error"
        while pos != None:
            opr, oprPos, item = self.getNextFunct(self.mask(expr), pos)
            if oprPos != None:
                pos = oprPos + 1
            else:
                pos = oprPos
            if opr == '-' and oprPos == 0:
                expr = '0' + expr
                oprPos = 1
            if opr != None:
                if opr in self.functs and item != None:
                    return "Error: Formula error"
                else:
                    variables.append((opr, oprPos, item))
        #print(expr)
        #print(variables)
        if len(variables) == 0:
            node = self.treeNode(expr.strip(), None, None)
            return node
        else:
            minimum = variables[0]
            for choice in variables[1:]:
                if self.functDic[choice[0]] <= self.functDic[minimum[0]]:
                    minimum = choice
        #print(minimum)
        if minimum[0] == '^' and type(minimum[2]) in [int, float]:
            if minimum[2] < 0:
                minimum = ('-', 1, 0)
                expr = '0' + expr
        if minimum[0] == '-' or minimum[0] == '/' and not good:
            #print(expr, minimum[1]+1, self.getNextFunct(self.mask(expr), minimum[1]+1))
            nextOpr, nextPos, nextItem = self.getNextFunct(self.mask(expr), minimum[1]+1)
            nextOpr, nextPos, nextItem = str(nextOpr), str(nextPos), str(nextItem)
            #print(nextOpr, nextPos, nextItem)
            if self.isNumber(nextItem):
                if minimum[0] == '-':
                    if nextOpr == '^':
                        superNextOpr, superNextPos, superNextItem = \
                                      self.getNextFunct(self.mask(expr), int(nextPos) + 1)
                        minimum = ('+', minimum[1], minimum[2])
                        if superNextPos == None:
                            superNextPos = len(expr)
                        expr = expr[:minimum[1]] + '+ -(' + expr[minimum[1]+1:superNextPos] + ')' +\
                               expr[superNextPos:]
                    else:
                        minimum = ('+', minimum[1], minimum[2])
                        expr = expr[:minimum[1]] + '+ -' + expr[minimum[1] + 1:]
                else:
                    minimum = ('*', minimum[1], minimum[2])

                    if nextOpr != 'None':
                        expr = expr[:minimum[1]] + '* (1/' + str(nextItem) + ')' + expr[int(nextPos):]
                    else:
                        expr = expr[:minimum[1]] + '* (1/' + str(nextItem) + ')'
        #print(minimum)
        node = self.treeNode(minimum[0], None, None)
        if minimum[0] in ['+', '-', '*', '/', '^']:
            node.lchild = self.constructTree(expr[:minimum[1]])
            node.rchild = self.constructTree(expr[minimum[1]+1:])
        else:
            starting_paren = minimum[1] + len(minimum[0])
            masked = self.mask(expr[starting_paren:])
            #print(masked)
            closing_paren = starting_paren + masked.index(')') + 1
            #print(starting_paren, closing_paren)
            if minimum[0] != 'mod':
                node.lchild = self.constructTree(expr[starting_paren:closing_paren])
            else:
                space = expr[starting_paren:closing_paren]
                comma = starting_paren + space.index(',')
                node.lchild = self.constructTree(expr[starting_paren+1:comma])
                node.rchild = self.constructTree(expr[comma + 1:closing_paren-1])
        return node


    def setRoot(self, expr):
        try:
            self.treeRoot = self.constructTree(expr)
            if type(self.treeRoot.value) == str:
                if 'error' in self.treeRoot.value.lower():
                    return False
            return True
        except:
            return False
        

    def evaluateTree(self, node):
        if node == None:
            return None
        elif type(node) == str:
            return "Error: Invalid function"
        elif type(node.value) == float:
            return node.value
        elif type(node.value) == str and node.value in self.functDic:
            return self.applyFunct(node.value, \
                                   self.evaluateTree(node.lchild), \
                                   self.evaluateTree(node.rchild))
        else:
            return "Error: Invalid function"


    def calc(self, expr):
        self.treeRoot = None
        self.varDic = {}
        self.getLines(expr)
        for line in self.lines:
            if len(line) != 2:
                return "Formula error: Invalid formula"
            line[1] = self.addStars(line[1])
            if line[0] == 'return':
                variable = '__return__'
            else:
                variable = line[0]
                if not self.isVariable(variable):
                    return "Formula error: invalid variable"
            if self.setRoot(line[1]):
                pass
            else:
                return "Formula error: Calculation error"
            value = self.evaluateTree(self.treeRoot)
            if type(value) == str:
                return "Formula error: Invalid formula"
            else:
                self.varDic[variable] = value
        try:
            return self.varDic['__return__']
        except:
            return "Error: No return statement"
