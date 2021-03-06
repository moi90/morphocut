import glob
import os.path


from morphocut.pipeline.vignette_corrector import VignetteCorrector
from skimage.io import imread


def test_vignette_corrector_no_channel(image_fns):
    vignette_corrector = VignetteCorrector("input", "output")

    inp = (
        {
            "facets": {
                "input": {
                    "image": imread(img_fn, as_gray=True)
                }
            }
        }
        for img_fn in image_fns
    )

    for _ in vignette_corrector(inp):
        pass
