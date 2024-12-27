
class StrategyBot:
    def __init__(self, strategy_name):
        self.strategy_name = strategy_name
        self.active = False

    def start(self):
        print(f"Starting the bot with strategy: {self.strategy_name}.")
        self.active = True

    def stop(self):
        print(f"Stopping the bot with strategy: {self.strategy_name}.")
        self.active = False

    def execute_trade(self, trade_data):
        if self.active:
            print(f"Executing trade: {trade_data}")
            return {"status": "success", "trade_id": "12345"}
        else:
            print("Cannot execute trade: Bot is not active.")
            return {"status": "failure"}
    