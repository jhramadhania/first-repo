stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
  return stock_prices[x-1]

def max_price(a, b):
  mx = 0
  for x in range(a, b + 1):
    mx = max(mx, price_at(x))
  return mx

def min_price(a, b):
  mn = price_at(a)
  for x in range(a, b + 1):
    mn = min(mn, price_at(x))
  return mn

print(max_price(3, 9))
print(min_price(2, 8))
print(price_at(5))

    