import re

from tools.utils import *
from module.uvr5.mdxnet import MDXNetDereverb
from module.uvr5.vr import AudioPre, AudioPreDeEcho
import ffmpeg
import traceback
from tools.device_selector import *


# DeEcho-Aggressive by default
class VocalSeparator:
    def __init__(self):
        self.root_path = get_root_path()
        self.weight_uvr5_root = os.path.join(self.root_path, "models/uvr5_weights")
        # self.input_path = os.path.join(self.root_path, "output", "audios")
        self.vocals_path = os.path.join(self.root_path, "output", "vocals")
        self.background_path = os.path.join(self.root_path, "output", "background")
        self.reformat_path = os.path.join(self.root_path, "output", "reformat")
        self.vocal_name = ''
        self.background_name = ''
        # self.model_name = "VR-DeEchoAggressive"
        self.model_name = "HP2_all_vocals"
        self.device = get_infer_device()
        self.is_half = is_half(self.device)

    def uvr(self, file_path, agg=15, output_format="wav"):
        """
            file_path: absolute path of the audio file
        """
        # agg: 人声提取激进程度, 0-20
        # output_format: ["wav", "flac", "mp3", "m4a"]
        logs = []
        model_name = self.model_name
        # file_paths = get_file_paths(self.input_path)

        if not os.path.exists(self.vocals_path):
            os.makedirs(self.vocals_path)
        if not os.path.exists(self.background_path):
            os.makedirs(self.background_path)

        if not os.path.exists(self.reformat_path):
            os.mkdir(self.reformat_path)

        try:
            is_hp3 = "HP3" in model_name
            if model_name == "onnx_dereverb_By_FoxJoy":
                pre_fun = MDXNetDereverb(15)
            else:
                func = AudioPre if "DeEcho" not in model_name else AudioPreDeEcho
                pre_fun = func(
                    agg=int(agg),
                    model_path=os.path.join(self.weight_uvr5_root, model_name + ".pth"),
                    device=self.device,
                    is_half=self.is_half,
                )

            filename = re.findall('.*/(.*?).wav', file_path)[0]
            output_path = self.root_path + f'/output/vocals/vocal_{filename}.wav'
            self.vocal_name = f'vocal_{filename}.wav_{agg}.wav'
            self.background_name = f'instrument_{filename}.wav_{agg}.wav'
            logger.info(output_path)
            reformat_required = True
            done = False

            # if vocal file already exists, skip
            if os.path.exists(output_path):
                logger.debug(f'[{filename}] => output file exists')
                return

            try:
                info = ffmpeg.probe(file_path, cmd="ffprobe")
                if (
                        info["streams"][0]["channels"] == 2
                        and info["streams"][0]["sample_rate"] == "44100"
                ):
                    reformat_required = False
                    pre_fun._path_audio_(
                        file_path, self.background_path, self.vocals_path, output_format, is_hp3
                    )
                    done = True
            except:
                reformat_required = True
                logger.debug(traceback.print_exc())
            if reformat_required:
                tmp_path = "%s/%s" % (
                    self.reformat_path,
                    os.path.basename(file_path),
                )

                cmd = "ffmpeg -i %s -vn -acodec pcm_s16le -ac 2 -ar 44100 %s -y" % (file_path, tmp_path)
                os.system(cmd)

                file_path = tmp_path
            try:
                if not done:
                    pre_fun._path_audio_(
                        file_path, self.background_path, self.vocals_path, output_format, is_hp3
                    )
                logs.append("%s->Success" % (os.path.basename(file_path)))
                logger.debug("\n".join(logs))
            except:
                logger.debug(traceback.print_exc())

                logs.append("%s->%s" % (os.path.basename(file_path), traceback.format_exc()))
                # logger.debug("\n".join(logs))

        except:
            logs.append(traceback.format_exc())
            logger.debug("\n".join(logs))
        finally:
            try:
                if model_name == "onnx_dereverb_By_FoxJoy":
                    del pre_fun.pred.model
                    del pre_fun.pred.model_
                else:
                    del pre_fun.model
                    del pre_fun
            except:
                traceback.print_exc()
            print("clean_empty_cache")
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        logger.debug("\n".join(logs))
