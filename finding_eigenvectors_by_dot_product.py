
# # # Finding Eigenvectors by Dot Product

# Let's take the matrix: A=[[1,2],[3,4]]
 
# this matrix has two eigenvalues and two corresponding eigenvectors. Let's find them with the `eig()` function:

    
import numpy as np
A = np.matrix([[1,2],[3,4]])
[eigenvalues, eigenvectors] = np.linalg.eig(A)
print(eigenvalues,"\n",eigenvectors)


# so:
# λ_1 = -0.372 >>>>> u_1 = [[-0.825],[0.566]]
# λ_2 = 5.372  >>>>> u_2 = [[-0.416],[-0.909]]


# 0. Let's calculate the angle that each eigenvector makes with the x-axis.


eigenvector1 = eigenvectors[:,0]
print("First Eigenvector:\n",eigenvector1)
print("-----"*2)
eigenvector2 = eigenvectors[:,1]
print("Second Eigenvector:\n",eigenvector2)
print("-----"*2)

tan1 = np.arctan2(eigenvector1[1],eigenvector1[0]) # Angle with horizontal, in radians
tan2 = np.arctan2(eigenvector2[1],eigenvector2[0]) # Angle with horizontal, in radians
angle1 = (tan1*180)/np.pi # Convert angle to degrees
angle2 = (tan2*180)/np.pi # Convert angle to degrees
print("First Angle: ",(angle1),"\nSecond Angle:",(angle2))
print("-----"*5)



# Let's try to find the eigenvectors using the "dot product" method:
# 1. Create a two-dimensional random vector `k` whose components are in the range ${x,y}\in [-1,1]$ (components do not have to be integers)
# 2. Calculate the angle this vector makes with the horizontal.
# 3. Let's multiply this vector by matrix A and calculate the angle it makes with the horizontal. Let's look at the difference between this angle and the angle we calculated earlier. Let's repeat the process until this difference is less than 0.0001. Let's print out how many steps we have reached this little difference. So we multiplied the vector `k` by the matrix `A` and we got the vector `k'`. If the angle between these two vectors is greater than 0.0001, we get the vector `k''` by multiplying the `k'` vector with the matrix `A`. We do the angle control between the vectors `k''` and `k'`. That is, the angle control is always between the now computed and previously computed vectors. 
# 4. Let's set the length of the vector we obtained last to be 1, its direction remains the same. Let's print the angle and the vector.
# 5. Let's repeat steps 1-4, 20 times. Is the angle we found one of 145,544 or -114,581?



for i in np.arange(0,20):
    k = np.random.rand(1,2)*2-1
    k = np.transpose(k)
    print("Randomly Generated Vector k:\n",k)
    print("-----"*2)
    step = np.array(k)
    while True:
        ang_rad1 = np.arctan2(k[1,0],k[0,0]) # Angle with horizontal, in radians
        ang_1 = (ang_rad1*180)/np.pi # Convert angle to degrees
        k1 = np.dot(A,k)
        ang_rad2 = np.arctan2(k1[1,0],k1[0,0]) # Angle with horizontal, in radians 
        ang_2 = (ang_rad2*180)/np.pi # Convert angle to degrees
        difference = abs(ang_2-ang_1)
        k = k1
        step = np.append(step,k)
        if(difference < 0.0001):
            print("Difference:",difference)
            print("Last Vector:",k1)
            print("Angle:",ang_2)
            num_of_steps = len(step)/2
            print("Step ",num_of_steps)
            break
    # Let's set the length of the vector we obtained last to be 1
    length = np.linalg.norm(k1)
    norm = [k1[0,0]/length,k1[1,0]/length]
    print("Norm Vector:",norm)
    print("-----------"*6)


    
    
