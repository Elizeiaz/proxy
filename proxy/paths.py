import os


class Path:
    def __init__(self):
        self.__cur_dir = os.getcwd()
        self.__root = os.path.normpath(self.__cur_dir + os.sep + os.pardir)

    @property
    def cur_dir(self):
        return self.__cur_dir

    @cur_dir.setter
    def set_cur_dir(self, new_cur_dir):
        self.__cur_dir = new_cur_dir

    @property
    def root(self):
        return self.__root

    @root.setter
    def set_root(self, new_root_dir):
        self.__root = new_root_dir

    @property
    def log_dir(self):
        return os.path.join(self.root, "log")

    @property
    def log_properties(self):
        return os.path.join(self.log_dir, "log.properties")
