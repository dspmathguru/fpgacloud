module fir
#( parameter
   BITWIDTH = 16,
   ACCWIDTH = 24,
   N = 16,
   P = 4
)
(
 input wire 		    clk,
 input wire 		    enable,
 
 input signed [BITWIDTH-1:0]  coeffs [N-1:0],

 input signed [BITWIDTH-1:0]  inP,
 output signed [BITWIDTH-1:0] outP
 );
   reg signed [BITWIDTH+P-1:0] acc [N-1:0];
   reg signed [BITWIDTH+P-1:0] outAcc;
   reg signed [2*BITWIDTH-1:0] mults [N-1:0];
   reg signed [BITWIDTH-1:0]   zs [N-1:0];
   
   wire signed [BITWIDTH-1:0]  outP;

   genvar 		       i;
   generate
      for (i = 0; i < N; i = i+1) begin
	 always @(posedge clk) begin
	    if (enable) begin
	       if (i > 0 && i < N) begin
		  mults[i] <= zs[i] * coeffs[i];
		  zs[i] <= zs[i-1];
	       end
	       else if (i == 0) begin
		  mults[i] <= inP * coeffs[i];
		  zs[i] <= inP;
	       end
	    end
	 end
      end
   endgenerate

   genvar j;
   generate
      for (j = 0; j < N; j = j+1) begin
	 always @(*) begin
	    if (j == 0)
	      acc[j] <= mults[j];
	    else
	      acc[j] <= mults[j] + acc[j-1];
	 end
      end
   endgenerate

   assign outAcc = acc[N-1];
   assign outP = outAcc[BITWIDTH+P-1:P];
   
endmodule
