from AlgorithmImports import *


class SMACrossoverTest(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2021, 12, 1)  # Set Start Date
        self.SetEndDate(2021, 12, 31)  # Set End Date
        self.SetCash(10000)  # Set Strategy Cash
        
        self.AddCrypto("BTCUSD")
        
        #self.SetBenchmark("BTCUSD")

        self.fast = self.SMA("BTCUSD", 5, Resolution.Minute)
        self.slow = self.SMA("BTCUSD", 60, Resolution.Minute)        

        self.previousTime = None        
        
        
    def OnData(self, data):
        if not self.slow.IsReady:
            return
        
        # check only once per minute
        if self.previousTime is not None and self.previousTime.minute == self.Time.minute:
            return        
        
        # small "tolerance" on checks to avoid bouncing
        tolerance = 0#.00015
    
        holdings = self.Portfolio["BTCUSD"].Quantity                
        
        # Not Holding + Crossover -> BUY        
        if holdings <= 0 and self.fast.Current.Value > self.slow.Current.Value *(1 + tolerance):
            #self.Log("BUY  >> {0}".format(self.Securities["BTCUSD"].Price))
            self.SetHoldings("BTCUSD", 1.0)

        # Holding + Crossunder -> SELL
        if holdings > 0 and self.fast.Current.Value < self.slow.Current.Value:
            #self.Log("SELL >> {0}".format(self.Securities["BTCUSD"].Price))
            self.Liquidate("BTCUSD")

        self.previousTime = self.Time        

        





