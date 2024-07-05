# SickFace
[![MasterHead](https://github.com/Inferencer/SickFace/blob/main/examples/repo%20imgs/SickFaceBanner.png?raw=false)](https://huggingface.co/spaces/Inferencer/SickFace)

New version releasing at https://github.com/Inferencer/myface
## Overview

This repository focuses on portrait animation, specifically lip-synchronization via 3DMM control, but also allows for video-driven animation.

# Note:

I will update this repo with correct layout and intruction but this has been tested on python 3.10 with cuda 11.8 in annaconda windows
## Setup
Please complete the following steps.

Clone the repository:

```
git clone https://github.com/Inferencer/SickFace.git
cd SickFace
```

We recommend to create a new conda environment:

```
conda create -n sickface python=3.10
conda activate sickface
```

### Dependencies

This code requires at least Python 3.10 and PyTorch.

 1. Install [PyTorch](https://pytorch.org/get-started/locally/) (>= 1.12.0)
    ```
    conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
    ```
 2. Additional dependencies can be installed via:

    ```
    pip install -r requirements.txt
    ```

  3. Run the gradio ui

    python app.py

Alternatively you can console commands using the following

 ```
python demo.py --checkpoint checkpoints/vox256.pt --config ./configs/vox256.yaml  --source_images ./examples/myimagefile.jpg --driving_video ./examples/mydriveingfile.mp4 --relative --adapt_scale --find_best_frame --audio
  ```
If you wish to use more than one source image you are welcome to use up to two in total by adding another image path such as
 ```
python demo.py --checkpoint checkpoints/vox256_2Source.pt --config ./configs/vox256.yaml  --source_images ./examples/myimagefile.jpg ./examples/myimagefile2.jpg --driving_video ./examples/drive.mp4 --relative --adapt_scale --find_best_frame --audio

  ```
You can use different file formats such as .png if you so wish but before using multiple source image I reccomend reading this [issue](https://github.com/Inferencer/SickFace/issues/1) you will also notice the checkpoint has changed to vox256_2Source.pt

### Pretrained Checkpoints

Pretrained models can be found at [google-drive](https://drive.google.com/drive/folders/1R9BuWM-kqPddriZtIVf5z3Yq14D4DDSP?usp=drive_link).

The models should be downloaded and placed in ./checkpoints so `checkpoints/kp_detector.pt` & `checkpoints/vox256.pt`. Note that all pretrained checkpoints are trained using the same keypoint detector weights.

## Features

### Version 1 (V1)
- **Code Base**: Uses code from [FSRT](https://github.com/andrerochow/fsrt).
- **Enhancements**:
  - Added upscaling implementation.
  - UI
  - Possible further training with the vox512 dataset or another dataset (not sure why vox256 has been the default in recent years.)
- **3DMM Selection**: The 3DMM to be used is yet to be decided from the following list:
  - CodeTalker
  - EmoTalk
  - Emote
  - FaceDiffuser
  - FaceFormer

### Version 2 (V2)
- **Upgrades**: Will incorporate advancements from InvertAvatar, Portrait-4dv2, or another state-of-the-art (SOTA) model released this year.
- **3DMM Upgrade**: Potential integration of the upcoming [Media2Face](https://www.youtube.com/watch?v=k-CO8bEOTyA).

### Version 3 (V3)
- **Future Goals**:
  - Expected release by late 2025.
  - Aim for Gaussian-based methods.
  - Focus on one-shot methods with minimal training requirements.
  - Training constraints: Should not exceed 1 hour on an A100 GPU and should use a maximum of 30 seconds of video identity data.

## Conclusion

SickFace aims to push the boundaries of portrait animation by leveraging state-of-the-art techniques and efficient training methods. Stay tuned for updates as we progress through each version!
