import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt


def convolution_layer(image,kernel,pad="SAME",strides=1):
    size_image=image.shape[0]
    z=kernel
    size_kernel=z.shape[0]
    if pad=="SAME":
        padding=int((size_kernel-1)/2)
    elif pad=="VALID":
        padding=0

    i=image
    f=np.zeros([size_kernel,size_kernel])
    size_output=int((size_image+(2*padding)-size_kernel)/strides)+1
    r=np.zeros([size_output,size_output])

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
        return r

    for m in range(new_matrix_size):
        if m>(size_output-1):
            break
        # strd_t2=0
        for n in range(new_matrix_size):
            if n>(size_output-1):
                continue
            for u in range(size_kernel):
                for v in range(size_kernel):
                    r[m,n]+=f[u,v]*new_matrix[u+m+strd_t1,v+n+strd_t2]
            strd_t2=(strides-1)
        strd_t1=(strides-1)
    return r





# img=cv2.imread(sys.argv[1])
# img=cv2.resize(img,(256,256))
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# kernel=np.array([[1,4,6,4,1],
#                  [4,16,24,16,4],
#                  [6,24,36,24,6],
#                  [4,16,24,16,4],
#                  [1,4,6,4,1]])
# kernel=kernel/256

# x=convolution_layer(gray,kernel)
# cv2.imwrite("result.jpg",x)
