from copy import copy

from squidpy.datasets._utils import ImgMetadata

_vfic = ImgMetadata(
    name="visium_fluo_image_crop",
    doc_header="Cropped Fluorescent image from `10x Genomics Visium dataset "
    "<https://support.10xgenomics.com/spatial-gene-expression/datasets"
    "/1.1.0/V1_Adult_Mouse_Brain_Coronal_Section_2>`__.",
    shape=(7272, 7272),
    url="https://ndownloader.figshare.com/files/26098364?private_link=4b3abee143a3852b9040",
)
_vhic = ImgMetadata(
    name="visium_hne_image_crop",
    doc_header="Cropped HnE image from `10x Genomics Visium dataset "
    "<https://support.10xgenomics.com/spatial-gene-expression/datasets/1.1.0/V1_Adult_Mouse_Brain>`_.",
    shape=(3527, 3527),
    url="https://ndownloader.figshare.com/files/26098328?private_link=33ef1d60cfcadb91518c",
)
_vhn = ImgMetadata(
    name="visium_hne_image",
    doc_header="HnE image from `10x Genomics Visium dataset "
    "<https://support.10xgenomics.com/spatial-gene-expression/datasets/1.1.0/V1_Adult_Mouse_Brain>`_.",
    shape=(11757, 11291),
    url="https://ndownloader.figshare.com/files/26098124?private_link=9339d85896f60e41bf19",
)


for name, var in copy(locals()).items():
    if isinstance(var, ImgMetadata):
        var._create_function(name, glob_ns=globals())


__all__ = [  # noqa: F822
    "visium_fluo_image_crop",
    "visium_hne_image_crop",
    "visium_hne_image",
]