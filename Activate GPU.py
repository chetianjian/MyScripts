import tensorflow as tf


class ActivateGPU(object):
    def __init__(self):
        self.is_available = bool(tf.config.list_physical_devices('GPU'))
        self.physical_device = tf.config.experimental.list_physical_devices("GPU")

    def set_gpu(self):
        if self.is_available:
            print(f"GPU availability: {self.is_available}")
        try:
            tf.config.experimental.set_memory_growth(self.physical_device[0], True)
            print("Num GPUs: ", len(tf.config.experimental.list_physical_devices("GPU")))
            print("Set Memory Growth Successfully.")
        except:
            print("Invalid device or cannot modify virtual devices once initialized.")
        return "Done."


print(ActivateGPU().set_gpu())