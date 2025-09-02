prices = [25,15,32,8,45,13,67,23]

max_price = max(prices)
min_price = min(prices)
total_price = sum(prices)
items_over_20 = sum(1 for p in prices if p > 20)

print("สินค้าที่แพงที่สุด:",max_price)
print("สินค้าที่ถูกที่สุด:",min_price)
print("ราคารวมทั้งหมด:" ,total_price)
print("จำนวนสินค้าที่ราคา > 20:",items_over_20)