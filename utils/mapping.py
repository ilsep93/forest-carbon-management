import geemap
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from ee import FeatureCollection, Image

forest_type_dict = {
    # "0 Unknown": "282828",
    "1 Evergreen needle leaf": "666000",
    "2 Evergreen broad leaf": "009900",
    "3 Deciduous needle leaf": "70663e",
    "4 Deciduous broad leaf": "a0dc00",
    "5 Mix of forest types": "929900",
}

land_cover_dict = {
    # "0 Unknown": "282828",
    "20 Shrubs": "ffbb22",
    "30 Herbaceous Vegetation": "ffff4c",
    "40 Cultivated and Managed Vegetation/Agriculture": "f096ff",
    "50 Urban/Built Up": "fa0000",
    "60 Bare/Sparse Vegetation": "b4b4b4",
    # "70 Snow and Ice": "f0f0f0",
    "80 Permanent Water Bodies": "0032c8",
    "90 Herbaceous Wetland": "0096a0",
    # "100 Moss and Lichen": "fae6a0",
    "111 Closed Forest, Evergreen Needle Leaf": "58481f",
    "112 Closed Forest, Evergreen Broad Leaf": "009900",
    "113 Closed Forest, Deciduous Needle Leaf": "70663e",
    "114 Closed Forest, Deciduous Broad Leaf": "00cc00",
    "115 Closed Forest, Mixed": "4e751f",
    "116 Closed Forest, Other": "007800",
    "121 Open Forest, Evergreen Needle Leaf": "666000",
    "122 Open Forest, Evergreen Broad Leaf": "8db400",
    "123 Open Forest, Deciduous Needle Leaf": "8d7400",
    "124 Open Forest, Deciduous Broad Leaf": "a0dc00",
    "125 Open Forest, Mixed": "929900",
    "126 Open Forest, Other": "648c00",
    # "200 Oceans/Seas": "000080"
}


def matplotlib_ramp_to_hexcodes(color_ramp: str, n_colors: int = 9) -> list:
    cmap = plt.get_cmap(color_ramp)

    # Generate the colors
    colors = [cmap(i / (n_colors - 1)) for i in range(n_colors)]

    # Convert to hex
    hex_colors = [mcolors.rgb2hex(color) for color in colors]

    return hex_colors


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
            # label=map_title,
            layer_name=map_title,
            orientation="horizontal",
        )
    if categorical:
        m.add_legend(legend_dict=data_viz, title=map_title)
    return m
