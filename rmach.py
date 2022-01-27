from collections import defaultdict

class machine:

    def __init__(self):
        self.regs = defaultdict(int)
        self.lbls = defaultdict(int)
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
            if type(q) == str:
                self.ptr = self.lbls[q] - 1
            else:
                self.ptr = q - 1

    def CheckLabel(self, l):
        lbl = l.strip()
        return len(lbl) and lbl[0] == '@' and lbl[1:]

    def SaveLabel(self, lbl, ptr):
        self.lbls['@' + lbl.strip()] = ptr

    def DeleteComments(self, l):
        hsh = l.find('#')
        if hsh != -1:
            return l[:hsh].strip()
        return l.strip()

    def LoadProg(self, file):
        with open(file, 'r') as f:
            ptr = 1
            for l in f:
                if lbl := self.CheckLabel(l):
                    self.SaveLabel(lbl, ptr)
                elif s := self.DeleteComments(l):
                    self.cmds.append(f'self.{s}')
                    ptr += 1 

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
    m.LoadProg('examples/mod3.txt')
    m.SetRegs({'a': 12})
    m.Run()
    print(m.lbls)