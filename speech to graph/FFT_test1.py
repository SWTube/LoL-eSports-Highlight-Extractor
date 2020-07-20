from __future__ import print_function, division

import thinkdsp
import thinkplot

"""
    Name :	    	AmorAmare
    Team :	    	Speech Recognition
    Created :		19 1015 jul20
    Modified :	    initial
    Purpose :		sound to graph
"""

FORMATS = ['pdf', 'jpeg']

def plot_tuning(start=0.0, duration=15.0):
    """Plots three cycles of a bell playing A4.
    start: start time in seconds
    duration: float
    """

    wave = thinkdsp.read_wave('one_person.wav')

    #extract segment
    segment = wave.segment(start, duration)
    segment.normalize()

    thinkplot.preplot(1)
    segment.plot()
    thinkplot.Save(root='sounds1',
                   xlabel='Time (s)',
                   axis=[start, start+duration, -1.05, 1.05],
                   formats=FORMATS,
                   legend=False)


def segment_wave(start=0.0, duration=15.0):
    """Load a violin recording and plot its spectrum.
    start: start time of the segment in seconds
    duration: in seconds
    """
    wave = thinkdsp.read_wave('one_person.wav')

    # extract a segment
    segment = wave.segment(start, duration)
    segment.normalize()

    # plot the spectrum
    spectrum = segment.make_spectrum()

    thinkplot.preplot(1)
    spectrum.plot(high=10000)
    thinkplot.Save(root='sounds2',
                   xlabel='Frequency (Hz)',
                   ylabel='Amplitude',
                   formats=FORMATS,
                   legend=False)

    """# print the top 5 peaks
    peaks = spectrum.peaks()
    for amp, freq in peaks[:10]:
        print(freq, amp)"""


def main():
    plot_tuning()
    segment_wave()

if __name__ == '__main__':
    main()