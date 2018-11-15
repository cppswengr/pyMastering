import cmd, pickle
from os import sys, path
from pathlib import Path

class TextInterface(cmd.Cmd):
    """Text-based interface for Pipeline"""
    prompt = 'Pipeline> '

    def _init__(self, keep_going, filename):
        super().__init__(completekey = 'tab')
        self.keep_going = keep_going
        self.path = Path(filename)
        # self.prompt = 'Pipeline> '

        try:
            with self.path.open('rb') as f:
                self.steps = pickle.load(f)
        except FileNotFoundError:
            self.steps = []

    def do_save(self, arg):
        """Save the pipeline"""
        if not self.path.parent.exists():
            self.path.parent.mkdir(parents = True)

        with self.path.open('wb') as f:
            pickle.dump(self.steps, f)

    def do_quit(self, arg):
        """Exit Pipeline"""
        sys.exit(0)

    def do_exec(self, arg):
        """Append a program invocation to the pipeline"""