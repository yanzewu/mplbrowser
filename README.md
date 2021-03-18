# MPLBrowser

Display Matplotlib image in your browser, instead of using X-Window system (often slow).

__Usage__: Just replace `plt.show()` by `mplbrowser.show()`. For example,

    import matplotlib.pyplot as plt
    import mplbrowser

    plt.switch_backend('Agg')   # This is not necessary, but useful when X11 is not functioning properly
    plt.plot([1,2,3])
    mplbrowser.mute_logging()   # Disable log from flask (not necessary)
    mplbrowser.show()

Then open browser at [http://127.0.0.1:8100](http://127.0.0.1:8100) to receive the image. The browser can receive images from multiple instances without refreshing.

__Installation__: run `pip install -e mplbrowser` after cloning the repository and switching to project rootdir.

__Prerequesties__: flask.


