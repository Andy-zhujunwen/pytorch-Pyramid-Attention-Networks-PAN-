import torch
from PIL import Image
import scipy.misc
import matplotlib.pyplot as plt
from torchvision import transforms
from data.utils import decode_seg_map_sequence
from torchvision.utils import save_image
import numpy as np
from data import custom_transforms as tr

from torchvision import transforms


def Normalize(x):
    x = np.array(x).astype(np.float32)
    x /=255.0
    x-=(0.485,0.456,0.406)
    x /=(0.229,0.224,0.225)
    return x

pic_path = './s1.jpeg'
#pic = scipy.misc.imread(pic_path,mode='RGB')
pic = Image.open(pic_path).convert('RGB')

pic = pic.resize((1024,512),Image.BILINEAR)
print('pic shape:{}'.format(pic.size))

pic = np.array(pic)
pic = Normalize(pic)

pic = np.transpose(pic,(2,0,1))
pic = torch.from_numpy(pic.copy()).float()
pic = pic.unsqueeze(0)


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
pic = pic.to(device)


convnet = torch.load('./convnet.pth')
pan = torch.load('./pan.pth')
convnet = convnet.to(device)
pan = pan.to(device)
convnet = convnet.eval()
pan = pan.eval()


out,z= convnet(pic)
feature = out[::-1]
print(feature[0].shape)
out = pan(feature)

out = out.data.cpu().numpy()
out = np.argmax(out,axis=1)
pre = decode_seg_map_sequence(out, plot=True)
save_image(pre,r'./testjpg.png')
