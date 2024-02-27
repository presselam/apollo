import os


class Configuration:
    _singleton = None

    def __new__(cls):
        if cls._singleton is None:
            cls._singleton = super(Configuration, cls).__new__(cls)

        return cls._singleton

    def __init__(self):
        self.base_dir = os.getenv("HOME") + "/.apollo"
        self.log_dir = f"{self.base_dir}/logs"
        self.history_dir = f"{self.base_dir}/history"

        for cache in [self.history_dir, self.log_dir]:
            if not os.path.exists(cache):
                os.makedirs(cache)
