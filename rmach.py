from collections import defaultdict

class machine:

    def __init__(self):
        self.regs = defaultdict(int)
        self.cmds = [0]
        self.ptr = 1

    def Z(self, n):
        self.regs[n] = 0

    def S(self, n):
        self.regs[n] += 1

    def T(self, m, n):
        self.regs[n] = self.regs[m]

    def J(self, m, n, q):
        if self.regs[m] == self.regs[n]:
            self.ptr = q - 1

    def DeleteComments(self, l):
        hsh = l.find('#')
        if hsh != -1:
            return l[:hsh].strip()
        return l.strip()

    def LoadProg(self, file):
        with open(file, 'r') as f:
            for l in f:
                if s := self.DeleteComments(l):
                    self.cmds.append(f'self.{s}')

    def SetRegs(self, reg):
        self.regs.update(reg)

    def Step(self):
        eval(self.cmds[self.ptr])
        self.ptr += 1

    def Run(self):
        while self.ptr < len(self.cmds):
            print(self)
            self.Step()
             
    def __str__(self):
        return str(self.regs.items())[len('dict_items'):] + '\n' + self.cmds[self.ptr][len('self.'):]


if __name__ == '__main__':
    m = machine()
    m.LoadProg('examples/mult.txt')
    m.SetRegs({'x':3, 'a': 5})
    m.Run()