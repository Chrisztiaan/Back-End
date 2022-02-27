# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1
leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')

# Part 2
leek_order = 'leek 4'
leek_order_amount = int(leek_order[leek_order.find(" "):])
sum_total = leek_order_amount * leek_price
print(sum_total)

# Part 3
brocolli_price = 2.34
brocolli_order = 'broccoli 1.6'
brocolli_order_amount = float(brocolli_order[brocolli_order.find(" "):])
total_price = brocolli_order_amount * brocolli_price
print(str(brocolli_order_amount) + 'kg broccoli costs ' + str(round(total_price, 2)) + 'e')
