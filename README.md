# taskworker-imagedescription

## Installation

Download and install CUDA 12.1 toolkit from https://developer.nvidia.com/cuda-12-1-0-download-archive (Select user defined and only "CUDA" if you have already installed newer versions of the graphics card driver)

```sh
python3.10 -m venv python-venv
python-venv\Scripts\activate
python -m pip install --upgrade pip
pip install numpy==1.26.4
pip install torch==2.1.2 --index-url https://download.pytorch.org/whl/cu121
pip install torchvision==0.16.2 transformers==4.44.2 einops==0.8.0 accelerate==0.34.2
git clone https://github.com/LLaVA-VL/LLaVA-NeXT.git llava
cd llava
pip install -e .
cd ..
```

On first run the AI models need to be downloaded (about 20GB).
DAS HIER GEHT NICHT! Abhängigkeitsprobleme!!!


## Ollama installation

Download and install Ollama from https://ollama.com/download.

```sh
python3.12 -m venv python-venv
python-venv\Scripts\activate
pip install ollama
ollama pull llama3.1
ollama pull llava:34b
```

Model library: https://github.com/ollama/ollama?tab=readme-ov-file#model-library

Hier geht es weiter: https://anakin.ai/de/blog/ollama-vision-llava-models-de/