import matplotlib.pyplot as plt


def Visualition(y1: list, y2: list, y3: list, y4: list, y5: list):
    # Days
    x = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]

    # Data
    axe_1 = y1  # [5, 1, 2, 3, 4, -5, 6]
    axe_2 = y2  # [2, 4, -1, 7, 8, 9, 10]
    axe_3 = y3  # [1, 3, 4, 5, 6, 8, 2]
    axe_4 = y4  # [1, 9, 6, 4, 8, 2, 7]
    axe_5 = y5  # [8, 2, 9, 4, 6, 2, 8]

    # add color
    plt.figure(facecolor="#14171A")
    ax = plt.axes()
    ax.set_facecolor("#14171A")
    # outer lines
    ax.spines["bottom"].set_color("#F5F8FA")
    ax.spines["left"].set_color("#F5F8FA")
    ax.spines["top"].set_color("#F5F8FA")
    ax.spines["right"].set_color("#F5F8FA")
    # axes
    ax.tick_params(axis='x', colors="#F5F8FA")
    ax.tick_params(axis='y', colors="#F5F8FA")

    # adding graphs to the digram
    # ,marker = 'o', markerfacecolor = 'r'
    plt.plot(x, axe_1, label="XRP", color="lightblue")
    plt.plot(x, axe_2, label="EOS", color="grey")
    plt.plot(x, axe_3, label="ADA", color="darkgreen")
    plt.plot(x, axe_4, label="MIOTA", color="purple")
    plt.plot(x, axe_5, label="NANO", color="blue")

    # naming axis
    plt.xlabel("Days", fontweight="bold", color="#F5F8FA")
    plt.ylabel("Grow in %", fontweight="bold", color="#F5F8FA")

    # giving title, save as png
    plt.title("The grow in the last Week", color="#F5F8FA")

    # change color of fond in legend
    l = plt.legend(facecolor="#14171A", frameon=False)
    for text in l.get_texts():
        text.set_color("#F5F8FA")
    plt.savefig("grow.png", bbox_inches="tight", dpi=300)
