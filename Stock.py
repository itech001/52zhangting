#coding=utf-8
class Stock:
     def __init__(self, symbol,dateV,open,close,close_adj,high,low,volume,prev_close_to_close,open_to_close,low_to_high):
         self.symbol = symbol
         self.dateV =dateV
         self.open = open
         self.close = close
         self.close_adj = close_adj
         self.high = high
         self.low = low
         self.volume = volume
         self.prev_close_to_close = prev_close_to_close
         self.open_to_close = open_to_close
         self.low_to_high = low_to_high
