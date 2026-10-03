# PROJECT 5: ECG Arrhythmia Detection
import numpy as np
import scipy.signal as signal

# Bandpass filter
b, a = signal.butter(4, [0.5, 40], btype='bandpass', fs=250)

# Simulated ECG signal
raw_ecg = np.random.randn(1000) + np.sin(2 * np.pi * 1.2 * np.linspace(0, 4, 1000))
clean_ecg = signal.filtfilt(b, a, raw_ecg)

# R-peak detection
peaks = signal.find_peaks(clean_ecg, distance=150)[0]
segments = [clean_ecg[i-50:i+100] for i in peaks if i > 50 and i + 100 < len(clean_ecg)]

print(f"Cleaned signal length: {len(clean_ecg)}")
print(f"R-peaks found: {len(peaks)}")
print(f"Segments extracted: {len(segments)}")

# Model architecture (requires TensorFlow if running)
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv1D, Dense, Flatten
# model = Sequential([
#     Conv1D(32, 5, activation='relu', input_shape=(150, 1)),
#     Flatten(),
#     Dense(5, activation='softmax')
# ])
# print("CNN model ready!")
