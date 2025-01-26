from pathlib import Path

"""
Makes a Path object using the input directory string.
If a relative directory, converts it to a Path then appends it to the given relative_base Path object.
Else, if the directory str is already an absolute directory, only converts it into a Path object.
"""


def make_absolute_path(ambiguous_dir: str, relative_base: Path = Path().absolute()) -> Path:
    try:
        # Attempt to build it as a relative path
        abs_path = (relative_base / ambiguous_dir.strip(
            '\\/')).resolve()  # Note: Strips the slashes to ensure joinpath works
        if not abs_path.exists():
            raise FileNotFoundError('Could not find file at directory \"' + str(abs_path) + '\"')
    except:
        # If no relative path found, try it as an absolute path
        abs_path = Path(ambiguous_dir).resolve()
        if not abs_path.exists():
            raise FileNotFoundError('Could not find file at directory \"' + str(abs_path) + '\"')

    return abs_path
