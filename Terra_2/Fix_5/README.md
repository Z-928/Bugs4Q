Summary

There was a bug in align_acquires. Measurement pulses which were perfectly valid were causing an error to be raised. Measure stimulus pulses weren't being aligned with the Acquire pulses.

Details and comments

This rescheduling pass doesn't support multiple measurements or pulses after measurements. Had to track which channels were acquired/measured at what times, and allow one acquire and one measure on each channel, both of which would get scheduled at the same time.
