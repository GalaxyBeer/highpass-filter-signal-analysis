
# High-Pass Filter Signal Analysis

A Python script for analyzing and filtering an audio signal using a Butterworth high-pass filter and visualizing the results in both time and frequency domains.

## How it works

Loading the Audio File: \n
An audio file is loaded through the specified file path. The sampling frequency and audio data are assigned to variables.

Creating the Butterworth High-Pass Filter: \n
The butter_highpass() function creates a Butterworth high-pass filter using the specified cutoff frequency and sampling frequency. This filter suppresses unwanted low-frequency components.

Applying the Filtering: \n
The highpass_filter() function applies the high-pass filter to the original audio data using the created filter. The result is stored in an array named filtered_data.

Saving the Filtered Signal: \n
The wavfile.write() function saves the filtered audio data to a WAV file with the specified file name and sampling frequency.

Plotting Signals in the Time Domain: \n
The original and filtered audio data are plotted as amplitude (voltage) versus time (seconds). The original signal is shown in blue, while the filtered signal is shown in orange.

Plotting Signals in the Frequency Domain: \n
The original and filtered signals are plotted as amplitude versus frequency (Hertz). These plots show the strengths of the original and filtered signals at various frequencies.

![image](https://github.com/GalaxyBeer/highpass-filter-signal-analysis/assets/72799974/fdf69841-0375-4feb-b31c-465a5969ff6e)

## How to Use

1. Place your audio file in the specified path.
2. Run the `highpass_filter.py` script to analyze and filter the audio file, and visualize the results.
3. The filtered audio file will be saved as `filtered_bird_plane_sound.wav`.

## Requirements

- `numpy`
- `scipy`
- `seaborn`
- `matplotlib`

## Contribution

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new pull request.
