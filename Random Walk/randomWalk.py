import matplotlib.pyplot as plt
from random import choice

# Setup plot theme
plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(15,9))
x_values = [0]
y_values = [0]


# Fucntion to get random movement
def move():
    x,y = 0,0
    moving = [-1, 1]
    for m in range(4999):
        x = x + choice(moving)
        y = y + choice(moving)
        y_values.append(y)
        x_values.append(x)


#Remove axies labels and set title
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_title('Random Walk \n', fontsize = 24)

move()
    
ax.scatter(x_values,y_values,c=range(5000), cmap=plt.cm.bone, s=10)

plt.savefig('randomwalk.png')
