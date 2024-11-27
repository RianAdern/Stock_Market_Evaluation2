

dicionario =[('S&P 500','^GSPC'),('Dow Jones Industrial Average','^DJI'),
            ('NASDAQ Composite','^IXIC'),('Nasdaq 100 Mar 24','NQ=F'),('Russell 2000','^RUT'),
            ('Crude Oil Apr 24','CL=F'),('Gold Apr 24 ','GC=F'),('Silver May 24','SI=F'),
            ('EUR/USD','EURUSD=X'),('GBP/USD','GBPUSD=X'),('USD/JPY','JPY=X'),('Bitcoin USD','BTC-USD'),
            ('FTSE 100 GBP','^FTSE'),('Nikkei 225 Osaka','^N225'),
            ('EUR/BRL','EURBRL=X'),('IBOVESPA','^BVSP'),('USD/BRL','BRL=X'),('IPC MEXICO','^MXX'),
            ]

#CodeStock = 0 #dicionario[]
print(dicionario[15])
print(dicionario[15][0])

for i in dicionario:
    print(i[1])