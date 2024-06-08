# SickFace

## Overview

This repository focuses on portrait animation, specifically lip-synchronization via 3DMM control, but also allows for video-driven animation.

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
