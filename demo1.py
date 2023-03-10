import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda_version)
print(torch.cuda.device_count())
print(torch.cuda.get_device_name())
# 1.10.1
# True
# 11.3
# 1
# NVIDIA GeForce GTX 960M