import matplotlib.pyplot as plt

#Days
x = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#Data
y1 = [5,1,2,3,4,-5,6]
y2 = [2, 4, -1, 7, 8, 9, 10]
y3 = [1,3,4,5,6,8,2]
y4 = [1,9,6,4,8,2,7]
y5 = [8,2,9,4,6,2,8]

#add color
plt.figure(facecolor="#14171A")
ax = plt.axes()
ax.set_facecolor("#14171A")
#outer lines
ax.spines["bottom"].set_color("#F5F8FA")
ax.spines["left"].set_color("#F5F8FA")
ax.spines["top"].set_color("#F5F8FA")
ax.spines["right"].set_color("#F5F8FA")
#axes
ax.tick_params(axis='x', colors="#F5F8FA")
ax.tick_params(axis='y', colors="#F5F8FA")

# adding graphs to the digram
plt.plot(x, y1, label="XRP",color="lightblue") #,marker = 'o', markerfacecolor = 'r'
plt.plot(x, y2, label="EOS",color="grey")
plt.plot(x, y3, label="ADA",color="darkgreen")
plt.plot(x, y4, label="MIOTA",color="purple")
plt.plot(x, y5, label="NANO",color="blue")

# naming axis
plt.xlabel("Days",fontweight="bold",color="#F5F8FA")
plt.ylabel("Grow in %",fontweight="bold",color="#F5F8FA")

# giving title, save as png
plt.title("no title yet",color="#F5F8FA")

#change color of fond in legend
l = plt.legend(facecolor="#14171A",frameon=False)
for text in l.get_texts():
    text.set_color("#F5F8FA")
#plt.savefig("grow.png",bbox_inches="tight",dpi=300)
plt.show()

