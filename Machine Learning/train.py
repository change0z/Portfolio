import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2
from tqdm import tqdm
import torch.nn as nn
import torch.optim as optim
from model import UNET
'''from utils import (
    load_checkpoints,
    save_checkpoints,
    get_loaders,
    check_accuracy,
    save_predictions_as_imgs,
)'''

#Hyperparameters etc.
LEARNING_RATE = 1e-4
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
BATCH_SIZE = 32
NUM_EPOCHS = 3
NUM_WORKERS = 2
IMAGE_HEIGHT = 160 # 1280 originally
IMAGE_WIDTH = 240 # 1918 originally
PIN_MEMORY = True
LOAD_MODEL = True
TRAIN_IMG_DIR = ""
TRAIN_MASK_DIR = ""
VAL_IMG_DIR = ""
VAL_MASK_DIR = ""


def train_fn(loader, model, optimizer, loss_fn, scaler):
    loop = tqdm(loader)

    for batch_idx, (data, targets) in enumerate(loop):
        data = data.to(device = DEVICE)
        targets = targets.float().unsqueez(1).to(device = DEVICE)

        #forward use float 16 training
        with torch.cuda.amp.autocast():
            predictions = model(data)
            loss = loss_fn(predictions, targets)

        # backwars
        optimizer.zero_grad()
        scaler.scale(loss).backward()
        scaler.update()

        # update tqdm loop
        loop.set_postfix(loss=loss.item())



def main():
    train_transform = A.Compose(
        [
            A.Resize(height=IMAGE_HEIGHT, width=IMAGE_WIDTH),
            A.Rotate(limit = 35, p = 1.0),
            A.HorizontalFlip(p=0.5),
            A.VerticalFlip(p=0.1),
            #ToTensor desn't divide by 255 like PyTorch,
            #it's done inside Normalize Function
            A.Normalize(
                mean=[0.0,0.0,0.0],
                std=[1.0,1.0,1.0],
                max_pixel_value = 255.0,
            ),
            ToTensorV2(),
        ],
    )

if __name__ == "__main__":
    main()

