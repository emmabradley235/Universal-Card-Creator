import yaml
from pathlib import Path
from path_utils import make_absolute_path


class GamePaths:
    def __init__(self, game_dir: str):
        self.game_folder = make_absolute_path(game_dir, relative_base=Path('_GameConfigs_'))

        self.game_info_config = self.game_folder / 'game_info.yaml'

        with open(self.game_info_config, 'r') as file:
            game_info = yaml.safe_load(file)
        
        self.card_field_config = make_absolute_path(
            game_info['Paths']['CardFieldConfig'],
            relative_base=self.game_folder
        )
        self.text_process_config = make_absolute_path(
            game_info['Paths']['TextProcessingConfig'],
            relative_base=self.game_folder
        )
        self.card_layouts_folder = make_absolute_path(
            game_info['Paths']['CardLayoutsDirectory'],
            relative_base=self.game_folder
        )
        self.fonts_folder = make_absolute_path(
            game_info['Paths']['FontsDirectory'],
            relative_base=self.game_folder
        )
        self.frame_elements_folder = make_absolute_path(
            game_info['Paths']['FrameElementsDirectory'],
            relative_base=self.game_folder
        )
        self.symbols_folder = make_absolute_path(
            game_info['Paths']['SymbolsDirectory'],
            relative_base=self.game_folder
        )



