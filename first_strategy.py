# region imports
from AlgorithmImports import *
# endregion

class DeterminedRedBison(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 9, 23)
        self.SetEndDate(2021, 1,1)
        self.SetCash(100000)

        spy = self.AddEquity("SPY", Resolution.Daily)

        spy.SetDataNormalizationMode(DataNormalizationMode.Raw)

        self.spy = spy.Symbol

        self.SetBenchmark( "SPY")
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin)
        self.entryprice = 0
        self.period = timedelta(31)
        self.nextEntryTime = self.Time


    def OnData(self, data: Slice):
        #price = data.Bars[self.spy].Close 
        if not self.spy in data:
            return

        price = data[self.spy].Close 
        
        if not self.Portfolio.Invested:
            if self.nextEntryTime <= self.Time:
                self.SetHoldings(self.spy, 1)
                #self.MarketOrder(self.spy, int(self.Portfolio.Cash / price) )
                self.Log("BUY SPY @ " + str(price))
                self.entryprice = price
        
        elif self.entryprice * 1.1 < price or self.entryprice * 0.9 > price:
            self.Liquidate()
            self.Log("SELL SPY @" + str(price))
            self.nextEntryTime = self.Time + self.period
        