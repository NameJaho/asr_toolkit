import json
import os

from funasr import AutoModel
from loguru import logger

from tools.utils import get_root_path


class FunAsr:
    def __init__(self):
        self.model = AutoModel(model="paraformer-zh", vad_model="fsmn-vad", punc_model="ct-punc-c",
                               spk_model="cam++",
                               )
        self.root_path = get_root_path()
        self.asr_path = os.path.join(self.root_path, "output", "asr")

    def asr(self, input_path, batch_size_s=300, hotword='魔搭'):
        # 如果需跑新的音频文件，取消注释
        # res = self.model.generate(input=input_path,
        #                           batch_size_s=batch_size_s,
        #                           hotword=hotword)

        # 测试用 demo文件为刘先生访谈
        with open(self.root_path + '/data/demo.json', 'r', encoding='utf8') as f:
            res = json.load(f)

        # 结果保存到 output/asr/output.json
        self.parse_content(res)

    @staticmethod
    def format_seconds(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{int(minutes)}分{int(seconds)}秒"

    def parse_content(self, data):
        ls = []
        for sentence in data[0]['sentence_info']:
            dic = dict()
            dic['user'] = f"user{sentence['spk']}"
            dic['text'] = sentence['text']
            dic['time'] = self.format_seconds(int(sentence['start']) / 1000) + '-' + self.format_seconds(
                int(sentence['end']) / 1000)
            ls.append(dic)
        merge = self.merge_user_texts(ls)
        self.save(merge)

    @staticmethod
    def count_question_marks(merged_list):
        """
            统计每个用户的问号数量，问号多的为主持人，但不一定准确
        """
        question_counts = {'user0': 0, 'user1': 0}
        role = {'user0': '', 'user1': ''}
        for entry in merged_list:
            question_counts[entry['user']] += entry['text'].count('？')
        if question_counts['user0'] > question_counts['user1']:
            role['user0'] = '主持人'
            role['user1'] = '嘉宾'
        else:
            role['user0'] = '嘉宾'
            role['user1'] = '主持人'
        logger.debug(f'question_counts: {question_counts}')
        logger.debug(f'role: {role}')
        return role

    def save(self, merge):
        # role = self.count_question_marks(merge) # 不准

        if not os.path.exists(self.asr_path):
            os.makedirs(self.asr_path)
        with open(f'{self.asr_path}/output.json', 'w+', encoding='utf8') as f:
            for item in merge:
                # nick_name = role[item["user"]]
                nick_name = item["user"]
                f.write(f'{nick_name}   {item["time"]}\n{item["text"]}\n\n')

    @staticmethod
    def merge_user_texts(ls):
        merged = []
        current_user = None
        current_text = ""
        start_time = ""
        end_time = ""

        for entry in ls:
            if entry['user'] == current_user:
                # Concatenate the text
                current_text += entry['text']
                # Update the end time
                end_time = entry['time'].split('-')[1]
            else:
                if current_user is not None:
                    # Save the previous user's combined entry
                    merged.append({'user': current_user, 'text': current_text, 'time': f'{start_time}-{end_time}'})
                # Reset for the new user
                current_user = entry['user']
                current_text = entry['text']
                start_time, end_time = entry['time'].split('-')

        # Add the last user's entry if not added
        if current_text:
            merged.append({'user': current_user, 'text': current_text, 'time': f'{start_time}-{end_time}'})

        return merged


if __name__ == '__main__':
    fun_asr = FunAsr()
    res = fun_asr.asr('../data/audios/1.wav')
