# pytorch-Pyramid-Attention-Networks-PAN-
train code + inference code were released. [pytorch version]

# PAN network：
![image](https://github.com/Andy-zhujunwen/pytorch-Pyramid-Attention-Networks-PAN-/blob/master/pan.png)
## FPA:
![image](https://github.com/Andy-zhujunwen/pytorch-Pyramid-Attention-Networks-PAN-/blob/master/fpa.png)
## GAU:
![image](https://github.com/Andy-zhujunwen/pytorch-Pyramid-Attention-Networks-PAN-/blob/master/gau.png)


## How to train
first enter the directory:
and follow the instruction:
1.write the dataset path in mypath.py
2. and run 
```
python train.py
```
after trainning,it will save two model: convnet.pth,pan.pth
## How to Inference：
#run:
```
python inference.py
```
# input:
## the Pic in validation dataset:
![image](https://github.com/Andy-zhujunwen/pytorch-Pyramid-Attention-Networks-PAN-/blob/master/pan%2Bcityspaces/s3.png)

## the Pic off the dataset:
![image](https://github.com/Andy-zhujunwen/pytorch-Pyramid-Attention-Networks-PAN-/blob/master/pan%2Bcityspaces/s1.jpeg)

# output:
## the Pic in validation dataset:
![image](https://github.com/Andy-zhujunwen/pytorch-Pyramid-Attention-Networks-PAN-/blob/master/pan%2Bcityspaces/testjpg.png)

## the Pic off the dataset:
![image](https://github.com/Andy-zhujunwen/pytorch-Pyramid-Attention-Networks-PAN-/blob/master/pan%2Bcityspaces/testjpg1.png)
