MockDecOperSist = [
    "***********************************************************************\n",
    "*                                                                     *\n",
    "*            CEPEL - CENTRO DE PESQUISAS DE ENERGIA ELETRICA          *\n",
    "*  CEPEL: DECOMP     - Versao 31.14 - Dez/2022(L)                     *\n",
    "*                                                                     *\n",
    "***********************************************************************\n",
    "\n",
    "\n",
    "   PROGRAMA LICENCIADO PARA OPERADOR NACIONAL DO SISTEMA ELETRICO ONS                                                                                                             \n",
    "\n",
    "\n",
    "____________________________________________________________________\n",
    "\n",
    " Backtest Preliminar CPAMP 2022-2023 - Hibrido DECOMP 01/2020 rv4                \n",
    "____________________________________________________________________\n",
    "\n",
    "--------------------------------------\n",
    "Resultado de operacao dos subsistemas.                                          \n",
    "--------------------------------------\n",
    "---------------------------------------------------\n",
    "IPER;      Indice do periodo                                                                                                                                                                            \n",
    "INO;       Indice do no                                                                                                                                                                                 \n",
    "ICEN;      Indice do cenario                                                                                                                                                                            \n",
    "IPAT;      Patamar de Carga                                                                                                                                                                             \n",
    "Dur;       Duracao                                                                                                                                                                                      \n",
    "SIST;      Numero do subsistema                                                                                                                                                                         \n",
    "Nome Sist; Nome do subsistema                                                                                                                                                                           \n",
    "Demanda;   Demanda                                                                                                                                                                                      \n",
    "GerPeq;    Geracao das pequenas usinas                                                                                                                                                                  \n",
    "Gter;      Geracao Termoeletrica                                                                                                                                                                        \n",
    "GterAT;    Geracao termica antecipada                                                                                                                                                                   \n",
    "Ghid;      Gero hidroeletrica                                                                                                                                                                        \n",
    "Geol;      Geracao eolica                                                                                                                                                                               \n",
    "Cbomb;     Energia Consumida para bombeamento                                                                                                                                                           \n",
    "Compra;    Energia importada                                                                                                                                                                            \n",
    "Venda;     Energia exportada                                                                                                                                                                            \n",
    "IntercLiq; Saldo da energia de intercambio                                                                                                                                                              \n",
    "Itaipu50;  Geracao 50Hz de Itaipu                                                                                                                                                                       \n",
    "Itaipu60;  Geracao 60Hz de Itaipu                                                                                                                                                                       \n",
    "Deficit;   Deficit no Subsistema                                                                                                                                                                        \n",
    "ENA;       Energia Afluente                                                                                                                                                                             \n",
    "EarmInic;  Energia Armazenada Inicial                                                                                                                                                                   \n",
    "EarmInic%; Energia Armazenada Inicial em percentual                                                                                                                                                     \n",
    "EarmFim;   Energia Armazenada Final                                                                                                                                                                     \n",
    "EarmFim%;  Energia Armazenada Final em percentual                                                                                                                                                       \n",
    "CMO;       Custo Marginal de Operacao                                                                                                                                                                   \n",
    "---------------------------------------------------\n",
    "\n",
    "@Tabela\n",
    "-----;------;------;-----;--------;----;---------------;------------;----------;----------;----------;----------;----------;----------;----------;----------;------------;----------;----------;----------;----------;---------------;----------;---------------;----------;---------;\n",
    "IPER ; INO  ; ICEN ;IPAT ;  Dur   ;SIST;   Nome Sist   ;  Demanda   ;  GerPeq  ;   Gter   ;  GterAT  ;   Ghid   ;   Geol   ;  Cbomb   ;  Compra  ;  Venda   ; IntercLiq  ; Itaipu50 ; Itaipu60 ; Deficit  ;   ENA    ;   EarmInic    ;EarmInic% ;    EarmFim    ; EarmFim% ;   CMO   ;\n",
    "  -  ;  -   ;  -   ;  -  ;  (h)   ; -  ;       -       ;    (MW)    ;   (MW)   ;   (MW)   ;   (MW)   ;   (MW)   ;   (MW)   ;   (MW)   ;   (MW)   ;   (MW)   ;    (MW)    ;   (MW)   ;   (MW)   ;   (MW)   ; (MWmes)  ;    (MWmes)    ;   (%)    ;    (MWmes)    ;   (%)    ; ($/MWh) ;\n",
    "-----;------;------;-----;--------;----;---------------;------------;----------;----------;----------;----------;----------;----------;----------;----------;------------;----------;----------;----------;----------;---------------;----------;---------------;----------;---------;\n",
    "   1 ;    1 ;    1 ;   1 ;  40.00 ;  1 ; SE            ;    48383.0 ;   3374.0 ;  6509.80 ;   548.00 ; 33567.62 ;     0.00 ;    13.58 ;     0.00 ;     0.00 ;    7576.16 ;  1900.00 ;  5009.89 ;     0.00 ;  12608.1 ;      47877.48 ;    23.43 ;      52743.55 ;    25.81 ;  956.18 ;\n",
    "   1 ;    1 ;    1 ;   2 ;  46.00 ;  1 ; SE            ;    44961.0 ;   3374.0 ;  6388.30 ;   547.60 ; 29077.62 ;     0.00 ;   115.60 ;     0.00 ;     0.00 ;    8207.08 ;  1900.00 ;  5670.89 ;     0.00 ;  12608.1 ;      47877.48 ;    23.43 ;      52743.55 ;    25.81 ;  923.10 ;\n",
    "   1 ;    1 ;    1 ;   3 ;  82.00 ;  1 ; SE            ;    37812.0 ;   3374.0 ;  6388.30 ;   546.60 ; 23161.62 ;     0.00 ;   115.60 ;     0.00 ;     0.00 ;    6031.08 ;  1900.00 ;  2865.60 ;     0.00 ;  12608.1 ;      47877.48 ;    23.43 ;      52743.55 ;    25.81 ;  870.31 ;\n",
    "   1 ;    1 ;    1 ;  -  ;   -    ;  1 ; SE            ;    42286.4 ;   3374.0 ;  6417.23 ;   547.21 ; 27259.10 ;     0.00 ;    91.31 ;     0.00 ;     0.00 ;    6994.77 ;  1900.00 ;  4144.26 ;     0.00 ;  12608.1 ;      47877.48 ;    23.43 ;      52743.55 ;    25.81 ;  905.21 ;\n",
    "   1 ;    1 ;    1 ;   1 ;  40.00 ;  2 ; S             ;    16123.0 ;   2065.0 ;  1901.10 ;     0.00 ;  4190.49 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    7966.41 ;    -     ;    -     ;     0.00 ;    496.6 ;       5781.02 ;    29.05 ;       5777.39 ;    29.04 ;  956.18 ;\n",
    "   1 ;    1 ;    1 ;   2 ;  46.00 ;  2 ; S             ;    14100.0 ;   2065.0 ;  1897.80 ;     0.00 ;  2045.77 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    8091.43 ;    -     ;    -     ;     0.00 ;    496.6 ;       5781.02 ;    29.05 ;       5777.39 ;    29.04 ;  923.11 ;\n",
    "   1 ;    1 ;    1 ;   3 ;  82.00 ;  2 ; S             ;    11458.0 ;   2065.0 ;  1888.30 ;     0.00 ;  1451.50 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    6053.20 ;    -     ;    -     ;     0.00 ;    496.6 ;       5781.02 ;    29.05 ;       5777.39 ;    29.04 ;  870.31 ;\n",
    "   1 ;    1 ;    1 ;  -  ;   -    ;  2 ; S             ;    13292.1 ;   2065.0 ;  1893.95 ;     0.00 ;  2266.36 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    7066.81 ;    -     ;    -     ;     0.00 ;    496.6 ;       5781.02 ;    29.05 ;       5777.39 ;    29.04 ;  905.21 ;\n",
    "   1 ;    1 ;    1 ;   1 ;  40.00 ;  3 ; NE            ;    13081.0 ;   5662.0 ;  3278.80 ;     0.00 ;  3329.23 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     810.97 ;    -     ;    -     ;     0.00 ;   1630.3 ;      20038.22 ;    38.83 ;      20818.72 ;    40.34 ;  881.71 ;\n",
    "   1 ;    1 ;    1 ;   2 ;  46.00 ;  3 ; NE            ;    12265.0 ;   5662.0 ;  3468.60 ;     0.00 ;  3953.21 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    -818.81 ;    -     ;    -     ;     0.00 ;   1630.3 ;      20038.22 ;    38.83 ;      20818.72 ;    40.34 ;  881.71 ;\n",
    "   1 ;    1 ;    1 ;   3 ;  82.00 ;  3 ; NE            ;    10967.0 ;   5662.0 ;  3278.80 ;     0.00 ;  2148.73 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    -122.53 ;    -     ;    -     ;     0.00 ;   1630.3 ;      20038.22 ;    38.83 ;      20818.72 ;    40.34 ;  870.31 ;\n",
    "   1 ;    1 ;    1 ;  -  ;   -    ;  3 ; NE            ;    11825.7 ;   5662.0 ;  3330.77 ;     0.00 ;  2923.89 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     -90.92 ;    -     ;    -     ;     0.00 ;   1630.3 ;      20038.22 ;    38.83 ;      20818.72 ;    40.34 ;  876.15 ;\n",
    "   1 ;    1 ;    1 ;   1 ;  40.00 ;  4 ; N             ;     5878.0 ;    567.0 ;  2936.50 ;     0.00 ; 13718.14 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;  -11343.64 ;    -     ;    -     ;     0.00 ;   1423.3 ;       3217.80 ;    21.27 ;       3215.86 ;    21.26 ;  881.71 ;\n",
    "   1 ;    1 ;    1 ;   2 ;  46.00 ;  4 ; N             ;     5755.0 ;    567.0 ;  3002.80 ;     0.00 ; 11994.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;   -9808.80 ;    -     ;    -     ;     0.00 ;   1423.3 ;       3217.80 ;    21.27 ;       3215.86 ;    21.26 ;  881.71 ;\n",
    "   1 ;    1 ;    1 ;   3 ;  82.00 ;  4 ; N             ;     5431.0 ;    567.0 ;  3027.90 ;     0.00 ; 10932.25 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;   -9096.15 ;    -     ;    -     ;     0.00 ;   1423.3 ;       3217.80 ;    21.27 ;       3215.86 ;    21.26 ;  870.31 ;\n",
    "   1 ;    1 ;    1 ;  -  ;   -    ;  4 ; N             ;     5626.1 ;    567.0 ;  2999.27 ;     0.00 ; 11886.28 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;   -9826.40 ;    -     ;    -     ;     0.00 ;   1423.3 ;       3217.80 ;    21.27 ;       3215.86 ;    21.26 ;  876.15 ;\n",
    "   1 ;    1 ;    1 ;   1 ;  40.00 ; 11 ; FC            ;        0.0 ;      0.0 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;       0.00 ;    -     ;    -     ;     0.00 ;    -     ;       -       ;    -     ;       -       ;    -     ;  881.71 ;\n",
    "   1 ;    1 ;    1 ;   2 ;  46.00 ; 11 ; FC            ;        0.0 ;      0.0 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;       0.00 ;    -     ;    -     ;     0.00 ;    -     ;       -       ;    -     ;       -       ;    -     ;  881.71 ;\n",
    "   1 ;    1 ;    1 ;   3 ;  82.00 ; 11 ; FC            ;        0.0 ;      0.0 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;       0.00 ;    -     ;    -     ;     0.00 ;    -     ;       -       ;    -     ;       -       ;    -     ;  870.31 ;\n",
    "   1 ;    1 ;    1 ;  -  ;   -    ; 11 ; FC            ;        0.0 ;      0.0 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;       0.00 ;    -     ;    -     ;     0.00 ;    -     ;       -       ;    -     ;       -       ;    -     ;  876.15 ;\n",
    "   2 ;    2 ;    1 ;   1 ; 152.00 ;  1 ; SE            ;    49356.0 ;   3502.0 ;  3173.90 ;   550.00 ; 37933.58 ;     0.00 ;    21.26 ;     0.00 ;     0.00 ;    7166.78 ;  3500.00 ;  6629.00 ;     0.00 ;  77693.9 ;      52743.55 ;    25.81 ;      88531.65 ;    43.33 ;  158.03 ;\n",
    "   2 ;    2 ;    1 ;   2 ; 182.00 ;  1 ; SE            ;    45816.0 ;   3502.0 ;  3175.90 ;   550.00 ; 34855.16 ;     0.00 ;    98.77 ;     0.00 ;     0.00 ;    6168.71 ;  3500.00 ;  6150.97 ;     0.00 ;  77693.9 ;      52743.55 ;    25.81 ;      88531.65 ;    43.33 ;  146.71 ;\n",
    "   2 ;    2 ;    1 ;   3 ; 362.00 ;  1 ; SE            ;    38351.0 ;   3502.0 ;  2636.90 ;   550.00 ; 27230.66 ;     0.00 ;   115.60 ;     0.00 ;     0.00 ;    6007.04 ;  1900.00 ;  4520.20 ;     0.00 ;  77693.9 ;      52743.55 ;    25.81 ;      88531.65 ;    43.33 ;   55.16 ;\n",
    "   2 ;    2 ;    1 ;  -  ;   -    ;  1 ; SE            ;    42706.4 ;   3502.0 ;  2895.12 ;   550.00 ; 31561.84 ;     0.00 ;    90.60 ;     0.00 ;     0.00 ;    6302.59 ;  2667.82 ;  5407.18 ;     0.00 ;  77693.9 ;      52743.55 ;    25.81 ;      88531.65 ;    43.33 ;  101.57 ;\n",
    "   2 ;    2 ;    1 ;   1 ; 152.00 ;  2 ; S             ;    15552.0 ;   1690.0 ;   732.30 ;     0.00 ;  4308.35 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    8821.35 ;    -     ;    -     ;     0.00 ;   3338.6 ;       5777.39 ;    29.04 ;       7183.46 ;    36.10 ;  158.03 ;\n",
    "   2 ;    2 ;    1 ;   2 ; 182.00 ;  2 ; S             ;    13575.0 ;   1690.0 ;   741.90 ;     0.00 ;  2305.49 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    8837.61 ;    -     ;    -     ;     0.00 ;   3338.6 ;       5777.39 ;    29.04 ;       7183.46 ;    36.10 ;  146.71 ;\n",
    "   2 ;    2 ;    1 ;   3 ; 362.00 ;  2 ; S             ;    11070.0 ;   1690.0 ;   680.50 ;     0.00 ;  1067.92 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    7631.58 ;    -     ;    -     ;     0.00 ;   3338.6 ;       5777.39 ;    29.04 ;       7183.46 ;    36.10 ;   55.16 ;\n",
    "   2 ;    2 ;    1 ;  -  ;   -    ;  2 ; S             ;    12703.9 ;   1690.0 ;   707.87 ;     0.00 ;  2099.22 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    8206.79 ;    -     ;    -     ;     0.00 ;   3338.6 ;       5777.39 ;    29.04 ;       7183.46 ;    36.10 ;  101.57 ;\n",
    "   2 ;    2 ;    1 ;   1 ; 152.00 ;  3 ; NE            ;    13028.0 ;   4839.0 ;  1465.20 ;     0.00 ;  4082.93 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    2640.87 ;    -     ;    -     ;     0.00 ;  10800.8 ;      20818.72 ;    40.34 ;      28879.74 ;    55.96 ;  158.03 ;\n",
    "   2 ;    2 ;    1 ;   2 ; 182.00 ;  3 ; NE            ;    12347.0 ;   4839.0 ;  1465.20 ;     0.00 ;  2420.13 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    3622.67 ;    -     ;    -     ;     0.00 ;  10800.8 ;      20818.72 ;    40.34 ;      28879.74 ;    55.96 ;  146.71 ;\n",
    "   2 ;    2 ;    1 ;   3 ; 362.00 ;  3 ; NE            ;    10894.0 ;   4839.0 ;   371.20 ;     0.00 ;  1851.28 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    3832.52 ;    -     ;    -     ;     0.00 ;  10800.8 ;      20818.72 ;    40.34 ;      28879.74 ;    55.96 ;   55.16 ;\n",
    "   2 ;    2 ;    1 ;  -  ;   -    ;  3 ; NE            ;    11740.0 ;   4839.0 ;   896.19 ;     0.00 ;  2487.40 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    3517.40 ;    -     ;    -     ;     0.00 ;  10800.8 ;      20818.72 ;    40.34 ;      28879.74 ;    55.96 ;  101.57 ;\n",
    "   2 ;    2 ;    1 ;   1 ; 152.00 ;  4 ; N             ;     6328.0 ;    437.0 ;  1648.40 ;     0.00 ; 16242.60 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;  -12000.00 ;    -     ;    -     ;     0.00 ;  12538.5 ;       3215.86 ;    21.83 ;       8796.75 ;    59.71 ;  109.23 ;\n",
    "   2 ;    2 ;    1 ;   2 ; 182.00 ;  4 ; N             ;     6237.0 ;    437.0 ;  1627.40 ;     0.00 ; 16172.60 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;  -12000.00 ;    -     ;    -     ;     0.00 ;  12538.5 ;       3215.86 ;    21.83 ;       8796.75 ;    59.71 ;  109.23 ;\n",
    "   2 ;    2 ;    1 ;   3 ; 362.00 ;  4 ; N             ;     5780.0 ;    437.0 ;   650.50 ;     0.00 ; 15534.64 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;  -10842.14 ;    -     ;    -     ;     0.00 ;  12538.5 ;       3215.86 ;    21.83 ;       8796.75 ;    59.71 ;   55.16 ;\n",
    "   2 ;    2 ;    1 ;  -  ;   -    ;  4 ; N             ;     6019.2 ;    437.0 ;  1123.88 ;     0.00 ; 15856.08 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;  -11397.78 ;    -     ;    -     ;     0.00 ;  12538.5 ;       3215.86 ;    21.83 ;       8796.75 ;    59.71 ;   81.11 ;\n",
    "   2 ;    2 ;    1 ;   1 ; 152.00 ; 11 ; FC            ;        0.0 ;      0.0 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;       0.00 ;    -     ;    -     ;     0.00 ;    -     ;       -       ;    -     ;       -       ;    -     ;  109.23 ;\n",
    "   2 ;    2 ;    1 ;   2 ; 182.00 ; 11 ; FC            ;        0.0 ;      0.0 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;       0.00 ;    -     ;    -     ;     0.00 ;    -     ;       -       ;    -     ;       -       ;    -     ;  109.23 ;\n",
    "   2 ;    2 ;    1 ;   3 ; 362.00 ; 11 ; FC            ;        0.0 ;      0.0 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;       0.00 ;    -     ;    -     ;     0.00 ;    -     ;       -       ;    -     ;       -       ;    -     ;   55.16 ;\n",
    "   2 ;    2 ;    1 ;  -  ;   -    ; 11 ; FC            ;        0.0 ;      0.0 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;       0.00 ;    -     ;    -     ;     0.00 ;    -     ;       -       ;    -     ;       -       ;    -     ;   81.11 ;\n",
    "   2 ;    3 ;    2 ;   1 ; 152.00 ;  1 ; SE            ;    49356.0 ;   3502.0 ;  6488.30 ;   550.00 ; 30754.89 ;     0.00 ;    21.26 ;     0.00 ;     0.00 ;   11031.07 ;  3500.00 ;  6629.00 ;     0.00 ;  54667.3 ;      52743.55 ;    25.81 ;      72795.86 ;    35.63 ;  777.75 ;\n",
    "   2 ;    3 ;    2 ;   2 ; 182.00 ;  1 ; SE            ;    45816.0 ;   3502.0 ;  6490.30 ;   550.00 ; 27312.62 ;     0.00 ;   112.54 ;     0.00 ;     0.00 ;   10410.61 ;  3500.00 ;  6150.97 ;     0.00 ;  54667.3 ;      52743.55 ;    25.81 ;      72795.86 ;    35.63 ;  762.47 ;\n",
    "   2 ;    3 ;    2 ;   3 ; 362.00 ;  1 ; SE            ;    38351.0 ;   3502.0 ;  6481.30 ;   550.00 ; 23898.37 ;     0.00 ;   115.60 ;     0.00 ;     0.00 ;    5494.93 ;  1900.00 ;  4520.20 ;     0.00 ;  54667.3 ;      52743.55 ;    25.81 ;      72795.86 ;    35.63 ;  745.90 ;\n",
    "   2 ;    3 ;    2 ;  -  ;   -    ;  1 ; SE            ;    42706.4 ;   3502.0 ;  6485.18 ;   550.00 ; 26288.58 ;     0.00 ;    94.20 ;     0.00 ;     0.00 ;    7989.39 ;  2667.82 ;  5407.18 ;     0.00 ;  54667.3 ;      52743.55 ;    25.81 ;      72795.86 ;    35.63 ;  757.19 ;\n",
    "   2 ;    3 ;    2 ;   1 ; 152.00 ;  2 ; S             ;    15552.0 ;   1690.0 ;  1507.40 ;     0.00 ;  7148.85 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    5205.75 ;    -     ;    -     ;     0.00 ;   4047.4 ;       5777.39 ;    29.04 ;       5775.34 ;    29.03 ;  777.75 ;\n",
    "   2 ;    3 ;    2 ;   2 ; 182.00 ;  2 ; S             ;    13575.0 ;   1690.0 ;  1517.00 ;     0.00 ;  4805.38 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    5562.62 ;    -     ;    -     ;     0.00 ;   4047.4 ;       5777.39 ;    29.04 ;       5775.34 ;    29.03 ;  762.47 ;\n",
    "   2 ;    3 ;    2 ;   3 ; 362.00 ;  2 ; S             ;    11070.0 ;   1690.0 ;  1543.70 ;     0.00 ;  3210.00 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    4626.30 ;    -     ;    -     ;     0.00 ;   4047.4 ;       5777.39 ;    29.04 ;       5775.34 ;    29.03 ;  745.90 ;\n",
    "   2 ;    3 ;    2 ;  -  ;   -    ;  2 ; S             ;    12703.9 ;   1690.0 ;  1528.79 ;     0.00 ;  4487.39 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;    4997.69 ;    -     ;    -     ;     0.00 ;   4047.4 ;       5777.39 ;    29.04 ;       5775.34 ;    29.03 ;  757.19 ;\n",
    "   2 ;    3 ;    2 ;   1 ; 152.00 ;  3 ; NE            ;    13028.0 ;   4839.0 ;  2939.70 ;     0.00 ;  4817.86 ;     0.00 ;     0.00 ;     0.00 ;     0.00 ;     431.44 ;    -     ;    -     ;     0.00 ;   3646.6 ;      20818.72 ;    40.34 ;      20895.20 ;    40.49 ;  777.75 ;\n",
    "\n",
]