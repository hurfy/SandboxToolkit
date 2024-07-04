from os.path import isfile


class TextureSet:
    # TODO: Perhaps we should pass not a path, but a ready-made set of paths to textures with the same name?
    def __init__(self, file: str, path: str) -> None:
        self._file     : str  = file
        self._path     : str  = path
        self._name     : str  = file.split('.')[0]
        self._textures : dict = self._build()

    def __str__(self) -> str:
        return str(self._textures)

    @property
    def file(self) -> str:
        return self._file

    @property
    def textures(self) -> dict:
        return self._textures

    def _build(self) -> dict:
        textures : dict  = {}
        types    : tuple = (
            ('translucent'      , 'trans'),
            ('ambient_occlusion', 'ao'),
            ('normal'           , 'normal'),
            ('roughness'        , 'rough')
        )

        for img_type in types:
            image = f'{self._path}/{self._name}/{img_type[1]}'
            textures[img_type[0]] = image if isfile(image) else None

        return textures
