
def my_tanh(x):
    e_power = 2.71828 ** (2 * x)  
    return (e_power - 1) / (e_power + 1)  


i1, i2 = 0.05, 0.1  

w1, w2, w3, w4 = -0.2, 0.4, -0.3, 0.1
w5, w6, w7, w8 = 0.3, -0.1, 0.5, -0.4

b1, b2 = 0.5, 0.7

net_h1 = (w1 * i1) + (w2 * i2) + b1
net_h2 = (w3 * i1) + (w4 * i2) + b1


out_h1 = my_tanh(net_h1)
out_h2 = my_tanh(net_h2)

net_o1 = (w5 * out_h1) + (w6 * out_h2) + b2
net_o2 = (w7 * out_h1) + (w8 * out_h2) + b2

out_o1 = my_tanh(net_o1)
out_o2 = my_tanh(net_o2)

print("Output o1:", out_o1)
print("Output o2:", out_o2)
