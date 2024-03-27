import matplotlib.pyplot as plt

fig, ax = plt.subplots()
dias = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
casos = {
    "Madrid": [2.87, 2.97, 3.04, 3.42, 3.69, 3.88, 4.11, 4.39, 4.39, 4.43, 4.80],
    "Barcelona": [2.14, 2.40, 2.35, 2.30, 2.44, 2.29, 2.38, 4, 5,3, 2],
}
ax.plot(dias, casos["Madrid"], color="tab:purple")
ax.plot(dias, casos["Barcelona"], color="tab:green")
plt.show()
