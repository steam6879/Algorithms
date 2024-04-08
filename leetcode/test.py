class Solution():
    def maxProfit(self, prices:list)->int:
        
        price_min = 10000 # 최저 주식값
        profit = 0 # 수익
        
        for price_current in prices:
            # 현재 가격 - 최저값의 값과 수익의 값 중, 최대값을 수익값으로 보고 스왑함
            price_min = min(price_current, price_min)
            
            # 현재 가격 - 최저값의 값과 수익의 값 중, 최대값을 수익값으로 보고 스왑함
            profit = max(profit, price_current-price_min) 
        return profit