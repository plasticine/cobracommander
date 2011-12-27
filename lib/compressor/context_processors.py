import subprocess
from os import path
from django.conf import settings

class CoffeescriptSyntaxError(Exception):
    pass

class Coffeescript(object):
    def __init__(self):
        self.cwd        = None
        self.stdout     = subprocess.PIPE
        self.stdin      = subprocess.PIPE
        self.stderr     = subprocess.PIPE
        self.command    = "%(binary)s %(args)s %(outfile)s %(infile)s"
        self.options    = {
            "binary":       settings.COMPRESS_COFFEE_BINARY,
            "args":         "-c -o",
            "infile":       path.join(settings.STATIC_ROOT, "coffeescripts"),
            "outfile":      path.join(settings.STATIC_ROOT, "javascripts")
        }

    def brew(self):
        try:
            command = self.command % self.options
            proc = subprocess.Popen(command, shell=True, cwd=self.cwd,
                stdout=self.stdout, stdin=self.stdin, stderr=self.stderr)
            filtered, err = proc.communicate()
            if err:
                raise CoffeescriptSyntaxError('Failed with error: "%s"' % err)
        except (IOError, OSError), e:
            raise FilterError('Unable to apply %s (%r): %s' %
                              (self.__class__.__name__, self.command, e))

def brew_coffee(request):
    """
    Brew out coffee files in development.
    """
    Coffeescript().brew()
    return {}
