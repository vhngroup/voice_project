# Voice Project: Zero-Shot Text-to-Speech with F5-TTS

## The Build
I implemented and configured a zero-shot voice cloning and text-to-speech pipeline utilizing the **F5-TTS** model. The core of this project focused on successfully provisioning and running the machine learning architecture on Intel hardware.

## The Challenge
Executing modern AI audio models outside the standard NVIDIA/CUDA ecosystem poses significant compatibility and performance hurdles. To solve this, I manually configured a **PyTorch** environment targeted for **Intel XPU** acceleration. This involved handling experimental nightly builds and integrating Intel-specific compute libraries (`intel-pti`, `umf`, `tcmlib`) alongside `torchaudio` to force the hardware to process the model's tensor operations efficiently. 

## The Outcome
The project resulted in `F5_TTS.ipynb`, a functioning environment that bootstraps the Intel XPU stack and prepares the F5-TTS model for voice generation. It demonstrates my ability to take cutting-edge ML research, adapt its execution to non-standard hardware compute architectures, and resolve complex dependency graphs to make experimental tools work in the real world.
