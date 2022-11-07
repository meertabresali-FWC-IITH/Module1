/* Generated by Yosys 0.9+2406 (git sha1 ca763e6d5, gcc 10.2.1-6 -fPIC -Os) */

(* top =  1  *)
(* src = "/data/data/com.termux/files/home/fpga-examples/blink/helloworldfpga.v:1.1-15.14" *)
module boolean(X, Y, Z, A, B);
  wire _0_;
  wire _1_;
  wire _2_;
  wire _3_;
  wire _4_;
  (* src = "/data/data/com.termux/files/home/fpga-examples/blink/helloworldfpga.v:7.13-7.14" *)
  output A;
  (* src = "/data/data/com.termux/files/home/fpga-examples/blink/helloworldfpga.v:8.13-8.14" *)
  output B;
  (* src = "/data/data/com.termux/files/home/fpga-examples/blink/helloworldfpga.v:3.13-3.14" *)
  input X;
  (* src = "/data/data/com.termux/files/home/fpga-examples/blink/helloworldfpga.v:4.13-4.14" *)
  input Y;
  (* src = "/data/data/com.termux/files/home/fpga-examples/blink/helloworldfpga.v:5.13-5.14" *)
  input Z;
  (* keep = 32'd1 *)
  outpad #(
    .IO_LOC("X20Y32"),
    .IO_PAD("33"),
    .IO_TYPE("BIDIR")
  ) _5_ (
    .A(_0_),
    .P(A)
  );
  (* keep = 32'd1 *)
  outpad #(
    .IO_LOC("X30Y32"),
    .IO_PAD("38"),
    .IO_TYPE("BIDIR")
  ) _6_ (
    .A(_1_),
    .P(B)
  );
  (* keep = 32'd1 *)
  inpad #(
    .IO_LOC("X10Y32"),
    .IO_PAD("27"),
    .IO_TYPE("BIDIR")
  ) _7_ (
    .P(X),
    .Q(_2_)
  );
  (* keep = 32'd1 *)
  inpad #(
    .IO_LOC("X12Y32"),
    .IO_PAD("28"),
    .IO_TYPE("BIDIR")
  ) _8_ (
    .P(Y),
    .Q(_3_)
  );
  (* keep = 32'd1 *)
  inpad #(
    .IO_LOC("X16Y32"),
    .IO_PAD("31"),
    .IO_TYPE("BIDIR")
  ) _9_ (
    .P(Z),
    .Q(_4_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:36.63-36.121" *)
  LUT3 #(
    .EQN("(~I0*I1*~I2)+(~I0*~I1*I2)+(~I0*I1*I2)"),
    .INIT(9'h0a8)
  ) A_LUT3_O (
    .I0(_2_),
    .I1(_3_),
    .I2(_4_),
    .O(_0_)
  );
  (* module_not_derived = 32'd1 *)
  (* src = "/data/data/com.termux/files/home/symbiflow/bin/../share/yosys/quicklogic/pp3_lut_map.v:36.63-36.121" *)
  LUT3 #(
    .EQN("(~I0*I1*~I2)+(~I0*~I1*I2)+(~I0*I1*I2)"),
    .INIT(9'h0a8)
  ) B_LUT3_O (
    .I0(_2_),
    .I1(_3_),
    .I2(_4_),
    .O(_1_)
  );
endmodule
