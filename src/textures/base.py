from numpy import array, any
from PIL   import Image, PyAccess


class Texture:
    # -> Special -------------------------------------------------------------------------------------------------------
    def __init__(self, path: str) -> None:
        self._image     : Image = Image.open(path).convert('RGBA')
        self._extension : str   = path.split('.')[-1]
        self._file      : str   = path.split('/')[-1]
        self._path      : str   = path

    def __str__(self) -> str:
        return (
            f'Name     : {self._file}\n'
            f'Path     : {self._path}\n'
            f'Extension: {self._extension}'
        )

    # -> Instance ------------------------------------------------------------------------------------------------------
    @property
    def extension(self) -> str:
        return self._extension

    @property
    def file(self) -> str:
        return self._file

    @property
    def path(self) -> str:
        return self._path

    def _save_as(self, extension: str) -> str:
        """
        Save the image with the specified format. By default, all images are opened in RGBA mode, if the image is to
        be saved in .jpeg format - it will be converted to RGB mode.
        :param extension: str: File format ('tga', 'png', 'jpeg')
        :return:          str: New file path
        """
        image : Image = self._image if extension != 'jpeg' else self._image.convert('RGB')

        image.save(
            path  := f'output/{self._file.replace(self._extension, extension)}',
            format = extension
        )

        return path

    def has_alpha(self) -> bool:
        """
        Primitive image check for alpha channel, current extension is checked with extensions that have no alpha channel
        :return: bool: True, if the image has an alpha channel
        """
        return self._extension not in ['jpg', 'jpeg']

    def is_transparent(self) -> bool:
        """
        This method checks if the image is transparent. The check is performed as follows: the alpha channel of each
        pixel is extracted from the image, and if any value in the array is less than 255, the image is transparent.
        :return: bool: True if the image is transparent
        """
        if not self.has_alpha():
            return False

        alpha_channel : array = array(self._image)[:, :, 3]

        return any(alpha_channel < 255)

    def generate_transparent(self) -> 'Texture':
        """
        Generation of _trans image, according to s&box requirements. Each channel of each pixel in the image is
        replaced by an alpha channel value.
        :return: Texture: Texture instance
        """
        if not self.is_transparent():
            raise TypeError(
                'Image is not transparent'
            )

        width  : int
        height : int

        new_path  : str      = f'output/{"_".join(self._file.split("_")[:-1]) + f"_trans.{self._extension}"}'
        new_image : Image    = self._image
        pixels    : PyAccess = new_image.load()

        width, height = new_image.size

        for y in range(height):
            for x in range(width):
                r, g, b, a   = pixels[x, y]
                pixels[x, y] = (a, a, a, a)

        # TODO: Might need to save the image differently, worth thinking about in the future
        new_image.save(
            fp     = new_path,
            format = self._extension
        )

        return self.__class__(new_path)


class TGAMixin:
    def save_as_tga(self) -> str:
        if not isinstance(self, Texture):
            raise TypeError(
                "save_as_tga can only be called on objects of type Texture"
            )

        return self._save_as('tga')


class PNGMixin:
    def save_as_png(self) -> str:
        if not isinstance(self, Texture):
            raise TypeError(
                "save_as_png can only be called on objects of type Texture"
            )

        return self._save_as('png')


class JPGMixin:
    def save_as_jpg(self) -> str:
        if not isinstance(self, Texture):
            raise TypeError(
                "save_as_jpg can only be called on objects of type Texture"
            )

        return self._save_as('jpeg')


class DDSTexture(Texture, TGAMixin, PNGMixin, JPGMixin):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class PNGTexture(Texture, TGAMixin, JPGMixin):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class TGATexture(Texture, PNGMixin, JPGMixin):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class JPGTexture(Texture, TGAMixin, PNGMixin):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
