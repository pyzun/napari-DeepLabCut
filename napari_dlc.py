from dlclabel import io
from napari_plugin_engine import napari_hook_implementation


@napari_hook_implementation(tryfirst=True, specname='napari_get_reader')
def load_images(path):
    if isinstance(path, str):
        path = [path]
    if path[0].endswith('png'):
        return io.read_images
    return None


@napari_hook_implementation(specname='napari_get_reader')
def load_labeled_data(path):
    if isinstance(path, str) and path.endswith('h5'):
        return io.read_hdf
    return None


@napari_hook_implementation(specname='napari_get_reader')
def load_config(path):
    if isinstance(path, str) and path.endswith('yaml'):
        return io.read_config
    return None


@napari_hook_implementation(tryfirst=True, specname='napari_write_points')
def save_keypoints(path, data, meta):
    return io.write_hdf(path, data, meta)
