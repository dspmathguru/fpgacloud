module dut_fir
#(parameter
  BITWIDTH = 16,
  ACCWIDTH = 24,
  N = 16,
  P = 0 // assumes inP is an integer not 1.15, etc.
);
   reg 		    clk;
   reg 		    enable;

   //reg [(BITWIDTH*N)-1:0] coeffs;
   reg signed [BITWIDTH-1:0] cs [N-1:0];
   reg signed [BITWIDTH-1:0] inP;
   wire signed [BITWIDTH-1:0] outP;

   initial begin
      //$from_myhdl(clk, enable, coeffs, inP);
      $from_myhdl(clk, enable, inP);
      $to_myhdl(outP);
   end

   genvar i;
   generate
      for (i = 0; i < N; i = i + 1) begin
	 //assign cs[i] = coeffs[BITWIDTH*(i+1)-1:BITWIDTH*i];
	 assign cs[i] = i;
      end
   endgenerate

   fir #(.BITWIDTH(BITWIDTH), .ACCWIDTH(ACCWIDTH), .N(N), .P(P)) dut
     (clk, enable, cs, inP, outP);

   genvar j;
   generate
      for (j = 0; j < N; j = j+1) begin
	 initial begin
	    if (j == 0) begin
	       $dumpfile("fir.fst");
	       $dumpvars(0);
	    end

	    $dumpvars(0, cs[j]);
	    $dumpvars(0, dut.zs[j]);
	    $dumpvars(0, dut.mults[j]);
	 end
      end
   endgenerate

endmodule
