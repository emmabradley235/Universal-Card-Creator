from typing import Dict
from pathlib import Path

from path_utils import make_absolute_path



class TextProcessingConfig:
    def __init__(self, config: Dict):
        self.symbol_start_flag = config['SymbolFlags']['Start']
        self.symbol_end_flag = config['SymbolFlags']['End']

        self.reminder_start_flag = config['ReminderTextFlags']['Start']
        self.reminder_end_flag = config['ReminderTextFlags']['End']
        self.italicize_reminder = config['ReminderTextFlags']['ItalicizeReminder']
        self.bold_reminder = config['ReminderTextFlags']['BoldReminder']
        self.reminder_color = config['ReminderTextFlags']['ReminderColor']

        self.toggle_italics_flag = config['FormatFlags']['ToggleItalics']
        self.toggle_bold_flag = config['FormatFlags']['ToggleBold']
        self.endline_flag = config['FormatFlags']['Endline']
        self.paragraph_flag = config['FormatFlags']['Paragraph']

        self.cardname_symbol = config['ReplaceWithCardname']

        self.font_name_flag_component = config['FontModFlags']['SetFontName']
        self.font_color_flag_component = config['FontModFlags']['SetFontColor']

        self.text_replacements = config['TextReplacements']

class FontSetConfig:
    def __init__(self, font_name, font_paths, font_folder_path: Path):
        self.name = font_name

        self.primary_font: Path = make_absolute_path(font_paths.get('Primary'), font_folder_path)
        self.italic_font: Path = make_absolute_path(font_paths.get('Italic'), font_folder_path)
        self.bold_font: Path = make_absolute_path(font_paths.get('Bold'), font_folder_path)
        self.italic_bold_font: Path = make_absolute_path(font_paths.get('Italic-Bold'), font_folder_path)
