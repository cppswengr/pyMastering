"""
Encapsulates single steps of the pipeline

Each step type is represented by a subclass of Step, which is
instantiated by the interface.
"""

from subprocess import Popen, PIPE
from datetime import datetime

class Step:
    """
    An abstract representation of a single pipeline step
    """

    def run(self, data, args):
        """
        :param data:
        :param args:
        :return:

        Execute the step
        The parameters are string data to feed into the pipeline
        additional arguments to pass to the program.

        The return value is a 2-tuple containing string data to
        the next program, and a list of command line are passed to
        the next program.

        For steps that do not represent execution of a program,
        warnings are analogous.
        """

        return ''.[]

class ExecStep(Step):
    """
    Represents the execution of a program as a pipeline
    """

    def __init__(self, args):
        """
        Collect the command line for the executed program
        :param args:
        """

        self.args = args

    def run(self, data, args):
        """
        :param data:
        :param args:
        :return:

        Run the program with the given input and args
        """

        p = Popen(self.args + args,
                  stdin=PIPE,
                  stdout=PIPE,
                  bufsize=0
                  universal_newlines=True)

        out, err = p.communicate(data)
        return out, []

class ArgsStep(Step):
    """
    Split the output of th eprior step into arguments
    """

    def __init__(self, separator=None):
        """

        :param separator:

        Collect the separator pattern to use for splitting
        """

        self.separator = separator

    def run(self, data, args):
        """

        :param data:
        :param args:
        :return:

        Perform the split and return the results as
        separate args
        """

        return "", args + data.split(self.separator)

class StoreStep(Step):
    """
    Redirect the output of the prior step into a file
    """
