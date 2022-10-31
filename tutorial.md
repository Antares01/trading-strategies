# QuantConnect Tutorial

QuantConnect is a browser-based algorithmic trading platform based on the LEAN algorithmic trading engine.

### LEAN Installation

Install LEAN CLI from https://github.com/QuantConnect/lean-cli. For more information consult the [*Getting Started*](https://www.lean.io/docs/v2/lean-cli/key-concepts/getting-started) section of the LEAN CLI documentation. The LEAN documentation can be found at https://www.lean.io/docs/v2. 

### The QuantConnect API
The [*Writing Algorithms*](https://www.quantconnect.com/docs/v2/writing-algorithms) section of the [QuantConnect documentation](https://www.quantconnect.com/docs/v2) 
provides a good starting point.

#### Basics
New strategies are written extending the QCAlgorithm class.

*Initialize()* &rarr; set parameters for backtest, add equities

*OnData()* &rarr;  actions performed every time we get a new detapoint (place orders based on conditions, update data structures, ...)

#### Brokerage Models
QuantConnect provides different brokerages models for backtesting and live trading. For more information consult the
[*Reality Modeling*](https://www.quantconnect.com/docs/v2/writing-algorithms/reality-modeling/key-concepts) section of the QuantConnect documentation.
