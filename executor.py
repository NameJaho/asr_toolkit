from tools import audio_extractor
from module.uvr5_model import VocalSeparator
from tools.my_utils import *
from loguru import logger
import os

OUTPUT_AUDIOS_FOLDER = 'output/audios'


class Executor:
    def __init__(self):
        self.vocal_separator = VocalSeparator()

    @staticmethod
    def convert_videos(input_path='data'):
        input_paths = get_file_paths(input_path)

        if not os.path.exists(OUTPUT_AUDIOS_FOLDER):
            os.makedirs(OUTPUT_AUDIOS_FOLDER)

        logger.info('Videos to audios conversion started...')
        for input_path in input_paths:
            input_file_name = get_file_name(input_path)
            output_file_name = f'{input_file_name}.wav'
            output_file_path = os.path.join(OUTPUT_AUDIOS_FOLDER, output_file_name)

            if not os.path.exists(output_file_path):
                audio_extractor.extract_audio(input_path, output_file_path)
        logger.info('Videos to audios conversion completed...')

    def separate_vocals(self):
        logger.info('Vocals separation started...')
        self.vocal_separator.uvr()
        logger.info('Vocals separation completed...')


if __name__ == '__main__':
    executor = Executor()
    executor.convert_videos()
    executor.separate_vocals()
