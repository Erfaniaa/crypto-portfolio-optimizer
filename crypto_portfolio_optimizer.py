from wallet_simulator import WalletSimulator


class CrytoPortfolioOptimizer:
	def __init__(self, candidate_coins, weights_step_precision_percent, simulation_start_date, simulation_end_date, start_wallet_size_usd):
		self.candidate_coins = candidate_coins
		self.weights_step_percision_percent = weights_step_precision_percent
		self.simulation_start_date = simulation_start_date
		self.simulation_end_date = simulation_end_date
		self.start_wallet_size_usd = start_wallet_size_usd
		self.total_portfolios_simulated = 0
		
	def check_if_input_is_valid(self):
		if self.simulation_start_date > self.simulation_end_date:
			print("simulation_start_date is greater than simulation_end_date")
			exit()
		if self.weights_step_percision_percent < 1:
			print("weights_step_percision_percent is less than 1")
			exit()
		if self.start_wallet_size_usd < 0:
			print("start_wallet_size_usd is less than 0")
			exit()
		if len(self.candidate_coins) == 0:
			print("candidate_coins is empty")
			exit()
		if int(100 / self.weights_step_percision_percent) != 100 / self.weights_step_percision_percent:
			print("weights_step_percision_percent is not a divisor of 100")
			exit()


	def find_best_portfolio(self):
		self.check_if_input_is_valid()
		self.weights = {}
		self.candidate_coins = list(sorted(self.candidate_coins))
		for coin in self.candidate_coins:
			self.weights[coin] = 0
		self.best_portfolio_weights = self.weights.copy()
		self.last_best_portfolio_weights = self.best_portfolio_weights
		self.best_portfolio_return_percent = -(10 ** 10)
		self.best_portfolio_maximum_drawdown_percent = -(10 ** 10)
		self.wallet_simulator = WalletSimulator(coins=self.candidate_coins, start_wallet_size_usd=self.start_wallet_size_usd, weights=self.weights, simulation_start_date=self.simulation_start_date, simulation_end_date=self.simulation_end_date)
		self.wallet_simulator.load_all_coins_prices()
		print()
		print("Please wait (if it's slow, you can increase weights_step_percision_percent)")
		self.bruteforce(0, 0)
		self.print_best_portfolio_details()
		print("Finished")

	def bruteforce(self, weights_sum, weights_index):
		if weights_sum > 1.00:
			return
		if weights_index == len(self.candidate_coins):
			if weights_sum == 1.00:
				self.wallet_simulator.set_weights(self.weights)
				self.wallet_simulator.run()
				current_portfolio_metrics = self.wallet_simulator.get_metrics()
				current_portfolio_return_percent = current_portfolio_metrics["return_percent"]
				current_portfolio_maximum_drawdown_percent = current_portfolio_metrics["maximum_drawdown_percent"]
				if current_portfolio_maximum_drawdown_percent > self.best_portfolio_maximum_drawdown_percent:
					self.last_best_portfolio_weights = self.best_portfolio_weights
					self.best_portfolio_return_percent = current_portfolio_return_percent
					self.best_portfolio_maximum_drawdown_percent = current_portfolio_maximum_drawdown_percent
					self.best_portfolio_weights = self.weights.copy()
				self.total_portfolios_simulated += 1
				if self.total_portfolios_simulated % 10000 == 0 and self.best_portfolio_weights != self.last_best_portfolio_weights:
					self.print_best_portfolio_details()
			else:
				return
		elif weights_index < len(self.candidate_coins):
			for k in range(101):
				self.weights[list(sorted(self.weights.keys()))[weights_index]] = k * self.weights_step_percision_percent / 100
				self.bruteforce(weights_sum + self.weights[list(sorted(self.weights.keys()))[weights_index]], weights_index + 1)

	def print_best_portfolio_details(self):
		print()
		print("best_portfolio_weights detected until now:")
		for coin in self.candidate_coins:
			print(f"  {coin}: {100 * self.best_portfolio_weights[coin]}%")
		print(f"portfolio_return_percent: {self.best_portfolio_return_percent}%")
		print(f"portfolio_maximum_drawdown_percent: {self.best_portfolio_maximum_drawdown_percent}%")
		print()
