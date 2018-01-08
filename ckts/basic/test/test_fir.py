import myhdl
from myhdl import Simulation, Signal, delay, intbv, bin, always

from fir import fir

BITWIDTH = 16
ACCWIDTH = 24
N = 16
P = 4


def clk_driver(clk, period=10):
  @always(delay(period // 2))
  def driver():
    clk.next = not clk

  return driver


def checker(clk, resetn, enable, inP, outP, out_enable):
  i = Signal(intbv(0))
  j = Signal(intbv(0))

  @always(clk.posedge)
  def check():
    if i == 20:
      resetn.next = intbv(1)

    if i == 40:
      enable.next = True
      inP.next = intbv(1)
    else:
      inP.next = intbv(0)

    i.next = i + 1

    if out_enable == 1:
      if outP != j + 1 and j < 16:
        print("ERROR: outP = ", outP, " not same as j = ", j)
      if outP != 0 and j > 16:
        print("ERROR: outP = ", outP, " not same as j = ", j)
      j.next = j + 1

  return check


clk = Signal(0)
resetn = Signal(0)
enable = Signal(0)
inP = Signal(intbv(0)[16:])
outP = Signal(intbv(0)[16:])
out_enable = Signal(0)

clk_driver_inst = clk_driver(clk)
dut = fir(clk, resetn, enable, inP, outP, out_enable)
check = checker(clk, resetn, enable, inP, outP, out_enable)

sim = Simulation(clk_driver_inst, dut, check)
sim.run(2000)
