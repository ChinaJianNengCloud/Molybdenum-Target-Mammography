import torch


cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")

if cuda_available:
    num_gpus = torch.cuda.device_count()
    print(f"Number of available GPUs: {num_gpus}")

    for i in range(num_gpus):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
    current_device = torch.cuda.current_device()
    print(f"Current GPU device index: {current_device}")
    print(f"CUDA version: {torch.version.cuda}")
else:
    print("CUDA is not available. Please check your PyTorch installation and GPU drivers.")
