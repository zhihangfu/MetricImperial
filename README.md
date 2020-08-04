# Metric & Imperial Length Units Conversion Tool
To save Metric kids like me who lives in an Imperial world, or Imperial kids who need to work with Metric system.

* You will need to have Python 3 installed.
* Run .py file in Mac OS.
* Change file extension to .pyw on Windows platform. This will tell Python on Windows to run without invoking the command prompt.
* .py and .pyw files only differ in file extensions, not in actual codes, changing extensions won't break the app.
* Unzip, double-click to run. Enjoy!

Caveats:
* The GUI depends on [Tkinter](https://docs.python.org/3/library/tkinter.html), which ships with Python 3, but may not work normal in virtual Python environments (such as anaconda and pyenv).
* UI may look awkward on platforms other than Mac OS or Windows, for I have not tested on such platforms.
* Let me know if there are any issues, I'd be happy to debug.

Version 1:
1. initial version. Units include mm, inch, feet&inch.

Version 2:
1. added a new line of units: pitch & pixel for assessing screen products. 

Version 3:
1. now you can use python expressions in Entry Boxes to do basic calculations!!
2. disabled input into “pixel”, for it's driven by resolution, not the other way around.
3. added “clear” button, which will delete all lingering numbers.
4. fixed bug that “pitch” input cannot be “0".
5. UI updates.

Version 3.1
1. Element sizes adaptive to windows size

![](/ScreenshotMacV3.1.png)
