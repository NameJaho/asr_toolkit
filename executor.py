from tools import audio_extractor
from module.uvr5_model import VocalSeparator
from module.asr_model import ASRModel
from tools.my_utils import *
from loguru import logger
import os

OUTPUT_AUDIOS_FOLDER = 'output/audios'
OUTPUT_TEXTS_FOLDER = 'output/texts'


class Executor:
    def __init__(self):
        self.vocal_separator = VocalSeparator()
        self.asr_model = ASRModel()

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

    def asr(self):
        input_paths = get_file_paths(OUTPUT_AUDIOS_FOLDER)

        if not os.path.exists(OUTPUT_TEXTS_FOLDER):
            os.makedirs(OUTPUT_TEXTS_FOLDER)

        logger.info('ASR started...')

        for input_path in input_paths:
            input_file_name = get_file_name(input_path)
            output_file_name = f'{input_file_name}.txt'
            output_file_path = os.path.join(OUTPUT_TEXTS_FOLDER, output_file_name)

            if not os.path.exists(output_file_path):
                text = self.asr_model.inference(input_path)
                write_text_to_file(text, output_file_path)
        logger.info('ASR completed...')


if __name__ == '__main__':
    executor = Executor()
    executor.convert_videos()
    executor.separate_vocals()
    executor.asr()
