from os import path
from compressor.conf import settings
from compressor.filters import CompilerFilter

class BrewCoffeeFilter(CompilerFilter):
    command = "{binary} {args} {outfile} {infile}"
    options = (
        ("binary", settings.COMPRESS_COFFEE_BINARY),
        ("args", "-c -o"),
        ("infile", path.join(settings.STATIC_ROOT, "javascripts")),
        ("outfile", path.join(settings.STATIC_ROOT, "javascripts")),
    )

class RequireJSFilter(CompilerFilter):
    command = "{binary} {args} {infile}"
    options = (
        ("binary", settings.COMPRESS_RJS_BINARY),
        ("args", settings.COMPRESS_RJS_ARGUMENTS),
    )
