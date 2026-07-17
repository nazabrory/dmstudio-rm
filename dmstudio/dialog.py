'''
dmstudio.dialog
---------------

Context manager that spawns a background thread to automatically dismiss
blocking "#32770" modal dialogs produced by Datamine Studio RM.
'''
import threading
import time
import contextlib

try:
    import win32gui
    import win32con
    import win32api
    WIN32_AVAILABLE = True
except ImportError:
    WIN32_AVAILABLE = False


@contextlib.contextmanager
def dialog_dismiss_context(title='Studio RM', interval=1.0):
    '''
    dialog_dismiss_context
    ----------------------

    Context manager that spawns a background thread to automatically dismiss
    blocking "#32770" modal dialogs produced by Datamine Studio RM (e.g.
    "Duplicate Project File" prompts). This is opt-in: it only runs when
    explicitly used as a context manager.

    Parameters:
    -----------
    title: str
        Window title to match for dismissal. Default: 'Studio RM'.
    interval: float
        Polling interval in seconds. Default: 1.0.

    Usage:
    ------
    from dmstudio import dialog, dmcommands
    cmd = dmcommands.init(version='StudioRM')

    with dialog.dialog_dismiss_context():
        cmd.copy(in_i='source', out_o='dest')
    '''
    stop_event = threading.Event()
    t = None

    def _dismiss_loop():
        if not WIN32_AVAILABLE:
            return
        while not stop_event.is_set():
            try:
                def _enum_callback(hwnd, _):
                    if not win32gui.IsWindowVisible(hwnd):
                        return
                    cls = win32gui.GetClassName(hwnd)
                    ttl = win32gui.GetWindowText(hwnd)
                    if cls == '#32770' and title in ttl:
                        # Try 'Yes' button (ID=6), then 'OK' button (ID=1)
                        for btn_id in (6, 1):
                            try:
                                win32api.SendMessage(hwnd, win32con.WM_COMMAND, btn_id, 0)
                            except Exception:
                                pass
                win32gui.EnumWindows(_enum_callback, None)
            except Exception:
                pass
            time.sleep(interval)

    if WIN32_AVAILABLE:
        t = threading.Thread(target=_dismiss_loop, daemon=True)
        t.start()

    try:
        yield
    finally:
        stop_event.set()
        if t is not None:
            t.join(timeout=interval * 2)
