class Stock:

    def __init__(self, symbol, target, stop_loss, trail_stop_loss_increment):
        self.symbol = symbol
        self.target = target
        self.stop_loss = stop_loss
        self.trail_stop_loss_increment = trail_stop_loss_increment

    def getSymbol(self):
        return self.symbol

    def getTarget(self):
        return self.target

    def getStopLoss(self):
        return self.stop_loss

    def getTrailStopLossIncrement(self):
        return self.trail_stop_loss_increment