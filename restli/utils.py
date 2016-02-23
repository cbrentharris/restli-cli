import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('restli')

class OutputMessages(object):

    GENERATING = """
    generating {}
    """

    OVERWRITING = """
    overwriting {}
    """

    LEAVING_FILE_UNTOUCHED = """
    leaving file untouched {}
    """

    WOULD_YOU_LIKE_TO_OVERWRITE = """
    It looks like there is already a file named {} within the directory {}. Would you like to overwrite it? (y/n) :
    """

    NO_DIRECTORY_FOUND = """
    No directory "{}" found in cwd. Please run restli --scaffold [project-name] --namespace [namespace] to generate a restli directory structure
    """

    # Thanks @dhobbs http://stackoverflow.com/questions/9727673/list-directory-tree-structure-using-python
    @staticmethod
    def tree(start_path):
        acc = ""
        for root, dirs, files in os.walk(start_path):
            level = root.replace(start_path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            acc += '{}{}/\n'.format(indent, os.path.basename(root))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                acc += '{}{}\n'.format(subindent, f)
        return acc
