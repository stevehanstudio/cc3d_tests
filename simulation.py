from cc3d import CompuCellSetup
from cc3d.core.PySteppables import SteppableBasePy

class SimpleSteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)

    def start(self):
        cell = self.newCell(self.TESTCELL)
        self.cellField[20:30, 20:30, 0] = cell

    def step(self, mcs):
        for cell in self.cellList:
            cell.targetVolume += 1
            cell.lambdaVolume = 2.0

CompuCellSetup.register_steppable(steppable=SimpleSteppable(frequency=1))
