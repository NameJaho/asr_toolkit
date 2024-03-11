from tools import audio_extractor
from module.uvr5_model import VocalSeparator
from module.asr_model import ASRModel
from tools.my_utils import *
from loguru import logger
from tools.my_utils import timer
import os

INPUT_VIDEOS_FOLDER = 'data'
OUTPUT_AUDIOS_FOLDER = 'output/audios'
OUTPUT_TEXTS_FOLDER = 'output/texts'


class Executor:
    def __init__(self):
        self.vocal_separator = VocalSeparator()
        self.asr_model = ASRModel()

    @staticmethod
    @timer
    def convert_videos(input_folder=INPUT_VIDEOS_FOLDER):
        input_paths = get_file_paths(input_folder)

        if not os.path.exists(OUTPUT_AUDIOS_FOLDER):
            os.makedirs(OUTPUT_AUDIOS_FOLDER)

        logger.info('Videos to audios conversion started...')
        for input_folder in input_paths:
            input_file_name = get_file_name(input_folder)
            output_file_name = f'{input_file_name}.wav'
            output_file_path = os.path.join(OUTPUT_AUDIOS_FOLDER, output_file_name)

            if not os.path.exists(output_file_path):
                audio_extractor.extract_audio(input_folder, output_file_path)
        logger.info('Videos to audios conversion completed...')

    @timer
    def separate_vocals(self):
        logger.info('Vocals separation started...')
        self.vocal_separator.uvr()
        logger.info('Vocals separation completed...')

    @timer
    def asr(self, input_folder=OUTPUT_AUDIOS_FOLDER, output_folder=OUTPUT_TEXTS_FOLDER):
        input_paths = get_file_paths(input_folder)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        logger.info('ASR started...')

        for input_path in input_paths:
            input_file_name = get_file_name(input_path)
            output_file_name = f'{input_file_name}.txt'
            output_file_path = os.path.join(output_folder, output_file_name)

            if not os.path.exists(output_file_path):
                text = self.asr_model.inference(input_path)
                write_text_to_file(text, output_file_path)
        logger.info('ASR completed...')


if __name__ == '__main__':
    executor = Executor()
    executor.convert_videos()
    # executor.separate_vocals()
    executor.asr()
