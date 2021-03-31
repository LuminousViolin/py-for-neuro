___
___
___

# import the file
h1_data = ___(
    file_name=___,
    squeeze_me=___)

# create a new key with the time points
# from 0 to the length of the data
h1_data["timepnt"] = ___
# select only those time point when spike occurred
h1_data["spike_time"] = ___
# set the window size (timepoints)
window = ___

# create a vector of zeros with the shape (window,)
h1_data["sta"] = ___
# iterate over all timepoints when spike occurred
# and use the time point as a end index
# note that we cannot take the window of length 150 for first 149 observations
for end_index in h1_data["spike_time"]___:
    # specify the start index of a window
    start_index = ___
    # take the slice from the stimulus value
    sample = ___
    # add the slice to the STA vector
    h1_data["sta"] += ___

# divide the resulted STA vector on the amount of time points
# to get the actual average
h1_data["sta"] /= ___

plt.figure(figsize=(10,5), facecolor="white")
plt.plot(range(0, 300, 2), ___)
plt.title('Spike-Triggered average', fontsize=18)
plt.ylabel('Stimulus Value, [mV]')
plt.xlabel('Time, [ms]')
plt.show()