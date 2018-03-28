import numpy as np
import cv2
import sys
# import matplotlib.pyplot as plt

# img=cv2.imread(sys.argv[1])
# img=cv2.resize(img,(256,256))
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imwrite("GRAY.jpg",gray)
# print(gray)

# size_image=gray.shape[0]
size_image=int(input("Enter size of image "))
size_kernel=int(input("Enter size of kernel "))
#kerel initialization
#edge detection filter
# z=np.array([[-1,0,1],
#             [-2,0,2],
#             [-1,0,1]])
# z=np.array([[-1,-1,-1],
#             [-1,8,-1],
#             [-1,-1,-1]])
#blur filter
# z=np.array([[1/9,1/9,1/9],
#             [1/9,1/9,1/9],
#             [1/9,1/9,1/9]])

# size_kernel=z.shape[0]

pad=input("Enter type of padding ")
strides=int(input("Enter stride length "))
if pad=="SAME":
    padding=int((size_kernel-1)/2)
elif pad=="VALID":
    padding=0

# i=gray
i=np.zeros([size_image,size_image])
f=np.zeros([size_kernel,size_kernel])
z=np.zeros([size_kernel,size_kernel])
# padding=0
# strides=1
size_output=int((size_image+(2*padding)-size_kernel)/strides)+1
# print(size_output)
r=np.zeros([size_output,size_output])

k=0

for p in range(size_image):
    for j in range(size_image):
        i[p,j]=k
        k+=1

#adding padding to image
new_matrix_size=size_image+2*padding
new_matrix=np.zeros([new_matrix_size,new_matrix_size])
new_matrix+=1

for m in range(padding):
    for n in range(new_matrix_size):
        new_matrix[m,n]=0
        new_matrix[new_matrix_size-(m+1),n]=0
for n in range(padding):
    for m in range(new_matrix_size):
        new_matrix[m,n]=0
        new_matrix[m,new_matrix_size-(n+1)]=0

for m in range(padding,new_matrix_size-padding):
    for n in range(padding,new_matrix_size-padding):
        new_matrix[m,n]=i[m-padding,n-padding]



# kernel initialization
for o in range(size_kernel):
	for p in range(size_kernel):
		z[o,p]=k
		k+=1

#inverting kernal
for o in range(size_kernel):
	for p in range(size_kernel):
		f[o][p]=z[(size_kernel-1)-o][(size_kernel-1)-p]


strd_t1=0
strd_t2=0

if strides>=2 and pad=="VALID":
    for m in range(new_matrix_size):
        if m>(size_output-1):
            break
        strd_t2=0
        for n in range(new_matrix_size):
            if n>(size_output-1):
                continue
            for u in range(size_kernel):
                for v in range(size_kernel):
                    r[m,n]+=f[u,v]*new_matrix[u+m+strd_t1,v+n+strd_t2]
            if strd_t2<strides:
                strd_t2+=1
            else:
                strd_t2=strides
        if strd_t1<strides:
            strd_t1+=1
        else:
            strd_t1=strides

else:
    for m in range(new_matrix_size):
        if m>(size_output-1):
            break
        for n in range(new_matrix_size):
            if n>(size_output-1):
                continue
            for u in range(size_kernel):
                for v in range(size_kernel):
                    r[m,n]+=f[u,v]*new_matrix[u+m+strd_t1,v+n+strd_t2]
            strd_t2=(strides-1)
        strd_t1=(strides-1)
# print(r.shape)
print(r)

# cv2.imwrite("re1.jpg",r)
# plt.imshow(r)
# plt.show()



# print(new_matrix.shape)
# print(new_matrix)

