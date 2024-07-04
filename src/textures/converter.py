from src.textures.base import Texture, DDSTexture, PNGTexture, TGATexture, JPGTexture
from typing            import Union
from os                import listdir


class Converter:
    # -> Special -------------------------------------------------------------------------------------------------------
    def __init__(self, path: str, extension: str, to: str) -> None:
        if extension == to:
            raise TypeError(
                f"The image is already in the right extension: {extension} -> {to}"
            )

        if extension not in (extensions := ["dds", "png", "tga", "jpg"]):
            raise TypeError(
                f"The source image does not match any of the available extensions: {extension} -> {extensions}"
            )

        if to not in (extensions := ["png", "tga", "jpg"]):
            raise TypeError(
                f"The final image does not match any of the available extensions: {to} -> {extensions}"
            )

        self._extension : str           = extension
        self._path      : str           = path
        self._to        : str           = to
        self._images    : list[Texture] = self._get_images()

    def __str__(self) -> str:
        return (
            f'Path     : {self._path}\n'
            f'Extension: {self._extension}'
        )

    # -> Instance ------------------------------------------------------------------------------------------------------
    @property
    def images(self) -> list[str]:
        return [image.file for image in self._images]

    @property
    def path(self) -> str:
        return self._path

    @property
    def extension(self) -> str:
        return self._extension

    def _get_image(self, path: str) -> Texture:
        match self._extension:
            case 'dds':
                return DDSTexture(path)

            case 'png':
                return PNGTexture(path)

            case 'tga':
                return TGATexture(path)

            case 'jpg':
                return JPGTexture(path)

            case _:
                raise ValueError(
                    f'The image does not match any of the available types'
                )

    def _get_images(self) -> list[Texture]:
        return [self._get_image(f'{self._path}/{img}') for img in listdir(self._path)
                if img.endswith(f'.{self._extension}')]

    def _convert(self, image: Union[DDSTexture, PNGTexture, TGATexture, JPGTexture]) -> None:
        match self._to:
            case 'png':
                image.save_as_png()

            case 'tga':
                image.save_as_tga()

            case 'jpg':
                image.save_as_jpg()

            case _:
                raise ValueError(
                    f'Conversion Error: {self._extension} -> {self._to}'
                )

    def convert(self) -> None:
        if not self._images:
            raise ValueError(
                f'The directory is empty: {self._path}'
            )

        for image in self._images:
            try:
                self._convert(image)

            except ValueError:
                pass


