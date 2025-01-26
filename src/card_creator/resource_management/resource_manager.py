from pathlib import Path

import yaml
from pydantic.v1.utils import deep_update

from config_wrappers import TextProcessingConfig, FontSetConfig
from path_management import GamePaths


class ResourceManager:
    def __init__(self, game_dir: str):
        self._given_game_directory = game_dir
        self.card_layouts
        self.update_configurations()

    def update_configurations(self):
        self.game_paths = GamePaths(self._given_game_directory)

        with open(self.game_paths.game_info_config, 'r') as file:
            game_info = yaml.safe_load(file)
            self.game_name = game_info['GameName']
            self.card_resolution = game_info['CardOutputResolution']
            self.card_display_resolution = game_info['CardDisplayResolution']

        with open(Path('config\\card_creator\\text_processing_defaults.yaml').absolute(), 'r') as file:
            text_processing_defaults = yaml.safe_load(file)
        with open(self.game_paths.text_process_config, 'r') as file:
            self.text_processing_config = TextProcessingConfig(
                deep_update(text_processing_defaults, yaml.safe_load(file))
            )

        with open(self.game_paths.card_field_config, 'r') as file:
            self.card_ui_fields = yaml.safe_load(file)

        with open(self.game_paths.font_configs, 'r') as file:
            font_configs: dict = yaml.safe_load(file)
            self.font_sets = {
                font_name: FontSetConfig(font_name, font_paths, self.game_paths.fonts_folder)
                for font_name, font_paths in font_configs['Fonts'].items()
            }
            self.default_font = self.font_sets.get(
                font_configs['Default'],  # Attempt to get the default font, but if its not valid for some reason
                self.font_sets[self.font_sets.keys()[0]]  # Get the first listed font
            )


if __name__ == "__main__":
    res = ResourceManager("Mechpoint")
    print(res.font_sets)
