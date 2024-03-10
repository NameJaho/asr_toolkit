import time
import os
from collections.abc import Sequence
import pkg_resources

from loguru import logger


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        class_name = args[0].__class__.__name__
        end_time = time.time()
        execution_time = end_time - start_time
        logger.debug(f"{class_name}.{func.__name__} executed in {execution_time:.4f} seconds.")
        return result

    return wrapper


def load_text(*file_paths, by_lines=False):
    with open(f_join(*file_paths), "r", encoding="utf-8") as fp:
        if by_lines:
            return fp.readlines()
        else:
            return fp.read()


def f_join(*file_paths):
    """
    join file paths and expand special symbols like `~` for home dir
    """
    file_paths = pack_varargs(file_paths)
    fpath = f_expand(os.path.join(*file_paths))
    if isinstance(fpath, str):
        fpath = fpath.strip()
    return fpath


def f_expand(fpath):
    return os.path.expandvars(os.path.expanduser(fpath))


def pack_varargs(args):
    """
    Pack *args or a single list arg as list

    def f(*args):
        arg_list = pack_varargs(args)
        # arg_list is now packed as a list
    """
    assert isinstance(args, tuple), "please input the tuple `args` as in *args"
    if len(args) == 1 and is_sequence(args[0]):
        return args[0]
    else:
        return args


def is_sequence(obj):
    """
    Returns:
      True if the sequence is a collections.Sequence and not a string.
    """
    return isinstance(obj, Sequence) and not isinstance(obj, str)


def get_root_path():
    package_path = pkg_resources.resource_filename(__name__, "")
    parent_path = os.path.dirname(package_path)
    return parent_path


def get_file_paths(directory):
    """
    从目录中读出所有文件路径，并生成一个列表。

    Args:
        directory (str): 目录路径。

    Returns:
        list: 文件路径列表。
    """

    # 获取目录中的所有文件和子目录
    files = os.listdir(directory)

    # 创建一个空列表来存储文件路径
    file_paths = []

    # 遍历文件和子目录
    for file in files:
        # 如果是文件，则将其路径添加到列表中
        if os.path.isfile(os.path.join(directory, file)):
            file_paths.append(os.path.join(directory, file))
        # 如果是子目录，则递归调用此函数来获取子目录中的文件路径
        elif os.path.isdir(os.path.join(directory, file)):
            file_paths.extend(get_file_paths(os.path.join(directory, file)))

    # 返回文件路径列表
    return file_paths


def get_file_name(file_path):
    """
    根据文件路径获取文件名，不要后缀。

    Args:
        file_path (str): 文件路径。

    Returns:
        str: 文件名，不要后缀。
    """

    # 获取文件名，包括后缀
    file_name = os.path.basename(file_path)

    # 分割文件名和后缀
    file_name, file_extension = os.path.splitext(file_name)

    # 返回文件名，不要后缀
    return file_name
