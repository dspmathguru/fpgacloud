import os

from myhdl import Cosimulation

cmd = "iverilog -g2012 -o fir.o ../fir.v dut_fir.v"


def fir(clk, enable, inP, outP):
  os.system(cmd)
  return Cosimulation("vvp -m ./myhdl fir.o -fst",
                      clk=clk, enable=enable, inP=inP, outP=outP)
