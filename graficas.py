import matplotlib.pyplot as plt

fig, ax = plt.subplots()
dias = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
casos = {
    "1": [2.25, 2.48, 2.70, 3.48, 3.64, 3.98, 4.02, 4.56, 4.90, 5.19, 5.67],
    "2": [1.92, 1.91, 1.88, 1.81, 2.17, 2.23, 2.19, 2.35, 2.39, 2.57, 2.87],
    "3": [1.64, 1.81, 1.76, 1.79, 2.04, 1.97, 2.06, 2.33, 2.11, 2.27, 2.25],
    "4": [1.56, 1.69, 1.72, 1.90, 1.87, 2.08, 2.02, 2.15, 2.11, 2.29, 2.27],
    "5": [1.87, 1.66, 1.86, 1.89, 1.90, 1.95, 2.15, 2.24, 2.15, 2.47, 2.43],
}
ax.plot(dias, casos["1"], color="tab:purple")
ax.plot(dias, casos["2"], color="tab:green")
ax.plot(dias, casos["3"], color="tab:red")
ax.plot(dias, casos["4"], color="tab:blue")
ax.plot(dias, casos["5"], color="tab:green")
plt.show()
