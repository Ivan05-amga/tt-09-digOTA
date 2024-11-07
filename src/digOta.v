module digOta (
    input Vip, 
    input Vin, 
    output Out
);
    wire INn, INp, Op, On, CM , En;


    assign INn = ~Vip; // IV1 
    assign INn = ~CM;  // IV2
    assign INp = ~Vin; //IV3 
    assign INp = ~CM;  //IV4 
    assign Op = ~INn; // IV5
    assign On = ~INp; //IV6 
    assign En = Op ^ On; // XOR1 
    assign Out = En ? Op : 1'b0; //BT1
    assign CM = ~En ? ~Op : 1'b0;


endmodule
