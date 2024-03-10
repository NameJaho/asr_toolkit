<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
1. Install ffmpeg
   
2. Donwload Pretrain Models.
   
   2.1 Downlaod Vocal Separation model [URV5](https://www.icloud.com.cn/iclouddrive/0bekRKDiJXboFhbfm3lM2fVbA#UVR5_Weights).


### Installation
1. Create independent Python Environment.
   ```sh    
    conda create -n asr_toolkit python=3.9
    conda activate asr_toolkit
   ```
2. Clone the repo
   ```sh
   git clone git@github.com:Jeru2023/asr_toolkit.git
   ```
3. Install packages
   ```sh
   install -r requirements.txt
   ```

## Vocal Separation
人声伴奏分离批量处理， 使用UVR5模型。 <br>

模型分为三类： <br>
<li>1. 保留人声：不带和声的音频选这个，对主人声保留比HP5更好。内置HP2和HP3两个模型，HP3可能轻微漏伴奏但对主人声保留比HP2稍微好一丁点； </li>
<li>2. 仅保留主人声：带和声的音频选这个，对主人声可能有削弱。内置HP5一个模型； </li>
<li>3. 去混响、去延迟模型（by FoxJoy）：</li>
   (1)MDX-Net(onnx_dereverb):对于双通道混响是最好的选择，不能去除单通道混响；<br>
   (234)DeEcho:去除延迟效果。Aggressive比Normal去除得更彻底，DeReverb额外去除混响，可去除单声道混响，但是对高频重的板式混响去不干净。<br><br>

附：<br>
1. DeEcho-DeReverb模型的耗时是另外2个DeEcho模型的接近2倍；<br>
2. MDX-Net-Dereverb模型挺慢的；<br>
3. 个人推荐的最干净的配置是先MDX-Net再DeEcho-Aggressive。<br>
                    
