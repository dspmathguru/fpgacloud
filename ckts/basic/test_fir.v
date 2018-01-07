`timescale 1 ns / 100 ps

module test_fir
  #( parameter
     BITWIDTH = 16,
     ACCWIDTH = 24,
     N = 16,
     P = 4
     )
   ();

   reg clk;
   reg 	  enable;
 
   reg signed [BITWIDTH-1:0] coeffs [N-1:0];
   reg signed [BITWIDTH-1:0] inP;
   wire signed [BITWIDTH-1:0] outP;

   always
     #10 clk = ~clk;
   
   integer 		      i;
   initial begin
      clk = 0;
      enable = 1'b1;
      inP = {N{1'b0}};

      for (i = 0; i < N; i = i + 1) begin
	 coeffs[i] = i;
      end
   end

   always @(posedge clk) begin
      inP = inP + 1;
   end

   fir u1(.clk(clk), .enable(enable), .coeffs(coeffs), .inP(inP), .outP(outP));

   integer idx;
   initial begin
      $dumpfile("test_fir.lxt");
      $dumpvars;
      for (idx = 0; idx < N; idx = idx + 1) begin
	 $dumpvars(0, test_fir.u1.coeffs[idx]);
      end
   end

   integer stop_counter;
   initial begin
      stop_counter = 0;
   end

   always @(posedge clk) begin
      stop_counter = stop_counter + 1;
      if (stop_counter > 100) $finish;
   end

endmodule





