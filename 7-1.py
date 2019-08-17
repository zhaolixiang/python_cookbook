prices={
'ACME':45.23,
'AAPL':612.78,
'IBM':205.55,
'HPQ':37.20,
'FB':10.75
}


#找出价格最低放入股票
min_price=min(zip(prices.values(),prices.keys()))
print(min_price)


#找出价格最高放入股票
max_price=max(zip(prices.values(),prices.keys()))
print(max_price)

#同样，要对数据排序只要使用zip()再配合sorted()
prices_sorted=sorted(zip(prices.values(),prices.keys()))
print(prices_sorted)