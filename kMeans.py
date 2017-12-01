import math

                         ## User Functions##

# computes the distance from a centroid
def distance (x, y, tx, ty):
    return math.sqrt(((tx - x) ** 2) + ((ty - y) ** 2))
    
# assigns a cluster to a given example
def getCluster(d0, d1, d2):
    # getting the assignment cluster
    lowest = min(d0, d1 , d2)

    # cluster assignment
    if (lowest == d0):
        return 0
    elif (lowest == d1):
        return 1
    else:
        return 2
        
    

                         ## PROGRAM PROPER ##
    
# variables
k = 3.0
m = 300.0


theta0x = 3.0
theta0y = 3.0
    
theta1x = 6.0
theta1y = 2.0

theta2x = 8.0
theta2y = 5.0
    
jCost = 0

# loop for each iteration
for i in range(1, 11):
    # file open
    fileR = open("kmdata1.txt", "r")

    # stores the summation of J cost values
    jSum = 0

    # stores the x and y values of clustered examples for centroid movement
    newTheta0x = 0
    newTheta0y = 0
    newTheta1x = 0
    newTheta1y = 0
    newTheta2x = 0
    newTheta2y = 0

    # number of examples per cluster
    countTheta0 = 0
    countTheta1 = 0
    countTheta2 = 0

    # create files to be written on
    name1 = "iter%d_ca.txt" % (i)
    fileW1 = open(name1, "w+")
    name2 = "iter%d_cm.txt" % (i)
    fileW2 = open(name2, "w+")
        
    # loop which iterates through each line in the file
    for line in fileR:
        values = line.split(" ")
        x = float(values[1])
        y = float(values[2])
        
        #compute the distance formula from each centroid
        d0 = distance(x, y, theta0x, theta0y)
        d1 = distance(x, y, theta1x, theta1y)
        d2 = distance(x, y, theta2x, theta2y)

        # get cluster assignment
        cluster = getCluster(d0, d1, d2)
        
        # update values needed for J cost and center movement
        if (cluster == 0):
            jSum += d0
            newTheta0x += x
            newTheta0y += y
            countTheta0+= 1
        elif (cluster == 1):
            jSum += d1
            newTheta1x += x
            newTheta1y += y
            countTheta1+= 1
        else:
            jSum += d2
            newTheta2x += x
            newTheta2y += y
            countTheta2+= 1
            
        # cluster assignment writes to file
        fileW1.write("%d\n" % (cluster))

            
    #moves the centroids then writes to file
    if (countTheta0 != 0):    
        theta0x = newTheta0x * (1 / countTheta0)
        theta0y = newTheta0y * (1 / countTheta0)

    if (countTheta1 != 0):
        theta1x = newTheta1x * (1 / countTheta1)
        theta1y = newTheta1y * (1 / countTheta1)

    if (countTheta2 != 0):
        theta2x = newTheta2x * (1 / countTheta2)
        theta2y = newTheta2y * (1 / countTheta2)

    # writing to file
    fileW2.write("%f " % (theta0x))
    fileW2.write("%f\n" % (theta0y))
        
    fileW2.write("%f " % (theta1x))
    fileW2.write("%f\n" % (theta1y))

    fileW2.write("%f " % (theta2x))
    fileW2.write("%f\n" % (theta2y))

    # computing the J cost and the change in J cost, then writes to file
    newJcost = (1 / m) * jSum
    fileW2.write("J= %f \n" % (newJcost))
    
    dJ = newJcost - jCost
    fileW2.write("dJ= %f" % (dJ))

    jCost = newJcost

    # file close    
    fileR.close()
    fileW1.close()
    fileW2.close()
    
                        ## END OF PROGRAM PROPER ##
