# Lunes

This is a little thought experiment: What if the calendar was mostly a lunar calendar? I mean months based on moon phase, but also days being determined by moonrise instead of sunrise. What would that look like? This little program was made to answer these questions.

Months start at the first moonrise after the new moon - keep in mind that a perfect new moon can happen when the moon is below the local horizon. The first month of the year is the month that contains the vernal equinox. I did this so that September, October, November and December align roughly with months 7, 8, 9 and 10. The vernal equinox does not align nicely with the phases of the moon unfortunately. This means that the first day of the year can be all over the place. This is the same reason that lunar based religious observances such as Easter and Passover can be all over the place on the Gregorian calendar.

A "lune" is a lunar day. It begins when the moon rises and ends at the next moonrise. Since the moon travels in the same direction as the Earth's rotation, each lune is 24.5 to 25.25 hours long. This means that each lune starts later each day, until a lune starts before midnight on one day and ends just after midnight two days later. This is demonstrated in the [tutorial](tutorial.md).

## Requirements

This program uses [PyEphem](http://rhodesmill.org/pyephem/index.html). I found that it needed to be compiled when I used pip on Linux. On Windows it was ready to go using pip. On Linux I would recommend installing it with your package manager if it is available on your distribution. I don't know how it goes with Mac.

On Windows, assuming you have Python 3 installed already, type `pip install pyephem`.

To get a quick summary for the current year, type `python lunes.py`. On Linux you may have to use the command `python3` to specify Python 3. You can have more fun in interactive mode. See the [tutorial](tutorial.md).

## TODO

- [ ] Add command line parameter handling.
- [ ] Allow users to specify their own location.
- [ ] Print out month calendar in MarkDown.
- [ ] Print out full year calendar in MarkDown.
- [ ] HTML output.
