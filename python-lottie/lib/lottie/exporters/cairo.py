try:
    import cairosvg
    has_cairo = True
except (ImportError, OSError):
    has_cairo = False

from ..parsers import glaxnimate_helpers

import io

from .base import exporter
from .svg import export_svg


def _export_cairo(func, animation, fp, frame, dpi):
    intermediate = io.StringIO()
    export_svg(animation, intermediate, frame)
    intermediate.seek(0)
    func(file_obj=intermediate, write_to=fp, dpi=dpi)


if glaxnimate_helpers.has_glaxnimate:
    @exporter("PNG", ["png"], [], {"frame"})
    def export_png(animation, fp, frame=0, dpi=96):
        data = glaxnimate_helpers.serialize(animation, "raster")

        if isinstance(fp, str):
            with open(fp, 'wb') as file:
                file.write(data)
        else:
            fp.write(data)

elif has_cairo:
    @exporter("PNG", ["png"], [], {"frame"})
    def export_png(animation, fp, frame=0, dpi=96):
        _export_cairo(cairosvg.svg2png, animation, fp, frame, dpi)


if has_cairo:
    @exporter("PDF", ["pdf"], [], {"frame"})
    def export_pdf(animation, fp, frame=0, dpi=96):
        _export_cairo(cairosvg.svg2pdf, animation, fp, frame, dpi)

    @exporter("PostScript", ["ps"], [], {"frame"})
    def export_ps(animation, fp, frame=0, dpi=96):
        _export_cairo(cairosvg.svg2ps, animation, fp, frame, dpi)
