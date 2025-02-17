import yfinance
from metrics import Metrics


class WalletSimulator:
	def __init__(self, start_wallet_size_usd, coins, weights, simulation_start_date, simulation_end_date):
		self.wallet_usd_over_days = []
		self.metrics = {}
		self.start_wallet_size_usd = start_wallet_size_usd
		self.coins = coins
		self.weights = weights
		self.coin_prices = {}
		self.simulation_start_date = simulation_start_date
		self.simulation_end_date = simulation_end_date
	
	def set_weights(self, weights):
		self.weights = weights

	def generate_metrics(self):
		return_percent = Metrics.calculate_return_percent(self.wallet_usd_over_days)
		maximum_drawdown_percent = Metrics.calculate_max_drawdown_percent(self.wallet_usd_over_days)
		self.metrics = {"return_percent": return_percent, "maximum_drawdown_percent": maximum_drawdown_percent}
	
	def load_all_coins_prices(self):
		for coin in self.coins:
			print("Downloading data for coin", coin)
			self.load_coin_prices(coin)
			print()

	def load_coin_prices(self, coin):
		df = yfinance.download(coin + "-USD", start=self.simulation_start_date, end=self.simulation_end_date, interval="1d", auto_adjust=True, prepost=True, threads=True)
		df = df.reset_index()
		df = df.dropna()
		df = df.loc[~df.apply(lambda row: (row == 0).any(), axis=1)]
		if df.shape[0] == 0:
			print("No data for " + coin)
			exit()
		df = df.dropna()
		coin_prices_list = df['Close'].squeeze().astype(float).tolist()
		self.coin_prices[coin] = coin_prices_list

	def generate_wallet_usd_over_days(self):
		self.wallet_usd_over_days = []
		min_coins_prices_len = 365 * 100
		for coin in self.coins:
			min_coins_prices_len = min(min_coins_prices_len, len(self.coin_prices[coin]))
		for i in range(min_coins_prices_len):
			current_wallet_usd = 0
			for coin in self.coins:
				current_wallet_usd += self.start_wallet_size_usd * self.weights[coin] * self.coin_prices[coin][i] / self.coin_prices[coin][0]
			self.wallet_usd_over_days.append(current_wallet_usd)

	def get_metrics(self):
		return self.metrics

	def run(self):
		self.generate_wallet_usd_over_days()
		self.generate_metrics()
