import yaml
from pathlib import Path
from PIL import Image, ImageTk
from pydantic.v1.utils import deep_update

from path_management import GamePaths


class ResourceManager:
    def __init__(self, game_dir: str):
        self._given_game_directory = game_dir
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
            self.text_processing_config = deep_update(text_processing_defaults, yaml.safe_load(file))
            self.symbol_flag_start = self.text_processing_config['SymbolFlags']['Start']
            self.symbol_flag_end = self.text_processing_config['SymbolFlags']['End']
            self.reminder_text_start = self.text_processing_config['ReminderTextFlags']['Start']
            self.reminder_text_end = self.text_processing_config['ReminderTextFlags']['End']



if __name__ == "__main__":
    res = ResourceManager("Mechpoint")
    print(res.text_processing_config)