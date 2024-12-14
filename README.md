## FINAL YEAR PROJECT - Part 1

# Self-Driving Car Simulation Using CNN

This repository contains the implementation of a self-driving car simulation using a Convolutional Neural Network (CNN). The project leverages NVIDIA's end-to-end deep learning architecture for autonomous navigation within the Udacity Self-Driving Car Simulator.

## Project Overview
The objective of this project is to simulate a self-driving car that can predict steering angles from input images, enabling autonomous navigation in a simulated environment. The project demonstrates the potential of deep learning techniques, particularly CNNs, for autonomous vehicle control.

### Key Features
- End-to-end deep learning model for predicting steering angles.
- Image preprocessing and data augmentation for robust training.
- Integration with the Udacity Self-Driving Car Simulator.
- GPU-accelerated training using TensorFlow and Keras.

## Prerequisites
### Software Requirements
- Python 3.7+
- TensorFlow 2.x
- Keras
- OpenCV
- Udacity Self-Driving Car Simulator

### Libraries
Install the required libraries using:
```bash
pip install -r requirements.txt
```

## Dataset
Data was collected using the Udacity Self-Driving Car Simulator in manual driving mode. The dataset includes:
- Images from three camera angles (left, center, right).
- Corresponding steering angle values.

### Data Preprocessing
- **Cropping**: Removes irrelevant sections (e.g., sky, car hood).
- **Normalization**: Scales pixel values to the range [0, 1].
- **Augmentation**: Introduces variations like flipping, brightness adjustment, and zoom.

## Model Architecture
The CNN model is inspired by NVIDIA's architecture and consists of:
1. Normalization Layer.
2. Five Convolutional Layers for feature extraction.
3. Three Fully Connected Layers for steering angle prediction.

### Activation Function
Exponential Linear Unit (ELU) was used to address vanishing gradient issues and ensure faster convergence.

### Optimization
- **Optimizer**: Adam Optimizer.
- **Loss Function**: Mean Squared Error (MSE) for regression.

## Training
The model was trained for 10 epochs using the prepared dataset. Data augmentation ensured robustness, and the model's performance was evaluated using validation data.

## Testing
The trained model was tested in autonomous mode within the Udacity simulator. It successfully navigated various scenarios, including:
- Straight paths and curves.
- Variations in lighting conditions.
- Minor road obstructions.

## Usage
1. **Clone the Repository**
   ```bash
   git clone https://github.com/31adityakumar/Self-Driving-Car-Simulator
   cd Self-Driving-Car-Simulator
   ```
   **Clone Data**
   ```bash
   https://github.com/rslim087a/track
   ```

3. **Run the Simulator**
   - Install the Udacity Self-Driving Car Simulator from [Udacity's GitHub](https://github.com/udacity/self-driving-car-sim).
   - Launch the simulator and choose the appropriate track.

 
4. **Create an environment & activate**


```bash
conda init powereshell
conda create -n sdcar python=3.7 -y
conda activate sdcar
```


4. **Install the requirements**

```bash
pip install -r requirements.txt
pip install python-engineio==3.13.2
pip install python-socketio==4.6.1
```

5. **Train the Model**
   ```bash
   python train.py
   ```

6. **Test the Model**
   ```bash
   python drive.py
   ```

## Results
The model demonstrated consistent performance in the simulator, maintaining lane discipline and effectively handling diverse scenarios.

### Sample Output
- **Training Loss**: See `training_loss.png` for the loss graph.
- **Autonomous Navigation**: The model's behavior can be visualized in `test_run.mp4`.

## Future Work
- Incorporate additional sensors like LiDAR and radar.
- Train on real-world datasets to improve generalization.
- Optimize the model for edge devices.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.


## Acknowledgments
- NVIDIA for their end-to-end learning architecture.
- Udacity for providing the Self-Driving Car Simulator.
- TensorFlow and OpenCV communities for their invaluable tools.
