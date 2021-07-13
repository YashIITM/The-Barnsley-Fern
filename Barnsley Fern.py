#Importing relevant python libraries :
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#Defining functions to plot the Barnsley Fern:
def f1(x,y):
    return (0.0,0.16*y)
def f2(x,y):
    return (0.85*x+0.04*y,0.85*y-0.04*x+1.6)
def f3(x,y):
    return (0.2*x-0.26*y,0.22*y+0.23*x+1.6)
def f4(x,y):
    return (-0.15*x+0.28*y,0.24*y+0.26*x+0.44)

#List of defined functions
functions = [f1,f2,f3,f4]

#We choose 100000 iterations to create our png file:
points = 100000
x,y =0,0

##The following code is used to generate the png file we desire using matplotlib.cm library:

#Initializations:
width, height = 300,300
fern_image = np.zeros((width,height))

#Loop that generates the 2D array fern_image with required values:
for i in range(points):
    #Choice function allows us to choose from 'functions' the entries with respective probabilities p:
    function = np.random.choice(functions,p=[0.01,0.85,0.07,0.07])
    x,y = function(x,y)
    ix,iy = int(width/2 +x*width/10),int(y*height/12)
    fern_image[iy,ix]=1
    
#We plot the image using matplotlib library:
plt.imshow(fern_image[::-1,:],cmap=cm.Greens)

#Following command shows us the plot:
plt.show()


#The following commented code was used earlier to generate the png file, however the resolution was unsatisfactory so we did what we did above:
# x_list=[]
# y_list=[]

# for i in range(points):
#     function = np.random.choice(functions,p=[0.01,0.85,0.07,0.07])
#     x,y = function(x,y)
#     x_list.append(x)
#     y_list.append(y)
    
# plt.scatter(x_list,y_list,s=0.15,color='green')

