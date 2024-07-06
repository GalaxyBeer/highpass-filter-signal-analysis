import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, lfilter

# Dosyayı yükle
fs, data = wavfile.read(r"E:\SayisalHaberlesme_Proje\kus_ucak_sesi.wav")

# Butterworth Yüksek Geçiren Filtre (High-Pass Filter)
def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

cutoff_freq = 1500  # kesim frekansı

# Filtreyi uygulayın
filtered_data = highpass_filter(data, cutoff_freq, fs)

# Sonucu kaydedin
wavfile.write('filtered_bir_plane_sound.wav', fs, filtered_data.astype(np.int16))

# Zaman ekseninde sinyaller
time = np.arange(len(data)) / fs

# Orijinal Sinyal (Zaman Alanı)
plt.figure(figsize=(12, 6))
plt.plot(time, data, label='Orijinal Sinyal')
plt.title('Orijinal Sinyal (Zaman Alanı)')
plt.xlabel('Zaman (s)')
plt.ylabel('Genlik')
plt.legend()
plt.grid()

# Filtrelenmiş Sinyal (Zaman Alanı)
plt.figure(figsize=(12, 6))
plt.plot(time, filtered_data, label='Filtrelenmiş Sinyal', color='orange')
plt.title('Filtrelenmiş Sinyal (Zaman Alanı)')
plt.xlabel('Zaman (s)')
plt.ylabel('Genlik')
plt.legend()
plt.grid()

# Frekans alanında sinyaller
data_freq = np.fft.rfft(data)
filtered_data_freq = np.fft.rfft(filtered_data)

freqs = np.fft.rfftfreq(len(data), 1/fs)

# 5 kHz'e kadar olan frekansları sınırlayalım
max_freq = 5000
freqs_limit = freqs <= max_freq

# Orijinal Sinyal (Frekans Alanı)
plt.figure(figsize=(12, 6))
plt.plot(freqs[freqs_limit], np.abs(data_freq)[freqs_limit], label='Orijinal Sinyal Frekans')
plt.title('Orijinal Sinyal (Frekans Alanı)')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.legend()
plt.grid()

# Filtrelenmiş Sinyal (Frekans Alanı)
plt.figure(figsize=(12, 6))
plt.plot(freqs[freqs_limit], np.abs(filtered_data_freq)[freqs_limit], label='Filtrelenmiş Sinyal Frekans', color='orange')
plt.title('Filtrelenmiş Sinyal (Frekans Alanı)')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.legend()
plt.grid()

plt.show()
