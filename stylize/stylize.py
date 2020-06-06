import os
import time
import re

import numpy as np

import torch
from torchvision import transforms

from PIL import Image

from stylize import utils
from stylize.transformer_net import TransformerNet

def style(img_path, model_path):
    device = torch.device("cuda")

    img = utils.load_image(img_path)
    content_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255))
    ])
    img = content_transform(img)
    img = img.unsqueeze(0).to(device)
    
    style_model = TransformerNet()
    state_dict = torch.load(model_path)
    for k in list(state_dict.keys()):
        if re.search(r'in\d+\.running_(mean|var)$', k):
            del state_dict[k]
    style_model.load_state_dict(state_dict)
    style_model.to(device)
    
    with torch.no_grad():
        output = style_model(img)
    
    img = output[0].cpu().clone().clamp(0, 255).numpy()
    img = img.transpose(1, 2, 0).astype("uint8")
    return Image.fromarray(img)