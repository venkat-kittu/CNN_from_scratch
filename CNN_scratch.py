import conv2 as c
import relu
import polling
import cv2
import sys
import numpy as np

x=cv2.imread(sys.argv[1])
x=cv2.resize(x,(256,256))
z=cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)
k=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
r=c.convolution_layer(z,k)
cv2.imwrite("conv2.jpg",r)
s=relu.relu(r)
p=polling.max_pool(s)
print(p.shape)
cv2.imwrite("polling.jpg",p)
p2=polling.avg_pool(s)
cv2.imwrite("avg_pool.jpg",p2)
