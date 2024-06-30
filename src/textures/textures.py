from numpy import array, any
from PIL   import Image


class Texture:
    # -> Special -------------------------------------------------------------------------------------------------------
    def __init__(self, file: str) -> None:
        self._image     : Image = Image.open(file).convert('RGBA')
        self._extension : str   = file.split('.')[-1]
        self._file      : str   = file

    def __str__(self) -> str:
        return (
            f'Name     : {self._file}'
            f'Extension: {self._extension}'
        )

    # -> Instance ------------------------------------------------------------------------------------------------------
    @property
    def extension(self) -> str:
        return self._extension

    @property
    def file(self) -> str:
        return self._file

    def __save_as(self, extension: str) -> None:
        """
        Save the image with the specified format.
        :param extension: File format ('tga', 'png', 'jpg')
        :return:          None
        """
        self._image.save(
            f'output/{self._file.replace(self._extension, extension)}',
            format=extension
        )

    def is_transparent(self) -> bool:
        """
        This method checks if the image is transparent. The check is performed as follows: the alpha channel of each
        pixel is extracted from the image, and if any value in the array is less than 255, the image is transparent.
        :return: bool: True if the image is transparent
        """
        alpha_channel : array = array(self._image)[:, :, 3]

        return any(alpha_channel < 255)


class TGAMixin:
    def save_as_tga(self) -> None:
        if not isinstance(self, Texture):
            raise TypeError("save_as_tga can only be called on objects of type Texture")

        self.__save_as('tga')


class PNGMixin:
    def save_as_png(self) -> None:
        if not isinstance(self, Texture):
            raise TypeError("save_as_png can only be called on objects of type Texture")

        self.__save_as('png')


class JPGMixin:
    def save_as_jpg(self) -> None:
        if not isinstance(self, Texture):
            raise TypeError("save_as_jpg can only be called on objects of type Texture")

        self.__save_as('jpg')


class PNGTexture(Texture, TGAMixin, JPGMixin):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class TGATexture(Texture, PNGMixin, JPGMixin):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class JPGTexture(Texture, TGAMixin, PNGMixin):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
