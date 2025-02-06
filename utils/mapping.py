import geemap
from ee import FeatureCollection, Image


def create_geemap(
    image: Image,
    data_viz: dict,
    map_title: str,
    center_by: Image | FeatureCollection,
    continuous: bool = False,
    categorical: bool = False,
):
    if continuous and categorical:
        raise ValueError("Only one of 'continuous' or 'categorical' can be True.")

    m = None
    m = geemap.Map()
    m.addLayer(image, data_viz, map_title)
    m.centerObject(center_by)
    m.add_text("Made by Ilse Paniagua")
    if continuous:
        m.add_colorbar(
            data_viz,
            label=map_title,
            layer_name=map_title,
            orientation="horizontal",
        )
    if categorical:
        m.add_legend(legend_dict=data_viz, title=map_title)
    return m
