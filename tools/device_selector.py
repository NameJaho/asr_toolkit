import torch


def get_infer_device():
    if torch.cuda.is_available():
        infer_device = "cuda"
    elif torch.backends.mps.is_available():
        infer_device = "mps"
    else:
        infer_device = "cpu"
    return infer_device


def is_half(infer_device):
    if infer_device == "cuda":
        gpu_name = torch.cuda.get_device_name(0)
        if (
                ("16" in gpu_name and "V100" not in gpu_name.upper())
                or "P40" in gpu_name.upper()
                or "P10" in gpu_name.upper()
                or "1060" in gpu_name
                or "1070" in gpu_name
                or "1080" in gpu_name
        ):
            return False
    elif infer_device == "cpu":
        return False
    return True
