# Crypto Portfolio Optimizer
Cryptocurrencies portfolio optimizer and simulator (useful for investors and holders)

<img src="https://github.com/Erfaniaa/crypto-portfolio-optimizer/assets/7780269/2b599a3e-eb85-429c-9b5e-0edde79d2590" width="70%">

## Description
This is a dynamic tool designed for investors stepping into the world of cryptocurrencies. This project is an essential guide for those uncertain about which assets to include in their portfolio. By leveraging a simulation (backtest) mechanism, provides a data-driven approach to asset allocation. This tool works by this assumption: sometimes, the market repeats itself!

## Key Features
- Personalized Portfolio Simulation: Input your candidate cryptocurrencies and a specific time interval, and our tool will simulate (backtest) how these coins have performed historically.

- Optimal Allocation Strategies: Through an analysis, the tool suggests allocations for each asset in your portfolio, ensuring a diversified investment strategy.

- Brute-Force Algorithm for Precision: At its core, the project utilizes a brute-force (backtrack) algorithm. This technique meticulously tests various portfolio combinations to find the most effective one for your goals.

- Focus on Minimizing Drawdowns: A key objective of our tool is to minimize the drawdown in your wealth chart over time, enhancing the stability and reliability of your investments.

## What is Drawdown?
Drawdown in finance refers to the peak-to-trough decline during a specific recorded period of an investment, a trading account, or a fund. It is usually quoted as the percentage between the peak and the subsequent trough. If a trading account has $10,000 at the peak and then drops to $9,000 before rising again, the drawdown is 10%. Drawdowns are important for measuring the historical risk of different investments, comparing fund performance, or monitoring personal trading performance. A key goal in finance is to minimize drawdowns to preserve capital and ensure a smoother investment growth trajectory.

## Why Use This Tool?
Investing in cryptocurrencies can be daunting due to their volatile nature. This tool empowers you to make informed decisions based on historical performance analysis, thus helping to demystify the process of crypto investment and asset allocation. There are some seasonalities in cryptocurrency prices due to Bitcoin halvings, and we want to take advantage of these Bitcoin cycles. Whether you're a seasoned investor or new to the crypto world, our Crypto Portfolio Optimizer is your companion in building a resilient crypto portfolio.

## Installation
First, clone the repository and then run the following command.

```pip3 install -r requirements.txt```

## Config
You can change the `config.py` file to change the simulation parameters.
- `CANDIDATE_COINS` is a list of coins you want to buy. 
- `WEIGHTS_STEP_PRECISION_PERCENT`: if you set you set it to 20, your portfolio might be something like this: 20% BTC, 40% ETH, 60% ETH (each weight will be a factor of 20%)
- `SIMULATION_START_DATE` indicates the start time interval of the simulation.
- `SIMULATION_END_DATE` indicates the end time interval of the simulation.
- `START_WALLET_SIZE_USD` indicates the total amount of money (in the US Dollars) you want to invest.

## Usage
Just run the following command.

```python3 main.py```

## Notes
- The cryptocurrency market is risky. Do your own research before trading and investing. You are responsible for your own actions in trading and investing.
- Try setting `SIMULATION_START_DATE` and `SIMULATION_END_DATE` to almost four years ago. Bitcoin halvings happen every four years, so some patterns may be repeated (obviously, it's not guaranteed).
