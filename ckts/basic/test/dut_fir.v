module dut_fir 
#(parameter
  BITWIDTH = 16,
  ACCWIDTH = 24,
  N = 16,
  P = 4  
);
   reg 		    clk;
   reg 		    enable;
   reg signed [BITWIDTH-1:0] coeffs [N-1:0];
   reg signed [BITWIDTH-1:0] inP;
   wire signed [BITWIDTH-1:0] outP;
   
   inital begin
      $from_myhdl(outP);
      $to_myhdl(clk, enable, coeffs, inP);
   end // UNMATCHED !!

   fir dut #(BITWIDTH, ACCWIDTH, N, P) (clk, enable, coeffs, inP, outP);

endmodule
