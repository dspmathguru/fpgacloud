import unittest

from myhdl import Simlation, Signal, delay, intbv, bin, , always

from fir import fir


class TestFIR(unittest.TestCase):
  def test1(self):
    def test(clk, enable, coeffs, inP, outP):
      for i in range(16):
        coeffs[i].next = intbv(i)[16:]
      enable.next = intbv(1)
      for i in range(16):
        if i == 1:
          inP.next = intbv(1)[16:]
        else:
          inP.next = intbv(0)[16:]
        yield delay(10)
        diff = bin(coeffs[i] - outP)
        self.assertEqual(diff.count('1'), 0)

    self.runTests(test)

  def runTests(self, test):
    enable = Signal(intbv(0)[1:])
    clk = Signal(intbv(0)[1:])
    coeffs = []
    for i in range(16):
      coeffs.append(Signal(intbv(0)[16:]))
    inP = Signal(intbv(0)[16:])
    outP = Signal(intbv(0)[16:])
    dut = fir(clk, enable, coeffs, inP, outP)
    check = test(clk, enable, coeffs, inP, outP)
    sim = Simulation(dut, check)
    sim.run(quiet=1)


if __name__ = '__main__':
  unittest.main(verbosity=2)
