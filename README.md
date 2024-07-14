# SmoothingPipe

## Introduction

Welcome to SmoothingPipe! This project is designed to implement a small 2D/3D smoothing libary.  

## Requirements

List the software and hardware requirements for your project. For example:

```
- Python 3.8+
- pip package manager
- Operating System: Windows/Linux/MacOS
- Dependencies: See `requirements.txt`
```

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/username/SmoothingPipe
   ```

2. Navigate to the project directory:
   ```sh
   cd SmothingPipe
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Start the application:
   ```sh
   python main.py
   ```

## Usage

Example of how to use a feature in your project:

```python
from smoothingpipe import SmoothingPipe as sp

# Use the SmoothingPipe
result = sp.convolution2D(y_noisy_data, kernel_size=15)
print(result)
```
