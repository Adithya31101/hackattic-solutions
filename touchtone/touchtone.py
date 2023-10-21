from requests import get, post
from os import system
import wave
import numpy as np
from bs4 import BeautifulSoup

res = get("https://hackattic.com/challenges/touch_tone_dialing/problem?access_token=b53b9d130f72e759").json()
system("wget -O dmtf.wav " + res['wav_url'])

DTMF_FREQS = {
    '1': (1209, 697),
    '2': (1336, 697),
    '3': (1477, 697),
    '4': (1209, 770),
    '5': (1336, 770),
    '6': (1477, 770),
    '7': (1209, 852),
    '8': (1336, 852),
    '9': (1477, 852),
    '0': (1336, 941),
    '*': (1209, 941),
    '#': (1477, 941),
}

def decode_dtmf(data, fps, window=0.06, ofset=15):
    # Initialize empty list to store the decoded keys and frequencies found
    keys = []
    found_freqs = []

    # Iterate through the signal in window-sized chunks
    for i in range(0, len(data), int(fps * window)):
        # Get the current chunk of the signal
        cut_sig = data[i:i+int(fps*window)]

        # Take the Fast Fourier Transform (FFT) of the current chunk
        fft_sig = np.fft.fft(cut_sig, fps)

        # Take the absolute value of the FFT
        fft_sig = np.abs(fft_sig)

        # Set the first 500 elements of the FFT to 0 (removes DC component)
        fft_sig[:500] = 0

        # Only keep the first half of the FFT (removes negative frequencies)
        fft_sig = fft_sig[:int(len(fft_sig)/2)]

        # Set the lower bound to be 75% of the maximum value in the FFT
        lower_bound = 0.75 * np.max(fft_sig)

        # Initialize empty list to store the frequencies that pass the lower bound threshold
        filtered_freqs = []

        # Iterate through the FFT and store the indices of the frequencies that pass the lower bound threshold
        for i, mag in enumerate(fft_sig):
            if mag > lower_bound:
                filtered_freqs.append(i)

        # Iterate through the DTMF frequencies and check if any of the filtered frequencies fall within the expected range
        for char, frequency_pair in DTMF_FREQS.items():
            high_freq_range = range(
                frequency_pair[0] - ofset, frequency_pair[0] + ofset + 1)
            low_freq_range = range(
                frequency_pair[1] - ofset, frequency_pair[1] + ofset + 1)
            if any(freq in high_freq_range for freq in filtered_freqs) and any(freq in low_freq_range for freq in filtered_freqs):
                # If a match is found, append the key and frequency pair to the lists
                keys.append(char)
                found_freqs.append(frequency_pair)
    return keys, found_freqs


def get_dmtf_sequence(fname):
  with wave.open(fname, 'rb') as wave_file:
    num_samples = wave_file.getnframes()
    fps = wave_file.getframerate()
    data = wave_file.readframes(num_samples)
    sample_width = wave_file.getsampwidth()
    if sample_width == 1:
        data = np.frombuffer(data, dtype=np.uint8)
    elif sample_width == 2:
        data = np.frombuffer(data, dtype=np.int16)

  keys, found_freqs = decode_dtmf(data, fps)
  return keys

# ans = "".join(get_dmtf_sequence('dmtf.wav'))
# out = system('./dtmf.py -i 0.015 ./dmtf.wav > res.txt')

# with open('res.txt', 'r') as f:
#   resPost = post("https://hackattic.com/challenges/touch_tone_dialing/solve?access_token=b53b9d130f72e759", json={
#     "sequence": f.read()[:-1]
#   })

fd = open('dmtf.wav', 'rb')
ans = []
html_text = post("http://dialabc.com/sound/detect/index.html", files={
    "wav": ('dmtf.wav', fd)
}).text
fd.close()
soup = BeautifulSoup(html_text, 'html.parser')
for d in soup.find_all("div", attrs={"class": "dtdTone"}):
    ans.append(d.text)

resPost = post("https://hackattic.com/challenges/touch_tone_dialing/solve?access_token=b53b9d130f72e759", json={
  "sequence": "".join(ans)
})
print(resPost.json())