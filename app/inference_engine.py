import onnxruntime as ort
import numpy as np
import cv2

class InferenceEngine:
    def __init__(self, model_path, use_gpu=False):
        providers = ['CUDAExecutionProvider'] if use_gpu else ['CPUExecutionProvider']
        self.session = ort.InferenceSession(model_path, providers=providers)
        self.input_name = self.session.get_inputs()[0].name

    def preprocess(self, image_path):
        image = cv2.imread(image_path)
        image = cv2.resize(image, (224, 224))
        image = image / 255.0
        image = np.transpose(image, (2, 0, 1)).astype(np.float32)
        return np.expand_dims(image, axis=0)

    def predict(self, image_path):
        input_tensor = self.preprocess(image_path)
        output = self.session.run(None, {self.input_name: input_tensor})
        return output
