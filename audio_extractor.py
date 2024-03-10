import subprocess


def extract_audio(video_file, output_file):
    """
    从视频文件中提取音频。

    Args:
        video_file (str): 要提取音频的视频文件路径。
        output_file (str): 要保存提取的音频文件路径。
    """

    # 调用 ffmpeg 命令
    subprocess.call(['ffmpeg', '-i', video_file, '-vn', output_file])