import pylsl

streams = pylsl.resolve_stream('name', 'PetalStream_eeg')
inlet = pylsl.StreamInlet(streams[0])
while True:
    sample, timestamp = inlet.pull_sample()
    print(timestamp, sample)