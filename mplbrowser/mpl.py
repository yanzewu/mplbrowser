
import matplotlib.pyplot as plt
import os.path
import io
import html
from . import app


def show_or_savefig(display_only, filename='image', format=None, port=None, wait_client=True):
    """ Send current figure to remote side. 
    display_only: Display file as SVG.
    filename: The filename to save and message title.
    format: If None, will detect from filename, or use PNG by default.
    port: Default is 8100.
    wait_client: If True, will block before any client is connected.
    """

    if not app._has_started:
        app.start_application(port if port else 8100)

    format_ = os.path.splitext(filename)[1][1:] if filename else format
    if not format_ and not display_only:
        format_ = 'png'
        if filename:
            filename = filename.rstrip('.') + '.' + format_
    format_ = format_.lower()

    if display_only:
        f = io.StringIO()
        plt.savefig(f, format='svg')
    else:
        f = io.BytesIO()
        plt.savefig(f, format=format_)

    f.seek(0)
    img_id = app.place_image_data(f.read(), filename=filename)

    app.place_block(filename, img_id=img_id, is_svg=display_only, img_name=filename, img_disp=False)
    if wait_client:
        app.wait_client()


def show(*args, **kwargs):
    """ Display the figure in browser window.
    filename: Title of message.
    port: Default is 8100.
    wait_client: If True, will block before any client is connected.
    """
    return show_or_savefig(True, *args, **kwargs)


def savefig(*args, **kwargs):
    """ Save figure to remote side.
    filename: The filename to save and message title.
    format: If None, will detect from filename, or use PNG by default.
    port: Default is 8100.
    wait_client: If True, will block before any client is connected.
    """
    return show_or_savefig(False, *args, **kwargs)
