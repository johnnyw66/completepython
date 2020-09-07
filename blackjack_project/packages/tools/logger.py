import sys


class BaseDebug():
        @staticmethod
        def who_am_i(frame_index=1):
                # frame '1' is the 'calling frame'
                return sys._getframe(frame_index).f_code.co_name

        @staticmethod
        def where_am_i(frame_index=1):
                return sys._getframe(frame_index).f_lineno

        @staticmethod
        def which_file(frame_index= 1):
                return sys._getframe(frame_index).f_code.co_filename


class Logger(BaseDebug):
    level = 0

    @staticmethod
    def log(msg,level = 0):
        if (level >= Logger.level):
            print(msg)

    def __init__(self, *args, **kwargs):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.decor_args = args
        self.decor_kwargs = kwargs


    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        def wrapped_f(*args):
            line_num = BaseDebug.where_am_i(2)
            source_file = BaseDebug.which_file(2)
#            self.logger(f"LOG:{self.decor_args[0]}:Level = {self.decor_kwargs['level']} Line: {line_num} {f.__name__} {args} @ {source_file}")
            Logger.log(f"{self.decor_args[0]} Line: {line_num} {f.__name__}{args} @{source_file}",self.decor_kwargs['level'])

            res = f(*args)
            return res
        return wrapped_f
