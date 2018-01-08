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


def checker(clk, enable, inP, outP):
  i = Signal(intbv(0))

  @always(clk.posedge)
  def check():
    enable.next = intbv(1)
    if i == 20:
      inP.next = intbv(1)
    else:
      inP.next = intbv(0)

    i.next = i + 1

  return check


clk = Signal(0)
enable = Signal(0)
inP = Signal(intbv(0)[16:])
outP = Signal(intbv(0)[16:])

clk_driver_inst = clk_driver(clk)
dut = fir(clk, enable, inP, outP)
check = checker(clk, enable, inP, outP)

sim = Simulation(clk_driver_inst, dut, check)
sim.run(2000)
