import audio_extractor
from my_utils import *
from loguru import logger
import os

OUTPUT_AUDIOS_FOLDER = 'output/audios'


class Executor:
    def __init__(self):
        pass

    @staticmethod
    def convert_videos(input_path='data'):
        input_paths = get_file_paths(input_path)

        if not os.path.exists(OUTPUT_AUDIOS_FOLDER):
            os.makedirs(OUTPUT_AUDIOS_FOLDER)

        logger.info('Start to convert videos to audios...')
        for input_path in input_paths:
            input_file_name = get_file_name(input_path)
            output_file_name = f'{input_file_name}.wav'
            output_path = os.path.join(OUTPUT_AUDIOS_FOLDER, output_file_name)

            if not os.path.exists(output_path):
                audio_extractor.extract_audio(input_path, output_path)


if __name__ == '__main__':
    executor = Executor()
    executor.convert_videos()
