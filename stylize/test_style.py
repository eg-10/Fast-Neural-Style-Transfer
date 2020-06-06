from PIL import Image
import torch
import re
from torchvision import transforms
import numpy as np
import os
import time
import stylize
since = time.time()

# def style(img_path, model_path):
#     device = torch.device("cuda")

#     img = utils.load_image(img_path)
#     content_transform = transforms.Compose([
#         transforms.ToTensor(),
#         transforms.Lambda(lambda x: x.mul(255))
#     ])
#     img = content_transform(img)
#     img = img.unsqueeze(0).to(device)
    
#     style_model = TransformerNet()
#     state_dict = torch.load(model_path)
#     for k in list(state_dict.keys()):
#         if re.search(r'in\d+\.running_(mean|var)$', k):
#             del state_dict[k]
#     style_model.load_state_dict(state_dict)
#     style_model.to(device)
    
#     with torch.no_grad():
#         output = style_model(img)
    
#     img = output[0].cpu().clone().clamp(0, 255).numpy()
#     img = img.transpose(1, 2, 0).astype("uint8")
#     return Image.fromarray(img)

# mosaic_epoch_1_Fri_Jun__5_09_47_23_2020_100000.0_500000000.0.model
# starry_epoch_1_Fri_Jun__5_08_13_12_2020_100000.0_500000000.0.model
# watercolor_epoch_1_Fri_Jun__5_09_45_28_2020_100000.0_500000000.0.model
# afermov_epoch_1_Fri_Jun__5_11_18_36_2020_100000.0_500000000.0.model
# landscape_epoch_1_Fri_Jun__5_08_15_17_2020_100000.0_500000000.0.model
# afermov_epoch_1_Sat_Jun__6_14_21_02_2020_100000.0_3000000000.0.model

base = 'D:\\Desktop\\try outs\\fast_neural_style_transfer'
model = 'starry_epoch_1_Fri_Jun__5_08_13_12_2020_100000.0_500000000.0.model'
img = 'TSLA.jfif'

img_path = os.path.join(base,'imgs', img)
model_path = os.path.join(base, 'models', model)

st = stylize.style(img_path, model_path)

st.save(os.path.join('D:\\Desktop\\try outs\\fast_neural_style_transfer\\ops','uuu.jpg'))
done = time.time()

print('done in total {}'.format(done - since))