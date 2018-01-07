import os

from myhdl import Cosimulation

cmd = "iverilog -o fir.o ../fir.v dut_fir.v"


def fir(clk, enable, coeffs, inP, outP):
  os.system(cmd)
  return Cosimulation("vvp -m myhdl.vpi fir.o",
                      clk=clk, enable=enable, coeffs=coeffs, inP=inP, outP=outP)
