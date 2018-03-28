import numpy as np

def max_pool(x,ksize=2,pad="VALID",strides=2):
    if pad=="SAME":
        padding=int((ksize-1)/2)
        # tt=x.shape[0]*(strides-1)+ksize-strides
        # padding=int(tt/2)
    elif pad=="VALID":
        padding=0
    strd_t1=0
    strd_t2=0
    size_output=int((x.shape[0]+(2*padding)-ksize)/strides)+1
    r=np.zeros([size_output,size_output])
    # print(size_output)

    #add padding
    new_matrix_size=x.shape[0]+2*padding
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
            new_matrix[m,n]=x[m-padding,n-padding]
    # print(new_matrix)

    for m in range(x.shape[0]):
        if m>(size_output-1):
            break
        strd_t2=0
        for n in range(x.shape[1]):
            if n>(size_output-1):
                continue
            for u in range(ksize):
                for v in range(ksize):
                    if r[m,n]<new_matrix[u+m+strd_t1,v+n+strd_t2]:
                        r[m,n]=new_matrix[u+m+strd_t1,v+n+strd_t2]
            if strd_t2<strides:
                strd_t2+=1
            else:
                strd_t2=strides
        if strd_t1<strides:
            strd_t1+=1
        else:
            strd_t1=strides
    return r

def avg_pool(x,ksize=2,pad="VALID",strides=2):
    if pad=="SAME":
        padding=int((ksize-1)/2)
    elif pad=="VALID":
        padding=0
    strd_t1=0
    strd_t2=0
    size_output=int((x.shape[0]+(2*padding)-ksize)/strides)+1
    r=np.zeros([size_output,size_output])

    #add padding
    new_matrix_size=x.shape[0]+2*padding
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
            new_matrix[m,n]=x[m-padding,n-padding]

    for m in range(x.shape[0]):
        if m>(size_output-1):
            break
        strd_t2=0
        for n in range(x.shape[1]):
            if n>(size_output-1):
                continue
            for u in range(ksize):
                for v in range(ksize):
                    r[m,n]+=new_matrix[u+m+strd_t1,v+n+strd_t2]
            r[m,n]=r[m,n]/(ksize*2)
            if strd_t2<strides:
                strd_t2+=1
            else:
                strd_t2=strides
        if strd_t1<strides:
            strd_t1+=1
        else:
            strd_t1=strides
    return r


# a=np.array([[1,2,3,4,5,6],
#             [7,8,9,10,11,12],
#             [13,14,15,16,17,18],
#             [19,20,21,22,23,24],
#             [25,26,27,28,29,30],
#             [31,32,33,34,35,36]])
# print(max_pool(a))
# print(avg_pool(a))