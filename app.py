import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fft import rfft, rfftfreq
from scipy.fft import irfft
import numpy as np
from scipy.io.wavfile import write
import IPython

def analyze_wav(uploaded_file, remove_freq_start, remove_freq_stop):
    st.title("Plot frequency before after")
    rate, data= wav.read(uploaded_file)
    data=data[:,0]
    N=int(len(data))
    yf_old=rfft(data)
    xf=rfftfreq(N, 1/rate)
    st.subheader("Before adjusting")
    plt.figure(figsize=(8,4))
    plt.plot(xf, np.abs(yf_old))
    st.pyplot(plt)
    yf_new=yf_old
    yf_new[:remove_freq_start]=0
    yf_new[remove_freq_stop:]=0
    new_sig = irfft(yf_new)
    adjusted_path=f"cleaned_file.wav"
    write(adjusted_path, rate, new_sig)
    st.subheader("Plot after adjusting")
    plt.figure(figsize=(8,4))
    plt.plot(xf, np.abs(yf_new))
    st.pyplot(plt)

    


def main():
    st.title("WAV Frequency Remover")

    uploaded_file=st.file_uploader("Upload a WAV file", type=["wav"])

    if uploaded_file is not None:
        remove_freq_start=st.number_input("What frequency to remove from?")
        remove_freq_stop=st.number_input("What frequency to remove to?")

        if st.button("Analyze"):
           analyze_wav(uploaded_file, int(remove_freq_start), int(remove_freq_stop))



if __name__=="__main__":
    main()

 



