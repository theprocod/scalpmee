class GoatRulesEngine:
    def __init__(self):
        self.daily_drawdown_limit = 3.0
        self.max_drawdown_limit = 6.0
        self.floating_loss_limit = 2.0
        self.max_trades_per_day = 10
        self.max_trades_per_hour = 3
        self.min_trade_duration = 120 # seconds

    def can_open_trade(self, current_floating_loss: float, proposed_risk: float) -> bool:
        if (current_floating_loss + proposed_risk) > self.floating_loss_limit:
            return False
        return True

    def remaining_daily_loss(self, current_daily_loss: float) -> float:
        return max(0.0, self.daily_drawdown_limit - current_daily_loss)

    def remaining_floating_loss(self, current_floating_loss: float) -> float:
        return max(0.0, self.floating_loss_limit - current_floating_loss)

    def risk_after_trade(self, current_risk: float, proposed_risk: float) -> float:
        return current_risk + proposed_risk
