__author__ = 'Mark Walker'

import os
import errno


def mkdir_p(path):
    """
    imitates mkdir -p by silently failing existence errors
    """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            pass
        else:
            raise


def get_temp_dir(subdirs=None):
    """
    Return a path to a suitable location for writing temporary log files. You
    can obtain a subfolder of the standard "/tmp"/"%TMP%" location by providing
    a list of subfolder names, so for instance subdirs=["folder1", "folder2"]
    would return "/tmp/folder1/folder2".

    Note that the directory is not automatically created.

    @param subdirs: A list indicating the subdirectory to create
    @type subdirs:  []

    @return:        The path to the temporary directory
    @rtype:         str
    """
    temp_dir = ""
    if os.environ.has_key("TMP"):
        temp_dir = os.environ["TMP"]
    elif os.environ.has_key("TEMP"):
        temp_dir = os.environ["TEMP"]
    elif os.path.exists("/tmp"):
        temp_dir = "/tmp"

    if subdirs is not None:
        temp_dir = os.path.join(temp_dir, *subdirs)

    return temp_dir