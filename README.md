# Ultrasound Image Classifier Desktop Application

A Windows desktop application designed for medical professionals to process ultrasound images locally using pre-trained ONNX neural network models.  
The application supports both standard images (JPG/PNG) and DICOM files, with CPU and optional GPU acceleration.

## Features
- **Batch Image Processing:** Select a folder and process 1–200 images at once.
- **ONNX Model Inference:** Run multiple models (e.g., gestational age, preterm risk).
- **DICOM Support:** Load and process medical imaging formats natively.
- **GPU Acceleration (Optional):** Boost performance via DirectML/CUDA if available.
- **Professional UI:** Built with a clean, medical-friendly design.
- **Admin-Free Installation:** Portable or installer builds that don't require admin rights.
- **Testing Suite:** Unit tests for core functionality and manual UI test workflows.

## Tech Stack
- **Python 3.8+**
- **PyQt5** — Desktop UI Framework
- **ONNX Runtime** — Model Inference Engine
- **OpenCV** — Image Preprocessing
- **pydicom** — DICOM Image Handling
- **SimpleITK** — Advanced Medical Image Utilities
- **PyTest** — Unit Testing Framework

## Installation

### Requirements
- Windows 10/11
- No admin privileges needed.

### Steps
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

Or use the pre-built **Portable Executable** / **Installer** (coming soon).

## Project Structure
```
ultrasound_app/
├── app/
│   ├── main_window.py        # Main UI and application logic
│   ├── inference_engine.py   # ONNX model loading and inference
│   ├── dicom_handler.py      # DICOM file support
│   └── utils.py              # Utility functions
├── models/                   # Pre-trained ONNX models (placeholder)
├── tests/                    # Unit tests
├── assets/                   # UI icons, images
├── main.py                   # App entry point
├── requirements.txt          # Python dependencies
├── README.md                 # Project overview
├── LICENSE                   # MIT License
└── .gitignore                # Git ignore file
```

## Testing
```bash
pytest tests/
```
Covers:
- Image preprocessing
- Model inference
- DICOM loading

Manual UI test scripts are provided separately.

## Deployment
- **Portable ZIP**: Just extract and run.
- **MSIX Installer**: (Planned) One-click install without admin rights.

## License
This project is licensed under the [MIT License](LICENSE).

## Author
**Abhishek Yadav**

> _Built to make AI ultrasound tools more accessible for medical professionals._
