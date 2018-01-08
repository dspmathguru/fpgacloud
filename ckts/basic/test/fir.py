import os

from myhdl import Cosimulation

cmd = "iverilog -g2012 -o fir.o ../fir.v dut_fir.v"


def fir(clk, resetn, enable, inP, outP, out_enable):
  os.system(cmd)
  return Cosimulation("vvp -m ./myhdl fir.o -fst",
                      clk=clk, resetn=resetn, enable=enable, inP=inP,
                      outP=outP, out_enable=out_enable)
