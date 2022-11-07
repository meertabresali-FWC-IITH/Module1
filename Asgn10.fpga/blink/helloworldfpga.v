module boolean(

    input   X,
    input   Y,
    input   Z,
    
    output  A,
    output  B,
    );

    
   assign A=(X&(Y|Z));
   assign B=((X&Y)|(X&Z));

    endmodule
