from pydantic import BaseModel, Field, validator
from typing import Literal, Any


# from exception.handlers import CategoryError


# 请求类型
# class BaseRequest(BaseModel):
#     @validator('category', check_fields=False)
#     def check_category_contains_colon(cls, v):
#         if ':' not in v:
#             raise CategoryError(400, '请输入完整的品类树(eg. 护肤:面部护理:洁面)')
#         return v


class NormalizeRequest(BaseModel):
    category: str = Field(..., description="用户输入的品类名", example="护肤")


class MainRequest(BaseModel):
    video_url: str = Field(..., description="视频链接",
                           example="https://sns-video-al.xhscdn.com/01e2b407823db72701037003818f3e0e32_258.mp4")
    video_id: str = Field(..., description="视频的唯一id", example="01e2b407823db72701037003818f3e0e32_258")
    video_tag_list: str = Field(..., description="视频标签", example='四宝茶;元气四宝;元气四宝汤;元气四宝茶')
    title: str = Field(..., description="视频标题", example="这个蜜桃味唇油可爱到我心里了 有被惊喜到")
    content: str = Field(..., description="视频文字内容",
                         example="唇油;唇蜜;变色唇膏;水光唇釉;美妆好物;apieu;apieu唇油")
    data: list = Field(..., description="视频数据")


class BatchRequest(BaseModel):
    data: list = Field(..., description="视频数据", examples=[[
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/red4?sign=e5df932d61d3e26732d589903c1d4206&t=65fb06d4',
    'video_id': '5817756a805d890bd7847eb5',
    'title': '直男程序员勇闯上海时装周',
    'video_tag_list': '',
    'content': '#上海时装周[话题]# 男神天团神游上海时装周 @ThreeKniFe @姚X旭 @JasonCao @rogerluo'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/annie_pen',
    'video_id': '58178143805d890bd7847ecb',
    'title': '据说升级新版4.11有彩蛋，原来是终于可以看Video笔记了',
    'video_tag_list': '',
    'content': '第111条笔记，第1条视频笔记！\n之前响应了生活薯的号召，悄悄投稿了小视频[喜欢]\n人生第一个小视频哦，创作于伦敦airbnb的小屋里，inspired by脸书上朋友的转发，感谢出镜的@吴小鳍儿 .\n发现现在手机端视频编辑加滤镜加字幕都好方便了～\n想着下次再玩玩什么主题的...'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/3821ed5d99ac04bdcc375417bbce5c5fba864e7d_v1_ln',
    'video_id': '581838a5b318f90d17ad3d69',
    'title': '万圣节美食恶搞教程，手残党和懒癌的福音',
    'video_tag_list': '',
    'content': 'Happy Halloween~ 小红薯们都要到糖果了嘛？生活薯来教大家点实用技能！几个简单的小创意~用最简单的零食，制作万圣节美食！教你在一群神经病中，疯得出！类！拔！萃！\n1 奥利奥蝙蝠：\n食材：奥利奥饼干、眼睛糖果\n做法：1）扭一扭、2）将饼干对半分开做翅膀，3）贴上眼睛。齐活！奏是这么简单！\n2 蠢萌魔鬼蛋：\n食材：鸡蛋、番茄酱、刻刀\n做法：看图作画........233333\n3 怪兽牙齿饼干：\n食材：曲奇饼、棉花糖、番茄酱、花生坚果\n做法：1）曲奇饼上涂抹番茄酱；2）在其中一片，用棉花糖排列摆出牙齿造型；3）盖上上层，用花生坚果拼成邪恶牙齿。大功告成！\n4 Pocky 木乃伊：\n食材：pocky、眼睛糖果、蛋黄酱、湿巾纸（尴尬.....只是为了摆盘.....如果要吃可以换成可以拉丝的芝士，然后加热一哈）\n步骤：1）白色“绷带”缠绕棒棒上，2）用蛋黄酱充当胶水，3）贴上眼睛。done！！\n5血渍创可贴\n食材：方形饼干（提示：稍软的较好）、芝士、番茄酱\n做法：1）掰开饼干呈长方形、2）粘上小片方形芝士、3）涂抹番茄酱做血.....搞定！\n6血腥魔鬼饮料\n食材： 龙眼、葡萄汁（or 苹果汁，总之看起来很像动脉出血赶脚的果汁，嘿嘿）\n做法：1）龙眼吃掉一半，露出邪恶的黑色的核，2）扔到果汁中！恶魔眼睛饮料上线！\n7棒棒糖小鬼：\n食材：棒棒糖、湿纸巾、眼睛糖果、蛋黄酱\n做法：1）用湿纸巾包裹住棒棒糖，（参考晴天娃娃制作方法），2）将眼睛用蛋黄酱粘贴住！哒哒\n特邀嘉宾：cos小黄人的...萝卜头小鬼们~\n是不是都超级简单？快来试试做一做吧！！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/58184f12d1d3b9145adbccd2?sign=684a46acede52d6ced1c5d8613160c25&t=65fb06d4',
    'video_id': '58184f12d1d3b9145adbccd2',
    'title': '今天宝宝要露一手，给你们看看一颗鸡蛋能有多萌~',
    'video_tag_list': '',
    'content': '作为一枚宝宝，不仅要吃得营养美味，更喜欢食物萌萌又可爱~[色色R][色色R][色色R]\n前几天@生活薯 约我进行#鸡蛋大改造，今天宝宝就来交个作业！[吧唧R][吧唧R]只需要简单几步，就能让圆滚滚的鸡蛋变身小熊、小兔、小刺猬~要说宝宝的手也是挺巧的嘛~[赞R][赞R]\n各位小红薯麻麻要不要一起试试看？一点小心思，就能让宝宝的食物变得更有趣哦~或者各位小红薯宝妈有没有什么独家食物改造法？记得发笔记@薯宝宝 告诉我哦~新版本还支持视频功能~\n如果想投稿，只要发送邮件到shuduizhang@xiaohongshu.com ，邮件标题记得写:薯宝宝收 哦~好学宝宝好期待学到更多呀！！[色色R][色色R][色色R][色色R]\nPS:@生活薯，快来应战#鸡蛋改造大法！[鄙视R][鄙视R][鄙视R]'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/58184f12d1d3b9145adbccd2?sign=684a46acede52d6ced1c5d8613160c25&t=65fb06d4',
    'video_id': '5819a7f236b2a8404a541592',
    'title': '鸡蛋变魔法！一颗鸡蛋肿么可以这么萌！',
    'video_tag_list': '',
    'content': '身为人父人母的薯粑粑麻麻们一定知道，为了让自己的娃吃口饭，是有多不容易。\n但是，如果能把食物做的萌萌哒，比如做成可爱的小动物～相信宝宝们一定会很喜欢！\n前几天，身为@薯宝宝 保姆的本薯，用几个鸡蛋，做成了小兔几、小刺猬、小熊…薯宝宝别提有多开心了！只要用心去发现，很多普通的食物都可以变得很有趣哦！\n你有可以让食物变魔法的小妙招嘛？记得发笔记告诉我们哦～还有还有，再有一阵子视频功能就要上线啦！队长等着看你们奇思妙想的小视频！多学几招用来哄薯宝宝。\n如果你等不急，现在就想发小视频，欢迎将视频发送至：shuduizhang@xiaohongshu.com 的邮箱中（MP4格式，3分钟以内），记得标注小红书ID和你的联系方式哦。队长在红薯地等你哈~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/581b414ff64b3d4f9b17f2de_4_compress_L1',
    'video_id': '581b414ff64b3d4f9b17f2de',
    'title': '健身它带给我的是一种个人的自律，一种对生活的感知',
    'video_tag_list': '',
    'content': '好开心可以分享视频啦，这是我上半年的一个健身视频记录📝\n对于我来说维持一个好的身材形态是一辈子的事情，所以我最看重的是生活方式的改变和坚持，无论饮食还是运动方式，都需要找到自己最适合的。别人的方法未必在你身上管用，就算管用，你坚持不下来也是没有任何意义的，自己不体会过永远不知道这其中的过程。\n健身它带给我的是一种个人的自律，一种对生活的感知，当拥有的这种自律，你的身体会变得越来越好，思路也会变得清晰，而且你给周边的人能够带来很多正能量和阳光的感觉。\n小红书更新版可以发视频了，率先体验一下。也想发视频的同学可以跟薯队长投稿：shuduizhang@xiaohongshu.com\n太开心了，接下来就可以跟大家分享更多“动”态啦✌️'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/581b6fc7805d893b801e53fe?sign=6e2bb212b3801753ab6176e8a6b4ae84&t=65fb06d4',
    'video_id': '581b6fc7805d893b801e53fe',
    'title': '迪拜跳伞攻略及视频',
    'video_tag_list': '',
    'content': '小红书终于可以发视频啦～迪拜跳伞的视频，先睹为快吧！！\n⚪️花费：1,999迪拉姆\n⚪️提醒：6-8月休息，其他月份请提前1-2月预定。\n⚪️预订网址：http://www.skydivedubai.ae/\n一般情况下新手都是有一名教练陪同（Tandem），Skydive Dubai的跳伞价格包含一位跟拍，跳伞结束后会以u盘的形式附送。\n⚪️预订的过程共分三步：\n1.点击Tandem后选择跳伞日期，白色日期为可选\n2.选择跳伞时间和人数，每个时间段只有10个名额，所以尽早预订\n3.填写个人基本信息姓名、邮箱、生日等并支付999AED订金（不需要任何护照和ID信息）\n预订完成后会收到确认邮件可以打印出来带到reception报到~\n从春意盎然的英国到迪拜，LZ刚出机场的那一刻是极度崩溃的，还好室内的温度特别舒服，怪不得迪拜的大街上基本上看不到人影\n先把行李放置后吃完早餐，离报到还有一段时间，由于之前选酒店特意选在Skydive营地附近，于是打算悠哉的步行过去，可是LZ错了...15分钟的路程足足走了40分钟，所以还是建议大家打车前往给自己预留足够的体力~\n⚪️跳伞前准备及注意事项：\n1.到了reception之后左手可以看到报到处，把之前打印出来的确认表交给工作人员测量体重合格即可~工作人员会给你一叠厚厚的文件签名，最后一条是人身意外发生，责任自负。签名完成后把文件交还即可交余下的1,000AED(刷卡现金都可)。\n2.交费完成后就是等待点名，这里特别提醒，因为每个时间段十个人，教练也需要休息，一般跳伞点名的时间比预约的时间晚2小时左右，没有必要到太早不然等的太焦灼。\n3.准备时间大可放松但注意随身的饰品一定要摘掉！！！LZ没有摘耳钉结果不知什么时候飞丢一只下来后一个中国女孩告诉我得亏耳钉掉了比较坏的情况耳朵会被扯破想想也是后怕...\n4.等待区前的大屏幕上会显示跳伞人员的分组和对应教练的名字，每架飞机三人跳伞，轮到该组的时候教练会叫你的名字（教练叫中文名的时候发音很奇怪，所以自己要多留心~）。\n5. 教练会简单的讲一些注意事项，同时也有中文动作解说牌简直贴心，之后跟拍的工作人员会来做一段简单的interview。\n然后就是跟随教练上飞机啦~~~飞到13,000英尺大概需要15分钟左右，期间教练会一直跟你讲话帮你放松。Skydibe Dubai并没有头盔和跳伞服，爱美的盆友也可以提前准备好美美的比较运动宽松的衣服。\n被教练推到舱门口的时候教练把脸板正让我向上看，还没给喘气的时间就直接被他推着跳了来...\n接着整个人都在风中凌乱了，教练会一直帮我调整脸的位置去对准相机，但宝宝真的是笑不出..\n自由落地大概5分钟左右，降落伞打开，整个人也淡定了许多，这时候教练会让你看看周围的景色，棕榈岛，Atlantis，帆船酒店尽收眼底，近处的繁华和远处的荒芜对比鲜明，迪拜真的是一半沙漠一半天堂。\n落地前教练会再次提醒你双腿抬起\n落地后等半小时左右就可以拿到u盘，可以选照片付费打印出来~\n下一站塞班跳伞见！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/581b7279805d895db535107a_compress_L1',
    'video_id': '581b7279805d895db535107a',
    'title': '深秋的温暖橘色',
    'video_tag_list': '',
    'content': '这次来首尔很不巧赶上“韩”流，早上最低气温有过零度哈哈！虽然天气是冷了一点，但是街边的叶子都成了黄色橘色，真的是非常美丽的金秋色！\n想到我有带一件橘色的大衣和这里的金秋的颜色很搭配，于是穿来和叶子合影啦！\n因为大衣颜色是橘色很出挑，但也很衬肤色的一个颜色。在款式上就非常的简洁，这种设计在搭配上会有更多种的可能性哈！大衣是长款哒，可以把自己裹在里面哟。\n包包是celine的mini box，短靴是在韩国买的哈！\n虽然秋天刚来又马上要走啦，希望大家都能拥有一个美好的金秋哟！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/581c04e2f64b3d763a02ed02_3',
    'video_id': '581c04e2f64b3d763a02ed02',
    'title': '重操旧业练个琴——古筝',
    'video_tag_list': '',
    'content': '看到笔记出了视频功能 一时兴起就发一段之前夏天在家录的弹古筝小视频啦 哈哈哈（那时候发的ins只能15秒[委屈]\n妈妈说我幼儿园的时候看了各种琴就是想学古筝 小时候学起来还特别认真 一回家就想练琴那种哈哈！从幼儿园中班开始学的古筝 一直学到初二考出了古筝八级。之后因为中考原因就弃琴了 现在想想真是有点遗憾～因为坚持下去再过两年就能考十级了诶！\n视频里的曲子是古筝曲《战台风》考七级的时候弹奏的 也是我最喜欢的一首古筝曲。此曲中的扫摇四点、密摇、扣摇、刮奏等来制造台风效果 都使古筝演奏的技巧进入了新高度！可惜短短15秒只能录到个开头～改次好好录个完整版哈哈\n感觉现在都是学钢琴阿 小提琴阿的比较多～作为中国的传统民族乐器 不知道有木有小红薯也喜欢古筝的[喜欢]'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/1_581c20e5d2c8a5219802d5a4_compress_L1',
    'video_id': '581c20e5d2c8a5219802d5a4',
    'title': '瑜伽如做人，“稳”为先',
    'video_tag_list': '',
    'content': '视频动态分享第二篇✌️\n聪明的肌肉定义是：灵活、拉伸、敏感 、筋膜放松\n所以忠于通过器械增肌塑形的男士女士更需要结合瑜伽对身体进行拉伸舒缓，从而提升身体的柔韧性，特别是长期僵坐在办公桌前导致的肩颈酸痛的白领们。\n瑜伽正是极佳的锻炼方法，在舒展筋骨的同时，更能消除心理上的压力，当然别以为瑜伽是女人们的专属，其实专注于练器械的男士们比谁都更需要瑜伽，很多男士常年器械练肩会导致弓背的状态，常年累月之后对于肩关节及脊柱的压力是非常大的，他们已经很难将手臂背到身后做拉伸，瑜伽正式在为你的关节减压之余，也能让你降低你在运动中受伤的风险。\n喜爱做瑜伽的女生恭喜你，你已经有了非常好的身形基础，如果你也可以配合一些器械，那么你的体重你的身形都会有很大改变哟，久而久之腰围小了，马甲线出现了，身体挺拔了，臀型也原来越上翘了，身材的比例就这样潜移默化的产生的微妙的变化。\n小红书更新版可以发视频了，率先体验一下。也想发视频的同学可以跟薯队长投稿：shuduizhang@xiaohongshu.com'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/f83687fa36c013e447896d20256878da2b4dd717_r_ln',
    'video_id': '581c7294d5945f6af6dd2410',
    'title': '🔛视频之杨大妈猜猜我的化妆品夺钱',
    'video_tag_list': '',
    'content': '吼吼吼！终于可以发视频啦！\n这段视频是之前录的啦，当时发不了小红书好桑心～现在终于可以发来给大家乐乐～\n（已经看过的…就…请一笑而过咯…🌚\n反正杨大妈觉得我的化妆品都是800块…\n除了他帮我买的眼霜价格记得可清楚了…\n（视频编辑的可用心 没啥好说的了….\n诶 杨大妈已经答应我帮我录个“南票帮我化妆”系列…嗯…下次视频债见！\n小红书终于有视频功能啦！赶紧投稿给队长测试一下。\n大家如果有3分钟内的短视频，也可以投稿给队长邮箱哦，email：shuduizhang@xiaohongshu.com'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/01e248068a20323501837003800478b51c_259.mp4',
    'video_id': '581d9b4040c79458be14842a',
    'title': '💪【有视频】瘦肚子/腰腹核心训练：来甩个战斗绳吧！',
    'video_tag_list': '',
    'content': '我是一个谁见到都会觉得是矮瘦子的人，但是也是一致公认吃饭很快又很多。所以只能靠花额外的时间去运动，遇到一个好的健身房眼睛都会发光。\n看到一个没见过没玩过的器材，觉得有意思当下就会下单买到家来，然鹅，战斗绳这东西家里客厅没有100平米明显就没办法舒展开，而且吓到了家里的小猫咪们可如何是好。\n所以其实我很少玩这个啦。\nps：我自己觉得动作不够标准，但是也不是超级不标准。\n需要注意的几点1，收紧核心，2，膝盖微曲不要超过脚尖3，手臂放松，通过肩膀背部带动手臂发力，避免过多代偿，4，手臂关节微曲紧绷。以一分钟为单位 重复5-6组 间隔休息1分钟，不过量力而行 1分钟对于大多数软妹是很难做到的啊。\n瘦肚子这个有用。看到健身房的大绳不知道怎么用可以看这个视频哟'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/4_581ddc72f64b3d2c5b1a8d68_compress_L1',
    'video_id': '581ddc72f64b3d2c5b1a8d68',
    'title': '萌宝探班小红书',
    'video_tag_list': '',
    'content': '今天宝宝我有神秘小客人哦~\n我书超红的萌宝ET@ETandFATTY 前来探班，引发了办公室大骚动！！[萌萌哒R][萌萌哒R]宝宝我以后也要这么讨人喜欢才行呀！[色色R][色色R][色色R]\n在会客厅接见我书美女团，解密我书冰箱中的秘密，视察我书工作氛围......ET的精力真是让本宝宝也甘拜下风[哭惹R][哭惹R][哭惹R]\n先给大家来段小预告~#ET探访小红书#可会是个系列呢~至于本宝宝会不会出镜？嘿嘿嘿嘿你猜~[惊恐R][惊恐R][惊恐R]\n当然当然，也欢迎各位好奇的薯爸薯妈，带着宝宝一起来我书玩耍~宝宝本尊会在这里迎接你们哦~[害羞R][害羞R][害羞R]\n当然咯~如果你愿意发个视频或者长笔记，先让宝宝我认识一下你家薯宝，也很欢迎哦~只需发送邮件到shuduizhang@xiaohongshu.com，标题中记得标注#报告薯宝宝，就有机会体验我们最新开放的长笔记和视频功能啦~想要用更多形式记录和分享关于薯宝们的一切，各位薯爸薯妈这就行动起来吧~\n等你们哦比心❤❤❤'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/5_58203546faa052411d10257d',
    'video_id': '58203546faa052411d10257d',
    'title': '日常裸妆教程 No Makeup Makeup #妆容教程#',
    'video_tag_list': '',
    'content': '出门见人要化妆已经成了一种文化，但是我们也不可能天天花30-40分钟画浓妆，这样又麻烦又不亲民😄\n今天跟大家分享一款心机裸妆，既提气色又不会显得很夸张，最重要的是快！10分钟以内搞定哟😉\n废话不多说，开始撸！\n1⃣️Laura Mercier保湿妆前乳，适合我这种混干或干皮，可以增加底妆的服贴度\n2⃣️YSL超模粉底液，我这个是新版、个人觉得旧版更好用，光泽感强又保湿，新版的在我脸上几乎是亚光的，但是遮瑕和持久度相对于旧版提高了🤗个人觉得会更适合混合偏油肌肤哟\n3⃣️接下来拿MAC 224晕染刷蘸取MAC单色眼影Wedge修鼻影、再将其带到眼窝，打造立体感。因为是裸妆所以我就不画多余的眼影了😉\n4⃣️植村秀睫毛夹将睫毛夹翘，再用Kissme浓密卷翘防水睫毛膏刷睫毛，这样既自然的增大了眼睛、又能突出眼神👁👁\n5⃣️用Sigma F05修容刷蘸取NARS修容粉Laguna，刷在脸颊两侧、颧骨下方和额头发际线处，使脸型显得更加精致小巧\n6⃣️腮红和嘴唇👄我用了同一款产品：YSL Rouge Volupte Shine圆管唇膏5号，先用唇膏在两颊各点三个点、拿手指晕开，再均匀的涂抹在嘴唇上。这样做的目的一个是快，一个是腮红和唇色一样会使整个妆容更和谐哦😉\n妆容完成！你们学会了嘛～\n如果喜欢请关注我吧，以后还会有更多教程哦😘\n小红书终于有视频功能啦！赶紧投稿给队长测试一下。 大家如果有3分钟内的短视频，也可以投稿给队长邮箱哦，email：shuduizhang@xiaohongshu.com。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/480x268/vcodec/libx264/1_582035c9d5945f307d1fef65',
    'video_id': '582035c9d5945f307d1fef65',
    'title': '周杰伦《默》',
    'video_tag_list': '钢琴演奏',
    'content': '之前看好声音的时候很喜欢杰伦自弹自唱的《默》，有空就练了出来，家里的谱子基本上都是钢琴王子Richard Clayderman，周杰伦和石进的，钢琴王子Richard Clayderman，每年都会去听他的新年演奏会，第一次去看的时候才刚学琴没多久，到如今的我，心境不一样感触也不一样，就连只看了他一次演奏会的男朋友也说他弹琴时的投入和优雅，自己看得也陶醉了。\n#小红书才艺大赛[话题]##我的个人技[话题]##钢琴演奏[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/6_58206f8814de4117d2a26912',
    'video_id': '58206f8814de4117d2a26912',
    'title': '用心和宝宝在一起#薯宝宝##讲故事#',
    'video_tag_list': '',
    'content': '👏👏👏恭喜视频功能上线啦！赶快来参加 @薯宝宝\n🍀一直觉的陪伴是最长情的的表白，最投入的爱。but，要是全身心的高质量陪伴。所以旅行和读书，是我最喜欢和宝宝一起做的事，这样的时光最100%属于对方，不会被琐碎俗事打扰。🍀\n✔️这套《嘟噜嘟嘟》系列是友赠的书，整体非常打破被动的故事套路，书中的角色通过读书人和小朋友直接互动、当然也是读书人和宝贝最棒的亲子时光。\n👉废话不多说、看视频吧。\n📎plus短短的视频花了好几个小时剪辑，用的是小影，简直手都快抽经了，喜欢请点个赞哦。\n🤓博主无妆，无发型，轻拍。\n博主睡衣：SML boutique🇨🇳\n宝宝睡衣：法国小帆船 petit-bateau🇫🇷'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/7_58207672046fc5531e2ebafd',
    'video_id': '58207672046fc5531e2ebafd',
    'title': '我的瑜伽启蒙老师🙏—我滴老爹',
    'video_tag_list': '',
    'content': '这是一篇视频哦！请猛戳——\n楼主之前发了一篇我老爹的文\n结果那么多人点赞\n我的心情是很复杂的（悲喜交织啊啊啊啊啊\n估计我老爸练个瑜伽可能就要变网red了\n没错，我爸是我的瑜伽启蒙老师，也是我偶像哈哈哈哈哈\n🌧\n今天下班的时候上海突然下起雨\n心情很差很low很不开心\n然后到家我突发奇想就边脱鞋边和我爸说\n“你来两个倒立好伐，我想拍一下”\n我一直在等我爸回应我说“好”\n等了3秒钟没回复\n进了客厅就看见我爸已经把瑜伽垫铺好🙄🙄（呃呵呵呵呵\n🙈\n然后就有了以下的这个小视频哈哈哈\n1⃣️头倒立\n要点：两手和头部成为等边三角形\n2⃣️头肘倒立\n要点：手是保护头部的\n3⃣️手倒立\n要点：手臂一定要有力才能做这个动作\n🔴以上的这些动作，整个过程都要保持呼吸，鼻吸鼻呼，千万不能憋气哦！核心（腹部）一定要收住，千万千万不能塌腰，当然不仅是核心，手臂两腿都是要用力的，同时收住会阴～\n⚫️所有的倒立做好，不要立马站起来，会把脑部供血不足头晕哦。做个婴儿式放松一下～～\n如果觉得自己手臂力量不够可以做海豚式来锻炼两臂（动作可baidu一下）\n以上视频和文字喜欢的可以点赞也欢迎和我交流\n不喜勿喷\nNamaste🙏'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/2_5820a441783623799aa8735d',
    'video_id': '5820a441783623799aa8735d',
    'title': 'paragliding in Interlaken',
    'video_tag_list': '',
    'content': '分享在茵特拉肯玩滑翔伞的美好回忆\n去之前 看攻略的时候就看到因特拉肯有跳伞和滑翔伞 不过需要提前几天预订 抱着试试的心态 没想到滑翔伞当天就行啊～\n路边有很多店 可以直接报名的\n太开心了 虽然心里有点忐忑 其实跟着教练的指令就可以了\n毕竟我不是一个人嘛\n当我真的飞起来的时候 真的觉得太太太值得了\n远处就是少女峰 脚下也是各种美景\n相信我 失重感就两秒吧\n之后就可以享受各种真的是很放松的状态\n滑翔伞一次是170瑞郎\n飞行中的照片和视频是40瑞郎 果断买下来啦！\n飞行过程中 教练还会跟你聊聊天 给介绍介绍这是啥那是啥的\n总之非常值得  可惜逗留时间太短\n有生之年  还想去飞一次😊'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/2_5821beb8b46c5d0e371d7f11_compress_L1',
    'video_id': '5821beb8b46c5d0e371d7f11',
    'title': '上海时装周，小红书专访第一Pose女王Coco Rocha',
    'video_tag_list': '',
    'content': 'Coco Rocha作为第一Pose女王被人熟知，\n据说她能连续摆100个不同的pose，\n连表情也全都不一样\n这次时装周，小红书有个难得的机会\n和Coco做了一次专访，快来跟Coco打个招呼吧！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/1_58232cfbd2c8a57c786ab491',
    'video_id': '58232cfbd2c8a57c786ab491',
    'title': '假如世上只剩三样化妆品',
    'video_tag_list': '日常妆容打卡',
    'content': '事情是这样的\n因为我比较懒\n没什么都是不想化妆的\n但是上周不是出去玩了么\n居然见到旧同学了\n重点是她说要！合！照！\n.\n.\n天啊\n她肯定要发朋友圈的\n这样全班同学看了我的素颜都会觉得\n---我最近过得是不是不太好\n(幸运的话也许还会收到救助红包-，-）\n但素！\n时刻带着偶像包袱的我早已预料到这一切\n但是我用的都是小包\n不可能放下我的全套化妆品的\n于是\n我就拿了我三个小法宝出来\n平安保住了我的女神（jing）形象哈哈哈哈哈\n.\n.\n今颠我要把我的小法宝传授给大家\n😎\n然后跟大家分享一下视频中用到的产品测评哦！\nCharlotte\xa0tilbury哑光唇膏口红\n色号：sexy sienna\n🌟\n这个测评一定要放首位啊！！\n太太太喜欢这个口红了\n本来就很喜欢这个牌子的这个系列\n是我人森第一次有要all in冲动的口红\n本来已经入了一支walk of shame的已经爱到不行\n最近入的这个sexy sienna又让我对它的爱升华了\n连重度直男癌（觉得不化妆是最好看）的阿红看到我第一眼就问，\n你的口红是什么颜色?\n我说，很好看？\n他说：是的。\n虽然这个叫sexy sienna，但是完全不是那种\n妖艳贱货的sexy耶！\n简直就是girlish，\n是有点偏橘的奶油少女粉。\n这个是哑光的，但是我这种沙漠嘴皮都不怕拔干，\n也不显唇纹！\n天啊，简直就是完美~\n总结：\n显白！少女！\n而且因为是哑光的，质感会比较好，而且比较持久。\n----------❤️------------\nkate三色立体眉粉\n色号：EX-5 深棕色\n✌🏻️\n这个必须一生推\n太实用啦！\n可以当眉粉，眼影，鼻影，脸部阴影，发际线粉。\n首先这个眉粉是三色哒\n可以应合不同妆容进行调色\n然后里面自带刷子，非常方便\n也很好上色，我基本出门一整天都不需要补\n而且价格也很实惠\n一盒可以用超久了\n比眉笔耐用非常多\n现在没化妆出门基本都会带着哈哈哈\n放包里不碍地方。\n----------❤️-----------\nYSL/圣罗兰\xa0逆龄女神肌密精萃粉底液\n色号：BR20\n这个我是要吐槽的🌚\n我买的是br20，比较热卖的一个色号。\n因为我是看了很多功课说比较贴服，\n还有适合干性皮肤才入手的。\n但是我觉得并不是特别贴服，\n还是会有假面感，特别是鼻翼的地方。\n然后最重要的一点是，\n长年不长痘的我，用了几天居然脸上长了好多痘痘🌋\n我本来以为是我上火还是过敏问题，\n但是工作室一妹子也用我的粉底液，\n居然也长了很多痘痘。\n所以我们就推测是这个粉底液的问题了。\n不过每个人用都不一样，\n这款好评还是超多的，\n建议大家到专柜试试再买。\n不然不适合放着就会很浪费。\n😘\n今天的分享基本就到这里了哦！\n谢谢看到这里的你，\n爱你/摸摸大\n#日常妆容打卡[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/2_58232f35d2c8a57dcc440cee',
    'video_id': '58232f35d2c8a57dcc440cee',
    'title': '不好好卸妆小心变成老太婆👵🏻--->👧🏼',
    'video_tag_list': '卸妆测评;芭妮兰 BANILA CO 致柔卸妆膏;缤若诗 Bifesta Bifesta高效眼唇卸妆液',
    'content': '论卸妆的正确打开方式\n哈哈哈，我要卸妆了，你萌快后退。🙈\n💖Banila.Co卸妆膏💖\n这个我空瓶N罐了，算是我史上空瓶最多的产品了。\n我个人觉得真的超好用，温和又干净。\n而且特别方便，直接按摩洗掉就好了，避免了用化妆棉擦擦擦的对皮肤的损害。\n而且一点都不会辣。\n洗完也不会油，不会干。超舒服的～\n一罐大概能用两个月吧，一次一点点就好了。无限推荐啊！！\n唯一缺点就是有时候卸一些眼妆细节卸不到位，我现在配合曼丹用觉得刚刚好。\n🌀Mandom曼丹眼唇卸妆液🌀\n终于入了这个曼丹的眼唇卸妆液，\n因为之前有问过小红薯们哪个眼唇卸妆比较好，\n大家居然一致推荐这个？！\n于是我就拿下了哈哈哈。\n💁\n缩缩我个人用后感，\n这个是没什么味道的，我大爱。\n这个这个上层是奶白色，\n下层是透明的，用之前要摇匀。\n我用的时候用化妆棉沾湿，再敷在眼部，\n大概十秒钟左右轻轻一擦，真的超干净的说，\n睫毛膏，眼线，眼影都被卸得干干净净的。\n而且最重要的一点是！！非常温和。\n但是我个人不建議用来卸全脸，要用化妆棉擦擦擦的，脸好痛，还是喜欢卸妆膏。\n但是我在考虑入个曼丹的卸妆巾，感觉很方便呢，出门旅游或者下班要去运动带上几张就好了。\n✌️\n以后我会用这个卸眼唇，芭妮兰的卸妆膏卸脸部，完美。\n#卸妆测评[话题]#\n#卸妆大挑战[话题]#\n\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/1_582d7d2540c7943b27737692_compress_L1',
    'video_id': '582d7d2540c7943b27737692',
    'title': '宝宝和朋友们的美好瞬间~|视频征集咯~',
    'video_tag_list': '',
    'content': '前几天本宝宝又有一枚访客哟~[吧唧R][吧唧R]\n这次是八个月的阿拉斯加犬蛋蛋（不是二哈不是二哈不是二哈说三遍。。。）\n蛋蛋很大只也很友善，对陌生人也没有戒心，宝宝很喜欢他[飞吻R][飞吻R][飞吻R]。虽然体型悬殊，但丝毫不妨碍宝宝和蛋蛋愉快地玩耍~和朋友在一起的时光总是特别开心，也幸亏保姆帮宝宝录下了这段视频~[害羞R][害羞R]\n各位薯宝一定也有这样的快乐瞬间，是否愿意来和本宝宝分享呢？\n所以！以下，\n本宝宝要向各位薯宝#征集视频#啦！\n小红书最新版本新添了视频功能，有趣的视频内容有机会出现在首页，被更多人看到哦~~目前这一功能还未全站开放，如果你想率！先！体！验！抢在别人前面，就赶快把你的作品砸向薯队长吧，传送门在此：shuduizhang@xiaohongshu.com.\n[赞R][赞R]视频投稿小Tips:\n1.宝宝们生活中每个值得记录的成长瞬间、与宝爸宝妈们的亲子互动、才艺展示（音乐、舞蹈.......）等等，只要与薯宝们相关的视频，请统统砸向本宝宝~\n2、视频投稿请用MP4格式保存，时长15秒～3分钟（不要超过3分钟哦）；\n3、如果你能用word撰写一些和视频相关的介绍、心得等，那就更好啦；\n4、记得在邮件中附上你的小红书ID和微信号哦~\nPS，本宝宝没有忘记摘眼罩的事情，周一见！'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/encoded/avthumb/mp4/s/853x480/vcodec/libx264/5_582ea201a4c80934b16a7199',
    'video_id': '582ea201a4c80934b16a7199',
    'title': '【用户视频投稿 | 新手厨娘的自制蛋挞处女秀】',
    'video_tag_list': '',
    'content': '队长今天好开心~昨天刚刚发出视频征集令~一早就收到了热情小红薯们的视频投稿。笔芯[飞吻R][飞吻R]\n今天播出的是【美食频道】，@Samy_不爱吃花生米 同学的自制蛋挞的视频。虽然这是她的制作首秀，但是烘焙手法和用料都很简单，而且看起来超级好吃！快来跟她学一下吧~\n【用料：\n❤全脂牛奶、奶油、两个蛋黄、细白糖\n❤220度20分钟左右，做出来的卖相当然跟外面卖的不能比😳但自己动手这么简单的过程能这么好吃😋也是超级高兴的一件事！！！】\n下一个频道放点什么好呢？小红薯泥萌还想看什么呢？由你们来决定！！快快给我们投稿吧！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/4_582ee0db36b2a81d9ac2cec2_compress_L1',
    'video_id': '582ee0db36b2a81d9ac2cec2',
    'title': '猫胖你真是够了啦！',
    'video_tag_list': '',
    'content': '果然是本宝宝的好盆友~今天就收到了猫胖的生活片（tou）段（gao），来自敲级有爱的@ETandFATTY [飞吻R][飞吻R][飞吻R]\n好羡慕它有鞋纸穿[扶墙R][扶墙R][扶墙R]（宝宝我只有不靠谱的尿布....[汗颜R][汗颜R]）\n更多猫胖大人和萌宝ET的幸福生活，关注@ETandFATTY 就可以一直follow啦~（本宝宝好想住\n她家[哭惹R][哭惹R][哭惹R]）\n各位薯妈薯爸~如果你也有随手拍下自家萌宝萌宠这么可爱的生活片段~欢迎#随时投稿#给本宝宝哦~\n只需发送邮件到shuduizhang@xiaohongshu.com,标题注明#报告薯宝宝+小红书昵称~本宝宝会火速来和你接头哒~等你哦~~[萌萌哒R][萌萌哒R][萌萌哒R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/2_583020fd046fc56a1747bcf9',
    'video_id': '583020fd046fc56a1747bcf9',
    'title': '用户视频投稿 | 简单的咖啡拉花小技巧',
    'video_tag_list': '',
    'content': '【美食频道】小课堂又开课啦~\n今早队长收到了一个匿名投稿，来自一个心灵手巧的神秘小红薯，他（她）用6秒钟制作了一个简单的咖啡拉花~\n@薯宝宝 看了居然也吵着非要我做给它，可它还是个宝宝不能喝咖啡呀，看来今天要先拿奶粉试试看了。队长于是整理了一份新手制作【心形咖啡拉花】的小技巧，分享给大家哦~\n❤1）奶泡一定要打得细腻绵密，将牛奶和奶泡充分融合，防止倒入咖啡后牛奶会渗透进咖啡的情况。\n❤2）选择杯口1/3处，开始倒入奶泡时小流量注入，并且刺破油脂。\n❤ 3）直到咖啡杯5分满后，保持加大的流量，手臂手腕配合，倾斜杯子，提高拉花缸。小流量注入，直线收尾。\n感兴趣的小红薯可以试试看哦~如果你做的更好或者有更妙的拉花技巧，记得拍视频发给我们。shuduizhang@xiaohongshu.com。 队长爱你哦~'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/58305d19b318f97c28d3f4ee?sign=9bc5377329ceacedb1e927bb448710f6&t=65fb06d4',
    'video_id': '58305d19b318f97c28d3f4ee',
    'title': '胡歌为你播报天气：11月25日，狂风暴雨，电闪雷鸣，他建议…',
    'video_tag_list': '',
    'content': '话不多说，胡歌老大的视频来了，小红薯让我看见你们的手！🖖🏻🖖🏻🖖🏻点！击！起！来！\n11月25日\n小红书红色星期五\n一年只有这一次\n比国外买还便宜！！！！！！\n🌪️折扣来得太快就像龙卷风🌪️\n⚠️SKII前男友面膜只要15元\n⚠️YSL星辰唇膏155元\n⚠️红吕洗发水15元\n⚠️JBL音箱155元\n⚠️英国剑桥包555元\n不吃土买遍\n网红彩妆、热卖护肤、大牌包包\n遇到这样的情况，\n相信你也不会淡定的！\n⚡️11月25日10:00 准点开抢，手慢无！⚡️\n想看更多老大的广告花絮和舔屏美图，请关注薯家族新成员———\n@娱乐薯'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrBP4qt8jSe4sKCJwcuonpkoiAgP_compress_L1',
    'video_id': '5832ff52a75c516a12883bd6',
    'title': '去年小红书全球大赏里最帅最性感的群舞哦',
    'video_tag_list': '',
    'content': '扭动得比女人还要妩媚妖娆百倍的，来自舞团souldance. 编舞的帅哥来自乌克兰，就是那个最左边的.\n穿上恨天高的高跟鞋，舞得全场high翻天.\n去年的全球大赏里，印象最深的就是这个舞团了[喜欢]\n整场show里最爱的是那段希腊舞，看得我热泪盈眶. 大家如果喜欢，也会分享出来哦！\n小红书终于有视频功能啦！赶紧投稿给队长测试一下。 大家如果有3分钟内的短视频，也可以投稿给队长邮箱哦，email：shuduizhang@xiaohongshu.com'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/1_5833f189d2c8a579f3e747e3',
    'video_id': '5833f189d2c8a579f3e747e3',
    'title': '💫小板鸭穿搭视频💫',
    'video_tag_list': '',
    'content': '这是一段用手机渣像素和一个编辑菜鸟编辑的近几天的穿搭视频\n虽然视频很渣 但是你们美就行了呀\n告诉我你们最喜欢哪一套呀'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/59f6a4cf0ef9994e9e22a32c9403745e5c1e9a9b_r_ln',
    'video_id': '583418f1b318f936a04f83a1',
    'title': '保证不喷，优雅开易拉罐',
    'video_tag_list': '',
    'content': '最新神技+生活小窍门！包你一看就想试，一试就停不下来！\n生活薯昨儿看到这个小方法立马觉得GET到了了不得的东西，今儿就立刻分享给大家啦~~原理就是把液体内部的二氧化碳气泡全都弹到易拉罐上部，开罐瞬间跑气！\n记得多弹弹弹弹弹，弹走气泡泡~~\n心动不如行动，试试看你行吗？同时，如果你有其他猴赛雷的生活神技，也可以发给薯队长shuduizhang@xiaohongshu.com  （标明你的小红书昵称和“报告生活薯”），惠及小红薯们呀！\n话题灵感来自@杰米'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/pgc/13bef555-34ab82a-b90b-96a5f89c2b86?sign=ea29f15fe46f57247cb21f780721bdb6&t=65fb06d4',
    'video_id': '58342331805d8926e7507981',
    'title': '十个橘猫九只胖 但求这只不会胖',
    'video_tag_list': '',
    'content': '哈哈哈我也要做奥斯卡薯！来发视频晒家喵！\n开始后3秒才会出现其身影！！耐心等待，前方高萌（sha）\n它叫毛利/猫力/Molly，是一只典型的爱吃爱谁爱粘人的橘猫，现在三个月多不到四个月。\n目前看来还是身手矫健的美男子，希望你可以继续keep fit  ♥'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/7_5834395fa75c51571c05e2ca',
    'video_id': '5834395fa75c51571c05e2ca',
    'title': '🎄圣诞元气绿-紫色妆容教程🎄',
    'video_tag_list': '单眼皮如何画眼妆',
    'content': '✨今天的妆容教程不是裸妆哦，是带有节日气氛的色彩妆容，主要突出眼部，用到的色彩也比较夸张和浓厚，唇笔我用的是NARS的唇膏笔，颜色是很自然的裸粉色\n✨在一款妆容中，夸张眼妆➕裸色唇膏才会美丽和谐又不过分夸张哟😉\n👇以下是这款妆容用到的化妆品和工具：\nDior瞬效美肌遮瑕膏 绿色\nDior Backstage Blender 白色\nGuerlain娇兰水感润彩粉底液\nBeautyBlender 粉色\nMAC单色眼影 Wedge\nToo Faced Chocolate Palette：Milk Chocolate，Cherry Cordial，Gilded Ganache，Candied Violate，White Chocolate，Champagne Truffle\nNARS Dual-intensity Eyeshadow Pasiphae\nThe Seam得鲜防水眼线液笔 黑色\nHourglass 砍刀眉笔 Dark Brunette\nShu Uemura植村秀睫毛夹\nMaybelline美宝莲紫胖子防水睫毛膏\nNARS Bronzer Laguna\nNARS Blush Luster\nCPB高光11号\nNARS唇笔 Rikugien\n.\n妆容完成，你们学会了嘛😘\n喜欢就关注我吧，会不断出#化妆教程#哒😘\n小红书终于有视频功能啦！赶紧投稿给队长测试一下。 大家如果有3分钟内的短视频，也可以投稿给队长邮箱哦，email：shuduizhang@xiaohongshu.com。\n#单眼皮如何画眼妆[话题]##日常妆容打卡[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/1_58367cbd507dbe1dab8f4ff8',
    'video_id': '58367cbd507dbe1dab8f4ff8',
    'title': '很高兴遇见你 ❄️ 小樽 ❄️',
    'video_tag_list': '',
    'content': '2016年的最后一场旅行选择了北海道\n最后一站就献给了小樽 一个浪漫的地方\n静谧的运河 童话故事里的木头房子 幽静的街道\n能想到的一切浪漫相关的 在小樽你都可以看到～\n❄️\n就是这样一座八爪鱼般的城市 小巧玲珑却又应有尽有\n绝对值得花一天的时间好好去感受它的美'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/e367575660164529c24b684d3208594492b5a4dd_v1_ln',
    'video_id': '5836e9219c73ef7823bed274',
    'title': '红色星期五，你们准备好了吗？',
    'video_tag_list': '',
    'content': '大促前夜，近乎疯癫的薯队长们也忙里偷闲的挑战了一次时下最热的mannequin challenge。初尝试请大家轻拍，哈哈哈\n#题为，备战红五的小角落～\n明天就是红色星期五了，大家都准备好了吗[偷笑R][偷笑R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/720x720/vcodec/libx264/2_58381f74f64b3d78f9a854e3',
    'video_id': '58381f74f64b3d78f9a854e3',
    'title': '发现丨星巴克新饮料：梦幻的气致冷萃咖啡',
    'video_tag_list': '',
    'content': '上海降温了，生活薯却顶着寒风为大家去试了星巴克的新饮料：气致冷萃咖啡，冰的！\n没错这不是冰啤酒，这是咖啡！别被绵密的气泡骗了。\n气致冷萃咖啡(英文名Nitro Cold Brew)，将氮气注入低温慢速萃取的冷萃咖啡中，绵密的泡沫就是这么来的，真的有奶油一般的顺滑质地。\n最有趣的就是咖啡端上来的1分钟：从咖啡师将咖啡注入玻璃杯的那一刻开始（跟黑色生啤倒进杯子几乎一样）。咖啡沿着透明的杯壁如微型瀑布一般倾泻而下，层层细致的气泡在咖啡中渐次升起。整个过程，呃，无比奇妙～～～～～～\n目前，全中国只有两家店有：北京国贸商城星巴克臻选门店和上海湖滨道星巴克臻选门店。售价42-68元。\n这是生活薯新开的栏目“发现”，小红薯们有发现什么好的新奇物事，都可以@我哦[飞吻R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/11_583ce9469c73ef35f55bb5d4',
    'video_id': '583ce9469c73ef35f55bb5d4',
    'title': '新手看这里！Morphe 12s眼影盘的5种画法',
    'video_tag_list': '',
    'content': '推荐新手一定要看！\n里面分享了这个眼影盘的基本配色\n还有眼影的基本画法\n学会之后基本所有眼影盘都能驾驭\n画法日常简单\n这个眼影盘很秋冬 显色度很棒价格不贵\n推荐！\n眼影刷:bareminerals\n睫毛膏：Kiss me\n小红书终于有视频功能啦！赶紧投稿给队长测试一下。 大家如果有3分钟内的短视频，也可以投稿给队长邮箱哦，email：shuduizhang@xiaohongshu.com。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/1_583d1988b318f94b2a50a5ba',
    'video_id': '583d1988b318f94b2a50a5ba',
    'title': '不开火2分钟早餐',
    'video_tag_list': '',
    'content': '早餐不吃好怎么减肥，看我只花两分钟不用开火就能搞定美味的早餐吧[讨厌]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/864x480/vcodec/libx264/2_583d348714de412fc18ddeb1',
    'video_id': '583d348714de412fc18ddeb1',
    'title': '圣诞妆容视频征集大赛颁奖啦！',
    'video_tag_list': '',
    'content': '两周前，美妆薯发起了征集圣诞妆容视频，赢取植村秀 X 村上隆圣诞限量合作款彩妆的活动。活动期间，雪花般的投稿飞到了美妆薯的邮箱，各种脑洞大开、新奇有趣的妆容视频让本薯深深叹服！\n最终，我们选出了10支视频作为本次活动的优胜作品。它们凭借着有趣、新颖的内容，高超的拍摄、剪辑技巧从万千投稿中脱颖而出！\n铛铛铛~本薯宣布，这10支视频的作者也就是获得植村秀 X 村上隆圣诞限量合作款彩妆的幸运儿是：@心柘 @宝宝不想取名字 @CandiceS @凌听雨凌听雨 @Yoyi高艺源 @宋依倩Yolly @YVONNEEE @Shaelyn林 @SayLaMoon🌙 @Diadem💓\n以上这10位红薯赶快将你们的信息发送至薯队长邮箱领取奖品吧！\n邮箱：shuduizhang@xiaohongshu.com\n邮件标题：圣诞妆容视频大赛优胜者@美妆薯\n邮件内容：\n1）小红书用户名\n2）微信号\n3）姓名、地址、电话\n（将按照这里的信息将奖品寄给你哦~）\n视频来自 @宝宝不想取名字'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/encoded/5_583ea8141b35a01facf000d9',
    'video_id': '583ea8141b35a01facf000d9',
    'title': '我的旅行化妆包里有什么？！My Makeup Bag！💄',
    'video_tag_list': '我的旅行化妆包',
    'content': "✨What's in my travel makeup bag？我滴旅行化妆包里有什么？\n✨今天这支视频跟大家分享一下我出门会带哪些护肤品➕化妆品，希望可以帮助到选择困难症滴盆友哦🤗\n内容/Products mentioned：\n1⃣️护肤品/Skincare：\nBobbi Brown Soothing Cleansing Oil/ Bobbi Brown卸妆油\nBlanc de La Mer/ La Mer美白净透洁面泡沫\nBeyond Phyto Aqua Toner&Emulsion/ 贝妍德植物源水漾水+乳\nEvian Natural Mineral Water Facial Spray/ 依云保湿喷雾\n春雨面膜、Jayjun玫瑰面膜\n2⃣️化妆品/Makeup：\nMake Up For Ever Smoothing Primer/ Make Up For Ever遮毛孔妆前乳\nCle De Peau Beaute Cream Foundation/ CPB光润粉霜\nCle De Peau Beaute Sponge(for cream foundation)/ CPB异形粉扑\nBenefit Rockateur/ 贝玲妃摇滚甜心腮红\nCle de Peau Beaute Highlighter No.11/ CPB高光11号\nKate Brown Shade Eyeshadow/ Kate骨干眼影 BR-2\nKissme Smooth Liquid Eyeliner/ 奇士美防水眼线液笔\nAnastasia Beverly Hills Brow Wiz/ Anastasia眉笔 Medium Brown\nShu Uemura Eyelash Curler/ 植村秀睫毛夹\nMaybelline The Falsies Volum‘Express Mascara/ 美宝莲紫胖子防水睫毛膏\nMAC Ruby Woo\nGiorgio Armani Rouge Ecstasy/ 阿玛尼红管唇膏 201\nYSL Rouge Volupte Shine/ YSL圆管唇膏 17号 Rose in Tension\nBurberry Lip Velvet No.417/ 巴宝莉哑光质感唇膏 417 Bright Rose\n.\n以上就是我的旅行化妆包滴内容，希望对大家有帮助哦😘\n#晒晒化妆包[话题]##旅行必带[话题]##我的旅行化妆包[话题]##晒晒我的化妆包[话题]#"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/480x268/vcodec/libx264/6_583edc59046fc57d268d4165',
    'video_id': '583edc59046fc57d268d4165',
    'title': '钢琴版《Fade》',
    'video_tag_list': '钢琴演奏',
    'content': "文武贝改编的钢琴版《Fade》，原版近五分钟，有点长了，就把重复多遍的删减至两遍，为了手型更好看把指甲剪短了很多，不过还有点指甲声，专业的宝宝不要太计较啦，之前很多人问我钢琴牌子，是Schonbrunn的，上周参加婚礼，放的是Jay's Wedding，唤醒了我的记忆，两年前有录过，当时还是虫虫钢琴网找琴谱，准备重新练练录给你们听～\n#小红书才艺大赛[话题]##我的个人技[话题]##钢琴演奏[话题]#"
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/4_583fb664046fc561aac577fa',
    'video_id': '583fb664046fc561aac577fa',
    'title': '澳洲✨平价好用🌸护肤品大推荐💗【视频】',
    'video_tag_list': '',
    'content': '这支视频给大家推荐一些澳洲平价好用的护肤品～我本人不是dg 所以只能给大家推荐和分享自己的爱用物和心得～💕\n视频中出现的产品⬇️\n1. Royal Nectar 蜂毒面膜 蜂毒眼霜 ，面膜是奶酪乳偏硬质地 茉莉香味 厚涂略有发热感 眼霜是杏仁味道 清爽不油腻 用无名指点涂在眼周\n2. lucas 木瓜膏 当唇膜 治烫伤 平价好用\n3. trilogy 玫瑰果油 30ml规格的含有抗氧化成分 混合面霜 面膜 或者直接点涂在痘印处 美白 滋润 祛痘印\n4. Natio 玫瑰香薰水 上妆前敷水膜效果非常好！日霜含有防晒指数 很适合秋冬哦\n5. Healthy care 面部精华 含有羊胎素 DNA RNA 还有金箔颗粒 非常清爽\n6. Swisse 维c泡腾片 草莓味 好看又好喝\n7. Blackmores 维E面霜 平价不油腻 用作乳霜或者妆前 网上很多从外包装来辨别真假的帖子 我个人觉得很不靠谱 我在澳洲 chemist warehouse 和Priceline里买到的包装也会有不同 三个月前和三个月后在chemist买到的 包装和味道浓淡也有不同 不管是批号的粗细大小 还是胶管的压合都会有不同 因为澳洲的品牌商其实不太在意包装 所以会有出入 不管是护肤品还是保健品 所以大家不要单凭什么真假辨别贴 就断定一个东西的真假啦 还是要找靠谱的人靠谱的地方入 依靠使用感才能发现真假～\n希望大家喜欢这个视频啦～欢迎大家留言～🤗'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/9d0b5e8000a2fcc856d17b8592bd052c609c3048_r',
    'video_id': '5840086ad5945f43fd4316c5',
    'title': '【伦敦游记】两分钟视频带你身临其境全伦敦最好玩的圣诞主题公园',
    'video_tag_list': '',
    'content': '每年冬天 海德公园（Hyde Park）都会有冬日仙境（Winter Wonderland）一般从11月末到1月初。有游乐园、溜冰场、马戏团。其中最重要的就是圣诞集市了 各种各样的小吃 像西班牙油条、热葡萄酒、德国大肠等等。看秀什么的更是必不可少 各种娱乐项目几乎都齐了！入场不要钱 当然要吃点什么玩点什么就要另外交钱啦！\n游乐园的项目和澳洲一样 需要在一个小亭子用钱买Points 1英镑=1point。像玩旋转木马啦 碰碰车啦 还有闯关的小屋子啦都需要用points的票进入。因为那些过山车刺激的项目没玩 所以两个人50英镑就足够啦！\n值得一提的是 Winter Wonderland里的冰场堪称英国最大的溜冰场 10万支灯光装饰 溜冰场的中心位置还有现场歌唱演奏表演 非常浪漫的气息。\n圣诞老人主题区最主要针对小朋友 里面充满圣诞节的布置 还可以与圣诞老人拍照。乐园里巨大摩天轮 虽然无法与伦敦眼相比 但高度60公尺也足以欣赏到海德公园周围美丽的夜景了。\n整个Winter Wonderland 聚集了马戏团现场表演 热闹的圣诞集市和一大堆的游乐项目。有的吃有的玩还有的看～不管你是专门来滑冰的还是想来玩上一整天 这里都是不错的选择。\n不多说了 看我两分多钟的视频就知道究竟有多热闹好玩了哈哈！（第一次做视频 才发现剪切配BGM都不是简单的事儿 不过做出来好有成就感[装酷][装酷][装酷]\n*附上交通信息：搭乘地铁Central线，至Lancaster Gate站或Marble Arch站下车，再步行约2分钟可到。或搭乘地铁Piccadilly线，至Hyde Park Corner站或Knightsbridge站下车，再步行约5分钟可到。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/2_5847a9dab46c5d1fae02fbb3',
    'video_id': '5847a9dab46c5d1fae02fbb3',
    'title': '一起来变小脸！面部修容提亮技巧',
    'video_tag_list': '',
    'content': '全部都是自己总结的经验技巧 没有报班学过\n属于欧美一点的修容方法\n本人脸大 特别大\n但是不会修的特别重 很自然的那种\n同时也会提到高光提亮的技巧\n视频中提到的产品：\ntoo cool for school三色修容粉\nrimmel bronzer\n丝芙兰49号斜角刷\nSIGMA 斜角刷＃e70\n美宝莲三色眉粉\nessence pure nude高光 ＃10\nbecca 高光粉 ＃pearl\nRT setting brush\nsigma 高光刷 #f35'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/11_584a60c5d2c8a548edb09c10',
    'video_id': '584a60c5d2c8a548edb09c10',
    'title': 'wi美妆视频-双色眼影妆',
    'video_tag_list': '',
    'content': '化妆其实很简单，干净的底妆，精致又简单的眼妆就能有与众不同的妆面效果。很多女生都害怕话眼妆，不会画眼妆，其实眼影不需要太多颜色，只要深浅两个颜色也能画个非常美妙的妆容哦！\n#wi美妆分享#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/2_584a9beefaa05208e4d1cade',
    'video_id': '584a9beefaa05208e4d1cade',
    'title': '你的唇膏到底有多粘杯？',
    'video_tag_list': '',
    'content': "周末到啦，美妆薯又来给大家布置周末美妆小功课啦！你的唇膏到底有多沾杯？\n美妆薯从办公室搜刮了11支唇膏和6支唇釉，先替大家做了一支小视频，最不沾杯的竟然集中在唇釉，而ESPOIR、JULEP这些新秀彩妆品牌也是表现出色，一点都不输大牌。\n第一组：\nYSL ROUGE VOLUPTÉ SHINE OIL-IN-STICK （圆管）\n沾杯指数：★★★★★\nBURBERRY KISSES\n沾杯指数：★★★★☆\nLE ROUGE GIVENCHY （小羊皮）\n沾杯指数：★★★☆☆\nTOM FORD LIPS&BOYS\n沾杯指数：★★★☆☆\n第二组：\nDIOR ADDICT FLUID STICK\n沾杯指数：★★★★★\nCHANEL ROUGE COCO\n沾杯指数：★★★☆☆\nGIORGIO ARMANI LIP MAESTRO LIP GLOSS\n沾杯指数：★★☆☆☆\nREVLON COLORSTAY MOISTURE STAIN™\n沾杯指数：★★★★☆\n第三组：\nETUDE HOUSE DEAR MY BLOOMING LIPS\n沾杯指数：★★☆☆☆\nCHARLOTTE TILBURY MATTE REVOLUTION\n沾杯指数：★★★☆☆\nLIME CRIME VELVETINES LIQUID MATTE LIPSTICK\n沾杯指数：☆☆☆☆☆\nESPOIR - NO WEAR SIGNATURE\n沾杯指数：★★☆☆☆\n第四组：\nJULEP It's Whipped Matte Lip Mousse\n沾杯指数：★☆☆☆☆\nROUGE DIOR\n沾杯指数：★★★★★\n3CE GLASS LIP COLOR\n沾杯指数：★★☆☆☆\nESTEE LAUDER PURE COLOR ENVY SCULPTING LIPSTICK\n沾杯指数：★★☆☆☆\n如果你觉得这个视频很有趣，你也想要参与，欢迎投稿给我们。\n我们对于视频的要求：\n1、\xa0 必须是MP4格式\n2、\xa0 时长最好不要超过5分钟\n3、\xa0 请保证在日光或者光线明亮的场所进行拍摄\n4、\xa0 投稿请发送至：shuduizhang@xiaohongshu.com"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/5b702dfa4907fd79b338b6287045861abb3989f5_r_ln',
    'video_id': '584aa6bcfaa05216c5cccc88',
    'title': '胡歌什么都懂，你们还爱薯队长吗？',
    'video_tag_list': '',
    'content': '没几天不见，胡老大又杀回来了！\n1分30秒的小片片里，胡歌哥哥为你解锁小红书的N种正确打开方式～\n从护肤心得，到生活神器，到穿搭指南，队长真的不是很明白，好端端一枚才华横溢的盛世美颜，为什么还要让自己又贴心又博学又懂生活又懂女孩纸了啦？！？！（咬手绢[扶墙R]）\n🍠队长我只想独享3200万小薯恩宠，胡歌处处要向本队长看齐，这是在搞事情呀！！[生气R]\n💥现在问题来了💥：\n如果胡歌和薯队长同时掉进水里，你们到底救谁？？？？\n（不许说红薯自己会浮在水里这种话！）\nP.S.\n现在，在小红书里搜索“胡歌”（搜索框自己往上看啦），选择“商品”页，你能找到一些不得了的东西哦！❤\nP.P.S\n不过，想到一个广告也能拍得这么好看，队长觉得自己还是才华蛮多的。\n今天的晚饭还是加个鸡腿🍗吧。\n祝你们今晚梦里也有胡歌，哦不，本队长哦～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/1_584e256bd1d3b92b8310a302',
    'video_id': '584e256bd1d3b92b8310a302',
    'title': '闪闪粉棕系眼妆',
    'video_tag_list': '',
    'content': '无聊再来一发化妆视频，其实化妆很简单\n隔离：sofina妆前乳\n粉底：chanel粉底液\n遮瑕：ipsa三色遮瑕膏\n定妆：纪梵希散粉1号色\n眉笔：爱丽小屋眉笔1号色\n眼影：爱丽小屋眼影盘6号色\n眼线：爱丽小屋101多功能笔1号色\n睫毛膏：芭妮兰首尔狐尾睫毛膏\n阴影高光：ponyeffect四色修容\n腮红：canmake\n唇膏：jillstuart 方管1号+唇蜜23号'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljRuZIhxA6cRL_Ym9PIFB_PVBGjs_compress_L1',
    'video_id': '585030fbfaa052135001c48d',
    'title': '小红书新版本的短视频功能终于发布啦，不一样的烟火来庆祝',
    'video_tag_list': '',
    'content': '短视频功能终于上线了，貌似目前只开放给了一些幸运的勤奋的小红薯，[喜欢][喜欢]小马薯可以哒！\n就用这不一样的烟火来庆祝这期待已久的新功能吧！\n烟火还是很壮观的，来自于去年新加坡的国庆演习（注意，只是彩排而已哦！）作为加班狗，拍摄于前公司办公室里，open view of 新加坡的滨海湾金沙酒店，full view of 整个烟火场景.\n最近开始研习眼妆，下一只视频想奋斗一下眼妆测评路线，大家会想看不[活力] @美妆薯'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lttBVco_fdgYEuTtqDCS6iupjf2h_compress_L1',
    'video_id': '5850a179d5945f15d2db9341',
    'title': '西班牙Bilbao米其林一🌟餐厅 chef现场做小甜品',
    'video_tag_list': '',
    'content': '能发视频了耶[得意][得意]\n西班牙北部巴斯克地区散落着最多的米其林星星，首府Bilbao好吃的不胜枚举。推荐一家和@包包包包有一只包包有一只包包 一起去吃的Etxanobe餐厅[得意]\n具体探店笔记之前写过啦。这里就奉上品尝菜单最后的压轴神秘甜品。\n点了Menú de degustación （品尝菜单）加上服务费，人均95€  12道餐，按照板鸭人民边吃边聊不停的用餐速度，可以吃3-4小时每道餐品都有小故事，大厨或服务生都会给你讲解一下背后的来由。\n大厨还是个中国文化迷，之前来过中国教课。看到难得一见的中国食客，很愿意和你聊[得意]\n题外话[活力]\n西班牙北部的亚洲游客相较于Madrid/Barcelona/Valencia/南部Andalucía要少很多。但如果喜欢美食，喜欢自驾游，喜欢hiking，很推荐西班牙北部深度游。[少女心]\n#用视频记录美食的别致瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fq4ZYuhSbIYm_wmoZDAesvxydnH2_compress_L1',
    'video_id': '5850cdb1d5945f5ab9374b2b',
    'title': '🔓短视频',
    'video_tag_list': '我和宠物的日常',
    'content': '#仨喵的日常#\n猫小七和tibi这对小两口，\n每天最喜欢的事情呢，\n大概就是在鸡肉面前花式秀恩爱了[抠鼻]\n此时此刻，\n我肉的内心潜台词一定是：臭 不 要 碾！\n介绍下它们仨：\n老大，猫小七，美短，男孩，傲娇粘人。\n老二，鸡肉，英短银渐层，男孩，爱摆臭脸粘人。\n老三，tibi，孟加拉豹猫，女孩，有着与外表不符的温柔性格。\n#我家宠物最萌的瞬间[话题]#\n#我和宠物的日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/lse47AK39OIFtUjtFEqack2HkSB7?sign=e194ed34b0af6028e16d644ed9a9749a&t=65fb06d4',
    'video_id': '5850f535d1d3b96b7af955b9',
    'title': '美甲心得，如何让水性可剥指甲油更持久？！',
    'video_tag_list': '',
    'content': '要用到的美甲工具有：\n1、指甲刀\n2、死皮剪\n3、抛光棒\n4、指甲油\n人鱼之水 羽衣甘蓝底油\n人鱼之水 免烤封层甲油胶\n人鱼之水 marry me系列甲油，色号：樱桃泡芙、宛若初见。伪装系列指甲BB。\n首先，清理我们的指甲\n1、洗手，然后剪好自己想要的长度\n2、去死皮、抛光。\n清理指甲的目的：\n一方面是为了清理干净你的指甲，另一方面其实是为了更好的上指甲油或是做指彩。\n然后，开始涂指甲油\n1、涂底油\n底油的作用是隔离指甲和指甲油，防止指甲断裂或分层。\n2、涂指甲油\n✖️错误的涂指甲油方法：\n很多宝宝都会有涂不均匀的烦恼，反复涂抹，容易使指甲变得不平整，还会把已经上好的颜色再带下来，影响光泽。\n☑️正确的涂指甲油方法：\n用最少的次数把指甲涂全，以中间、左、右这三笔来完成上色的动作。如果觉得涂一层没有明显效果，则可以干后再涂一层，效果就出来了\n一般浅色的涂三层，深色的涂两层就够了。\n最后一步：涂顶油\n很重要！！！涂顶油（亮油）为了增加甲油亮度，使指甲油不易脱落。而且使甲面更加平滑、如水晶般透亮，使指甲油保持更长久的时间。\n小贴士：值得注意的是，在涂了水性指甲油后，不要马上长时间浸泡在热水里，否则会容易脱落，最好是在4个小时之后，这时指甲油已经完全附着在你的指甲上了。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ln28yJc27MBnUsxB8hDF_sYsZKLc_compress_L1',
    'video_id': '5850f8fcb46c5d4282e04d84',
    'title': '谁说便宜没好货？muji四色眼影表示不服！',
    'video_tag_list': '',
    'content': '#跟着视频画眼影#\n😳啊 我来试试新功能…这款眼影是我逛muji时随便买的，大概60出头的样子吧，很便宜。拆开后试了下，竟意外的好用！～粉质软糯，显色不飞粉，上眼不灵不灵的，随便一抹就很好看～\n〔敲黑板划重点〕它不仅可以当眼影，还可以用来画腮红、高光、卧蚕，一盒眼影搞定一个妆，很适合懒人和学生党妹子们～'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lv0ghZElRWWwhH3-WUA6AslG6cRM_compress_L1',
    'video_id': '5850ffbd78362318d79340ac',
    'title': '吃什么已经不重要了～新加坡圣淘沙海底餐厅',
    'video_tag_list': '',
    'content': '今天小周末 你们都去哪里嗨\n马不停蹄工作了三天的我 表示我要回家躺 哈哈\n新版本可以发视频啦～更直观啦\n分享个之前发过的 圣淘沙岛上的海底餐厅～\n吃什么真的不重要 重要的 真的很美啊～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liV69JUzq37Ip0BXr3UVCsnFYDq__compress_L1',
    'video_id': '58512c04d2c8a528a752c71b',
    'title': '视频功能新体验-大溪地Borabora让人窒息的美',
    'video_tag_list': '',
    'content': '传一个大溪地的视频过下瘾\nTahiti 的Borabora岛，我的终极海岛！\n在水飞上航拍的效果简直惊艳！\n坐帆船出海，拍到清澈的海面...\n这一切太美好，必须拿出来和姐妹们分享😛😛😛'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljxQiYm91lAx6-k0yfJs8bRF4JW6_compress_L1',
    'video_id': '5851345fd2c8a5355352c726',
    'title': '🍚吃货发超爱的拌饭——橘炎胡同员工饭🍚',
    'video_tag_list': '',
    'content': '🍚此条纯粹为了感受新功能[笑哭R]饭超好吃！[色色R][色色R][色色R]\n🍚打算周末搞个头发相关的视频，也没拍过，不知道会成什么样，我争取不太监。[叹气R][叹气R][叹气R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvRO2kJbXzgBzfG-4yKbKoNq1GpP_compress_L1',
    'video_id': '58514c42b46c5d4081b15fc2',
    'title': '敏感肌看过来！亲测有效的换季敏感好物！',
    'video_tag_list': '',
    'content': '好开熏小红书开了视频权限，我决定把之前录的敏感肌的碎碎念拉出来二次曝光～好可惜只有五分钟的时间限制后面可能看不全了哦\n不过不耽误敏感的宝宝们过来种种草～\n希望我推荐的温和护肤+卸妆你萌能喜欢～\n么么哒！如果想看什么内容欢迎随时留言骚扰我哟\n@美妆薯 看过来哟～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lp2FQd5ll08KqzBHJ1Me8ycple2C_compress_L1',
    'video_id': '58514db314de415e0059953f',
    'title': '💄H&M #Brandy Snap & 视频求教💄',
    'video_tag_list': '',
    'content': '💄之前试色过的BrandySnap，这只好美，我都快啃完了！早知道该用一囤一的。[扶墙R][扶墙R][扶墙R]\n💄微博大神们的嘴角到唇峰画法我怎么画怎么不顺，所以一直都是这么画的…管它的顺手就好。[得意R][得意R][得意R]\n🎬在家练习拍视频，找不到手机架了[哭惹R]。sei能指教一下，视频画面怎么剪切成想要的比例？[叹气R][叹气R][叹气R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/li9KYrz2dl0Ilqcce7GCgBVFLFX8_compress_L1',
    'video_id': '585208b2faa0522bd4c96482',
    'title': '天气太冷不敢敷面膜？洗澡时花三分钟就好啦',
    'video_tag_list': '',
    'content': '诶嘿嘿，发视频的小玛丽又来啦～好多人都觉得天气冷敷片状面膜太冷了，但是我有办法在洗澡的时候同时解决敷面膜的问题～只要花三分钟敷一敷就搞定啦！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltzJ-AIY823DemjdU6FGIig4RWlJ_compress_L1',
    'video_id': '58520c64faa0523288c96480',
    'title': '就算冬天也要记得防晒补涂啊！脸和身体要分开哦',
    'video_tag_list': '',
    'content': '对于在南方的我来说，冬天露肤程度也是挺厉害的，所以！长时间外出还是要记得补涂防晒的！\n面部我一般会用防晒棒，这样带妆补涂也方便。\n身体就用防晒喷雾多盆几遍，不过要注意外出高铁和飞机安检，喷雾不一定能带上去哦！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgT66Fird4S-k4lpJegXIacM76vi_compress_L1',
    'video_id': '58520e06d1d3b93b1716c3e7',
    'title': '戴眼镜也不能忘记眼妆！来给眼妆加点料吧～',
    'video_tag_list': '',
    'content': '#跟着视频画眼影#\n戴眼镜的妹子是不是经常被人说一脸懵逼双眼无神，肯定是因为没化眼妆啦～！然而眼镜妹的眼妆不需要很浓，够用就好，看我给眼睛加了点什么料吧'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loUPJiEyXAIpoyUx2Osy6pTLtQvc_compress_L1',
    'video_id': '5852384cd5945f5cb7b9f104',
    'title': '颜值高到梳头都能高潮的天使梳，买了绝对不后悔！',
    'video_tag_list': '',
    'content': '这个梳子叫tangle angel天使梳，为啥叫天使梳呢，当然是因为人家名字里有angel啦！哈哈哈哈哈哈好肤浅，是的就是那么肤浅。还有就是这把梳子的外形就是一对翅膀，好看得不止一点半点！\n我买的是珍珠白色的，另外有好几个颜色也是美哭！\n我一直在纠结到底买哪个颜色！绿松石色和紫色也好美！粉色也好美！\n就像我在视频里说的一样，这个梳齿细软长，梳开打结的头发so easy，还不会有静电。最关键的还是你照着镜子梳头的时候，真的觉得自己上升了不止一个档次好吗？！\nand看视频就可以看出来真的能把乱发梳的超级垂顺，还有光泽感，跟路边两块一把的贱货真的不一样～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lh74xFKRw8zfZAUCtsP2Y-0StXBN_compress_L1',
    'video_id': '5852454cd5945f70e4b9f101',
    'title': '冬季护体只涂身体乳？',
    'video_tag_list': '',
    'content': '身体护理除了涂身体乳，可能你还需要一个柠檬[腹黑]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrbivmdUkK9SY0wWyfiMtMwhxpx__compress_L1',
    'video_id': '58525362faa0521a7b97ddb3',
    'title': '外出游玩回来记得要急救护肤哦！',
    'video_tag_list': '',
    'content': '长痘黑眼圈什么的，出去玩一趟熬个夜全都出来了[哭哭]只有这些能救救我的问题肌肤'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liy4UQF5Y5hV7Sm8Ja2Gjb1DjuHf_compress_L1',
    'video_id': '58525b79b46c5d3ed2e2f5b2',
    'title': '张雨绮红唇粗眉仿妆，仿不了她的胸可以仿她的脸啊',
    'video_tag_list': '',
    'content': '臭不要脸的玛丽又开仿妆了[腹黑]\n这次选的还是红唇女神张雨绮，仿妆要点就是皮肤要白，眉毛要粗，嘴唇要红，修容要狠[讨厌]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llqHjZEF-5Kbq2ctFvJoEnia3pYY_compress_L1',
    'video_id': '58528e8fd5945f590b7c1a59',
    'title': "周杰伦《Jay's Wedding》",
    'video_tag_list': '小红书才艺大赛',
    'content': '杰伦婚礼上的背景音乐，不是传统的婚礼曲，而是他自己编谱作曲，简直用心到极致，再看一次杰伦的世纪婚礼还是很震撼，第一次听就爱上，想练出来的曲子，不知道你们是不是，每次婚礼上一响起背景音乐，新娘牵爸爸手走进来的时候我都会眼睛红，不知道将来自己婚礼上会不会哭成泪人。\n#小红书才艺大赛[话题]##我的个人技[话题]##钢琴演奏[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg_p0PSdJR4Zmh3w5niRzYCboh46_compress_L1',
    'video_id': '58563510d5945f7f31fe253a',
    'title': '近期空瓶～',
    'video_tag_list': '',
    'content': '跟大家分享下近期空瓶，\n哈哈哈又回购有不回购哒！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lo7UtUfrZe1zGYKK4PxHencli4qx_compress_L1',
    'video_id': '58565405d1d3b952e5b5821e',
    'title': 'Broken face 线条款创意妆',
    'video_tag_list': '',
    'content': '终于能自己发视频了 庆祝下[喜欢]\n[装酷]灵感来自碎玻璃\nproducts ：anastia 阴影膏，ysl粉底液，101stick，眼影来自无名牌\n步骤：\n打底白色，建议用人体彩绘，这次用提亮笔打太淡\n阴影要重\n用眼影勾线，加重提亮\n配装饰和隐形眼镜[装酷]\n之后想画欧美妆 么么哒'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lig8Zmfj9h49kUpw_5lTyzW3Ekqt_compress_L1',
    'video_id': '5857d5e5faa052721846f91f',
    'title': '美瞳推荐分享篇 #视频',
    'video_tag_list': '',
    'content': '给大家录一个美瞳特辑篇\n一直会有人问到美瞳 然后就整理了一下分享给大家\n其实平时在学校都戴眼镜也很少带美瞳\n但是还是有些好看有舒适的美瞳推荐给大家啦\n我一般都是日本代购买的美瞳 从日本邮寄到英国\n希望视频对大家有帮助\n喜欢记得点赞哦么么哒\n[飞吻R][飞吻R][飞吻R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lknySsq6xYG89vTfHgyTN8RWLnEN_compress_L1',
    'video_id': '5858b44614de411d08114191',
    'title': '西班牙塞戈维亚百年烤乳猪店',
    'video_tag_list': '',
    'content': '这家店就在塞戈维亚大水渠旁边，据说国王以及各界名流都来吃过。这里最著名的烤乳猪餐，特色就是用盘子来切割，以证明他们的烤乳猪烤的多么好，最后要把盘子在客人面前摔碎。\n盘子碎片就在我们的腿边划过，我问导游，这样摔会不会碎片划伤客人，他说这么多年就发生过一次，那个领队是回民，按理不应该进来，但他带的是客人在里面吃饭，他就进来看了这个仪式，结果就他的腿隔着裤子都被划破了，你说神不神'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/FusKTTCaQhY5kDFPLL2qz896-sbw?sign=be2122f9813d075c31c36353688d3d47&t=65fb06d4',
    'video_id': '5858f91ad1d3b940957483db',
    'title': '我们会握手啦 ( ˘ ³˘)♥ 家有小法斗',
    'video_tag_list': '',
    'content': '[得意] 英文名 cash\n[喜欢] 中文名 牛牛\n年龄 6个月\n特技一 百米冲刺\n特技二 握手\nvideo里面就是握手的片儿 啊哈哈哈 没有吃的奖励的情况下哦\n[喜欢][喜欢][喜欢]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltyhx9Q57Xm_C9Y63gudtNyqWBxH_compress_L1',
    'video_id': '58590f657836231b99da6dd3',
    'title': '和小伙伴的冬日冰岛自驾🇮🇸',
    'video_tag_list': '',
    'content': '最近一直没发小红书，因为我在冰岛啊！超级遥远的国度～\n这里简直太好玩啦，等我回去整理照片写游记给大家，先放一个小视频预告一下～\n紧接着还会去巴黎，布鲁塞尔和阿姆斯特丹，小红薯们不要取关我呦[飞吻R][飞吻R][飞吻R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkPllVbJP_XUS26gaUkx1VAoOBQ4',
    'video_id': '5859dd7ad2c8a5556f4401f7',
    'title': '🌸零基础化妆教程视频🌸',
    'video_tag_list': '',
    'content': '菜鸟，化妆小白们的福利时间～\n很多宝宝都来找我想让我有空一定要出个基础版化妆教程，这次不辜负大家期望，我们从零开始\n看着人家画出来的妆容都是裸透肌，不要以为裸透肌这么简单，只是气垫拍一拍那是商家卖产品的说辞，真正的裸透感需要画出来哦～\n#wi美妆分享#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrxRUEhFRko7C5VnoQ31bEIpxlRF_compress_L1',
    'video_id': '5859f88e783623656130670c',
    'title': '👇🏻在家就可以做的腿部练习🏃🏻\u200d♀️(含视频)',
    'video_tag_list': '练出翘翘蜜桃臀',
    'content': '由于小红书最近在更新视频功能，我晚发了几天[扶墙R] 让大家久等了!\n上次发的腹部练习看到有人多人点赞和收藏，看到留言说想要练习腿部，那这周就录了一个腿部练习的视频，希望大家跟我一起来完成\n有很多小红薯也许没有健身房资源，所以我这次录的是在家里也可以做的[得意R]\n一共四个动作，不难，很简单，很基本，等大家掌握好这些基本的腿部练习我再带大家练习带重量的动作\n-----开始-----\n1. 深蹲 X 20\n2. 弓箭步 X 各10\n3. 侧弓箭步 X 各10\n4. Jump Squats X 15\n-----结束-----\n这样算一组，一共三组，每组休息30秒到1分钟。\n⚠️4个动作之间要连续起来，不要休息\n深蹲的要领就是要感觉后面有一把椅子，往后坐的那种感觉。背要直，不要弯背弯腰。下蹲时，膝盖不要超过脚尖。脚的站位是跟肩膀垂直或者比肩膀再宽一点。\n如果这些做下来很困难，那就减一半次数，慢慢来增加。\n大家一起来加油⛽️[赞R]\n#腿部塑形视频[话题]#\n#无器械锻炼视频[话题]#\n#必须要安利的健身动作[话题]#\n#练出翘翘蜜桃臀[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/lgpVNl00mOXrRm6y1j9U1I-eaXbi?sign=fa3565dfca411ba60cdf6e2285f31797&t=65fb06d4',
    'video_id': '585a1dfbd2c8a527eb4401f7',
    'title': '🌸冬日暖红色系妆容视频🌸',
    'video_tag_list': '',
    'content': '冬日就应该暖暖的才温柔，推荐一款暖红色系妆容教程，从眼影的选择就要从红色系开始考虑哦～\n咦！最近怎么我都在推荐红色系，果然女生还是喜欢红色比较多，不管是粉红还是大红[飞吻R]\n这款的妆容的感觉就是温暖，配上厚厚的高领脑子就再合适不过了\n#wi美妆分享#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltgX1Ofk1SP4__PEX2HWDLtpDEZV_compress_L1',
    'video_id': '585a42fc14de410140114198',
    'title': '🐠潜水小视频+体验式潜水指南',
    'video_tag_list': '',
    'content': '🐠试着发一个小视频，之前在塞班岛潜水拿相机录的，没有剪辑，拿iMovie加了音乐，但是不能调节声音，大家凑合着吧，潜水的声音比较大…那个手一直在想着抓鱼的就是我🤗\n🐠那就借着视频用亲身经历和大家聊聊如果第一次潜水的话的注意事项。刚好马上元旦、过年放假肯定好多红薯们要去海岛度假啦，希望这篇有用的~\n🐠我们当时自己在淘宝上搜“塞班岛潜水”就会出来很多（其它热门海岛景点同样适用），随便找的一家，后来体验下来觉得还是很靠谱的。就是自己在那边做游客潜水的中国人团队，比旅行社要便宜也不坑，带着你下去潜水什么的觉得都挺专业的，价格不太记得了好像是500一人，体验式深潜，酒店接送，装备他们提供，教学+体验大概需要一个早上吧。约好时间到酒店接我们，然后上一个大的游轮，游轮上还会有别的教练带着别的游客，但是总人数不多很安全的。然后在游艇上换衣服，自己事先要在酒店穿好泳衣，到船上一套潜水服就好。说了注意事项后就会慢慢带我们下水了\n🐠我们一行是5个人，那个教练和他的一个助教两个人带我们5人，先是在水浅处确保你会潜水的呼吸了。这个还挺要命的，我一开始不会呼吸，以为是像平常那么很轻微的呼吸就好，结果发现一进水就很闷，后来发现要像用吸管吸水那样大口呼吸，就很顺畅了。呼吸正常了我个人就是没什么问题了就直接下水了。心里一定不要害怕，当时同行的一个朋友一直觉得自己呼吸不畅就无法下水，结果最后没能潜水只能上船等我们。过后她觉得也是自己心里作用比较害怕，呼吸其实没什么问题\n🐠我们当时潜水是一直抓着一根绳子跟着教练走，结果有个朋友没抓住，加上她又比较轻，一下就浮到水面上了，教练给她加了几块铅吧她才又下来。当然像我这种重量级的应该不会出现这样的情况。总之大家就是别害怕，听清楚教练的注意事项和口令，下水都是用手势沟通。咱们中国的游客比较强大所以一般在外面比较火的海岛都是会有中国的潜水教练的，所以沟通也是无障碍\n🐠然后这个视频，我当时租了一个奥林巴斯的防水相机，给教练帮拍帮录的非常方便，淘宝上就能租～这种美妙的瞬间一定要留念下来呀\n🐠总之，潜水一定要体验呐~开启新世界美妙极了，国外的海都好蓝，真的就是宝石的颜色形容不出来的，鱼儿也是各种美腻欢脱~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/louOt-rb8jq_JtvGB3xFutzOTUj-_compress_L1',
    'video_id': '585b3a61b46c5d52d26cd57d',
    'title': '响应队长号召🎉 | 属于你的圣诞Music是…',
    'video_tag_list': '',
    'content': '#小红薯的圣诞节#\n圣诞节，真爱至上。\n每年圣诞，点击率最高的电影必须是圣诞至上Love Actually……\n在这个最经典又最温馨的片段里，小红薯是否听到了最熟悉的圣诞歌声？\n万能的薯队长将圣诞旋律悄悄捕捉了下来，放在了小红书的圣诞限定小红盒上。属于你的圣诞music又会是哪一首？'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/1_585b57a4d1d3b91e9f6a392c',
    'video_id': '585b57a4d1d3b91e9f6a392c',
    'title': '👏🏻新手看过来 - 做美妆视频so easy！',
    'video_tag_list': '',
    'content': '小红书的短视频功能已上线，相信很多热爱美妆和化妆教程小伙伴都跃跃欲试，可是从没有接触过视频制作的小白童鞋该怎么办呢？\n不要担心，看了这支小视频你们就会有信心啦！其实想要做好视频hin简单～\n🔧首先，你需要拍视频的工具🔧\n1⃣️相机：可以是相机，单反，微单，摄像机，还可以用手机哦！📱iPhone6s、7的相机功能其实已经灰常强大了哦！具体的拍摄工具根据自己的需求和budget来选择。只要录像功能能达到1080✖️1920就可以（现在相机基本都没问题）\n2⃣️三脚架：这个非常！非常必要！一定要把相机固定再拍摄哦，不然抖动着拍出来的效果一定不会好，还容易把自己和观众弄的眼晕🤣\n3⃣️光源💡：好的光源可以提高视频的质量和质感，尤其是当你拍摄的地点光源不足的时候，可以选择环形灯、LED灯，也可以是摄影棚内用的那种柔光灯箱（我管它叫大罩灯🌟）\n🔧拍摄工作完成，就是后期的制作了🔧\n💻先将视频导入电脑，然后直接使用一款视频剪辑app或者软件就可以，我用的苹果本儿，所以我剪辑视频的工具就是电脑里自带的iMovie，其实还有几个更高级的付费软件，不过iMovie对我来说已经足够了，毕竟我又不做大片儿🤣\n好啦，今天唠嗑到这里，你们学会了嘛？\n快快开始吧！\n#视频教程# #短视频#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liB6xk2WyDvZiE2TQWAvtiVj_VGy_compress_L1',
    'video_id': '585b5a3ad5945f400f61e8df',
    'title': '【视频来了】健身没有借口，做一切你能做的，你就会成功',
    'video_tag_list': '',
    'content': '话说，最近小公举我左手腱鞘炎一直不能正常训练，但对于我来说，这个怎么可以成为阻碍我健身的拦路虎，真正的勇士就是克服困难，想尽一切办法训练呀😊😊于是各种研究如何不用左手一样可以训练到各个部位的方式。于是乎，练着练着突然练成了跪姿单手俯卧撑，哈哈哈，想要起飞！\n原来只能一次发一个小视频哦，还想发几个我这个残疾人研究的各种训练法呢，嘻嘻。下次再发吧'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrT5rmsKpToohjmGsJ3-fVpjKwnE_compress_L1',
    'video_id': '585bee24d2c8a550951816f9',
    'title': '闺蜜🎄聚餐💗',
    'video_tag_list': '',
    'content': '今天晚餐在Coquille Seafood Bistro  上海 法国餐厅吃饭好开心，上班的疲惫全部都没有啦😘😘\n祝福大家圣诞新年愉快。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luDa5mGelUJ3ght4Eog_JoCdJ8WP_compress_L1',
    'video_id': '585cc77414de4130447bf2b3',
    'title': '只用手指上妆大挑战',
    'video_tag_list': '',
    'content': '请不要耻笑我的眉毛[抠鼻]\n用手指画什么都难不倒我，眉毛眼线除外[哭哭][哭哭][哭哭]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lq37YHdlj3RbC1QMXuwmgfoGcZLK_compress_L1',
    'video_id': '585d2930d1d3b90a2fcb3141',
    'title': '什么都不买也要买这个！',
    'video_tag_list': '',
    'content': '最近很多妹子问我用什么眼影，\n推荐一个我日常用最多的眼影盘哦！\n超级万能的说～❤️\n#Pony第二代八色眼影盘#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/pgc/1b68af92-02b0899-88a6-31af0f13cac4_compress_L1',
    'video_id': '585d44c23460941c84a55113',
    'title': '要比比圣诞礼物吗？你可能还不如这条狗',
    'video_tag_list': '',
    'content': '圣诞礼物清单看到有审美疲劳了有没有，圣诞好物比繁星还多，重点是来分享下本大王种下的新草，有美容界的“颜王”，有抢破头的好用神器，还有让肌肤也有执念的网红款。（当然还有幸邀请到网红狗子bobby，此处掌声雷鸣）\n最有仪式感的圣诞美妆礼物——Burberry 圣诞系列\n这个系列之前已经有过完整描述了，想看的同学可以翻下我上上上篇笔记，有讲的很详细~\n比天上星星更明亮的是你的眼——HR圣诞限量礼盒\n其实此次HR的圣诞礼盒不能叫做限量，因为它也就是用6款睫毛膏+6款眼霜，随便你任意搭配组合购买。此次我选择了2款眼霜+2款睫毛膏，试用都在视频里咯~\n好气色Must Buy——Shiseido圣诞限定单品\n准确的说是心机彩妆的一个限定色唇膏——温柔的豆沙色真的非常好看，而且特别滋润~\n再加一个明年1月会出75ml大瓶装红腰子精华，不变的配方加大的容量，价格也很合理，爱用者可以去专柜蹲守了~\n以上就是这次视频的大概内容啦~看完记得点个赞哦~~以及，狗子是不是很可爱！！！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/li3hvF5ss6Zv2PCb3ca1PV79om-v_compress_L1',
    'video_id': '585d5d17faa0522606ff0d8d',
    'title': '#视频教你画底妆#',
    'video_tag_list': '',
    'content': '🎉大家最爱的功能贴又来啦！这次不只是帖子，而是手把手的视频教学哦！\n👆🏻要知道，在一个妆容中，底妆是整个妆容的基石，占据了至关重要的地位，只有底妆质量高，后续上妆的效果才能出来。就像画画一样，只有画布质量高，整幅画才会显得更高级、有质感。\n👆🏻其实一个完整的底妆应该还要包括修容，但今天我打算先focus在foundation，那就让我们开始吧🤗\nProducts used：\n1⃣️Laura Mercier Foundation Primer Hydrating/LM保湿款妆前乳：因为冬天气候干燥，使用一款保湿型妆前乳可以增加粉底的服帖度。\n2⃣️Dior Fix it Color Correct/迪奥瞬效美肌修色棒遮瑕膏：一共四个颜色，因为我角质层比较薄、脸颊有红血丝，所以选择了可以中和泛红的绿色。\n3⃣️Tom Ford Traceless Foundation/TF圆管粉底液 #01 Cream：这款粉底液妆感自然，服帖度比较高，质地也比较滋润，很适合秋冬使用。不用挤太多，少量涂全脸即可～\n👆🏻这里给一个小tip：如果秋冬皮肤干燥、不贴妆，可以用沾湿的海绵蛋代替刷子上妆哦😉\n4⃣️NARS Radiant Creamy Concealer/NARS妆点甜心遮瑕蜜：选择比粉底浅1-2个色号的液态遮瑕、涂在面部需要提亮的地方，这样可以根据#明凸暗凹#的光学原理增加面部的立体度，你们发现没有，将提亮遮瑕图在眼下V区，连泪沟神器都省略啦！买不到pk107的小伙伴大可直接用这个方法哦✨✨✨\n5⃣️MAC Mineralize Concealer/魅可矿物遮瑕 #NW20：再用一款比粉底液深一个色号的遮瑕点涂在用痘印或斑点的地方进行局部遮瑕。\n到这里一个较为完整的底妆就完成啦！你们学会了吗？\n想看修容教学的小伙伴不要着急，我们下次见哈😘\n#化妆教程# #功能贴#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/0e2b800f9850916b216e8aa13aec3d5675f36ecf_v1_ln',
    'video_id': '585dea22d5945f34a829fa0d',
    'title': '🌸内扣BoBo头烫发技巧视频🌸',
    'video_tag_list': '',
    'content': '作为一个爱剪短发的女生来说，每天早上如果让我花很长时间打理头发真的很费时间\n推荐这款👉内扣卷发棒👈我是无意间在某宝上搜到的，没有品牌150多人民币，用了快一年的还在用，真心划算，必须推荐给大家～（其实我已经默默安利的身边不下50个人买了～都说好用）\n我的发质不软不硬180度刚刚好，如果发质偏硬的女生可以调节到200度\n至于左转还是右转的问题，只要你往下拉的时候转头也是往下转的状态就可以了，每个人可能情况会不一样\n这个视频一样对早上没时间打理头发的女生多些帮助～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lniEwjlpG4TDFplg5dC_eQWQC5Ec_compress_L1',
    'video_id': '586113187836230b54c5f73a',
    'title': '【视频来咯】一组腹肌训练的视频来也',
    'video_tag_list': '',
    'content': '录了一组腹肌训练的视频，发现原来只能发五分钟，那么只能分两篇发了，这是平时小公举我都会练的动作，上腹，下腹，侧腹都会练的动作，薯友们，有兴趣可以试试哦，就会拥有完美马甲线了呢，我平时都是负重的，当大家觉得动作越做越没有效果的时候负重便是提升突破的好方法哦。\n还有另一半视频动作会再发一篇，谢谢大家关注与支持'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljpaCjnNZZILWuVYPpbi0TmOYQWj_compress_L1',
    'video_id': '586117e778362311e2312630',
    'title': '【视频来了2】紧接上一篇的腹部训练动作',
    'video_tag_list': '',
    'content': '由于上一篇视频长度不够，分成了两个视频！谢谢支持，由于比较仓促录的比较粗糙，以后会更好的录并带有讲解的😛😛😛'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/ls2JUq1xaD77E-CmNSWVxnNTFnE4_compress_L1',
    'video_id': '58625684b46c5d721b553d76',
    'title': '📢你们要的上肢练习来啦! 💪🏻(含视频)',
    'video_tag_list': '',
    'content': '[扶墙R][扶墙R]\n我又没有按时发...由于前几天在飞机上飞了20多个小时，视频我都忘记录啦！\nOK，言归正传... 这次呢我录了一个需要哑铃的四个动作因为家里没人帮我录啊！！只能去健身房了😂😂😂\n-----开始-----\n1. Arm raise\n2. Shoulder press\n3. Arm row\n4. Reverse W\n-----结束-----\n每个动作做完后休息15-30秒，然后做下一个。我视频里用的重量是5KG，所以如果你刚开始练习的话，我建议你从3KG开始。重量都是可以慢慢增加的嘛，但是动作一定要对哦[飞吻R]\n这算一个循环然后做三个循环。我每天练的上肢训练不止四个动作，我会做8-10个动作，但是由于我不想录个超长视频，让大家觉得无聊，所以就先教给大家四个动作[吧唧R]\n⚠️动作要领：\n1. 做的时候不要耸肩或者肩内扣\n2. 背要直\n3. 两脚之间的距离是肩的宽度\n4. 头往前面看，头要直，不要低头或者仰头太多\n如果你还有什么问题，就留言吧！\nPS: 请问大家下周想看什么呢？🤓\n#哑铃杠铃教学视频[话题]#\n#手臂塑形视频[话题]#\n#肩部塑形视频[话题]#\n#背部塑形视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/4daa6761-ca5a3e7-ad9d-709c2aefd8ed_compress_L1',
    'video_id': '58627a0da9b2ed7880e01e99',
    'title': '前方高污慎入！妹子们不会洗脸的话一定要有一个打泡神器',
    'video_tag_list': '',
    'content': '总而言之，本次安利的就是\n超适合不会打洗面奶泡沫的人\n来点水、做点抽插运动、就能出来白花花软绵绵的泡沫的\n爱丽小屋洗面奶起泡器！\n这东西怎么用有多好用就看视频吧！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/pgc/d8123933-7e94ce9-b8d0-7d8039979b01?sign=0ad22f61d208b417e499488f89a03a76&t=65fb06d4',
    'video_id': '5863139934609467a1cccba0',
    'title': '#零基础化妆教程视频-part2#',
    'video_tag_list': '',
    'content': '之前发过一贴“零基础的化妆视频”，我以为宝宝们学起来很简单，想不到对于新手、菜鸟来说，要学会也不是很容易，感谢宝宝们的留言，让我知道还要把妆容再简化些~\n这次我再简化了化妆步骤，只要几样工具就能画出一个干净清爽，文静甜美的日常出门妆，希望宝宝们能早日学会！！！\n我个人认为这个妆容还是有小心机的，因为不用画眼影，但一定要夹翘睫毛，涂一层睫毛膏，就会有种画了眼线眼睛瞬间放大的假象感，(*^__^*) 嘻嘻……\n这款妆容我用到的是son&park的粉底棒，因为粉底棒遮瑕力会比较高，所以也免去了遮瑕的烦恼，所以如果有小雀斑的女生或者像我一样黑眼圈比较重的女生可以试试用粉底棒打底，如果想要再自然点的妆感，也可以选用稍微遮瑕好点的粉底液或者bb霜。\n这个视频的主要初衷就是简单，但又必须“完美”\nso~大家学起来吧~\n#wi美妆分享#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/7b0aee4b-1ca3a9d-9bd8-5abd521c0b15_compress_L1',
    'video_id': '58671719a9b2ed0a2a9c1986',
    'title': '塞班跳伞视频及全攻略',
    'video_tag_list': '',
    'content': '⚪️高度：4,200米（地面算起）\n⚪️价格；529刀（含拍照）\n⚪️特点:俯瞰塞班岛全景，衣服和鞋无需自备；酒店接送（忘返可以不是同一目的地）\n⚪️可选高度：2,400/3,000/3,600/4,200米\n⚪️预定：塞班跳伞没有官网，一般可以找塞班地接或是某宝报名~\n我在某宝旅行社预定，参加双十一活动，2,149RMB为3,500米的全款，拍照需要当场付现或是刷卡149刀。\n但到了现场你们懂的，被工作人员一顿说服，说越高越舒服blabla，于是乎升了4,200的高度，加拍照共189刀，算下来共3,500不到，还是挺合算。（迪拜跳伞的价格是1,999AED 合人民币3,500左右）毕竟塞班和迪拜都是高消费的地方。跳完等待20分钟左右可以拿到照片和视频的VCD。这里注意想要即时拷出视频和照片的旁友最好自备电脑，因为岛上好多小酒店是没有business center的。这个也可以出行前和酒店沟通好。\n⚪️和迪拜跳伞区别之一\n衣服需要穿准备好的跳伞服，而不能穿自己的，所以没有带很多长袖长裤来岛上的妹纸穿着人字拖和短裙就可以轻松来跳，现场准备的鞋码很齐全。\n⚪️和迪拜区别之二\n迪拜跳伞是跟拍，也就是一个教练串联带你，还有一个教练一起跳下，全程跟拍。这个有利有弊，迪拜跟拍我的教练算是比较成功，关键的景色都抓拍的很到位；塞班的全称是教练拍就会每张照片！！都有教练的胳膊！！不过教练很贴心，真的全方位抓拍。\n⚪️和迪拜的区别之三\n迪拜跳伞的高度只有一个，3,500米，而且是算海拔高度。\n塞班相对来说可以飞的高一些，一般都会从云中坠下。最高自由落体30s。\n⚪️说到底是不是越高越舒服\n这次跳伞完全没有了上次的恐惧感，所以从飞机跃下的一瞬间还是非常的享受。但因为自由落体的时间较长。所以耳朵会有一段时间的不适。工作人员会一直强调如果有耳压就狂咽口水，可宝宝连嘴都合不上[扶墙R][扶墙R][扶墙R]\n在空中盘旋大约15分钟，可以见到很多开小飞机也见不到的景色，也算是不狂此跳了。\n感觉跳伞只是体验，有过一次便会对这种刺激的感觉上瘾，虽说工作人员把跳伞的游客比做教练的背袋，什么都不用自己控制，但对风景的体验和自我的享受是各种项目都无法超越的。\n@小红叔'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsEhXSd94B1P9lFwvmTid8PZNbGU_compress_L1',
    'video_id': '586917d2d5945f430bd0dc04',
    'title': 'CC紫灰色眼妆教程😍✨',
    'video_tag_list': '',
    'content': '⭐️第一次上视频(^O^)，希望快点上真人教学的视频，因为比想像中难，我要练习多几次啊🙈 视频中有眼妆步骤啊！\n⭐️今天尝试化一个紫灰色的眼妆[喜欢] NARS双色眼影#Jardin Perdu，两个色的显色度都好高👍🏻，视频中手臂试色我只涂了两层，左边偏银灰色，右边是中间的紫色带点闪粉色偏光，而两色叠加就是最右边的蓝紫色带点灰[少女心]\n⭐️Nars的眼影粉质很细而且不会飞粉，持久度比stila高，真的好用😍！而这个双色眼影偏闪光真的特别美，实物更美[飞吻R]！推荐白皮👍🏻，黄皮可以试其他色号！这个色比较没那么日常，但如果看厌了大地色或橘粉色的宝宝们不防一试啊！[得意] @美妆薯'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/e4e0e3e164d6c0fd0d53af2c4e1c9314f6a0781e_r_ln',
    'video_id': '586cfc30b46c5d6210ed251f',
    'title': '🏃🏻\u200d♀️在家就能练肩背😉（含视频）',
    'video_tag_list': '',
    'content': '上一周呢我发了一个上肢的哑铃练习，但是考虑到好多小🍠好像都比较喜欢看我在家就可以做的练习。那这次呢，我就录了一个没事晚上在家都可以做的练习\n-----开始-----\n1. T (20次）\n2. Y (20次）\n3. W (20次）\n4. Circle (20次）\n-----结束-----\n⚠️\n1. 头微微抬起，离地面1拳或者2拳的距离\n2. 头不要上仰太多，头跟身体垂直\n2. 脚尖朝地，不需抬起\n3. 在做的时候，手臂不要碰到地面\n这四个动作每个20次，做完一个接着做下一个，中间不要休息。做完四个动作算一个循环，然后休息1分钟。一共做3组。如果一开始觉得很累，20个做不下来，那就减少到15个或者10个。 慢慢来增加数量 [赞R]\n如果你还有什么问题，那就留言提问吧[萌萌哒R]\n#无器械锻炼视频[话题]#\n#手臂塑形视频[话题]#\n#肩部塑形视频[话题]#\n#背部塑形视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsSREBZGmH2wZMld29F233WWBJdT_compress_L1',
    'video_id': '586ddd48d1d3b975d62a16e4',
    'title': '🦌新年第一天——奈良之旅🦌',
    'video_tag_list': '',
    'content': '🦌hi，大发肥来啦～前两天手机罢工，今天终于拿到新手机了，火速吧视频po上来分享～[害羞R][害羞R][害羞R]\n🦌奈良的小鹿好可爱哦，贪吃鬼！[飞吻R][飞吻R][飞吻R]'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/pgc/6267958a-f0f005d-8b45-ccba1bbc39a2_compress_L1',
    'video_id': '586de1a1a9b2ed03d0c636ed',
    'title': '拍个视频告诉你3000块的限量版戴森吹风机值不值得买',
    'video_tag_list': '',
    'content': '不知道有多少妹子跟我一样，长年累月的用着同一款吹风机，明明它很重很吵，吹的时间长了还会有一股糊味儿，可是好像换个别的也是大同小异。\n跟群里的宝宝们讨论了很久，总结了传统吹风机的几大问题，看看你们家的有没有中招？\n1、丑。。\n2、功率不够，又长又厚的头发要吹半小时真的不能忍\n3、声音大到作死\n4、吹后脑勺和头顶真是累\n5、一不小心又烫到头皮，吹完头发跟稻草一样\n6、有诡异的焦糊味\n7、部分设计功能有缺陷\n如果你的吹风机跟我的一样，那就真的可以考虑换掉啦！话说3000块买个吹风机真的有点贵，可是真的好用啊，就当投资了嘛~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lualOZeFsRT0wyNDOcVmgFVHQ96z_compress_L1',
    'video_id': '586e3481d2c8a561b5ba6a1a',
    'title': '🦌说好的吃货呢——被小鹿嫌弃了🦌',
    'video_tag_list': '',
    'content': '🦌之前明明吃的好开心[哭惹R]说不理人就不理[扶墙R][扶墙R][扶墙R][扶墙R]'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/lpq-mAnKoff8FQJxSjgvAyxGBXt2?sign=e402e74011b9ff0d9844208270f750ce&t=65fb06d4',
    'video_id': '58705d5fd2c8a543729778ef',
    'title': '【五分钟的好气色妆容】懒人妙招 手把手教你完成速效甜美元气妆',
    'video_tag_list': '',
    'content': '出门要迟到了怎么办？短期出行我化什么妆？没时间化妆也要美美的出门～然而没有气色的脸颊会让妆容大打折扣 今天分享一款好气色妆容 甜美的同时元气度UP 五分钟即可搞定！\n【底妆】\n隔离液—兰芝 紫瓶隔离液\n提亮液—VDL 提亮液\n气垫bb—YSL气垫bb#10\n【眉毛】\n眉笔—爱丽小屋 双头旋转眉笔#03\n染眉膏—爱丽小屋 染眉膏#3\n【眼妆】\n眼影—TOMFORD 双层眼影膏#03 Golden Peach\n眼线—3CE 棕色眼线笔\n睫毛夹—SUQQU\n睫毛膏—KISS ME\n【腮红】\n腮红—NARS 深喉\n腮红刷—NARS 歌舞伎藤腮红刷\n【唇妆】\n唇釉—ARMANI 红管#401\n-\n第一次录视频啰哩啰嗦hin多地方拍的不到位 你们能看懂且喜欢就好啦！[喜欢]'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/FmhVwVskOwrgpBBhBtnRN3smfYhI?sign=6ea3f0522e3a84f5dbf887a81bbf1a29&t=65fb06d4',
    'video_id': '587095e078362342a123df7c',
    'title': '毛利猫走平衡木',
    'video_tag_list': '宠物技能大赛',
    'content': '毛利猫新技能get！！🐈\n难度系数1.0，无托马斯全旋，无分腿侧空翻…\n下雨天的周末愉快！[讨厌]\n老视频参与本期新话题[得意]\n#我和宠物的日常[话题]##宠物技能大赛[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljAVS8CrZwCRPnXm2McX85jIh9-J_compress_L1',
    'video_id': '5871ed3eb46c5d2f374520c5',
    'title': '肉丸阿姨2017首支爱用品视频',
    'video_tag_list': '',
    'content': '啊哈哈哈！因为烫了失败的爆炸头于是绑了这个村村的肉丸头。\n大家不要嫌弃我哈！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpAMawX0elterd2Uc43N-M5eyjiW_compress_L1',
    'video_id': '5871edec7836237c9e23df7c',
    'title': '你的包里有什么？',
    'video_tag_list': '',
    'content': '啊哈哈哈！！\n妈妈再也不用担心我选不到封面了～\n你们平时出门都会带些什么呢？！\n今天我就来分享我包里的小咪咪～🤘🏻✨\n#晒包赢红包#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lqO75dYmwAznjgwGjQ_Qv2CaNGEb_compress_L1',
    'video_id': '5872134cd1d3b9684cee02d1',
    'title': '宝贝🐱🐱NEW YEAR大餐：大龙虾 这伙食不错',
    'video_tag_list': '',
    'content': '我家猫咪小公举们遇到我们这种产屎官也是很无奈的，\n我们把吃剩的龙虾壳拿给他们玩，都表示很好奇😝😝😝\n为了吸引她们靠近 我放了小零食在龙虾周围和背上，她们竟然都不敢去吃，后来可能发现没什么危险才敢靠近哈哈。\n顺便请教下资深的铲屎官们 猫咪平时除了网上购买的粮食罐头零食，可以给她们吃蒸鱼蒸虾吗？\n#家有小主#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrU8tGCViyhmk48FKz41yVqzhW6T_compress_L1',
    'video_id': '58739db7d5945f032cb8b1f2',
    'title': '乐感一级棒🤘🏻',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lnv61yibdFGnncPtQ9-pWDopcPxI_compress_L1',
    'video_id': '5873a342b46c5d748b2ccc40',
    'title': '#化妆教程# 冬日元气桃花妆',
    'video_tag_list': '单眼皮如何画眼妆',
    'content': 'Candice苏妹儿的#化妆教程视频#又来啦！\n💕这次是偏韩系的桃花妆，省去了复杂的修容的步骤，15分钟内就可以完成，简单易学，很适合新手入门哦～颜色也是粉嫩粉嫩的，那就让我们一起给这个沉闷的冬天带来一抹活泼的生气吧！\n1⃣️妆前：我用Becca液体高光Pearl代替了妆前乳，涂抹在面部中间区域，给肌肤提亮又增加了一些保湿度\n2⃣️Dior DreamSkin梦幻美肌修颜气垫粉底，因为我冬天皮肤很干，这款气垫很保湿并且含有护肤成分，所以不会不贴妆或浮粉哦，缺点就是几乎不带遮瑕度\n3⃣️MAC单色眼影Wedge修鼻影，绝对的鼻影神器！带一点灰调的哑光棕色，非常适合做鼻影修容，效果干净又自然\n4⃣️眉毛部分我最近发现了一款#画眉神器#：璐比眉章Lubi，有三款眉形可以选择，自然眉，韩式眉，平直眉，大家可以根据当天的妆容来选择用哪一对印章，直接按一按就上色啦，几秒钟就可以画完一支眉毛，非常适合新手，如果追求完美可以像我一样再拿眉梳扫一扫👀\n5⃣️Bbia眼影笔，色号w4，粉玫瑰色，涂抹在眼皮上再用手指晕开；The Seam得鲜眼线胶笔，酒红色，画的粗一点哦😉\n6⃣️把睫毛夹翘，再涂上美宝莲紫胖子防水睫毛膏，真爱！用了一大把，相信一直follow我的小伙伴已经看它一遍又一遍了🤣\n7⃣️Clinique倩碧小雏菊腮红04 Plum Pop，很鲜艳有活力的泡泡糖粉色，细看带微闪、上脸后就不明显啦～哦对了，小雏菊的显色度蛮高的，下手可以轻一些哦😘\n8⃣️3ce唇膏#601，超级超级艳丽的玫红色，感觉这种色只有韩国品牌能做出来哈哈，涂抹在嘴唇中间，再用手指向外侧晕开💋\n妆容完成！你们学会了嘛🎉🎉\n喜欢就关注我吧，会不断出新视频哒😘\n#单眼皮如何画眼妆[话题]##眼妆每日打卡[话题]##日常妆容打卡[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpqONuYTZzUJoZh5aQTRbC-PZoCu_compress_L1',
    'video_id': '5876ead4d2c8a5384dd810ad',
    'title': '三分钟换4种风格，只靠换配饰口红和发型',
    'video_tag_list': '',
    'content': '啦啦啦，好久没发视频了，这次来挑战三分钟换4种风格，只需要换个口红、配饰和发型，不同的风格就出来啦～快评论留下你最喜欢的一个look[得意]爱你们'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrLN9GSKr75BOhRxGslrRI5EP3zO_compress_L1',
    'video_id': '5876ed07d2c8a53b05d810af',
    'title': '2016定下的小目标，我都完成了吗？',
    'video_tag_list': '',
    'content': '在2017年的第一个月，我决定把我2016年第一个月定下的小目标拿出来溜溜，顺带溜溜男朋友，哈哈哈哈哈哈哈哈哈全程是笑点………请尽情观赏'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpHYylnjeZ36Ql6f9YvOZUx8nwQK_compress_L1',
    'video_id': '587886837836235bc20610ac',
    'title': '有好歌听的一天🎧',
    'video_tag_list': '',
    'content': 'The XX真的是四年不发歌 发歌听四年。心情大好的一天，Pico也喜欢的曲风[装酷]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/b8c2c7e6-a668da8-9eb6-c69c86c48974_compress_L1',
    'video_id': '587a3b13a9b2ed4637d95843',
    'title': '我化妆关你什么事啊？？？',
    'video_tag_list': '',
    'content': '爱化妆的美少女肯定或多或少都遇到我视频里拍的这些人，拜托我化个妆关你什么事，唧唧歪歪的酸我们还不如赶紧去原地爆炸吧！～爱美无罪，化妆有理，好看的小姐姐们要雄起～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lod2g1IDfbOvE54pJaG0heAvQHXW_compress_L1',
    'video_id': '587a773114de414b5a37f8a2',
    'title': '【视频】8支MAC秋冬口红试色',
    'video_tag_list': '',
    'content': '之前的被封了重新发～\n吃土色、姨妈色、豆沙色、脏橘色都有啦～\n布光不是很有经验所以整体拍出来感觉颜色都有些偏亮和偏暖…实物在自然光下的颜色会更暗一些\n当然每个人唇色、肤色、光线、拍摄设备和显示器不同，所以我的试色不可能跟你一模一样，还请大家仅供参考，理智种草哦'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljLWGw2WPvcPGH2YdYJBt-Y54lPU_compress_L1',
    'video_id': '587b8504d1d3b9482d770810',
    'title': '让你画个卧蚕不是白带啦！',
    'video_tag_list': '',
    'content': '妹子们醒醒，卧蚕微微提亮就好了！请不要拿死白的颜色画两条白带在眼底好嘛[害怕][害怕][害怕]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lruCCDMeCWCiqdPCe9yzwf5N2_ZR_compress_L1',
    'video_id': '587ce667d5945f5314192aec',
    'title': '创意中国风口红试色💄💋💄',
    'video_tag_list': '',
    'content': '有着浓浓武侠情结的我，这次将武侠风格融入到整体造型中。灵感来源于林青霞版的东方不败，哈哈。这样的中国风你们喜欢吗？\n来说说视频中出现的羽西虫草焕颜唇膏笔，上色效果非常好！有虫草精粹配方，所以不会很干，挺滋润的，秋冬用也是ok的啦！哈哈，尖头的唇膏设计，对于画各种唇线也非常方便。\n🌟朱砂红：这个颜色是我最喜欢的，颜色非常正的大红色！超超超级美啊！感觉这个唇色搭配什么妆容和发型都立马很大牌范儿。而且很神奇的是显皮肤白呢！\n🌟品红：个人感觉介于粉红色和玫红色之间，很清纯很活泼的一种颜色。搭配时装也很不错，开春穿个小裙子配这个唇色非常青春啊！哈哈\n🌟珊瑚红：有点橘红色的感觉，这个颜色我也很喜欢，不像朱砂红那么有气场，更多了一份妩媚的感觉。显肤色白皙，气色会很好，可用的场合也挺多的！\n拍摄剪辑不易，欢迎大家点赞收藏，支持原创，么么哒。 @小红叔'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/4e21b859af2046f0797085e087f1f4f0b4e9e528_r_ln',
    'video_id': '587e14327836233fa11b8b85',
    'title': '眼膜才不是鸡肋！冬天不长干纹全靠它！（下）',
    'video_tag_list': '',
    'content': 'too cool for school摇滚华丽蕾丝眼膜\n外观：❤❤❤❤\n很酷炫的夜礼服假面面具式设计，上面还有蕾丝花纹，上脸效果蛮带感的。\n便利度：❤❤❤\nQQ的果冻凝胶膜被折叠包裹在两层塑料垫纸中间，拿出来的时候精华液有点滴落，不太好上脸。\n服帖度：❤❤❤❤❤\n意外的服帖度很好，而且沉甸甸的挺有分量感。从眉毛上端一直延伸到苹果肌上端，两侧延伸到太阳穴位置，包裹的面积非常大。连鼻梁处都可以贴的很紧密。\n功效和持久度：❤❤❤\n满足了最基本的补水效果，但是并没有觉得特别给力，同样效果维持在大约2小时。\n总体评价：❤❤❤❤\n设计外观上迎合了少女心们的搞怪心理~跟艺妓面膜异曲同工了。精华液不算多，所以不建议超时使用。没有什么的味道，有分量感的膜体能给眼部一定的正压舒缓功效。同样只能躺着做，是最适合敷眼膜无聊时自拍的道具款眼膜。\nDHC水嫩眼膜\n外观：❤❤❤\n包装盒和单片包装一模一样中规中矩，真空包装，撕开后是很老实的两片凝胶眼膜。\n便利度：❤❤❤❤❤\n没有精华液的黏贴使用，所以无论何时都能贴上直接用，包括妆面上也可以直接使用。不影响活动，可以戴眼镜，也可以贴着睡觉。\n服帖度：❤❤❤❤❤\n高分子凝胶层撕拉的时候不会拉扯到皮肤，所以贴上去以后可以随意更改位置。因为是黏性贴合的，所以不存在气泡或者不贴合的现象。\n功效和持久度：❤❤\n改善干纹的效果一般，冰凉的使用感倒是很好地帮助消除水肿。功效持久度在1小时左右。\n总体评价：❤❤❤\n就像是便利贴一般的眼膜，贴上去以后完全不影响正常的活动。贴了15分钟后，原本有0.5mm左右厚度的凝胶层会慢慢变薄。原本疲惫干涩的眼睛得到舒缓，没有肿胀感。但是细纹什么的过一会儿还是跑出来了。比较适合喜欢方便的人使用，或者午休后来一帖醒醒神去去肿也不错。\n天气一冷就不想敷面膜，这个可以理解，但是天气一冷一干，眼周问题真的就层出不穷。所以别再觉得眼膜是鸡肋啦，好好爱护眼周肌肤吧~毕竟爱是做出来嘛！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/1e94ce2fa73db4eaa5380cba2c6f3e8ccb4a6519_v1_ln',
    'video_id': '587ee89e78362362df1b8b84',
    'title': '关于修容！',
    'video_tag_list': '',
    'content': '今天跟大家分享我平时的修容技巧和比较喜欢用的修容产品哦～\n修容棒是爱丽小屋的Play 101\n#彩妆##修容#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lihGEa78EykmhV2UbYA0Y6PuDKUV_compress_L1',
    'video_id': '587f22acb46c5d6a3928f6ef',
    'title': '青椒素肉丝—素食照样吃出肉味来！秘诀就在这里',
    'video_tag_list': '',
    'content': '关注FateVegetarian，第一时间观看更多视频.'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lvqpKXHiocQ7zRXP65LzdTN6jjAC_compress_L1',
    'video_id': '58802f8614de410b9ff249f9',
    'title': '13支豆沙色系唇膏试色分享：ysl214，cpb唇釉13号等',
    'video_tag_list': '',
    'content': "💋继之前好评如潮的【16支YSL唇膏试色视频】之后，Candice苏妹儿的又一大波干货分享来啦！\n✨这次的视频是我手头的13支裸色系 - 豆沙色系的唇膏试色，包括cpb黑管唇釉13号，ysl214，kvd double dare，lolita II等…\n✨我个人最爱的就是【裸色系】和【红色系】唇膏，而豆沙色系则是裸色系的一个分支，姨妈色也属红色系。\n✨在整理这期口红试色视频之前自己都没想到原来我有这么多豆沙色系的💄，本来只做了12支，但是发现其实Charlotte Tilbury的Walk of Shame也算是深豆沙色，只不过它偏砖红色调。好啦，那就让我一一的给大家介绍这些口红吧！\n1⃣️NARS唇笔Rikugien：Satin质地，带一点微微珠光感的裸粉色，很温柔，最重要的是，这么裸的粉色竟然不！显！黑！个人觉得只要皮肤不是很黄很暗沉都能驾驭。\n2⃣️Rimmel唇膏NO.705 Let's Get Naked：带粉色调的裸色，比Rikugien更裸，这支唇膏比较挑肤色，如果不是很白会容易显黑，但是它涂上会有种欧美风的性感😉\n3⃣️Make Up For Ever NO.N9，带橘调的豆沙色，hin好看，非常百搭可以搭配任何妆容，很显气质而且不挑肤色，是之前美国丝芙兰送我的，国内专柜不知道能不能买到。\n4⃣️Armani红管唇膏NO.201： 棕调裸色，超级显气质，有种白领的成熟美，只要不是很黄的皮肤都可以驾驭，有种女王范儿，我涂这支口红出门总被问✌️\n5⃣️CPB黑管唇釉 NO.13：亮亮的粉玫瑰豆沙色，质地和其他口红不一样，有点像唇彩的赶脚，滑滑的亮亮的，滋润度很高，这个颜色比较活泼，个人认为春夏天使用会更美哦\n6⃣️Givenchy纪梵希小羊皮唇膏NO.105：这一系列里我个人最爱的一支！！！冷调/蓝调玫瑰豆沙色，质地很黄油很像厚重而滋润，持久度也蛮高的，颜色超级好看，因为颜色是冷色调所以非常显人白，涂上它自拍怎么拍怎么美，这一支都快被我用完了！\n7⃣️Givenchy纪梵希小羊皮唇膏NO.104：土橘棕色，104和105是我在小羊皮系列中最爱的两支，104比105颜色更棕、还带一点橘色调，白皮和健康肤色涂上都超级美，很适合上班、面试、见家长涂！当然平时出去逛街也木有问题的啦🤗\n8⃣️YSL方管哑光唇膏NO.214：暖调玫瑰豆沙色，又称蔷薇木色，这个颜色超级抢手，火的一塌糊涂，确实很美，涂上后整个人都变温柔了🙈个人认为ysl的方管哑光系列比之前的Rouge Pur Couture出的颜色更美更有质感！\n9⃣️MAC See Sheer：是我比较早期入的MAC唇膏，之前还没火起来…很多人都说see sheer是豆沙色，我感觉它更像蜜桃色，satin质地，有一点微微的光泽感，很百搭，春夏天画个蜜桃妆超级活泼可爱😉\n🔟Bobbi Brown Sheer Lip Color NO.10 Carolina：冷调烟熏玫瑰豆沙色，也是我超爱超爱的一支！比其他裸豆沙色要稍微深一点，但却被sheer的质地中和了，涂上嘴一点都不深，有气质又显白，白皮黄皮都能完美驾驭，是属于把人变得更美更好的那种颜色！使用率hin高^_^\n1⃣️1⃣️Kat Von D唇釉Double Dare：哑光玫瑰豆沙色，刚涂上是有一点点亮的，过不到1分钟就变哑光质地，非常持久有点像油漆的赶脚😂，有一点点挑肤色不过只要不是很黄就还好\n1⃣️2⃣️Kat Von D唇釉Lolita II：土橘棕色，和DD有点像但是更橘一点，比dd挑肤色，更适合白皮，或者小麦肤色😉\n🎉彩蛋🎉\n1⃣️3⃣️Charlotte Tilbury Walk of Shame：这支红透半边天的唇膏就不用我多说了，包装美、质地好，虽然这一系列叫复古哑光唇膏，但其实一点也不干，颜色更是美死！超级显白，而且有气质！非常适合秋冬使用，配上个大衣和围巾，嘴唇映衬的美出天际👄\n感谢大家的收看，希望对你们有帮助哦😘"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/0cbc366c-9fbda79-a4db-1bb785f70ade_compress_L1',
    'video_id': '58818359a9b2ed48b5a8fc9d',
    'title': '按摩大法好，靠人不如靠自己！舒适减压自己在家也能做~',
    'video_tag_list': '',
    'content': '哎哟~我可以发小视频啦！！！！哇啦啦~我可以开始跟大家唠唠叨叨啦！恩~一年前去泰国回来录的片子，当时买了那么多精油最推荐还是这个Panpuri的按摩套装。\n约莫着今年新年又会有大批泰国党要刷碧海蓝天，一生推给大家咯！去都去了，还是不要错过！\n工作以来一直是对着电脑的工作，肩颈劳损的问题也逃不了！除了工作间的放松外，回到家也可以试试这样的按摩方式，非常舒服减压。\n第一条片子，过年期间会有个送福利的帖子，这几天就会出了！大家过年记得来玩哦~！恩！没错！送！福！利！\n喂喂第一条视频诶！此处是不是应该有掌声~~'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lqtmDWXN02UHMbtJHN92L5ZXBTr8_compress_L1',
    'video_id': '58818c7ad1d3b9630f1badc2',
    'title': '米其林三星主厨推荐：凉拌荷兰豆',
    'video_tag_list': '',
    'content': '肉食者的素食主义'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loSUElp09HELgv37SzHNWFy2XLFp_compress_L1',
    'video_id': '5882037ed5945f458738221f',
    'title': '最爱最减龄的三个发型分享～',
    'video_tag_list': '',
    'content': '哈哈哈！！\n分享三个我平时最爱的发型，\n也是被人问得最多哒哈哈哈～\n都非常简单好学🎉✨\n忘记拍封面了～太难选啊哈哈哈\n希望大家会喜欢！\n小年快乐～么么哒❤️🎉'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luvAlRYdau7zPxekVDKPf0jsUL6w_compress_L1',
    'video_id': '5882d6b0d1d3b95f0293c696',
    'title': '✨去首尔一定要感受的夜文化',
    'video_tag_list': '',
    'content': '每天逛到好晚\n估计因为时差缺一点也不困\n周末朋友带着去club\n说一定要去感受一下\n因为和国内的真的不一样\n国内的我就只去过北京五道口的一个小的学生玩的\n所以…… 我我就说说朋友跟我说的对比\n大概就是氛围比较好\n没有很乱，收费也比较合理\n主要玩的都是年轻人\n💓弘大附近也有很多club真的都是学生\n一两万韩币的门票，一杯酒免费\n💓江南附近的档次高一些，\n朋友说区别就是装修好一些，歌好听一些\n但也没有很贵，我们去的也就三万韩币门票\n本来昨天没打算去的\n我就穿着我的长裙…… 去了夜店\n不过居然在夜店看见好多妹子都穿长裙\n我就放心了，哈哈哈\n对了，首尔真的木有韩剧里的欧巴\n这是来首尔唯一的失望………\n男生我以为也都是180➕😂😂😂\n以为全是韩剧里的欧巴\n不过韩国人确实比较会穿衣服\n脸一般会穿衣服也加分啦\n所以朋友一定要带我去club\n说帅哥多\n不过确实是来首尔这么多天\n看见最多帅哥的地方了\n妹子们打扮也没有很妖艳\n很多穿运动鞋的\n韩国人的音乐细胞加舞蹈细胞真的是满满的\n感觉每个人都好会跳😂😂😂\n而且出门就可以打车🚖\n车也很多\n非常的方便\n我去的这个地方叫：\n🌸OCTAGON 🌸\n不定期会换一些DJ\n音乐基本都是英文歌\n我还蛮想听韩文的😂😂😂\n韩国的唱歌房也是个神奇的地方……\n下次有机会再给大家写😂\n#用视频记录旅行[话题]##舞蹈教学视频[话题]##带着小红书去旅行[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lt_L2ADPMfBqgp9CbtiekMhtAWk9_compress_L1',
    'video_id': '5882d6fbd5945f550dd112f8',
    'title': '今年过节不送礼？别开玩笑了！',
    'video_tag_list': '',
    'content': '又到了一年一度回家探亲的节日（啊呸，我这个每个月都回家的人过年跟平时有什么区别），然而在各种环境的影响下，已经工作的妹子们犒劳一下家里人给钱是应该的，送礼物就是表达妹子们心意的时候啦～来看看我这次过年回家给家里人准备了什么礼物吧！（心疼钱包，瘦得真快………………and我家里人都是很朴实的人，所以我都没买很贵的东西[不满]兰蔻那个油还是别人给我的………'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/cd85c6f554722b5e2d54bf8f6316c6bd009caf8e_v1_ln',
    'video_id': '5882d95cd1d3b963f27afaa3',
    'title': '意大利面只要这几样食材，立马变得美味！',
    'video_tag_list': '',
    'content': '★★★★★\nFateVegetarian\nMenu\n面食是很多人喜爱吃的，面食吃的时候，对身体没有太多影响，面食很容易消化，不过在吃面食前，需要注意对它制作进行了解。\n不同面食制作方式不一样的，意大利空心面的做法如何呢，这样的面食制作也不是很复杂，下面就详细的介绍下。\n★★★★★\n创意指数\n意大利肉酱面\n▼\n意大利肉酱面\n·食材·\n空心面、肉末、洋葱、番茄酱、黄油\n橄榄油、糖、盐、芝士粉、蒜末、黑胡椒\n✤ · ✤ · ✤\n①洋葱切片\n②蒜切末\n③空心面煮8分钟\n④沥干水分\n⑤爆香蒜末\n⑥加入肉末翻炒\n⑦倒入番茄酱\n⑧倒入糖\n⑨黄油加热，加热空心面，加少许盐\n⑩倒入肉酱\n⑪撒上芝士粉\n⑫意大利肉酱面就完成啦~！'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/FgBi2NUpzcj4Tjo_J5hq17pinGf4_compress_L1',
    'video_id': '5884268214de414f61e7d07b',
    'title': '【论女生力量训练的重要性】',
    'video_tag_list': '',
    'content': '不足为奇的是很多女生平日都会问:\n该怎么练，腰能细一点？肚子能小一点？\n请问怎么减腹部脂肪？\n请问马甲线怎么练的？\n我跑步腿会变粗吗？我腿粗不敢跑步啊。\n我就是胳膊有点粗，胳膊能细点就好了，其他都不用练。\n😔但几乎没有女生提及: 如何增加上肢力量,这类的问题。（完完全全彻彻底底的没有‼️）\n很多人想当然的以为力量训练就是增肌，会长出夸张的肌肉，尤其女生，一提到力量训练就避而远之、逃之夭夭，唯恐自己长出那些满身的夸张肌肉。一想到减肥，就会第一时间想到跑步加节食。没错，有氧确实是减脂的方法，但绝不是唯一的方法。以现在主流的审美来看，女生，你不光要瘦，还要有身体的肌肉线条，四肢紧致最好能有些许肌肉线条，腰腹木有赘肉最好能有马甲线（🤘🏻我对自己的要求永远是坐着和侧躺的时候肚子也必须是平的！）前凸后翘，该瘦的地方瘦，该有肉的地方有肉。（尼玛，这社会当女银真心不容易呀🙃）力量感不光是会让男人充满阳刚气，也会让女生浑身上下散发魅力。\n👀那么问题来了：👩女生为啥也要做力量训练？\n之前有一句话，叫认真的女人最美丽，而我想说，认真运动的女人最美丽！欧耶✌️\n没错，知道为什么吗？因为现如今早已经不是古代的吃不饱阶段了，只有古代社会在食品缺乏的社会大环境下，以胖为美、富态被认为是家里条件不错，营养摄取丰富，那绝对是大户人家呀。社会永远是这样， 稀有的才会珍贵。如今，庞大的胖子数量直接反映食物的丰富程度。而想要瘦，却变得没那么容易，你得时刻跟自己的懒惰和欲望做斗争。想要练成马甲线人鱼线，你还得吃的科学、练的系统。恩，管理自己比领导他人要难的多。你们说，这样的男银女银，不值得敬佩吗？\n👀女生练力量，有啥用？\n1.提高基础代谢，体型更好看！\n拥有更多的肌肉量就意味着你有更快的基础代谢，每磅额外增加的肌肉可以增加50—100大卡的基代。增加力量训练提高肌肉含量，让你在除了训练日之外的日常里，坐着也能瘦哦。\n2.更年轻、更健康、更好的状态！\n还有很多妹子担心，长出那种粗壮的手臂和大腿，但是，现在早已得出结论：虽然在肌肉体积和力量之间确实存在一定关系，但是力量的增长也可以在没有肥大的肌肉中产生。例子请看那些瑜伽空手倒立高手，各个力量惊人，但是肌肉体积并不夸张。而且，最重要的一点，肌肉生长在**酮的刺激下会效果显著，但是女性的**酮含量，你懂的。So，你以为想长肌肉那么EASY？\n所以你还认为上肢力量并不重要，可有可无，那我这里肯定的告诉你：“NO”！好的上肢力量将会为你插上一对翅膀。👼'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loex7Zo2oslGS-GczSmA59F8KSp7_compress_L1',
    'video_id': '5884513db46c5d22bb02f014',
    'title': '化了这个乖巧妆，拜年人见人爱红包速来',
    'video_tag_list': '',
    'content': '每逢过节倍烦恼，到底要画个啥妆七大姑八大姨们才能满意呢？答案就在清透装嫩这四个字。不要浓不要浓不要浓，记得了吗？好吧话不多说详情看视频吧[得意]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/eb93696a75602b83543445f01f1f4341fe4e9c1f_v1_ln',
    'video_id': '58846f43d2c8a522627f61fa',
    'title': '💂🏻\u200d♀️首尔旅行攻略---你一定要去感受的弘大夜生活',
    'video_tag_list': '用视频记录旅行;韩国;首尔',
    'content': '弘大附近有很多逛街的衣服店\n如果懒得去东大门淘货的话\n弘大是一个不错的选择\n因为东大门真的需要很强的耐心和体力\n弘大这里的衣服有些也是东大门买不到的\n东大门也没有很便宜\n所以DG们真的是良心价\n➕➕➕➕➕➕➕➕➕➕\n👉🏻女生衣服买买买路线\n在弘大的地铁站附近就开始导航搜stylenanda弘大店\n然后跟着导航走\n一路上有很多可以逛的小店\n衣服，饰品什么的\n还有一些不错的咖啡馆\n这些都需要你一一去发掘\ncafe de paris 也在這條路上\n可以順便去拔草\nStylenanda對面就是CHUU\n负一楼是内衣\n其实这些店里的衣服也会选得眼花缭乱\n建议大家官网选好之后店里试穿这样\n感觉现在还是习惯网上买衣服😂\n不然就是网上选好店里买\n不然真的不知道买什么………\n➕➕➕➕➕➕➕➕➕➕➕\n👉🏻弘大夜文化一条街\n从弘大地铁站出来后往stylenanda走\n走到第一个转盘右转\n这里晚上很多人跳舞\n唱歌这样\n小哥哥们都还可爱 哈哈哈\n虽然脸一般\n但是跳起舞来\n帅帅帅\n妹子们真的是不怕冷……\n光腿……光腿………\n听朋友说有时候练习生们也会来这样演出\n弘大基本每天人都很多\n特别是周末的时候\n一定要来逛逛\n弥补自己平时在大街上没看见韩剧里欧巴的❤️\n在弘大附近吃饭也是要做了检查ID的\n不满19岁不可以喝酒，不可以进Club\n所以大家出门记得带好ID\n（旅游的就是带护照就好啦）\n早上五点钟\n弘大附近都还是一堆人……\n韩国人真大是能喝、能玩、能跳😂😂😂\n#用视频记录旅行[话题]##舞蹈教学视频[话题]##带着小红书去旅行[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/6f3a051da1b5f76b3d74d36ad0d49443fb9fba53_v1_ln',
    'video_id': '5885778bb46c5d28a9a5c264',
    'title': '麻婆豆腐—美味诀窍大揭秘！',
    'video_tag_list': '',
    'content': '★★★\nFateVegetarian\nMenu\n麻婆豆腐（英文名：Mapo Tofu）也称为陈麻婆豆腐，是四川省地方传统名菜之一。\n麻婆豆腐外观色深红亮，红白绿相衬，豆腐形整不烂，吃起来具有麻、辣、烫、嫩、酥、香、鲜等风味。\n★★★\n创意指数\n麻婆豆腐\n▼\n麻婆豆腐\n·食材·\n韧豆腐、豆瓣酱\n花椒、蒜、姜、葱\n生抽、糖、盐、生粉、花椒粉\n✤ ·\xa0✤ ·\xa0✤\n①\xa0豆腐切块\n②豆腐浸泡10分钟\n③放入姜蒜、花椒、豆瓣酱煸炒\n④加入水\n⑤等沸腾倒入豆腐\n⑥撒入盐、糖、生抽\n⑦勾芡\n⑧撒入花椒粉、葱花\n⑨快来征服你的味蕾吧~！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ls1GIG7hjQl3mo30_k57F4su0Vqe_compress_L1',
    'video_id': '5885f090d5945f36fa6bdc6a',
    'title': '一大波面膜袭来请接好哈！',
    'video_tag_list': '',
    'content': '前几周刚做完果酸需要天天来一记面膜补水，所以囤了一大堆面膜，就来一个个数这些面膜我都打几分吧！有更好用的也可以安利给我！[得意]'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/FmpJ8e4x0Oma1SNsa-vEn1MsjU14?sign=da183913dd9fa242e49e0160abe19623&t=65fb06d4',
    'video_id': '5887074114de417d195a347e',
    'title': '❣️Sonny Angel 👼宝宝们',
    'video_tag_list': '',
    'content': '看了就心情好的天使宝宝们～\n话不多说 看视频'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lm_-JZzfIBPN5jBjqzvx9WHhbyaE_compress_L1',
    'video_id': '5888386efaa0524895a5b559',
    'title': '一把勺子就能学会做元宝—上海蛋饺',
    'video_tag_list': '',
    'content': '★★★★★\nFateVegetarian\nMenu\n上海人过年.必吃的金元宝----蛋饺~\n有着老一辈传统影子的美食~寓意年年捧着金元宝~招财捞金~\n★★★★★\n创意指数\n上海蛋饺\n▼\n·食材·\n鸡蛋、肉末、猪油\n姜、葱、酒、生抽\n✤ · ✤ · ✤\n①切葱花\n②切姜末\n③鸡蛋打匀\n④肉末放入酒、生抽、盐、葱姜末，抓匀\n⑤猪油均匀涂抹\n⑥倒入鸡蛋液\n⑦放入肉末\n⑧蛋皮微微上翘，用筷子均匀翻压\n⑨美味的蛋饺上桌啦！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loWh6icqbjQkBPJfj401mjOzT1oA_compress_L1',
    'video_id': '588858b0d5945f468ae27045',
    'title': '秃子的自救方法-发际线阴影笔！',
    'video_tag_list': '',
    'content': '笑什么笑！脱发嘛中年人总会有的哼唧！面对越来越光的额头，我不得不拿出一个宝贝，客官来根发际线笔吗[得意]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg8PtpTsoud1Hnr2D8iOpeS4rQtB_compress_L1',
    'video_id': '5888b17afaa0526345fcfb70',
    'title': '',
    'video_tag_list': '',
    'content': '给宝宝用牙线的正确姿势\n1、宝宝面朝上平躺\n2、成年人坐下，让宝宝的头处于你的两腿间\n3、有必要的话，利用两腿夹住宝宝。当然切勿强制按住，以免产生逆反心理。\n4、用牙线清理\n5、用牙刷刷\n6、用温水漱口\n至于多大的孩子可以让他们自己刷牙，目前我家5岁的哥哥早晨自己刷，晚上还是我给他刷，因为感觉他自己刷刷不干净。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lk9l-wBYS74a1opeskQHmaOjeUCb_compress_L1',
    'video_id': '5889f7e5faa0522a1b1a4903',
    'title': '家里也可以做出美味的春卷，秘诀就在这里！',
    'video_tag_list': '',
    'content': '★★★★★\nFateVegetarian\nMenu\n春卷，又称春盘、薄饼。是中国民间节日的一种传统食品。\n现在有关春卷的谚语也很多，如“一卷不成春”，春的意思在这里就是春之吉兆。\n★★★★★\n创意指数\n三鲜春卷\n▼\n·食材·\n娃娃菜、肉丝、春卷皮\n香菇、姜、料酒、生抽、胡椒粉\n✤ ·\xa0✤ ·\xa0✤\n①娃娃菜洗净沥干\n②肉丝放入生抽、盐、料酒、胡椒粉，均匀搅拌\n③娃娃菜切丝、香菇切片、姜切末\n④炒香姜末\n⑤倒入肉丝清炒\n⑥盛出备用\n⑦清炒娃娃菜、香菇，加少许盐\n⑧加入肉丝继续清炒\n⑨勾芡\n⑩用清水涂抹边角\n⑪中火炸至两面金黄\n⑫春节怎么能少了这道点心~！快来试试吧！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/lhc-7StjYLOlm9YKgFjYV7tp44oj?sign=50287f19405da614957d62202b27dcdd&t=65fb06d4',
    'video_id': '588cae7cd5945f3b4044b5eb',
    'title': '大年初一的日常--好吃的西北菜+我与娃娃机之间的爱恨情仇',
    'video_tag_list': '',
    'content': '大年初一的日常，除了吃吃吃，还有和娃娃机之间故事～哈哈哈，祝大家新年快乐哈～🎉🎉🎉\n先来说说今天的美食吧！\n中午本想去吃火锅，但是火锅店不营业就去吃西贝莜面村。（视频中读错了，哈哈，这里科普下“莜”读yóu😌）虽然我是南方人，但真的是超级爱北方的菜啊！哈哈。这家之前有来吃过，口味挺不错的。烤鱼超级推荐！鱼肉又香又嫩，分量也很足。羊肉串我觉得还算ok，没有到特别好吃的地步。葱油拌秋葵推荐下，很清爽，超级爱吃啊！果蔬沙拉也属于比较清淡的，哈哈，过年有不能大鱼大肉的每天吃，还是要多吃一些蔬菜的。沙荆汁和蓝莓汁实在是有点甜，在减肥的妹子建议少喝，哈哈。杂粮拼盘其实也挺甜的。别看我们两个人把这么多全都吃完了，我现在正在跑步机上写笔记哦！\n再来说说今天的穿搭look\n外套：年前代购的粉色仿皮草，这个颜色真的超级美！虽然看上去脏脏的，但还是挺洋气的，搭配牛仔裤短靴非常潮！\n牛仔裤：free people的经典破洞九分裤，这样的牛仔裤是属于开春必备的！哈哈，弹力很大，官网这款有好多种颜色，个人感觉天蓝色最青春最显瘦了！\n靴：也是free people的，哈哈，我就是free people的忠实粉丝。短靴跟不是很高，所以走路超级舒服，这个颜色也是很百搭的驼色。官网好像有在打折，折后价格不贵，建议入手哈！@小红叔'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/d4d5514e86d8ab84211109a7ee52b40a0a6eedc7_v1_ln',
    'video_id': '588cdebdd5945f5e0be27045',
    'title': '上海迪士尼烟花表演🎇冰雪奇缘',
    'video_tag_list': '',
    'content': '感觉上海过年越来越没年味了[委屈]小时候还能在外婆家放放烟花 每年过年放烟花的时候都特别开心\n好像自从去年开始上海就不给放烟花了…一家人从一起放烟花的乐趣变成了抢红包😂\n大半夜的没睡着 发个上个月在上海迪士尼录的烟花表演视频 之前在东京的迪士尼都没有看到烟花 说真的去迪士尼的目的就是为了看烟花！我好像对烟花有迷之热爱[笑哭R][笑哭R][笑哭R]觉得很浪漫阿～～～\n上海迪士尼的烟花表演配合灯光秀 真的真的hin壮观 我本来是没看过冰雪奇缘这部动画（后知后觉[委屈]）我能说我是看了迪士尼的冰雪奇缘烟花表演才去补看的动画吗 哈哈哈\n总结！上海春节放不了噼里啪啦bombom的烟花 发个烟花视频感受一下好了[喜欢]'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/luUSZDMQ5GuBHWH-kf5NmyFG2BnA_compress_L1',
    'video_id': '588eb89ad1d3b932fc7f3dc4',
    'title': 'Anantara Chiang Mai resort',
    'video_tag_list': '',
    'content': '用手机自带的编辑器随便剪了一个\n度假在酒店葛优躺实在太舒心'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/pgc/93031a26-e82cfb7-bfed-338eb7725a5d?sign=896e4e0c8892eac50da180d9c072838a&t=65fb06d4',
    'video_id': '588ec8023460945d1661955d',
    'title': '手工蛋饺～～ 妈妈的味道～～～',
    'video_tag_list': '',
    'content': '小时候过年最重要的一个节目就是，\n等在做蛋饺的妈妈旁边，\n妈妈偶然夹过来一只做破的鸡蛋皮，\n虽然淡淡的，\n但在孩子的心里，\n那是最幸福的味道。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/4363dcca2ff7ef108978085ee96c34cf4cd28b74_r_ln',
    'video_id': '58902e487836230d910b144b',
    'title': '日本高山县新穗高原❄️北阿尔卑斯山',
    'video_tag_list': '',
    'content': '新穗高原被称为北阿尔卑斯山\n路途遥远却第一次忍不住想要拍自然景观，然后再感动一下还好我喜欢的地方正在和喜欢的人们分享❄️\n这里有新穗高缆车是日本唯一的双层缆车，也就是缆车是有上层和下层的，这样可以容纳更多的人乘坐。缆车的运行也是分段的：新穗高缆车总路程3，200米，分为两个阶段。第一段是从新穗高温泉站(海拔1117米)搭乘，行驶4分钟抵达锅平高原站(海拔1305米)；第二段，从白桦平站(海拔1308米)行驶7分钟抵达西穗高口站（海拔2156米）\n赶上好天气真的好棒，什么玉龙雪山，赶紧拜拜[偷笑R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltUabirCHMiDhlCD005pgC87_SPk_compress_L1',
    'video_id': '58907893b46c5d33a0bad6e7',
    'title': '纯搞笑-高抬腿涂口红大挑战',
    'video_tag_list': '',
    'content': '哈哈哈哈哈哈哈哈哈哈我又来耍宝了，高抬腿涂口红能涂到什么程度，你们可以看看。友情提示请不要在口中有食物或者有水的时候观看，不然屏幕脏了我不赔[装酷][装酷][装酷]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgF1kyZUrmn8Tv-GX4h6IZNtSAVz_compress_L1',
    'video_id': '5890939bfaa0526caea629f5',
    'title': 'Mix Restaurant',
    'video_tag_list': '',
    'content': '火焰冰淇淋蛋糕\n还挺好吃的，这个绿球球325泰铢\n内含饼干，黄桃，草莓，红莓，葡萄，布朗尼，燕麦，雪糕\n位置：直辖县Nimmanhemin路1巷，就在art mai酒店后面\n#清迈##泰国菜#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lt0_0FM-mP75aapJDqYyJWRiYCme_compress_L1',
    'video_id': '589402e9d5945f6924100570',
    'title': '这款火爆的玫瑰煎饺你还不会做吗？',
    'video_tag_list': '',
    'content': '★★★★★\nFateVegetarian\nMenu\n不知道从哪一天起，爱上了做早餐，更喜欢和爱的人一起享受早餐时光\n温暖而幸福的早餐时光，在这个看脸的时代，饺子也在拼颜值了O(∩_∩)O~\n★★★★★\n创意指数\n玫瑰煎饺\n▼\n玫瑰煎饺\n·食材·\n猪肉末、香菇、饺子皮\n姜、生抽、料酒、盐、油\n✤ · ✤ · ✤\n①香菇、姜切末\n②肉末加入盐、香菇、姜、生抽、料酒，拌匀\n③腌制10分钟\n④用5张饺子皮，分别在2/1处叠加\n⑤放入适量肉末\n⑥手指沾水抹边对折\n⑦从边角慢慢卷起\n⑧整理花边\n⑨中火煎一分钟\n⑩加入适量清水\n⑪转小火焖5分钟收干水分\n⑫美味的玫瑰煎饺就出炉啦~！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/e44c8160c1c918046e445727def72a5cdf92dcfe_r',
    'video_id': '5894052dd2c8a503c1c6c703',
    'title': '#一周一##宝宝#吃饭#',
    'video_tag_list': '',
    'content': '我女儿在一周一的时候完全独立进食，只需要把食物递给她。视频是一周一独立吃饭的小视频，吃了三碗瘦肉粥，还有一些水果 葡萄🍇，橘子等…\n很多盆友让我发分享，如何让一岁的宝宝可以独立进食。那我稍微讲下如何引导孩子吃饭。\n在宝宝5个多月可以坐的时候，每当我们吃饭时就会让她坐在餐椅上参与我们，给她一点即化饼干，形成初步的餐椅与食物的关系。养成之后吃饭坐餐椅的习惯。接着在添加辅食6-8个月的过程中，逐步添加手指食物 让她有更强的参与感。在她出生后，生活中遇到各样事情，我都会跟她分享，也会告诉她吃饭的时候不可以看手机不可以看电视，尽量少说话。8-10个月的时候对食物的敏感度提高，用小嘴探索食物的味道 我也尽量去做合她胃口的辅食。8个月之后吃饭时会给她一个碗 一个勺子 让她参与 或多或少有些食物 她可以慢慢玩慢慢吃，这是个探索阶段 不需要打断她，食物撒在地上衣服上墙上都没关系，她还没有对环境整洁与否的意识… 只需建立她对吃饭的兴趣。10个月-1岁想要尝试用碗勺吃饭 我就不断的鼓励她，这样是对的 爸爸妈妈就是这样做的，当着她的面吃饭，告诉她：食物真好吃，自己吃饭的感觉真棒！出于模仿和好奇的能力，他会不断尝试。在1岁零几天的某一天，我走开一会儿发现她碗里的食物少了一半，当我尝试喂食她的时候，她推开我的手，示意我她要自己吃。\n这过程中，她会有模仿各样我们吃饭的特征，比如食物太烫，我们会搅拌一下，或者两只碗去匀汤。孩子都会学习，当他有这样的行为的时候，不要立刻去阻止，她肯定是跟身边的人学会的，告诉她我们在什么情况下才会有这些的行为，并且尽量避免在孩子面前去做这样的行为。\n渐渐的孩子掌握了这门技能，也会爱上吃饭。那就不用操心了。\n@薯宝宝'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/lv-r3kzAmtFGnhiqvncrXwI7L3rv?sign=b9e024f841e290875a77cd64b431c857&t=65fb06d4',
    'video_id': '589411f9b46c5d6399bad6e7',
    'title': '酒红色眼妆不难画，让我来教你',
    'video_tag_list': '',
    'content': '谁说酒红色眼妆不会画，我来教你一招鲜这样的当时画最简单啦~\n🌸产品清单🌸\nsofina妆前乳\n阿玛尼大师粉底液5号\nclio遮瑕棒2号\n嘉娜宝天使蜜粉\n爱丽小屋眉笔1号\nponyeffect四色修容\nKose visee眼影pk3\n爱丽小屋101多功能笔1号+美少女战士眼线液笔\n资生堂睫毛夹\n芭妮兰狐尾巴睫毛膏\nkiko腮红1号\n爱丽小屋晶莹炫彩唇膏Be109'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llG7crxfc5zl8DOvZzmvW3BNBskS_compress_L1',
    'video_id': '58957e6a14de417076a29c20',
    'title': '3000公里跨越摩洛哥版图的Road trip路线图',
    'video_tag_list': '',
    'content': '12天的行程，在摩洛哥版图的中北部逆时针方向绕了一圈.\n从大西洋海岸的卡萨布兰卡出发，经过古城、Atlas雪山山脉、撒哈拉沙漠、蓝色小镇、直面直布罗陀海峡的地中海，回到大西洋岸.\n当地人说最推荐3-4月，1月虽有些冷也还是不错的. 走过临海和沙漠，温差都比较大，这个季节里白天太阳下徒步，也还是要晒晕的感觉，很难想像夏天里45度高温来是要被烤成什么样.\nDay 1: 索维拉 （大西洋风城，权利的游戏里龙母的奴隶湾！）\nDay 2/3: 马拉喀什 （赭红古城）\nDay 4: 瓦尔扎扎特 （穿越Atlas雪山脉）\nDay 5: 撒哈拉沙漠 （谜之撒哈拉，夜里星空很梦幻）\nDay 6: 菲斯 （途径北非小瑞士伊夫兰，古城菲斯）\nDay 7/8: 舍夫沙万 （蓝色山城小镇）\nDay 9: 丹吉尔 （直面直布罗陀）\nDay 10: 阿斯拉（大西洋和地中海交界）\nDay 11: 卡萨布兰卡 （北非谍影）\n摩洛哥属于第一眼美女，大片拍出的各种美. 主要看景看人文，食物难吃至极，至今想起塔吉锅的味道还在🤢.\n感谢小伙伴Yvonne美女的讲解~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lid50wQRfx_8vKBJffgwhr-Cpc74_compress_L1',
    'video_id': '5895fb2b14de414258af0372',
    'title': '清透混血妆',
    'video_tag_list': '',
    'content': '更新一发以前拍的视频，然后最近染发了其实更像混血了hhhhhhhh'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljqXJtZeoOlwB_sBUXVuB3kZ7Ree_compress_L1',
    'video_id': '5896d51cd5945f5ca2100571',
    'title': '【 包包里有什么 | 外出必备小物 】',
    'video_tag_list': '',
    'content': '第一次录视频好害羞都不敢看镜头，赶紧匆忙说几句话逃走哈哈。\n希望大家不要嫌弃啦~\n📌\n很多人都会烦恼小包的容量问题，虽然我一直买小包，但是觉得能兼具实用性这点还是比较重要。\n我个人买包的首要要求是能够装得下手机以及相机。\n这只chanel cf 是20cm的大mini，我觉得容量大小都还不错，如果再小一些的话我就会觉得有些不太方便了。\n📌\n视频中包包里装的东西：\n7plus、卡西欧tr600\nCHANEL 卡包\nSK-II 棒棒糖粉凝霜\nCPB 遮瑕膏\nTOMFORD 方管口红\nK-Palette 1DAY TATTOO 24小时持久防水极细眼线液笔\n谢谢你们来看，希望可以帮助到你们参考哦。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqMckfzP3y_Ii6qJzQnncIp42j1w_compress_L1',
    'video_id': '589734e4d1d3b930587f3dc4',
    'title': 'Skydive in Dubai❤️',
    'video_tag_list': '',
    'content': '给自己的一份三十岁生日礼物～\n话不多说 先睹为快 哈哈哈哈哈\n表情太难了 整个脸都感觉被吹歪\n将就看看哈哈哈'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhTvyhm7NRC1pN5NH_P4G1VsZh1C_compress_L1',
    'video_id': '5897ebd0faa0526bf2a629f5',
    'title': '来撸干脆面！',
    'video_tag_list': '',
    'content': '小家伙们巨逗，完全自来熟！\n怎么个自来熟？\n凑过来卖个萌就开始掏你衣服兜，\n看上什么拿起就走[抠鼻]\n爬上桌抢饮料玩儿！\n一只得手会叫帮手过来一起抢[石化]\n运气好也会碰到温顺的那只，\n窝在腿上求抚摸的[喜欢]\n过两天我再认真写一篇\n---------------------------\nBonita di café\n韩国，首尔，麻浦区西桥洞，364-24 5F\n地铁2线，弘大入口站，9号出口'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/8e3e7a36d7fa5a698feaad361ee2587afa09221f_r_ln',
    'video_id': '58980c57faa0525f6fa629f5',
    'title': '【视频】cpb长管隔离&香缇卡隔离',
    'video_tag_list': '肌肤之钥 clé de Peau Beauté 钻石光感隔离乳/黑管隔离滋润型 SPF20 PA++;香缇卡  Chantecaille Just Skin Anti Smog Tinted Moisturizer修复保湿隔离霜SPF15;平价又好用的隔离',
    'content': 'Hi大家好\n这两款隔离超多仙女问我使用感受～\n简单总结一下\n💋cpb长管隔离\n控油效果好，让底妆持久，一整天完美无瑕的感觉真的很棒～我个人干皮，放在春夏会更好。\n油皮混油皮也可以尝试这一款，因为我真没感觉这款滋润，当然也可以买短款的哈，说是更加控油～毕竟我是干皮，油皮还是要再做做功课🤗\n💋香缇卡隔离\n色号alabaster 真的是我超级喜欢的隔离，保湿滋润，有光泽，看起来皮肤质感很好～让底妆更加服帖，对干皮来说，这几个优点足够让我爱上它了。\n谢谢仙女们支持～有问题可以留言给我。\n🙈视频里的这个妆容我发分享了哦～就是这个视频的下一篇笔记，有兴趣可以看一看😘\n温馨提示‼️请不要在我的评论区打广告，如果有人提供购买链接，比如个人微信或淘宝，小仙女们请谨慎😱真假请自行判断，与本人无关。\n\n\n#平价又好用的隔离[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llO78-2U-j72OBeB4AT4sPLBP8zv_compress_L1',
    'video_id': '589834487836236c0df41ec7',
    'title': '南非旅游🇿🇦注意事项',
    'video_tag_list': '南非;用视频记录旅行',
    'content': '原来南非这么好玩这么美！\n小红书的第一个视频就献给南非啦～\n以下是一些注意事项，我想起来的话会继续补充\n📱wifi的话可以机场提前租，我们租的是52块一天的\n和其他非洲国家比南非的网路其实已经很快了，但在高速公路啊或者是比较偏僻的地方是根本跑不动的，比如我们住在一个动物园酒店的时候连信号都没有只能用酒店Wi-Fi\n但在开普敦或者是比较城市的地方都还挺快的\n桌山上甚至还有免费极速Wi-Fi 真的了不起！\n✈️签证\n签证都是寄去上海办的，个签400好像，不用脂膜。未满十八岁要出生证明和公证书具体的话可以官网看或者咨询旅行社\n我们是新加坡航空飞到约翰内斯堡，出海关要很久因为他们动作很慢，真的巨慢无比！\n大家要注意，机场的工作人员会上来搭讪问要不要帮你啊？要不要帮你拿行李呀？千万不要看他们也不要理他们假装听不懂马上离开，不然他们会向你索取小费，不是1刀而是要100rmb 哦！而且只要你给了第一个人钱，后面还会有更多的人跟上来找你要钱，所以真的不要看他们马上走！\n☁️南非的夏天一点都不热，没出太阳的时候还要穿一件薄外套，下雨也是一阵一阵几分钟就下完了 。但因为万里无云所以记得做好防晒！\n但好望角开普角海风真的特别大！🌀吹的我头痛，姑娘们最好两个人手牵手或者抱着走，我们那天在十二门徒峰风真的太大了我眼睁睁看着一个大叔刚下车就被风吹得飘起来！我和闺蜜为了不被吹走只能抱着走👭长这么大第一次觉得自己身轻如燕瘦如闪电⚡️连拍照都要我爸抓着我我才不会飞走😂大家不要穿太短的小裙子不然一直要当玛丽莲梦露很累的。\n当时隔壁有一位女士穿着仙女短纱裙在我们车旁拍照，风吹得她站不稳然后她就蹲下来拍，蹲下来裙子又被风吹起来，露出白色的打底裤，她也还是在努力的凹造型😂全车人看着她笑到没声音，闺蜜笑得都摔倒了啊哈哈\n💰机场换汇率比较不好，我们是带着美金去太阳城换成南非兰特的。南非物价很便宜，和国内三线城市差不多\n🍉国内有的水果这里都有，水果全部都超级便宜，只有香蕉贵一点。而且盛产黄桃，喜欢黄桃的宝宝们可以吃个双了🥛奶制品很浓，但我觉得有点过于浓了，他们都好重口味呀🍗炸鸡汉堡薯条什么的都超级咸，鸡肉比较柴。虽然柴又咸但吃起来真的很够味！！！越吃越香！分量也都很大很实在。\n‼️\n特别提醒下去旅游钱要记得先买【大南非标】插头\n南非的插头真的巨大，普通的万能插头什么的里面根本没有这个，一定要先国内购买好，不然到了当地再买价钱就是翻了好几倍的\n自来水都是可以直接喝的，酒店都有烧水壶。\n但南非酒店几乎都不提供除了洗发露沐浴露身体乳以外的一次性用品。所以大家记得带好牙刷牙膏拖鞋什么的。\n⚠️大家去南非旅游的时候注意安全哦\n因为贫富差距大所以南非很多很穷的黑人很可怕，偷对于他们来说技术性太强所以一般选择用抢的，大家不要单独行动晚上最好不要出门，包包一定要顾好哦！也不要在公共场所翻包包，不然会被盯上的。\n#我的小众旅行攻略[话题]##用视频记录旅行[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrUN_U1j9h63QnRp8WeiJaW0cDmY_compress_L1',
    'video_id': '589946a4faa05230eb242619',
    'title': '如此美味的菠萝炒饭，你还不会做吗？',
    'video_tag_list': '',
    'content': '★★★★★\nFateVegetarian\nMenu\n菠萝炒饭是菠萝肉，与新鲜蔬菜等一起在油锅中翻炒，炒好的米饭用菠萝壳装即可食用。\n该饭具有酸甜可口，营养丰富的特点，特别适合儿童食用。\n★★★★★\n创意指数\n黄金菠萝炒饭\n▼\n黄金菠萝炒饭\n·食材·\n菠萝、米饭、方腿\n鸡蛋、三丁、咖喱粉、盐\n✤ ·\xa0✤ ·\xa0✤\n①菠萝一切为二\n②挖出菠萝肉\n③菠萝切丁\n④方腿切丁\n⑤鸡蛋打匀\n⑥鸡蛋加盐清炒，备用\n⑦三丁过沸水\n⑧热油锅，加入米饭、鸡蛋、三丁、火腿丁翻炒\n⑨加入咖喱粉\n⑩撒盐调味，最后倒入菠萝丁翻炒\n⑪盛入菠萝中即可'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/37dc2700-10b5e2e-bfee-bbbb5406aac5_compress_L1',
    'video_id': '589ab40a7fc5b8133d8269ff',
    'title': '去滑雪一路上竟然这么美！',
    'video_tag_list': '',
    'content': '第一次在小红书上发视频！激动！\n纯白色的广袤大地和起伏山峦、还有那些满头枝丫的树。在白雪的包裹下，像是一棵棵充满细节、精致又脆弱的珊瑚。阳光温柔的洒下来，仿佛入了仙境！\n一路上用手机录了很多片段，拼凑成一小段视频，尽管表现力不及当时感受到的一半，也想要展示给大家这一路的美好！\n当然还有一些滑雪场的片段，以及一丢丢我老公滑雪的样子（朋友滑单板🏂手持go pro录的，不免晃的厉害，已经尽力了……）\n片子4分钟，1分37秒开始滑雪场，2分10秒开始滑雪的镜头。\n希望大家喜欢！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liXWd4Kw0iItf5gE56q-Mk2XR3A0_compress_L1',
    'video_id': '589bd8e5d5945f7609af9e2d',
    'title': '每日穿搭--情人节chic浪漫搭配',
    'video_tag_list': '',
    'content': '还有几天就到情人节啦！特地拍摄了一段小短片记录穿搭，这套搭配chic的同时又不失女人味。\n白毛衣搭配破洞牛仔裤，还有一丝丝随性的感觉。不过我最喜欢的是不同颜色的毛球耳环，实在是太可爱啦！\n用视频记录穿搭的感觉真有趣，大家喜欢吗？嘿嘿@小红叔 @穿搭薯'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltxLVz69vAax_9XuCJ6G19-bnXKb_compress_L1',
    'video_id': '589c16b078362363824d297d',
    'title': '斐济挑战 14000ft/4300米高度跳伞 全景跟拍',
    'video_tag_list': '',
    'content': '在去斐济之前，就看到有说跳伞不能错过！终于体验到了，说下经过！\n本来儿子也要跳8000ft的，胆子真大😅😅可是教练看到之后说太瘦太小了，脖子太细，万一降落伞打开时候爆开脖子会承受不住很危险，所以就不冒险了，只能取消，儿子还一度很郁闷。\n我和老公一起尝试了最高的14000ft/4300米，一架小飞机可以带2个人上去跳，正好和老公一架，视频就不从头开始了，从最刺激的跳开始😛😛\n当跳完以后发现还好选了最高的高度，自由落体时间是60秒！如果12000ft自由落体是45秒，10000ft是30秒，如果8000ft的话，那只有15秒！\n自由落体是最最最爽的，那感觉无法形容，爽到爆，恨不得伞不要打开！就是脸会被吹的变形，所以下意识告诉自己注意形象，注意形象，要抿嘴，不能大笑😆😆\n当伞打开以后就是自由翱翔阶段了，比起自由落体真是弱爆了！\n教练都是澳洲人，很nice，飞机上各种拍，还会分散注意力，和我聊天，不过其实也没啥好紧张的，伞打开后还让我自己掌舵，left hand pull hard，and then right hand，蛮好玩的😏😏\n建议如果要去跳伞的姐妹一定要选全景跟拍，这样才能完全拍出跳出来的状态和空中翻滚，翱翔的样子！\n就价格上来说，skydive是国际连锁，价格都差不太多，迪拜，塞班，新西兰和澳洲都有！\n斐济的价格14000ft/4300米跳伞是780斐济币，摄影摄像分几种，光教练摄影拍照是220斐济币，加上全景跟拍就是510斐济币，所以跳最高的要么是1000斐济币，要么1290斐济币，我选择全景跟拍，这样折和下来就是4200人民币的样子！\n衣服可以穿自己的，其实刚跳出去的时候还是蛮冷的，但是伞打开后，速度慢下来就很热了！\n顺便说下小香的古巴T，跳伞很合适，袖子包裹的很到位，穿着很舒服☺☺\n好啦，算是完成人生一大挑战了，无遗憾啦...'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luiBuJhLaI_5OQ78RMv4y860mr3C_compress_L1',
    'video_id': '589c2d0bb46c5d3ffce73f6c',
    'title': '⚡️简单的眉毛画法⚡️',
    'video_tag_list': '',
    'content': '第一次发美妆视频啦，因为我说话好慢，然后5分钟不够啦，当中就变声了几段哈哈！\n然后一开始我说错啦，是bobbi brown的眉笔，不是眼线笔，是深棕色哒！染眉膏是恋爱魔镜的04号！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luxLA4feNwR3Utz6hu-v-lqBhnvS_compress_L1',
    'video_id': '589c31c4d2c8a5552476ae0e',
    'title': '眼线到底怎么画？',
    'video_tag_list': '',
    'content': '因为眼尾有点下垂，所以喜欢画这种眼尾上扬的眼线，让自己看上去精神一点。\n但是上扬眼线容易画出很凶的感觉，到底怎么搭配才又媚又温柔呢？\n1⃣️上扬的线条要细腻，不要太粗，这个要勤奋多练 2⃣️细细慢慢的描画，一笔不要下手太重 3⃣️新手不要追求浓重的黑色，选择棕色更佳 4⃣️准备一支棉签棒，沾卸妆水，及时调整不满意的地方 5⃣️上扬眼线最好不要搭配冷色调眼影，棕红色系是最最惊艳的搭配 6⃣️注意贴着睫毛根部画，不要留白\n#眼线到底怎么画#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lh47Q8GKPlRs2NtO36MMQuteagJR_compress_L1',
    'video_id': '589c9f79b46c5d4f97b8e953',
    'title': '意犹未尽的SKYDIVE❤️Video',
    'video_tag_list': '',
    'content': '哈哈哈～毁形象的视频 用“vue"做的短视频 截取精彩部分\n跳下的一瞬间 没忍住在大叫“啊”[哭哭]\n整个脸就是两个字👉🏻惊悚 哈哈哈[石化]\n来给大家具体说说这次跳伞经历吧[喜欢]\n👉🏻预定时间:我提前了一个月预定的 建议大家也提早订\n然后就是最好放在行程的一开始几天里\n因为跳伞要看天气 如果天气不好会被cancel\n时间放在前面的话 还可以往后换时间哦\n我就是2号被取消的 然后换到了5号～\n被cancel的那天 心里非常难受 真的很怕跳不成\n千里迢迢就是为了来跳伞的啊～\n👉🏻预定方式:我是某宝找的定的 在网上付了2k多人民币到了现场再付款1k迪拉姆 总的价格在4krmb左右～包含跟拍\n大家也可以在skydive官网预订～某宝的话就是多了200多rmb的服务费 当天会有某宝中国工作人员指导你填表格（so自己定也很ok简单哦）\n👉🏻过程:我预约的是12点 其实轮到我的时候已经快1点半拉\n因为每个批次有限人员 加上教练也要休息啦\n所以填表格付完款后耐心等并且仔细听教练呼喊你的名字就好啦\n被叫到名字后 教练会讲解注意事项和动作\n很简单～比如跳下去拍拍你后 就可以自由发挥动作啦[得意]\n👉🏻体会:讲真期待这次跳伞很久了 自从在因特拉肯坐了滑翔伞后就决定来一次跳伞 终于在2017年完成啦\n说实话在等待的过程中就很紧张啦 上了飞机更是紧张的不行\n跟拍给我录video的时候 问我如何 我说excited\n录完我马上和教练说 我害怕[害怕]\n教练估计心理也是想 女人真可怕 真善变[震惊L]\n我是最后一个跳的 看到人家都下去了\n宝宝更加慌了 [石化]\n一边在嘀咕omg 一边被推走到机舱门口 往下看了一眼[石化] 还没等我反应过来\n就被教练推了下去 嘴里在喊“啊"[震惊L][震惊L][震惊L]\n你们看视频就知道了 我真是没忍住\n因为本来想做个美美的表情往下跳的啊[石化]\n哈哈哈哈哈 也好 够真实\n然后失重感就一小会 一丢丢 ～\n空中风非常大 很快就会被托起 做一些动作和看看美景就好啦\n耳朵会有一点点疼 也是可以忍受的那种～\n以上❤️非常感谢这次经历 ❤️\n晚上我妈还给我打电话说 不允许跳第二次了[震惊L]\n跳之前只字未提 就怕她担心睡不着觉[震惊L]\n而我老爸在电话里说 他也想跳 哈哈哈～\n勇敢如爸[装酷]'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/loMwLPUUhGGetb1CMdbm_Noq7MoA_compress_L1',
    'video_id': '589d2f71d5945f0c4c7d8644',
    'title': '情人节CP大挑战 宝宝篇',
    'video_tag_list': '',
    'content': '#情人节CP大挑战#\n亲爱滴薯爸薯妈薯宝们，宝宝有个喜大普奔的好消息～\n今天起截至2月15日\n所有小红薯都可以尽情体验小红书最新的视频功能啦！\n【你只需要】\n1、拉上你最爱的人（恋人、朋友、亲人……宠物也可以！）\n2、完成一个双人游戏（不要胡思乱想，具体下面有示范）\n3、拍下视频\n4、在视频笔记的正文里打上#情人节CP大挑战#的话题标签\n就可以参加！\n成功参与话题活动的小红薯，将可以在2月15日之后，永（bai）！久（song）！保留视频功能哦～～～\n本宝宝为家有薯宝的小红薯们，准备了特别版视频模板，薯爸薯妈和薯宝们可以按照宝宝给的视频样式来拍摄哦～\n【宝宝专属游戏规则如下】\nStep.1 介绍下宝宝和自己～\nStep2. 让宝宝选支唇膏给麻麻/粑粑涂上～\nStep3. 最重要的！爱的啵啵不～能～少～\n按要求完成视频拍摄，才算任务挑战成功哦～宝宝等着你[飞吻R][飞吻R]\n还在等什么！快抱起家里的天使宝宝，组成最强CP来参加我们的情人节特别企划吧！\n记得打上#情人节CP大挑战#的标签才能更快被队长找到哦～\n最后特别感谢美腻薯妈@👰🏻MissyHalloween👒 和涵涵宝宝的完美出镜～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lt_dWswXSlnU4EHYdEUQKZ42uIX2_compress_L1',
    'video_id': '589d300ed1d3b90c1787aa0a',
    'title': '情人节CP大挑战—美食篇',
    'video_tag_list': '',
    'content': '#情人节CP大挑战#\n情人节倒计时，响应队长号召，一起来撒狗粮好伐啦？狗粮.jpg怎么够？狗粮.avi.mov才够嘛！今天起截至2月15日，你也可以尽情体验小红书最新的视频功能啦！\n❤️你只需要：\n1、拉上你最爱的人（恋人、朋友、亲人……宠物也可以！）\n2、完成一个双人游戏（不要胡思乱想，具体下面有示范）\n3、拍下视频\n4、在视频笔记的正文里打上#情人节CP大挑战#的话题标签就可以参加！\n还有个福利~！成功参与话题活动的小红薯，将可以在2月15日之后，永久保留视频功能哦～～～\n[少女心]生活薯来说说美食篇的大挑战玩法：\nSTEP 1. 选取一样食物，比如饼干棒、鱿鱼丝、意大利面……推荐你们用一些细长条的食物呀\nSTEP 2. 一人一端开始吃\nSTEP 3. 把食物吃完，最好能以一个爱的小亲亲结尾哟(づ￣3￣)づ╭❤\n就是这么简单！生活薯等你来战喔~\n记得在笔记正文中加上#情人节CP大挑战# [得意][得意]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/b8cb33201d7f48a03cb5bea6b96b11c49a1990b0_r_ln',
    'video_id': '589d35f5faa0523221bc0d9f',
    'title': '情人节CP大挑战——美妆篇',
    'video_tag_list': '',
    'content': '今天起截至2月15日\n你也可以尽情体验小红书最新的视频功能啦！\n你只需要：\n1、拉上你最爱的人（恋人、朋友、亲人……宠物也可以！）\n2、完成一个双人游戏（不要胡思乱想，具体下面有示范）\n3、拍下视频\n4、在视频笔记的正文里打上#情人节CP大挑战#的话题标签就可以参加！\n🔺美妆薯游戏规则：\n拉上你最爱的人，互相为对方化妆（局部即可，比如唇膏，眉毛……），并用手机或相机记录下你们的甜蜜互动。\n🔺美妆薯打标签TIPS：\n在话题前后打上半角（即英文版）的 # ，示范：#情人节CP大挑战#。正确的标签才能让美妆薯看到大家的帖子哦～\n成功参与话题活动的小红薯，将可以在2月15日之后，永久保留视频功能哦～～～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsJsDgwY59QOacoWScqsoLmnp_RK_compress_L1',
    'video_id': '589d3a0afaa0523fafc2ed66',
    'title': '情人节CP大挑战 – 时尚篇',
    'video_tag_list': '',
    'content': '今天起截至2月15日\n你也可以尽情体验小红书最新的视频功能啦！\n你只需要：\n1) 拉上你的TA\n2) 完成下面的双人游戏\n3) 拍下视频\n4) 在视频笔记的正文里打上#情人节CP大挑战#的话题标签\n就可以参加！\n成功参与话题活动的小红薯，将可以在2月15日之后，永久保留视频功能哦～～～\n情人节CP大挑战\n时尚篇双人游戏：\n情人节要到啦，\n是不是很期待来自你的TA\n的特别礼物呢～\n比如…\n你最爱的包包？\n但是！除了买买买，\n你的TA知道这些包包的芳名怎么念吗？\n还是…\n一直很笃定地认定 LV = “驴牌”？\n这个情人节，就来挑战一下TA的时尚度吧！\n猜猜下面这些品牌，\n在TA口中会变成什么…？\n1)\xa0\xa0\xa0\xa0\xa0\xa0 Louis Vuitton\n2)\xa0\xa0\xa0\xa0\xa0\xa0 Yves Saint Laurent\n3)\xa0\xa0\xa0\xa0\xa0\xa0 Givenchy\n4)\xa0\xa0\xa0\xa0\xa0\xa0 Versace\n5)\xa0\xa0\xa0\xa0\xa0\xa0 Coccinelle\n6)\xa0\xa0\xa0\xa0\xa0\xa0 Loewe\n7)\xa0\xa0\xa0\xa0\xa0\xa0 Mansur Gavriel\n8)\xa0\xa0\xa0\xa0\xa0\xa0 Delvaux\n9)\xa0\xa0\xa0\xa0\xa0\xa0 Proenza Schouler\n10)\xa0\xa0 Hermes\n把这些品牌截个屏，\n拍拍TA念的时候\n自(yi)信(lian)满(meng)满(bi)的模样吧！\nP.S. 这些品牌的正确发音会在另一篇穿搭薯笔记揭晓哦～'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lh91Af0PmRti6NZshYJ-LSc6cX3e_compress_L1',
    'video_id': '589d4ba5faa0527e15c2ed65',
    'title': '【 手残党也能画好的日常眼线 】',
    'video_tag_list': '',
    'content': '其实我也是刚开始画眼妆不久，所以不要担心画不好哈，而且这种清淡的眼线搭配很多眼影都很好看。\n因为我日常妆都比较淡，而且眼皮十分显色的原因，我个人比较喜欢画棕色眼线，也显得眼神更加柔和。\n我这次用的是cpb眼线膏102号，这种膏体虽然不像眼线笔那样一笔成型，但可以画出由浅至深的效果，而且如果不熟练的话也可以少量多次的慢慢添加。\n眼线膏自带的眼线刷特别好用，可以画出很细的线条。\n📎\n#眼线到底怎么画#\n首先先把头微微仰起画一下内眼线，不要让睫毛缝隙留白。\n因为我的眼角有些下垂，所以外眼线我是不画眼头部分的，从眼睛的三分之一处开始，慢慢往眼角延伸，眼尾自然上扬。\n📎\n这次画的是个很细的眼线，比较适合裸妆。\n如果想更明显一点搭配比较深邃的妆容，只要加粗一些就好啦。\n希望可以帮助到你们哦。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llJ8C4HnQ_r2EO6JskXEVSS8lTHT_compress_L1',
    'video_id': '589d7974d2c8a57d2ebaa590',
    'title': '#第一次发视频#带你们看看大纽约！曼哈顿必须要去的地方！',
    'video_tag_list': '',
    'content': '一个礼拜居然升级可以发视频啦！\n赶紧先来testing一下！\n这个视频是2016圣诞节在纽约拍的，想展现给大家纽约的圣诞怎么过？纽约圣诞去哪儿玩？😊\n我的老粉宝宝们应该都看过啦,有的宝宝还看了十几遍，绝对真爱啊！\n视频从拍摄，到构思，到剪辑，到配乐，都是我亲自做的哦！似不似我有点厉害，哈哈哈…\n这几个地方都是纽约旅行必去的哦，要去的宝宝可以收藏哈！\n希望你们喜欢，定期分享视频😛'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lijlCHkyzxAzljjfYw52DEV2qAPF_compress_L1',
    'video_id': '589d8cb4783623640ba8936b',
    'title': '四个版本的拿小拳拳捶你胸口',
    'video_tag_list': '',
    'content': '[得意]玛丽又开始放飞自我了，这段文字谁特么写的太羞耻了…………这次包含温柔版&真我版&粤语发骚版&粤语真我版[得意]如果你笑了，请给我一个赞好吗！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loxsGcICG4FOpo1p6nTiTZkAmgK0_compress_L1',
    'video_id': '589ea8ebfaa0522f520fc94d',
    'title': '内含新手画眉大法❤️情人节妆容必杀技❤️',
    'video_tag_list': '',
    'content': '哈哈哈，今天分享几个情人节妆容小tips，\n快点get起来去俘虏心爱的他啊哈哈哈。\nps：内含新手画眉大法✅\n还有如何防止眼部掉妆呢！\n最后，口红怎么才能持久又不沾杯秘诀😎'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ccf7b04a6c14c2d37491d5cd700a1ededff0d2cb_v1',
    'video_id': '589ecd69faa0522e5e7c0f1a',
    'title': '元宵节怎么能少了这碗—桂花酒酿圆子',
    'video_tag_list': '',
    'content': '★★★★★\nFateVegetarian\nMenu\n桂花甜酒酿是上海和江苏一带的汉族传统名点。\n酒酿在明朝才作为小吃，色泽洁白，香味浓郁，阴凉甘甜。\n★★★★★\n创意指数\n桂花酒酿圆子\n▼\n桂花酒酿圆子\n·食材·\n小圆子、酒酿、冰糖\n枸杞、糖桂花\n✤ ·\xa0✤ ·\xa0✤\n①煮开水，倒入圆子\n②再次煮沸后加入冰糖\n③加入酒酿\n④加入枸杞\n⑤最后盛出后倒上糖桂花\n⑥饭后来一碗桂花酱酿圆子，妙哉！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lspP2dl6cSwJWgYeTNpc6zknM5xf_compress_L1',
    'video_id': '589ed27414de413154b1e0ae',
    'title': '巴厘岛悬崖spa💆',
    'video_tag_list': '',
    'content': '原来视频和照片不能一起发、好无趣🙄。\nbali岛的悬崖spa最出名的是ayana、然后就是这家karma kandara了。因为住的这家酒店所以就做的这家啦。只有为数不多的几间spa室都需要提前预定、每一间都可以感受来自印度洋的海风轻拂、听着海声做spa是不是想想都很心动。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhfk_255PKoEllu8rD9QqhLMfoY6_compress_L1',
    'video_id': '589efd3e7836234cf627f5a3',
    'title': '两只Cherry键盘',
    'video_tag_list': '',
    'content': '粉嫩少女心的是我哒\n炫酷变色的是直男的\n[抠鼻]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luYf9yani9c6c7qbexx4SX_e2NXI_compress_L1',
    'video_id': '58a06871d2c8a504403da84c',
    'title': 'tf白管07试色视频',
    'video_tag_list': '',
    'content': '如视频\n我现在把库存视频都拿出来了[得意R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnAPLMoYE_PawyhtQFa-M19QNy7o_compress_L1',
    'video_id': '58a110a7b46c5d61f5da5a77',
    'title': '【Suri亲测】4moms杰伦同款哄睡神器电动摇篮',
    'video_tag_list': '薯妈必备早教玩具',
    'content': '美国直邮买的摇篮，#薯妈必备早教玩具[话题]#娃第一次上去就乖乖坐了20分钟，确实省力多了！终于不用抱着娃哄了！简单说下这款摇篮的几个特点：\n1、有5种摇晃模式，宝宝不会乏味，我用的是左右摇；\n2、背景音有几种可以选择，白噪音、心跳音、海洋音等等，帮助小宝宝睡觉；\n3、我买的是蓝牙版，可以通过蓝牙连接手机，播放手机上下载好的儿歌或者故事语音，这样可以让娃一边摇一边听故事；\n4、宝宝头上悬挂的三个小球有两面，一面是彩色的一面是黑白的，正好小月龄让她看黑白面当黑白卡用，大月龄了再看彩色的；\n5、绒布座套可以整体拆下来扔洗衣机里面清洗烘干，这点太重要了；\n6、座椅有安全带，原则上宝宝会爬就不能坐了，怕她掉下来，所以比较合适的使用区间我觉得是1-7个月。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lo_KTXlh2M0Jh2vzMIRRYTmCOEQQ_compress_L2',
    'video_id': '58a1288ad2c8a561fe9efb7c',
    'title': '',
    'video_tag_list': '旅行小视频',
    'content': '澳大利亚悉尼跳伞\n前两年去悉尼的时候跳了次伞，我这人胆子比较大，最欢玩刺激的但不爱恐怖的，最近想找人一起去欢乐谷都很难了，大家很惜命[吧唧R]。悉尼跳伞很便宜，我记得加上录像一共才2000多吧，反正比国内便宜太多太多！\n我觉得跳伞最刺激的不是跳下去，是刚才还在和你打招呼的人突然就下去了，然后下一个就轮到你的时候，哈哈哈。胆子大的人去尝试次吧，不会后悔的。\n@薯队长  @生活薯  @视频薯 #澳大利亚旅行[话题]##旅游[话题]##我的极限运动体验[话题]##旅行小视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/f5ae31c11266dc844a8aa90f2c470cc49fab549a_r_ln',
    'video_id': '58a138a2b46c5d6c0f96f48e',
    'title': '2分钟学会美味的烹饪技巧——金针菇培根卷',
    'video_tag_list': '',
    'content': '★★★★★\nFateVegetarian\nMenu\n培根金针菇卷是用培根和金针菇做成的菜。\n烟肉味道极好，常用作为烹调。\n★★★★★\n创意指数\n金针菇培根卷\n▼\n金针菇培根卷\n·食材·\n金针菇、培根、葱\n蚝油、糖、淀粉\n✤ · ✤ · ✤\n①培根切半\n②培根卷起\n③用一根葱将培根卷困扎\n④用小火煎至两面金黄\n⑤热油锅加入蚝油、糖\n⑥勾芡收汁\n⑦培根卷淋汁'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/FqjS76feRVreeZCRHsPmJubCjyiS?sign=c28bed9e16719c2baa55ea90f8e1a535&t=65fb06d4',
    'video_id': '58a16394b46c5d024d86393a',
    'title': '跳舞真的很快乐，汗流浃背的感觉很爽',
    'video_tag_list': '',
    'content': '体力有点跟不上，要多多锻炼了～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lt2gWB2hbUvUK8oT_1HCiZPC0b-H_compress_L1',
    'video_id': '58a179c8b46c5d5044edddd3',
    'title': '简单易上手的画眉方法（视频➕文字版）',
    'video_tag_list': '',
    'content': '一个无眉星人的画眉过程...\n第一次发视频，丑话说前面可以提意见，尽量改。但是恶意语言，请您自重😈\n产品：MAKE UP FOR EVER防水眉形修正液\nSEPHORA 35号刷子\n（我只画了底妆，没修容没眼妆🙀🙀🙀）\n如果眉毛乱乱的先确认好眉形刮出大致形状。\n首先用眉形修正液挤一颗红豆大小就足以👌够用两个眉毛的！然后按照眉头👉眉峰👉眉尾确认三点画出一条线，然后上面也按照形状画出一条线，这样眉毛的轮廓就出来了。\n其次填满它，填填填......（记住！少量多次，不然会很尴尬很夸张！）\n最后用小刷头晕一下眉头部分，让它看起来更自然。\n每个人肯定都有画眉尴尬期尤其是我们这种无眉🙈不过也有好处，可以随意切换自己喜欢的眉形😻\n我是建议能画就不纹，要纹就别图便宜。#简单易上手的画眉方法#\n最后，谢谢欣赏💌'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvVwnoxbchYlRHdEj-5lEYLeDnpj_compress_L1',
    'video_id': '58a1ce45d1d3b969de0c774d',
    'title': '6周密集美白计划，赶在夏天来之前白成一道光！',
    'video_tag_list': '',
    'content': '玛丽又来了，这次我来说护肤！素颜勿喷，长痘黑眼圈我也不想的，过年天天两三点睡，所以说女人皮肤保养还是要靠睡啊！这个美白计划主旨就是：美白精华主攻，别的美白产品打辅助。这次使用的美白精华是欧缇丽的美白精华，温和、亮白、滋润感十足，足够我给五星好评。再加上sk2晶莹露、雅诗兰黛美白水、欧缇丽葡萄籽晚霜，我对我自己白成一道光还是蛮有自信的！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llN62M-tOGju1t4qxz8Gw_oo5FZx_compress_L1',
    'video_id': '58a1d666d1d3b908bf7fa0b6',
    'title': '带妆10小时不脱妆，我靠的是它们',
    'video_tag_list': '',
    'content': '密集发视频的玛丽来安利持妆力超强的一套彩妆了！我这天就用这些顶着一天的妆容从早十点到晚九点。雅诗兰黛double wear真的要一生推啊一生推，剩下的看视频吧，不详细说了[瞌睡]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/cb6cc41edb16a0bc1360109b6dbf35a920596774_r_ln',
    'video_id': '58a2798014de411b0b4db5b9',
    'title': '情人节玩浪漫？一招瞬间征服女朋友！',
    'video_tag_list': '',
    'content': "情人节 \xa0 \xa0 \xa0 \xa0特辑\nI didn't think that I could ever trust happiness. Then I met you. Happy Valenti ne's Day, Dear.\n我一直不相信有真正的“幸福”，直到不久以后，我邂逅了你。亲爱的，情人节快乐。\n......\n情人节爱心套餐\n·食材·\n番茄、黄瓜、胡萝卜、草莓、西红柿\n橘子、火腿肠、鸡蛋\n1.番茄45°中间切开\n2.用牙签串起\n3.每次切入时不要切断，用刀身往外压形成花瓣状\n4.用牙签固定\n5.香肠45°中间切开\n6.穿上牙签\n7.胡萝卜切片\n8.黄瓜切片\n9.切出2个小三角形\n10.中间切出三角形\n11.用牙签固定\n12.香肠中间切开，留1公分不切断\n13.成爱心状用牙签固定\n14.镂空部分倒入鸡蛋煎至嫩黄\n15.番茄切片\n16.裱花摆盘\n17.情人节爱心套餐上桌啦~！"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgfnPfIDAr224rybk774cWajfeuT_compress_L1',
    'video_id': '58a29908d5945f42913afdd7',
    'title': '亲眼看过在喷的火山吗？我正在亲眼看🤗#直播视频#',
    'video_tag_list': '',
    'content': '我亲眼看到喷岩浆的火山口了，正在活跃ing！\n那个蠢蠢欲动的岩浆，人生又一小目标圆满了 🤗\n这个世界你必须要亲眼看[机智][机智][机智]\n随便给你们感受一下，火山岩浆噼里啪啦的感觉[调皮]\n正上方的只用眼睛看了，来不及拍了[偷笑]\n实时更新视频！\n后面还有滑翔伞，溪降，日出，等等…\n欢迎关注，欢迎收藏！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luyPdHz4ATK7c13pDdJQFZVmWiL__compress_L1',
    'video_id': '58a2d2d57836236d558255ac',
    'title': '简单的眼影画法（单眼皮/内双都适用）',
    'video_tag_list': '日常妆容打卡',
    'content': '分享一款极其简单的眼影画法👀很容易，很好学，就算新手也无压力👍#日常妆容打卡[话题]#\n首先NAKED作为2/3眼皮打底。\n哑光浅棕色，可以加深轮廓或者晕染深色，不过我喜欢作为打底，可以让我这样的单眼皮看起来不那么肿✌\n然后用BUCK强调↕️上下眼尾。\n哑光红棕色，这个盘子里就两块哑光一个是naked 另一个就是这个了。\n其次DARKHORSE作为眼线，简单画出一条线就OK，很自然不夸张的同时又有一种放大眼睛的错觉。\n偏冷的深棕，珠光质地。\n接着SMOG晕染上眼尾，少量就行🌟\n珠光棕色，超级无敌百搭。\n最后用HALF BAKED体谅眼球中央，一点就够[得意R]\n灿烂的金色，这块颜色非常饱满，相当好看！！！\n这个眼妆不挑口红，什么色系都不错👍👍👍\n还有我想说，单眼皮也很美，没必要跟风拉双眼皮。\n最后的最后，谢谢欣赏💌'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/373202a1799ca3144e97a9d5b0a8f6494dac861d_r',
    'video_id': '58a2d83ed2c8a560ef2c50b0',
    'title': '职业运动员在健身房练什么？😜 （视频，本人）',
    'video_tag_list': '',
    'content': '运动员需要练的体能跟普通健身是有一大些不同的。体能对一个运动员来说是不可以缺少的一部分。运动员都是针对个人项目来做体能训练。有些运动需要更多的上肢训练，而有些运动更需要下肢训练。\n我是一名网球运动员，我认为这个项目在体能方面是练的很全面的一个项目。在比赛场上快速移动，还要打出有力的击球，所以在健身房里要练的东西有很多😆\n我练的体能项目包括：\n- 心肺，肌力，核心，平衡，爆发力，脚步运用，协调性，等等...\n最后还有女生最关心的穿着...[偷笑R] 上衣和短裤都是Lululemon, 鞋子是Nike专业网球鞋，男款的\n#弹力带教学视频[话题]#\n#健身球教学视频[话题]#\n#健身器械教学视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/ltC5J3bCPfMMgOAMrqAOgSUMrgeH?sign=a7102b36bd15267ae39ce23ccfca3670&t=65fb06d4',
    'video_id': '58a4fd66d5945f6ef797a6cd',
    'title': '#化妆视频#大地色canmake日常妆容',
    'video_tag_list': '',
    'content': 'CANMAKE眼影很多人都有，但对于化妆菜鸟来说，如果使用这款眼影给自己画个日常精致又得体的妆容，wiwi新出化妆视频给大家秀一个!'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg_LVVDVSsl1vJn8ssO86vEfF-3Q_compress_L1',
    'video_id': '58a54169d2c8a55b8d346c97',
    'title': '每日穿搭--皮草搭配运动风一样很精彩（视频版）',
    'video_tag_list': '',
    'content': "昨天po了一组皮草搭配的笔记，谢谢小红薯们的支持和鼓励，今天我来po视频版的啦！哈哈\n具体衣服的介绍，图文的笔记都有我就不再多说啦，今天主要来聊聊视频吧！\n以前自己一直是用照片记录穿搭，拍了几年了也算是驾轻就熟。视频的领域完全是自学拍摄剪辑后期，虽然视频呈现出来的效果会更生动，但也真心比照片辛苦！哈哈。这段视频中一个跑步的镜头，来来回回上下楼梯十几次，等于做了有一场有氧运动了，好在效果还不错，啦啦啦。兴趣真的是最好的老师呀。\n✨视频拍摄器材：佳能5D3\n✨后期剪辑：Final Cut Pro\n✨BMG：Hold on we're going home\n大家有什么关于视频的问题也欢迎给我留言，一起讨论进步哈，么么哒。[喜欢]@穿搭薯 @小红叔"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmZGVKBUS-ZiCGz-X44_DouHekrU_compress_L1',
    'video_id': '58a6729778362375496b9e19',
    'title': '',
    'video_tag_list': '',
    'content': '看完这个视频，记得清洗下你们的粉扑哈\n我用的是人手一瓶的大创洗粉扑清洁剂，又便宜又好用，具体看视频吧😘'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lutbCqUiZfWRsutPtPOwTg2daiUP_compress_L1',
    'video_id': '58a67606d1d3b96f1eb50e75',
    'title': '炒面美味不粘锅的小技巧—家常炒面',
    'video_tag_list': '',
    'content': '★★★★★\nFateVegetarian\nMenu\n炒面是流行于大江南北的中国传统小吃，\n一般是指两种，一种是炒面条，另一种是炒面粉。\n★★★★★\n创意指数\n家常炒面\n▼\n家常炒面\n·食材·\n面条、青菜、香肠\n鸡蛋、生抽、老抽、盐\n✤ ·\xa0✤ ·\xa0✤\n①沸水下面，稍微沸腾一下就好，中间加一次冷水\n②捞出面条后过下凉水，然后沥干备用\n③香肠切片、青菜去根\n④鸡蛋打散\n⑤热油锅，倒入鸡蛋炒好备用\n⑥锅中加入香肠翻炒到变色后，加入青菜清炒\n⑦在青菜全部出水分之前，倒入面条翻炒\n⑧淋入生抽、老抽，盐少许\n⑨最好倒入鸡蛋清炒\n⑩美味的家常炒面开吃啦~！\n#在家做炒面[话题]##面条的花式做法[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmNbA9QsKRv7ehsn1yHcY6DKFuVE_compress_L1',
    'video_id': '58a67c1bb46c5d754dc3afbf',
    'title': '早餐吃什么',
    'video_tag_list': '',
    'content': '爱茉莉抹茶酱（福利社）\n雀巢麦片\nvogel麦片😑（福利社）\n还有牛奶和全麦面包\n煮鸡蛋忘拍了\n你们猜1分07秒会不会被屏蔽😂'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lowJ4-gIt9DdWFONlLqXXEt3lH9V_compress_L1',
    'video_id': '58a70673d2c8a541de43f674',
    'title': '只有非常努力， 才能看起来毫不费力。',
    'video_tag_list': '',
    'content': '虐腹顺便拍个小视频，嘻嘻，这个动作练腹很有用哦！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/90d77ec1-06d21b6-9dd9-a796a6def975_compress_L1',
    'video_id': '58a9b3893460943123c36d11',
    'title': '没有开瓶器怎么办，教你一招巧开瓶盖',
    'video_tag_list': '',
    'content': '其实开瓶盖根本不需要什么开瓶器，只要用我们家里都会有的东西，利用杠杆原理就能轻松快速地开瓶盖了。别傻傻地用牙齿咬了，不卫生又不安全哟。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvE05N3xuqtqftPqjTY0u1Id9FTh_compress_L1',
    'video_id': '58aa792ed1d3b913def190e7',
    'title': '【叁月】周末约会妆',
    'video_tag_list': '',
    'content': '第一次尝试化妆视频，一定要说出来纪念一下下，嘻嘻嘻，希望以后可以坚持定期来跟大家分享视频（如果大家稀饭d话）[飞吻R]\n视频中用到的东东我都有标注哦~今天用的基本都是我喜欢的常用的东西[得意R]\n尤其是IPSA的蜜粉，有点冷门但是很好用。改天我自己PO 给大家看\n眼妆部分👀&口红部分👄\n为了更清晰的展示颜色和画法，我做了图文的步骤分解哈~\n可以看下一条笔记啦~👇👇👇\n💗💋💗\n么么哒'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ll0nmNSQxzMrI4GjF3jqY-BDC5Ec_compress_L1',
    'video_id': '58aa85f4b46c5d45275e62f8',
    'title': '【 浅谈十款精华 | 质地对比 】',
    'video_tag_list': '',
    'content': '精华属于护肤品中不可或缺的环节。\n今天来讲讲手头上这十款精华。\n因为视频时间有限，所以每款精华只能几句带过，具体会出文字版本。\n视频主要就是为了能直观展示一下每款精华的质地。\n📎\n出场顺序：\nWhoo后 密贴/秘贴循环精华\nWhoo后 密贴/秘贴自生精华\nCaudalie 欧缇丽SOS莹润保湿精华\nCaudalie 欧缇丽臻美亮白精华液\n雅诗兰黛 ANR即时特润修护肌透精华露 小棕瓶\nSK-II 精研祛斑精华液\n黛珂紫瓶保湿精华\n黛珂曲酸精华\nLaneige 兰芝致美紧颜修护精华液\n资生堂新透白精华\n📎\n#敏感肌必入修复精华#\n希望帮助到你们参考哈～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/e7528781-1067f1a-87df-0ea399eac874_compress_L1',
    'video_id': '58aa9f81a9b2ed1cef4ad910',
    'title': '教你自制懒人卤蛋',
    'video_tag_list': '',
    'content': '看别人做卤蛋要熬一大锅，而且要熬很久，有没有觉得特别麻烦？今天教你懒人卤蛋法，怕麻烦或者只想吃一个卤蛋的时候就可以做起来啦。\nPS：觉得生抽太咸的话可以用少点生抽，多放点老抽哟。\n#卤蛋这么做超美味[话题]#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lkDyHyi8YvIzFdAs8L0-BNkA5qPP_compress_L1',
    'video_id': '58aafecffaa05253bf785562',
    'title': '💋新年大红唇妆容💋',
    'video_tag_list': '新年大红色唇膏',
    'content': "🎉说是新年…其实已经不新了哈哈\n最近实在是比较忙，所以很久没有更新视频了，让大家久等了！\n还好没有出正月，赶紧把这支大红唇#妆容教程#送给大家！希望小伙伴们在新的一年像💄一样红红火火，光彩夺目🌟🌟🌟🌟🌟🌟🌟🌟\n👇下面让我列举一下这支化妆视频用到的化妆品：\n1⃣️Dior瞬效美肌修色棒 💚绿色\n2⃣️Givenchy Photo'Perfexion 纪梵希感光皙颜粉底液 #101 Perfect Beige\n3⃣️Anastasia Beverly Hills Brow Wiz #Medium Brown\n4⃣️MAC单色眼影：Wedge，Naked Lunch\n5⃣️Makeup Geek单色眼影：Hipster，Mango Tango\n6⃣️Bobbi Brown流云眼线膏 #黑色\n7⃣️植村秀睫毛夹\n8⃣️美宝莲紫胖子防水睫毛膏\n9⃣️NARS修容粉 #Laguna\n1⃣️0⃣️Benefit Rockatuer 贝玲妃摇滚甜心腮红\n1⃣️1⃣️BECCA高光粉 #Moonstone\n1⃣️2⃣️NARS哑光唇笔 #Cruella\n.\n以上，欢迎小伙伴们来围观哟😘😘\n#单眼皮如何画眼妆[话题]##日常妆容打卡[话题]##新年大红色唇膏[话题]#"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpmfAXoEmyUq8x0MLfyrx7mcFi8L_compress_L1',
    'video_id': '58ab92e4d5945f7466299728',
    'title': '不伤发的卷发方法！',
    'video_tag_list': '',
    'content': '啊哈哈哈今天跟大家分享一个我近期最喜欢的卷头发方法，\n非常方便、节省时间重点还不伤发哦！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkvkab8wNV4FapwRMqvGx-p-t_ZM_compress_L1',
    'video_id': '58abd56ed1d3b9161bf190e9',
    'title': '收纳王子登录湖南卫视《我是大美人》拯救卧室整理大改造',
    'video_tag_list': '',
    'content': '湖南卫视《我是大美人》，收纳王子国内第一次真人收纳秀before/after，各种实用收纳技巧敬请关注！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/9e05a92d-48dd74b-8fda-d5a3f1a8087a_compress_L1',
    'video_id': '58abdfe97fc5b8172c9845b6',
    'title': '教你自制芳香除湿剂',
    'video_tag_list': '',
    'content': '#梅雨季除湿大法[话题]#\n清洁三剑客之一的小苏打除了做清洁用，还能用来做除湿剂哟。做好的除湿剂可以放在衣柜、厕所等容易潮湿的地方。瓶子里的小苏打在吸水气后会结成块状，结块的小苏打又可以拿出来做清洁用了，非常实用又节省~请再call me 一次省钱小能手。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/a2713ba1f3980eea98bda7e900f279a8273fc544_r_ln',
    'video_id': '58ac76ffd5945f257c299728',
    'title': '吃对了，减肥事半功倍！😋自制减脂沙拉教程（视频版）🎥',
    'video_tag_list': '',
    'content': '#减肥减脂吃这些[话题]#\n前几天发了一篇笔记是说我在减肥期间会吃的自制蔬菜沙拉图文教程。今天来和大家分享一下视频版本啦！视频呈现的更直观一些，嘿嘿。\n顺便再回答一下大家问的比较多的问题哈。\n1⃣️这道沙拉是在什么时候吃？\n我一般会在晚餐的时候吃，有的时候午饭也会吃。但更多的是在晚餐的时候吃。我一般每天摄入热量比大约是早餐：30-40%，午餐30-40%，晚餐：20-30%。\n2⃣️除了吃沙拉要不要吃别的？\n咱们每顿正餐都需要尽量保证摄入碳水化合物、维生素、蛋白质。虽说减肥，但营养还是要跟的上啦。这也是我一直所推崇的健康减肥啦！所以除吃沙拉还需要吃一些主食。建议大家可以用紫薯或者红薯代替米饭或面条。这是因为首先薯类食物原本热量就比米饭低，其中含有丰富的膳食纤维，很容易增加人们的饱腹感，能够用更少的能量让人感到满足，间接减少进食的量，而且膳食纤维多的食物人们也会不经意地多嚼几下，而咀嚼往往容易刺激大脑神经中枢，让大脑产生饱了的错觉。膳食纤维也有助于保持肠道健康，缓解便秘，所以也有助减肥。我一般会吃一个小小的紫薯或者红薯。要注意控制量哈。\n3⃣️沙拉酱可以用别的代替吗？\n当然可以呀。这可以根据自己的口味，我还尝试过用低脂酸奶也不错啦！之后会分享更多其他减脂餐的做法哒。\n4⃣️只吃沙拉就能瘦吗？\n哈哈哈，回答当然是NO啦！减肥是场持久战，需要养成健康的生活饮食习惯，还需要有一定的运动。只吃沙拉会营养不良，说不定哪天嘴馋了还会让你暴饮暴食。所以，一定记得营养均衡啦！\n5⃣️除了沙拉会吃肉吗？\n会呀会呀，我真的是无肉不欢，但自从减肥后我几乎不吃猪肉，更多的是选择鸡胸、牛肉和鱼肉。这几种肉类脂肪含量低，蛋白质含量棒棒哒。而猪肉的营养价值和这几种比起来不是特别高，但脂肪含量却很高。所以我一般很少很少吃猪肉。\n这五个是上篇笔记问的比较多的问题，大家如果有其他关于减肥和健身相关的问题，也欢迎给我留言哈，我会尽量回答哒，么么哒。 @小红叔'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FlyUmzSY2w6oOdtmcL21wwIFjJAL_compress_L1',
    'video_id': '58ad0a6bd1d3b912432f029b',
    'title': 'urban decay的叠加就是给你一个新色号',
    'video_tag_list': '',
    'content': '这次用urban decay的cowboy叠了visee的单色018，感觉就变成一个新色了，几乎任何颜色眼影叠加都可以让原来的颜色变华丽哦～'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/pgc/6a1fe443-a5ec18b-851a-c28aa84a99ff_compress_L1',
    'video_id': '58ae96b9346094486d5eb950',
    'title': '（珍藏版）让懒癌患者也能爱上厨房的食谱大公开',
    'video_tag_list': '',
    'content': '今天是懒人吃货的合集~想自己做点什么好吃的解解馋，但是又懒癌发作，这就是懒人吃货矛盾挣扎的内心（我就是）。有了这些轻松做零食的方法，再懒也能自己动手丰衣足食啦~你看我这么懒都动手做了︿(￣︶￣)︿\n温馨提示：草莓进微波炉前一定要跟着我做吸管去蒂的处理，要不就用牙签之类的扎穿果肉，不然会炸啊！会炸啊！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhjd3v8mxGqUO8vszmAT3oo7Yd-g_compress_L1',
    'video_id': '58aead20d5945f385c9b5b66',
    'title': '【视频】Tomford 唇膏试色',
    'video_tag_list': '最难买的唇膏色号',
    'content': '产品清单：跟视频顺序一样🤗\n💋07pink dusk\n裸粉色，喜欢春夏用，非常滋润，很少女的颜色。\n💋09first time\n裸色，很干，夏天很喜欢用，不是很提气色，但是我觉得很好看，搭配好妆容哦～\n💋03Casablanca\n说过无数次，超级喜欢的玫瑰豆沙色，喜欢薄涂～适合秋冬\n💋09true coral\n大热的颜色，珊瑚红色，比较鲜艳，好看！\n💋15wild ginger\n橘红色，除了喜欢我还能说什么，大爱😂😂怎么那么适合我呢，哈哈哈哈哈。\n💋16scarlet rouge\n火到每天看到它十几遍，嗯还是有道理的，复古红，薄涂很好看，气质又不会很突兀，喜欢啦啦啦🎉\n谢谢仙女们支持😘\n#最难买的唇膏色号[话题]##唇妆试色报告[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/1ea0f39f-8c107dc-8677-10ac8bd37aea_compress_L1',
    'video_id': '58afecaa346094518188bb6a',
    'title': '开价护肤品真能“媲美”天价霜？热门贵妇霜表示怎么可能',
    'video_tag_list': '',
    'content': '#热门面霜测评[话题]#“便宜到上天的护肤草单，国货大牌全都有！”“这个牌子口碑好到炸裂，开架护肤品竟如此好用 ！”“百元以下！这些护肤好物值得一囤再囤”……此类夸赞平价开架产品的噱头标题，真想叫皮皮虾去敲敲这些个编辑的脑袋，除了标题党你还能干嘛？这些东西你自己都用过？真的有你写的这么好用？除了开篇的百元单品一路推到千元单品你不是在逗我？\n既然开架牌那么喜欢“媲美”的对象，干脆就拎3款主流又经典的贵妇霜出来遛遛，看看花几千块买回来的小小一瓶是不是真的那么厉害。\n一共准备了3款热门贵妇霜作为试用：\nCPB金致乳霜（黄金年代限量包装版）\nSISLEY抗皱修活御致臻颜霜\nLa Prairie鱼子精华琼贵乳霜（sheer版）\n💰价 格\nCPB：RMB 7000/50g 、RMB 4500/30g（真是一般牌子想都不敢想）\nSisley：RMB 3300/50g\nLa Prairie：RMB 3900/50g\n🎁外 观\nCPB：❤️❤️❤️❤️❤️\n比常规金色款更加五光十色的黄金年代限量包装版，立体切割造型像宝石一样超有辨识度，贵气又抢眼，空瓶做摆设也有sense。整个瓶身只有盖子上有个一咪咪大的logo，无比任性。\nSisley：❤️❤️❤️❤️\n白色瓶身简洁优雅，除了瓶盖顶部有一个大大的s 标志——非常不明显，金色logo的腰带平添一份贵族感。\nLa Prairie：❤️❤️❤️❤️\n蓝瓶银盖大logo，瓶身上的英文简单粗暴的告诉你我就是鱼子酱、奢华霜、很轻薄！\n🎎配 件\nCPB：❤️❤️❤️❤️❤️\n流线型设计的金属挖勺非常趁手，让整个过程变得很有仪式感。配套的底座让这根小挖勺可以很好的收纳。\nSisley：❤️❤️\n配送了一个塑料薄片挖勺，略显简陋\nLa Prairie：❤️❤️❤️\n圆片型挖勺很特别，但是真的蛮费量的，这么大一片挖下去真心痛。没有底座也不方便收纳。\n💰护肤成本\nCPB：❤️❤️❤️\n绿豆大小用量，30g可以用1个半月左右，每天成本100块，就当天天都去看IMAX电影咯\nSisley：❤️❤️❤️❤️❤️\n绿豆大小用量，使用3-4个月，每天成本36块，也就是每天一杯星巴克\nLa Prairie：❤️❤️❤️❤️\n黄豆大小用量，使用2-3个月，每天的成本65块，等于每天来杯星巴克以后，还可以加个小甜点\n💆🏻质地感受\nCPB：❤️❤️❤️❤️❤️\n质地扎实丰润的淡黄色乳霜，极易推开\nSisley：❤️❤️❤️❤️❤️\n质地软糯的米黄色的霜体，延展性非常好\nLa Prairie：❤️❤️❤️❤️❤️\n质地相对轻薄的乳黄色霜，质地看上去水水的，极易延展\n🌷香调气息\nCPB：❤️❤️❤️❤️❤️\n淡淡的植物清香，若有若无很高级\nSisley：❤️❤️❤️❤️❤️\n明显的薰衣草及马郁兰香气让人感觉十分放松舒缓。\nLa Prairie：❤️❤️❤️❤️\n三款霜中它的味道最为芳香浓郁，而且留香时间最久。\n🍃吸收和质感\nCPB：❤️❤️❤️❤️\n吸收速度极快，快速调整肌肤状态，感觉滋润而不油腻\nSisley：❤️❤️❤️❤️❤️\n吸收速度极快，使用后肌肤有紧实提拉感，呈现健康的半哑光状态\nLa Prairie：❤️❤️❤️❤️❤️\n吸收速度极快，使用后肌肤柔软平整，回复水油平衡\n🐲主打功效\nCPB：从1982年到现在已经是第七代的金致乳霜，延续一贯的新肌肤细胞思维理论，一瓶搞定抗皱、紧实、滋润、修护及预防老化的问题。\nSisley：独家抗老三次元理论，延长细胞寿命，细胞级别的修护肌肤。\nLa Prairie：富含高浓度的臻稀鱼子精华以及品牌独有的活细胞精华，有助于促进肌肤中的胶原蛋白生成，并可有效预防其进一步流失。\n👩\u200d👩\u200d👧\u200d👧适合肌肤类型\nCPB：适合所有类型肌肤，尤其是经常受损、失去自律平衡的肌肤，不过小只君觉得南方的大油田肌肤还是要慎重。\nSisley：特别适合城市的亚历山大肌，如果你作息紊乱，喜欢抽烟喝酒，还不怎么爱运动。不想改变生活习惯却又想要完美肌肤，这一瓶能满足你。\nLa Prairie：25岁以后想要对抗初老问题，就感受下鱼子酱的力量吧。乳霜质地比较薄轻盈,很适合年轻肌肤使用，坐标南方也不会觉得油腻。同款面霜会相对丰盈些，适合大干皮和北方的气候。\n👸🏻最后忍不住还要再啰嗦几句，护肤是一件漫长的终身事业，没必要省吃俭用咬牙切齿的去买瓶贵妇霜——那讲真我还不如买个包。可是老话都说好货不贱，诚然有品牌溢价的因素在，仍不可否认每一款贵妇霜都有它身为贵妇的理由。价格不是评判护肤品好坏的唯一标准，平价也确实有它值得点赞的地方。但就个人经验来看，无论是使用感受，还是对于肌肤的真实影响，贵妇产品都是平价产品无法“媲美”的。\n很诚恳的说一句，在预算以内，护肤的银子真没法省。一两个月看不出，放到十年后，你会很感谢今天的决定。#热门面霜评测'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/fb9345bb-c3af957-910b-15a4d1f2daa9_compress_L1',
    'video_id': '58b01147a9b2ed026cae73de',
    'title': '到底哪种解冻肉的方式最有效，今天实验给你看',
    'video_tag_list': '',
    'content': '网上看到好多解冻肉的方法，其中让喵招有点在意的就是在肉的上下铺锡纸。到底这个方法是不是有那么神，和传统的隔水解冻法比起来到底哪个方法会更快更靠谱呢~今天喵招就来实验试试看~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvcbxlHgZXk7lBWhGDoBOnmgnNq-_compress_L1',
    'video_id': '58b302ccd5945f4f1f4c8a4a',
    'title': '单眼皮不简单-眼线篇',
    'video_tag_list': '',
    'content': '有幸被美妆薯选为彩妆新品测试小分队的一员，今天我要测试的产品是植村秀3月即将上市的全新升级版如胶似漆眼线笔。[得意R]\n眼线一定是众多单眼皮们的心头烦！\n费死劲都画不好，不是晕了就是不是好。\n有这种烦恼的旁友们可以试试植村秀的这款如胶似漆眼线笔。\n我选眼线的主要条件：首先持久度要好，其次不会晕或者说不会晕的太过分以及好上手，最后好卸妆。\n💫本人：单眼皮，眼皮爱出油，眼妆不做任何打底。\n💫颜色：黑色。\n💫笔头很细可以说极细吧，属于偏硬的笔芯儿。\n步骤：内眼线👉外眼线👉轮廓\n显色度：💥💥💥\n流畅度：💥💥\n防水度：💥💥💥\n脱妆度：💥💥\n易卸度：💥💥💥\n缺点：1.笔芯是那种旋转式的，只要是转出去了就转不回来了，所以大家在用的时候一定要少量多次！\n2.个人认为超过十小时眼角会晕一些，但是是可以接受的范围。\nPS：我做了小测试 使劲搓揉都不会花\n虽然时间长了眼角会稍微晕些，但是整体还算是OK的。\n最后，\n谢谢大家伙儿的观赏💌'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgftC4rmH1nJ7nIO0XaRyDVprmzO_compress_L1',
    'video_id': '58b3970dd2c8a548eea0b6cd',
    'title': '温和又好用的护肤品❤️',
    'video_tag_list': '',
    'content': '今天来跟大家分享我平时最爱用的几样护肤品，虽然不是我用的全部，不过是我觉得最好用的几样。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/1fddd554a1d89701523383c4f85ac81b98ac61a7_r_ln',
    'video_id': '58b3fb7e7fc5b853f89ce7ab',
    'title': '最适合强迫症的小妙招诞生了! 一瞬间就能撕掉所有的标签',
    'video_tag_list': '',
    'content': '有时候买个超好看的新碗或者新杯，撕掉标签后居然在上面留了胶还有纸的痕迹，简直不能更生气。今天的小妙招教你用家里常有的东西来完美去掉这些烦人的标签哟，除了视频里教的方法，还有用电吹风吹热标签的方法哟~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/59e88be7-664383a-ab9c-04965c7c99e7_compress_L1',
    'video_id': '58b3fbca7fc5b850f29ce7ac',
    'title': '最快开火腿肠的方法在这里了! 赶紧学会吧, 太机智了',
    'video_tag_list': '',
    'content': '想来根火腿肠，手边却没有剪刀的时候，有没有觉得特别尴尬？（我是柔弱的妹子，才不会用牙咬呢）\n没关系，今天的小妙招，我们用一根牙签就能轻松开火腿肠了~画面非常优雅，而且开的很完美嘿=w=\n#肉食动物最爱的美食[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/7c5b2fb57d10ffd02e240aa5dea3f8345a6fc75b_r',
    'video_id': '58b3fc52a9b2ed6ec638de19',
    'title': '煮饭界的奥斯卡, 30秒就能学会用锅煮出超好吃的米饭',
    'video_tag_list': '',
    'content': '小时候一直智障地以为只有电饭锅能煮饭，到稍微大些的时候才知道用普通的锅也可以煮饭。今天的妙招，就是教大家用普通锅煮出好吃的米饭的方法~如果赶时间的话，可以用温水煮饭来加速米的水分吸收。\nPS：如果要煮加入其它配料的饭，比如说蔬菜，蘑菇之类的，加的水要比原来多一些，火候控制的重点是延长小火煮的时间'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrzUXnTRS2zFgFeC833M_YX5f3fO_compress_L1',
    'video_id': '58b4fb90d5945f42050683fe',
    'title': '热门胶类眼线笔使用测评',
    'video_tag_list': '',
    'content': 'Adora胶类眼线笔从质地到色泽都是眼线笔类的不错选择。\n今天Adora找来了三支热门的胶类眼线笔来进行真实测评。\n⚠️：当然测评结果是在这三个产品之间的评测，不带有普遍性。或许这里的一🌟和其他产品比起来还是最优的也说不定哦。[吧唧R]\n1⃣️一号选手：LB鲜奶油超防水眼线笔\n显色度：🌟🌟🌟🌟🌟的确很黑\n流畅度：🌟 膏体没发流畅画出来\n粗细软硬：🌟粗得很难画得细致 膏体偏硬\n防水度：🌟🌟🌟🌟🌟\n脱妆度：🌟🌟🌟🌟🌟\n易卸妆：🌟🌟🌟🌟\nPS.用专门的眼唇卸妆液才是正确的选择 。普通液体、啫喱质地的柔性卸妆产品只适合卸脸上的妆，眼妆会卸不干净。\n2⃣️二号选手：shu uemura 植村秀 新如胶似漆眼线笔\n显色度：🌟🌟🌟🌟🌟绝对黑\n流畅度：🌟 🌟🌟🌟🌟单手操作都没问题\n粗细软硬：🌟🌟🌟🌟🌟细腻柔滑 眼部比较舒服\n防水度：🌟🌟🌟\n脱妆度：🌟🌟🌟🌟🌟\n易卸妆：🌟🌟🌟🌟🌟\n3⃣️三号选手THREE双头眼线笔\n显色度：🌟🌟🌟🌟直观感觉不如植村秀那么那么黑\n流畅度：🌟 🌟🌟🌟还算居中\n粗细软硬：🌟🌟🌟🌟膏体比较软 但画起来没有植村秀流畅\n防水度：🌟🌟🌟\n脱妆度：🌟🌟🌟🌟🌟\n易卸妆：🌟🌟🌟🌟🌟\n手部的测评和真实眼部操作其实也存在一些差异，所以真实的眼部使用感才是第一重要的。产品好坏，使用感说得算哈！@美妆薯'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lk_mp3aVwZWW6pszS6qJ23pwxY8a_compress_L1',
    'video_id': '58b4fbd8b46c5d4a47738e0f',
    'title': '无油健康早餐-香蕉松饼',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n香蕉松饼是一道美食，由香蕉、鸡蛋、鲜奶等材料制作而成。\n今天小圆就教大家在家里做这道无油健康早点。\n★★★★★\n创意指数\n香蕉松饼\n▼\n香蕉松饼\n·食材·\n香蕉、鸡蛋、牛奶\n面粉、糖、黑芝麻\n\u200b\n1.香蕉捣碎成泥\n2.倒入鸡蛋、糖均匀搅拌\n3.倒入面粉\n4.倒入牛奶搅拌均匀\n5.无油小火煎即可\n6.煎至表面有气孔，翻面再煎20秒\n7.简单美味的香蕉松饼开吃啦~！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/6ac4c9579d09d1c24ad8d82840b0e3ca449caa91_r_ln',
    'video_id': '58b56c083460942e6895e8e2',
    'title': '叉子还有你意想不到的作用哟，这么做可以挤柠檬汁，你知道吗？',
    'video_tag_list': '',
    'content': '用手挤柠檬汁的时候，有没有种挤不干净，果肉里面其实还有很多柠檬汁没有挤出来的感觉？但是怎么用力都挤不出来，特别纠结。今天的小妙招，比徒手直接挤柠檬要省力，而且能把柠檬汁挤得特别干净哟~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lr6qCEuSHYhBA7X-d4d42UrdwmlH_compress_L1',
    'video_id': '58b597cf14de41729970137e',
    'title': '米牙的一周健身日志 ：Tueseday打卡咯',
    'video_tag_list': '',
    'content': '近期计划：练习上臀部，提高提高提高😄😄\n今日练臀+腰腹和背激活：\n1、登山机 30分钟 7-8level\n2、侧腰 负重5kg 5组✖️15个 左右都做\n3、上臀部 负重6kg 4组 ✖️20个\n4、全蹲深蹲 15kg杠铃 5组 ✖️20个\n5、器械坐姿腿外展 40.5kg 5组 ✖️20个 练臀姿势\n6、背部激活： 11+2.5kg 拉背 6组✖️ 20个\n总共锻炼时间约1小时 40分钟 （包含间歇休息时间）消耗卡路里估算800卡肯定是有的😗\n希望我给自己的课表可以帮助到大家制定运动计划。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lo_kw9qDgR2JG2d7Wf4JR0uqXzeR',
    'video_id': '58b6223b7836237164a20392',
    'title': '好久不见的日常，哈哈，第一次放飞大疆无人机！😉😉😉',
    'video_tag_list': '',
    'content': '#无人机[话题]#\n好久没有在小红书发日常视频啦！哈哈。\n这次的日常主要就是录了一个减肥期间可以自己在家做的小零食的视频，第一次放飞了大疆无人机。当然，饭也是要吃的！哈哈哈哈哈😜😜😜\n话说自从前几天买了大疆无人机，@大狗熊先生 就沉迷于无人机的研究中，昨天终于去进行第一次放飞了！\n我的大疆是在官网上购买的，具体购买细节和使用方法如果大家感兴趣，晚一些我来写笔记哈，么么哒。😁😁😁@小红叔\n#智能设备推荐[话题]#\n#无人机设备推荐[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/44c30b0abc001e7bdc45110b723a11c3a297cbc9_v1_ln',
    'video_id': '58b67380d5945f6e6c4d9918',
    'title': '小羽私厨之椒盐薯角',
    'video_tag_list': '',
    'content': '这道椒盐薯角很适合朋友聚会时做零食，是那种吃完一块再来一块，然后忍不住还要再来一块的选手。😊'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/2f1ed413f1b3e7511e76e7bad866715b98dab67f_v1',
    'video_id': '58b684b07fc5b8210f4ac3e7',
    'title': '牛人教你怎么吃虾不用手！动作实在太帅气了，我一定要学！',
    'video_tag_list': '',
    'content': '今天教大家剥熟虾壳的实用方法。只要有勺子和叉子，就能手不沾虾地剥出虾壳咯，适合在外吃饭装逼用~也非常适合有洁癖的人嘿嘿~手上也不怕有一股虾的腥味了~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/6c2413213d105e7bc8be2113545942ae306c8ee7_v1_ln',
    'video_id': '58b7954d7836237c1354aec3',
    'title': '小羽私厨之蒜泥白肉',
    'video_tag_list': '',
    'content': '这道蒜泥白肉，在传统白肉的基础上搭配上清新的黄瓜，又凹了个造型，又好看又好吃，绝对是无肉不欢的人的最爱'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltgRxYPKwQPXZweuVMdZUe_UN-ZO_compress_L1',
    'video_id': '58b8dd9e14de41037820f098',
    'title': '【干货附防疫针时间表】瓜子乖宝打针全程无哭闹，赞一个~',
    'video_tag_list': '',
    'content': '💕💕💕瓜子乖宝又打防疫针啦，每次小葵子带宝宝☺️☺️☺️打针心都要碎成渣渣啦，恨不得扎自己身上，小瓜子也是每次出门打针，眉头也是紧锁哈哈哈，惆怅死了，不过宝宝一直很乖啊，打针的时候也是嗯嗯嗯的却没有大声哭闹，针头戳进去的时候还一脸呆萌，往里面推液体的时候会哼唧哼唧的，吓得老公说不是痛觉有什么问题吧，大夫听了就笑了，不会的，这个针头痛感很小，说明你家宝宝承受能力强，真是一个乖宝宝~\n💕💕💕要知道，幼龄宝宝打针可不能出纰漏，有很多需要注意的事情，比如拉肚子发热等特殊情况下都不能打针，大夫说曾经有个家长不当心带着发热的宝宝去打防疫针结果造成了宝宝器官变形，艾玛，听的我浑身起鸡皮疙瘩！\n💕💕💕所以特别附上宝宝们打防疫针时间表及需要掌握的接种禁忌，小红书的准妈妈们、新手妈妈们看过来哇~ 欢迎留言交流哇~\n🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉\n🐷一类疫苗\xa0🐷\n💕出生时： 卡介苗、乙肝疫苗（基础）一个月：乙肝疫苗（基础）\n💕两个月：脊灰疫苗（基础）\n💕三个月：脊灰疫苗、百白破疫苗（基础）\n💕四个月：脊灰疫苗、百白破疫苗（基础）\n💕五个月：百白破疫苗（基础）\n💕六个月：乙肝疫苗、A群流脑苗（基础）\n💕八个月：麻疹疫苗、乙脑疫苗（基础）\n💕九个月：A群流脑苗（基础）\n💕1.5-2岁：百白破疫苗、麻疹疫苗、乙脑疫苗（加强）\n💕3岁：A群流脑苗（加强）\n💕4岁：脊灰疫苗（加强）\n💕6岁：百白破疫苗（加强）、乙脑疫苗、A群流脑苗（加强）\n🐻二类疫苗\xa0\xa0🐻\n💕（1）A+C群流脑疫苗：3周岁注射1针次，6、9周岁各加强一针。\n💕（2）无细胞百白破疫苗：可替代全细胞百白破疫苗，接种程序同全细胞百白破疫苗。\n💕（3）麻腮风疫苗：1.5-2周岁注射一针，基础免疫后4年加强1针。\n💕（4）甲肝减毒活疫苗或甲肝灭活疫苗：甲肝减毒活疫苗接种时间是2岁时注射1针，4年后加强1针。灭活疫苗1-16岁接种2针，间隔6个月，16岁以上接种1针。\n💕（5）水痘疫苗：1-12岁接种1针次。\n💕（6）B型流感嗜血杆菌苗：2、4、6月龄各注射一次，12月龄以上接种一针即可。\n💕（7）流行性感冒疫苗：1-3周岁每年注射2针，间隔1个月。3周岁以上每年接种1次即\xa0可。\n👉👉👉重点来啦👉👉👉                                          👏🏻接种疫苗的禁忌\xa0👏🏻\n🐸（1）卡介苗禁忌： 早产的宝宝、低出生体重的宝宝(出生体重小于 2500 克)、难产的宝宝应该慎种。正在发热、腹泻、严重皮肤病的宝宝应缓种。结核病，急性传染病，心、肾疾患，免疫功能不全的宝宝禁种。\n🐸（2）脊髓灰质炎三价混合疫苗禁忌： 服苗前一周有腹泻的宝宝，或一天腹泻超过 4 次者，发热、急性病的宝宝，应该暂缓接种。有免疫缺陷症的宝宝，正在使用免疫抑制剂(如激素)的宝宝禁用。对牛奶过敏的宝宝可服液体疫苗。\n🐸（3）百白破疫苗禁忌： 发热、急性病或慢性病急性发作期的宝宝应缓种。中枢神经系统疾病(如癫痫)，有抽风史的宝宝，严重过敏体质的宝宝禁用。\n🐸（4）麻疹疫苗禁忌： 患过麻疹的宝宝不必接种。正在发热或有活动性结核的宝宝，有过敏史(特别是对鸡蛋过敏)的宝宝禁用。注射丙种球蛋白'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgukRwxaAumZP-RLQdAb88FAnot0_compress_L1',
    'video_id': '58b8e44bfaa0527ad081c95a',
    'title': '好喝又暖胃的排毒美容饮品--姜枣牛奶',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n姜枣红糖是一道美味而且功效齐全的糖水，只需要用到红枣和生姜就可以发挥很好的功效。\n姜枣红糖中的生姜有杀菌的功效而红枣有养血补气的功能。\n★★★★★\n创意指数\n姜枣牛奶\n▼\n姜枣牛奶\n·食材·\n红枣、牛奶\n红糖、姜\n1.红枣去核，生姜切片\n2.倒入清水煮开\n3.依次倒入红枣、姜片，拌匀\n4.倒入红糖\n5.倒入牛奶\n6.迅速搅匀煮沸即可\n7.好喝又暖胃的姜枣奶茶就完成啦！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/d8efbbb83df93995610b758729e0ffee1d16a4ef_v1_ln',
    'video_id': '58b91c2b3460940fe99aa8e4',
    'title': '都说不能用刀直接切三明治，但是她却能切出完美三明治，秘诀在这',
    'video_tag_list': '',
    'content': '教你切出漂亮的三明治\n切三明治的时候，面包和酱料经常会被刀挤散出来，弄得周围都是，而且切得也不好看。今天小喵招，教你切出漂亮的三明治，以后可以带三明治便当在小伙伴面前晒啦~\nPS：这个方法同样适用于切寿司卷哟！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/002615c2fd643da9fe3746e7fd092d6d3b088131_v1_ln',
    'video_id': '58b91f13faa05252e9703be4',
    'title': '小羽私厨之岩烧乳酪厚多士',
    'video_tag_list': '美食才是人生主角',
    'content': '岩烧乳酪这几年特别火，每次在街边闻到它的香味，就忍不住要买来吃，后来干脆自己在家做了，把料放得足足的#美食才是人生主角[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnfqXSgMDq7xqk7ZLG7G-9sBVFsF_compress_L1',
    'video_id': '58baa72f783623316a70ba93',
    'title': '唇釉怎么涂？视频教你打造欧美厚唇！',
    'video_tag_list': '',
    'content': '视频中用到的唇膏是：阿玛尼红管402 、huda唇釉\n第一次自己录视频剪视频，真的是困难重重，秘制尴尬。视频up主们真的是不容易！！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkS1Es8iAiV56XxeCpxI7euPLmxV_compress_L1',
    'video_id': '58bb7cd5b46c5d0de6ff1c16',
    'title': '🌠流星眉vs 剑眉——哪个大发你更爱？🌠',
    'video_tag_list': '',
    'content': '🌠上次画眉长贴好多菇凉建议我画流星眉。那我今天就来对比一下流星眉和我习惯的剑眉，都是什么样的效果～[害羞R][害羞R][害羞R]\n🌠拍视频太难了好嘛！你们都是怎么做到从容说话的啊？！[扶墙R]这只视频是我关厕所坐马桶上拍的我会说？[笑哭R][笑哭R][笑哭R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvuV0UcB30aRYhcTwRuwsMN8YPHe_compress_L1',
    'video_id': '58bb82f2faa05241ce2715b8',
    'title': '卷发三分钟蓬松术',
    'video_tag_list': '拯救头发油腻的好东西',
    'content': '像我这种细软塌发质的，就算烫了头不打理还是会丑丑的，所以就来分享一下平时出门我是怎么简易的做头发造型的吧～and真不是广告，是在屈臣氏有满减一下买了好几样而已[少女心]#拯救细软发大作战[话题]##拯救头发油腻的好东西[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgxdQSg1dEsoqv1ZWdNiyU6aihyw_compress_L1',
    'video_id': '58bbcd61d2c8a50a94f5e389',
    'title': '南方人第一次见到下雪是怎样一种体验？',
    'video_tag_list': '',
    'content': '第一次见到雪的玛丽，是怎样的呢？？？？？（基本上都是兴奋+吃吃吃…and二月底峨眉山大雪啊金顶变雪顶美到哭泣！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/llJFIQIedu118Ftuk7YufcHpqSOi?sign=f0c51a4c40f55793acf5a771f0c63266&t=65fb06d4',
    'video_id': '58bc095ad2c8a55823f5e389',
    'title': '封面的这款眼妆视频教程终于出炉啦~',
    'video_tag_list': '爱丽小屋;谜尚;资生堂;如何画眼妆让眼睛变大',
    'content': '想知道这款眼妆的画法，继续看视频就可以啦，对了对了，最近感觉眼袋又深了，大家不要嫌弃哦，等我再存点钱，我回去割眼袋哒\n眼影：#极密#4色眼影3号&5号色\n眼线：#极密#多功能笔黑色\n睫毛：睫毛打底膏+4D睫毛膏\n睫毛夹：睫毛夹\n#眼妆每日打卡[话题]##日常眼妆怎么画[话题]##如何画眼妆让眼睛变大[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvgv0O7KaL5WDLl_hrvZUSxsnvWD_compress_L1',
    'video_id': '58bcd81178362353a870ba93',
    'title': '💁🏻吹风机打造自然内卷中发&大发头发爱物推荐💁🏻',
    'video_tag_list': '头发那点事儿;戴森',
    'content': '💁🏻为了拍这个视频我特地洗了个头666，王肉肉都看傻了…我语速本来就快，再1.5倍速编辑简直要飞起！[笑哭R][笑哭R][笑哭R]\n💁🏻真的很烦早上起床头发乱翘，所以洗完头一定要吹呀～视频前3min都是话痨，推荐一些爱物，包括dyson吹风机的功能之类的，想看吹头发的直接⏩快进哈～[得意R][得意R][得意R]\n⚠️好多盆友问梳子链接，马爸爸网搜一下关键词“3d球形梳”，品牌是日本的，叫“lucky”。搜出来价格各种不一，我买的60+。大发觉得这种没啥技术含量的，买到质量好一点的就ok了，五六十块，七八十块都可以哈～[飞吻R][飞吻R][飞吻R]\n#头发那点事儿[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/8256ce2bd89113d73344d0c7fb10fe3ecfc39661_v1',
    'video_id': '58bce0a3b46c5d55aeff1c16',
    'title': '最好的止咳方法—盐蒸橙子',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n不管怎样都比咳得难受要好，也比吃药来的好。★★★★★\n创意指数\n蒸盐橙\n▼\n蒸盐橙\n·食材·\n香橙、盐\n1.水中加盐，将橙子浸泡10分钟\n2.将橙子横切一刀，上面小，下面大\n3.放入碗中，撒上盐，用牙签戳小孔\n4.大火蒸15分钟\n5.挖出果肉，用勺子捣碎果肉\n6.将果肉放入橙皮中，倒入橙汁\n7.蒸盐橙就完成啦~！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/17530add09f9c910ebfb78ec3e2cb129e549556b_v1_ln',
    'video_id': '58bd0bbe7fc5b80cf73477a5',
    'title': '就这一杯，打败所有奶茶店！【曼食快语】',
    'video_tag_list': '',
    'content': '最近办公室的小伙伴都迷上了奶茶店的鲜芋奶茶，下午茶的时间，一下要点十几杯。我也尝了一次，感觉还是自己做的奶茶比较好。\n今天就来做一杯火遍所有奶茶店的鲜芋薏米乌龙奶茶！\n食 材\n⊙香芋泥：芋头200g，炼乳2大勺，牛奶80ml\n⊙奶茶：牛奶250ml，香芋泥随意，薏米随意，浓茶50ml\n步骤\n1.薏米浸泡过夜\n2.薏米沥干水后和清水倒入小锅，大火煮开后转小火煮半小时\n3.芋头去皮切厚块，蒸20分钟\n4.薏米煮至15%呈开花状，捞出待用\n5.蒸好的芋头与炼乳、牛奶一起加入搅拌机打碎，待用\n6.泡乌龙茶\n7.小火煮牛奶，煮至冒小泡之后按口味加入糖，煮开之后立即关火\n8.薏米、香芋糊放入杯中\n9.倒入热牛奶，冲入乌龙茶，完成！\n#办公室下午茶[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ln8TSIR5mYRLKx2HkypaeOsZZ9VV_compress_L1',
    'video_id': '58bd1d5e14de415ad3f294f9',
    'title': '小羽私厨之蔬菜酿鸡翅',
    'video_tag_list': '',
    'content': '做这道蔬菜酿鸡翅完全是一时兴起，当时觉得这么做应该挺好玩的，就试了一下，结果口感竟意外的好'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/bdf0cd3a397a8ad1faf4d681ce7a8dcfd0bfc18f_r_ln',
    'video_id': '58bd1e933460943289f1745e',
    'title': '实拍餐厅是如何清洗顾客用完的玻璃锅具的！这个方法真是简单粗暴',
    'video_tag_list': '',
    'content': '玻璃锅的优点挺多的，耐高温，聚热和保温性能也好，烧开后关火还能沸腾好久。不好的地方就是容易粘锅，底部经常会烧出黑垢，用钢丝球很难擦洗，而且容易磨花。今天的小妙招，小苏打又登场啦~教大家轻松对付玻璃锅这些顽固的污渍~用小苏打水烧开的时候可以看到锅底那些污渍会冒泡哟！特别有趣。'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/8c9d33ea-959658c-8c4e-54837035897a?sign=1c2c7f2f690cb34b282ac927c848929e&t=65fb06d4',
    'video_id': '58bd1ee17fc5b874de93a577',
    'title': '不锈钢勺子还能用来洗手？快速去除烦人的异味',
    'video_tag_list': '',
    'content': '做菜的时候加些蒜味道会香很多，但是切蒜的时候就比较尴尬了，手上会沾上蒜味，洗了好几遍洗手液还会有一股味道残留。今天的小妙招，用一样家里常见的东西就可以轻松去蒜味哟！连金属皂都不用买了~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lowKYeHBfpKRma1Cg_5nOIqAE4N-_compress_L1',
    'video_id': '58bd2225d5945f2d4f86a5aa',
    'title': '#每日穿搭#如何美美绑丝巾，视频教程来咯',
    'video_tag_list': '',
    'content': '因为之前几次穿搭笔记，有搭配丝巾。很多宝贝们，都问丝巾哪里买？怎么绑？今天就给你们来了一个视频哈！\n希望你们喜欢哟😛\n有问题可以留言问我哈！\n我会一一给你们解答😁😁😁'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsZhsyDn4c7F0yLHCj4Vio6Ldg34_compress_L1',
    'video_id': '58bd764814de413ddecdbd4f',
    'title': '【日常妆容打卡 - 简单又快速的工作妆容/10分钟裸妆】',
    'video_tag_list': '罗拉玛斯亚 Laura Mercier 妆前乳;肌肤之钥;香奈儿 Chanel Poudre Universelle Compacte柔光完美粉饼;芭比波朗;Hourglass ;魅可 M.A.C 时尚焦点单色眼影;纳斯 NARS 双色眼影;植村秀 shu uemura 如胶似漆眼线笔 墨黑;植村秀 shu uemura 专业睫毛夹;奇士美 kissme Heavy Rotation MEGA 凄盛浓密防水睫毛膏;sigma;Hourglass  限量版柔光亮颜高光脉络腮红 ;资生堂 Shiseido 时尚色绘尚质修颜腮红高光饼;肌肤之钥 clé de Peau Beauté 光柔粉霜 SPF20 PA++;单眼皮如何画眼妆',
    'content': '#日常妆容打卡[话题]#\n今儿来分享一个日常裸妆给大家，也可以叫她10分钟快速妆容，专治起的晚！\n这个妆容不难，也不会耗费很长时间，适用于任何场合，用到的产品也都是神器哟～\n为了使这个妆容的受众群体更广泛，我采用了一支唇膏展示两种妆效的方法，厚涂可以下班跟小伙伴聚餐，party当然也可以啦！上班见领导就拿纸巾把表面的一层抿掉就好啦😉\n用到产品清单/Products used：\n\n光润粉霜 B10\n魔术底妆刷\n色号20\n129腮红刷\n砍刀眉笔 色号Dark Brunette\n色号Soft Brown\nM.A.C眼影刷217，224\nNARS Kuala Lumpur吉隆坡\n\n\nkissme浓密卷翘防水睫毛膏\nMAC Mineralized Skinfinish/ 矿物质修容粉 色号Dark\nF05修容刷\nHourglass五花肉腮红 Ethereal Glow\npk107 泪沟神器\nSheer Lip Color 唇膏色号10. Carolina\n.\n完毕，谢谢大家的收看哦😘\n#日常眼妆怎么画[话题]##眼妆每日打卡[话题]##单眼皮如何画眼妆[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg12S64iwfVi-ERZguP50rXrnpYZ_compress_L1',
    'video_id': '58be1f1cd2c8a552c66e0eb4',
    'title': '路人变仙女--日常妆',
    'video_tag_list': "日常妆容打卡;芭妮兰 BANILA CO 幻彩修颜液;USTAR 三色修容盘遮瑕膏;伊思  it's skin 晶钻完美蜗牛BB霜;SANA  EXCEL三用细致眉笔;凯婷  KATE 自然眉色染眉膏;纪梵希 Givenchy 四宫格明星哑光定妆蜜粉;汤姆·福特 TOM FORD eye color quad四色眼影;Canmake 唇部遮瑕膏/打底膏;梦妆 Mamonde 发际线粉/阴影粉;资生堂 Shiseido 3D立体超广角213睫毛夹;悦诗风吟 INNISFREE 纤巧精细睫毛膏;3CE 双色高光修容粉饼",
    'content': '今天跟大家分享我平时出门的日常妆哦！\n精致的妆容代表了你的生活态度，\n里面会讲到我化妆的全部步骤和爱用的化妆品。\n化妆品牌子和型号都写在视频里面了哟！\n#日常妆容打卡[话题]#\n1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.#Yolinna唇釉豆沙色\n10.\n11.\n12.\n13.'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltTrF7_xCc3lq4zktkYolHJayy-O_compress_L1',
    'video_id': '58be2c5afaa0521f83ee6dcd',
    'title': '接上条Tripollar使用教程～',
    'video_tag_list': '',
    'content': '这条是跟上条功课一起出哒！\n因为我觉得Tripollar的使用还是需要一定技术的...\n搞不好会烫到记几[吧唧R][吧唧R]\n鹅且Po过这款的人都说凝胶要一点点。具体多少估计大家都不明白～所以\n出了个视频使用教程啦～\nPS：我没有全脸使用（因为前一天晚上刚用完）\n大致给大家示范了一下～效果真的蛮好的。。\n比我用黄金棒和ya-man与没有效果。\n希望给想要入坑的宝宝们一点参考哦！\n【具体使用效果，讲解功课见上条笔记啦】'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhn4c7yBUGx0Nqaee3oF9JDppnme_compress_L1',
    'video_id': '58be7290d5945f38196cbbc4',
    'title': '🏃🏻\u200d♀️腿部阻力练习2（含视频）',
    'video_tag_list': '练出翘翘蜜桃臀',
    'content': '上次发过一个自重腿部练习的视频得到大家的好评，那这次就给大家演示一个不去健身房确有阻力的腿部训练。\n首先需要一条拉力带，然后找一个空间就可以开练啦！😃还有这个拉力带有不同的力度，具体看商家的介绍。某宝搜索：拉力带/弹力带就能看到了..\n---开始---\n1. 左右两侧移动 X 各10个 （拉力带在脚踝部位）\n2. 深蹲 X 10 （拉力带在膝盖上面）\n3. 平行抬腿 X 各10个\n4. 45度后抬腿 X 各10个\n这样做下来四个动作算一组，一共做4组。每组做完后可休息1分钟，再进行下一组。\n---结束---\n⚠️注意的事项：\n1. 腹部要收紧\n2. 头不要摆动\n3. 深蹲时，膝盖不要内扣\n4. 动作停顿3秒，不要快速收回\n如果在健身房深蹲动作姿势不正确的同学可以借用拉力带来纠正动作。\n想看更多健身视频的话，就点击我的主页，里面有更多的视频。有时间的话我就会试着多发些视频，谢谢大家的支持 🙏\n如果有问题就在底下问我吧！[飞吻R]\n#弹力带教学视频\n#腿部塑形视频\n#练出翘翘蜜桃臀[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhqx4LLpxABFgtb6LVW8ys_Bxlgz_compress_L1',
    'video_id': '58be8859d2c8a53f9f6e0eb6',
    'title': '阿玛尼唇釉试色',
    'video_tag_list': '乔治阿玛尼;最难买的唇膏色号',
    'content': 'Hi大家好，今天天气太好所以拍个视频，给大分享阿玛尼唇釉里面我喜欢的几支🤗\n💋阿玛尼红管500\n💋阿玛尼红管501\n💋阿玛尼红管200\n💋阿玛尼红管405\n💋小胖丁504\n看到好多小伙伴比较关心干不干这事儿，我必须认真说一下，红管500和501比较干的，200和405真心不干，虽然都是红管哑光丝绒唇釉，整体上都比较干，但是每个颜色的滋润度还是有区别的。\n小胖丁我用不干，质地特别舒服。\n另外，就是红管200真的比405难买很多。全靠机遇，我也不懂为什么难买得色号我都能刚好遇上😂\n#最难买的唇膏色号[话题]##唇妆试色报告[话题]##阿玛尼唇釉试色[话题]#\n谢谢仙女们的支持，么么哒🤗'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lv7c0EIWWQ5xBAmVCRKlr0oc4EfE_compress_L1',
    'video_id': '58bea38ad5945f60d8c193a7',
    'title': '💪🏻健身日常——练手臂💪🏻',
    'video_tag_list': '见人不如健身',
    'content': '💪🏻吃货管不了嘴只能迈开腿啦…一边椭圆机一边剪视频很酸爽！[笑哭R]练完记得一定一定一定要放松！大发我以前就是只运动不懂得拉伸放松，腿越来越粗。下次有空做个放松的贴好不好～[害羞R][害羞R][害羞R]\n💪🏻蓝鲸的小伙伴，你们都在哪健身呀？来约一个不？～～～[得意R][得意R][得意R]\n💚运动内衣：UNIQLO\n💛运动裤：maia active\n💙鞋：nike\n⚠️视频1.5倍速播放的哟～[飞吻R][飞吻R][飞吻R]\n#手臂塑形视频[话题]#\n#无器械锻炼视频[话题]#\n#哑铃杠铃教学视频[话题]#\n#健身器械教学视频[话题]#\n#厉害了我的健身房[话题]#\n#见人不如健身[话题]#\n#健身穿什么[话题]#\n#手臂如何塑形[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkKGZtRqeASbM3uaYo7ILwxR3CDZ_compress_L1',
    'video_id': '58bf82e114de41140d1f28da',
    'title': '关爱女性：食疗缓解痛经的小妙招—龙眼茶碗蒸',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n不管怎样都比咳得难受要好，也比吃药来的好。★★★★★\n创意指数\n蒸盐橙\n▼\n蒸盐橙\n·食材·\n香橙、盐\n1.水中加盐，将橙子浸泡10分钟\n2.将橙子横切一刀，上面小，下面大\n3.放入碗中，撒上盐，用牙签戳小孔\n4.大火蒸15分钟\n5.挖出果肉，用勺子捣碎果肉\n6.将果肉放入橙皮中，倒入橙汁\n7.蒸盐橙就完成啦~！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/16c3aaa6-d471921-bd42-e7a641a56b84?sign=a095d422146c53a03b69ea444df5c94c&t=65fb06d4',
    'video_id': '58bf9f823460945fe515213c',
    'title': '護眼產品該怎麼選',
    'video_tag_list': '',
    'content': '針對葉黃素、藍莓、黑豆種皮、維生素a之適應正說明'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/eeab95bfe747d532be3730adfe49e5452b98103d_r_ln',
    'video_id': '58bfd0067fc5b8466f5edf27',
    'title': '我们才不过妇女节，女生节创意甜品,教你自制微波炉焦糖布丁',
    'video_tag_list': '',
    'content': '今天是粉红粉红的少女节呀，乙女们！不如做个满满少女心的焦糖布丁犒劳一下自己吧~之前看很多私信和评论说没吃过布丁的，所以今天教大家超简单的布丁做法。材料仅需要砂糖，水，鸡蛋，牛奶，耐热容器和微波炉就可以啦~\n步骤：\n1.在耐热容器中加砂糖1大勺和水1小勺，微波炉中高火加热1分半做布丁的焦糖。\n2.在另一个稍大的容器中加入蛋，砂糖2大勺和牛奶120毫升搅拌均匀做布丁液。\n3.布丁液过筛后倒入刚刚做好焦糖的容器中，用微波炉低火加热5分钟（记得加热时间不要太过啊！宁少不多啊！）\n4.冷却10分钟，就可以开吃啦~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltHhtxAMAfAiaQlu2c_6OJyK6j5A_compress_L1',
    'video_id': '58c0339a14de413b471f28da',
    'title': '宇宙奶茶店喜茶排队攻略&新品试饮',
    'video_tag_list': '这家奶茶店的奶盖超好喝;喜茶HEEKCAA·广州花城汇南店',
    'content': '不务正业的美妆博主又来了！\n这次给大家带来的是\n一家红遍广州and上海的奶茶店－－喜茶！\n据说上海排队可以到四五个小时？？？？？？\n广州人民表示不解，然后花了五分钟点单半小时等茶，顺便尝了一下新品[得意][得意][少女心][少女心]#排队超久的人气奶茶店[话题]##这家奶茶店的奶盖超好喝[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrptrC1EZ2XGgYZCqGz_vaKQR6ay_compress_L1',
    'video_id': '58c038fbd5945f601a8ab031',
    'title': '三生三世十里桃花白凤九仿妆',
    'video_tag_list': '明星仿妆我最像;迪奥 Dior 魅惑丰唇蜜;植村秀 shu uemura 如胶似漆眼线笔 墨黑',
    'content': '#创意仿妆秀[话题]# 来晚啦来晚啦，三生三世已经播完了我才开始拍仿妆。迪丽热巴演的白凤丸真的太可爱了！仿的是妆不是人勿喷，and用品都写在视频里的了不要再问我用的是什么了，自己看好吗，我懒死了[得意]ps衣服是我的睡袍哈哈哈哈哈哈哈#明星仿妆我最像[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpV4p4Q0nK3HoYzdoTOWOr8iEEnF_compress_L1',
    'video_id': '58c0cca9d5945f4a393419c2',
    'title': '初春补气神器—白菜豆腐羊肉锅',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n羊肉的肉质细嫩，容易消化，高蛋白、脂肪含量很少，是防寒温补的美味菜肴。\n羊肉性温，常吃羊肉，还可以增加人体热量，抵御寒冷，帮助消化，起到抗衰老的作用！\n★★★★★\n创意指数\n白菜豆腐羊肉卷\n▼\n白菜豆腐羊肉卷\n·食材·\n娃娃菜、羊肉卷、北豆腐、香菇\n胡萝卜、葱、蒜\n料酒、生抽、盐\n1.豆腐切块\n2.胡萝卜切片\n3.香菇切花刀\n4.娃娃菜切块\n5.葱蒜切末\n6.热油锅爆香葱蒜\n7.倒入羊肉卷炒至出油备用\n8.倒入娃娃菜\n9.加入热水\n10.放入豆腐、胡萝卜、香菇大火煮开\n11.沸腾后加入料酒、生抽、盐拌匀\n12.小火炖煮5分钟倒入羊肉\n13.早春补气神器上桌啦~！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqgbao7dTIQFqzAYrMvj5mJu4euN_compress_L1',
    'video_id': '58c0e11cfaa0521c2d849b42',
    'title': '【视频】单眼皮驾驭chanel268红棕色眼影',
    'video_tag_list': '单眼皮如何画眼妆;Suqqu 自然平衡三色眉粉 附刷子;香奈儿;赫莲娜 HELENA RUBINSTEIN 蕾丝睫毛膏;凯婷  KATE 睫毛打底膏;奇士美 kissme 花漾美姬泪眼不晕染眼线液;Suqqu 银色超级睫毛夹',
    'content': 'Hi大家好，视频妆容分享来喽💃🏻\n香奈儿268这盘眼影火爆程度不用多说，我一开始不怎么长草，结果每天被各种刷屏，每个人都要夸赞一翻，又这么难买，价格被炒的很高，所以我就说，一切随缘吧！\n没想到，真的被我买到了。\n今天刚刚开封，第一次画，想要打造一个适合单眼皮的红棕色眼妆，效果我自己很满意哦～\n不得不说我今天搭配的唇膏也是出乎意料的喜欢，chanel2017春季唇膏新品62，现在好像刚有一点风吹草动，已经不太好买，如果喜欢就赶紧下手，再火一点就更难了。\n🍷🍷🍷我不是什么专业的美妆博主，一切都是因为爱好，喜欢玩彩妆，兴趣使然所以才做分享，如果大家觉得好玩或者有收获，我会很开心，谢谢你们的支持🙏，如果觉得不好玩看不下去，也请多些善意。\n有缘相识，无缘陌路。感恩我善良的小仙女们，我记忆力还不错，经常留言给我的我都有印象，谢谢你们常来看我，手动比心❤❤❤\n#四色眼影盘怎么画[话题]#\n#单眼皮如何画眼妆[话题]#\n\n\n\n\n\n'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lpW8fE0erWovmbgU9e7XUFUrD5KQ_compress_L1',
    'video_id': '58c10b207836235f53acb481',
    'title': '戴眼镜的眼妆怎么化！三分钟出门啦～',
    'video_tag_list': 'ZOEVA;植村秀 shu uemura 如胶似漆眼线笔 墨黑;植村秀;赫莲娜 HELENA RUBINSTEIN 猎豹睫毛膏 - # 01 黑色 Black Black ;赫莲娜;爱丽小屋 Etude House my little nut 胡桃夹子Play101多功能眼影笔 限量版;眼镜妆也美丽',
    'content': 'hi～我是每只眼睛有450度滴四眼妹Adora #眼妆每日打卡[话题]##日常妆容打卡[话题]##眼镜妆也美丽[话题]#\n天天戴隐形眼镜和美瞳偶尔眼镜不舒服可怎么办😭😭😭\nso戴眼镜也不能吃藕啊😜\n眼镜虽然有修饰脸部滴作用同时也会遮挡我们眼镜的美，那么就要配合👓先生显现出双眸魅力啦\n⚠️选择眼影建议裸色或是南瓜色以及所有日常清洗的色盘。我选择了你们最最最爱的carmel melange南瓜色🎃来示范喽。用其中的4个哑光色和一个金属色打造清新立体的眼镜眼妆。\n⚠️眼线 只化内眼线即可，不要太过浓重会丢了戴眼镜的纯美哦[活力]\n我对这支眼线笔的爱无法用语言形容[喜欢]好用到感人啊\n⚠️睫毛膏#赫莲娜 HELENA RUBINSTEIN 猎豹睫毛膏 - 建议选择纤长自然不结块滴。最贴近自然的睫毛才是动人滴睫毛[得意]\n⚠️窝蚕  选择珠光体量滴窝蚕笔 加大清新值\n好啦！三分钟over滴眼妆可以出门啦[少女心]\n#跟着视频画眼影[话题]# #日常妆容打卡[话题]# #眼镜妆也美丽[话题]# #眼镜妆教程[话题]#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lpQpr_23B9CagpiztOq1kaRHl7OH_compress_L1',
    'video_id': '58c1354d14de4167935a07b3',
    'title': '粗略的渣渣图教程',
    'video_tag_list': '',
    'content': '其实我p照片最麻烦的就是推推推啦\n用的第1⃣️个软件是facetune\n跟美图秀秀比起来\n这个推没那么好控制\n因为没有圆圈在\n但我太喜欢这个的平滑了\n比较自然跟relook比起来\n如果美图秀秀推完再来facetune平滑的话\n太麻烦了\n所以现在就多练习练习😂😂\n第2⃣️个软件是VSCO\n平常都是用这个调景色或者吃的\n因为有调过的的照片在\n所以直接复制编辑就好\n每张照片就都是同一个色调了\n第3⃣️个软件就是instagram\n人像的调光我是比较喜欢用这个的\n这个滤镜比较好看\nVSCO里面滤镜有点太多啦\n决定不下来'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/2740b2214b0611919bf209caf75ce34d235490df_v1',
    'video_id': '58c2206b783623370eed0bcf',
    'title': '抗癌明星蒜蓉西兰花，美味小技巧',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n蒜蓉西兰花是一款清清淡淡，做法又简单的家常小炒，耗时短，很方便。\n西兰花是防癌抗癌的明星蔬菜，热量非常低，非常适合于减肥。★★★★★\n创意指数\n蒜蓉西兰花\n▼\n蒜蓉西兰花\n\u200b\n·食材·\n西兰花、蚝油、蒜、盐\n1.西兰花切成小块\n2.西兰花沸水中焯至变绿\n3.沥干过冷水\n4.蒜切片、末\n5.起油锅蒜片炒至焦糊盛出\n6.倒入西兰花翻炒，加少许盐\n7.盛出摆好造型\n8.起油锅倒入蒜蓉、蚝油清炒\n9.加入适量清水炒至粘稠\n10.淋上酱汁\n11.小资生活从这一刻开始~！\n#超级下饭的家常菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/lpqrGE28q29IrBf5iLMcKf-lTbR4?sign=4d821c4e827ddf8b955feec21315b42b&t=65fb06d4',
    'video_id': '58c220dbd1d3b93c6e780feb',
    'title': '小羽私厨之龙利鱼狮子头',
    'video_tag_list': '',
    'content': '这道用龙利鱼做的狮子头，鲜美可口，又很清爽，非常适合有老有小的全家宴。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsQwztFgmnewXgq8OJG5I4tRC3xC_compress_L1',
    'video_id': '58c28b41d1d3b95393094d0a',
    'title': 'Lime Crime独角兽唇彩视频多色试色',
    'video_tag_list': 'lime crime;lime crime VELVETINES独角兽哑光雾面唇彩;唇妆试色报告',
    'content': '🦄️独角兽Lime Crime铁粉#唇妆试色报告[话题]#\n今天选了我使用率最高的几支Lime Crime的唇彩进行视频展示\n虽说唇彩这个东西因人而异，but图片上的美色到底在真实生活中到底啥样子会根据光线、妆容、皮肤态、角度等等因素而不同。so 视频都是在环形灯状态下真人试色，加上动一动角度不同会更立体滴感受美色到底啥样子啦啦啦\n好啦 这几支独角兽唇彩出境顺序为：\n1⃣️Lola\n2⃣️pink champagne\n3⃣️elle（看着特别nude涂上美腻没想到啊）\n4⃣️bleached（桃粉裸 大爱） 赶紧收了这支[得意]\n5⃣️cashmere（这是一支被国外达人各种爱的颜色 貌似亚洲女生没那么完美效果）\n6⃣️red velvet（大红）插播一句小红书里有卖的⚠️suedeberry是发橘色的红 ，涂不来大红色的可以选这支 翘美啊！拯救涂不来红唇👄的人[喜欢]这就是我人生中第一支红色 ，涂上不会被妖魔的红[得意]\n7⃣️salem（发棕的裸色）话说真心类似wicked，还是这支wicked更美更紫红色  酷到绝对类似破产姐妹的Max'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/2afe89c9-1df460d-8748-2b912f205b52?sign=f3fbb87126dc4ebfeb49387f4b5ddfa6&t=65fb06d4',
    'video_id': '58c28cc67fc5b8548a06fcff',
    'title': '根本不用买专业量勺，利用身边的小东西，也能变成专业料理达人',
    'video_tag_list': '',
    'content': '喜欢看着食谱做饭的小伙伴们肯定都有过这样的问题，1大勺是多少，1小勺又是多少？没有量勺的话，这大勺和小勺应该怎么把握？这个时候，就要掏出我们的神器——瓶盖君啦！300ml饮料的圆瓶盖基本都是一样的规格哟，以后就不用买量勺啦（机智脸）'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpppVcTteZbIZXjIWk48ueqSO4RR_compress_L1',
    'video_id': '58c36218d2c8a551bf10acf2',
    'title': '💪🏻迎接夏天——练出美背💪🏻',
    'video_tag_list': '',
    'content': '💪🏻周末早安，加班🐶大发发来问候～[哭惹R][哭惹R][哭惹R]\n💪🏻上次健身视频发出以后，有盆友问怎么练背，刚好周四健身练了背，个么就喊教练帮我拍了每个动作的视频，剪在一起啦～[害羞R][害羞R][害羞R]\n💪🏻周四主要练背，顺带最后练了点腹部。最后一个练上腹的动作我是真的没劲了，一点儿也不标准，大家别打我…[笑哭R]练完动作照例要接有氧，这样健身效果最高效。我这次接的是跑步机快走，坡度6速度5，40min以上。练完务必拉伸放松哟～[飞吻R][飞吻R][飞吻R]\n💪来说一下我对建身的态度吧。私教对于我还是蛮有必要的。工作五年健身五年，从刚开始自己拼命有氧到请了私教系统训练，其中的差别是很明显的。很多动作都是在接触了私教课后才知道原来自己根本就练错了，劲儿没使对，天天累的半死还成效甚微。[叹气R][叹气R][叹气R]\n💪🏻视频后面有我跟我教练的合照，每次照片视频都是麻烦他帮我拍哒，身材棒棒的，颜值高高的（嗯没错他逼我说的🙄️），重点是练！的！好！[得意R][得意R][得意R]'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/ljjWXEZmpXVM848nXDZTX48n48hb?sign=b69b86a54dac2efcf7066f11b6757ff8&t=65fb06d4',
    'video_id': '58c3962ad5945f3ee0bc973d',
    'title': 'DAISO大创生活小物分享',
    'video_tag_list': '大创;那些生活中的神器',
    'content': '#那些生活中的神器[话题]#\n提起大创，我想大家一定不陌生，比如大创面膜罩、大创洗刷液、大创睫毛雨衣~都是很红的小物品，其实大创的奇思妙想远远不止这些哦。很多生活小物品都有很好的创意，我之前就很喜欢大创的生活小物，但是我这个拖延症一直没出笔记，所以这次即直接给大家上视频，也比较直观。\n视频上的物品依次顺序：\n1.\xa0\xa0\xa0\xa0\xa0\xa0 DAISO大创 亚克力透明小物收纳盒\n2.\xa0\xa0\xa0\xa0\xa0\xa0 DAISO大创 地垫\n3.\xa0\xa0\xa0\xa0\xa0\xa0 DAISO大创 抽屉分隔板\n4.\xa0\xa0\xa0\xa0\xa0\xa0 DAISO大创 吸盘挂钩\n5.\xa0\xa0\xa0\xa0\xa0\xa0 DAISO大创 毛巾架\n6.\xa0\xa0\xa0\xa0\xa0\xa0 DAISO大创 玫瑰花朵餐垫\n7.\xa0\xa0\xa0\xa0\xa0\xa0 DAISO大创 夜光开关贴\n8.\xa0\xa0\xa0\xa0\xa0\xa0 DAISO大创 洗碗海绵\n9.\xa0\xa0\xa0\xa0\xa0\xa0 DAISO大创 海绵收纳架\n10.\xa0\xa0 DAISO大创 硅胶手套\n11.\xa0\xa0 DAISO大创 抹布\n12.\xa0\xa0 DAISO大创 分隔化妆收纳盒\n13.\xa0\xa0 DAISO大创 洗衣皂\n14.\xa0\xa0 DAISO大创 便携湿巾\n💖💖💖\n@生活薯\n好啦，就是这些。之前的慢慢刚分享给大家。(* ￣3)(ε￣ *)'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqnww9l-as9WE_opHkVEgivoPmkV_compress_L1',
    'video_id': '58c4eddcfaa052791e4d6287',
    'title': '',
    'video_tag_list': '乐高;视频推荐玩具',
    'content': 'LEGO乐高 大众T1野营车\n型号：10220\n拼装完成✌️\n\n#视频推荐玩具[话题]#\n#家有玩具大推荐[话题]#\n#玩不腻的益智玩具[话题]#\n@视频薯  @娱乐薯  @生活薯'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/431b87df8245dab029077f5d60109872542bdf7a_v1_ln',
    'video_id': '58c545c77fc5b834afc59fbc',
    'title': '在泡发香菇之前一定要放一样东西，但很多人不知道',
    'video_tag_list': '',
    'content': '很多人习惯用开水泡发香菇，但过高的水温会导致香菇鲜味流失。泡香菇最好的方法，就是用温水，水中加一些白糖的话可以更好地锁住香菇中的鲜味。这里还有个小窍门，想更快速泡发香菇的话，可以把香菇根掰下来再泡哟。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvYU5MJ_aWbctvbo3DfvBJvm6IPh_compress_L1',
    'video_id': '58c5ae1814de415cbfcfb6ac',
    'title': '搓澡舞',
    'video_tag_list': '',
    'content': '我被这歌洗脑了好几天\n终于有一个人愿意跟我一起玩了\n哈哈哈\n#舞蹈教学视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/5473a1f434f89e337331b0c6b4b9f7c1876af19e_r',
    'video_id': '58c61666faa052469525ff44',
    'title': '一学就会的“鱼香肉丝”做法',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n“鱼香”与“余香”谐音，另一种说法是“余香肉丝”。余香系列的川菜，最主要的辅料是四川辣豆瓣酱。\n主料配以四川辣豆瓣酱加上其他调料烧出来的菜肴，其味厚重悠长，余味缭绕，回味无穷，称余香。\n★★★★★\n创意指数\n鱼香肉丝\n▼\n鱼香肉丝\n·食材·\n猪里脊、莴笋、黑木耳、胡萝卜\n蒜、姜、葱、豆瓣酱、盐\n糖、醋、料酒\n生抽、老抽、生粉\n1.黑木耳用40°热水泡开\n2.倒入料酒、生抽、老抽、盐、油、生抽\n3.拌匀后腌制15分钟\n4.将醋、生抽、料酒、糖、盐混合调制鱼香汁\n5.莴笋去皮切片\n6.葱姜蒜切末\n7.热锅冷油倒入猪里脊炒至变色盛盘备用\n8.热油锅爆香姜蒜末，倒入豆瓣酱炒至出红油\n9.依次倒入黑木耳丝，胡萝卜丝，莴笋丝\n10.清炒片刻倒入里脊肉迅速炒匀\n11.倒入鱼香汁\n12.大火爆炒1分钟收汁\n13.最好撒上葱花，超级下饭的鱼香肉丝就做好啦~！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/5619c08a9c8422b5159e262442599f43641d4f69_r',
    'video_id': '58c66374a9b2ed1cd12d91c6',
    'title': '食用小苏打不仅可以用来烘焙，背后还有那么多生活小技能',
    'video_tag_list': '',
    'content': '小苏打是个神奇的好东西，真希望每个人家里都能有(>`ω´<)既能食用又能拿来做各种生活用品，比如万能的清洁剂，还有除湿剂等等，真是家庭必备神器。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llMJb_c5Fsg0E2IqBd-JbrIa5ElG_compress_L1',
    'video_id': '58c6ceead1d3b910a6b51004',
    'title': '白色情人节应景巧克力妆容',
    'video_tag_list': "巧克力与爱;我的情人节;I'M MEME 我爱十色眼影盘;I'M MEME 我爱眼线笔;I'M MEME 我爱粉底棒;I'M MEME 我爱眉笔;I'M MEME 我爱遮瑕膏",
    'content': '又是深夜踩点发视频的玛丽！314白色情人节，不知道大家都有啥安排呢，没安排不如把自己化成巧克力girl去融化他的心吧[得意]#我的情人节[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljis5WIhBw7uot3uyuLcvQOacWQh_compress_L1',
    'video_id': '58c76f21b46c5d10c8d68e1c',
    'title': '想保留最鲜美的滋味就这样吃—爆炒蛏子',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n爆炒蛏子是一道特色名菜，属鲁菜系。色泽美观，鲜香味浓，可口美味，是简单美味的海鲜下酒菜。\n味甘、咸，性寒，有清热解毒、补阴除烦、益肾利水、清胃治痢、产后补虚等功效。\n★★★★★\n创意指数\n爆炒蛏子\n▼\n爆炒蛏子\n\u200b\n·食材·\n蛏子、青椒、红米椒、青米椒\n葱、姜、蒜\n豆瓣酱、生抽、盐\n1.蛏子倒入盐水中两小时待其吐沙\n2.青椒切丁、红青米椒切小圈\n3.葱切段、蒜切末、姜切丝\n4.热油锅倒入豆瓣酱炒至出油，倒入葱姜蒜爆香\n5.倒入青椒、青红米椒清炒片刻\n6.倒入生抽\n7.倒入蛏子爆炒1分钟\n8.别怕辣哦~！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljh6sC-gBz9d-Fb1AJ9KXRoJFX_j_compress_L1',
    'video_id': '58c7843a783623623b4035c8',
    'title': '莓果色妆容💜',
    'video_tag_list': "粉底持久度大比拼;I'M MEME",
    'content': '白色情人节来点不一样！\n莓果色妆容💜\n#日常妆容打卡[话题]#\n#粉底持久度大比拼[话题]#\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/lgjCnv_qle0qlD3kxeajdx52TrDK',
    'video_id': '58c78d5bd5945f46f8fc1e53',
    'title': '小羽私厨之炒年糕',
    'video_tag_list': '',
    'content': '“”韩式辣酱炒年糕”这个有名的韩国小吃并不是炒出来的，而是加水跟辣酱煮出来的。吃起来香香辣辣，很有嚼头。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/5445eb7a769be495620ed848bc6b601e44af811f_r',
    'video_id': '58c7a8187fc5b82baa545009',
    'title': '百年蜂蜜老字号，结晶已久的蜂蜜却被人一分钟就搞定！',
    'video_tag_list': '',
    'content': '蜂蜜结晶后高于40度会逐渐开始融化，但是温度过高的话又会破坏蜂蜜的营养。因为之前挺多评论和私信问蜂蜜结晶怎么恢复，所以今天就教大家两种方法恢复结晶的蜂蜜，高于40度低于60度是恢复蜂蜜结晶的最佳环境，所以温度的把握还是挺重要的。\nPS：加热的时间会因结晶的程度和量会有些不同，所以建议一边观察一边操作哟~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lj86RfHPv0_AhWyZO0c9hEgGkhp4_compress_L1',
    'video_id': '58c8cada14de4143a5759373',
    'title': '春季的“黄金菜”：清炒莴笋',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n清炒莴笋是一道美味的菜肴。\n特点清炒莴笋制作简单，营养丰富，口感良好。\n★★★★★\n创意指数\n清炒莴笋\n▼\n清炒莴笋\n·食材·\n莴笋、红米椒、盐\n1.莴笋去皮切片\n2.红米椒切圈\n3.倒入莴笋快速翻炒\n4.撒盐调味\n5.摆盘用红米椒点缀\n6.简单又美味的料理就完成啦~！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvuRhBa5XF4aqKGIwM77K4N_byxh_compress_L1',
    'video_id': '58c92736d5945f0f726a34c1',
    'title': '#丸子头大作战#女神经视频搞笑分享解说🤣超easy✌🏻',
    'video_tag_list': '',
    'content': '啦啦啦！\n粉4000来po个视频🤣\n🌚如果掉粉就怪自己不作不会死😆\n原因就是我真的帮身边超多的同事闺蜜都扎过丸子头\n这个方法真的超级简单👍🏻\n一根皮筋搞定好嘛！\n超级快！一分钟差不多就可以扎好了！😅✌🏻\n不喜欢请绕道…[活力]\n喜欢的点个赞🤣👍🏻\n衣服是郭先生这次泰国买的，之前有po\n妆是早上化的\n化了一天居然也没掉我也服了！[装酷]\n大家随便看看吧！🤣\n好多妹子都说试过成功了！\n啦啦啦！！\n[少女心][少女心][喜欢][喜欢][装酷][装酷][得意][得意][活力][活力]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/2c2c1d167ea28bffa7f69b307afa7fce3d2d9e7f_v1',
    'video_id': '58ca679d3460944e9e5a4cf7',
    'title': '回形针解决生活中5种尴尬的问题',
    'video_tag_list': '',
    'content': '#视频教你生活小窍门[话题]#\n回形针是个好东西~除了平时的学习办公，还有生活上的用途~今天喵招教你回形针的5种实用的用法，可以非常轻松地解决生活上一些问题哟！\n1.解决透明胶带找不到撕口的问题\n2.自制书签\n3.代替爱疯的取卡针\n4.书包的防盗锁\n5.修理坏掉的拉链'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpev3FirUxuB9UHKez2gcrNO1u-t_compress_L1',
    'video_id': '58ca76ddd5945f3d5f56185a',
    'title': '底妆美到让直男放下王者荣耀',
    'video_tag_list': '轻薄底妆如何画',
    'content': '啊哈哈哈，标题不要太欠抽，\n是同事帮我改的！不过...我喜欢🙈✨\n今天跟大家分享一个我平时最最最爱的上底妆手法，这样可以让我们的底妆更加贴服，水润，均匀而且更加持久！！😎✌🏻️\n⚡️✨\n今天选用的粉底液有点厚重，\n适合喜欢遮瑕度比较高的妹纸，\n但是手法一定要get哦！\n还有大家记得不要忘掉脖子的地方～\n无论是上妆的时候还是卸妆的时候😎\n#完美底妆这样画[话题]#\n#轻薄底妆如何画[话题]#\n#视频教你画底妆[话题]#\n#粉底持久度大比拼[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmSDiouXLoldcQXQPjoyfaPFzSp0_compress_L1',
    'video_id': '58cb549814de4141f024d534',
    'title': '鲜上加鲜的做法—清蒸桂鱼',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n清蒸桂鱼是一道福建的汉族传统名菜。\n属于闽菜系，其特色为色泽淡稚悦目，味似蟹肉，鲜香馥郁。\n★★★★★\n创意指数\n清蒸桂鱼\n▼\n清蒸桂鱼\n·食材·\n桂鱼、火腿\n大葱、蒜、姜、葱\n白酒、蒸鱼豉油、盐\n1.去内脏后，从头向下斜切出几条平行的刀口，只切单面\n2.鱼身撒盐\n3.刀口处、鱼肚内均匀涂抹，\n4.切葱段、姜片\n5.切大葱、蒜片\n6.放置备用\n7.将桂鱼移至葱段和姜片打底盘中\n8.鱼腹内塞入姜片、葱段\n9.淋白酒去腥\n10.切口处插入火腿片\n11.大火烧开水后，等蒸汽上来放入桂鱼蒸8分钟\n12.蒸到第5分钟时开锅倒入蒸鱼豉油\n13.起油锅下蒜片、火腿丝、大葱丝，大葱丝断生即可\n14.趁热倒在桂鱼身上\n15.再用香菜点缀即可上桌'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqMeYwsMmAWG_qxFKIAaKtq5QfLa_compress_L1',
    'video_id': '58cb5888d2c8a515f86f0a02',
    'title': '【泰国穿搭合集】曼谷—芭堤雅—清迈',
    'video_tag_list': '',
    'content': '越来越爱用视频的方式记录下旅行的足迹\n之前去了泰国十天\n曼谷3天2晚—芭堤雅3天2晚—清迈5天4晚\n最喜欢的还是在清迈的日子 特别的悠闲自在\n所以视频中出现最多的也是清迈的景色\n有没有看到熟悉的地方呀[喜欢]'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lqnWlJgjhCPm5Q3saEuZSi3qk-id_compress_L1',
    'video_id': '58cc8409d2c8a518f4ec2d51',
    'title': 'VR日上免税店半日游+虚拟现实游戏馆',
    'video_tag_list': '',
    'content': '📒之前发过文字版笔记，补上视频～第一次出镜献丑啦！\n❤️这次的体验，加心最喜欢的是VR日上免税店（游戏也喜欢），这里不用护照、不用排队、顺丰包邮...最重要的是，库存和价格跟机场日上免税都是一模一样。\n🎁为我们这种一下子适应不了VR购物的人，这里还提供了PC版，在电脑上就可以看货下单了！简直是福音啊，果断摘下眼镜，挑到了纪梵希禁忌之吻16号——大热色黑色唇膏梅子色，用银联卡线上付了款，心满意足。\n❤️场馆名称：趣味人VR购物体验馆\n地址：上海国际旅游度假区核心区申迪东路399弄188号G-CUBE创艺方2层201室\n交通：11号地铁线迪士尼站下车，3号口出来直走看到GPark的标志，以及一个大型的变形金刚，它手指的方向就能看到G-CUBE的场馆啦，具体位置是在二楼。\n💰单独玩任何一个区域是160元；套票价格300元包含两个区域。\n游戏区的项目也可以单独玩，价格写给大家——魔力互动 49元；无限驾驶 59元；无限畅游 29元；太空舱69元。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/d50908d32e296941581a8bd1149030d37969cb51_v1',
    'video_id': '58ccbbd8a9b2ed40a626bfe2',
    'title': '接上篇短笔记，小红书曼谷outing的视频也出炉啦啦啦',
    'video_tag_list': '',
    'content': '拍摄时间：2017年3月11日~14日\n视频时长：3:38\n视频内容：小红书员工曼谷ouitng\n咳咳咳，一切尽在不言中哈哈\n💗💗💗\n广告时间：\n小红书还在招人奥~ 希望下一次出行也有你的身影~\n岗位详见小红书app“薯管家”ID、各大招聘网站或www.xiaohongshu.com/join\n么么哒！~[害羞R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loKhQNs72CleCIBxR6vkL-cDeHBn_compress_L1',
    'video_id': '58cd1ce37836236b948400a8',
    'title': '不用出去美甲店自己也可以diy华丽丽的美甲嗷',
    'video_tag_list': '亮片美甲惹人爱',
    'content': '手残党玛丽居然能给大家发美甲教程，笑死人了！啊哈哈哈不过这个真的是我在家自己做的，以我这种手残程度来看，也是rio简单，真的。假睫毛胶水&亮片小碎钻简直是神器！来学起来吧[得意]#DIY美甲教程[话题]##亮片美甲惹人爱[话题]##美甲时不能少的亮油[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/lvjJoOJlt7Qy0Jb0NHeY-J81dsx8?sign=47f232451f8b75413b9632c060be6b0f&t=65fb06d4',
    'video_id': '58cd497e14de416f93c5d0a0',
    'title': '#半丸子头教程#怎么都不会掉的哟！超简单✨🤣不笑算我输',
    'video_tag_list': '',
    'content': '答应宝宝们的半丸子头教程\n哈哈哈哈…\n建议屏住笑观看…\n女神经美不过三秒…\n郭先生说这样下去会掉粉[石化]\n啊哈哈哈哈哈…\n我不怕啊…因为这就是我啊！\n喜欢的点赞❤️\n不喜欢…咋整啊…\n😅随便看看吧…我自己都觉得拍的太丑…'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkwmzqVdyWT26iX9dRcToWxeG4gO_compress_L1',
    'video_id': '58ce1684d5945f1b6ed44e8d',
    'title': '【视频】打造单眼皮橘棕色眼妆之cpb316',
    'video_tag_list': '单眼皮如何画眼妆',
    'content': '#单眼皮如何画眼妆[话题]#Hi大家好，今天给仙女们分享一下我的另一盘挚爱的眼影cpb316🎉🎉🎉🎉除了火出外星的chanel 268红棕色，我个人觉得cob316橘棕色也非常值得收😘\n重点是单眼皮也一样可以驾驭哦💖美美哒\n🍃dior眉粉\n仙女们，上一篇长笔记我的眉粉眉笔测评有没有看💃🏻没看的快去看哦😘😘\n🍃ka修容膏 好用好用 特别爱！\n🍃cpb眼影316\n橘棕色，超美啊，去年也是火的不行，不过你们知道我很喜欢橘色，所以毫不犹豫就早早预定了，我觉得真的是太美，一年四季我都要拿出来画🙈🙈\n画法认真看视频哦，单眼皮妹纸们请抱紧我🤗🤗🤗画法很简单，日常又好画才是常态\n🍃眼线笔kissme\n一直用这款哈哈哈哈哈\n🍃HR蕾丝睫毛膏\n最爱用的一款，浓密纤长都不错，不过最近发现CT也不错😘\n🍃suqqu睫毛夹\n🍃smashbox唇釉outloud\n🔥🔥🔥🔥这么火的唇膏还有人不知道吗，是的我竟然我不知道，被朋友推荐来的，真心是我的本命之一啊，脏橘色💥💥💥好看炸啊，你们看我的阿玛尼唇釉试色那个视频就知道，我超喜欢吃土色脏橘色，本来一开始还嫌弃这种颜色，后来被阿玛尼200折服，一发不可收😂😂😂\n谢谢你们的支持😘😘😘另外，我想说的是，我喜欢自然的妆效，尤其是日常妆，所以视频和图片里看起来可能稍稍显得清淡，其实现实生活中看起来也是很自然的妆效，不会突兀，如果视频中看起来特别明显的眼妆，那现实生活中绝对不是自然日常妆，那肯定是偏浓的妆🙈🙈🙈\n这个妆的图文版在下一篇笔记哦😂'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/likBBEQZyK_sH952CrC8IPjlj59K_compress_L1',
    'video_id': '58ce22a5b46c5d1704e4e989',
    'title': '化妆视频|爱丽小屋西柚色眼影画法Part1',
    'video_tag_list': '',
    'content': '新买了伊蒂之屋的西柚色眼影就很激动，马上给大家拍个化妆视频秀一秀，因为这款之前貌似很多地方都缺货，所以看到有买了就直接购入，整体眼影色真的挺漂亮的，习惯了红色眼妆，换个西柚色的也很精彩，睫毛打底膏我觉得不贴假睫毛的时候是一定要用的，真的能刷出很翘很长的睫毛哦～话不多说看视频吧～\n产品：\n碧柔防晒霜\nysl黒丝缎妆前乳\nbobbibrown遮瑕膏\n阿玛尼大师粉底液\nclio遮瑕棒\n嘉娜宝天使蜜粉\n伊蒂之屋眉笔\nponyeffect四色修容\n伊蒂之屋10色眼影\n美少女战士眼线液\n伊蒂之屋101多功能笔1号色\n伊蒂之屋睫毛打底膏\n谜尚4d睫毛膏\n自然乐园腮红1号色\ncpb高光14号色\n伊蒂之屋口红pk005\n#跟着视频画眼影[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lhNrtoglAXecrilL6keOgxKteE6Y_compress_L1',
    'video_id': '58ce27b1faa052776a587568',
    'title': 'Tom ford 四号Honeymoon眼影视频教程，约会妆',
    'video_tag_list': '玫珂菲 MAKE UP FOR EVER FACE & BODY liquid make up 水粉霜;汤姆·福特;香奈儿 Chanel ROUGE ALLURE VELVET炫亮魅力丝绒口红/唇膏;寇吉 Koji Dolly Wink益若翼眼线液笔;跟着视频画眼影',
    'content': '❤️Tom ford 四号Honeymoon眼影视频教程，春天约会妆容教程❤️\n#四色眼影盘怎么画[话题]#\n#跟着视频画眼影[话题]#\n#新手最容易上手的眼影盘[话题]#\n#日常妆容打卡[话题]#\n第一次录视频，忐忑+害羞，但是装作自己很酷的样子🕶\n之前po的是图片形式的教程，感觉喜欢的人很多，所以搞了一个眼影视频教程，时间有限，视频的重点就是🔝眼影部分。这是我第一次录视频如果有不足请多包涵，希望以视频的形式大家能看的更明白。\n毕竟是视频不能好好p一下啊哈哈哈哈，其实我是糙汉子类型，却长着一张babyface的脸啊哈哈哈哈，女汉子也会有不酷的时候、也会有些害羞🕶哈哈哈哈🙃🙂🙃我已经把用到的对应的化妆品都在视频上写出来，so你们可以找到相关产品名字\n眼影教程部分：\n一共四个颜色，1号最浅色，2号棕色，3号酒红色，4号深酒红色。\n▪️Step1 - 用1号大面积涂抹眼部，做为提亮跟打底\n▪️Step2 - 用2号涂抹眼皮中部跟尾部，用小眼影刷涂抹下眼尾\n▪️Step3 - 用3号酒红色涂抹，范围比Step2小一点，接近睫毛根处涂抹（其实三号上了眼皮之后没有那么红、偏棕）\n▪️Step4 - 用4号紧沿着睫毛根处涂抹加重，再用1号在眼皮中部提亮\n\n眼影\n\n#YSL方管唇膏试色[话题]#1号\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqksiTWwCiXa6NNJXxjfA0PDSIYu_compress_L1',
    'video_id': '58ce4b1e7836232849380133',
    'title': '单眼皮不简单之眼影（简单易上手）',
    'video_tag_list': '单眼皮如何画眼妆',
    'content': '大家好，这次分享的是zoeva的眼影盘和眼妆。\n当然大家有不同牌子但相同类似的眼影颜色也OK的啦[活力]\n我事先先画好了底妆眉毛啥的这就不多说了......\n来着！首先，我们用到的颜色！焦糖shai儿、砖红shaier、金shai儿、粉shaier带金偏光、深棕shai儿。\n然后第一步，焦糖打底上眼皮.\n第二步，转红晕染上下↕️眼尾.\n第三步，用金提亮眼球中央.\n第四步，偏光提亮内眼角和卧蚕位置.\n第五步，深棕色画个假眼线。\n最后在补上睫毛膏腮红口红就完事了！\nps：口红是Mac的chili\n最后的最后谢谢大家的观赏以及一直支持我的小伙伴儿们！笔芯💌#单眼皮如何画眼妆[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/e32dddb1-206c5e6-aaed-93a6b3210a96_compress_L1',
    'video_id': '58cf4a1ba9b2ed771c006d00',
    'title': '这盘Dior5色眼影 脚残都能画得超好看',
    'video_tag_list': '',
    'content': '这盘Dior五色眼影#708琥珀色，说是手残党福音真的一点也没错。不管是用海绵刷、化妆刷还是手指，1分钟就能搞定眼妆，而且怎么画都不会出错。\n这一盘一共有5个颜色，其中4个眼影色+1个眼线膏，颜色从珠光米白到深咖啡色，任何肤色使用都很自然\n今天用的是最简单的平涂法来展示这款眼影，别说手残了，就是脚残都能画好看哦！\n#跟着视频画眼影'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvaMwcevpcXEwZhgRVKWdzSnOMPY_compress_L1',
    'video_id': '58cf5467d1d3b90c4893e18e',
    'title': '吃出春天的味道—香椿炒鸡蛋',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n香椿芽，别名：香椿、椿、春阳树、春甜树、椿芽、毛椿、古名杶、櫄，别名椿芽。\n每100克鲜嫩茎叶中含水分约84克、蛋白质9.8克左右、维生素C58毫克及钙、磷、维生素A、维生素B1、维生素B2等，并具芳香气味。\n★★★★★\n创意指数\n香椿芽炒蛋\n▼\n香椿芽炒蛋\n·食材·\n香椿芽、鸡蛋\n红米椒、盐\n1.沸水过香椿芽去除草酸\n2.除去根部\n3.切末\n4.鸡蛋打匀\n5.热油锅倒入鸡蛋液\n6.鸡蛋成块状倒入香椿芽末\n7.清炒片刻加入盐\n8.均匀翻炒\n9.红米椒点缀\n10.准备开动吧~！\n#超级下饭的家常菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ca1a1b3e5c1293a519aa4603392a3ccf3061669d_r_ln',
    'video_id': '58cfc8b614de4120dfe9defd',
    'title': '马甲线翘臀必备💪Gym罗马椅的多重使用',
    'video_tag_list': '',
    'content': '罗马椅最多被使用于练习核心部位：主要是后腰部（山羊挺身式）视频中动作1⃣️。\n其实用于上臀部的训练也是效果非常显著的。\n个人认为体重太轻的人山羊挺身比深蹲更适合，深蹲大腿前侧的代偿作用也是有些明显的，虽说动作标准会好一些，but 有时候很难保证随时动作标准。\n动作1⃣️： 山羊挺身式，\n大家请注意看，我将支点下调到接近大腿根部，以上臀部为轴心。妥妥的练到最难练习的上臀。\n5组 ✖️12个 根据自己的能力负重 我是6kg\n💗要领：每次挺身 臀部使劲挤压！由臀部发力带动身体抬起！\n动作2⃣️：侧腹练习+外加🌟转体🌟\n💗要领：手臂完全放松，由侧腰部带动起身，身体接近180度时，腹部带动转体。记住哦发力点一定是在侧腹部。\n腹肌马甲线的练习：侧面就是扭动（俄罗斯旋体）、正面就是折叠（卷腹、仰卧起坐。基本原理如此，所以把这两个结合起来外加负重。效果自然是好的。\n4组 ✖️左右各12-15个 负重6kg\n今天找小伙伴帮忙拍了视频，好难得😜\n以后争取每周都更新视频教大家如何练习具体部位。\n#臀部塑形视频[话题]#\n#健身器械教学视频[话题]#\n#哑铃杠铃教学视频[话题]#\n#练出马甲线[话题]#\n#练出翘翘蜜桃臀[话题]#\n#健身器械的正确使用方式[话题]#\n#必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luagIkTY9HrG2iWL_3Cwa0n6U-rg_compress_L1',
    'video_id': '58d0889bd1d3b9448c2833a5',
    'title': '小日常😁',
    'video_tag_list': '小红书萌娃大赛',
    'content': '昨天出门办点事情 回来有点晚 一进家门 正准备给D宝穿睡袋 D宝看见妈妈自己高兴的咯咯笑起来～ 能这样开心的笑 就是孩子吧 心都要融化了\n他好像什么都不懂 又好像什么都知道 宝宝怎么会那么讨人喜欢💓\n5M+5D 记录一下此时此刻……\n#小红书萌娃大赛[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhCsWNuWSeGcD2Vc2GIqWsHuttwf_compress_L1',
    'video_id': '58d0a12114de410a6f82d47b',
    'title': '无需刀工，超简单的椒盐排条',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n《椒盐排条》是一道主要由猪肋骨做成的上海菜。\n排条外焦里嫩，口味咸鲜，香味浓郁。\n★★★★★\n创意指数\n椒盐排条\n▼\n椒盐排条\n·食材·\n猪排条、鸡蛋\n洋葱、青椒、红椒\n蒜、椒盐粉、五香粉\n料酒、盐、淀粉、面粉\n1.用刀柄敲打排条两面使其变松\n2.加少许盐、料酒、五香粉腌制半小时\n3.红、青椒切丁\n4.洋葱、蒜切末\n5.备用\n6.鸡蛋打散\n7.鸡蛋液倒入腌制好的排条中，加入淀粉\n8.用手抓匀\n9.粘好蛋液的排条放到干面粉里滚一下\n10.油烧至六成热，转小火下排条\n11.炸至黄色捞出\n12.再开中火倒入炸好的排条复炸至金黄色\n13.起油锅爆香大蒜\n14.倒入切好的洋葱、青、红椒末清炒\n15.倒入排条\n16.撒上椒盐粉\n17.不说啦开吃！\n#超级下饭的家常菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liPLfHPfLGzv_ygGLF5Xu_nts-nl_compress_L1',
    'video_id': '58d114aafaa0526b97ae6254',
    'title': 'Yanis Marshall上海站大师课',
    'video_tag_list': '',
    'content': '全世界要论哪个男的最骚，舞蹈圈就数Yanis Marshall了！没错！就是那个在B站红翻天的Yanis！！终于来中国了....提前两个月定的MasterClass课程！！而且限额60名，上海只停留2天，然后他就回美国巡回了。\n光是Warm up就已经要了半条命，现场基本全是专业舞者，中外都有。虽然我以前经常在明星演唱会上伴舞，强度和老外他们还是不能比的。第二天肯定就是瘫掉的节奏～\n这里没人教你手怎么放，脚步怎么变，全靠自己跟，上课的都是冲着Yanis来的，学他对节奏的控制、编舞的技巧和规律。不得不说他每一个肢体都是很到位的，想做好一个动作全身肌肉都要控制、控制、控制！\n所以，跳舞不是你们看上去那么容易的。\n#舞蹈教学视频'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fh0CVzx7NIrnknVOo1eClj9vAL_U',
    'video_id': '58d136317836231d8b8ba6df',
    'title': '去年在清迈',
    'video_tag_list': '',
    'content': '终于能发短视频了，试个水😝'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg1kfTE62Ro6S9pmKm2nWS3x_hRJ_compress_L1',
    'video_id': '58d15a53d5945f71fa224ecf',
    'title': '史上最简单眼影画法😂一个随意的视频分享哈哈哈',
    'video_tag_list': '平价好用的单色眼影;汤姆·福特;汤姆·福特 TOM FORD 幻魅双色眼影;乔治阿玛尼',
    'content': 'Hi我的仙女们，这大半夜的发视频真是头一回啊🙈🙈🙈本来我要洗漱了，结果就是突然想画个我平时工作超级喜欢画的妆容🤗🤗\n‼️‼️史上最简单妆容，没有之一！！哈哈哈\n我平时工作的妆容都比较淡，而且忙起来真的是没有时间画那么多步骤，所以，为了整个人看起来不至于没气色，但是又要符合我的自身情况，我一般都会用单色眼影比较多🎉🎉开始分享啦\n这个视频我主要跟大家分享了两样产品，都是我最近超级爱用品哦😘\n🎀TF眼影膏03golden peach\n是一个非常非常漂亮的蜜桃色，我在视频中说了，这个颜色不适合肿眼泡，因为会更显肿🙈眼影膏质地柔滑，特别好推，用手指涂抹就可以轻松搞定，再点缀一点亮片，真的是blingbling的，因为蜜桃色颜色很浅所以很低调，但是加上亮片又很美的让人心动❤真心是我工作日常妆的最爱眼影！！\n🎀阿玛尼红管唇釉202\n这个颜色我没有给大家推荐过，因为！我觉得可能很多人会不太接受🙈\n这个色号绝对是冷门，功课很少，没怎么被拿出来说过，当然也不太好找得到。\n吃土色中的奶茶色，我这么说就能体会到了吧，其实我自己擦它之后呈现出来的是相对淡一些的奶茶色，特别气质的颜色，很戳我的颜色，今年很流行奶茶色哦～又喜欢吃土色又喜欢奶茶色，刚好就这一支，绝对爱上😘😘\n‼️这个视频就是一时兴起录下来的，正常情况我都会白天录的哈～就当做聊聊天啦\n我非常非常感谢好多仙女喜欢我，特别开心，希望有机会多跟你们交流❤\n晚安啦💋\n#平价好用的单色眼影[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/1a141566dcefe313a134da0b260c0bb1808fd391_r_ln',
    'video_id': '58d1f3d7faa0525412ae6256',
    'title': '网红茶叶蛋来袭，制作诀窍大公开！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n茶叶蛋，著名汉族小吃，中国的传统食物之一，全国大部分地区都有该小吃。\n因为茶叶有提神醒脑的功能，故在烫煮过程中加入少许茶叶，煮出来的蛋便色泽褐黄。\n★★★★★\n创意指数\n茶叶蛋\n▼\n茶叶蛋\n·食材·\n鸡蛋、红茶\n八角、桂皮\n糖、盐、酱油\n1.菜叶沾水贴在鸡蛋表面\n2.再用纱布包裹起来\n3.冷水放入鸡蛋\n4.放入调料包\n5.倒入酱油\n6.倒入糖\n7.大火煮开\n8.煮开后转小火八分钟\n9.关火后继续在茶水中浸泡一个晚上\n10.印花茶叶蛋你吃过吗？\n#卤蛋这么做超美味[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ll-o5HoUom2Nvd2R_CDZqs13xrW2_compress_L1',
    'video_id': '58d21da214de4121950aa356',
    'title': '【视频】单眼皮大地色&吃土色妆容分享',
    'video_tag_list': '汤姆·福特;乔治阿玛尼;单眼皮如何画眼妆',
    'content': 'Hi大家好，我听到了小仙女们的心声，你们让我拍的大地色妆容来啦🤗\n☘TF03cocoa mirage\n经典哑光大地色，粉质超级超级好啊，这一盘哑光大地色我特别喜欢，可浓可淡，又日常好画😘\n☘阿玛尼红管202\n吃土色中的奶茶色，👆🏻上一支视频笔记有详细介绍哦\n谢谢支持❤❤❤\n#四色眼影盘怎么画[话题]##单眼皮如何画眼妆[话题]##阿玛尼唇釉试色[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llOTowusSVz3Mz0YskbGQMT3Rv3D_compress_L1',
    'video_id': '58d229d8b46c5d55c728634a',
    'title': '小羽私厨之玫瑰花煎饺',
    'video_tag_list': '',
    'content': '玫瑰花煎饺，我们一起让传统的饺子也变变样吧，玫瑰花形状的煎饺，端上桌绝对会让所有人都惊艳'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/84eb4d58-aff348d-a67c-479843737b42?sign=2424212644bade4b3635224b62c422ac&t=65fb06d4',
    'video_id': '58d22e9da9b2ed6acee7e2aa',
    'title': '没有剪刀时怎么办，每家每户都有的小工具，超轻松的开袋方法',
    'video_tag_list': '',
    'content': '是不是经常发现有些塑料包装纸特别不容易打开，或者连开口都没有设计？身边如果没有带剪刀的话，那么就很尴尬了。\n没关系，利用两枚硬币就能轻松解决这个问题哟~♡꒰*･ω･人･ω･*꒱♡力度的把握比较重要，多试几遍就可以成功了哟~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvbZKpgHxoKjVtogretY36uTTVHX_compress_L1',
    'video_id': '58d253a914de41208d82d47b',
    'title': '【Adora分享】多款美妆工具使用感受（二）',
    'video_tag_list': 'CAILYN  BUILT-IN BRUSH COVERAGE FOUNDATION 内置伸缩刷头无暇保湿粉底膏 (02-ADOBE);Real\xa0Techniques 脸部套刷;Real\xa0Techniques 眼部套刷;Real\xa0Techniques Bold Metals金属系列化妆刷;白凤堂;晃祐堂 KOYUDO Collection系列化妆刷;竹宝堂 chikuhodo G系列化妆刷套装;植村秀 shu uemura 太阳花化妆刷套装 X 2016年村上隆合作限量版;拉杜丽 Laduree BRUSH HOLDER贵族浮雕肖像化妆刷筒;魅可 M.A.C 魔法化妆刷套装;达芬奇 da Vinci 专业眼部化妆刷4件套;Coastal Scents 迷你精英系列化妆套刷（带刷包）;sigma 高档羊毛专业12支套刷;Wet n Wild 专业化妆刷;Velvet  10支化妆刷具套组',
    'content': '昨天和大家分享了上妆的海绵和清洗类的产品使用体会，今天我们继续biubiubiu……,\n化妆刷是化妆必备工具之一，曾几何时的我也指着一套基础刷打天下的心，后来自行体会了什么是上战场枪不好使，英勇无用😳\n最近都在用牙刷式的粉底刷上妆，本以为这么大刷子肯定没海绵效果好，那天拿回家才发现，OMG太软了，舒服得不要不要的…我就赶紧行动起来当即用了它上粉底液。最吃惊的是，它竟然 不！吃！粉！比起美妆蛋来说，还省粉底液，感动哭😹以下几款都还不错\n\n\n要是买个Artis Brush的就更完美了[得意]\n继续说说硅胶粉底工具 这个真心长得像个硅胶鞋垫[害怕]\n貌似ipsa家最早推出了这个家伙来上粉底 后来就很多品牌都出了硅胶垫哈哈………这个家伙的好处就是：不吸粉！所以不会浪费那么多粉底。触感也像个nu-bra[活力]\n只是涂多了粉底的时候，它可没办法帮你吸收掉……\n好的化妆刷一定是会更易于上妆,有种神枪在手画哪有哪的感觉。\n\n\n\n\n\n最近火热的化妆刷大多数是人工纤维毛，质感柔软舒适上妆也不错。所以综合使用效果和价格，是大多数美女选择的领域。好一些的纤维毛除了柔软细腻还能稍稍滴抓粉。差一些的和大多数仿品也就是软，而已。你不能要求他有什么上妆效果,除非你是神级达人用什么tools都能画的完美[活力]\n主要纤维毛的粉底刷不吸水、延展度较高，这也是是人造刷毛的优点。不吸水，因此可以将粉底液较完全的全部使用掉，不会粘在我们的刷毛上造成浪费。\n我选刷子有三条参考建议：\n第一 皮肤触感舒适\n先不论什么毛，什么价位，肌肤之亲的毕竟是要往脸上戳的所以还是要温柔一些，劣质毛会扎脸或细节的毛突出同时感觉到别扭。\n第二 是否抓粉 易上妆\n纤维毛抓粉力一般不如动物毛🐒。但在一定程度内不会影响妆效。\n动物毛有自身长的毛鳞片，伸缩性、吸水性都会有，自然上妆会服帖舒适。动物毛也不是所有的毛抓粉。\n动物毛最优降次排列：貂毛、黄狼毛（一般较贵 一支几百到几千不等，几十块钱的呵呵 你敢用我叫你勇士），其次是灰鼠毛🐿️（也不便宜🙄）、水洗小马毛（柔软性好价格适中）\n市面上最常见的化妆刷毛是山羊毛跟马毛。但山羊毛和马毛的也不是都一样的，过高档一些的山羊毛又分7个等级。分别是：细光峰 中细光峰 中光峰 中白光峰 白尖峰 黄白尖峰 黄尖峰。🙄一般用来制作腮红刷、暗影刷、蜜粉刷、扇形刷等等\n的刷子匠心品质\n\n\n\n日本是产化妆刷的强地👍一个村子里的制刷工人都是一个工艺做几十年，一件事情极致不已。这样的氛围下的手工制刷简直就是手工艺术了，所以一支刷子也蕴含着很多心思和精力。这种匠心品质和精神恰恰是我们快餐人生里缺少的部分。Wayne Goss大叔也是讲自己的化妆刷品牌放到了日本制造。可见用心。\n第三 刷头的形状 有些刷子会有非常严谨且用起来很方便的刷头。比如我败了一只Anastasia的#7号 眉刷 又特意跑去买了个网上的高仿对比一下差别。你猜怎么样？简直大吃一惊！\n从外观上两把刷子的感觉极相似，连杆的字体粗细都很到位。只是一个刷头毛质严谨，紧密又光泽，另一个相比之下草草了事的斜头毛。化的时候对比更夸张。正品沾完眉膏后化出非常细的线条，几乎能和真眉毛以假乱真。仿品画出来就是一坨，粗粗的黑线，感觉是涂色笔。你说这样的眉笔还没化就甩开各位好几个档次了，妆效可想而知。😳\n综上所述，希望能给仙女们一些帮助。在化妆刷上建议大家一定不要马虎，用在眼睛、皮肤上的都是脆弱的皮肤。粗糙不好的毛直接会导致过敏和戳伤🙈。刚上手的仙女们可以选购一些品质不错的刷子品牌比如sigma、毕加索、suqqu、make up forever、MAC、NARS、等等\n\n\n\n\n'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/fbfac7ed-9323a98-919f-90a2faf32aba?sign=67a83ee9949a656e09b8873c4d28b016&t=65fb06d4',
    'video_id': '58d29c1334609438b8dec119',
    'title': '你有多久没有陪伴父母一起出行？',
    'video_tag_list': '',
    'content': '我们做了一次实验性采访，6位在都市生活工作的年轻人和6位父母亲，就他们印象最深刻的一次旅行做了回答…结果竟然大不相同！！！你有多久没有陪伴父母一起出行？'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/abaf89904234062248522e9288f25679c534f9f2_r_ln',
    'video_id': '58d336d014de415621ad2ac5',
    'title': '可乐鸡翅最简单的做法，快来学学吧',
    'video_tag_list': '',
    'content': '#跟着视频学做菜[话题]#\n★★★★★\n小圆食记\nMenu\n可乐鸡翅是以鸡翅和可乐为主料制作而成的美食。\n味道鲜美，色泽艳丽，鸡翅嫩滑，咸甜适中，又保留了可乐的香气。\n★★★★★\n创意指数\n可乐鸡翅\n▼\n可乐鸡翅\n\u200b\n·食材·\n鸡翅、可乐\n盐、姜\n料酒、生抽、老抽\n1.鸡翅正面斜切2刀\n2.背面斜切一刀\n3.生姜切片\n4.锅中放入鸡翅、生姜\n5.倒入清水\n6.大火煮开去杂质\n7.沥干水分备用\n8.热油锅依次倒入鸡翅、料酒、生抽、老抽、盐\n9.倒入可乐\n10.中火煨至汤汁变浓\n11.小资生活从这一刻开始！\n#懒人版鸡翅[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/5482d3d0-5844264-91c9-8fbac3312984?sign=7acd40011f9a449932827c821c47233c&t=65fb06d4',
    'video_id': '58d3a95c346094428b272f9e',
    'title': '维密天使的no1健身利器｜拳击小科普101',
    'video_tag_list': '',
    'content': '自从开始打拳\n我已经习惯别人说\n啊你又瘦了\n哎你肌肉好紧实啊看着\n哇你打拳是么好酷啊\n每天最盼望的事情就是\n上课打老师\n回家打男友\n还幻想着月黑风高路遇不平拔刀相助\n反正就是女侠风\n因为太爱\n忍不住自己辞职开了一家工作室（多洒脱，详情见我们简介s）\n里面有拳击、有舞蹈、还有燃脂塑形课程\n虽然创业狗很辛苦\n但是看电脑看累了就去打两拳跳支舞\n什么烦恼都没有了\n欢迎大家来找我们玩儿\n今天穿的是海淘的aimn裤子，运动内衣是淘宝买的，没有牌子，但是胸小就是穿什么都一样呀🙄️\n运动那么多？我为什么要打拳？\n1，拳击是一种让你“上瘾”的运动。这很重要。\n如果你每次跑步做hiit或者跟着keep练，都要情不自禁看表的话；请你想象有一种运动，能像巧克力蛋糕一样，吃的时候享受每一刻，吃完还会憧憬下一次。\n总有人把打完拳之后的“高潮”感觉与跑步之后的“runner\'s high"相提并论，没”高潮“过的赶紧试试吧\n2，超级燃脂塑形的维密秀前必备训练\n这世界上没有比维密超模更需要在短时间内变成自己最好看样子的了。所以她们选择苦练拳击。一个小时的拳击大概可以消耗520大卡的热量，而且是减脂+塑形双管齐下，尤其是对手臂及背部线条的塑造。看看专业拳击手，你就懂了\n3， 减少压力/发泄工具\n这个不用说，你懂的。（不懂的请看上面的视频）\n3， 减少压力/发泄工具\n这个不用说，你懂的。（不懂的请看上面的视频）\n4，增加骨密度\n骨密度指的是骨骼里矿物质的含量，也称骨骼矿物质密度。女生骨密度的峰值在30-34岁达到，随后就会逐年降低，也就是说你会越来越容易受伤和骨折。而拳击和举铁这种负重训练，则可帮你对抗骨质流失，并实现逆增长。是真的，文献里的。\n#拳击教学视频[话题]#\n#维密塑性靠拳击[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/cf4c1c97-8b0ed03-8a40-fc94bcaf99e4?sign=3fdcaf889763be6edd79db6ab847ed16&t=65fb06d4',
    'video_id': '58d3ceca7fc5b859179d7612',
    'title': '偷窥健身“网红”的一天|减脂期吃什么怎么练',
    'video_tag_list': '',
    'content': '自从当了网红\n当然，我可能只是网\n好像还没红\n但是当网红好难啊！\n集合世界三大苦逼\n又当设计狮又当码农又当民工\n而且还要美还要瘦还要蜜桃臀\n所以除了工作还要撸铁有氧两小时\n不然你们就要退票了！🙄\n所以好多人问我\n你是怎么做到的！！\n尤其现在低碳水饮食，那你还能吃些什么\n快来看健身网红如何度过一整天\n加班狗们，no excuse!\n（附赠加班狗福利：超级高效臀腿训练）\n练一组不够？关注我们的公众号 Fit4Life健身与美食，里面各种减脂增肌小秘籍哦！\n自己练不过瘾？快来店里和我们一起变瘦！地址在北京建外soho西区17号楼2505哦\n#全身减脂教学视频[话题]#\n#健身食谱教学视频[话题]#\n#哑铃杠铃教学视频[话题]#\n#健身器械教学视频[话题]#\n#科学减脂食谱[话题]#\n#高效瘦腿攻略[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/95223ba4-43e695f-b3ee-c38c723c3a3c?sign=7c377bb0501d2528fd31847d1676e13e&t=65fb06d4',
    'video_id': '58d3cfb97fc5b85bdc9d7612',
    'title': '怎么吃碳水越吃越瘦｜高效燃脂全身训练｜高碳日三餐记录＋食谱',
    'video_tag_list': '',
    'content': '对于一个特么一家子糖尿病，\n不吃碳水会死的老阿姨，\n低碳的日子真是太难熬了，\n还好精明如我忽悠让某人吃了atkins ,\n自己选择了舒服很多的carb cycling ,\n在连续两天的低碳日之后，\n终于迎来了春天般温暖的高！碳！日！\n其实碳水和川普一样，\n都被媒体过度妖魔化了。\n精加工的糕点零食的确应该少吃，\n但是水果、粗粮以及根茎蔬菜都属于纤维丰富的“高级”碳水，\n吃对了不仅不会胖，\n还能够减脂增肌呢！\n想知道其他减脂增肌的秘笈？\n快关注我们的公众号 Fit4Life健身与美食\n各种干货等你来哦\n#全身减脂教学视频[话题]#\n#健身食谱教学视频[话题]#\n#哑铃杠铃教学视频[话题]#\n#健身器械教学视频[话题]#\n#科学增肌食谱[话题]#\n#科学减脂食谱[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/5774e841-5ea9eab-9001-3cab81f0dbe8?sign=afe3e22c2170ec6ecbb1cdce4a0fcef4&t=65fb06d4',
    'video_id': '58d3d0b87fc5b865c89d7613',
    'title': '这个春天如何每周瘦3斤|像健身网红一样过周末',
    'video_tag_list': '',
    'content': '三分练七分吃，说的太对了。\n一旦稍微控制饮食，\n你会发现运动变得事半功倍了！\n因为这几周在做低碳水减肥挑战（请见公众号往期文章），所以要严格控制碳水的摄入，\n想起来很痛苦，但经过一周半的摸索，我的身体已经适应了这种变化\n因为碳水在体内会需要吸收大量水分，减少碳水的摄入之后，感觉马甲线一下子就清晰了，而且吃完饭，也不会涨肚。。。\n好神奇！\n最最棒的，因为可以吃很多肉，\n所以我感觉每次吃饭，都还是很有尊严的人类!\n最近在练臀腿的坑里越钻越深...\n之前感觉练臀必然伴随着粗腿\n但是现在发现，\n原来有辣么多的动作是只练臀肌不练大腿的\n不早说！\n所以每周两次臀腿训练最好\n第一次综合练，臀腿一起练\n第二次做臀部的单独训练\n效果真的好\n想看更多臀腿训练视频？\n可以去公众号 Fit4Life健身与美食\n里面干货多多\n等你哟\n#全身减脂教学视频[话题]#\n#健身器械教学视频[话题]#\n#健身食谱教学视频[话题]#\n#无器械锻炼视频[话题]#\n#臀部塑形视频[话题]#\n#腿部塑形视频[话题]#\n#弹力带教学视频[话题]#\n#哑铃杠铃教学视频[话题]#\n#泡沫轴教学视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/1d638f7e7265f91a6b31307ff21d3d56ca9e2795_r',
    'video_id': '58d3d45f7fc5b86c0f9d7614',
    'title': '五个动作让你大腿再也“合不拢”',
    'video_tag_list': '',
    'content': '好多人小窗问我怎么减大腿内外侧的脂肪，\n说最大的梦想就是两腿合上后中间有条缝。\n还记得阿姨们之前讲过的不？\n要想局部减脂，\n就好比希望同一蓄水池里的水位高低不平，\n是不可能实现的，\n请大家别做梦了！\n但是阿姨们还说过，\n减脂虽然只能全身减，\n塑形却最好分部位进行。\n怎么才能练出thigh gap\n（两腿合并中间的缝隙）?\nGiselle阿姨手把手教给你，\n附赠办公室美腿秘籍，\n某些角度比较污，\n建议不要对着老板做🙄️\n跟着视频练不过瘾？\n欢迎北京的朋友来建外soho西区17号楼2505找我们玩儿昂！\n不在北京的朋友可以关注我们的公众号 Fit4Life健身与美食\n里面各种干货帮你在夏天来之前瘦5斤哦\n#腿部塑形视频[话题]#\n#弹力带教学视频[话题]#\n#高效瘦腿攻略[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ab45237370de6383c1fb75705da4042776db6a37_v1_ln',
    'video_id': '58d3e59837cec9411fefe9a9',
    'title': 'Hip Abductor 练臀大法 | 再不用担心粗大腿❤️',
    'video_tag_list': '练出翘翘蜜桃臀',
    'content': '一般健身房的亲们看到Hip Abductor （大腿外展练习器）都会按照图示方法去使用，的确是可以练习大腿外侧力量和一小部分的臀部外侧。\n然鹅！我想减肥的美女们谁也不想狂加重量练起大粗腿，不加重又没有什么明显效果！\nSo，这个简单的弓背动作可将发力点稳定的控制在下臀部外侧。\n换句话说：臀部下垂元凶一般就是下臀外侧肌肉无力松弛，可见pp要上重量的重要性啦。\nwell：\n我的训练计划如下：\n6组✖️12次 90磅重量 状态好的时候再+2.5kg\n这6周内，基本每次去健身房我都会练习这个动作，也从60磅慢慢加到了90磅+。\n结合有氧运动跑步椭圆机等，做到腿瘦pp翘的效果。我觉得我应该po一张最近练出来的对比图😊\n#我为瘦身打卡[话题]#\n#练出翘翘蜜桃臀[话题]#\n#健身器械教学视频[话题]#\n#臀部塑形视频[话题]#\n#腿部塑形视频[话题]#\n#必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnEK7k-hVrGuGWXBb5SUfXwuKJKl_compress_L1',
    'video_id': '58d3f59c696012781a8ec79a',
    'title': '🌈每天都能化的日常妆（PART 1）',
    'video_tag_list': '',
    'content': '#日常妆容打卡[话题]#\n学生妹上学、OL上班无压力~\n不会化妆、新手手残也不怕~\n据说是直男最爱的清纯淡妆~\n时间有点超分开传，记得看PART 2哦'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgHYijf_akZWvNtSYbtfp60Rp5mr_compress_L1',
    'video_id': '58d3fa7878362308acafb868',
    'title': '空瓶记2⃣️2⃣️',
    'video_tag_list': '空瓶记',
    'content': '视频形式录一次试试\n#空瓶记[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lq8EGIj_0Dy4zY3cOqY9IosgWu_Q_compress_L1',
    'video_id': '58d3fbcbe9521a616b939482',
    'title': '眼影试色视频so easy, 用文艺复兴网红盘来涂涂涂涂涂',
    'video_tag_list': 'Anastasia;得鲜 ;跟着视频画眼影',
    'content': '看了美妆薯的30秒眼影视频教程，发现原来彩妆视频也是我等彩妆小白可以小试牛刀的. 兴奋，撒花，立马照葫芦画瓢来一篇.\n💄国际惯例说明一下：彩妆届唇膏热爱者，底妆实验者，眼妆初级者，眼影小白一个. 眼窝深，眼皮油，双眼皮有时会变三眼皮[喜欢]\n💄眼影手法：基本停留在“涂涂涂涂涂”阶段，看了大触们的笔记对打底晕染啥的基本原理都学习了，但缺乏实践. 目前画眼影全凭画画的感觉，光和影和颜色，怎么好看怎么来吧...\n💄视频里是最近常用的，适合新手，更适合快手\n的#新手最容易上手的眼影盘[话题]#文艺复兴盘，颜色都很美啊，目前只用了RED OCHRE（红枫色，是Chanel 268替代款哦），显色也比较持久，如果做好眼部打底会更持久. 这款网红盘是去年朋友从美国丝芙兰买的，据说也是断货款.\n的卧蚕高光棒，大概30不到吧，平价好用. 我就用来打亮卧蚕，让人精神好多.\n#跟着视频画眼影[话题]#\n#双眼皮如何画眼妆[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg7efftV0KUz5XUrFmZ5K2z_RLHE_compress_L1',
    'video_id': '58d3fd6f14de4178c7170b79',
    'title': '🌈每天都可以化的日常妆（PART 2）',
    'video_tag_list': '',
    'content': '接PART 1哦\n#日常妆容打卡[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/01e24807c720386a01837003803c3cfdc4_259.mp4',
    'video_id': '58d48665d1d3b94b5678ce27',
    'title': '好吃又能止咳的小秘法——橙皮蜜饯',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n香橙含有大量的维生素A，可作为健胃剂。\n橙皮很早就是中药的一种，味辛微苦，入脾、肺二经。治咳嗽化痰。\n★★★★★\n创意指数\n橙皮蜜饯\n▼\n橙皮蜜饯\n·食材·\n橙子、糖\n1.橙子用盐水洗净，切成8瓣\n2.用刀去除果肉\n3.切成丝\n4.放入锅中煮沸，转小火再煮10分钟\n5.沥干水分备用\n6.锅中倒入糖\n7.加入清水\n8.将橙条倒入锅中，小火煮至橙条半透明\n9.放在盘中，晾60分钟至水蒸发\n10.晾好的橙条放入白糖中蘸匀\n11.好吃又能止咳的小秘法'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnqb6EhoaWWN4tZkFDM8NVgdKPqr_compress_L1',
    'video_id': '58d4a0dbd5945f7e6f519553',
    'title': '耳饰分享 tb篇～',
    'video_tag_list': '精致的小耳坠',
    'content': '刚刚收到美妆薯可以发tb店铺推荐的话题\n#最值得收藏的淘宝店[话题]#\n就迫不及待先来分享网上购入的耳饰集合（其实还有一个门店购买的耳饰集合） 都是比较便宜的 适合学生党\n💕草莓耳线 【诗云不语】\n这个店主是个美妆博主 但我买的这个好像已经下架了\n大家可以搜搜看关键词 他家其他的饰品也很有自己的风格\n💕绿 蓝 粉 三对略夸张耳饰【我的公主韩国进口饰品】\n第一次买 除了第一对绿色的80➕ 其他两个都20➕\n但感觉质量很好诶 做工很精致 当下很多流行的款式都有！\n💕亲爱的公主病同款 星星耳饰【SuzyAcc韩国饰品】\n这对也是单价80➕ 但是做工很好哦 很精致\n也是个蛮大的店铺 款式也很对\n💕珍珠耳饰 【南瓜小姐 银饰】\n她家都是比较日常的银饰 金属过敏的妹子们可以选择\n单价也都在可接受范围内 包装挺好的\n买一副耳饰送了超多耳塞 还有擦银布\n💕阿吉豆同款【Chez Helen】\n这款也下架了 大家可以考虑截屏搜同款\n💕其他购入过的店铺推荐\n【MACMODE ACCESSORIES】大牌设计 单价在在30➕\n买过开口的珍珠戒指 拍照巨好看！\n【鹿尔饰品】买的是戒指不是耳饰 也是银制的饰品\n模特兼店主小姐姐长得很舒服\n和【南瓜小姐 银饰】相似度很高\n💕其他已经收藏还没下单的饰品店\n【脂肪商店CnHnOn】略欧美 简单精致款 夸张款都有\n【芒果饰品MG】很便宜 有耳夹 流行款式都有\n【奶奶 STUDIO】很便宜 有耳夹 日韩欧美流行款都有\n【KEYT ACC】价格不贵 超有个性的一家！\n【也桃 原创饰品】单价30➕ 可爱又有设计感的一家\n【STANDII手作】手作风格的一家 单价20➕\n【胡大大是聪明小可爱】（名字太长搜这个就好）适合学生党 简约精致不夸张\n💕因为有耳洞 所以我大部分挑的都是无耳夹的店铺\n分享给有耳洞的小仙女们 无耳洞的小仙女们 也可以问问店家可以不可以做耳夹款\n💕建议大家 带耳钉注意定期消毒 带的时候温柔一点不然打了很久也可能会搓破 若是觉得耳朵有点痒 及时用青霉素眼药膏或者酒精棉球等消毒 防止耳朵发炎情况继续恶化\n💕希望这个分享对大家有用哦\n比❤️#最值得收藏的淘宝店[话题]#\n#精致的小耳坠[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/lsc7-iyYv128TLQRpZ22C5Ds758Z?sign=586f7d7efff30043a2388bb0c9d3365d&t=65fb06d4',
    'video_id': '58d4ea2814de41143a999b36',
    'title': '爱丽小屋西柚色眼影Part2 |化妆视频',
    'video_tag_list': '',
    'content': '话说在前面（我已经感觉到自己又老又丑了，大家将就下吧~）\n这次是第二种爱丽小屋西柚色眼影盘的画法视频\n整体妆容明显有橙色系的感觉，还是挺喜欢这种眼妆感的，比较活泼点啦~\nsofina妆前乳\nysl黑丝缎妆前乳\n自然乐园双头遮瑕膏\n雅诗兰黛气垫粉底棒1w2色\n嘉娜宝天使蜜粉\n爱丽小屋眉笔\n爱丽小屋西柚色眼影盘\nLB眼线胶笔\n迷上4d睫毛膏\njillstuart腮红1号色\nponyeffect四色修容粉\n爱茉莉唇油9号色\n#平价也有好品味[话题]##美妆新人[话题]##入门级彩妆[话题]##平价好用的单色眼影[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/a629a2bfdbe9e9b634c83a991e5d9d31e6f51f50_r',
    'video_id': '58d4ec69a9b2ed1591c3bdab',
    'title': '洗面奶用到最后总是挤不出来？教你一招用得一点不剩',
    'video_tag_list': '',
    'content': '大家有没有遇到过这样的烦恼，快要用完的牙膏和洗面奶等这些管状设计的东西，包装内肯定留着最后一点没用完，但就是这么难挤！\n今天的喵招就来教大家不用剪开包装，就能快速挤出剩余洗面奶的方法！这个方法适用于所有管状设计的塑料包装哟！\nPS：有些牙膏包装比较硬的，可以用根吸管把瓶身吹鼓起来，再盖起来甩。'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/c6e008b6-be7cd30-ad5f-299407653856?sign=3bc90b9d09e9416d4e3eca255b10ecd2&t=65fb06d4',
    'video_id': '58d5213a7fc5b836de8256cd',
    'title': '干货！【28枚Makeup Geek单色眼影试色：包括常态色，duo-chrome，foiled-eyeshadows等】',
    'video_tag_list': '平价好用的单色眼影;Makeup Geek',
    'content': '今儿来给大家分享我最爱最爱的一个眼影品牌：美国一超有名级资深的YouTuber自创的品牌【Makeup Geek】\n作为一名美妆狂人，市面上的中高端眼影我几乎都用过，包括Dior，YSL，Chanel，Tom Ford，NARS等等等等。。。\n但我最爱的就是Makeup Geek，绝对专柜彩妆的品质➕开架彩妆的价格，超级划算。而且选择多样，种类齐全，色彩多样，显色度高，好取粉，无数个爱她的理由！总之就是一个字 - 超级好！\n而且她家彩妆非常科学的一点就是都是单色的，包括眼影，腮红，修容等等... 所以可以选择自己喜欢的颜色再组合到一起放在z-palette里，避免了传统4色或5色眼影盘中有1-2个不常用的颜色被浪费的弊端。\n视频里一共有28枚眼影，包括：\n1️⃣15枚regular eyeshadows/常态眼影粉：Shimma Shimma, Creme Brulee, Hipster, Mocha, Cocoa Bear, Bitten, Unexpected, Cupcake, Cosmopolitan, Mango Tango, Homecoming, Prom Night, Drama Queen, Corrupt, Peacock\n2️⃣6枚Duo-chrome/偏光眼影：Voltage, Karma, Mai Tai, Ritzy, Typhoon, Blacklight\n3️⃣6枚Foiled-eyeshadows/油性眼影（膏）：Whimsical, Nostalgic, Pegasus, In The Spotlight, Grandstand, Center Stage\n4️⃣1个Pigment/眼影粉：Birthday Wish\n.\n以上，希望大家喜欢！😘\n#平价好用的单色眼影[话题]##新手最容易上手的眼影盘[话题]##我的彩妆测评[话题]##创意彩妆试色[话题]##小众妆品我来捧[话题]##眼妆每日打卡[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/adce029a-96052af-a259-688e10b18bbb?sign=a947b330b501d7b0065662e0b08e13cd&t=65fb06d4',
    'video_id': '58d52621a9b2ed6341c5a5fb',
    'title': '六个动作让你穿着马甲线过夏天',
    'video_tag_list': '',
    'content': '如果喜欢我们的内容，\n在北京的孩子们可以来店里找我们玩儿昂\nfit4life实体店地址：北京市朝阳区建外SOHO西区17号楼2505-08\n北京今天下雪了，\n你是不是以为夏天还很远，\n还可以把减脂的计划再推一推？\n错！\n下周末就26度了你招吗？\n对啊天气就是抽风啊，\n夏天来的让你措手不及，\n衣柜里的吊带热裤已经在跟你say hello了，\n你攒了一冬天的肚子是不是也是时候该say goodbye了呢？\n别着急，\n网红阿姨们带你一起，\n每天20分钟，\n赶在夏天来临之前练出迷人马甲线！\n#练出马甲线[话题]#\n#腰腹塑形视频[话题]#\n#无器械锻炼视频[话题]#\n#必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/ff57cad627d3a1ed076517f610880986edb827c8_r_ln',
    'video_id': '58d624fae9521a3655130c82',
    'title': '修眉➕画眉技巧大公开！',
    'video_tag_list': '贝印 KAI 修眉刀;SANA  EXCEL三用细致眉笔;凯婷  KATE 自然眉色染眉膏;实用的修眉小技巧',
    'content': '我觉得眉毛在我们妆容里面真的特别重要，\n精致的眉毛可以帮我们加分不少，\n今天我就来给大家分享我的修眉➕画眉小技巧哦！\nps：粤语视频对于我来说就是个坑，啊哈哈哈，每次打字幕打到疯～🙈✨\n#适合新手的眉笔[话题]#\n#实用的修眉小技巧[话题]#\n#简单易上手的画眉方法[话题]#\n\n\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgnXuk141cP4cfjqmRd_a2f-ykoA_compress_L1',
    'video_id': '58d64dd137cec93855ec8c7d',
    'title': '如何优雅地把Plus放进Chanel 小盒子17cm小号',
    'video_tag_list': '',
    'content': '感觉plus简直是个魔咒啊\n所有迷你包包的笔记下面，都有评论问plus放得进去吗\n😂\n这个Chanel小盒子/小箱子，小号宽度17cm\niPhone Plus的高度是16cm\n[抠鼻]\n江湖传言放不进plus\n也有人说可以斜着放，但是很占空间\n其实应该：\n这样放\n:::\n包内分2个隔层\n把plus放进后面那个隔层\n然后轻轻一推\n让手机贴着后壁\n就搞定啦\n不占空间，这层还可以放其他小物\n取出来也不难，很顺手\n[少女心]\n不要放在前一个隔层，两侧被撑开后，拉链会刮到这个隔层的皮面\n[活力]\n很多人喜欢小号的上身效果，放心买吧，plus不是障碍'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/lj6hNEVfhp9G1BuD4Wvzjz_IWpat_compress_L1?sign=563940be40d873c2b288f6f8e6626ecf&t=65fb06d4',
    'video_id': '58d7cfc6f138213687f7db60',
    'title': '单眼皮之单色平价眼影不平淡',
    'video_tag_list': '平价好用的单色眼影',
    'content': '大家好，今天分享的是好用且评价的单色眼影和妆容～\n#平价好用的单色眼影[话题]##日常妆容打卡[话题]#\n由于视频时间的缘故里面就没有配文字，还请大伙儿多多包涵！\n我这回用手指当刷子使得，我觉得省事儿！各位不喜欢用手指的或者掌握不好力度的该用刷子用刷子。\n1⃣️我有这么些个单色眼影，都是我平常会用到的（我不是收集控，所以只买自己喜欢的或者说是用得上的，这样才不会浪费😉）\n2⃣️我这次不推荐Bobbi的，毕竟价格不是所有人都接受的。colourpop的也挺多人推的，我下次再说。今天就分享好买，平价，又不错的爱丽小屋。（我这块已经买了两年了，不存在任何关于政治甚至国家的问题，纯粹是好用还便宜。如果有意见的请你别看了，我没要求你看，而且你也别给我评论，我看着闹心。谢谢合作）\n3⃣️色号是【0638】我感觉是棕调的树莓色（我瞎起的）不会显得眼睛肿，我认为是很日常的颜色。质地不错不飞粉还算是好晕染，带妆六小时左右无压力。\n这样的眼妆基本上是两三分钟就可以搞定的，比如上学上班起晚了，画个类似这样的眼妆也是个不错的选择！既省时省力省钱又干净利落大方。\n🔥我最近发现有许多伸手党...连一个小孩都懂的道理但是现在还是有许多人...这是一个很不礼貌的行为...所以我决定以后每篇文章后我都会➕这样一行话：\n现在是一个文明又健康的社会，如果没用“您好，请，谢谢”类似的话语，我一概不会回复！我不会理会没有礼貌的人，谢谢大家合作[赞R]\n最后，谢谢大家的观赏💌'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/87d1b279-aadc970-b5c0-69abb8c07b60?sign=ea90f00efa9d163db01dc2cbc2e6ac38&t=65fb06d4',
    'video_id': '58d873ff7fc5b8531e416a9a',
    'title': '【女性健康那些事儿】',
    'video_tag_list': 'BLACKMORES;BLACKMORES 月见草精华胶囊;日常美容保健品',
    'content': '今天苏妹儿要来和大家聊聊关于女性健康的问题，当今社会的亚健康人士真的太多了，我认为这是一个非常重要的问题，绝不能被忽略！\n⬇️那我就跟大家建议几点，希望对你们有帮助：\n1️⃣形成健康的作息习惯，其实11点前能够睡觉是最科学的，但是绝大多数人（包括我自己）都做不到，所以我觉得最晚不要超过12点睡觉，长期熬夜也容易发胖呢！\n2️⃣健康的作息习惯有了，接下来当然是饮食习惯啦，三餐一定要正常吃，绝对、绝对不能胡乱节食，一个是这样一定会反弹，另一点就是很多菇凉因为节食减肥连姨妈都不来了，这个问题很严重☝️。\n3️⃣可以结合着保健品由内而外双管齐下 - 给大家推荐几款针对女性生理健康的：\n✨Blackmores月见草胶囊：190粒/瓶，一天1~3粒，主要针对痛经和经期不准，小红书就可以买到😉\n✨hyperbiotics合百益蔓越莓益生菌：30粒/瓶，平常饭前饭后都能吃，一天1-2粒，要是需要密集型就2-3粒，旗舰店就有卖，价格也不贵！\n✨GNC葡萄籽精华：100粒/瓶，每天睡前一粒，这个功能是抗氧化，不是针对妇科炎症的，但是女性坚持吃也hin好哦~\n4️⃣生命在于运动，要锻炼！我一直有健身的习惯，一周会去3-4次健身房，其实当你习惯了锻炼就停不下来了，会成为生活中不可缺少的一部分。如果你所在的城市空气好，建议多去户外锻炼，经常跑步可以增强体质。平时如果太忙没时间去健身房也可以在家跟着keep练哦，每天2组就ok啦~\n☝️最后要嘱咐大家，平时多喝水，多吃蔬菜水果和高蛋白的食物，多运动才能健健康康的哦！\n.\n那今天的分享就到这里，希望对大家有帮助，我们下支视频见😘\n#9月囤货反馈[话题]##最新保健品播报[话题]##日常美容保健品[话题]##健身是把整容刀[话题]##我的护肤日常[话题]##种草能手[话题]##新草报道[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhVY96xn-b0hwe24Y1Uvv-Svxwlp_compress_L1',
    'video_id': '58d87ce11d0ca30f602991f5',
    'title': '锁住这道春风里弥漫的鲜气——芦笋百合炒虾仁',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n芦笋百合炒虾仁，是一道家常菜。\n制作原料主要有芦笋、百合、虾仁。\n★★★★★\n创意指数\n芦笋百合炒虾仁\n▼\n芦笋百合炒虾仁\n·食材·\n芦笋、虾仁、百合\n蒜、姜、盐\n料酒、胡椒粉、生粉\n1.虾仁倒入料酒、生粉、盐、胡椒粉\n2.拌匀腌制10分钟\n3.百合用水浸泡防止变黑\n4.姜切片\n5.蒜切末\n6.芦笋去皮\n7.切成段\n8.过沸水30秒左右\n9.热油锅爆香姜蒜\n10.倒入虾仁炒至半分熟\n11.倒入百合、芦笋\n12.清炒片刻加入料酒、盐\n13.下班犒劳下自己吧！\n#超级下饭的家常菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/632c7e6cbf1a8c0d5ae3fbcae61658737878dba0_r_ln',
    'video_id': '58d881b934609428510df6dc',
    'title': '奶油居然可以这么打发，速度快到你都想不到',
    'video_tag_list': '',
    'content': '每次喵酱手动打发奶油，总有人吐槽喵酱有麒麟臂。今天教大家一个小妙招，不用麒麟臂也能比较快速地手动打发奶油哟！'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lvTX3TLmSjnwUJnv8paekfw1rs6Z_compress_L1',
    'video_id': '58d89dec02f37d3abae914d7',
    'title': '我的旅行箱里有什么！第一集',
    'video_tag_list': '我的旅行标配',
    'content': '哈哈 我本来想给大家录一个短视频。结果要分两集。\n回来给大家整理一个需要注意的旅行文。比如泰国要自己带拖鞋什么的。现在就简单的给大家看看视频吧。\n两个视频都是五分钟。\n#旅行必带[话题]#\n#我的旅行标配[话题]#\n#旅行装[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/lnfQG6rOPTxsycIxUR6OeRBNFlKY?sign=499bef76529d259545e86005e6580663&t=65fb06d4',
    'video_id': '58d8a17c14de41785677f96d',
    'title': '我的旅行箱里有什么？第二集',
    'video_tag_list': '我的旅行标配',
    'content': '总之，不带完整，我这心里就不得劲。所以都带了。大家分享一下。\n还有熊本熊湿巾说成轻松熊了，我对不起部长[活力]\n#旅行装[话题]#\n#旅行必带[话题]#\n#我的旅行标配[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/pgc/8c4ec56e-363e7fb-8ccc-71a41158c9a8_compress_L1',
    'video_id': '58d8f27e346094265b71e56f',
    'title': '超简单收纳法！袜子如何折叠才能更省空间',
    'video_tag_list': '',
    'content': '有时候买了很多收纳箱，放没几件衣服袜子就塞得满满的了。对于喵酱这个收纳控而言，如何优雅的收纳衣物，一直是一门很深奥的学问。\n今天的喵招就教大家能够超省空间的袜子折叠法，四四方方的看起来非常舒服，而且能够大大提升你的收纳效率哟～(◍•ᴗ•`◍)*＊抛弃以前那种看起来圆鼓鼓的叠袜法吧，不用把袜口扯得很大，所以这种叠法还可以延长袜子的寿命呢~#生活妙招\n#视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/4465162f-54a6875-ae78-628e787198ba?sign=810fffd9a4d19a1e876a6f4582eca848&t=65fb06d4',
    'video_id': '58d916017fc5b8453d7fbb20',
    'title': '网红减肥也作弊｜姨妈期健身怎么练',
    'video_tag_list': '',
    'content': '一场雨夹雪之后，\n北京的冬天officially算是过去了，\n健身房里蹭蹭的上人，\n我们的studio这两天也特别热闹。\n经过一个冬天的自我欺骗，\n大家开始战战兢兢的正视自己囤了5个月的膘，\n明白大臂上白花花的肉马上就要藏不住了。\n还有好多人，\n胳膊也细，\n但是软塌塌的没有线条。\n其实在我看来，\n女生最好看的，\n就是夏天穿吊带时露出小麦色紧实的肩臂，\n因此今天的视频就带大家练！肩！臂！\n我们“红”了以后，\n收到来自大家最多的疑问，\n就是经期到底能不能锻炼，怎么练？\n其实理论上来讲（不是中医的理论昂），\n经期不仅可以，而且应该锻炼，\n有的人在经期一点儿感觉都没有，\n深蹲该50kg一两都不带少的（比如Weiya）。\n而我自己在经期的前两天会明显腰酸无力，\n所以会避免做大重量和高强度的训练。\n当然，因为每个人的体质都不同，\n大家还是要根据自己的感受量力而行。\n如果有痛经的问题，\n则应该尽量杜绝腹肌训练，\n因为很多动作会挤压子宫，\n造成经血不调。\n最后，我要坦白，\n因为血崩了，\n所以我在低碳日偷吃了巧克力芝士雪球，\n而且假装自己没吃，\n反正我无赖也不是一天两天了🙄️\n如果喜欢我们的视频，就请关注公众号 Fit4Life健身与美食， 我们每周三更哦！😄😄😄\n#经期如何健身运动[话题]#\n#肩部塑形视频[话题]#\n#手臂塑形视频[话题]#\n#健身食谱教学视频[话题]#\n#健身器械教学视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/e495af89-fcfaa76-bf56-95bc298778ba?sign=37ee277bae55858a0c4927a041d6ba83&t=65fb06d4',
    'video_id': '58d919127fc5b8609c7f4471',
    'title': '最全美背训练指南（还有逗比部分请看完整版）',
    'video_tag_list': '',
    'content': '我们两个并不是专业的健身教练，就是自己喜欢，建议大家在健身之前还是咨询专业人士昂。\n当然，想看我俩逗比的可以去公众号关注我们哟（Fit4Life健身与美食）～\n#健身器械教学视频[话题]#\n#背部塑形视频[话题]#\n#哑铃杠铃教学视频[话题]#\n#无器械锻炼视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lt5qWeui1c9jbc-4cINwYaK4V1rv_compress_L1',
    'video_id': '58d935e8faa0521668ee76a2',
    'title': '手残党的卷发卷刘海视频',
    'video_tag_list': '',
    'content': '上次发的卷发视频没想到小红薯还挺多问题咨询的，这次睡前随便剪个，还是没洗头的新手，勿喷哈！\n卷刘海从1：38开始\n为了庆祝5w粉，此条视频下评论告诉我喜欢看我的哪类笔记，4月5日抽取一名幸运儿送出神秘小礼品一份哦！[飞吻R][飞吻R]'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/58e15cc6-274f668-8313-1eb3326e8bcb?sign=b884c35d59fb597617bcaa4155ffa8c9&t=65fb06d4',
    'video_id': '58d94bb47fc5b87843f7ba1b',
    'title': '后-VIP活動花絮',
    'video_tag_list': '',
    'content': '活動花絮剪輯'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpbDhKBRMO15kQzc0K4P-uyplyhu_compress_L1',
    'video_id': '58d9cd38faa0522105d7d4aa',
    'title': '豆腐最嫩滑的吃法——翡翠豆腐羹',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n菠菜豆腐羹是民间的传统家常菜，以其清淡爽口而深得人们喜爱。\n众所周知，豆腐和菠菜都是很有营养，而两者的搭配更是营养丰富。\n★★★★★\n创意指数\n翡翠豆腐羹\n▼\n翡翠豆腐羹\n·食材·\n菠菜、韧豆腐、盐\n1.用刀柄把豆腐压碎\n2.菠菜切末\n3.沸水倒入豆腐\n4.倒入菠菜末\n5.煮沸后勾芡\n6.撒入盐调味\n7.均匀搅拌\n8.清香扑鼻的翡翠豆腐羹就完成啦'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luOULo9c7FfmQHylBPrXmwO5UtIp_compress_L1',
    'video_id': '58d9d44137cec90de3d5f53c',
    'title': '【 让懒人也爱上洗刷～ 】',
    'video_tag_list': '如何选择和使用化妆刷',
    'content': '分享一下我日常的洗刷方法以及用到的一些小工具。\n如果刷具清洁不到位则会影响妆感，甚至让刷毛受损。\n这款洗刷水我已经用了好多瓶了，清洁很彻底。\n它的快干效果是我特别喜欢的，基本晚上洗第二天早上就能用。\n希望大家都可以温柔的对待自己的刷具，白了个白～\n#如何选择和使用化妆刷[话题]#\n#化妆刷如何清洗[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/6b8d67af-bad0370-973f-82b52b53985e?sign=2519f259d55a4619c44a8555029e05cb&t=65fb06d4',
    'video_id': '58da46f97fc5b808d7b706f5',
    'title': '🌈每天都可以化的日常妆 by @Anna_ZhuXuan',
    'video_tag_list': '迪奥 Dior 魅惑唇膏;肌肤之钥 clé de Peau Beauté 美白隔离;圣罗兰 Saint Laurent TOUCHE ÉCLAT 明彩笔;魅可 M.A.C 时尚焦点单色眼影;纳斯 NARS 炫色腮红;花娜小姐;Real\xa0Techniques 眼部套刷;Real\xa0Techniques 旅行套刷;迪奥;Anastasia;3CE 超细不易晕染眼线液笔;凯婷 ;资生堂 Shiseido 3D立体超广角213睫毛夹;赫莲娜 HELENA RUBINSTEIN 猎豹睫毛膏;魅可;乔治阿玛尼 Giorgio Armani 臻致丝绒哑光唇釉;斩男妆这样画',
    'content': '用到的产品：\nDior | dior addict lip glow #004\nCle De Peau Beaute | voile blanc brighting enhancer base\nDior | dior skin forever perfect cushion #020\nYves Saint Laurent | touche éclat #2\nMAC | eye shadow #Wedge\nReal Techniques | brow brush\nReal Techniques | domed shadow brush\nNARS | blush #Orgasm\nReal Techniques | multi task brush\nReal Techniques | base shadow brush\nMiss Hana | shining under eye crayon #pearl pink\nAnastasia | tinted brow gel #Caramel\nStylenanda 3CE | super slim pen eyeliner #Brown\nKate | deep trap eyes #BR-1\nReal Techniques | accent brush\nShiseido | eyelash curler\nHR | lash queen feline blacks #01\nMAC | mineralize skin finish #Soft and gentle\nReal Techniques | pointed foundation brush\nGiorgio Armani | lip maestro #500\nSweety-eye正品美瞳网 #青春巧克力\n#斩男妆这样画[话题]##日常妆容打卡[话题]##日常眼妆怎么画[话题]##夏日缤纷妆容色[话题]##美妆新人[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/e13444b4-1806d82-b395-38bc8e299b08?sign=4705c8f210cd14d2a1c6fbb8f18cfd2e&t=65fb06d4',
    'video_id': '58da533a34609410a272ed8b',
    'title': '在家就可以做的比基尼肩臂训练',
    'video_tag_list': '',
    'content': '好多人说没时间去健身房，其实只要有个哑铃（片），好看的肩臂在家也能练！\n视频里只是一遍的动作，如果想要效果明显，建议至少跟着做两遍，每周三次哦！\n健身真的是最公平的事情，付出和结果永远对等，大家加油昂～\n如果喜欢我们的视频，欢迎关注我们的健身与美食，北京的朋友可以来我们在建外soho西区17号楼2505的实体店玩儿哦～\n#肩部塑形视频[话题]#\n#背部塑形视频[话题]#\n#哑铃杠铃教学视频[话题]#\n#无器械锻炼视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ffcdfed10b6aa864a501e7975767d82851481cd6_v1',
    'video_id': '58db1eb4b46c5d47f487fb93',
    'title': '苏州樱桃肉，酥烂入味，色香味俱佳！',
    'video_tag_list': '',
    'content': '#跟着视频学做菜[话题]#\n★★★★★\n小圆食记\nMenu\n\u200b樱桃肉是一道江苏省苏州市的传统名菜之一，属于苏菜系。\n始创于江苏，清乾隆年间传入宫中，特点色泽樱红，光亮悦目，酥烂肥美。\n★★★★★\n创意指数\n樱桃肉\n▼\n樱桃肉\n·食材·\n五花肉、菜笕、红曲米\n葱、姜、山楂、冰糖\n生抽、料酒、盐\n1.冷水下五花肉\n2.放入葱结、姜片\n3.大火煮沸后倒入料酒\n4.过温水清除杂质\n5.汤汁滤出备用\n6.红曲米用纱布包起\n7.肉皮切出小方格\n8.翻面切出井字格\n9.砂锅底部放入葱、姜片\n10.肉片部分朝下放\n11.放入山楂、红曲米、汤汁\n12.倒入生抽、料酒、盐\n13.大火煮开后转小火煨40分钟\n14.取出葱结、红曲米，倒入冰糖关盖收汁\n15.将肉移入碗中，淋入汤汁\n16.放入蒸锅中焖煮半小时\n17.菜笕过水摆盘围边\n18.淋上酱汁即可\n19.苏州人的春天——苏州樱桃肉'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/e5f05efafd21ab7e898780829540faba9df63838_r',
    'video_id': '58db8c793460940d4cdf4380',
    'title': '尴尬！你的拉链又拉不上啦？快点擦擦这个吧！',
    'video_tag_list': '',
    'content': '生活中经常会遇到拉链卡顿、不流畅的问题，有时候喵酱会感觉影响了一整天的好心情呢。\n今天又要请出万能的“凡士林”小伙伴啦！只要轻轻一抹，就能立刻让卡顿发涩的拉链恢复顺滑哟！亲测非常有效哟~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmsT_jDCZf6vOAJ9AiUayp0AqGLY_compress_L1',
    'video_id': '58dc721ad2c8a5062e81416d',
    'title': '甜蜜和幸福一起来品尝—草莓夹心巧克力',
    'video_tag_list': '',
    'content': '#最拿手的草莓食谱[话题]#\n★★★★★\n小圆食记\nMenu\n巧克力的香甜浓郁，草莓的清香，再配合上花生碎；\n这道小点心草莓夹心巧克力可是居家旅行必备之美食。\n★★★★★\n创意指数\n草莓夹心巧克力\n▼\n草莓夹心巧克力\n·食材·\n草莓、巧克力、花生\n1.用牙签固定住草莓\n2.捣碎花生\n3.倒出备用\n4.巧克力掰成小块\n5.巧克力隔水用小火加热至融化\n6.搅拌均匀\n7.草莓在巧克力酱里面转几圈\n8.撒上花生碎\n9.下午茶时间到啦！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/cedbbabf-decc59b-aa5d-8990e33cbb1d?sign=8e478b3a7b549a5aa82f28a192f1d634&t=65fb06d4',
    'video_id': '58dce2007fc5b81bb094df91',
    'title': '只要30分钟，帮你持续燃脂40小时的高效塑形利器',
    'video_tag_list': '',
    'content': '工作太忙，\n作为加班狗和出差狗的你完全找不出时间去健身房？\n别着急，\n阿姨们为你量身定制随时随地都能练的HIIT课程！\n啥是HIIT?\nHIIT又叫高间歇有氧，被实验证明最有效的塑形利器！\n每次30分钟，\n练完后还会持续燃脂40小时，多划算！\n快快跟着阿姨们练起来！\n如果喜欢我们的视频，欢迎关注我们的公众号 Fit4Life健身与美食，在北京的朋友欢迎来我们在建外soho西区17号楼2505的studio玩儿昂～\n#全身减脂教学视频[话题]#\n#无器械锻炼视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/3e83e20c-28fb31b-a22b-8b8d9f5f2983?sign=fbed092b31b6fb965f1e5188355fbeef&t=65fb06d4',
    'video_id': '58dcfa7c34609448c4474918',
    'title': '【视频】换季除了换衣服💋唇膏也得换',
    'video_tag_list': 'YSL圆管唇膏试色;乔治阿玛尼 Giorgio Armani 黑管漆光迷情唇釉;香奈儿 Chanel ROUGE ALLURE炫亮魅力口红/唇膏;娇兰;迪奥',
    'content': '#春夏最爱的清新口红[话题]#\nHi大家好，春夏爱用唇膏分享来了~具体内容大家看视频哈~~\n💋YSL圆管12\n💋阿玛尼黑管500\n💋香奈儿136\n💋迪奥DIOR漆光唇釉740\n💋娇兰M65\n滋润度：12=500=740＞M65＞136\n之后还会跟大家分享爱用品哦~\n谢谢支持~\n你的化妆台上永远缺一支唇膏😂\n#YSL圆管唇膏试色[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltl9sQCSU0uU70sXtVRoQDlCR9UY_compress_L1',
    'video_id': '58ddc410b46c5d1efb4af549',
    'title': '0失败快手菜—糖醋脆皮豆腐',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n豆腐营养丰富，含有铁、钙、磷、镁等人体必需的多种微量元素；\n还含有糖类、植物油和丰富的优质蛋白，素有“植物肉”之美称。\n★★★★★\n创意指数\n糖醋脆皮豆腐\n▼\n糖醋脆皮豆腐\n·食材·\n韧豆腐、西红柿\n葱、生抽、料酒、糖、醋\n1.洗净后豆腐中间切开\n2.依次切成块备用\n3.西红柿去芯\n4.西红柿划网刀切成末\n5.倒入料酒、生抽、糖、醋、水调成糖醋汁\n6.热油锅放入豆腐煎炸\n7.底部成焦黄色翻面炸至两面金黄，出锅备用\n8.油锅倒入西红柿\n9.清炒至变软倒入豆腐\n10.倒入糖醋汁\n11.大火收汁\n12.撒上葱花即可'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/f2b6333b1d1773387f43e443b605849a4723d5e3_r_ln',
    'video_id': '58de08f7faa0521d021d298a',
    'title': '健身房器械使用指南👉🏻美背！背部塑形挺拔',
    'video_tag_list': '',
    'content': '心心念念的视频教程来啦，跟着我一起练出美背，告别驼背，完美塑形☺\n👉🏻视频里的动作依次是：\n🌟1.杠铃俯身划船\n经典动作\n女生重量：5KG\n🌟2.单臂俯身划船\n女生重量：5KG~10KG\n🌟3.山羊挺身\n又练到翘臀，又练背部\n视频里的山羊挺身，幅度要更下。但是那天去朋友的健身房，这个器械不稳，有点问题\n所以视频里我的幅度没有很下去，大家注意哦，幅度要大大的，感受臀部加紧，哈哈。\n🌟4.硬拉\n经典中的经典动作，又练背部又练翘臀✌️\n女生重量：5KG~10KG\n按照自己的能力，可以慢慢加重量。\n🌟视频的的动作每个做15个，每个动作4组\n夏天要到了，大家准备好了吗？\n👉🏻文字具体攻略，我上一篇笔记有详细攻略和讲解，大家可以看看，哈哈哈。\n会多多分享视频和健身攻略给大家哦，么么哒\n健身器械教学视频 无器械锻炼视频 我为瘦身打卡 肩部塑形视频 背部塑形视频\n健身器械的正确使用方式 必须要安利的健身动作'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/93f595df-85bbd94-a3ad-0188e866ba00?sign=5bbfea86bc494d05424f589332e92160&t=65fb06d4',
    'video_id': '58de361c7fc5b87d37e9d639',
    'title': '教你一招，拯救断裂的口红，不再害怕手残男友',
    'video_tag_list': '',
    'content': '新买的口红刚到，迫不及待旋转出来，完美的膏体啊！正要慢慢享用时，它竟然断了！这难道就是传说中对于女生而言的“世界十大惨案”之一吗？不过，憋方！赶紧来看这期的喵招，小天使喵酱教大家只要用吹风机，就能优雅解决这种尴尬的问题哟~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrX_7Jc8dUV1q_9q7Oyi0X24SZym_compress_L1',
    'video_id': '58de6f0b7836230b69961a85',
    'title': '5分钟快手自然通勤妆！手残党福利！',
    'video_tag_list': "雅漾;美宝莲 Maybelline Fit Me遮瑕液笔;I'M MEME 我爱修容棒;猿始人 H.S MAKE 白玫瑰纯露喷雾;Tarte;兰蔻;兰蔻 Lancome 催眠睫毛膏 -#01 Noir Hypnotic ;梦妆;Real\xa0Techniques;Real\xa0Techniques 美妆蛋;无印良品;无印良品 MUJI 睫毛夹;乔治阿玛尼 Giorgio Armani 极缎丝柔精华粉底液（滋润型）;元气少女必备腮红",
    'content': '第一次拍视频传小红书呢～请多多包涵～🙏🏻🙏🏻\n这个妆主要是提气色的，妆前妆后不会区别很大～不过也够快手够简单，手残党也没在怕的！最适合忙忙碌碌的早晨了～💃🏻💃🏻\n产品list：\n1. 雅漾日间隔离乳这款隔离超适合干皮用来打底，保湿效果不错～还有spf30的防晒值，我超爱！[飞吻R]资生堂工厂代工的，所以不会像其他欧美防晒那样油那样闷，超级好吸收又温和～👍🏻👍🏻\n2. 阿玛尼发光小滴管02号 精油类粉底液超级水润好推，轻度遮瑕，适合瑕疵少的干皮，比如我！（脸呢？）[偷笑R] 妆效是光泽肌！\n3. 美宝莲fitme遮瑕10号色 平价好用，适合干皮的一款遮瑕～轻薄好推眼下也不卡粉～\n4. IM MEME修容棒 质地丝滑好涂抹好推开～效果自然～\n5. 猿始人白玫瑰纯露喷雾 喷雾很细，适合用来定妆，不会弄花妆面～玫瑰纯露又能保湿，香味又好闻！\n6. tarte腮红 色号tipsy 粉橘色系超级显气色好🤗🤗但又不会太粉嫩显得很幼齿～最大的优点是超持久！超长待机一天12个小时就是不脱妆呀不脱妆～#元气少女必备腮红[话题]#\n7. 兰蔻催眠睫毛膏 根根分明又浓密～不会苍蝇腿！我这个是老版的会晕，所以记得买防水版的～#兰蔻 Lancome 催眠睫毛膏 -\n8. 梦妆唇釉09号色 算是大热的土橘色系的吧？但没那么土，比较偏红，更像是枫叶色～🍁显白显气质～\n工具list：\n1. real techniques 美妆蛋 打湿以后很好用～软软的，不怎么吸粉～\n2. real techniques 底妆刷 虽然是底妆刷但我觉得因为是纤维毛所以略硬，上底妆易产生刷痕，用来上膏状阴影倒是刚好！简直完美～\n3. 玖歌国色天香系列腮红刷 国产刷具～动物毛软软的不扎脸～抓粉力刚刚好～\n4. muji便携睫毛夹 弧度很贴合我眼睛弧度～不会夹到眼皮，夹完睫毛很翘！可以持续一整天～\n希望大家喜欢今天的视频，第一次拍用的手机前置摄像头，画质渣，技术渣，大家凑合看看吧～如果你们喜欢这样的形式以后会改进设备哒～～～接受合理批评和建议～🙋🏻🙋🏻不接受谩骂和羞辱～🙅🏻🙅🏻\n啊 关于眉毛 我真的是不会修不会画 刚好有刘海 就skip掉了～就当是最近流行的野生眉吧～科科～💃🏻💃🏻\n#五分钟妆容挑战[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvAU2gzr8s1L7_0XGwUsC2XRoELN',
    'video_id': '58de7b30fb68a26f70fb6eac',
    'title': '王公子的心得—底妆视频篇（王公子说话啦）',
    'video_tag_list': '底妆评测看视频;芭比波朗 Bobbi Brown Intensive Skin Serum Foundation密集修护虫草菁华粉底液;肌肤之钥 clé de Peau Beauté 钻石光感隔离乳/黑管隔离滋润型 SPF20 PA++;sleek   高光修容盘',
    'content': '艾瑞巴蒂大家好！这个视频是一篇关于底妆的视频。作为非专业人士的一个测评吧......#底妆评测看视频[话题]##日常妆容打卡[话题]#\n惯例：王公子是混干皮（T区出油）敏感肌白皮偏黄。底妆要求：尽量控油，脸颊不起皮，不过敏。\n坐标北京，95后学生一枚。\n整个视频用到的产品：\n🌟cpb长管儿隔离\n🌟Bobbi brown虫草粉底液\n🌟makeup for ever的眉型修正液专柜或丝芙兰都有。\n🌟眼影COLOURPOP，色号均为I SPY 、MELROSE&MOONWALK。\n🌟修容\n🌟睫毛膏是Dior纤羽防水睫毛膏。\n🌟唇膏MAC，色号MOCHA。\n以上是用到的产品，如评论有问均不回复（望大家理解）\n这款粉底液是我用过最长一段时间的，除了好用我无话可说，目前我还没遇到过说他不好的评价。我只想说他是一款养皮的粉底液，就算再差的皮肤状态涂它是不会出错的。其他官方的介绍我就不废话了，随便一个po主都有写。\n尤其是上妆的第三到第六个小时左右是最显皮肤好的一个时间段（我是这样，其他人我就不知道啦）\n就算是超过八个小时也不会有很大的瑕疵，不卡不干，挺棒的。\n唯一的缺点就是不太便宜，对于学生来说...咳咳...\nPS：如果没有“请问、您好、谢谢”等用语我是不会回复的，毕竟现在是文明健康的社会，没有人喜欢没有礼貌的人，谢谢合作啦！笔芯！也欢迎大伙儿和我讨论心得和建议看法💬\n最后谢谢大家的观看，回见了您内💌'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lni1htX1JJ0sS0OgrKwIZfT3gP6q_compress_L1',
    'video_id': '58df3f9ffaa05219a7fecdb0',
    'title': '两分钟任意拍 | 用视频分享你的护肤步骤',
    'video_tag_list': '护肤步骤看视频;护肤步骤看视频',
    'content': '本期视频话题：#护肤步骤看视频[话题]#\n小红薯们好～美妆薯日常刷评论，发现有看到好多小红薯不知道护肤步骤哎！\n于是美妆薯发起#护肤步骤看视频[话题]#的视频活动，不管你是护肤大神还是自成一派，简单拍摄两分钟的视频，就可以来分享自己的护肤步骤了哟～\n心急想看答案的小薯，请戳链接#护肤步骤看视频[话题]#已经有很多奥斯卡薯率先分享了！稍后美妆薯还会出合集呢～科科\n想要发视频但还没权限的北鼻们在下面留言🙋🏻🙋🏻🙋🏻美妆薯会来勾搭你们，美妆薯爱你们[飞吻R]\n———薯队长华丽登场———\n大家好，我是美妆薯的好朋友薯队长，美妆薯力邀我来拍个视频给大家做个示范😬😬我给大家示范三种护肤步骤的拍法～想要拍摄护肤步骤的视频，稍微瞄一眼薯队长的视频就能学会啦～\n🌝第一种：基础简单版本——卸妆+清洁+补水\n卸妆的重要性美妆薯强调无数遍了，哪怕只用防晒，都会乖乖卸妆；\n洁面产品建议大家在手上搓出泡沫，泡沫能带走脸脸上的油脂灰尘，水冲洗一下，脸脸就干净了；\n皮肤状态好的时候，我只用棉片擦拭一下皮肤，做个二次清洁。然后再取少量化妆水拍在脸上，就可以简单的补水了。\n🌝第二种：日常精致升级版——从洁面到面霜\n洗完脸后，我会使用肌底液，来强化肌底吸收能力。\n（刚刚不懂事的小助理拿错薯队长的肌底液当成精华，她已经知错了[扶墙R][扶墙R]）\n然后再拍化妆水，接着涂一些功能性的精华，比如美白精华/抗氧化精华，涂抹精华时要记得避开眼周；\n用完精华，在眼睛处使用眼霜。\n最后使用乳液或者面霜就可以了。\n关于究竟是用面霜还是用乳液，一般而言，干性皮肤的小红薯可以用面霜，油性皮肤的小红薯用乳液足够了。\n🌝第三种：大神级华丽进阶版——如何叠加N多个精华\n周末想要放松一下，照顾一下我的皮肤，那我会叠加N多个精华，保湿精华、水杨酸精华、美白精华、抗氧化精华等等哦……\n我会根据质地来使用：先用水性的精华，再用油性的；先用清爽的，再用滋润的，要是有哪种精华会搓泥，我一定放在最后用。\n———美妆薯分割线 ———\n终于甩掉了上面啰里八嗦的薯队长🙊🙊\n看完了薯队长的视频，是不是觉得拍护肤视频超级简单呢！赶紧来参加#护肤步骤看视频[话题]#话题吧～\n薯队长为大家示范了三种不同的护肤步骤视频，聪明的小红薯是不是一看就会？你可以在视频中介绍简单的或者复杂的化妆步骤哦～\n【如何参加视频活动？】\n1️⃣参加话题活动就是在发笔记的页面，输入框的旁边# 戳下去，输入#护肤步骤看视频[话题]#～\n2️⃣还不知道怎么发视频的朋友们，戳美妆薯的《美妆博主第一步！从拍一个30S的眼影视频开始～》\n3️⃣视频中提及的重点，可以在笔记中用文字再强调一遍哦～\n美妆薯期待看到你们的视频哟～[飞吻R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmv37FsNEPEpIJPyQzxeKXWt9urC_compress_L1',
    'video_id': '58df5745d2c8a53ac97ce482',
    'title': '【Adora干货】零瑕疵底妆必备—多色遮瑕盘实用方法',
    'video_tag_list': '视频教你画底妆;Physicians Formula 双头黑眼圈遮瑕膏;美宝莲 Maybelline 黑眼圈橡皮擦遮瑕膏;NYX 遮瑕3C修容盘;Wet n Wild 无瑕好漾系列四色修颜遮瑕色盘;Tarte;丝荻拉  Stila 七色遮瑕修容盘',
    'content': '注意⚠️：今天只说的是有！颜！色！的修颜遮瑕修容盘 不是所有类型的遮瑕盘。[活力]#完美底妆这样画#视频教你画底妆\n多色修容遮瑕，本质上就是利用颜色之间的互相抵消遮盖来达到遮盖面部瑕疵，实现零瑕疵底妆。\n一些遮瑕盘之间的颜色使用在瑕疵部位可以达到消除脸上不同程度甚至所有瑕疵的效果。再去修饰底妆就会有透亮完美的肌肤了。但这个过程也需要根据不同的皮肤问题来进行不同的遮瑕步骤，能让遮瑕步骤在妆容上起到无与伦比强大的作用。\n关于底妆步骤请观看另一份视频《视频教你化底妆》在此不赘述\n第一、选择遮瑕盘。市面上的各类遮瑕盘比比皆是，而你也不知道到底买哪个？是干什么用的？ 貌似都说是遮瑕盘，到底区别又在哪里？\n1⃣️彩色遮瑕 是典型的对皮肤有色泽修正作用修颜作用的遮瑕产品。它不同于一般的肤色系🏼遮瑕只是在色号深浅上不同，肤色系盘主要是可以对面部起到面部不同部位肤色深浅塑造作用和局部遮瑕，达到轮廓分明的效果。\n多色、彩色遮瑕修容突出在于更改修正皮肤本来色调的遮瑕选择。eg.比如我想消除脸部的红色调，就选择彩色遮瑕里的绿色来进行遮盖抵消掉红色。\n于是你看到那么多种遮瑕盘，而每种颜色都不同😳心里都在WTF到底都是什么鬼我怎么知道买哪个😂\n应付常见的面部问题遮瑕当然有4～6个颜色就足足够了。（除非是你想遮纹身、胎记、伤疤等这些特殊效果遮瑕）\n以下几盘都是热门选手：\nNYX 遮瑕3C修容盘 种草她第一，看谁拔得快😂\nWet n Wild 无瑕好漾系列四色修颜遮瑕色盘\n\nWet n Wild 无瑕好漾系列四色修颜遮瑕色盘（视频露出以及遮瑕示范图）\n视频露出tarte6色遮瑕盘详细名称为：Tarte Athleisure Skincare Collection for Spring 2017 （购于他人转）\n\n\nstila的遮瑕盘也是热门选手 只是我更喜欢💕tarte的滋润度\n郑瑄茉 JUNGSAEMMOOL 彩妆师专业遮瑕盘\n（视频露出滴遮瑕盘还有）：\nphysicians Formula 遮瑕盘\nmakeup revolution 遮瑕盘\nMorphe多色遮瑕盘\ntarte item wipeout color correcting palette 修颜遮瑕盘\n第二，有了自己的日常遮瑕盘或是 有着重需求遮瑕的人。哪些颜色用于遮什么？[少女心]\n紫色消除黄色：遮黄、暗沉、点亮沉闷肤色\n粉色消除棕色：斑点、暗沉、纹、晒斑\n黄色消除紫色：遮紫、淤青、缓和泛红\n绿色消除红色：晒伤、红斑、泛红、红血丝、红肿、红痘印\n红色消除绿色：顽固黑眼圈、深暗眼斑、纹身\n橘色消除蓝色：遮蓝、黑眼圈、淤青\n桃色消除蓝色：黑眼圈、淤青、色素斑、过亮\n第三，肿么用？涂哪里？\n脸部不同区域相对经常出现的问题：\n脸颊：泛红、斑点、暗沉、惨白、淤青\n鼻翼：泛红，痘痘、毛孔\n黑眼圈、泪沟、眼部暗沉、\n唇周：暗沉、发黄、泛红\n额头：泛红、暗沉 等等\n特殊部位遮瑕：（视频露出）it cosmetics byebyeundereye（购于beautylish）\nPhysicians Formula 双头黑眼圈遮瑕膏\n美宝莲 Maybelline 黑眼圈橡皮擦遮瑕膏\n第四：注意⚠️ 上遮瑕后不要像涂护肤乳一样的涂抹遮瑕，而是轻点式的晕开遮瑕产品在脸上，否则遮盖不住反而都被涂开了。\n重点部位重点遮瑕，不必要每个人都需要全脸修正肤色的，只做局部修正遮瑕即可。因人而需，因人而异。[讨厌]\n没有人会有一张完美无暇的脸，你看电影🎬那还有后期滤镜效果，拍广告修图师都是专业技能要高超的职业，so我们都要接纳自己的不完美和瑕疵，来试着和瑕疵熟悉，明白自己每个瑕疵的颜色和深浅程度才能选择最合适贴切的遮瑕色进行遮瑕修正。\n这样零瑕疵底妆并不是天方夜谭。拍照你都不用美颜那么辛苦啦💦[活力]出片的视觉反而更真实。\n嗯嗯 详情见视频内容，需要修容区域图的和对应颜色图以及视频内容图片请给我留言。[喜欢] mua～💋'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lunsWJOuUgXnvjlVz68EaXED_QJt_compress_L1',
    'video_id': '58e0682c02f37d7d6035f5fd',
    'title': '本期话题：用视频记录美食',
    'video_tag_list': '用视频记录美食;用视频记录美食',
    'content': '#用视频记录美食[话题]#\n薯队长猜，此时此刻，要么你已经在出门郊游的路上，要么你还在被窝里考虑着brunch吃什么。\n无论你是外出探店，还是在家亲自下厨，总会发现一些美食有意思的瞬间。\n比如古镇街边小吃的现场制作，家里烘焙出炉的时刻，餐厅里惊艳的现场餐品制作，总让你忍不住拿起手机拍上一段视频来纪念~\n快快快来参与：听起来名字特朴实、发笔记一定特诱人的新话题#用视频记录美食[话题]# \xa0！\n【视频拍什么？】\n如果你亲自下厨做菜烘焙，可以记录激动人心出炉/出锅的时刻，超级简单，只需要一个镜头就能完成！如果身边恰好还有小伙伴，可以让TA帮你拍摄制作中间一些小步骤。\n如果你和好友外出探店，可以用视频捕捉餐厅里那些惊艳的瞬间，比如海底捞里的甩面表演，比如餐厅里大厨现场亲自为你做的甜品，比如咕嘟咕嘟，冒着热气，渐渐沸腾的火锅……\n【笔记文字写什么？】\n如果是在家拍摄的做菜烘焙视频，记得用文字简单介绍一下你的制作方法和步骤。\n如果是在餐厅里拍摄的美食视频，除了介绍这道餐品以外，一定记得加上餐厅名字、所在城市和地址喔~\n最后记得在笔记文字里@你的小红薯伙伴，让更多小红薯一起加入美食视频放毒大计之中！！\n如果没有视频权限却又很想发笔记的宝宝，快来给薯队长或生活薯留言吧！\n以上美食视频分别来自小红薯@小肥肥猪和大长脸羊的日常\xa0@Agieemia皮卡秋\xa0@李奶奶的厨房\xa0@太阳猫美食TV @喵招'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgZyQcZ7DfN0oYYxpF2ieEmJbtWT_compress_L1',
    'video_id': '58e0af9602f37d1e3a35f602',
    'title': '生活情景游戏绘本之《睡觉吧！》',
    'video_tag_list': '',
    'content': '#视频绘本打卡[话题]#\n薯宝宝前些天买了 0-3岁幼儿生活场景绘本，想用视频的方式拍给大家欣赏~\n【书名】：0-3岁幼儿生活情景游戏绘本《睡觉吧！》\n【作者】：阿妮卡托雷\n【出版社】：长江少年儿童出版社\n【推荐理由】:这本绘本里，宝宝在睡觉前有种种要求——想要喝NeiNei，想要玩具，想要讲故事，就是不太情愿一人独自睡。最后宝宝乖乖入睡是因为有妈妈的陪伴，让宝宝有安全感；\n麻麻们和宝宝一起阅读这本书的时候，就可以借此机会，让宝宝培养起良好地入睡习惯，让宝宝来说出心里的想法~\n所以想要推荐给各位薯妈！麻麻们也来一起#视频绘本打卡[话题]#吧'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lkRnzrlUOB3Ktqv4ADLEOW5c-hZt_compress_L1',
    'video_id': '58e0b8ebe9521a4eb864d99a',
    'title': '点点点绘本   按一按变多，摸一摸变色、摇一摇会乱跑',
    'video_tag_list': '',
    'content': '【书名】:点点点绘本\n【作者】:埃尔维•杜莱\n【推荐理由】:这是一本按一下会变多、摸一摸会变色、摇一摇还会跑得到处的超有趣绘本。\n麻麻们通过简单的指令，让宝宝手指点一点，就会有好多色彩缤纷，大大小小的点点蹦出来！\n用文字太难表达出绘本的有趣啦，请看视频💗\n一起参与#视频绘本打卡[话题]#，记录下你和宝宝读过的有趣绘本吧!'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lid4OxSfWsP6Bbi_mJiS-Tlt830p_compress_L1',
    'video_id': '58e0d46e37cec91db757d4d5',
    'title': '神户牛肉一对一服务',
    'video_tag_list': '用视频记录美食',
    'content': '#肉食动物最爱的美食[话题]##用视频记录美食[话题]#\n吃货们看了这个视频是不是很饿呢？看着专业的👨\u200d🍳现场制作地道的神户牛肉，享受VIP待遇\n很推荐的一家～steak house坐落在神户的地标东方酒店17楼的牛排屋，是日本大众点评排名第二的吃神户牛肉的地方最近还是蛮🔥的，里面环境不错可以俯瞰神户港，里面很多日本的情侣约会吃饭，国人知道的并不多国内的大众点评上推荐的人不多，每一道菜都非常精致，看着厨师每做完一道端到我面前都会介绍一下如何吃更好，都是一对一的服务，服务非常周到'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/fdf079cd4350e33cd0e5f187a6ea0153695573db_r_ln',
    'video_id': '58e0d91f6960120db8d1f175',
    'title': '烤蟹黄',
    'video_tag_list': '京都不容错过的美食',
    'content': '#用视频记录美食[话题]##京都不容错过的美食[话题]#\n这个是在京都的蟹道乐（京都本店）吃的，也是我最喜欢的一道菜～烤蟹黄（鲜美无比😋）\n我觉得这个烤炉很像是我小时候家里用的煤球炉子～只不过这个是mini版的～[偷笑R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhY3Bx0W7WcLGNqNo2mdVNCeLY98_compress_L1',
    'video_id': '58e12746696012673fd1f165',
    'title': '京都车站Porta Dining 超暖胃的茶泡饭',
    'video_tag_list': '用视频记录美食;日本;京都',
    'content': '#用视频记录美食[话题]#\n连着n个小时没睡好+没怎么吃正经食物，一路赶路的疲惫被京都车站旁的一家茶泡饭店给治愈好了。这家店在Porda Dining下，人气很高，提供10种不同的茶泡饭，价格在700-1000yen不等。\n#物有所值的平价日料店[话题]##今天吃什么[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lv3awjWOR3iOzBvpQI0ZVxgjsD8n_compress_L1',
    'video_id': '58e12a50a9be5d471239fece',
    'title': '一个"尴尬"的卸妆视频',
    'video_tag_list': '卸妆测评',
    'content': '#卸妆测评[话题]##平价好用卸妆[话题]#\n#卸妆大挑战[话题]#响应 @鱼罐头_ 小姐姐的点名\n今天终于拍了一个卸妆视频了hhhh\n刚好因为湿又野粉底液到了试了一下就顺便拍了\n第一次录视频尴尬癌犯了😂😂有点手忙脚乱\n人丑声音难听就加快了时间 这样不用听我的原音hiahia\n用到的卸妆产品：\n💕曼丹眼唇卸妆液\n💕芭妮兰绿色卸妆膏\n💕丝塔芙洗面奶'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/c34506e7-832eb9e-8d9e-e3b8aba0ea63?sign=9abc688b317bd67b26e77fbc343a6754&t=65fb06d4',
    'video_id': '58e137623460941838a20e61',
    'title': '小长假别偷懒，只要30分钟，在家做的的高效全身HIIT燃脂训练！',
    'video_tag_list': '',
    'content': '小长假第一天你是怎么度过的？\n在家宅着补觉补美剧？\n和亲朋好友出游逛街吃大餐？\n还是加班狗干了一整天活累觉不再爱？\n发现没有，\n假期很容易打乱我们平时的生活习惯，\n比如早睡早起的作息，\n比如规律的健身，\n比如健康的饮食。\ngym关门成了我们偷懒最大的理由，\n身材好不好也不差这几天对么？\n但是三天养惰性，\n慵懒的假期之后你可能需要很久才能恢复之前健康的生活状态。\n所以咬咬牙，\n不需要任何器械工具和特殊场地，\n30分钟跟着Giselle一起做个HIIT训练刷刷脂，\n保证你做完之后全身舒爽，\n无负罪的去跟闺蜜下午茶吧！\n如果喜欢我们的内容，欢迎关注同名平台（细节看我们的介绍）Fit4Life健身与美食！\n#全身减脂教学视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhwIIHBIEaz4LITeuE31TXYFfsXl_compress_L1',
    'video_id': '58e2792bd2c8a507f6ff6957',
    'title': 'Morphe×Kathleenlights眼影盘眼妆视频',
    'video_tag_list': '新手最容易上手的眼影盘',
    'content': '自从入手这款眼影盘，家里其他的眼影盘都变成浮云~感觉都要打入冷宫~超爱这款眼影盘，显色度超棒！不管是珠光还是哑光色，画出来的眼妆都超美，别的不得了，先来看看吧~#新手最容易上手的眼影盘[话题]##平价好用的单色眼影[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liPQjfLuzigWjMWpfI4uwFACc1k1_compress_L1',
    'video_id': '58e2c2f17836236c454a6832',
    'title': '美食日常记录❤️',
    'video_tag_list': '视频记录下厨',
    'content': '平时做饭时候拍的一些[喜欢][喜欢][喜欢]\n番茄肥牛\n土豆饼\n糖醋黑线鳕haddock\n干锅花菜\n鸡蛋玉米煎饼\n甜椒酿肉\n海鲜豆腐汤\n糖油粑粑\n意式千层面\n#美食才是人生主角[话题]##用视频记录美食[话题]#\n#今天吃什么[话题]##视频记录下厨[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/01e2480ed522ad86010370037fefed94c3_259.mp4',
    'video_id': '58e3092ed1d3b9497e947e0e',
    'title': '清明时节必须品尝的一道美食——马兰头香干',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n马兰头又名马兰、螃蜞头草等，属菊科马兰属多年生草本植物。\n由于寒食节与清明节合二为一的关系，一些地方还保留着清明节吃冷食的习惯。\n★★★★★\n创意指数\n马兰头拌香干\n▼\n马兰头拌香干\n·食材·\n马兰头、香干、圣女果\n生抽、麻油、糖、盐\n1.香干过沸水\n2.切成条状\n3.再改刀切成末\n4.圣女果切瓣\n5.马兰头过水沥干\n6.切成末\n7.倒入生抽、麻油、盐、糖调味\n8.均匀搅拌\n9.倒入小碗中，用勺子压平\n10.圣女果点缀即可\n11.清明节吃一道明目养颜菜吧~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/22a7af339fa5d232c93f8fdaa0093213a2b79433_r_ln',
    'video_id': '58e4589ed1d3b939d8947e0d',
    'title': '银鱼炒蛋不腥气又美味的小诀窍！',
    'video_tag_list': '',
    'content': '#超级下饭的家常菜[话题]#\n★★★★★\n小圆食记\nMenu\n银鱼炒蛋是一道色香味俱全的传统名菜，属于江苏菜。\n银鱼的营养价值很高，营养学家普遍承认它是“长寿食品”，是“水中的软白金”。\n★★★★★\n创意指数\n银鱼炒蛋\n▼\n银鱼炒蛋\n·食材·\n银鱼、鸡蛋\n葱、姜、料酒、盐\n1.倒入清水泡发\n2.葱姜切末\n3.鸡蛋打匀\n4.倒入姜末、料酒拌匀\n5.倒入鸡蛋液再次拌匀\n6.|热油锅倒入鸡蛋液炒至成块\n7.倒入盐调味\n8.装盘撒上葱花\n9.健康营养的快手菜就完成啦~！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgYPrkRikw7dZRiA3_kpm_lH4hc2_compress_L1',
    'video_id': '58e5ab991d0ca301676ba416',
    'title': '教你做一道满屋飘香的——鱼香茄子煲',
    'video_tag_list': '',
    'content': '#超级下饭的家常菜[话题]#\n★★★★★\n小圆食记\nMenu\n茄子煲属于粤菜，其实来历深远，贾思勰《齐民要术》中有“ 缹茄子法”正是茄子煲的老祖宗。\n“缹 ”字一望即知乃是将瓦罐置于火上，意思大致相当于煨或者煲，茄子“用子未成者以竹刀骨刀四破之，汤炸去腥气。\n★★★★★\n创意指数\n鱼香茄子煲\n▼\n鱼香茄子煲\n·食材·\n茄子、肉末、洋葱\n米椒、葱、蒜、高汤\n豆瓣酱、老抽、陈醋\n糖、盐、淀粉\n1.茄子切段，再切条\n2.放入水中打湿，沥干备用\n3.蒜切末、米椒切丁、洋葱切丝备用\n4.筷子周边迅速冒泡油温合适\n5.倒入茄子炸软\n6.捞出茄子轻轻挤压，挤出多余的油份备用\n7.热油锅倒入蒜末、豆瓣酱炒香\n8.倒入肉末清炒\n9.肉末断生后加入老抽、盐、糖、陈醋\n10.清炒片刻放入米椒\n11.倒入高汤拔均\n12.倒入茄子清炒\n13.勾芡炒匀关火\n14.砂锅置于炉上，下洋葱丝\n15.大火将砂锅烧热，将茄子打入砂锅内\n16.撒上葱花即可享用~！'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/luIcLRBZInYPt-geTy1Sgq9DC6ro_compress_L1',
    'video_id': '58e5ba10a9be5d15d58cd89d',
    'title': '名副其实的云瀑❤️',
    'video_tag_list': '',
    'content': '一点小日常♪(´ε｀)'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmAhDNrDNMnfHEMOUCuUbzuo3f1K_compress_L1',
    'video_id': '58e5be1514de41586bc49924',
    'title': '360°全面解析小瓜子第一本布书绘本💕💕',
    'video_tag_list': '宝宝英文启蒙绘本',
    'content': '🍒小瓜子的第一本布书，来自美国品牌芝麻街，是让家人从美国带回的，所以价格不详。\n🍒不得不佩服老外在宝宝玩具上费劲了心思，效果确实不错呢，连我和老公都很喜欢翻一翻，哈哈\n🍒80后一定都不陌生芝麻街的故事，这本书的主角就是超级可爱的小怪兽宝宝Elmo，围绕他展开的bedtime story，讲述五颗天上的小星星来帮助Elmo入眠，帮他沐浴、穿睡衣、唱歌、找玩具等步骤，绘本读起来超级温馨，虽然小瓜子现在只有七个月大，我也很喜欢每天拿出来给他翻翻看看，讲讲小星星的故事，他会很开心的眨巴眨巴眼睛细细的聆听。\n🍒这本书最大的特点就是设置了很多小机关，比如给elmo盖的小毛毯，把玩具从小箱子中拿出来，给elmo穿睡衣，还有声响机关，响纸等，集合声音、色彩、故事情节于一体，锻炼婴幼儿手动、听力、视觉等各方面系统的能力。\n🍒脏了也不怕，水里洗一洗就好啦。\n🍒具体细节宝宝们查看视频哦~每一页都有详细分解呢～\n喜欢的宝宝请多鼓励多关注哟～\n爱泥萌～\n画外音：拍的时候小瓜子嗯嗯啊啊的在旁边抢书，哈哈哈哈，仔细听还是能听出来他的嚎叫哈哈哈\n#视频绘本打卡[话题]#\n#一起读绘本[话题]#\n#宝宝英文启蒙绘本[话题]#\n#这些布书撕不烂[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fqn2-CztHTVbdWeGhEEWHmdeC5l__compress_L1',
    'video_id': '58e5d37fd2c8a57420ea51ce',
    'title': '航拍处女作—卡萨布兰卡哈桑二世清真寺',
    'video_tag_list': '',
    'content': '在卡萨布兰卡的最后一天，用mavic pro航拍的哈桑二世清真寺，清晨的景色还是很美的，过几天如果有空给大家写摩洛哥攻略，有问题的可以在这条视频下面留言，我会在攻略里全部回答大家。😁'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmcKMBW9XppgdxsDi-MiJuFWJlHm_compress_L1',
    'video_id': '58e610091d0ca3385f6ba422',
    'title': '【视频】我爱用的防晒～想白就要认真防晒',
    'video_tag_list': '肌肤之钥 clé de Peau Beauté 亮彩莹润防晒霜SPF50 PA++++;怡丽丝尔 elixir 日间美白防晒美容乳液金色滋润型 SPF50+PA++++;黛珂 COSME DECORTE 高级能AG防晒霜SPF50+ PA++++\xa0;碧丽妃;春季防晒必备',
    'content': 'Hi大家好，之前有小伙伴想让我分享爱用防晒，今天就以视频的方式给大家分享一下👏🏻👏🏻👏🏻👏🏻\n👉🏻我是大干皮哦\n👉🏻\n👉🏻\n👉🏻\n👉🏻防晒\n#春季防晒必备[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/58514ed1-0c0a25e-b1b1-36913f820a7b?sign=46a7ca31dbc90b93d909f71c4e59c0ca&t=65fb06d4',
    'video_id': '58e6160a3460946b62a858bb',
    'title': '新买的皮鞋穿几天就脏了怎么办？涂一点这个，让皮鞋焕然一新',
    'video_tag_list': '',
    'content': '家里买了新皮鞋、新皮具，长期使用后渐渐发现光泽和颜色会慢慢淡去，也许还会出现难看的擦痕。今天喵招教大家如何保养皮革，让你的皮具重新焕发光彩！性价比很高哟~\nPS：妹子们穿的JK鞋如果发现太硬了容易磨脚后跟，有可能是鞋子油脂散失、过于干燥引起的发硬，可以用这个方法养护，连续涂抹凡士林然后放置几天，这样鞋子会变得柔软些，而且会光亮很多哟。#生活妙招\n#视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/de0e4d9c-0d8847e-83e7-04bc625078ae?sign=cb44471d59b6e369428440538b9a6265&t=65fb06d4',
    'video_id': '58e63a927fc5b81a9ab4b76d',
    'title': '健身神补剂｜好喝低卡的香蕉莓子蛋白粉奶昔',
    'video_tag_list': '',
    'content': '蛋白粉是健身届运动补剂中扛把子，但是女生该不该吃蛋白粉，怎么吃，什么时候吃？本期视频我们来为你解惑！\n如果喜欢我们的内容，请关注全平台同名 Fit4Life健身与美食\n什么是蛋白质\n女生减肥，大家都知道控制碳水和脂肪的摄取，可是最最重要的事，却被很多人忽略了，那就是蛋白质的摄取。\n蛋白质由氨基酸组成，是合成人体一切细胞、组织的重要成分。换句话说，如果身体是一栋房子，蛋白质就是砖。\n人体进行的所有生命活动，都需要蛋白质的参与；尤其是人体组织的生长与修复。尤其对于女生来讲，如果你想要紧致的肌肉，光滑有弹性的皮肤和健康的头发和指甲，那就需要每天摄入足够的蛋白质。\n你每天吃够蛋白质了吗\n蛋白质虽然重要，但是吃得太多，太少都不行。官方文献显示，人体每天应该摄取1-2g/公斤体重的蛋白质。对于我俩这样的健身狂人来讲，我们每天大概要吃100-150g的蛋白质才能维持旺盛的新陈代谢水平以及肌肉生长的需要。这就相当于20多个鸡蛋，或者一斤鸡胸肉。\n如果每天吃20多个煮蛋白或者一斤烤鸡胸，可能整个人都会疯掉；海鲜神马的成本太高毕竟不能天天吃，但是如果靠红烧肉或者炸鸡来补充蛋白质，又可能会先撑成一个胖子。所以，蛋白粉就便成了高效方便的蛋白质补充剂，而且超级美味！（尤其如果你是甜食控）\n蛋白粉怎么吃\n我们最最喜欢的做法，就是蛋白粉smoothie了。初夏时节，运动过后喝一大杯解渴解馋零负担的smoothie，感觉冰淇淋不再是真爱，立马变身元气美少女！（制作方法请见视频）\n小总结\n蛋白质的合理摄入，对于减脂或是增肌的我们，尤其是女生，是至关重要的。蛋白质不能少吃，但是也不要多吃。因为蛋白质无法像碳水和脂肪一样在身体里进行储存，摄入太多，一是会造成热量负担被存储成脂肪，二是会增加肾脏的代谢负担。所以科学合理的计算是至关重要的！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvMblNIPJhaya7ON_xLQ6W99VvX6_compress_L1',
    'video_id': '58e6fd3dd2c8a54a8edee5a0',
    'title': '菠菜这样做下酒开胃，又不失营养',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n春天的尾巴！眼看夏天就来了，过完了节该清理肠胃了，吃清爽的菜肴吧。菠菜是最普通的时令蔬菜，娇嫩的小菠菜口感清甜特别清爽，凉拌着吃又别有一番好滋味呢。\n★★★★★\n创意指数\n香辣菠菜\n▼\n香辣菠菜\n·食材·\n菠菜、花生、辣椒干\n蒜、生抽、香醋、白糖、盐\n1.菠菜过沸水\n2.捞起后冷水浸泡\n3.沥干备用\n4.切蒜末\n5.倒入辣椒干、蒜末\n6.烧热油，淋上拌匀\n7.倒入花生拌匀\n8.倒入生抽、香醋、盐、糖调味\n9.均匀搅拌\n10.酱料淋在菠菜上\n11.这样的菠菜又开胃又不失营养~'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/854x480/vcodec/libx264/pgc/f3119998-bcf5fec-af7d-45914d0b6830?sign=82e0f00fb1ad6cef69158f94092e97a8&t=65fb06d4',
    'video_id': '58e73d6e34609415a523df5d',
    'title': '小个子女生必看：身高158 春季穿搭 |  Zara | 优衣库 | Topshop | Other Stories | San',
    'video_tag_list': '小个子显高穿搭',
    'content': '今天给大家分享我春季的新衣试穿，作为一个小短腿，显腿长是我对衣服的最大诉求，希望能帮助到和我一样的小仙女~\n以下是按照视频介绍顺序的产品名称：\n*品牌 Zara*\n很雷的黄上衣：\nTOP WITH BOW AT THE BACK\n白裙裤：\nFLOWING FRILLED SHORTS #white\n*品牌 Sandro 现在75折快去看！*\n浅蓝上衣：\nCOTTON TOP WITH WAVE CUT-OUTS\n深蓝短裙：\nELASTICATED KNIT SKIRT NAVY BLUE\n粉色连衣裙：\nHONEYCOMB FABRIC SLEEVELESS DRESS\n*品牌 优衣库*\n白T\nWOMEN U CREW NECK SHORT SLEEVE T-SHIRT\n*品牌 & other stories*\n大雷的长裙：\nPleated Skirt\n肉粉色衬衫：\nWide Cuff Silk Shirt\n*品牌 Topshop*\n牛仔裤：\nPETITE Jamie Jeans\n同款颜色有一点点不一样\n#每日穿搭#春天甜美风#衣橱穿搭日记#基本款穿出时尚感#平价好穿牛仔裤#小个子显高穿搭#160cm女生穿搭'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/51fb0015-80fff03-9405-08970f09db85?sign=b1ee13cead593c7c06eb5706ab3c2ff4&t=65fb06d4',
    'video_id': '58e75223346094136423df5b',
    'title': '【手把手教你如何画眉 - 跟无眉星人说拜拜😉】',
    'video_tag_list': '适合新手的眉笔;Anastasia',
    'content': '之前的化妆视频里有好多小伙伴都留言说希望我能出一期画眉教程的视频，here we go！\n眉毛在一个妆容中是灰常灰常重要滴，不仅可以使脸型更立体，更能凸显出五官的精致。想想看一个妆容哪里都画好了就是没有眉毛该有多吓人😨\n不过不用担心，看了今天的视频相信大家就可以学会啦！\n⬇️完整步骤：\n1️⃣了解自己的脸型\n2️⃣根据自己的脸型修眉，定下来一个基本的形状\n3️⃣画眉：眉笔+眉刷就ok，如果很讲究还可以在画好后用染眉膏，不过我比较懒所以这一步就省略啦！\n选用的眉笔是我的最爱：Anastasia Beverly Hills Brow Wiz，色号是Medium Brown，我的Ride or Die，已经说过无数次了！好用好用好用，没有缺点！新手老手都适合！\n两头：一头是笔芯，够细所以可以很精准的画出眉毛的轮廓和形状，软硬度和显色度也很适中，不会画成蜡笔小新✌️一头是眉刷，画完后扫一扫使眉毛深浅过度自然并且和整个妆面更好的融合在一起。\n以上，一个眉妆就完成啦！\n你学会了嘛？😘\n#日常妆容打卡[话题]##眼妆每日打卡[话题]##适合新手的眉笔[话题]##五分钟妆容挑战[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FhBf6xU39RCfA95LQxBvwW1DONgA_compress_L1',
    'video_id': '58e79048d2c8a53608658ca1',
    'title': '蛋壳球baby四维视频',
    'video_tag_list': '',
    'content': '孕23w+2做的四维，做四维的时候，竟然在摸屁屁，摸完屁屁又摸自己的头[叹气R]另一只手还塞在嘴里吃，好不卫生啊[笑哭R]\n我们的蛋壳球宝宝四维视频长得像爸爸，高高大大的鼻梁、大嘴巴、小脸蛋，根本就不像我，好难过[扶墙R]不过，我只希望他的眼睛像我就好了，健健康康出生。\n好多人都说看视频像个男宝宝，现在都35w+4了，照了3次B超，托熟人看都还看不到男女[笑哭R]我已经放弃了，等生出来就知道啦，给我们一个惊喜[得意R]女孩子就可以一起跟我买裙子，买护肤品，买口红……买买买，男孩子就可以跟我老公一起保护我[飞吻R]\n我没有约到第一医院，妇儿医院和明州医院，就花了580元在宁波爱博尔妇产科医院做了四维，因为有baby四维光盘送，觉得很有纪念价值，拿回家后自己用爱剪辑软件在电脑上合成了一个视频，配上了背景音乐🎵虫儿飞。baby以后看了会觉得很神奇吧[吧唧R]\n说一说四维和三维：\n三维和四维算是孕中期步入孕晚期前的一次“大排畸”检查，比较重要，近年来开始普及，可以较清楚地看到baby生长发育情况，估算baby的胎龄、体重，检查baby心脏、四肢是否健全等等，检查胎儿是否存在生理缺陷等情况。\n为了以防做四维三维的时候baby不动或睡着了等情况出现，建议孕妈妈提前做好胎教，避免需要二次做四维三维的情况出现。可以提前告诉baby要去做四维三维啦，让他/她知道，虽然他不一定听得懂，但是我感觉提前做胎教还是有一定用处的。另外，在做四维三维之前多走动，站立，不要一直坐在椅子上，baby容易睡着。准备点食物以防四维一次不通过饿肚子。\n更详细版的孕期40w检查请见我之前发布的孕期检查笔记📒里面有很详细的说明。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpA4JK2LZoIMcxRuR4dgqLMS3BsL_compress_L1',
    'video_id': '58e799b6d5945f5fec1d39dd',
    'title': '21天减脂训练营：体验Day1🏃',
    'video_tag_list': '',
    'content': '受小伙伴怂恿昨晚下班去体验了一次由国家健美比赛教练、评委-纪凯莉老师 创办的“21天减脂训练营”。\n朋友圈已发出去视频大家都在鄙视我说不能再减脂啦，由此声明我只是替周围需要减脂的宝宝们去体验训练营效果哒。我深刻的意识到自己现在练有氧掉的基本大部分是肌肉。\n工作室性质，强度较大，10个人一个小课堂但是教练助教一共有6个，每个人动作都会被纠正、被鼓励坚持下来、和稍稍挑战自我。\n习惯了单打独斗的我，没想到竟然还可以融入进来，蛮有意思的，我嘴里一直在叫“太坑了，弃坑别人去”😄\n训练内容：⬇️\n1⃣️折返跑+教练发出口令-听口令burpee\n2⃣️药球burpee 35秒\n3⃣️弹力绳小跑 如我视频中所示，但是绑在固定物体上\n4⃣️Vipr 我最爱的 器材\n5⃣️快速跳软体\n6⃣️战斗绳\n2-6动作循环3组 每个动作35 seconds\n然后再来升级版：增加外力或两人互动\n1⃣️burpee 举起药球再使劲砸地\n2⃣️两人对拉弹力绳，如视频\n3⃣️快速爬软体\n4⃣️vipr互撞再倒退到原位\n5⃣️战斗绳大幅度加强版\n循环3组 每组35秒。\n外带心率带监控心率😜\n给减脂的朋友借鉴，不过团队氛围会很不一样哈哈。我还有两次体验机会下次再看看还有什么可以学习💗'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljXNmS4nugAKHpWiyVj-bNuuV9-c_compress_L1',
    'video_id': '58e86e0afaa05220cfe93468',
    'title': '超美大波浪卷发视频教程',
    'video_tag_list': '撩头发也要美',
    'content': '良心制作的卷发教程，卷出超美超蓬松超详细的大波浪发型\n心血来潮的想做这个卷发的视频，可能是天气变暖了我也开始躁动起来了哈哈哈\n这个视频里有文字也有配上我的解说，但是呢还是给大家总结一下步骤\nstep1 ：将头发分区，上半部分外侧的头发梳起来，先卷下半部分内侧的头发\nStep2 ：所有下半部分内侧的头发，需要⭐️🔝用内扣、向内侧旋转⭐️卷发，卷好后停留20秒。\nStep3 ：卷好下半部分的头发后放在脖子一侧，将梳起来的头发松绑放在脖子的另一侧（这样分开区域就不会那么乱）\nStep4 ：这一次这些刚刚梳起来的上部分的头发，要用向⭐️外侧旋转⭐️的方式卷发，停留20秒。\nStep5 ：全部卷好后用梳子梳开，抓一抓美一美就完成啦\n⚠️全程注意⚠️ 卷发棒很烫，一定要小心不要烫到手。\n#撩头发也要美[话题]##卷发[话题]##新发型[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lswXoyLAXm2CKsiFJ2m4BbMUowH6_compress_L1',
    'video_id': '58e8d1ada9be5d65c8a045db',
    'title': '2017上海秋冬时装周',
    'video_tag_list': '',
    'content': '#上海时装周[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lpFgb9MfPbp_O1pFFLinWVeYTZ7E_compress_L1',
    'video_id': '58e9126e783623632b4464a8',
    'title': '可以发视频了？——农村女英语教师下课后发神经了',
    'video_tag_list': '',
    'content': '对对对\n属于发神经时间段'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luAaCs9s_PR-rsREnHE2xfOeh8L1',
    'video_id': '58e9b1b0e9521a5cca601b6c',
    'title': '农村英语教师之——包里都有啥',
    'video_tag_list': '汤姆·福特;古驰;芬迪;J Brand;黄金鹅;江诗丹顿;尚美巴黎',
    'content': '\n\n这是去年5月份拍的一个视频\n哈哈哈哈哈哈哈\nmuahhhhs\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llWbX6BljkwjxGhdm_TqNLFMYpes_compress_L1',
    'video_id': '58e9d3e1a9be5d2846a045df',
    'title': '#上海时装周#设计师推荐，太好看，开秋买什么看过来',
    'video_tag_list': '上海时装周',
    'content': '#上海时装周[话题]#ing，下雨天赶个show😔\n看到好看的衣服忍不住来给你们分享…\n品牌vacae，第一次了解她的作品…\n真好好看，大气，超级适合我！\n开秋还是流行茱萸粉呀，然后显白的气质红色，还有特殊面料处理或者荷叶边设计的黑色款😛\n看到更多赞的设计师再跟你们分享哦😛'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgaNejtPApQf9Z4_eQYY2pv2AgYM_compress_L1',
    'video_id': '58e9e133fb68a26e84f61902',
    'title': '大阪米其林一星 北村寿喜烧',
    'video_tag_list': '米其林探店报告',
    'content': '关西暴走之旅就用一顿寿喜烧来做ending吧[少女心]\n#用视频记录美食[话题]##米其林探店报告[话题]##米其林日料店[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrZVKtRXH-2JK5ISxn1iGSiYRaff_compress_L1',
    'video_id': '58ea0504faa0526f8c1151a6',
    'title': '上海下雨天的早餐？来SUMERIAN来杯小蘑菇的咖啡',
    'video_tag_list': '用咖啡saymorning',
    'content': '#早餐喝什么[话题]#上海陕西北路上的SUMERIAN，在light&salt隔壁，有着硕大的贝果和超可爱的咖啡师小蘑菇.\n可爱的小蘑菇拉花超厉害，性格也可爱，喜欢坐在咖啡师前的吧台边聊天边试她的新咖啡. 今天试了试Konga Ice, 埃塞Konga的冰咖啡，从啤酒管道口打出，特别的发酵味，爱酒和咖啡因的同学们一定要试试.\n☕️推荐拿铁控试一下黑糖奶油拿铁、南瓜拿铁\n感觉夏天里会常来[喜欢]\n#用咖啡saymorning[话题]##用视频记录美食[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljMgPWlO5E9Gd2MQmRV3pGqGXXxV_compress_L1',
    'video_id': '58ea0f0e14de4131f926d228',
    'title': '【Adora干货】修容粉饼手法小技巧',
    'video_tag_list': '娇兰 Guerlain 提洛可修容粉饼;Physicians Formula 摩洛哥系列超滋养坚果油修容粉饼;Physicians Formula 阿甘油超滋养柔滑粉饼;Physicians Formula 四季修容粉饼;BECCA Shadow & Light Bronze/Contour Perfector™  双色修容粉;如何修容可以让脸变小',
    'content': '有人问我修容粉饼也就是暗影该怎么用。[活力]很多博主都po过暗影高光脸上使用位置的图片。那么我就来说说大家没说的，但是的确起到关键作用的内容。就是修容粉饼使用手法👋！#如何修容可以让脸变小[话题]# @美妆薯\n讲真，就算花了银子💰买了各种修容粉饼、修容盘，但是一上手发现根本化不来人家图片效果有木有[害怕]\n那一定是没人告诉你，怎么用刷子刷、怎么个方向刷、怎么个范围刷、怎么个速度刷………\n这些就是上妆后修容效果的决定性因素啦！\nAdora温馨提示：所有的脸部行为（指粉状产品的上妆）建议都要小幅度、快速滴晕染。不要汉子一般的重手一笔下手[害怕][害怕][害怕]化妆是一蹴而就不来的。\n刷刷刷！轻、细、入微滴让妆容晕染在肌肤上，当然所有美妆都是粉质、颗粒等和皮肤融合的一个过程，过程中恰如其分的细腻是让肌肤和妆品完美碰触的过程。如果我们把自己当作一张脸（对！发挥一下想象），你是喜欢轻柔舒适滴粉刷将粉按摩在脸上呢还是暴力滴刷刷两笔一坨又厚重的甩在脸上的感觉好呢[害羞R]\n细腻的妆容会有别样的感染力，往往那些很强大妆感的化妆技术都是由入微的每个细节而来的。希望仙女们都能成为将爱和美的意念融入每个上妆过程的达人，享受美妆的体验。[飞吻R]\n最后分享我喜欢用的修容粉饼宝宝们\n\n\n\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loVXqxxJaGMavJVDo3FBQSiEQzAR_compress_L1',
    'video_id': '58ea1fecf138213044bdd01e',
    'title': '视频｜这里有一些平凡又闪亮的故事，说不定也包括你的在内',
    'video_tag_list': '小红薯档案馆;小红薯档案馆',
    'content': '明天又是周一啦，面对又要展开的新的（有本队长陪伴）一周，你是期待？还是期待？还是期待？\n今天，本队长难得走个心灵路线（🙄️）主要是为了给大家介绍一位薯家族新成员——@小红薯档案馆\n这是一个专门收集就像你这样的小红薯最真实的个人故事的地方。\n档案馆薯馆长上线#小红薯档案馆[话题]#故事征集也已经两周了，这些日子里，他们三个🍠，一辆🚗，跑遍全中国，只为来到你身边，听你亲口说说自己和小红书的故事。\n故事的第一站 —— 上海。\n@💋superwoman💋🌻⚽️4⃣️  ，一个无论再苦再累都懂得好好爱自己的女足运动员。\n@suki是只小兔几🐰，拥有着一个会从小红书中给她寻找惊喜的真爱未婚夫。\n@徐oo，一个毫不闭塞，不断完善自己，给孩子更好生活的辣妈。\n#小红薯档案馆[话题]#里收集的都不是什么酷炫拽炸天的惊人事迹。\n而是每一只小红薯不断学习更爱自己也更爱生活的真实经历。\n本队长希望也相信，一定还有更多更多的小薯，也有自己的独家心得——关于如何欢快地把每一个平凡的日子都过得无比闪亮。\n喜欢听故事、或者同样想分享自己故事的小薯，可以戳进@小红薯档案馆，还有更多精彩等着你。\n最后，我想说，虽然 @小红薯档案馆 的馆长可能不同意，但是本队长也是默默地把这一整个故事收集和分享，看成是一次全中国小红薯❤️花式表白薯队长❤️的，活动。\n你们说：我理解的对吗？？'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/9f9e7a19-d0da001-b24b-59808d441853?sign=cbdc91c8ba33ba11c8a1a5ba672f771e&t=65fb06d4',
    'video_id': '58ea22fa34609406df80a4a7',
    'title': '教你一招超省钱！自制个性化妆包，好看到不愿离手！',
    'video_tag_list': '',
    'content': '刚吃完的糖果包装太可爱不舍得丢弃怎么办？不如继续发挥他们的卖萌值，做一个环保简单的收纳袋吧！\n随身携带、方便收纳，重点是还可以自己随心所欲选择款式，再也不用纠结收纳和颜值不兼顾的问题啦~#DIY #生活妙招 #化妆包'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/887b8949dca507e14f68f157311687044756f113_v1_ln',
    'video_id': '58ea239f3460943f4f2baffe',
    'title': '一顿丰盛的早餐一定离不开鸡蛋，教你做超快手微波炉水波蛋',
    'video_tag_list': '节后瘦身必吃TA',
    'content': '教你做微波炉水波蛋|水波蛋到底有多少种做法呢？这次喵招创新了一种用微波炉就能轻而易举地做出完美水波蛋的做法哟~不用担心做出来的水波蛋不完整或是破裂。非常适合厨房新手来使用哟~#美食 #美食妙招 #生活妙招#节后瘦身必吃TA[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/da4b1f8c63f2c4ba60c46dafb217a7cd3cdbaa47_r',
    'video_id': '58ea28cfa9be5d482478ecac',
    'title': 'No她No玩！王阿姨出游必备双肩包！',
    'video_tag_list': 'MCM;适合出游的双肩包',
    'content': '#高颜值双肩包[话题]##适合出游的双肩包[话题]##高颜值出游包[话题]##出游穿搭小贴士[话题]#\n欢欣鼓舞第一次参加穿搭薯话题，特意做了一个可爱的小视频给大家全方位介绍这款王阿姨的出游必备双肩包，希望宝宝们能看的更清楚哦[喜欢][喜欢][喜欢][喜欢]\n【MCM Stark Mini-米色】\n[装酷]这款包包王阿姨已经背了快三年，虽然不像Eason唱的“背了六年半”，但的确是“背到现在还没烂”[得意]，质量真的敲好！\n[少女心]王阿姨身高164，出游从不穿高跟鞋，只穿平底鞋，穿着style也比较休闲运动风，这款mini MCM包特别实用也非常上镜哦。\n[得意]别看我叫Mini，但容量可真不少哟！出游基本携带的东西统统可以装下，王阿姨平常出游还喜欢带着一大包抽式纸巾以防万一（没办法，谁让俺是巨蟹座♋️呢），某问题的啦，妥妥的都塞进去！😁😁而且双肩包出游好不容易被偷东西，因为可以随时根据人流情况，把包包正背到胸前的呀！[讨厌]\n💓百搭米色，深浅衣服都可和谐共处，王阿姨平常穿衣黑白灰居多，搭配起来毫无压力。✌️\n[哭哭]唯一缺点：太贵。而且越来越贵。三年前，王阿姨这款在韩国VIP购买3200块，现在估计至少3500了，喜欢的宝宝们，剁手要趁早啊！\n⚠️两点注意：\n1）MCM包包几年前比较流行，双肩包属于烂大街款式，但最近几年火热度不如以前，不太适合追赶时髦的宝宝哦！\n2）MCM双肩包的尺寸繁多，一定要根据自己的身高选择合适的尺码哈。\n[装酷]欢迎喜欢CallMe王阿姨的宝宝们各种点赞，收藏和关注，你们的鼓励是我最大的动力哦[少女心]\n-------------------------------by CallMe王阿姨\n------------------照片取景自美国奥兰多&迪士尼\n-----------视频取景自“美国威尼斯”罗德岱堡海滩\n----------------------第一次做视频感觉羞羞的[委屈]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgGKq-tF5pFq_tNv4UjCt-qggxz8_compress_L1',
    'video_id': '58eaf1166960125c0715a69b',
    'title': '这样做的“手撕包菜”麻辣鲜香，超级下饭',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n手撕包菜是一道色香味俱全的汉族名菜，属于湘菜系。此菜红白相间，麻辣鲜香，爽脆清甜，可开胃增食欲。\n★★★★★\n创意指数\n手撕包菜\n▼\n手撕包菜\n·食材·\n包菜、五花肉片、辣椒干\n蒸鱼豉油、蚝油、花椒、盐\n1.包菜切半\n2.再改刀切四段\n3.用手撕成小块\n4.热油锅倒入五花肉片\n5.肉片炒散后倒入花椒、干辣椒\n6.加入清水\n7.水煮干后，炒出麻辣的香气\n8.炒香后倒入包菜翻炒均匀\n9.包菜变软，加入适量的盐、蚝油、蒸鱼豉油\n10.大火翻炒至7分钟熟，即可关火出锅\n11.麻辣鲜香，快给我来2大碗米饭~！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/llZZBPoLfPc7XXCl-WudlaInzvif?sign=f5c08849ceed5d0e7bb4b18a4132a6c5&t=65fb06d4',
    'video_id': '58eb2029696012073a33395c',
    'title': '我在减肥了——这是running man challenge',
    'video_tag_list': '',
    'content': '你们不要说了\n我在减肥了\n真的\n拼了\n[扶墙R][扶墙R][扶墙R][扶墙R][扶墙R]\n跟这个视频没关系\n这是去年5月的\n[扶墙R][扶墙R][扶墙R][扶墙R][扶墙R][扶墙R][扶墙R]\n你们跳跳看\n我累死了\n哈哈哈哈哈哈哈\n最后\n我很认真\n我在减肥'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FhhXOJfmb1zTPFQDjtooM__A2Y3i',
    'video_id': '58eb24bd14de41272a440f97',
    'title': '全部都是ggdb小脏鞋小脏鞋——最后一点存货',
    'video_tag_list': '黄金鹅',
    'content': '\n我很认真\n我在减肥中'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/5d6d7523d4955099edbb7490877ac4767dc950ce_v1_ln',
    'video_id': '58eb273db46c5d17ef38c261',
    'title': '赤脚拍的～从不P腿，傲娇脸，哈哈哈哈',
    'video_tag_list': '这么穿显腿长',
    'content': '可以发视频咯～#这么穿显腿长[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/fa729325782e44bb7ad1f577ead9f2ba18b40370_r',
    'video_id': '58eb2f803460943cbc80a4a6',
    'title': '【拿YSL方管214 教你画一个春日元气玫瑰妆容😉】',
    'video_tag_list': '圣罗兰 Saint Laurent ROUGE PUR COUTURE THE MATS 方管口红/唇膏;玫珂菲;芭比波朗;Anastasia;纳斯;植村秀 shu uemura 如胶似漆眼线笔;圣罗兰;魅可;单眼皮如何画眼妆',
    'content': '这支化妆教程视频的灵感来自YSL的方管214，最火豆沙色唇膏之一。\n本来打算和小伙伴出去逛街，因为天气hin好，穿的衣服颜色也比较清爽，所以挑口红的时候就选了豆沙色，画的妆容当然也要应景啦😉\n这个妆容qiao简单，因为想突出自然的玫瑰、裸妆、温柔妆感，所以没有打高光也没有用散粉定妆，眼影色调是偏裸的大地色，☝️但也有亮点哦，我在这个妆容里画了比较明显的卧蚕，更加突出了双眼的明亮和女性的温柔感~\n⬇️Products used/用到的产品：\nSmoothing Primer/毛孔隐形妆前乳\nSkin Foundation Stick/粉妆条，色号0.75 Ivory\nBrow Pencil/眉笔，色号Dark Brown\nLaguna修容粉\nToo Faced Chocolate Bar眼影盘：White Chocolate， Salted Caramel，Semi-Sweet， Marzipan，Champagne Truffle\n\nClinique/倩碧小雏菊腮红，色号13 Rosy Pop\n方管哑光唇膏214\n⬇️Makeup Brushes/刷具：\nBobbi Brown魔术底妆刷\n129腮红刷，224，217眼影刷\nSigma E55眼影刷\nSigma F05修容刷\n.\n以上，希望你们喜欢😘\n#日常妆容打卡[话题]##眼妆每日打卡[话题]##单眼皮如何画眼妆[话题]##入门级彩妆[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkYxsc_ozUPvTdkF1_vpvTx22i90_compress_L1',
    'video_id': '58eb3faca9be5d7cfb9f31ff',
    'title': '5分钟快手约会妆',
    'video_tag_list': '',
    'content': '平时一副网瘾少女的模样，突然有了约怎么样在最短的时间里妆扮好出门呢？\n产品清单：\n美宝莲遮瑕\nl.a.girl 高清粉底液\n植村秀眉笔\nrcma散粉\nbbia眼线笔\nstila眼影腮红盘\nnars腮红盘\n恋爱魔镜睫毛膏\nkiko双头唇釉\n#妆前妆后大对比[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luh7LHFuDgYmW3PG8_p4daIIP8Eb_compress_L1',
    'video_id': '58eb4f04b46c5d20c697a0d3',
    'title': '#试试视频笔记#已经回到国内啦，缓两天开始认真写游记',
    'video_tag_list': '巴厘岛阿雅娜水疗度假酒店',
    'content': '回来发现有视频权限啦[萌萌哒R]感谢可爱的薯队长[害羞R]\n昨天凌晨转机 延误到三点才起飞，今天已经回到祖国的怀抱啦[吧唧R]\n歇两天开始整理照片，准备写完整的游记和攻略分享给大家[害羞R]\n先上一段岩石酒吧rock bar的小视频试试功能啦[吧唧R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lv730VCV8rAYgRdqNEiUcs5di5t3_compress_L1',
    'video_id': '58eb6fa41d0ca31eba5e5738',
    'title': 'Vespet猫爬架',
    'video_tag_list': '我和宠物的日常;宠物名人',
    'content': '推荐视频里的猫爬架啦，炒鸡实用，比cats实用好多好多，垫子可以换洗，质量很结实，猫猫可以磨爪，也可以在圆圈里面睡觉觉，主要是不会闲置😂😂，而且呢，价格优惠很多，一千三百多元，比国外便宜好多好多#我和宠物的日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luv6xD7BO-GLwkiG-KeSG7AsMXUP_compress_L1',
    'video_id': '58eb731978362330d6331b3b',
    'title': 'Cats猫小Z大跳台',
    'video_tag_list': '我和宠物的日常;宠物名人',
    'content': '优点：质量很好，做工很好，材质也不错，曲木系列，没有味道，猫咪会跳上去玩，磨爪\n缺点：不太实用，拍拍照很好，猫咪是不会在上面睡觉的，价格贵，要上墙，不用了墙上会有孔孔，家里墙面装修很贵的童鞋要慎重考虑！\n另外一个小消息：商品页面介绍里面有20元的优惠券，买一个都有，买的多要分开买，我买了三个，分三笔，优惠了60元哦！#我和宠物的日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/568x320/vcodec/libx264/pgc/0a0350e8-322ceb4-ba70-e3a3964bbb6d?sign=cc92abef3b9241f58253ec7a2d2570cc&t=65fb06d4',
    'video_id': '58eb747534609441aa6b33fe',
    'title': 'Yvonne视频日记-北海道滑雪之旅',
    'video_tag_list': '北海道;北海道滑雪酒店首选',
    'content': ' #北海道滑雪酒店首选[话题]# #用视频记录美食[话题]#\n昨晚说好的北海道滑雪之旅视频来啦！\n这里还有位神秘嘉宾出场哦~\n跟着我们一起体验北海道酒店，一起逛街，\n去滑雪场，还有热腾腾的日式火锅！\n还有分享给你们买的各种雪具，和北海道小物，特产~\n如果你还没有看到昨天的北海道滑雪笔记，\n在这里给你一个福利小总结\n--------------------------------------------------------\n推荐酒店：\n1.\tAya Niseko 新雪谷绫公寓式酒店\n出门直接上山，超级便捷\n有公共温泉，也可以预约私人温泉哦\n2.\tSuiboku Niseko 水墨服务式公寓\n风景极美！共5曾，顶层两件是复式\n推荐购物：\n1.\tI-Gate\n可以买到两个很适合女生的雪服品牌哦\n一个是Perfect Moment，颜色很美\n另一个是Phenix，超级修身~\n2.\tMuse\n内有多家精品、品牌雪具店，\n还有超有feel的咖啡厅！\n--------------------------------------------------------\n好啦，如果你想看更多酒店和购物的细节+图片，\n可以去点击上一篇哦\n希望看了视频，你也感受到了北海道风情~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrGCqeCMM3a5-3BN6kEWmxJJrtqY_compress_L1',
    'video_id': '58eb7aa578362349b2331b3b',
    'title': '',
    'video_tag_list': '直男测试',
    'content': '直男测试直逼100分 💯\n女票说这个太屌丝 像快手的风格\n可我还是想发 [哭惹R]\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lixfY0EZzQnQl0m__O8RqnQdtvTX_compress_L1',
    'video_id': '58eb8e68d2c8a52a7f088158',
    'title': '日系淡妆，打造清透好皮肤的森绘梨佳仿妆，很适合小白新手',
    'video_tag_list': '妆前妆后大对比',
    'content': '这个日常妆很好上手，特别适合新手。妆容重点就是有妆似无妆，粉底用的是雅诗兰黛白金级粉底液，清薄妆感弱，像本身的好肌肤那样自然。\n第一次拍化妆视频，纠结很久终于是拍了，我总觉得自己不上镜，呕像包袱太深~\n如果你们觉得配音声音有点怪那是因为我感冒了（我是不会承认我平时声音也不咋地~）\n早就料到化妆时候会出现各种BUG，特地选了个没有任何技术难度的淡妆来画，但是还是出了些小状况 ~这次画的仿妆挑的是我很喜欢的日杂麻豆，因为她的妆很淡，这次拍的也没有明显的眉形和眼线之类的可以发挥，所以拍完之后真的是浑身哪里都不像，大家不要过分纠结像不像本人，主要仿的是妆容~\n小红书上只能插5分钟的视频，所以这个不是完整版的，切掉了一些内容（硬是把十几分钟的剪剪剪剪得我好忧伤），但并不影响观看的~\n#妆前妆后大对比[话题]##我最爱的彩妆品牌[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmToIGZRZUINMOLAU8somgF7NGbc_compress_L1',
    'video_id': '58eb91bd14de4136940ab788',
    'title': '嗲猫曼森森',
    'video_tag_list': '我和宠物的日常',
    'content': '发一个小视频，回应一下朋友为啥养猫不养狗，哈哈！\n赖皮猫，困了就找我😂😂#我和宠物的日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsX_QsjcaDbmIwCLImejum6TnvKn_compress_L1',
    'video_id': '58eba62802f37d4136df561f',
    'title': '看似玉米？无比美味的冰激淋甜点',
    'video_tag_list': '首尔;视频打卡好玩的冰淇淋',
    'content': '好喜欢这个话题#我爱高颜值冰淇淋[话题]##用视频记录美食[话题]##视频打卡好玩的冰淇淋[话题]#，手机里的视频多为美食[喜欢]，让我慢慢分享舌尖上的小红书.\n这道corn icecream玉米冰激淋是米其林Jungsik的一道甜点料理. 用玉米须、玉米调味和玉米做出的充满玉米牛奶味的冰激淋. 真是可爱动人的创意，吃起来超有幸福感.\n上海的大家都最爱哪里的冰激淋呢？'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lo7LU7Tv4hbB4ihXliWwg6_pmMuR_compress_L1',
    'video_id': '58ebbe9d14de415d0c16cf86',
    'title': 'CL满钻鞋➕Astley Clarke首饰们',
    'video_tag_list': '克里斯提·鲁布托;少女心手链',
    'content': '前面的几篇都有介绍哈\n晚安[飞吻R]\n银钻\n#少女心手链[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvfcH4uPh0M2hq9moHLUvyNzzX4o_compress_L1',
    'video_id': '58ebcb19d5945f2c00cf37e5',
    'title': '🥓🥞🍤🍗🥘🥗🍣🍝🍜',
    'video_tag_list': '视频记录下厨',
    'content': '对最近就是很懒，啥都不想写，于是再来发个日常\n平时的早餐：培根，煎蛋\n芹菜炒粉条\n麻婆豆腐\n甜椒酿肉\n日式咖喱鸡饭\n香蕉玉米烙饼\n萝卜烧肉\n红三剁\n土豆排骨汤\n番茄鸡翅\n布朗尼蛋糕\n中间穿插了一些我的晚餐[得意]\n#今天吃什么[话题]##视频记录下厨[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/b9e96000-269deb1-8e58-359951010b51?sign=576f116bd1483aeb2cadc7e47d4d21d4&t=65fb06d4',
    'video_id': '58ec59d97fc5b83438b5f21d',
    'title': 'Beauty and the Beast 美女与野兽Belle仿妆【视频】',
    'video_tag_list': '创意仿妆秀;植村秀 shu uemura 自动砍刀眉笔;植村秀 shu uemura 无色限柔雾唇膏',
    'content': '图文版本也发在我的主页了记得去看哦~\n\n\n#创意仿妆秀[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhTBTSXePrQ-PyqP7pBjHrVv4ZEa_compress_L1',
    'video_id': '58ec5fbbfb68a23bea049dcf',
    'title': '绝对停不了嘴，爆爆爆好吃的凉拌香辣藕片',
    'video_tag_list': '',
    'content': '#超Easy的凉拌菜[话题]#\n★★★★★\n小圆食记\nMenu\n女人要想拥有好的气色，饮食方面的调养尤为重要。民间有“荷莲一身宝，秋藕最补人”的说法.\n★★★★★\n创意指数\n凉拌香辣藕片\n▼\n凉拌香辣藕片\n·食材·\n藕、小米椒、蒜、姜\n辣椒粉、香油、糖、醋、盐\n1.藕洗净去皮\n2.切成片状\n3.小米椒切圈状\n4.姜蒜切末备用\n5.沸水下藕\n6.沥干放入凉水\n7.烧热油\n8.淋在辣椒粉上\n9.放入小米就、姜蒜末\n10.再淋上辣酱油\n11.倒入适量的糖、盐、香油、醋、白芝麻\n12.搅拌均匀\n13.一道香辣可口的凉拌菜就完成啦~!'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lta5MlljHWCIwsbiCZgc84MhSuxA_compress_L1',
    'video_id': '58ec86f3696012435cf39bff',
    'title': '第一次录视频，护肤的重点',
    'video_tag_list': '',
    'content': '视频灯光不好，还请大家将就看，我是真的不喜欢用美颜滤镜，虽然更好看，但是我觉得那样太假，用了美颜就算是烂脸皮肤也照样看着很好。我相信，你们要的是真实的我，而不是经过美颜后说我的皮肤很好零毛孔快来看我啊，哈哈。不过，下次我会注意下灯光，这次拍的有点暗了。\n1⃣️饮食：减少糖分摄入，主食粗细粮结合。尽量吃GI值低的食物。一般GI值高糖分就高。\n2⃣️运动：给自己坚持运动动力。一周至少运动两次，三次更佳，四次最好。一次运动包含30分钟有氧➕1小时无氧。中间请不要聊天玩耍😎\n3⃣️不要忽略的护肤步骤：\n1、肌底液，加速后续护肤品吸收。\n2、护肤油，修复肌肤。\n3、“周末霜”，一周至一个月中让皮肤休息一天。\n第一次录视频说的不好的地方还请大家谅解，有点眼袋，因为我现在真的好困，拿午睡的时间来录视频😞\n#护肤步骤看视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/cdf0a9298197035780c58cdcc390020045cf7ec0_r_ln',
    'video_id': '58ec908b78362373051f2331',
    'title': '古老礼堂毕业典礼🇬🇧',
    'video_tag_list': '带着小红书去旅行',
    'content': '测试一下视频功能[惊恐R][惊恐R]\n哈哈哈，曼彻斯特大学数学院研究生毕业典礼🎓🎓🎓\n是哒，你没看错，我是学数学的[笑哭R][笑哭R]\n古老的⛪️，百年历史啦，老视频分享一趴[哭惹R]\n大家一定记得去🇬🇧玩的时候，多逛逛教堂哦\n会不定期分享好吃的好玩的好看的，燕窝养生，美容护肤，记得关注哦[飞吻R]\n#最爱旅行地[话题]##带着小红书去旅行[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpZWkjB_rbzCM_8yUFsF1RDA2m5I_compress_L1',
    'video_id': '58ec91a3faa0524f039ad070',
    'title': '💁🏻女生必练💪🏼有氧过后必须有加组坐姿夹腿训练！',
    'video_tag_list': '',
    'content': '因为女生经常穿高跟👠\n会造成股四头和大腿外侧肌肉代偿过多\n（公子就是这种体型😭）\n又经常坐着办公 久不运动\n髂腰肌和大腿内侧其实是无力状态\n不管是跑步还是椭圆机\n在找不准臀部发力为主的情况下\n加上核心不够稳定 会过多使用股四头发力\n有氧后加几组坐姿夹腿\n锻炼大腿内收肌 是公子必练哦~\n不仅可以塑造大腿内侧线条加强内收肌\n平衡大腿发力 减少外侧和股四头的发力\n对于锻炼👦🏻👧🏻PC肌也是非常好的动作\n红薯们记得哦~公子一般是5组\n重量根据自己的实际情况增加\n第一次练习会有很酸痛得感觉\n那是你从未锻炼过这块肌肉\n记得练完需要拉伸哦~\n加油加油~\n#健身靠装备[话题]##健身穿什么[话题]##厉害了我的健身房[话题]##我为瘦身打卡[话题]##练出翘翘蜜桃臀[话题]##周末去运动[话题]##臀部塑形视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/13f0f30ef045c124439422b8a8c8705da5990f65_r',
    'video_id': '58ec9bf57fc5b833d1e085ac',
    'title': '成本仅需5元！教你做超快手牛奶炖饭',
    'video_tag_list': '用视频记录美食',
    'content': '“午餐吃什么？”一度是许多办公室白领的终结问题！简单便宜的便利店小吃是否真的能满足上班族挑剔的胃口呢？今天喵招带来用便利店都能买到的三角饭团和乳制品，微波炉轻轻一转，就能变身成日式经典的牛乳炖饭，营养又美味哟~！   #美食才是人生主角[话题]# #西餐快手料理[话题]# #用视频记录美食[话题]# #叮！零失手微波炉食谱[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/338bab6a035f92788b97b43dea0c6501f846361e_v1',
    'video_id': '58ecc83fd5945f76d28ebcd6',
    'title': '第一次发视频😜#clc-鬼怪# #kpop舞蹈#',
    'video_tag_list': '舞蹈表演;韩国',
    'content': '第一次发舞蹈视频 也是我们舞团第一次外拍 前后大概排练了四五次吧 不算特别完美 但是大家都很用心呢❤️\n一大清早就赶到徐汇滨江 十几度的天穿着短裤短裙 还好天气比较给力 一直都阴沉沉的 直到拍完之后才下的雨[偷笑R]\n#舞蹈表演视频[话题]##舞蹈表演[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luO34gmgS4lsFgUR5uBkZiiGeO6y_compress_L1',
    'video_id': '58eccb8702f37d5eacfc6ea9',
    'title': 'Yvonne教你✨眼约会妆容',
    'video_tag_list': '香奈儿 Chanel 自然亮肌粉底液;植村秀 shu uemura 专业睫毛夹;芭比波朗 Bobbi Brown 流云眼线膏套组;汤姆·福特 TOM FORD cheek color腮红;跟着视频画眼影',
    'content': '#日常眼妆怎么画[话题]##最适合春夏的眼影[话题]##跟着视频画眼影[话题]#\n春天是最适合约会的季节！今天要教给小红薯们一套简单好用的约会妆容！\n约会妆的关键在眼睛！想象抬头的一瞬间，眨巴眨巴的闪亮眼睛太让人心动啦\n以下是细节福利: 视频中的化妆品哦\nStep 1 底妆： Chanel粉底液\n\nStep 2 眼部打底： Nars\n\nStep 3 眼影： MAC Ellie Goulding限量眼影盘\nStep 4 加深眼影外V\nStep 5 晕染眼影\nStep 6 加闪粉：3ce\nStep 7 眼线： Bobbi Brown眼线膏\n\nStep 8 睫毛： Shu Uemura 植村秀睫毛夹\n\nStep 9 画眉：Anastasia眉膏\nStep 10 遮瑕 + 高光 MAC 六色遮瑕盘\nStep 11 定妆粉 MAC定妆粉饼\nStep 12 腮红 Tom Ford腮红\n\n最后提醒一下小红薯们，底妆一定要找到适合自己肤质的品牌哦\n小红薯们快点行动起来 练习你的约会妆容吧\n如果有任何美妆的问题也欢迎给我评论哦'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljJ3JAQ9OSwM9cfbfyr_uPxOenhy_compress_L1',
    'video_id': '58ece0827836236e1b96526d',
    'title': '燕窝炖煮直播💋炖煮方法大揭密',
    'video_tag_list': '周末吃啥',
    'content': '之前写过燕窝的N种吃法😘宝宝们可以去瞅瞅[赞R]\n今天刚多好一盏燕窝，炖煮成功，软糯浓稠，之后按之前笔记写法，加入牛奶，椰汁水果等，做成各种逼格很高的睡前补品哦[飞吻R]\n干燕窝之前也推荐过很多不同店家，今儿炖的001[萌萌哒R]\n🌷方法：\n🌱泡发：干燕窝泡发1.5小时，撕碎。[吧唧R]\n🌱挑毛：挑小细毛。用镊子挑，或者筛子在水里过滤。[萌萌哒R]\n🌱继续泡发2个小时，盛出备用[赞R]\n🌱炖煮：水刚没过燕窝为好，别放太多水哦[扶墙R]不然会化水[扶墙R]隔水炖！如果是自家大锅，是水烧开放入，30分钟完成[得意R]我是用的炖锅，具体如下⬇️\n🌸炖锅：天际，隔水炖锅，小蓝胖，有子母两个炖盅，可叠放一起，我平时一个人吃，就只用小炖盅，架空蒸，燕窝档1小时。大炖盅架起来正好能在水里，小的就不行啦[萌萌哒R]\n🎉欢迎有更好炖煮经验的小红薯来和我切磋技艺呀，一起把燕窝炖的棒棒哒[赞R][赞R]\n自己炖乐趣多[赞R]\n🎉会不定期分享好次的好玩的好看的，旅行穿搭，美容养生，记得关注宝宝哦[飞吻R]\n#美食才是人生主角[话题]##吃货小分队[话题]##周末吃啥[话题]##网红美食我来推[话题]##高颜值厨具[话题]##颜值爆表的brunch店[话题]##双十一买什么[话题]##下午茶GOGOGO[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lgNyyoTmE_nvG53WJ9m2VM19-bnn_compress_L1',
    'video_id': '58eceb6ed1d3b961bb2d3a2f',
    'title': '彩妆界黑马——性价比超高的口红试色分享',
    'video_tag_list': '最值得入手的平价唇膏',
    'content': '好久没发视频的玛丽来一发认认真真的试色视频了！这次给大家试色的国货中的彩妆黑马--烙色，她家口红产品线也不少，这次我尝试的是三种质感完全不同的口红，但是统一的就是质地都好轻薄，唇感一级棒！详细的大家看视频吧！#唇妆试色报告[话题]##最值得入手的平价唇膏[话题]#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lh66dnIDJ552haromLRVEhIaVNpf_compress_L1',
    'video_id': '58ecf5ebfaa0522033038f80',
    'title': '哈哈哈哈哈哈哈——瘦了0.5',
    'video_tag_list': '',
    'content': '答应我\n看到最后\n〰〰〰〰〰🍓\n吃饭去[笑哭R]\n发重复了一个视频😂\n我就靠这个减肥了[得意R]\n毛衣MaxMara weekend，现在没有卖啦！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/ccb517ad-d27b221-bd57-819c2d0b9bad?sign=471426287868c0ea6376dd89c645a979&t=65fb06d4',
    'video_id': '58ed75e87fc5b83726c3d240',
    'title': '最近最值得收的两个盘！！你值得拥有！！',
    'video_tag_list': '',
    'content': '哈咯 大家好 好久不见！！\n第一次以视频的方式和大家见面，希望不要被吓到。。～\n因为时间限制 这个视频只能和你们分享两个产品 但这是我这个月买到的最喜欢的两件产品\n一个是too faced的natural love眼影盘\n一个是benefit的cheek parade腮红修容高光盘\n具体信息视频里都有\n希望你们可以喜欢这支视频！！\n爱你们的颠颠！！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvb7TBrw9BWkvIUTF1fA65So-w3I_compress_L1',
    'video_id': '58edc58002f37d547c044aa0',
    'title': '✨🍽超简单水波蛋+Hollandaise Sauce (Egg Benedict)做法',
    'video_tag_list': '用视频记录美食',
    'content': '早餐丰盛吃～☀️\nEnglish muffin或者吐司配上菠菜、pastrami、Benedict和Hollandaise Sauce就是一顿心满意足的brunch配置～\n简单快手的美味今天就来教给大家[偷笑R]\n第一次剪视频 有什么不足还请多见谅哈🙆🏻\n虽然步骤视频里面都写了，为了大家看得更清楚我下面还将详细再写一遍哈 还有一些注意事项啥的[吧唧R]\nrecipe里面用量一人份哈，绝对饱饱的超满足哈哈😃\n准备食材：英式松饼/吐司🍞、菠菜（或自己喜欢的任何蔬菜）、pastrami（或者三文鱼、培根、肉饼等）、鸡蛋四颗🥚、unsalted butter、柠檬🍋、盐、黑胡椒粉、黑胡椒碎\n食材不用拘泥哈配菜都可自行调整，喜欢啥咱就放啥[吧唧R][吧唧R][吧唧R]\n做法：\n▫️先来做Hollandaise Sace，热锅然后切一小块黄油丢进去融化，之后转移到小碗一旁放凉备用\n▫️另煮沸一小锅水一会儿要用\n▫️两颗鸡蛋打破只取蛋黄，挤点柠檬汁加入适量温水手动打匀（蛋白我也没浪费存起来健完身煮着吃了哈哈[害羞R]）\n▫️这时候锅里水差不多沸腾了，把搅拌盆转移到沸水上继续搅打\n▫️蛋黄糊糊变得稍微浓稠时倒入刚才的黄油搅匀直至酱汁感受到达理想厚度。倒出来加盐巴和黑胡椒粉调味，Sauce就完成了\n▫️另取两颗鸡蛋，分别倒入小漏勺里过滤 目的是滤掉一些细小的絮状蛋清，蛋闷出来就会比较完整好看\n▫️过滤完以后两颗鸡蛋分开放在两只小碗（一定分开放不要放一起）\n▫️煮一锅水 时刻勘察当它快要沸腾而没有沸腾时关火（还未产生翻滚的大泡泡），贴着锅的边缘缓慢地倒入鸡蛋\n▫️同样方法倒入第二只，两只隔开一定距离不要使它们互相接触\n▫️盖上锅盖，保持此时的水温闷大约5分钟\n▫️等待的时间处理别的食材。English muffin切成两半热锅倒一点点油muffin两面稍稍煎一下\n▫️菠菜烫一烫，摆到muffin上\n▫️pastrami或者培根也煎一煎，pastrami买来就是熟的，但还是加热下，早上最好吃热食哈\n▫️这时候也差不多5分钟了，紧张激动地打开锅盖哈哈 完美的Benedict水波蛋完成啦～\n▫️摆盘，淋上Hollandaise Sauce，开吃！\n水波蛋最难也是唯一难的部分是流动的生蛋倒到水里会迅速散开，所以步骤中一些比较特别的部分目的就是努力不让它散开比如过滤掉絮状蛋清。\n关于水波蛋的做法其实网络上可以找到蛮多的，比较常见的是加白醋还有叫你在水里搅出漩涡然后蛋顺着漩涡倒进去啥的，我觉得要么就是过于复杂要么就是不太好操作。\n按照我上面提供的方法呢可以基本保证零失误做出完美的水波蛋，屡试不爽哦😜\n总结水波蛋key points：1⃣️过滤絮状蛋清；2⃣️下锅前就要分开放；3⃣️水不要煮到沸腾，若沸腾 就会散开；4⃣️关火后赶紧把蛋下锅，下的时候又要慢慢下；5⃣️贴着锅的内侧边缘缓缓倒入鸡蛋，不要一下子猛地倒进去 那样会散开\n学会了吗～你也动手试试吧～～\n别忘了点赞啦么么哒[飞吻R]\n#用视频记录美食 #跟着视频学做菜 #美食才是人生主角#营养又好吃的健康早餐'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmI8ZEpbjvYeBTPd2zqp0aTgJ2Cq_compress_L1',
    'video_id': '58edd15cfaa052567c1e2920',
    'title': 'Jenny厨房之overnight oatmeal',
    'video_tag_list': '',
    'content': '本来我自己就一直在吃麦片\n太喜欢麦片➕牛奶的口感\nins上这个太出名\n一直想着要做一下\n大家可以搜索小红书有各种recipe\n我大概是这样做的（大家可以自由发挥）\n✅最下面是麦片＋牛奶（多少取决于杯子的高度，自己感觉一下就可以了）\n✅然后铺上水果再倒上酸奶（我放了香蕉还有柑橘）\n✅用保鲜膜盖住存冰箱\n✅第二天麦片水果都吸收了牛奶跟酸奶口感特别好\n✅接着铺上一层燕麦\n✅再铺上自己喜欢的水果，坚果，饼干等（我在最上面一层撒了奥利奥饼干碎，也可以在之前冰箱取出之后先放上再铺麦片和水果等）\n🌈一杯能量满满的overnight oatmeal就完成了\n管饱\n颜值又高又营养\n❤\n#好吃健康的燕麦食谱[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqNHZM67pu_TGV3FMwNZqYkn2jw2_compress_L1',
    'video_id': '58edd7ff02f37d320ec986ba',
    'title': '单眼皮不简单—单眼皮也可以很“亮”',
    'video_tag_list': '单眼皮如何画眼妆',
    'content': '这个视频分享的是平价中的战斗机！\nColourpop的眼影套装：Love A Flare（6色）\n其中视频用到的颜色（按前后顺序）：\nI SPY(哑光）类似于蜜桃色吧\nMELROSE（哑光）红棕色，不过我觉得他更浆果一点\nMOONWALK（偏光）偏黄红（这个偏光真的是好看到不能够再好看）\nHEAD RUSH（哑光）虽然是棕色但他有点儿是绿调\n视频中用到的产品：\n底妆是Bobbi的/散粉是纪梵希四格/眉笔是爱丽小屋的灰棕色/阴影是贝玲妃的hoola/高光是mac的Lightscapade/口红mac的taupe\n〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰\n原谅我不是专业的测评，只能根据自己的感觉来叙述和讲解😣😣😣有可能有的地方叙述的不好或者大家理解不了就给我评论，能解答的我尽量解答😯\n还有就是我很欣慰，很多的小伙伴看了我的视频，开始相信自己的单眼皮了！😆😆😆我真的超级高兴！我发视频最初的目的，就是可以让更多的单眼皮朋友去相信自己的相信自己的单眼皮有很大的可塑性，也可以美美的，。不要因为不是双眼皮就气馁就去拉双眼皮（当然，除非您是真的很喜欢双眼皮）\n也非常谢谢一直支持我喜欢我的小伙伴，你们都是最美的！\n➰➰➰➰➰➰➰➰➰➰➰➰➰➰➰➰➰\n给我提意见或者问问题可以给我评论～但是！如果没有“您好、请、谢谢”类似的礼貌用语我是不会回复的，毕竟大家都喜欢和有礼貌的人交流（笔芯）#单眼皮如何画眼妆[话题]##平价好用的单色眼影[话题]##跟着视频画眼影[话题]#\n最后谢谢大家的欣赏和支持💌'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lj17sEXlaUkwc2o2S9XPvIq8Mc51_compress_L1',
    'video_id': '58ee3e62d1d3b9162ed9f3e3',
    'title': '不做网红喵真的可惜了这委屈相',
    'video_tag_list': '',
    'content': '每天都是这幅表情，委屈受气包，真的没人欺负他，全家都宠他，饿不着，冷不着，两个窝轮流住，每天吃进口主食罐头，一包唯优，还要抱着睡[鄙视R]#我和宠物的日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhTxBBQc7cmlyxDjuvjPi5I0SkFu_compress_L1',
    'video_id': '58ee6f1fd2c8a54b67e8dc4a',
    'title': '玩坏了——Zara星星银线丝绒外套',
    'video_tag_list': '',
    'content': '太爱这件外套了\n应该没有卖了……'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ee184c0f18e8c4e5481d28e52339d44c37f62c40_r_ln',
    'video_id': '58eebdb614de415f9b108721',
    'title': '这样的洋葱莲藕你吃过嘛——莲花洋葱',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n菜不仅要做得美味，更要好看！用洋葱做成一个莲花！看起来好美！\n★★★★★\n创意指数\n莲花洋葱\n▼\n莲花洋葱\n·食材·\n洋葱、藕\n蒜、香油、盐\n1.藕洗净去皮\n2.切成片，冷水浸泡\n3.洋葱切成8瓣\n4.洋葱分小瓣撕开\n5.倒入适量的盐、香油调味\n6.均匀搅拌备用\n7.藕沥干水分放入适量的盐、香油，拌匀备用\n8.蒜切末\n9.炒香蒜末备用\n10.洋葱瓣围边\n11.中间放上藕片\n12.淋上蒜泥，铺平\n13.叠加至三层\n14.小资生活从这一刻开始'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/3273eb2c-75d2ebb-b72d-5cb720a12bd9?sign=0f7284fafeab7372c35977eaa0ad6b49&t=65fb06d4',
    'video_id': '58eef5793460946ad49e64d8',
    'title': '小秘密告诉你，恋爱这么谈就对了！',
    'video_tag_list': '小红薯档案馆;小红薯档案馆',
    'content': '薯馆长这次憋了一个超喜欢的大招！分分钟虐哭羡慕满眼心！\n来自 @suki是只小兔几🐰 的甜蜜爱情故事。\n前不久薯馆长刚刚围观了这个漂亮的小姐姐试婚纱，讲真月老居然是小红书，你敢信？\nsuki的丈夫作为曾经的宅男代表，也是完全不了解女孩子们买买买的心态。直到遇见自己喜欢的她，去了解她喜欢的小红书，打开了宠爱她的新世界的大门。\n宅男送出能永久保鲜的永生花，以及精心布置的求婚现场，哇，真的很棒棒呀！\n看到小红薯这么幸福，馆长真的很开心。\n女朋友们看完赶紧发给自己的男朋友看看，单身的小姐姐们也可以留着当考核标准呀。（心机的馆长大大）\n好了！虐狗请不要停！强烈要求大家继续拿甜蜜的故事来砸我！加入#小红薯档案馆[话题]#即可参与！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/lv3gF9ogZ7QLSA0mR7LIMfI88gsq?sign=7aedc9874d01cca97d7694660448fada&t=65fb06d4',
    'video_id': '58ef0caad5945f3470758a60',
    'title': '王公子的心得—护肤篇',
    'video_tag_list': '茵芙莎 IPSA 流金岁月美肤水;香奈儿 Chanel 山茶花保湿精华露;格莱魅  Glamglow 水漾泥润面膜;格莱魅  Glamglow 黑瓶火山泥发光面膜;格莱魅  Glamglow 紫色紧致撕拉面膜;油皮也能用的保湿精华',
    'content': '哈喽，艾瑞巴蒂❤️\n这个视频想和大家分享我的护肤想法和一些废话（巴拉巴拉～）#我的护肤日常[话题]##护肤步骤看视频[话题]##油皮也能用的保湿精华[话题]##无限回购护肤品[话题]#\n王公子从小坐标北京，95后，油皮，爱起痘的油皮（稍微吃点刺激性食物就会爆痘，而且姨妈前期也会爆痘）但是做了皮肤测试，结果显示的是我正在往中性皮靠拢。\n我之前用的护肤品是香奈儿山茶花系列（以后我试着出个心得）\n然后呢～所有的产品我都在视频介绍过了～哦！对了！我的洗面奶也是山茶花系列的，很好用！我用了3⃣️管了有用过同款产品的小伙伴可以给我评论讨论心得～\n我是没用过眼霜，如果有好的推荐也可以给我评论啊！！！主要是针对黑眼圈的！！！感激！\n这些产品小红书都有卖！很方便！\n\n\n\n\n\n我很欢迎大家给我评论讨论心得，但是没有“您好、请问、谢谢”等类似的礼貌用语我均不给回复，毕竟您尊重我了我就会尊重您。\n最后呢谢谢大家的欣赏\n谢谢各位小伙伴的支持\n💌'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltiUEMo2lN6vJX2vot7DP09VyvZs_compress_L1',
    'video_id': '58ef14e8b46c5d42f335fced',
    'title': 'Jenny厨房之overnight oatmeal(有步骤)',
    'video_tag_list': '',
    'content': '#隔夜燕麦粥[话题]#\n这次加了点步骤\n炒鸡简单\n孩子也喜欢吃哦\n随便发挥\n真的超级随便\n夏天要来了\n吃这个瘦起来\n❤\n最下面是先放麦片，倒入牛奶，刚刚覆盖住麦片就行，然后放上水果，再倒入酸奶，用保鲜膜裹住放冰箱，第二天取出我加了奥利奥碎。\n奥利奥碎就是用饼干装进保鲜袋，用手敲醉，或者圆柱体东西滚压碎。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fsoki6eFzwJaPvo85BRKUkJBpGrL_compress_L1',
    'video_id': '58ef291214de415315108721',
    'title': '你就适合田园风美甲💅清新又美腻！',
    'video_tag_list': 'Miss candy;我们就爱纯色美甲',
    'content': '看多了浓妆艳抹，有时候来点小清新，也会让人眼前一亮～so这次推荐给大家的是一款超级小清新的田园风美甲💅\n跳跃的亮黄色搭配清新的晕染花式，看一眼就会爱上😍\n✨材料清单：护甲水+白色+橘黄色+亮黄色+墨绿色+彩绘笔\n（这些颜色在日常使用也是很百搭、不挑皮的哦～）\n👆具体的美甲步骤看视频，（划重点）✍️里有有晕染美甲的画法小窍门，来围观咯～ @美妆薯  @穿搭薯\n#上班look不无聊[话题]##我们就爱纯色美甲[话题]##DIY美甲教程[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrq2pqqr62AzC2Ko8nR2ERD1KT7g_compress_L1',
    'video_id': '58ef8849b46c5d4d912a97f2',
    'title': '4/10上海时装周大秀！',
    'video_tag_list': '最仙婚纱款式',
    'content': '4/10晚上和美女姐姐们一起看的一场大show～#上海时装周[话题]#\nMOVOUS家的仙女礼服裙&婚纱～之前发过照片了～但是其实动态更美呢！傻呵呵的我忘了把视频放上来～\n#最仙婚纱款式[话题]##最美修身婚纱[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lroaMTbZuKwH1QyHZbnONLhFcoC4_compress_L1',
    'video_id': '58ef9061b46c5d665fffdba3',
    'title': '这几天在海陵岛拍节目',
    'video_tag_list': '',
    'content': '海陵岛真不错，东西好吃，海滩也很干净！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lk30lpKbLSwO-cZ8vhD4lULvqGKq_compress_L1',
    'video_id': '58efa341d2c8a53777cc5ac1',
    'title': '旅行笔记🦌日本奈良公园的小鹿🦌',
    'video_tag_list': '用视频记录旅行;奈良',
    'content': '#用视频记录旅行[话题]#\n去年♡到日本京都的🌸奈良公园🌸♡\n拍到可爱的小鹿🦌🦌\n表面看起来非常温顺\n当游客买了小鹿饼干🍪以后，就一只一只围过来\n#文艺少女风[话题]#\n🦌🦌如果不给🍪饼干🦌🦌，就拉你的裙子，咬你的后背，用头撞在你身上😑\n为了🍪饼干可以疯狂的小鹿🦌🦌但是依然可爱🦌\n#日本旅行攻略[话题]##带着小红书去旅行[话题]##最爱旅行地[话题]##我的小众旅行攻略[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luqnZkCNuJN5Oy8zH_xepHmVjIhe_compress_L1',
    'video_id': '58f00da1d1d3b978553af3b0',
    'title': '浪浪浪之重庆的两路口皇冠👑大电梯',
    'video_tag_list': '重庆;我的小众旅行攻略',
    'content': '地点：地铁1⃣️号线两路口站3号门出来是最快的\n⚠️大电梯是个交通工具，因此是跟公交车🚌一个价钱的。\n价格：¥2.00\n单程时间：5min\n开放时间：至22:00\n坡度只陡，长度之长！\n那时已经很晚了，本来不抱希望的以为又要错过了\n兄弟伙的朋友说走嘛下去看看，结果还在营业，我本来想照张像就算了 卖票阿姨不让😂\n结果坐下去又坐上来，坐上来不要钱😂\n#我的小众旅行攻略[话题]#\n@小红叔  @生活薯\n我发现重庆让我流恋的不只是在那里生活的兄弟伙，还有山城美食，以及重庆人的性格—比较大方耿直热情的那一类👍🏻\n下篇总结去了n次重庆，怀念和推荐的美食攻略\n记得关注我+点赞收藏'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llW0FbgHTGqaNSR5MAHIYms-IkRp_compress_L1',
    'video_id': '58f043e8d2c8a52f5dcc5ac2',
    'title': '搭配这种食材口感立马变鲜美 水芹炒香干',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n水芹清香，微苦，本草中记载有退热解毒，降低血糖之功效。因为茎是从头到尾都是空的，所以俗语常吃水芹喻意路路通畅。水芹本身非常鲜嫩，特意用了金华火腿粒，通过葱姜烹锅，焙出咸香，搭配香干，以突出水芹特有的清香。\n★★★★★\n创意指数\n水芹炒香干\n▼\n水芹炒香干\n·食材·\n水芹、香干、胡萝卜、火腿\n小米椒、姜、葱、糖、盐\n1.火腿切丁\n2.清水浸泡去除多余盐分\n3.摘去水芹根部\n4.摘去老叶子\n5.用水清洗后切长段备用\n6.切去小米椒头部\n7.香干切条\n8.胡萝卜切丝\n9.热油锅炒香小米椒、姜、葱末\n10.炒出香气后倒入火腿丁清炒片刻\n11.加入胡萝卜丝、香干条翻炒\n12.胡萝卜丝变软后快速倒入水芹煸炒\n13.倒入适量的盐、糖调味\n14.大火快速翻炒几下即可出锅\n15.听音乐，做美食，享受小资生活'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/5fb4078fe99755076832ad9410cbb8eafea93822_v1_ln',
    'video_id': '58f05b7cb46c5d12242a97f5',
    'title': '',
    'video_tag_list': '',
    'content': '让男评委都坐不住的男脱衣舞！！！！\n意大利帅锅Gabriel esposito 领衔\n这一群磨人的小妖精，简直让人喷鼻血！\n弯了弯了，又弯了！！！\n这次要来个笼子关起来，每天跳一遍了！\n借用杨迪的一句话，这个世界太不公平了！颜值又高还会撩骚！\n转自  欧美综艺'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/a48d671ddb2be9545b571c0632f811ad8ab1540b_v1_ln',
    'video_id': '58f0add67fc5b82c37c89a5e',
    'title': '你不知道的5种凡士林妙用，赶紧get起来',
    'video_tag_list': '凡士林',
    'content': '关于凡士林，你真的会用吗？小小凡士林还真是不简单，可是传说中的性价比之王哟！今天来看看无所不能的凡士林到底能帮我们解决生活中多少烦心事呢？\n#视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lu1s2nI5n6yffcfLidaonfOhX5aA_compress_L1',
    'video_id': '58f0bdccb46c5d5dafffdba0',
    'title': '不走心快速眼妆#通俗易懂类型',
    'video_tag_list': '西柚色眼影怎么画',
    'content': '哈哈这个是我接着上一个发的视频 来出的一个不走心眼妆。\n你们可以先去看上一个视频，但上个视频我把速度调快一点所以声音就完全变了，这个视频声音是原声。\n首先背景音乐：Lying Together\n这首歌是我每次化妆都会听的歌\n粉底：虫草粉底液 00号\n眉笔：Tomford 04\n眼影：Suqqu 02\n睫毛夹：植村秀\n睫毛膏：Kiss Me\n下睫毛膏：倩碧\n口红：YSL唇釉08\n#跟着视频画眼影[话题]##西柚色眼影怎么画[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/335882618e2ea1ae1e8f0a93d47a841d34127bc7_r',
    'video_id': '58f0e80dd1d3b92c893af3a9',
    'title': '边走边拍～',
    'video_tag_list': '用视频记录旅行;文莱',
    'content': '#用视频记录旅行[话题]#\n去文莱旅游～最值得入住的帝国酒店\n酒店周边的风景也是最好的，很适合休闲的度假小住几天\n'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/ll9n2To6pTG5bYp3pDrNl6vtQNhk_compress_L1',
    'video_id': '58f0f7a5d2c8a50ecad35b40',
    'title': '发一段海胆小视频',
    'video_tag_list': '',
    'content': '哈哈哈哈哈哈哈'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FpExO_DVj6ojgu45y3u7Jjz5CuUp_compress_L1',
    'video_id': '58f17f32d2c8a53d3ad35b3c',
    'title': '本期话题:装修视频记录',
    'video_tag_list': '',
    'content': '#装修视频记录[话题]#\n难得周末好时光~小红薯们现在是不是躺在你们的爱窝里，懒洋洋地晒着太阳？\n看着自己美美地爱窝，觉得幸福感爆棚！\n那不如来参与个#装修视频记录[话题]#的话题呗！\n【视频拍什么？】\n用视频拍下家里有趣的一盏灯，或是布置得最满意的一个角落，或是家里一个空间的换360度无死角的装修展示！\xa0还可以一边拍视频一边给视频配音介绍和大家唠唠嗑儿~\n下一个录播网红就是你！\n【笔记文字写什么？】\n记得要一定要在正文中打上话题标签哦！#装修视频记录[话题]#\n然后可以和大家分享一下你的装修小心得哦~以及视频中涉及到的单品的品牌和价格信息，做一枚合格的种草机！！\n如果没有视频权限却又很想发笔记的宝宝，快来给生活薯留言吧！\n以上视频来自小红薯\xa0@\xa0悦小喵爱臭美_\n号外|小红书最新4.18版本已上线，话题活动规则有了重大变化！！\n新版本中，笔记将通过在正文中打上# 话题 而不再是给图片加话题贴纸参加话题~~'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/d71315a1-2e7e241-a436-d0bf91dcbaae?sign=a69e1fc1190366dfe6f4e293388da882&t=65fb06d4',
    'video_id': '58f1bed93460943f746a627c',
    'title': '8周健身小白变身比基尼女神计划（线上减脂营）',
    'video_tag_list': '见人不如健身',
    'content': '最近收到很多小红薯的留言，关于减脂，关于增肌，关于饮食；关于如何减掉肚子上的肉和翘臀不粗腿。很多问题，其实是一两句话说不清楚的，为了让大家更加综合系统的看到我俩日常的训练和饮食，我们精心制作了一期大的策划，健身小白变身比基尼女神8周挑战！\n在这八周里，你将要和我们一起：\n－\t开始前，拍一张全身照片并在小红书上@fit4life, 准备充满正能量的8周！\n－\t八周内，每周按照我们3次的训练和饮食视频，一起吃的健康练的科学！\n－\t做好作业，我们会推荐一些其它APP上的训练和fit4life比基尼减脂塑形训练，让你一周7天持续燃脂不停歇\n－\t坚持一下：无论多么好的计划，不坚持都无法成功。每天打卡@fit4life, 8周后我们会选出最有毅力的女神，并赠送女神大礼包！！\n在8周后，你不但会从健身小白变身比基尼女神，我们还会帮你，让更多的小红薯认识你，让你的正能量激励更多的人！赶快加入我们吧！\n想第一时间看到我们的视频？快关注同名平台 Fit4Life健身与美食 吧！\n@小红叔 #健身是把整容刀[话题]##健身靠装备[话题]##科学减脂食谱[话题]##见人不如健身[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lt_5BOVJrdGeYmPJDY6PFiRQTqgm_compress_L1',
    'video_id': '58f1c0afb46c5d43cb5dba04',
    'title': 'Cherry__ZZ | pony告诉你，正确涂防晒的心机',
    'video_tag_list': '',
    'content': '每日更新 喜欢点赞关注 | [飞吻R]pony告诉你，正确涂防晒的心机tips'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/e6d45feb0d689541e8b8fb378ab2b849bed2317f_v1_ln',
    'video_id': '58f20d30b46c5d4bc25dba02',
    'title': 'shourouk这么美的手链怎么没人发#闪瞎的手链#',
    'video_tag_list': '少女心手链',
    'content': '去年买的\n我记得香港代购的\n施华洛世奇钻\n法国珠宝品牌\n她家的耳环 手链 项链\n特别有个笑脸跟爱心的炒鸡可爱\n炒鸡！\n钻好闪！\n刺绣，水晶，非常有份量，是皮质的反面，1300左右价格，我觉得性价比很高❤\n#少女心手链[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltDVbbtJbgthDFptCLW384Ds5igy_compress_L1',
    'video_id': '58f23c9bd2c8a53c2024317e',
    'title': '隔壁老王家的布偶猫🐱～萌萌哒肥肥哒～小视频揭露吃货真面目',
    'video_tag_list': '我和宠物的日常',
    'content': '朋友家里的布偶猫炒鸡漂酿～\n大名小米，小名1w8，\n特点～能吃能睡能拉超级懒～\n性格超级好，随便摸随便蹂躏，就是不生气哦～\n#我和宠物的日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lojerYe3mAmBp49i6NeQ_YwO_VAe_compress_L1',
    'video_id': '58f2446914de414731f1cb05',
    'title': '2017.3.12@上海梅赛德斯，张学友创造永恒经典演唱会～',
    'video_tag_list': '去听一场演唱会',
    'content': '从中学时代就开始听张学友的歌～\n特有的磁性声音，优雅的俏皮兰花指😂～\n这辈子看的最多的演唱会～\n你若唱到老，我亦伴到老～\n永远的男神没有之一！\n#去听一场演唱会[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/llUTwEXTIOARVW2UBKb9abHksCPo_compress_L1',
    'video_id': '58f2501ad2c8a50607cbb1ba',
    'title': '预告✨除了网红店还有原生态茶园 @杭州',
    'video_tag_list': '杭州',
    'content': '今天去了原生态的茶园，相较于漫天飞的西湖龙井，今天亲眼看到了从采摘、制茶的过程，跟采茶人聊了很多。现在市面上困境在于你有钱也未必能够买到真的龙井茶，特别是明前龙井和雨前龙井。\n龙井茶的采茶期就是3、4月，头茶最好，清明前是明前龙井、谷雨前是雨前龙井。而雨后龙井在市场上的价格则比较便宜。等到7、8月的夏茶更是被他们称为“不太值钱”。\n还有关于“新茶”“陈茶”等等关于龙井茶叶的东西，等正片视频剪辑好了会告诉大家哦！😛\n'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/385a3023-aaf65bb-a6db-5aa6a962c851?sign=1bfe3ffc29eacba05710f5ca2261c541&t=65fb06d4',
    'video_id': '58f2caea34609454701781bb',
    'title': '早餐 ｜ 快手美味香蕉飞碟包',
    'video_tag_list': '',
    'content': '外焦里嫩，浓香四溢\n做法：\n把两片方吐司面包各涂一层花生酱，其中加一层鲜香蕉片，放入三角形的电热三明治机（类似于电饼铛）里，加热3分钟！\n加热后的香蕉嫩糯，花生酱甜滑，面包酥香，美味你懂的！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lu7IrWRHFuW7tUiKAXhCYmVgSS4Y_compress_L1',
    'video_id': '58f2cc4c14de411600f1cb03',
    'title': '拒绝❌水煮 美味健康三明治',
    'video_tag_list': '',
    'content': '面包是我自己做的无油无糖全麦南瓜🎃面包\n炒鸡炒鸡好吃😋 没有具体数量的方子 全凭感觉放的\n因为我已经到达一定境界了哈哈哈哈 小伙伴想尝试的可以自己查找一下配方\n鸡胸肉我在前一天晚上加料酒，蚝油一丢丢，生抽一丢丢，黑胡椒粉，淀粉腌制的，所有调料你都可以自己任意放，别问我行不行，不放糖都行！！\n第二天早上煎一下就好啦😋\n我很喜欢吃的三明治，喜欢的人可以试试呦～\nps: 可以加番茄酱，但是尽量不要放沙拉酱。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luBveH8duh5DQ3g-vcTsZYDteNPt_compress_L1',
    'video_id': '58f31bbfd2c8a5170b24317d',
    'title': '曼谷s2o',
    'video_tag_list': '泰国;曼谷;去音乐节玩耍',
    'content': '这是我第一次去音乐节\n也是第一次到曼谷的泼水节\n买票的时候买的vip\n毕竟个子不高\n怕在站在下面会闷会臭臭\n结果在上面站了一会\n好！无！聊！\n我们就喝了两桶酒之后下去了\n努力挤到前面之后\n一下子那感觉真是不一样啊\n特别是水一泼\n大家都嗨了\n万分后悔没有在T里面穿泳衣\n至于妆\n我也没用防水的\n蹦到最后美瞳摘了扔了\n妆也全用纸给擦了\n头发呢也最好是扎起来\n或者戴帽子\n不然水泼过来\n一是眼睛睁不开\n二是头发简直太多水\n一路上去的时候坐车上\n一路被泼\n真的是很气\n但是也好开心啊\n好像看我们3个女孩子特想泼我们\n都手指着我们跑到车道上用小水桶泼\n回来的时候就决定要欺负别人\n买了水枪\n结果看到小孩不敢泼上了年纪的不敢泼情侣不敢泼\n我们大概是买来装饰的😄😄😄😄\n#分享好生活[话题]##用视频记录旅行[话题]##去音乐节玩耍[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/liEn4E1rqvHNEWY1N612VrkwPunj_compress_L1',
    'video_id': '58f33e5e14de413020f1cb04',
    'title': '#美甲教程DIY#北欧家居风编织美甲',
    'video_tag_list': '',
    'content': '做了一个北欧家居风编织美甲，低调日常，显气质\n用到的产品：\nOrly三合一底油（不好用👎易剥落，手边暂时只有这一瓶底油）\ninnisfree29大理石蛋糕，裸色里有红色微粒，和小麦制的北欧风餐具很像。\nthe face shop指甲油03，深灰色，比较好涂，刷子很好用，又便宜\n用到的印花油是乔安家的白狐印油，便宜大碗\n印花板是海燕hehe084，编织花纹很好看\n#DIY美甲教程[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ls4NB-GeHMJTdlwwv_O3jyi34b_5_compress_L1',
    'video_id': '58f34ba5d1d3b95d51a2f861',
    'title': '妆前VS妆后',
    'video_tag_list': '妆前妆后大对比;苏菲娜 SOFINA 控油瓷效防晒隔离妆前乳;RMK 水凝柔光粉霜 SPF24 PA++;beautyblender 美妆蛋;罗拉玛斯亚 Laura Mercier 散粉;植村秀 shu uemura 砍刀眉笔;汤姆·福特 TOM FORD eye color quad四色眼影;凯婷  KATE 睫毛打底膏;魅可 M.A.C 时尚焦点单色眼影;圣罗兰 Saint Laurent ROUGE VOLUPTÉ SHINE OIL-IN-STICK  滋润莹亮纯魅口红/唇膏',
    'content': '每个人都不完美啊 但是我们可以去追求更美好的自己\n我从来不排斥化妆 她带来的不是欺骗 不是掩饰\n她带给我们的 是更美更自信的自己\n💕sofina控油妆前乳 台版\n\nrmk圆管粉底液101 ➕covermark提亮妆前乳\n\nbeautyblender 美妆蛋\n\nLaura mercier散粉➕muf 128仿刷\n\n玛丽黛佳眉笔 深棕色➕植村秀砍刀眉笔02\n\ntomford四色眼影 20 disco dust\n\n资生堂睫毛夹➕kate白色睫毛打底➕innisfree睫毛膏\n\n倩碧腮红08 ➕Mac omega\n\n资生堂pk107➕Laura mercier高光\nysl圆管46\n\n💕希望小仙女们都能迎接更美好的自己\n比❤️\n#妆前妆后大对比[话题]#\n#春日樱花妆[话题]#\n#春夏最爱的清新口红[话题]#\n#YSL圆管唇膏试色[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Ft6_FCtdg9w4PSrudnHi2G2pgs_H_compress_L1',
    'video_id': '58f363cad1d3b936c40f9f60',
    'title': '请你喝一杯美翻的银河✨',
    'video_tag_list': '',
    'content': 'The Fun House凡食堂\n位置：交道口南大街东旺胡同17号\n⚠️别拐弯,一直走。相信自己,你一定找得到 门头比较小\n大众点评五星好评店，需要提前一周预约\n老板电话比较难打，直接发短信更合适\n是个宝宝一定也是为了银河前来，颜值有了就足够了[偷笑R]\n很好喝噢，酒精含量很低几乎没感觉'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/2d1c4054fdd7f496f139814689cac935b1d62c83_v1_ln',
    'video_id': '58f42ccbb46c5d7d9250b177',
    'title': '有秘方！又香又脆的香辣脆皮鸡翅，一步一步教你做',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n香辣炸鸡翅是一道以鸡翅、香辣炸鸡腌料等为主要食材制作的美食。香辣炸鸡翅菜肴特征诱人的香辣气味，辣味纯正清爽，引人食欲。\n★★★★★\n创意指数\n香辣脆皮鸡翅\n▼\n香辣脆皮鸡翅\n·食材·\n鸡翅、玉米淀粉、面粉\n五香粉、辣椒粉、胡椒粉\n料酒、盐\n1.鸡翅正反两面切斜刀\n2.倒入胡椒粉、辣椒粉、五香粉、料酒、盐\n3.用手抓匀，腌制4小时使其入味\n4.面粉混入玉米淀粉，其比例为5比1\n5.加入适量的五香粉、胡椒粉、盐\n6.均匀混合\n7.鸡翅表面均匀上粉\n8.用手用力按压使其均匀上粉，来回3-4次\n9.鸡翅快速入水捞出\n10.表面再次上粉\n11.用手搓揉鸡翅表面使其产生鳞片状\n12.筷子周边迅速起泡油温合适\n13.下鸡翅，调至小火来回翻面\n14.炸至两面金黄即可出锅\n15.香脆嫩滑比FKC的还好吃呢~！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhwJpDfEz5GX8MgOXtOkC3UB7Q0B_compress_L1',
    'video_id': '58f461e114de4130d29c994a',
    'title': '【 我的旅行化妆包 】',
    'video_tag_list': '旅行带什么护肤品',
    'content': '快要放假了，应该很多人会有出行计划，所以就赶紧来更一发化妆包视频。\n我喜欢分格很科学的化妆包，这样不会弄乱里面的东西，也可以节省空间有效分配。\n今天讲的是出门半个月以内会带的护肤品化妆品，具体的看视频啦～\n#我的旅行化妆包[话题]#\n#晒晒化妆包[话题]#\n#晒晒我的化妆包[话题]#\n#旅行带什么护肤品[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/5952ca32-bb0af05-a10e-13bae9e20a1c?sign=c11d92f2bd28bb4fc8ab5d9b67260bad&t=65fb06d4',
    'video_id': '58f47bba3460947d3a49aacc',
    'title': '化妆视频|春末桃花妆',
    'video_tag_list': "PONY EFFECT;I'M MEME 我爱哑光蜡笔唇膏;I'M MEME 我爱蜡笔唇膏;I'M MEME 我爱十色眼影盘;PONY EFFECT 幻彩美颜腮红棒;PONY EFFECT 莲采润白气垫粉底霜;桃花妆眼影教程",
    'content': "感觉隔了好久终于又出视频啦~对不起大家啦~\n这次新入手好多来自I'm meme 和的产品，之前一直想入手ponyeffect的气垫，这次终于一起下手了，想不到好用的不要不要的~遮瑕力超级棒，看我怎么遮红色就知道啦，因为颜色是适合我皮肤的sand色，所以底妆贴合感超棒！\n在说说这只ponyeffect的腮红棒，包装实在是美赞死了，超爱这种金属光泽感，顶部斜切面的设计，很有未来感，超级喜欢，想不到作为我的黑眼圈遮瑕这么好用！！（哈哈哈，有点歪了）\n眼影用的是I'm meme眼影盘02号色，我家本来就有01色，这下都齐了，2号色偏红色系，所以话桃花妆再适合不过啦。\n最后再来说下I‘m meme的唇膏蜡笔，好滋润啊，我觉得这两个颜色叠加涂更加好看，有一点点渐变感觉，笔芯比日常用唇膏芯小，所以勾勒嘴唇很方便，适合随身携带哦~\n一起来看我的视频吧~\n#日常妆容打卡[话题]##夏日缤纷妆容色[话题]##日系妆容腮红画法[话题]##桃花妆眼影教程[话题]# @美妆薯"
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/b75cf01d-b18452b-b124-72a29c8ca86d?sign=2c9962413aa5c31894ddafe086615e29&t=65fb06d4',
    'video_id': '58f49cc67fc5b8615572b0bc',
    'title': '8周挑战第一周（1）：健康食品大采购｜四个动作帮你建立核心稳定',
    'video_tag_list': '8周变身比基尼女神;8周变身比基尼女神',
    'content': '#8周变身比基尼女神[话题]#比基尼女神8周挑战第一周- 三分练，七分吃，快跟随weiya和giselle去超市采购健康的食品，换掉你的白米白面，并用蔬菜水果塞满冰箱吧！\n想变成运动达人？首先你要学会激活核心肌群-四个明星动作让你找到核心稳定，一秒变pro.\n最后，不要忘记完成你们的家庭作业！持续关注我们，周三视频里会有新的任务 \xa0给自己加油打气，请在小红书上@fit4life 每天打卡，并加#8周变身比基尼女神[话题]#标签；8周过后，惊喜大礼等着你！\n任务一：去超市采购健康食品\n－\t白米换糙米，白面包换全麦面包，其他精粮换粗粮\n全谷物/粗粮富含更多营养，而且是升糖指数较低的选择，这就意味着，吃糙米/全麦面包/粗粮更利于保持血糖的稳定，于是多余的糖分就不会存储成脂肪了! 更重要的是，由于富含膳食纤维，全谷物还能增加饱腹感，让你吃的更少还不容易饿\n－\t黄豆，鸡胸肉和鸡蛋：每天摄入足够的蛋白质\n黄豆，鸡蛋和鸡胸肉都是非常优质的蛋白质，而且鸡蛋和鸡胸肉脂肪含量很低，所以是非常好的补充蛋白质又不长胖的食物。每天摄入足够的蛋白质，是我们变身运动达人和保持好皮肤的关键哦！\n－\t脱脂奶和全脂奶：自制低脂无糖希腊酸奶\n市面上低脂又无糖的酸奶选择很少，蛋白质含量高口感又好的希腊酸奶又很贵，所以我俩习惯自己去超市买牛奶，再用酸奶机自制希腊酸奶（做完普通酸奶后，在纱布上滤上4个小时就是希腊酸奶啦），好喝又不贵！大家快来试试看\n－\t大量的蔬菜和水果\n每次去超市，我们都要买上一大筐新鲜的蔬菜和水果。绿叶子菜吃的时候就不用看分量了，吃多少都是零负担的，水果的话我们独爱草莓和蓝莓，配上酸奶或者制作奶昔，都是好看又好吃！\n任务二：激活核心训练\n请跟随本视频后半段，本周做1-2次激活核心的练习。我们精心挑选了激活核心肌肉群的四个招牌动作，帮你找到核心收紧的感觉。要想训练时动作准确且避免受伤，激活核心是你的第一课，也是最重要的。\n任务三：腹肌练习家庭作业\n请在keep里搜索“核心改造”课程（基础）完成1-2次，或者在fit4life公众号完成“6个动作，让你穿着马甲线过夏天”训练（进阶）1-2次\n周三视频会有新的全身训练任务，请持续关注我们！想第一手看到我们的视频？快快关注同名全平台 Fit4Life健身与美食'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmPHMSXJVdN_i2Mk2iuK47ZcQ283_compress_L1',
    'video_id': '58f4b33514de41520cbd4375',
    'title': '#kpop舞蹈# 第二弹 #aoa-excuse me#',
    'video_tag_list': '韩国;舞蹈教学视频',
    'content': '第二个舞蹈视频 这次前后也就排练了三次吧 而且最后还是自拍的😂😂看来下次不能偷懒 还是要抓个人帮忙拍一下[得意R]\n#舞蹈表演[话题]##舞蹈教学视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/loAapzhbHbNecaYv4JHNWBsTFvPk_compress_L1',
    'video_id': '58f53b1414de41296497f87c',
    'title': '日常记录3',
    'video_tag_list': '视频记录下厨',
    'content': '☀️☀️☀️\n随便拍的一些平时做的菜，我也是每次突然想起来才去拿手机拍的哈哈！[喜欢][喜欢][喜欢]\n这支视频里拍到的菜：\n海鲜面\n生炝芹菜丁的拌料\n芹菜洋葱炒蛋\n秘制排骨焖饭（这是一道看着图就能脑补出味道的好吃到哭泣的主食！）\n干煸豆角\n蜂蜜酸奶涂吐司🍯🍞\n菠萝咕咾肉全过程（炸酥肉开始）🍍\n豆角焖面\n红烧羊排\n老奶洋芋\n菠萝/杏子芝士蛋挞菠萝\n泰式红咖喱海鲜炒饭\n清蒸比目鱼🐟\n蚂蚁上树\n秋葵炒蛋\n香蒜蜂蜜煎鸡胸肉（好吃到爆炸，减脂增肌首选）\n西红柿炒西葫芦（配色超好看的）\n清炖竹丝鸡（乌骨鸡）🐤\n#今天吃什么[话题]##视频记录下厨[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llnv3EhKFdfRNzYwFwJD5UtVPqAB_compress_L1',
    'video_id': '58f582a8d1d3b95d329b7a34',
    'title': '魔都最火“腌笃鲜”，真真让人鲜掉眉毛',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n腌笃鲜，属于江南吴越特色菜肴，现已是上海本帮菜，苏帮菜，杭帮菜中具有代表性的菜色之一。\xa0“腌”，就是指腌制过的咸肉；“鲜”，就是新鲜的肉类（五花肉、蹄髈、小排骨等）；“笃”，就是用小火焖的意思。\n★★★★★\n创意指数\n腌笃鲜\n▼\n腌笃鲜\n·食材·\n春笋、五花肉、咸肉\n百叶结、葱、姜、料酒、盐\n1.春笋去皮\n2.切成滚刀块\n3.葱姜备用\n4.鲜肉切块\n5.浸温水1小时\n6.五花肉焯水\n7.煮沸捞出洗净\n8.咸肉焯水备用\n9.砂锅中倒入清水煮开\n10.倒入葱姜、五花肉、咸肉、料酒，大火煮沸后调至小火炖煮\n11.30分钟后放入春笋\n12.慢炖一小时，放入百叶结\n13.再煨10分钟关火\n14.喝完这碗汤把春日的记忆留在肚子里~\xa0！\n#超级下饭的家常菜[话题]##人民的家常菜[话题]##我的私房菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmAndiS_pTttDyaM8wmXQPV1cWsJ_compress_L1',
    'video_id': '58f598f2d1d3b931d9871cc8',
    'title': 'Cherry__ZZ | 我的包包里都放了什么',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltU62Nw_5ru4N_McHjO9PBr3a1fR',
    'video_id': '58f5afd914de413df1bd4375',
    'title': '修长美腿练起来！👀',
    'video_tag_list': '必须要安利的健身动作',
    'content': '#必须要安利的健身动作[话题]#\n瘦腿视频来了，专门找我的健身教练给你们录的，最专业的讲解，也是最专业的动作，希望对你们有用。👐🏻👐🏻\n不要想着求速度，要坚持并且有效率的训练。‼️\n这几个动作都是练臀腿的，练的时候尽量把臀部夹紧收腹\n动作有可以在家练，也可以在健身房练的，夏天到了😊一起加油吧💓（对了之前有妹子问过我睫毛增长液 我找到名字了，但是那条评论我找不到了，叫M2beaute 不错的 朋友用过，说不错，就是容量少了点，但是不会腻。我是种睫毛的我没用过。）你们可以参考下😊\n#必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/4bedeb2ec825a77f498227205cd96abba646b096_r_ln',
    'video_id': '58f5b07dd2c8a50c342c0d09',
    'title': '一秒变脸',
    'video_tag_list': '',
    'content': '过敏终于要好了～天气也暖和了，心情超级好'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/li-7BBtC95mLS9yGPp1CszP9AKan_compress_L1',
    'video_id': '58f5e82514de41031dbd4384',
    'title': '如何使用海淘网Asos战略贴视频#Rita聊天室#视频',
    'video_tag_list': '',
    'content': '来出一个视频 分享一下如何使用海淘网Asos来挑一些好看又适合自己的衣服～\n希望对你们有帮助啦\n以后我也会经常以视频方式和大家聊一聊 推荐一些好用的东西 💋\n希望你们会喜欢啦 记得点赞么么哒💙💜💚❤💛'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/89b14af306a50939a04ed29673e8326237d0e2bb_v1_ln',
    'video_id': '58f5fa2a7fc5b8112df3708b',
    'title': '过期的护手霜不要扔！教你4招护手霜的妙用提升生活技能',
    'video_tag_list': '平价好用护手霜',
    'content': '一些商场经常会有护手霜的促销，一不小心没忍住就买了一堆，有时候味道腻了，或者买的味道不合心水，没等到用完就买了其他香味的新护手霜，不知不觉间很多护手霜就闲置或者过期了，这双想让人剁的手啊！（快告诉我有多少躺枪的）\n不过那些过期或者闲置的护手霜也不要轻易扔了哟！可以继续让它们发挥其它的作用。喵招今天带来护手霜的4个生活小妙用，赶紧学起来吧！  |   观看喵招的日常。#平价好用护手霜[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkc_bzWRTpBNJTWD_CTW_k5w-sr3_compress_L1',
    'video_id': '58f605e0b46c5d43bb9a424a',
    'title': '💪🏻胖子的健身日常——胸器养成💪🏻',
    'video_tag_list': '健身器械教学视频',
    'content': '💪🏻今天po的穿搭大家都看了嘛，系不系有小盆友夸我胸型不错？[害羞R]今天就来聊聊胸部的锻炼。\n💪🏻好久没发健身视频，中间断了两周胡吃海塞&加班胖我也是没脸面对教练了。[叹气R]赶紧打卡补起来啊！四月不减肥，胖的像赵薇啊！（这是个梗，我是爱赵薇的）[笑哭R][笑哭R][笑哭R]\n💪🏻很多菇凉都会忽略锻炼胸部，一个好的胸型，绝不是简单靠内衣可以塑造的哦，我们的目标是不穿内衣也有浑圆挺拔的胸部！[害羞R][害羞R][害羞R]\n💪🏻坊间流传谣言，说不穿内衣会下垂？❌错！你的胸部下垂胸型外扩都是肌肉太过松散，胸部组织老化对抗不了地心引力的问题。相反如果只是穿内衣而不锻炼，反而会让你的胸部渐渐产生依赖，降低了自身支撑力。所以练胸部，狠！重！要！[得意R][得意R][得意R]\n💪🏻有些菇凉又要问了，练胸会不会越来越小啊？如果你因为健身运动胸部缩水了，那只能说你是瘦了！所以基本上根本没有局部瘦这种好事，要瘦都是全身瘦，你只有全身减脂+局部塑形才会让身材最没自信的地方慢慢美起来。并且锻炼胸部主要是针对我们平时忽略的上胸肌肉（我不专业昂），让胸部更加集中，挺拔。所以即使你运动E变成了D，别忘了你底围也在减小啊。我们要的是好看的姿态，而非纯粹的欲望大！[吧唧R][吧唧R][吧唧R]\n⚠️说明：\n1⃣️视频中动作均为1.5倍速剪辑。\n2⃣️每组动作8-15个看情况和负重增减。四-五组一做。\n3⃣️每组内休息不超1min，每个动作间休息不超3min。整套练完约一小时。\n4⃣️负重增减，一般第一组热身小重量，中间2-3组加一些重量，以略微吃力为好，最后可以来一组挑战重量，保证安全的情况下加重多一点，哪怕只做3-5个。\n5⃣️练完48h内练有氧效果加乘，大发一般紧接着跑步机/椭圆机40-60min。\n6⃣️放松很重要！腿粗的每次都要放松，另外练哪也要放松哪。（以后有机会出长贴讲放松吧，照片实在难拍）。\n‼️最后‼️健身贵在坚持，不然复胖分分钟！（是我没错…[哭惹R][哭惹R][哭惹R]\n#见人不如健身[话题]##健身器械教学视频[话题]##健身器械的正确使用方式[话题]##必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loG4QfgoEeweTncvkVRFMmqEeK_5_compress_L1',
    'video_id': '58f6c215b46c5d49439a4248',
    'title': '土澳复活节假期的视频穿搭秀～澳洲牌子我的真爱❤️',
    'video_tag_list': '',
    'content': '当我后知后觉发现小红书能发视频后，就一直跃跃欲试打算试下视频笔记。第一次拍摄比较生疏，剪辑也全靠自己，希望看着还不错😁😁就是发上来可能有点压缩画质不清晰啦😂😂下次再录视频我想想解决方法。\n来说回正篇，上周终于迎来了土澳上半年最大的复活节假期，相当于国内的五一，连放四天假，终于可以不上班穿美美的出去玩啦✨✨✨hin开森～\n话不多说，来奔主题介绍视频里三套穿搭吧～\n第一套上衣是今年还挺流行的喇叭袖样式的，并且比起一般喇叭袖，这件更加喇叭..百褶袖子，一抬手就是一道扇子。很喜欢～百搭的白色。半裙是我个人最爱的有点朋克风的皮带扣半裙。这件我真是很爱，之前泰国行笔记里也有出镜搭配其他上衣。这一整套均来自澳洲本土设计师品牌Asilio。\n第二套渐变流苏针织连衣裙，有点波西米亚民族风格，随着走动裙摆摆起来非常好看，动态比静态要好看更多。颜色也是冰淇淋的春夏色。是我一眼看中的款。这条裙子和搭配的腰带均来自澳洲本土设计师品牌Ixiah。（这牌子很多适合度假款的仙裙）\n第三套我之前笔记也有出镜，刺绣的露背连体裤。纯棉质地真的很舒适穿着，去海岛港口城市逛暴走只要做好防晒，其他都很舒适很吸汗。喜欢这条连体裤，真的被路人说衣服好看的概率很大。牌子依然是澳洲牌子seven wonders。\n然后提前预答下大家会问的问题：\n1:用什么拍的视频\n答：单反佳能6D\n2:背景音乐是？\n答：bossa nova版的lovin you\n3:我不在澳洲，如何享有视频中的衣服\n答：万能某宝\n4:视频剪辑所用的软件\n答：爱剪辑➕美拍'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/e165e7bdc186f8600158a958694791b9b8373486_r_ln',
    'video_id': '58f6d6f114de4160e5c14af5',
    'title': '经典糖醋带鱼，大厨配方2分钟搞定！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n带鱼富含优质蛋白质、不饱和脂肪酸，还含有丰富的DHA和维生素A、维生素D，是很好的补虚劳，养肝及促进乳汁生成的食物，经常食用对女性有丰胸和消除疲劳的功效。带鱼含有丰富的镁元素，对心血管系统有很好的保护作用，有利于预防高血压、心肌梗死等心血管疾病。常吃带鱼还有养肝补血、润肤养发、健美等功效。\n★★★★★\n创意指数\n糖醋带鱼\n▼\n糖醋带鱼\n·食材·\n带鱼、姜、葱\n生抽、料酒、醋、胡椒粉、糖\n1.姜切丝，葱切末备用\n2.带鱼洗净，倒入姜丝、料酒\n3.均匀搅拌并腌制30分钟\n4.调配糖醋汁，1勺料酒+2勺生抽+3茶匙糖+4勺醋，搅匀备用\n5.带鱼擦干水分\n6.热油锅，放入带鱼，尽量不要在锅中移动，待其变脆翻面\n7.用小火煎至两面金黄\n8.倒入调配好的糖醋汁\n9.倒入姜丝、胡椒粉\n10.大火煮开后盖上盖子，小火焖煮10分钟\n11.开盖收浓汤汁\n12.摆盘后撒上葱花\n13.外脆里嫩的糖醋带鱼就完成啦~！\n#超级下饭的家常菜[话题]##人民的家常菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljpC4JzL_GahbSsQ5KYNY-Jzytum_compress_L1',
    'video_id': '58f6db08b46c5d20869a424a',
    'title': '做家务要从娃娃抓起💁🏻\u200d♂️',
    'video_tag_list': '',
    'content': '最近小胖学会做很多家务，擦地，喂鱼，洗车还有给nunu梳毛毛😊感觉我和nunu以后只用负责摊在沙发上看电视就好😏'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loEyXaL6tpxJDTZUCa9cJvs6TnTy_compress_L1',
    'video_id': '58f72185d1d3b94b58d57349',
    'title': '【 护肤必不可少的深层清洁 】',
    'video_tag_list': '超强深层清洁面膜;茵芙莎 IPSA 粘土深层清洁面膜;斐珞尔 FOREO Luna 2代标准版洁面仪;The Beautools Rocklean毛孔清洁器 TBR',
    'content': '如果你觉得护肤品开始难以吸收，或者上妆开始浮粉，出现种种以前没有的问题，那在考虑产品适不适合你的同时，也需要看看是否深层清洁已经做到位。\n我日常除了清洁时会使用露娜洗脸仪以外，也会使用The Beautools Rocklean清洁铲。\n这个产品又是小红书给我种的一颗大草。\n我是中性肤质，两颊比较容易敏感，角质层较薄。\n之前一直没有入手的原因就有些害怕这个金属片儿我的敏感肌会不能承受，但是试用过之后发现只要控制好力度以及频率，它还是很温和的，而且效果真的很明显。\n最近发现用清洁铲之前使用一下清洁面膜效果会更好呐～\n📌\n具体产品以及用法看视频哈～希望这个视频可以帮助到你们参考。\n#超强深层清洁面膜[话题]#\n#洁面美容仪测评[话题]#\n#美容仪体验报告[话题]#\n\n\n'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/e65e4c19c84eb913a9b05f0e5d401fffe89e900a?sign=4c1a103cf6c27d4e48d31f8e31b776be&t=65fb06d4',
    'video_id': '58f72419d1d3b9555f2a41a3',
    'title': '生骨肉=肉+内脏+骨头',
    'video_tag_list': '',
    'content': "我研究生骨肉有一段时间了，但是从没有实施起来，生骨肉虽说是raw meat，但并不是生肉就是生骨肉，猫咪要吃到三四种类型的生肉加骨头以及内脏，才算是生骨肉，光喂生肉或者生肉泥或块真的不是生骨肉，这是很大的误区！我个人也喜欢喂生肉，但我不喂骨头，我家猫不吃我是真的没有办法，生骨肉的操作最大的难度就是猫不吃！但是呢，我喂生肉，我有刷牙，每吃一顿就刷牙或者给磨牙的小零食（以后会推荐）。你可以去闻一个经常吃生肉泥不怎么刷牙的猫的嘴巴，都是一股恶臭味！\n个人建议打算喂生骨肉的猫友，一定要科学定餐，科学的喂，首先要搞清楚什么是生骨肉，怎么操作杀死寄生虫等等，另外生骨肉并不是神药，可以解决猫的一切问题，要科学对待吧！\nKibbles is not raw meat abstractly, without bones to chew It won't take any time to get some teeth ailments, like gingivitis. I feed my cat meat not raw meat, so I brush my cats' teeth to get rid of bad breath and redness gums caused by kibbles"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/8e003e91234ca74922e020b04302f50f5350506b_r_ln',
    'video_id': '58f72c19a9b2ed56319c0b95',
    'title': '生活达人自制手机支架，没想到过可以这么简单，一看就会！',
    'video_tag_list': '',
    'content': '想要在手机上看视频？却苦于没有手机桌面手机支架吗？\n这次教大家利用身边不同大小的两个燕尾夹就能悄然变成一个简单手机架咯~超级简单，保证你一学就会！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsEUGox5zgGFoBw48CXEomvP7H18_compress_L1',
    'video_id': '58f76eeeb46c5d207b37c7b6',
    'title': 'FrancFranc变色杯小视频',
    'video_tag_list': 'francfranc;适合当礼物的杯子',
    'content': '这个杯子要拍来个视频会更直观，小❤遇冷水就会渐变红，好萌！\n#我就是个杯子控[话题]##适合当礼物的杯子[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhT-ASi0emsBo0ETWe8hhVKyrOeD_compress_L1',
    'video_id': '58f772b5d1d3b978872a41a3',
    'title': '夏天快到了，此时不动更待何时',
    'video_tag_list': '8周变身比基尼女神;Lorna Jane;Lululemon;耐克',
    'content': '看到@fit4life 发起的话题活动#8周变身比基尼女神[话题]##必须要安利的健身动作[话题]#\n算算离夏天不远了，离17%的小目标还有很大距离[哭哭]\n感冒快好起来，健身房动起来～\n白色上衣\n健身裤\n健身鞋'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhAtGG3qDgvIROBGgLkQxOK8MQTO_compress_L1',
    'video_id': '58f77c6614de413ed9ac3950',
    'title': '来自台湾的网红绵绵冰icemonster',
    'video_tag_list': '网红美食我来推',
    'content': '这款是咖啡味道的超好吃！店里有可以拍照超大的道具杯，还有很好吃哒华夫饼miamiamia#网红美食我来推[话题]#就在三里屯太古里南区B1'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/llaIsLhKZ8exSvO0uvGA28n0bUhI_compress_L1',
    'video_id': '58f80c1ed1d3b90d742a41aa',
    'title': '吃货限定话题：零食试吃测评',
    'video_tag_list': '零食试吃测评;零食试吃测评;零食试吃测评',
    'content': '都在说“春天不减肥，夏季徒伤悲”，可此时此刻还是很难抗拒零食的诱惑诶！怎么办了啦~\n来来来，今儿就给你个机会，把深藏肉与名的零食、压箱底的零嘴、新入手的小食统统拿出来，一起来给其它红薯安利种草，一起月半咯！\n只是图文笔记来发#零食试吃测评[话题]# 还不够，那就用视频来互相伤害呗！\n网上很流行的零食开箱测评视频，今天和生活薯一起来做⬇️\n先从一件小零食入手来拍吧，15秒小视频拍起来超简单：\n1.\xa0\xa0\xa0\xa0\xa0\xa0 拍拍拍零食的外包装 大约4秒\n2.\xa0\xa0\xa0\xa0\xa0\xa0 拍拍拍拆开零食的包装 大约4秒\n3.\xa0\xa0\xa0\xa0\xa0\xa0 拍拍拍包装里零食的真实样子 大约4秒\n4.\xa0\xa0\xa0\xa0\xa0\xa0 拍拍拍把零食一掰为二，展示质地 大约3秒\n5.\xa0\xa0\xa0\xa0\xa0\xa0 写写写文字里写下零食的口感味道，种草/拔草理由，在哪里买的，多钱买的\n6.\xa0\xa0\xa0\xa0\xa0\xa0 加加加话题活动#零食试吃测评[话题]#嗷~ 参与活动方法和往常一样，在笔记文字输入框下方，点击#，输入#零食试吃测评[话题]#，就可以成功参与本期话题活动啦！\n以下还有加分项⬇️\n在第4和第5步之间：插播一段自己吃零食的样子吧 ^o^\n想来发视频笔记的小红薯请记得在笔记下方给生活薯留言嗷，生活薯会一键传送视频门给你~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqWgURZ1eW5vBpHl2XgNgNFW2aGb_compress_L1',
    'video_id': '58f827c6d1d3b97e1dd5734c',
    'title': '金针菇最美味的吃法，别只会扔火锅里了！',
    'video_tag_list': '',
    'content': '\u200b★★★★★\n小圆食记\nMenu\n油泼金针菇是用烧热的油泼在煮熟含有佐料的金针菇上，其制作方便，色泽鲜美，又具有很高的营养价值，深受大家喜爱。金针菇具有食疗保健的药用价值，其性寒，味咸，滑润。有利肝脏，益肠胃，增智，抗癌等功效。\n★★★★★\n创意指数\n油泼金针菇\n▼\n油泼金针菇\n·食材·\n金针菇、小米椒、\n蒜、葱、生抽、蒸鱼豉油\n1.葱蒜切末备用\n2.金针菇去除根部\n3.撕成小段\n4.金针菇吊焯水捞起备用\n5.倒入适量的生抽、蒸鱼豉油、葱、蒜\n6.烧热油淋在金针菇上\n7.金针菇也能吃出别样的风味~！\n#超级下饭的家常菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llgtRZQPLdy7fTTZI2XjpjuoGIMx_compress_L1',
    'video_id': '58f84c2814de410ba4c14af2',
    'title': '最萌最暖心～一条大海参',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '每次工作或学习，都会这样碍事😢😢\n虽然碍事，可我舍不得赶走，万一下次不来了😂😂\n#我家宠物最萌的瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/05906254ea08357a37c5bc3cefc2f65b26506bae_r',
    'video_id': '58f87aea7fc5b8034d967689',
    'title': '健身黄金运动｜做好了美腿翘臀，做错了伤腰的硬拉',
    'video_tag_list': '8周变身比基尼女神',
    'content': '#8周变身比基尼女神[话题]#姑娘们如果想要蜜桃🍑臀，那么硬拉是你的必修课。但是因为硬拉这种复合动作涉及全身多组肌群，发力顺序和要点很多又很复杂，而且一旦做不好就很容易受伤，所以今天网红制作了一分钟的短视频，分享硬拉的要点和辅助工具😊\n📌硬拉分很多种：\n传统硬拉：一般指屈膝硬拉，又根据站姿分为窄距（传统）和宽距（相扑站姿）；宽距站姿更多刺激大腿内侧肌肉\n直腿硬拉：不弯腿，最常见的是更注重大腿后侧练习的罗马尼亚硬拉\n除了杠铃以外，我们还可以使用哑铃，T字杠，壶铃，绳索和史密斯机联系硬拉。\n📌辅助工具：\n腰带：使用大重量练习我个人还是习惯用腰带，不仅保护脊柱（不带腰带受过伤，下不了床😢），而更多帮我们感知呼吸。硬拉动作开始时，深吸一口气到腹腔，感受横膈膜的张力和腰带对抗的力量，就找到了这个感觉\n握力带：如果不是专业运动员，当做大重量硬拉时，建议使用握力带（用法看视频），可以帮我们克服握力不足的障碍\n鞋：做硬拉的时候，切忌穿气垫鞋，软鞋底会让我们容易重心不稳。建议穿converse 或者vans之类的板鞋，当然也可以赤脚🙄️\n📌准备姿势：\n脚：双脚与肩同宽，脚尖向前（宽站姿超过肩宽，脚尖向外45度）\n重心：身体重心在杠铃正上方\n背：夹紧肩胛，激活横隔肌，不要弓背或塌腰\n📌开始硬拉：\n呼吸：上提杠铃前，深吸气吸入腹腔，激活横膈肌\n手：双手用力从两侧要将杠铃“掰弯”的感觉😉\n脚：双脚用力向下踩\n膝盖：上拉过程中膝盖不晃动，随上拉伸直（不超伸）并锁住\n髋部：随上拉过程伸髋，在顶端夹紧臀肌，并作3秒停留（非常重要的3秒）\n长视频和文章请移步：fit4life健身与美食，有任何问题欢迎留言。本期视频参考了Layne Norton, Amanda Bucci, Jim Stoppani几位大神的教学指导，感谢大神们🙏  @杰米'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luS5-MloC86r9V8rDLH5mS_rzQNE_compress_L1',
    'video_id': '58f88351d1d3b9537af1f199',
    'title': '支持国货我们从零食开始～',
    'video_tag_list': '办公室必备零食',
    'content': '#零食试吃测评[话题]#\n最近我养成良好的习惯就是吃啥前都要先🎬下来\n可以记录下来我吃过哪里零食\n好吃还是不好吃都要一一📝下来～\n今天的主角是百草味开心果\n也算是支持国货了\n#办公室必备零食[话题]#\n#国产零食良心推荐[话题]#\n#煲剧必备零食[话题]#\n#零食发现家[话题]##看剧必备零食[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpJL6bdAodZpT1Ko3YwPzbmIsp05_compress_L1',
    'video_id': '58f89d1514de412c56017675',
    'title': '小红书「我是歌薯」来了！大家快来一展歌喉！',
    'video_tag_list': '我是歌薯',
    'content': '#我是歌薯[话题]#\n民间隐藏着各路喜欢唱歌的小红薯们，都总有那么几首是KTV必唱的保留曲目。\n终于大家现在都可以用视频来记录下自己的歌声，和其他小红薯们分享啦！\n快点录上一段你的拿手歌曲，参加#我是歌薯[话题]#的话题活动吧~\n歌唱大赛视频录制Tips：\n1.三招轻松录曲目\n✨选个背景音乐，边播边录上一段视频，当然清唱一曲也是不错的选择\n✨在KTV里唱歌，直接拍摄，录上一段视频\n✨高阶选手就发挥你的十八般才艺，开始你的表演咯\n2. 正文记得做个自我介绍并写上唱的歌歌名\n3. 最重要，记得打上#我是歌薯 的话题哈\n感谢视频中小红薯 @Littlezizi   @👓花生米儿  @亚宁大大大阿七 @熊哥痴汉  @LiveinD 的献唱\n其他的小红薯快来参加活动吧，期待来自你的歌声噢！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luWId7JAooOhahpE_w0WxROHFugi',
    'video_id': '58f96f1cd2c8a5737087886e',
    'title': '拒绝大脸👀大咬肌拜拜👋瘦脸篇',
    'video_tag_list': '能瘦脸的按摩手法',
    'content': '#能瘦脸的按摩手法[话题]#\n人生第二次录视频献给你们😂，录得很急，时间很紧，也录得很烂😂先不要打击我😭我会努力改进的😁还有就是！因为真的没想到你们会那么支持我的笔记！也没想到会获得那么多关注！很开心！谢谢你们！想说给你们送点东西。点赞👍的宝宝里，随意抽取两名宝宝，分别送出52元红包（礼轻情意重😝）因为小红书没有办法私信（我没有用微博）所以我会直接在评论下方@   中奖的宝宝，中奖的宝宝记得留下你们的支付宝号码，三天内没有回复的就重新再抽😊好了入正题！\n说说我的脸：我的脸，是属于那种典型的娃娃脸😂脸上非常多肉！最瘦的时候体重只有93斤，但是如果光看我的脸（不看全身）别人会以为我有100斤（这就是所谓的脸胖毁所有😂）\n我一直追求那种脸小，肉肉的感觉（因为我的脸很多肉，所以我的追求一般会贴合我自己实际状况😐毕竟这些肉是会跟随我一辈子的😐）也因此！我很注重咬肌大小！如果脸庞➕咬肌大。那估计我会发疯😑所以，通过网络与朋友推荐，综合了一些关于瘦脸的方法和知识分享给大家😉（说一下按摩咬肌的问题，虽说要用力按摩，可是力度保持在自己的承受范围就好，不要过了啊！怕导致肌纤维损伤或者断裂‼️这样就会有反作用了😢）：\n首先说明：打瘦脸针的确可以瘦脸，它会让肌肉松弛、萎缩变小、麻痹过于发达的肌肉‼️（这个针可以尝试性的打！但是不建议依赖它来达到瘦脸效果！）因为副作用还是明显的，在视频我有提到，下面再补充一下：\n👀瘦脸针打多了容易出现抗体，导致再次注射无效。\n👀一般为期一年效果的瘦脸针，其实半年左右就会失效，需要重新打。\n👀医师的技术也是个问题。注射剂量和部位不同，容易引起左右脸不对称😑\n其实平常生活中也有一些小方法是可以做到瘦脸的😻\n1⃣️：正确的咀嚼，一口食物在牙齿两侧各咀嚼15-25次，然后吞咽。（可以防止脸部大小了不对称的问题😇）\n2⃣️：去水肿。热毛巾敷脸15-20分钟+去水肿食疗（之后笔记我会发）\n3⃣️：芹菜+西柚榨汁后涂抹到脸上15min后，温水洗净（这个方法网上介绍，据说很管用，我没试过，有兴趣的妹子可以试试😝）\n4⃣️：将双手放在下巴两侧，食指、中指、无名指力量分别往两边颚线往上提拉按摩（这是网上推荐的另外一个按摩法，不仅瘦脸还可以促进淋巴排毒，大概按摩3分钟就差不多了。不需要太用力😊，我打算今晚回家试试这个方法）'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/cdc7c616-0a658fb-976e-5d85bfeb596d?sign=a901837096b3964b8a38282ab248151e&t=65fb06d4',
    'video_id': '58f98d273460947d427a5f93',
    'title': '在外面吃饭怎么计算卡路里｜吃外食如何不长胖',
    'video_tag_list': '8周变身比基尼女神;8周变身比基尼女神;8周变身比基尼女神',
    'content': '#8周变身比基尼女神[话题]#想减肥又没时间自己做饭？在外吃饭又不知如何计算吃了多少卡？快跟随weiya和giselle吃遍她们最爱的西餐中餐日餐，沙拉、三明治、日式定食和中式炒菜，一眼看出卡路里含量！还有网红分享的外食吃不胖的小秘密。8周挑战的第一周就要过去啦，想要加入我们的妞们，还来得及哦！记得周末不要忘记完成作业并且持续关注我们，周一的视频千万不要错过！记得每天加标签#8周变身比基尼女神[话题]#并@fit4life 打卡哦  ，8周之后有惊喜大礼等着你！\n外食原则之：西餐\n沙拉和三明治是网红最常选择的午餐；因为这无疑是热量最低而且最“干净”的午餐，吃完完全没有负罪感。今天尝试了新元素的super food新菜单，感觉很是不错\n几个tips:\n--沙拉和三明治是最适合健身星人的外食啦\n--一般的大碗沙拉卡路里含量在250-420克之间，鸡肉，海鲜为主料的一般卡路里含量较低，油醋汁是酱汁里面最瘦的。\n--推荐含有鸡胸肉，鸡蛋，豆类等蛋白质含量丰富又低卡的沙拉\n外食原则之：日餐\n毕竟是亚洲胃，总吃沙拉也受不了，日餐可能是最“干净”和营养的亚洲料理了\n日餐tips:\n--深海鱼类富含人类必须的omega3不饱和脂肪酸，所以去吃日餐，不要忘了多吃一些生鱼片（除了贵没毛病），既有健康脂肪也有丰富的蛋白质呢！（海鲜过敏和不能吃生食的，请用日式烤鱼和鸡蛋啥的代替）\n--一份标准日式定食，如果只吃100g米饭的话（视频里有教你怎么量），是480卡左右，相当不错！\n--日餐里，寿司米和盖饭里的米饭，是最胖的之一（胖的当然还有天妇罗啥的）所以如果想要控制卡路里的话，把寿司改成生鱼片，盖饭也请少吃一些大米饭！！\n外食原则之：我大中餐\n中餐永远是网红最爱的饭，没有之一。中餐并不是洪水猛兽，吃的对了，照样不会长胖\n中餐tips:\n--肉类请选清蒸或红烧的，不要油炸或者煎烤；另外鱼类和鸡鸭比猪肉，牛肉什么的脂肪含量要低\n--蔬菜是最吸油的了，一旦烹饪不好，卡路里含量会很高。所以蔬菜请尽量选择上汤，白灼或者蒸菜，上汤菠菜和娃娃菜是网红最爱！\n--中餐最要命的就是主食了，炸酱面茄子面网红一看见就必须吃一大碗。。。所以点菜的时候，请不要翻到主食那一页！！吃少量米饭或者有可能的话换成杂粮（糙米，玉米，紫薯，南瓜），是最好的选择！\n视频里满满干货请一定看完，不要忘了完成你的家庭作业哦！我们周一见！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lovaEscTg0OJ5ACRNNCCT4C5hFou_compress_L1',
    'video_id': '58f9f13914de415f41ff3bf3',
    'title': "L'Amour Patisserie🍧到底是什么风格？",
    'video_tag_list': '少女心爆棚的高颜值咖啡馆',
    'content': "这是我拍过最好笑的小剧场了😂😂忍不住要发出来\n好奇的话就就快去吃吃看吧！\n【具体图片看我上上条po哦】\n🍓店名：\nL'Amour Patisserie\n🍓地址：\n百度地图上直接搜【lamour patisserie】就有啦\n思明区湖滨西路1号109（小学路沙拉怪兽隔壁）\n🍓营业时间：\n13:00-22:30\n#厦门人气美食[话题]##厦门旅行攻略[话题]##下午茶必备小糕点[话题]##下午茶GOGOGO[话题]##高颜值甜品店[话题]##少女心爆棚的高颜值咖啡馆[话题]#"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/b5b74c06242d19f776be4fdf037dcab1c90f7cdc_r',
    'video_id': '58f9f4a3d1d3b913ed3602df',
    'title': '#kpop舞蹈# 第三弹👏',
    'video_tag_list': '',
    'content': '第三支舞 其实拍摄的时间比之前两支舞都要早 jessica的wonderland 很适合春天的一首歌 有一种甜甜的味道[萌萌哒R]'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/liXaR2ks9pxyU_w6KRyK0EPehcwO',
    'video_id': '58f9fad4b46c5d49e063af88',
    'title': '#我是歌薯# make u feel my love',
    'video_tag_list': '我是歌薯',
    'content': '么么哒～大家周末愉快哦～\n#我是歌薯[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkvK-dFvksoBOgsmLWIT9Lui4oAW_compress_L1',
    'video_id': '58fa13cad1d3b90d1ad32e38',
    'title': 'city of stars——唱的不好，我喜欢这首歌',
    'video_tag_list': '我是歌薯',
    'content': "我爱星星。#我是歌薯[话题]#\n以前唱歌还可以，后来上课太多的课，声带不行了，但是偶尔的时候会用软件唱一会歌，放松一下。\n说实在的，我因为这首歌看的这个电影lalaland。\n然后更爱这首歌。\nJohn legend版本也好听。\n因为之前单纯录的歌，不是mv，不可以导出，所以就用学校的音响翻拍的。\n晚安。\nCity of stars\n城市星空\nAre you shining just for me?\n你是否只为我而闪耀\nCity of stars\n城市星空\nThere's so much that I can't see\n还有太多我未曾看到\nWho knows?\n是否有人知道\nI felt it from the first embrace I shared with you\n当我第一次与你相拥时\n我们共同感受到这一切\nThat now our dreams\n如今\n已成为我们共同的梦\nThey've finally come true\n终有一天 我们会将它实现\nCity of stars\n城市星空\nJust one thing everybody wants\n所有人共同追求的只有一件事\nThere in the bars\n在酒吧中\nAnd through the smokescreen of the crowded restaurants\n穿过人群 烟雾缭绕的饭店\nIt's love\n那就是\n爱\nYes, all we're looking for is love from someone else\n是的\n我们共同苦苦追寻的就是这份爱\n来自于那个特别的人的爱\nA rush\n一次突如其来的涌上心头\nA glance\n一次温柔的注视\nA touch\n一次难以忘怀的触摸\nA dance\n一次翩翩共舞\nA look in somebody's eyes\n用心的注视某人的双眸\nTo light up the skies\n就能点亮这整片星空\nTo open the world and send it reeling\n去打开世界的大门 让我四处遨游\nA voice that says, I'll be here\n这时 一个声音告诉我\n我也将与你同在\nAnd you'll be alright\n所以 一切安好\nI don't care if I know\n我不在乎\nJust where I will go\n我将去向何处\n'Cause all that I need is this crazy feeling\n我需要的只是这份珍贵的感觉\nA rat-tat-tat on my heart\n我的心❤️在雀跃\nThink I want it to stay\n我愿意此刻永存\nCity of stars\n城市星空\nAre you shining just for me?\n你是否会这样只为我闪耀\nCity of stars\n城市星空\nYou never shined so brightly\n你从未如此耀眼迷人"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltCJm4Ddgt4K7d-LjxHm1N_6G3Pd_compress_L1',
    'video_id': '58fa38cfd1d3b91885d32e34',
    'title': '一只不为臭脚所动的小猫咪',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '[得意]不务正业沉迷吸猫的玛丽来更新视频了，今天给大家带来的是…………猫片！哈哈哈哈哈哈哈哈哈，这是我家新成员，三个月大美短妹妹，闺名：福虎（请f和h不分的人大声朗读10遍），哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈。小猫咪特粘人特乖巧，刚来的时候一身猫癣，毛都快掉光了，涂了两周药，晒了几天太阳现在好一些些[得意]以后的视频也会有她出境哒#我和宠物的日常[话题]##我家宠物最萌的瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/058e306627181b13360582fb8a41d26277db88c8_r_ln',
    'video_id': '58fa66e2d2c8a53a93ea5b90',
    'title': '面膜推荐视频 #Rita聊天室',
    'video_tag_list': '消灭黑头小TIPS',
    'content': '主要是以保湿面膜和祛角质黑头面膜为主的分享：）\n背景音乐是Yuna的《Crush》\n祛角质面膜：\n雅漾磨砂面膜\n祛黑头面膜：\nDMC冻膜\n保湿面膜：\n兰芝睡眠面膜\nSisley 两款保湿面膜（蓝色偏轻薄 紫色强保湿）\nDr. Jart 蓝色包装面膜\nBarrier Repair 敏感肌保湿面膜\nFancl 保湿面膜\n希望对干皮或混干皮有帮助啦😘😘😘\n#干皮最爱补水面膜[话题]##适合学生党的平价面膜[话题]##消灭黑头小TIPS[话题]##我的护肤日常[话题]##一起敷面膜[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lv6dMn6h7OtP5_oDBEOiPMZZqUrF_compress_L1',
    'video_id': '58faa52ad2c8a5037a6466dc',
    'title': '近期爱用品分享#Rita聊天室#好物推荐#视频',
    'video_tag_list': '春季防晒必备;好物',
    'content': '来出一个近期爱用品分享吧：）刚刚还发了一个视频，现在又发一个，超级高产哈哈\n我发现录视频更加轻松真实方便些，不知道你们喜不喜欢看我视频哈😊（来自大脸的召唤）嘻嘻\n整理了一下 这些分享的东西是我这两个月最爱用的产品：\n防晒霜：科颜氏 （真心特别好用）\n美白牙齿： Carbon Coco 牙粉和牙膏 （建议晚上用，有些麻烦要多刷很多次才能刷干净，用了5次，再用一段时间看有没有大效果哈）\n隐形眼镜盒子：Muji无印良品 （卫生又方便携带）\n精华油：海蓝之谜 La Mer Renewal Oil （五星级好用）\n粉底： Bobbi Brown 虫草粉底液 （比YSL气垫更滋润的粉底液）\n眼影： Suqqu 02号\n眉笔： Urban Decay 超细笔头眉笔 棕色🏾\nTom Ford 04号眉笔\nPS： 视频录到一半 男朋友就下班回家 看我在录视频 一直在搞笑逗我😂笑场2秒钟 😂😂\n希望你们会喜欢啦 记得点赞么么哒😘\n还有什么想看【Rita聊天室】的内容和话题 可以在评论里留言噢😊😊\n#春季防晒必备[话题]##我的护肤日常[话题]##好用护肤油[话题]##牙齿保护计划[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lly7CCG67n_eR_XgMsRAcFMgTyQ5_compress_L1',
    'video_id': '58fafc61b46c5d31ea9c8b71',
    'title': '对着宝宝吹气吐舌头的宝宝好萌😋',
    'video_tag_list': '小红书萌娃大赛',
    'content': '你有试过对着宝宝吹起吗？🌬️真田大叔说对着宝宝吹气每个宝宝都会吐舌头😛超级萌哦～粑粑麻麻也试试吧😘\n#KO酱的日常#\n#小红书萌娃大赛[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/1fdcf942f2e6314593ec23b4b7647e81791fd2c7_r',
    'video_id': '58fb0bfcd2c8a553ad6466dc',
    'title': '人生中一定要看一场bigbang演唱会👑',
    'video_tag_list': '去听一场演唱会',
    'content': '2014年上海YGfamily演唱会\n2015年北京bigbang演唱会\n2016年天津bigbang演唱会\n作为一个VIP连追了三年演唱会\n个人感觉，最好看的还是YGfamily那场\nbigbang、2NE1、鸟叔、WINNER、EPIKHIGH全部到场\n不过以后估计都不会看到那么好看的演唱会了\n#偶像的演唱会[话题]#\n#去听一场演唱会[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgGmkJTzSfuYTEWoKeD7JaBx0AFP_compress_L1',
    'video_id': '58fb4a6cd2c8a5225dac873f',
    'title': '#西班牙旅游攻略#住宿#交通#景点#购物#旅游视频分享',
    'video_tag_list': '西班牙旅行攻略;西班牙;巴塞罗那;马德里;塞维利亚;伊比萨',
    'content': '西班牙🇪🇸旅游回来 做个小总结分享给大家吧 总体来说 幸福感满满[得意][得意][得意]\n总共去了八天 旅行路程：巴塞罗那➡️马德里➡️塞维利亚➡️伊比萨\n首先来说一下第一站巴塞罗那 我们从London Gatwick出发去Barcelona 因为是下午四点半出发 差不多两个小时就到了 当地时间是下午七点半（有一小时的时差）当时知道是会比较晚到的 所以前两天的酒店定在市中心 地理位置比较好的地方 方便行动 ➡️酒店第一晚和第二晚（总共500欧）：\nCatalonia Square 4* Sup 加泰罗尼广场酒店\nRonda Sant Pere, 9, Eixample, Barcelona, 08010, 西班牙\n电话: +34933023386\n这家酒店因为地理位置极佳 在市中心 所以门面不是很大 但是里面的设施 房间大小以及服务都不差 是我欧洲游到现在觉得不错的酒店 电梯里还会偶遇同样来旅游的欧洲人 聊天时都会聊起这酒店不错 酒店楼下就是购物一条街 对面就是西班牙的连锁购物中心-英国宫百货 楼下就是麦当劳 晚上回家可以带点当夜宵 哈哈哈 不过酒店一楼常备有免费的牛奶饮料薯片沙拉等食物给住客 我饿时经常去拿薯片吃😋此外酒店离我们要去的景点都很近 google map步行十多分钟就到巴特罗之家以及米拉之家 我们什么交通都尝试过 地铁 步行以及出租车 因为我们同行的人比较多 所以地铁和出租车相比 出租车更划算 因为巴塞罗那并不大 去再远 车费也就10欧左右 人均一下比地铁划算 当然如果不怕累 步行是开销最低的 我们到的前两天都会步行 到处看看 逛逛 到后面都见识过之后 就会开始走到哪出租车叫到哪 对了 另提一下当地的电话卡 我们在当地比较受欢迎的Orange连锁店购入了2G流量电话卡 20欧 这八天几乎用得刚刚好 毕竟人在外面 得有能联络的手机傍身 这样才有安全感 第一天到的是下午 所以我们在酒店附近吃完挑了一家比较热闹的餐厅吃完晚饭就在附近走动走动 观察有没有第二天比较感兴趣的商店 第二天早起直奔巴特罗之家 米拉之家 和圣家堂 圣家堂的票是提前买的 巴特罗之家的票是当场排队的 不过也挺快 就是人有点多 米拉之家之前看攻略说和巴特罗比逊色一点 就是露台比较好看 所以我们就步行去了米拉之家 在外面观望了大致 但是巴特罗和圣家堂的设计真的有惊艳到我 太美了 圣家堂还未完全造好 所以不推荐购登塔票 其实跟在英国约克大教堂的登塔差不多的感受 沿着很窄小的楼道上去 从教堂50m高处看风景 没有教堂内的设计有感染力[装酷]\n第三天我们入住巴塞罗那比较有名的酒店 位于海边➡️ W Barcelona 巴塞罗纳W酒店（一晚430欧左右）\nPlaça Rosa dels Vents, 1 - Passeig Joan de Borbo, Ciutat Vella, Barcelona, 08039,\n电话: +34932952800\n海景房的海景真的超美 一定要住高层 景观更美 里面的设施也都超棒 一楼有个小bar 晚上吃完饭 还会和朋友们小酌一番 聊聊天 玩玩游戏💓 bar外面有个露台 有白色的沙发床还有泳池之类的设施 我之前的穿搭笔记中有分享照片 大家感兴趣的可以去看看 第三天我们叫出租车去了博盖利亚集市 里面各种各样的美食 不过温馨提示 外面的小店价格会比里面的小店贵一点 所以进去了之后再考虑买啥吧 还有 集市人多 扒手也多 西班牙最多的就是小偷 我很多朋友被偷了钱包护照 可麻烦了 所以建议大家去西班牙旅游一定要管好自己的随身物品回酒店后我们会去海边游玩 沿海边一排都是各种各样的餐厅 所以我们沿沙滩一路散步看风景 饿了渴了就找一家顺眼的吃 味道都不错 不过西班牙有传统的收小费习惯 不管是叫出租车还是吃饭 都会要消费 出租车的消费会在计价器里直接给你订好 吃饭的消费有些服务员会直接向你讨要 有些会安排在付费单里 看情况给 基本在5欧左右吧\n第四天出发坐火车去马德里 火车票都是提前订好打印出来的 在携程上就可以定 这次旅游定酒店这些的都是用携程和booking定的 但是我比较推荐携程 价格更便宜些 而且靠谱 booking总会出现一些意外的问题 比如私信我要我私下付酒店费用到一个银行账户（以为是诈骗邮件 多次确认后才付费 总之很操心）巴塞➡️马德里火车3小时左右\n马德里酒店：马德里洲际酒店(InterContinental Madrid)（一晚1200人民币）\n地址（Address):\tPaseo De La Castellana 49,钱贝里区,马德里,马德里自治区,28046,西班牙( Paseo De La Castellana 49,Chamberí,Madrid,Madrid,28046,Spain)\n电话（Tel):\t34917007300\n在马德里 我们主要是去逛了当地的英国宫百货EI Corte Ingles 碰到lamer在打折 一口气买了之后要用的面霜 精华水还有眼霜之类的护肤品（用后会给大家出相关分享 耐心等待哦）中途逛到celine看到价格比英国便宜 就入了一只小包 之前笔记中有分享过的 感兴趣的可以去看看 除了逛街 还去了皇家马德里足球主场 买了参观票 一张25欧的样子 原本还觉得就看个球场票价好贵 但是真正进去了 你就会觉得西班牙人民真的很实在 让你从上到下每个角度都观看一下球场 还会参观各种奖杯展览馆 球队历史介绍 以及球员入场会经过的通道和他们用过的洗漱间 完全零距离接触和感受 [吧唧R]\n因为马德里就呆了一天 其他景点也没有去 不过看攻略里说马德里皇宫和丽池公园都是挺值得去的 大家感兴趣可以做参考\n之后去了马德里-塞维利亚 火车路程两小时左右 入住的酒店：\n塞维利亚唐帕酒店(Hotel Don Paco Sevilla)（一晚1600人民币）\n地址（Address):\tPLAZA PADRE JERONIMO DE CORDOBA, 4,老城区,塞维利亚,安达卢西亚,41003,西班牙( PLAZA PADRE JERONIMO DE CORDOBA, 4,Casco Antiguo,Sevilla,Andalucía,41003,Spain)\n电话（Tel):\t0034-95-450 6999\n处于比较热闹的地段 但是附近建筑都偏陈旧 运气很好 当天到达就遇到酒店楼下在举行塞维利亚的圣节（holy week）这也是问酒店reception的小哥得知的 他还一脸你们竟然不知道的震惊表情 所有当地人都跟随游行团队静静注视 很隆重 因此 很多交通都被限制了 我们打车到酒店附近的一条街就下车步行了 [扶墙R] 塞维利亚主要去参观了西班牙广场 以及在去寻觅花朵冰淇淋Amorino 在大教堂边上 但是卖完了🤣 至于西班牙广场还是比较值得一去的 很有西班牙的风味 建筑设计都很有特色 还有随处可见的另一种交通工具 马车 不会妨碍交通 已经完全融入其中\n最后就要强烈推荐西班牙的Ibiza岛屿 塞尔维亚➡️伊比萨 飞机一个多小时到达 入住酒店 强烈推荐：sud ibiza suites 差不多2000rmb一晚 机场打车过去15-20分钟左右 很快 酒店很新 设施齐全 位于海边 风景极佳 房间超大超棒 有阳台 有小客厅 还有一个mini厨房 浴室还有备牙刷 一般欧洲酒店很少会有备一次性牙刷 这个很赞 酒店楼下沿海就是一排各式各样的餐厅 西餐中餐日料 应有尽有 挑你最爱[赞R][赞R][赞R] 酒店唯一的缺陷就是没有提供早餐 不过他有推荐附近的餐厅吃早餐 享有特殊折扣 ibiza很少有见亚洲人 几乎是欧洲人的度假胜地 当地最出名的就是晚上的夜生活 各种各样的club 各种百大DJ在里面打盘带你high 第一晚 我们去了reception小哥推荐最有名的pacha club 门票50欧一人 含一杯酒 这些夜店几乎都是12点以后开门 1-2点都是热场 之后才是真正的开始 [得意R] 不过现在的我处于老年体质 玩到一半就困了 扛不住了 然后在凌晨三点左右就回家了 太累了 感觉屁股和腰扭到抽筋 第二天睡到自然醒 我们乘着渡轮去了旁边的小岛formentera 大概三十分钟 之后可以直接打的去那里最出名的粉色沙滩 但我们一行人作死 一定要租自行车骑环岛 遇到个上坡 差点没把我老命搭上 在太阳的暴晒下 骑了一个小时还没到 我们决定撤回 打车去 😂 幸运的是还好回头打车 因为后来发现我们骑自行车骑错了方向 真的大写的雷[笑哭R][笑哭R][笑哭R] 到了粉色沙滩 一切真的美得跟画一样 虽然粉色沙滩并没有明显的粉色 但是并不妨碍你观赏美景 在海边玩耍 formentera是个还未被完全开发的岛屿 所以里面的景色都是纯天然的 玩累了去边上的餐厅点杯喝的 吃个蛋糕 大大的满足[萌萌哒R][萌萌哒R][萌萌哒R] 回酒店后 同行的小伙伴租了车带我们去兜风买吃的 回酒店后集聚在一个房间客厅玩游戏 这样的度假生活真的太享受 有点不想回英国啦 岛屿不大 我们到处游逛的时候就把很多景点在无意中逛了个遍 ibiza大致给我一种当初去希腊圣托里尼的感觉 都是白白的房子 慢节奏的度假生活 超级棒 [赞R][赞R]\n这次的分享写得实实在在 希望大家喜欢 记得点赞和关注哦 此视频也有分享到我的微博 感兴趣的记得关注徐不圆Maggie哦[害羞R]\n#西班牙旅行攻略[话题]##欧洲旅行攻略[话题]##小长假怎么玩[话题]##小长假去哪儿[话题]##带着小红书去旅行[话题]#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/FiBDQCW6oGM1T7F-1ujK0UR6tK_Z_compress_L1',
    'video_id': '58fb5662d1d3b91ef0c03a70',
    'title': '萌犬的日常😶',
    'video_tag_list': '我和宠物的日常',
    'content': '最近一直没时间拍健身的东西，争取下周末拍一组出来！先透剧一下🙊 也许会是海滩，比基尼题材哦。如果大家喜欢健身，来我主页，里面很多健身视频。\n今天就跟大家分享一下我家米宝吧！😛\n平时没事的话我就会带她出去玩。昨天早上带她去球场看训练，下午回家睡好觉带她去荡秋千，看起来挺开心的。\n#我和宠物的日常[话题]##我家宠物最萌的瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liPpgaF-dWWySfqldyqaqO__GmFx_compress_L1',
    'video_id': '58fb94cad2c8a51e31c2815c',
    'title': '金毛三木木',
    'video_tag_list': '',
    'content': '我们全名叫三木小娇娇帅宝宝咩咩[偷笑R]\n这毛发～亮瞎了麻麻的眼😍'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvOsXMB5Bo_oDRxbn-RpSFcIW88d_compress_L1',
    'video_id': '58fb94fcd2c8a51e31c2815f',
    'title': '猫奴的日常✔️',
    'video_tag_list': '我和宠物的日常',
    'content': '#我家宠物最萌的瞬间[话题]##我和宠物的日常[话题]#\nwuli seren的宝贝已经长大会跑啦。\n昨天写了一大堆内容结果没保存闪退了，今天只好来重写一篇，最近有很多宠友来问我幼猫的饲养问题，正好借这个机会来科普一下幼猫的成长和发育当中需要注意的事项。\n最近红书有人不正当的传播了错误的知识，比如把薮猫的后代说是萨凡纳，把美国猫舍正在繁育的狞猫和家猫的后代F1基础猫卡拉猫说成是宠物猫。在这里我希望红书能够正确的筛选帖子，不要误导宠物家庭和消费者。我也来正确的做一下简单的科普：\n（F1在我们繁育中称为基础猫，基础猫是指猫科野生动物和家猫交配生下来的第一代，我们称为F1基础猫，它并不是被认证的宠物猫。薮猫，狞猫，包括我们孟加拉豹猫的祖先亚洲豹猫，这些都是需要合法的野生动物许可证才能饲养的野生动物，而且国内规定，家庭或个人饲养野生动物，入关前就需要做去爪手术，就是把指甲去掉，这是极其痛苦和残忍的，望大家周知。F1就是第一代基础猫，一般具有80%的野生动物基因，只有F1之后到F4，也就是第四代基础猫，把野生动物的基因通过一代代的稀释到了25%左右，从第五代F5开始有了一个健康并且合格的种群，通过专业的品种猫协会（例如TICA，CFA）的品种委员会成员一致许可，才能认定其为一个新的有血统的正规的宠物猫品种。这就是为什么正规猫舍繁育出来的小猫是具有证书，并且能够查到前五代及以上的血统的，类似我们说的家谱！）\n科普结束，下面来说一下幼猫饲养的知识和注意点：\n首先母猫怀孕周期是63天，但是从受孕开始，母体的饲养环境就需要一定安静且安全的空间，小猫的胚胎在母猫体内23天起，就会模拟未来的生存环境，会在母体内学习奔跑，挥爪等动作，甚至还会相互用头部顶撞哈哈，所以母体相对安全的环境会幼猫从小的性格培养，也具有一定的影响哦！\n而研究表明，位于两个雄性胚胎当中的雌性胚胎，会相较其他雌性来的好斗，因为激素的原因所导致的，所以很多宠友一直会来问我：老黄我的猫脾气不好，请问有什么办法可以让它好相处一点吗？想要改善这种问题也不是没有办法的，答案是：每天陪它玩耍一小时以上，玩到它累，然后抚摸它，这时候的猫咪会比较信任你，从而能够和你建立一种平衡的关系。\n再回到幼猫的饲养，幼猫从出生开始是又聋又哑的，所以它通过气味来寻找猫妈妈的乳头来吸食乳汁，这时候母体消耗的营养是非常大的，母性强的猫妈妈会把自己的营养都给小猫，所以这一时期的猫妈妈需要补充更多的营养成分，例如羊奶粉，液体钙，都是很好的针对哺乳期的母猫补充营养的保健品。\n而幼猫12天睁眼开始，它就开始学习模仿猫妈妈的所有行为，包括学习捕猎技巧，这种行为在流浪猫身上体现的更多，所以流浪猫很多性格比较烈，这和在野外生存有一定的关系。同样的，也再一次提到小猫性格养成的关键：母体的饲养和哺乳环境。\n如果母体的生存环境向来是安全的，那么小猫的性格也会通过遗传，一直保持一种稳定的状态。在繁育中，公猫影响着小猫的骨量和体型，而母猫的毛色，和头版包括性格，能一定的综合和改良基因，这也就是为什么我们通常说要在正规猫舍购买幼猫的原因：一来血统能够保证基因，二来先天的母体饲养条件就比较安全，性格也比较亲人。基本上爸爸妈妈，甚至爷爷奶奶都是从小养到大的，是一个完整的种群。而世界名猫协会TICA规定：为了保障母体的健康，两年只能生育三胎小猫。不可频繁繁殖，而是健康繁育！\n40天开始，幼猫进入离乳期，开始断奶进食幼猫猫粮，而从这一天一直到60天，意味着母体抗体也渐渐减弱，所以到60天断奶，我们的小猫如果吃喝拉撒一切正常，例如自主进食，大便成条，健健康康，基本在70天左右，我们就可以人工注射疫苗，产生抗体来保证免受病毒，同时也必须驱虫，保证体内体外健康。\n同时，疫苗分别注射两针，第一针和第二针之间间隔是15天，而疫苗在体内生成抗体也需要15天左右。所以整个周期为30天，也就是一个月。这就是另一个为什么正规猫舍的小猫基本在3个半月左右才会去新家的原因。而好的负责任的猫舍，还会在幼猫3个半月左右，去正规的医院进行一个抗体滴度测试，来测试幼猫体内的抗体水准，如果某一项薄弱，我们则需要再补一针哟！大家不要以为疫苗注射了就都能产生抗体，这是错误的观念。因为我们注射疫苗不是一个形式，而是正儿八经的要为了小猫的健康考虑，做到最好的保障，\n以上就是我们的幼猫从出生到三个半月的所有健康科学的饲养方法，然后从小猫3个月开始，我们就可以给他们补充发育宝粉和它成长所需要的成长营养粉，比如氨基酸牛磺酸等。有些宠友说自己猫掉毛严重，这就是缺少牛磺酸呀！！！\n另外小猫4个月左右开始换牙，注意不要让小猫吃不干净的东西，以防它生口炎哟！\n最后，所有的猫咪都必须3个月体内体外驱虫，一年一次疫苗，不要觉得成年猫抵抗力好就不会传染到猫瘟鼻支哦，为了爱猫的健康，一定要做好它们的保护措施！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ll6ZUDvGpFcKDxra2YDBRZTdzoXN_compress_L1',
    'video_id': '58fbabd614de4176fe965449',
    'title': 'Jenny厨房“夏日糖水”之雪莲桃胶炖雪梨（详细视频&步骤）',
    'video_tag_list': '美食才是人生主角',
    'content': 'Jimmy最近咳嗽，所以做了这个糖水。\n#美食才是人生主角[话题]#\n用到的东西很简单，皂角米，桃胶，枸杞，红枣，丑耳，雪梨，冰糖，还有陶瓷锅。\n哦对了，桃胶的名字很好听，叫桃花泪。\n当然雪梨也可以换成苹果或者其他水果。桃胶也可以换成燕窝。\n步骤\n✅皂角米，桃胶提前12小时泡发\n✅丑耳提前30分钟洗净泡发，剪去根部\n✅把皂角米，桃胶，丑耳放入陶瓷锅加入水大火转小火炖1小时左右，我炖的时间稍加长了一点\n✅加入红枣，雪梨，枸杞，冰糖，中火或者小火继续炖煮，直到冰糖融化，差不多就可以了\n最后，可以加入牛奶或者椰浆服用，根据个人口味还可以再添加蜂蜜或者糖。\n很粘稠，喝完嘴巴都黏黏的，并且很爽，哈哈哈哈哈哈哈。\n这个比较有润肤的功效哦，适合全家享用，不过孕妇能否喝，这个不是很清楚。\n炒鸡简单的糖水，只不过时间稍微长了一点。\n😘'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/luCMroe-xA4bGiQCfSF0By7wcF4u_compress_L1',
    'video_id': '58fbe38814de412d3e8c8366',
    'title': '上海老面馆 米道老灵额',
    'video_tag_list': '上海;今天吃什么',
    'content': '#我爱吃面[话题]##用视频记录美食[话题]#\n今日天气晴朗，风和日丽，适宜外出散步，跟着 @史小姐-Stella 来探店吃了外貌低调，但味道惊艳的上海老面馆。\n招牌黄鱼煨面，推荐指数🌟🌟🌟🌟🌟\n汤底非常浓，不觉得像是用浓汤宝熬出来的，喝出了诚意。黄鱼也是煮到入口即化啦，想起了当年刚刚登陆魔都的家有好面黄鱼面，不过现在似乎flop了[瞌睡]\n炸猪排 推荐指数🌟🌟🌟🌟\n炸猪排淋酱油，好吃。[少女心]\n据说大肠面也好吃，下次要去试～\n#今天吃什么[话题]##午饭吃什么[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvgcHB_Dt0-eiV0y_-OfTatVvu2K_compress_L1',
    'video_id': '58fbf69c14de4155c08c8367',
    'title': '胖Q的假期🐴',
    'video_tag_list': '',
    'content': '很久没和胖Q这样粘在一起了👅'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltuydPngE_2ca6kPnvtFaxVylQmc_compress_L1',
    'video_id': '58fc0b35b46c5d431d4ba29b',
    'title': '自弹自唱小鲜肉',
    'video_tag_list': '',
    'content': '我喜欢宝宝能有音乐细胞！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/fc373d21e839f67e766f1a65ffe016f21ffeaf31_r_ln',
    'video_id': '58fc54f33460945b7bf5ffd8',
    'title': '视频🎬 | 北京的女孩子们，是如何好好生活的？',
    'video_tag_list': '',
    'content': '周一又要来了！薯队长给你打鸡血的星期天故事会又到了，小板凳和掌声准备好了吗？\n这一次，队长的好战友@小红薯档案馆 出发去了北京，认识了3个在北京奋斗、打拼的小红薯，在她们身上看到，一个人在大都市生活，经营自己的小生活也可以很美好。\n小个子的幼儿园老师丁丁，心里积蓄着巨大的能量，她在小红书里看到了不一样的世界，从她的收藏夹、心愿单一个个变成现实。她坚持通过自己的努力去看到更美好的世界\n坚强独立的@L姐姐，再忙再累也会好好宠爱自己，生活里的磨练、打击都将成为她人生的奖励。她坚持给自己最好的宠爱，从第一瓶胶原蛋白开始。\n经营生活的@小倩老师永远大一，她说：“我的房子是租来的，但我没有一天不认为它是我的家。”她坚持生活得精致，就是给自己最大的尊重。\n这些小红薯们不约而同所坚持的，正是对她们而言最美好的人生规划。\n你在向往着什么？你又在坚持着什么？\n如果你也想你认真生活的故事被更多人听见，如果你也想分享你的快乐和努力，加入#小红薯档案馆[话题]# 吧！\n这里搜集每一个小红薯的真实故事，下一个可能就是你哦！\n对了！号召大家都去关注@小红薯档案馆 哦！\n明天又是继续打拼的新一周～春暖花开～队长爱你～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lui8rBrpsE0zeVzX1BUiWYqInYmo_compress_L1',
    'video_id': '58fc81b3d1d3b955d7d6c618',
    'title': '臀部训练动作（有一定训练基础的初级健身者）',
    'video_tag_list': '见人不如健身',
    'content': '#必须要安利的健身动作[话题]#\n臀部训练动作来啦！\n我是来兑现承诺的\n今天录的相对较简单但是做好了感觉超好的几个动作（动作太多太多、从简单的开始）\n我一直提倡科学健身、所谓科学健身第一就是得保证安全 其次是动作的合理性！\n训练动作成千上万、看别人做的很炫酷的、不一定适合自己、因为每个人的运动表现和体质都不一样、我们要做最适合自己的动作、出汗不是目的，也不能说明减脂效果、最最重要的是肌肉能找到收缩感！\n很多初级健身者都会羡慕那些已经健身很久的高手、觉得她们做的很炫酷感觉很嗨很有效果、当自己尝试的时候发现根本不像看见的那么轻松，做起来很吃力，根本无法完成、甚至是第二天会关节疼痛身上各种不舒服！[笑哭R][笑哭R][笑哭R][笑哭R]\n我相信这些大家都多少有过、说这些不是为了打击大家、是为了严肃的提醒大家一定要注意安全、安全第一、效果第二！\n例如我去年夜跑不长眼、一脚踩坑里把半月板撕裂了、一个不留神，真是肠子都悔青了啊[哭惹R][哭惹R][哭惹R]\n所以大家都要引以为戒、一定不要极端、慢慢来！\n视频是针对有一定健身基础的人（至少最起码的动作模式要会、肌肉会发力）\n整个训练的顺序是目前相对最科学最安全的流程：\n分别是：\nStep1:目标肌肉的筋膜放松\nStep2:全身关节肌肉的动态拉伸\nStep3:全身有氧热身，提高体温\nStep4:目标肌肉激活\nStep5:正式训练\nStep6:对应肌肉的拉伸放松\n动作一要点[得意R][得意R][得意R]\n泡沫轴（筋膜放松球，花生球等）对臀部做放松、时间不能太短、每侧最少3分钟）\n臀部靠上的地方（臀中小肌）坐压在泡沫轴上\n身体重心放一侧倾斜、来回小幅度滚动\n放松哪一侧哪侧的腿翘起来放在另一条腿上面\n动作二要点[得意R][得意R][得意R]\n动态伸展、活动肩关节和髋关节，拉伸后侧肌肉，避免训练中因身体僵硬导致活动受限\n两侧交替进行\n前面的腿伸直并勾脚尖、后侧的腿下去的时候微微屈膝、背打直、手顺着身体两侧由髋关节滑至脚踝、重复进行/\n注意,前面的腿确保伸直、背打直\n下去的时候整个大腿后侧会感觉到明显的拉伸感（柔韧性差的人到这儿会表示很痛苦）\n后背肌肉力量弱的人、下去的时候会发现背很难打直（平时久坐的人最明显）\n骨盆前倾的人，平时腰容易酸疼的人、下去的时候会觉得腰很酸，但是又很舒服\n圆肩驼背的人，肩关节不灵活的人、起来的时候，手没办法并在一起伸展至头顶上方（就是手上不去）\n是不是看似简单的动作，做起来好费劲、还规矩这么多？？？\n是不是我说的这些情况你多少都有点？\n大家不要着急、慢慢来、这是一个很好的动作、只要有空都可以做、15-20次一组、可以用来训练前的热身、也可以当作柔韧性训练、特别是柔韧性不好、身体僵硬的人、多练习这个、对于提高运动表现有很好的效果！\n动作三要点[得意R][得意R][得意R]\n有氧热身、跑步机、划船机、滑雪肌、椭圆机等等都可以、\n5-10分钟即可，确保全身热起来！\n动作四要点[得意R][得意R][得意R]\n臀部的激活、确保正式训练的时候臀部肌肉充分发力\n第一个激活是普拉提的蚌式（保证身体侧向躺稳，核心收紧、用臀部深层肌肉（臀中小肌、梨状肌）发力带动大腿往外打开、动作要慢、不要用惯性！\n往上打开的时候呼气、还原下来的时候吸气\n做到臀部特别特别酸为止～\n第二个激活动作是俯卧Y字训练（俯卧位、收核心、两腿分开、屈膝、脚后跟靠一起、勾脚尖、臀部用力往上抬起臀部）\n动作要慢、上去呼气，下来吸气、不用抬太高，髋关节能离开地面就可以、做到臀部酸到不行为止\n这个动作大腿后侧的膕绳肌也会有感觉、但是注意力要尽量放在臀部、让臀部多找感觉\n正式训练分别是：\n杯式深蹲[赞R]\n（负重按照自己的能力选择合适的、力量弱的可以从徒手开始、力量强一点的可以把手上的负重换成合适重量的壶铃、哑铃、杠铃、Vipr等）\n双腿分开略比髋关节宽一点、脚尖向外打开约45度角、收核心、背部打直、屈髋屈膝下蹲、下蹲过程脚尖和膝盖必须在一个方向、切忌不要膝盖内扣和外翻、下蹲的时候膝盖尽量在脚尖内\n下蹲吸气、蹲起呼气\n15-25次/组  3-6组\n弓箭步蹲[赞R]\n（可以原地、也可以做动态的走起来、前面的腿下蹲的时候屈膝90度、不要往脚尖外顶！背打直、下蹲的时候把身体重心往前倾、屈髋作主导、起来的时候臀部和大腿共同发力（常规的弓步蹲身体重心不用往前、保持直立就可以、我为了减少大腿股四头肌和参与、特意把重心向前了、这样起来的时候臀部的感觉更好）\n大家根据自己的情况去做角度和重心的调整、总之要确保自己能驾驭、能找到发力感\n吸气下蹲、呼气蹲起\n每侧15-25次/组\n3-6组\n原地的做好了再进阶到动态走动的版本！\n壶铃硬拉[赞R]\n（复合动作里最重要最重要的一个动作、也是练就好臀好腿好背的绝佳动作）\n硬拉对于激活训练我们后侧链肌群绝对是立竿见影、久坐、后背力量弱、圆肩驼背、臀部扁平的人群应该把硬拉早日提上日程、练腿、练背、练臀的时候都可以加入硬拉的训练\n今天用壶铃做的屈腿硬拉（硬拉的方式有很多种、后期会慢慢讲）（负重也可以换成哑铃 杠铃 vipr 绳索 杠铃片等）\n注意以下的重点：双脚分开略比肩宽、、核心收紧、背部始终打直、屈髋微微屈膝、臀部先往后走、壶铃垂直下放到两脚足弓之间的连线中间、呼气收核心臀部主动发力伸髋拉起壶铃至身体站直、臀部夹紧、重复动作15-20次\n下放吸气、呼气拉起\n15-20次/组 3-6组\n重量根据个人能力合理安排、不可盲目追求大重量！\n（重中之重、核心收紧、背部挺直、屈髋伸髋为主导、膝盖不可往前屈太多）\n单侧屈髋[赞R]\n这个动作也可以放在硬拉前面做、虽然是徒手动作、但是核心稳定性差的人也不太容易做好、平时在家在办公室可以利用休息时间做几组、能缓解身体的僵硬！\n注意：同样背部打直、臀部先往后推再自然微屈膝、收核心、重心放在前侧的支撑腿和臀、脚尖冲正前方、膝盖和脚尖一致、臀部主动发力带动伸髋起来\n15-20次/组\n3-6组\n壶铃摇摆[赞R]\n这个放在最后收尾、整个臀部、大腿后侧、大腿前侧、核心、心肺都全面参与！心率会很快提升、屁股也会很酸、柔韧性不好的人大腿后侧会拉伸得比较有感觉、这个是个功能性的训练动作、对加强后侧链有很明显的效果、关键减脂效果也是数一数二的[赞R][赞R][赞R]\n注意⚠️ 背一定要打直打直、核心一定要收收收、手放松、不要紧拽壶铃、勾住就可以、屈膝不可太多\n吸气下 呼气起～\n20-30个/组\n3-6组\n或者定一个个数的目标、尽力去完成✅\n（例如、目标200个壶铃摇摆、尽力做、做到做不动、臀部酸到不行就停下来休息一下再接着做、直到做完200个、给自己记下总耗时、下次再做同样的个数、努力把时间缩短）\n练就不要忘记拉伸放松😊😊\n第一个拉伸动作：拉伸髂腰肌、膝盖落地、把大腿和骨盆往下压一下、力气不用太大、一般人都会很有感觉（保持15-25秒）\n接着把小腿往大腿后侧方向压、充分拉伸大腿前侧股四头肌、（保持15-25秒）\n第二个拉伸动作：拉伸大腿后侧、一条腿绕道另一条腿前侧、微屈、后面的腿伸直、手向下去触摸地面（保持15-25秒）\n第三个拉伸动作：臀部拉伸、坐在垫子上、前侧腿屈膝90度、后侧自然打直、手重叠往前推、尽量往地面贴\n保持15-25秒\n所有单侧动作都是两侧交替进行～\n如果时间允许的话、建议把刚开始的泡沫轴筋膜放松再做一遍会更好！\n总之不要忽视拉伸和放松😌\n一个强有力的臀部、不仅仅是为了性感好看、它是髋关节最重要的肌肉、臀部肌肉有力能很好的稳定住骨盆、骨盆只是不正了、腰椎颈椎都会跟着歪、整个人的体态就会不好、身上也就跟着各种疼！\n为了好体态 美臀 身体健康加油练臀吧[得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R]\n之后会陆续更新中级 高级臀部动作！\n有不明白的地方大家留言问我～\n明天更新一套拉伸放松动作、需要的宝宝可以关注一下！\n#厉害了我的健身房[话题]##见人不如健身[话题]##健身是把整容刀[话题]##健身穿什么[话题]##健身靠装备[话题]##举铁P.K.瑜伽[话题]##必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg1Mf2q5I15rQngqDskSyM1kMFuF_compress_L1',
    'video_id': '58fcb8dbd2c8a55815c2814e',
    'title': '东京Day2',
    'video_tag_list': '',
    'content': '昨天到东京在下雨，今天就放晴啦！浅草人虽然多还是来打了个卡。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqR9hB71vkjrj2z1tilCKd-M1EBJ_compress_L1',
    'video_id': '58fcc8b214de4161aa8c8365',
    'title': '现场版林宥嘉-《成全》',
    'video_tag_list': '去听一场演唱会',
    'content': '全世界第三爱的男人。#去听一场演唱会[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhEy8R2tTjbSFb7kVI0emPtTEHNe_compress_L1',
    'video_id': '58fccd51b46c5d5fcf4ba295',
    'title': '布偶布偶小布偶',
    'video_tag_list': '',
    'content': '给二儿子洗白白，这么乖的喵回家有罐头吃！么么帅儿子！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/9481488f-5cea65d-9bcd-959462e88885?sign=9a939c8dfcd1528ad0ef03ec587ab452&t=65fb06d4',
    'video_id': '58fd41fa7fc5b866e476c3c1',
    'title': '【手把手教你如何护发➕造型👸】 附demo~',
    'video_tag_list': '我的护发秘籍;沙宣',
    'content': '一直follow我的小伙伴都知道我对头发很舍得下功夫，之前分享的护发秘籍反响也hin好，所以呢~这次就让我来跟大家分享一下我近期爱用滴护发➕造型品✌️\n讲真，我超舍得在头发上花钱，这些年下来所有叫得出名字的中高端洗护发和造型品都用过，但是呢，不是每个人都愿意在头发上花这么多钱，再加上我后来回国了很多东西没那么好买了...所以呢，我就开始尝试一些既容易买到、价格又相对亲民的护发和造型品~\n☝️用了一些之后发现...【高手在民间】这句话不是瞎说的，真的不一定越贵就越好，hin多平价品也很好用的。比如沙宣的这几样营养喷雾、精油和弹力素，每瓶都是100ml的容量，价格也就50+这样，真的很划算，使用感也很好，关键是绝大多数人都消费得起！\n☝️为了让大家看的更清楚明了，我给大家录了个demo小视频，顺便教大家如何打理洗后的头发，以及使用弹力素来造型~视频总比图片来的更生动，对不对呀？😁\n好了，更多内容就看视频吧！\n.\n以上，感谢观看，欢迎关注😘\n#我的护发秘籍[话题]##拯救细软发大作战[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/1bf9ea603933222e08fb74698da4318272a010eb_v1',
    'video_id': '58fd6deed1d3b91763c03a7e',
    'title': '谁说厨神才会做，2分钟学会这道花开富贵鱼！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n\u200b花开富贵我中国传统吉祥图案之一，代表了人们对美满幸福生活、富有和高贵的向往。\n这花开富贵鱼不是只有两个美好的寓意这么简单，拌着鲜美的汤汁，和这么华丽的造型做映衬，绝对算的上色、香、味俱全的美食!\n★★★★★\n创意指数\n花开富贵鱼\n▼\n花开富贵鱼\n·视频音乐·\nEliane - Raindrops\n·食材·\n鳊鱼、圣女果\n洋葱、青椒、红椒、姜\n料酒、蚝油、胡椒\n蒸鱼豉油、糖、盐\n1.切去鱼头鱼尾\n2.鱼腹处刺开，以便于造型\n3.用剪刀剪去鱼鳍\n4.从鱼背入刀，均匀切片，保留腹部不切断\n5.姜切丝、青红椒切丁、洋葱切丁备用\n6.倒入0.5茶匙盐、料酒2茶匙、蚝油3茶匙、蒸鱼豉油4茶匙、白砂糖2茶匙、胡椒粉1茶匙、清水200ml\n7.均匀搅拌备用\n8.热油锅倒入洋葱\n9.炒出香味后倒入青红椒丁\n10.清炒片刻倒入调料汁\n11.煮沸盛出备用\n12.姜丝铺底\n13.将鱼平铺成圆形，鱼头放入圣女果点缀\n14.水开后移入蒸锅，蒸至10分钟鱼眼突出\n15.将汤水控出\n16.淋上调至好的酱汁\n17.周末用这道菜去征服你的家人吧~！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhegKcxm4_qEHWxWux7eHdRwzPtP_compress_L1',
    'video_id': '58fd7de314de41440f96544b',
    'title': '手机摄影爱好者才知道的神器',
    'video_tag_list': '手机摄影好用利器;摩米士 momax 精英手机三脚架',
    'content': '“手机如何拍夜景？”\n“手机怎么拍长曝？”\n“夜晚拍照容易糊怎么办？”\n“拍照时手拿不稳怎么办？”\n“为什么我的手机拍不出漂亮的星空”\n.......\n小摩的回答\n“首先你要有个三脚架"\n很多人一副韩红听了要打人的表情\n“excuse me??? 我用手机拍照就是图个方便，你现在要我备个三脚架”\n但是有了三脚架在夜景、长曝、运动物体以及长焦拍摄时确实能带来很好的成片效果\n一般的手机三脚架都是桌面脚架，高度低，角度少，应付个普通场景还行，但如果想像相机那样拍摄夜景、长曝光，高度肯定是不够的。如果用高一些的专业脚架，虽然拍摄起来方便，但操作复杂，携带不便，跟手机摄影的初衷相违背。\n😊这一次，我们对三角架进行了重新打造，融合了手机脚架和相机脚架的特点，脚架展开的工作高度在1.3米左右，360°全景云台可以最大限度的保证拍摄角度，完全是相机的Style。同时新增自拍杆功能，取出中轴连接手机夹即变身自拍杆。\n算上云台，收拢后也只有28.3cm长度，0.86kg，不论是手拿还是放在包里，都非常方便。不过对于这样的三脚架，只架一个手机好像有点大材小用[汗颜R]。\n没错！\n她的最大承重2.5kg，架单反、GoPro运动相机、麦克风、自拍杆等设备都没问题！\n有了这个脚架，手机就可以拍延时了，棒棒哒~\n\n#手机摄影好用利器[话题]#\n#新品抢首发[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/ddb6afc2-4b8a187-87b3-84a850787a32?sign=6d8015e28668bf01d5fc95546691c8cd&t=65fb06d4',
    'video_id': '58fdbb327fc5b861e2bb383c',
    'title': '维密女神的美腿塑形训练',
    'video_tag_list': '',
    'content': '又到了穿裙子短裤露腿的季节了，腿部有赘肉怎么行！跟着这套腿部塑形教程一起练起来吧，消除腿部肥肉，练出一双大长腿！更丰富更完整的训练计划欢迎下载「火辣健身app」，或者微信关注「火辣健身」。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/f1d06d547bb85d4437779a353945f2eab28b4f54_r_ln',
    'video_id': '58fdc93fb46c5d2305ac805d',
    'title': '香水特辑分享#Rita聊天室#香水#视频',
    'video_tag_list': '这支香水最性感',
    'content': '被催了很久的香水分享哈哈希望你们会喜欢啦～\n视频背景音乐是 Aimee Allen 唱的《La La Land》\n上衣是：Self Portrait /墨镜很久前买的\n香水依次是：\nTomFord Jasmine Rouge （茉莉花味）\nTomFord Cafe Rose （六神花露水高级高配版）\nTomFord Oud Wood （性冷淡风烟熏木香味）\nTomFord Soleil Blanc （白色奶油淡香，包装满分）\nNarciso Rodriguez For Her (粉色包装，淡淡石榴香）\n(Maison Martin Margiela) Replica Tea Escape(绿茶味)\nMiumiu 红头包装香水 （包装可爱满分，香味浓郁）\n法国工厂自制香水 Fragonard （味道自选）\nMarc Jacobs Daisy (雏菊系列四瓶装，适合出门旅游携带）\n香水的依次名字我已经分享在这笔记里啦，希望你们喜欢啦：） 记得点赞么么哒😘\n#春夏香水种草[话题]##这支香水最性感[话题]##香水瓶也有高颜值[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/ea45317c-2f14271-bf38-728c1508f9b0?sign=dcbe49ee87a0c19a1400cc14b5050b4e&t=65fb06d4',
    'video_id': '58fdca4d7fc5b848e1ade7bb',
    'title': '没想到洗鞋原来这么轻松，后悔这么晚才知道',
    'video_tag_list': '视频教你生活小窍门',
    'content': '鞋子穿久了容易脏，特别是小白鞋，脏的快，被别人一不小心踩了一脚马上就留痕迹了。看着鞋子脏心里也难受，可是洗鞋这件事，光是想想就觉得很麻烦！今天喵酱就来教大家一个超简单的方法——用身边的牙膏君，就可以很轻松地刷下污渍，让你以后再也不怕洗鞋啦！#视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/fb9f05d8c5443990e467bc64fcf694d8b7f1c0cc_r_ln',
    'video_id': '58fdce92d2c8a552a8cd533c',
    'title': '',
    'video_tag_list': '',
    'content': '练出蜜桃臀🍑 4个动作臀腿塑形，负重训练一起练翘臀✌️\n感受臀部发力，注意力在屁股这里[得意]心中默念：我要翘臀\xa0要翘臀 要翘臀！\n练臀4个经典动作，同样可以练到臀部的动作千千万，[得意]今天和大家分享分享4个经典动作：\n负重硬拉 （5kg）\n器械外展（50kg 左右）\n负重深蹲（5kg）\n箭步蹲\n😘频率：每组15个*4组 \xa0一共4大组 。动作可以交替完成。\n😘【要更有效的蜜桃臀的宝宝】选择负重+臀大肌 +大腿 股四头肌 发力的动作\n【蜜桃臀的养成】女生不用太害怕腿粗哦，没有那么容易粗腿的啦，感受臀部发力，心中默念我要翘臀要翘臀。\n🙈一个立体的翘臀 离不开大腿肌肉的支持，要不要练腿和臀容易粗腿，它会让你臀部更有力。选择负重+臀腿动作，会让效果增加！\n....................................................\n😉具体的臀部教程，在我的上一篇笔记中有哦~\n么么哒，加油！\n健身器械教学视频 无器械锻炼视频 练出翘翘蜜桃臀 见人不如健身 厉害了我的健身房 必须要安利的健身动作'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmQOVIWwSbfdcJ-ZZwVJCNbM0b6w_compress_L1',
    'video_id': '58fde1d7d1d3b9450aa598f5',
    'title': '🎬视频话题：去听一场演唱会',
    'video_tag_list': '去听一场演唱会;去听一场演唱会',
    'content': '“很小的时候，就一直心心念念有一天能去听爱豆的演唱会。后来终于有了这一天，我看到了舞台上光芒万丈的那个人，跟着他唱，跟着他笑。身边的姑娘一直激动到颤栗，我们一起万人大合唱。那一刻我唯一的一个念头，就是喜欢这个人真的是太好了。”\n这一次的视频话题，就来分享最让你感动的演唱会现场吧～说不定能发现一批志同道合的小红薯呢！\n[得意]队长教你怎么参加活动：发视频笔记的时候，在输入框上方，戳表情符号右边的#，就进入话题库啦，输入￼#去听一场演唱会[话题]#就可以参加了呦！\n跟红薯们分享你最爱的演唱会信息，比如【去听了2017上海香蕉计划音乐节，全世界第三爱的林宥嘉唱了《成全》】\n当然啦队长相信迷妹迷弟们的力量！[装酷]\n视频来自 @熊哥痴汉'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljVKY_oggMGfSX4H3Lxe0b7Rgays',
    'video_id': '58fde768b46c5d0882ac8058',
    'title': '泡沫轴肌肉放松/ 想瘦腿想肌肉紧实有力必须做的事！',
    'video_tag_list': '见人不如健身;小红书',
    'content': '除了训练、你还有更重要的事情要做！\n有很多时候你会发现自己下肢很僵硬、总在练也不见瘦、练就了肌肉发力感不好、还会出现各种酸疼不适……\n不是你练得不够、只是你缺少肌肉和筋膜的放松！\n在训练过程中、肌纤维是在不断收缩变短的、经常练又不及时放松拉伸 时间久了肌肉就会越来越紧张僵硬！\n一天将近十个小时的工作基本都是坐着的、很多肌肉更是长期处于紧张状态、长期如此肌肉会变短、不仅会导致活动受限、还很容易受伤[汗颜R][汗颜R][汗颜R]\n这也就是有很多久坐人群在生活中会因为一个很普通很小幅度的动作就会扭伤拉伤等（例如：猛地一扭头看东西、突然去够一个高处的东西、突然起身等）\n就是因为身体太僵硬、紧张长期处于紧张并且无力的状态（这种紧还不是肌肉训练的紧、属于今儿紧而无力）\n肌肉不断缩短而不及时拉长、时间久了肌肉形态也会很难看、没有美感……\n所以总练腿又不拉伸放松腿部肌肉它肯定就看着不会瘦 啦！\n肌肉肌筋膜太紧张僵硬还会阻碍下肢的血液循环、让腿越练越难看、更重要的是、当肌肉长期紧张变短、也会大大的影响训练效果，肌肉找不到发力点，无泵感等等…\n宝宝们都火速行动起来吧……\n充分利用健身房里的放松工具\n实在没办法的可以自己买一个在家里（视频中的泡沫轴和筋膜放松球都可以、很实用、几乎所有部位都能放松到）\n其实不仅仅是训练前后需要放松肌肉、平时在家只要有时间都可以做放松、因为大部分人都是长期久坐的高压工作状态、几乎都会存在因为肌肉紧张而导致的各种腰酸背疼等…\n关键是真的超舒服😌啊！\n最最关键的是能瘦腿啊能瘦腿[赞R][赞R][赞R]\n今天分享的是以下肢为主的部分动作（包含大腿前侧肌肉、大腿内侧肌肉、臀部肌肉、阔筋膜张肌、髂胫束、小腿后侧肌肉、后背上中下段肌肉、颈部肌肉）\n都是平时很容易紧张导致体态出问题的肌肉、一定要多放松！\n之后再给宝宝们分享其他的动作！\n请默默忽略最近因为腿伤体脂率一路飙升的我、直接看动作就好[得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R]\n#健身是把整容刀[话题]#\n#厉害了我的健身房[话题]##见人不如健身[话题]#\n#健身靠装备[话题]##健身穿什么[话题]#\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljWlWGdENQ_fQhsQFBuh-mWI8Y1d_compress_L1',
    'video_id': '58fdeb12d1d3b96441a598f8',
    'title': 'Swarovski金色choker多种戴法分享——哈哈哈哈',
    'video_tag_list': '克罗心;汤姆·福特;迪奥;施华洛世奇',
    'content': 'choker流行很久啦\n\n下课拍了一下几种戴法\n请原谅我的逗逼\n其实穿v领或者衬衫戴更美\n😘\n这个几百块\n但是闪闪闪\n长袖是\n口红是07 Paradiso\n墨镜是'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/d4481699-c003bb9-ac7f-01a522e55b5d?sign=37e2bf8e3859167c83f20c94c1fc4c9c&t=65fb06d4',
    'video_id': '58fdeeaa7fc5b82fa5ade7bb',
    'title': '网红的一日三餐｜亚洲人也可以拥有蜜桃臀训练',
    'video_tag_list': '8周变身比基尼女神',
    'content': '#8周变身比基尼女神[话题]#8周健身小白变身比基尼女神挑战已经过去整整一周啦，\n在这一周里，\n你是否完成全部训练作业并按时打卡了呢？\n你是否已经用白水替代各种含糖饮料，\n用粗粮替代精米精面了呢？\n你是否在点外食的时候开始注意烹饪方法并估算热量摄入了呢？\n如果以上这些你全部都做到了，\n那姑娘，\n快给自己点一个大大的👍，\n相信马上你就可以穿着马甲线过夏天啦！\n如果你刚刚才看到我们的文章和视频，\n那也没关系，\n现在开始一点都不晚，\n还有7周咱们迎头赶上！\n食谱和健身部分的细节请移步同名平台 Fit4Life健身与美食，我们等你哟～\n还有记得@fit4life 打卡哦'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fln9FMIzeDvh-R7uXuZA_WfwZakT_compress_L1',
    'video_id': '58fe0dd3d1d3b96028ded2fa',
    'title': '10秒叠出酒店一样的毛巾',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lmBcphXQdM_w-siasVnwtBYaTZfF_compress_L1',
    'video_id': '58fe0e29d1d3b9618ba598f8',
    'title': '听一场伍佰叔叔的演唱会',
    'video_tag_list': '去听一场演唱会',
    'content': '#去听一场演唱会[话题]#\n哈哈哈哈哈哈哈 有没有伍佰叔叔的歌迷\n我是跟着我家朱哥去的 平时一直听他哼唧哼唧\n现场超嗨的 不愧为摇滚天王!!!\n全场座无虚席 差点没买到票😂\n一起嗨'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/fc9c7d401cc5bce823a2368b7c581b5cb219a014_r',
    'video_id': '58fe0f5114de413a3a9cdcc6',
    'title': '小空间收纳T恤的方法',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/FvAb_wPz7aDqoEt9O-jWBuzWvgXe_compress_L1',
    'video_id': '58fe0faad1d3b9668ba598f5',
    'title': '如何有效收纳袜子并且方便查找',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luITkGEvK54vKje8c0IA5seD0v30_compress_L1',
    'video_id': '58fe1083d1d3b96ac7a598f5',
    'title': '厨房收纳神器之节省空间又美观的调味罐',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loj-oZCqkZs1rCzXTpLEMA_l1S8K_compress_L1',
    'video_id': '58fe1121b46c5d12e34455fe',
    'title': '亲子玩具',
    'video_tag_list': '小月龄宝宝益智玩具;小月龄宝宝益智玩具',
    'content': '玩具名字：猴子游戏。\n红色、黄色猴子各六个，两幅带圆珠的钓竿，玩法请见视频。😂这个玩具锻炼小孩手、眼协调能力的发展，要静下来看清楚才能准确钓上来一个，培养孩子心理素质。\n可以家长宝宝一起比赛有个互动也不错，赶紧试试吧😎😎\n#宝宝早教这么做[话题]# #新款宝宝玩具[话题]#  #小月龄宝宝益智玩具[话题]#\n@薯宝宝'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luHXYWW-p5YSMD-gNuyaVLqnICuN_compress_L1',
    'video_id': '58fe33bed1d3b963fa34a119',
    'title': '值得一再encore的歌神张学友演唱会～',
    'video_tag_list': '去听一场演唱会',
    'content': '#去听一场演唱会[话题]#\n一直想着手机里的视频无用武之地，看到这个话题太棒了！之前和朋友从广州去东莞看张学友的演唱会，真的太值得了！\n从舞美都绚烂到停不下来，加上歌神的实力就不多说了，唱足三个小时，50多岁的人又唱又跳，真的让我肃然起敬。\n我们听张学友的歌长大，很多歌听到都会触动泪点，像这首《你的名字我的姓氏》，不是因为什么感情原因，而是一种成长的回忆，那个时候小时候的我！\n接下来很快中山站开票了，我打算再去encore一次。希望你也喜欢这个经典之作。😛'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljrbOPxKVDxoEAVhH1eQ9i3CGBqu_compress_L1',
    'video_id': '58feafdcd2c8a5434c2858c5',
    'title': '今年成都夏天最火的冰淇淋非她莫属',
    'video_tag_list': '',
    'content': '💥💥美国叠堆冰淇淋，5.1太古里不见不散\n视频不能p，你们将就看看我那张大脸[捂脸]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhz0GbaFM_Jer6vmNqjNE3c7LBmO_compress_L1',
    'video_id': '58fee2b5d1d3b9029d836206',
    'title': '儿子 好想给你生个姐姐 😂',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/7aef371cf166d3c4a28e755391b2e60348265905_r_ln',
    'video_id': '58fee46414de41348a818059',
    'title': '现场版田馥甄-《小幸运》',
    'video_tag_list': '去听一场演唱会',
    'content': '#去听一场演唱会[话题]#\nhebe真是唱功了得，最喜欢小幸运这首歌啦！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/9a86f3b3fefec8532913f75d6266813ba164bf67_v1',
    'video_id': '58ff586f14de41644324617a',
    'title': '学了之后会上瘾的T恤折法！',
    'video_tag_list': '',
    'content': '总说分不清楚正反的亲们，反过来折叠就好了呀[抓狂R]，先从底部开始对折再对折，领口和logo都露在外面[笑哭R][笑哭R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lp7pEdWtCrUARbskkRwxC8TMSbh1_compress_L1',
    'video_id': '58ff61e814de41097e246179',
    'title': '毫无由来的乐',
    'video_tag_list': '',
    'content': '每天这小孩就是各种乐\n早晨起来 睁开俩眼就是乐\n吃饭乐 喝水乐 玩儿起来就乐了\n跟熟悉的人乐 陌生人也乐\n有时 望着某样东西出神 也会呵呵傻乐\n要不是因为有朋友的儿子取名叫乐呵 呵呵 哈哈\n我一定也取个相关小名儿 凸显你的特质'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lm_K7qJI08Ke3-i_L3yclO3GSxnx_compress_L1',
    'video_id': '58fff9b7b46c5d504410e59d',
    'title': '小男孩真的很喜欢的一款二合一滑翔车',
    'video_tag_list': '玩不腻的益智玩具;特宝儿 TOPBRIGHT 二合一滑道赛车',
    'content': '#玩不腻的益智玩具[话题]#我家宝宝的玩具箱里真的囤了一堆的小车车，百玩不厌，不用特别再另外玩点什么，只要拿到车，就能在地上滑啊滚啊玩很久。然后自从上次给他买了个工具台后，发现了他也是真的爱动手，爱敲打。\n现在宝宝两岁生日了，就想给他买个他能喜欢玩的玩具当礼物，很早开始看起了，都没什么特别合适的，直到看见某宝上关注的这家特宝儿玩具店上新了这款敲打台，觉得简直就是量身替我儿子设计的啊。结合了敲打与滑翔车，折叠的时候可以用小锤子敲敲打打，打开来就是一个长轨道，正好用来玩小车。买来儿子简直爱不释手，天天拎着个敲打台，唯一有点不足的就是车子只有一辆，幸好家里小车很多，可以换着来玩滑道车。\n\n我自己也亲自体验示范了下，他就迫不及待的自个拿去玩去了。😂😂😂我想说：儿砸，为娘还没玩够吖～～～～#薯妈必备早教玩具[话题]##新款宝宝玩具[话题]##视频推荐玩具[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lr1QAQrRNcwzSE1-DI4lr2S--Dea_compress_L1',
    'video_id': '59000e9514de411152652b49',
    'title': '山药“冰激凌”吃过吗？1分钟学会最时尚的吃法！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n蓝莓山药，又称蓝莓山药泥，是夏日里既美味又养生，同时又老少皆宜的凉菜，说是凉菜倒是更象饭前甜点，吃起来酸甜可口。\n山药以清蒸最能吃出它的原味。我做的这个蓝莓山药泥，颜色好看，样子很像冰激淋呢，放到冰箱里冰过之后再拿出来吃，相似“蓝莓冰激凌“来了~！\n★★★★★\n创意指数\n蓝莓山药\n▼\n蓝莓山药\n·视频音乐·\nThe Band Perry - If I Die Young\n·食材·\n山药、蓝莓酱\n1.山药洗净去皮\n2.切成条状备用\n3.移入蒸锅\n4.盖上盖子，大火蒸10分钟至山药彻底变软\n5.用勺子碾碎山药成泥状\n6.把山药泥装入裱花袋中\n7.在盘中裱花定型\n8.最后淋上蓝莓酱大功告成\n9.酸甜可口放入冰箱后好似冰激凌呢~！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ll7PoTlvE5AMvFF4Y6AcArKA4qI5_compress_L1',
    'video_id': '59001dafb46c5d60aed934f4',
    'title': "silk'n jewel 视频使用教程来",
    'video_tag_list': "Silk'n",
    'content': '前几天发了一个图文长贴～[吧唧R]\n（想看的往前翻一下我的笔记嘻嘻嘻）[吧唧R][吧唧R]\n前几天用的时候顺带手拍的～比较随意哈哈哈哈[吧唧R][吧唧R][吧唧R]\n希望可以帮助到想要脱毛的婊贝们[吧唧R][吧唧R][吧唧R][吧唧R]\n @薯宝宝'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljVCP9jtmu2y_JjoJB6YENyOHs-c_compress_L1',
    'video_id': '590041c4d1d3b91c681076c8',
    'title': '原来这么多年内衣一直都叠错了？',
    'video_tag_list': '',
    'content': '#视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lk0H9e1FD-l6ejbEbC2U43wceu8m_compress_L1',
    'video_id': '590047d814de416440246179',
    'title': '一条能拉车的苹果数据线👇',
    'video_tag_list': '好用数据线推荐',
    'content': '生活中总有偶尔的“撒野”，比如\n手机电量太少，车子突然出故障了，\n突然想跳绳找不到绳子？\n……\n来来来！解决方案都在这呢~\nMOMAX新款耐用编织线，这是一条能拉车的数据线\n经过史上最严苛的变态测试👏\n3年质保也不是谁都能做到的[得意R]\n等到有一天厌倦它了，想找个理由换掉它，它还完好无损，太过结实耐用也挺烦的！[汗颜R]\n真的感觉这辈子用这一根数据线也就够了。\n#新品抢首发[话题]#\n#好用数据线推荐[话题]#\n#科技拯救世界[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltQQJe5KIcO20ueKEkKQhuj59hLL_compress_L1',
    'video_id': '59007629d2c8a52b848cec0c',
    'title': '[女神经变女神系列化妆教程]适合春夏的橙色系质感妆容 日常妆',
    'video_tag_list': '跟着视频画眼影',
    'content': '视频里用到的：Becca紫色妆前乳、stila遮瑕盘、资生堂遮瑕笔、兰蔻气垫CC霜、Rimmel哑光控油粉饼、Sleek眼影600、SUQQU眼影 02光橙花、植村秀眼线笔、CPB高光、资生堂Pk107、WET N WILD唇线笔、露华浓露小蜜015 、Tarte十色腮红盘NYX定妆喷雾\n#妆前妆后大对比[话题]##新手最容易上手的眼影盘[话题]##我最爱的彩妆品牌[话题]##跟着视频画眼影[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/26156acd-18fb61f-8a65-3790208f3a4c?sign=a0606bf51da5a6532de0abb419e253b4&t=65fb06d4',
    'video_id': '59008871a9b2ed55e26a8264',
    'title': '哑铃讲解全身训练｜如何练出完美比基尼体型',
    'video_tag_list': '8周变身比基尼女神',
    'content': '#8周变身比基尼女神[话题]#想改善体型到底应该练力量还是有氧？为什么我稍微练了下腿，就觉得小腿明显粗了而大腿仍然堆满肥肉？本期视频Giselle和Weiya和你分享：比基尼小姐般小巧紧致的身形是如何练就的？常见的误区有哪些？后半段的视频，就是一个为追求更好线条的女生量身打造的哑铃全身训练（降阶组方式），在健身房和在家随时随地练起来！当然了，最大的惊喜在视频的结尾....\n什么是小巧紧致身形训练？小重量，多组数的力量训练+hiit有氧训练\n什么是小重量？就是每个动作做到15次左右正好力竭的重量\n什么是多组数？12-15次动作一组，做3-4组\n为什么要做hiit? hiit训练是单位时间燃脂效率最高的有氧运动，如果想在短时间内改变体型，这个最适合你啦！\n视频中的哑铃全身训练（降阶组训练方法）\n-为什么设计这个训练？用哑铃这种小重量，然后用降阶组的方法达成肌肉的最大疲劳，可以有效的塑造小巧紧致的肌肉，非常适合女生！\n-器械：如果在健身房就拿3对重量依次减轻的哑铃，如果在家一对哑铃就好啦！\n-训练方法：降阶组的训练方法是用从重到轻的重量连续做一组动作，中间不休息；做完全部的动作之后再组间休息的训练方法\n动作一：哑铃深蹲+箭步蹲 - 24次（每个重量8次）\n动作二：相扑深蹲+二头弯举 - 24次 （每个重量8次）\n动作三：俯卧撑+单手划船 - 24次 （每个重量8次）\n动作四：肩上推举+请安弓箭步 - 24次 （每个重量8次）\n动作五：负重两头起 - 24次 （一个重量就好了）\n今天的作业：视频中哑铃全身训练1-2次。比基尼女神8周挑战刚刚开始，快和闺蜜们一起来参加！持续关注我们，每天@fit4life 运动打卡，八周之后有惊喜！\n还有记得关注我们同名平台 Fit4Life健身与美食'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FsXwlpNVpYOo_5eshVO8TxzoIK8R_compress_L1',
    'video_id': '5900995714de4111b0246179',
    'title': '最新眼妆视频出炉',
    'video_tag_list': '',
    'content': '一款bulingbuling的眼妆\n擅长运用杏色、粉色，红棕，和细闪，和亮闪质地的眼妆产品就可以达到泪目的效果，同时可以让普通的妆容立马灵动起来，肤色偏黄的姑娘们就采用暖色系的眼影可达到更理想的效果'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lq7Vs05GGdZYHNecz-MJ7NIGeSeY_compress_L1',
    'video_id': '59009a8314de41156424617d',
    'title': '〔Americano 美式〕视频系列',
    'video_tag_list': '',
    'content': '2017年 将会 推出 魏小哈 第一个视频系列 "AMERICANO ／ 美式" 因为爱咖啡 因为爱一个人 因为怕寂寞 因为还要等待 因为爱走走走 因为爱穿搭 因为文艺范儿 因为 美 的 方式 所以我因你 而记录\n#不喝咖啡会死星人[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnBY9NcG_GUDrjzJ11w2PvPBrdTv_compress_L1',
    'video_id': '5901523114de412b8ee528af',
    'title': '烤味增牛舌（31）',
    'video_tag_list': '漂洋过海来吃你;悉尼',
    'content': '这是今年春节在悉尼的日本小店买的味增牛舌，碳、炉子烧烤工具小店都有，太阳下面过热春节，安逸嘛！\n#漂洋过海来吃你[话题]# '
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqRlFVDyLTZuaxmqxizexizWdv5b_compress_L1',
    'video_id': '59017034d1d3b94d84a0a4ab',
    'title': '剥个完整的皮皮虾',
    'video_tag_list': '',
    'content': '最爱吃皮皮虾，要想吃个完整的，这个方法还不错！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lj01V4gmuPNhDJ51_IHhgT_ZGubk_compress_L1',
    'video_id': '5901822eb46c5d643630ded5',
    'title': '【Adora干货】黑眼圈遮瑕五步走（详细）',
    'video_tag_list': '专治黑眼圈的遮瑕;贝玲妃 Benefit 节日限量零毛孔底妆;Smashbox  亮肤妆前乳无油清爽型;MILANI 眼部打底膏;纳斯 NARS 妆点甜心遮瑕蜜;Hourglass;RCMA;Hourglass  腮红高光五色限量面部盘;Anastasia 限量四色高光盘;肌肤之钥 clé de Peau Beauté 亮采柔肤粉/立体高光粉;BECCA Shimmering Skin Perfector Pressed 高光粉饼;Wet n Wild 浮雕高光蜜粉饼;纪梵希 Givenchy 17年春夏限定面高光',
    'content': '欠给小仙女们的黑眼圈遮瑕大法来啦😘\n话说这视频拍完了半个月我才剪好😂\n黑眼圈👀的确是困扰我们生活，立马增龄十岁的大扫把星[震惊L]\n除了日常的黑眼圈去除和眼部保养，上妆效果也会大受影响。\n于是在修容遮瑕盘怎么用的视频之后，最多的就是要求将黑眼圈的遮瑕过程po出来喽#专治黑眼圈的遮瑕[话题]#\n[喜欢]\n第一步：打底\n对于干性皮肤，打底是为了让皮肤不那么干燥上妆不会卡粉、积线。\n对于油性混合性皮肤，打底是为了让皮肤更细腻零毛孔，底妆服帖。\n遮瑕顾名思义要遮，遮就是要覆盖，那么一层一层覆盖难免妆感会比无妆要看起来厚啊！但是又不能那么厚重看起来影响心情那么lou。所以要既遮住瑕疵又要清透妆效。\n⚠️于是请切记，每一次遮盖都控制用量到最少，少到你几乎不敢相信[抠鼻]（遮瑕产品质地都比较强遮盖力并有一些厚度或是稠度）只遮盖住即可，不要多多益善。别看就这一个小差别，要不效果差出一个珠穆朗玛峰。[得意]\n我是干性皮肤 极干的眼周皮肤我使用一般打底几乎无感，于是简单粗暴的用了farsali的rose gold 美容精油，这瓶家伙在国外可是火的美妆博主人手一瓶啊！哈哈哈😭\n油性皮肤建议用无油的啫喱或慕斯产品打底比如 反孔精英 油皮的无暇肌肤亲妈\n\n\n等等都可以[得意]\n第二步：颜色修正\n之前给大家做了修容遮瑕盘怎么用视频里的遮瑕修正颜色对照表，绿色——修正泛红\n黄色——修正紫色\n紫色——修正暗黄………那些比较针对脸部肌肤，话说黑眼圈可是个个例，只会更甚不会轻点哦。每个人的黑眼圈颜色都不一样，于是很多小仙女发现，自己的盘子根本应付不来自己的千年熊猫眼🐼\n于是我又出图啦！针对黑眼圈的颜色修正：\n蓝色——用桃色遮瑕遮盖\n紫色——用黄色遮瑕遮盖\n蓝+紫色——用桃色+粉色+黄色遮瑕遮盖\n褐色——橘色遮瑕遮盖\n深褐色或黑色——用红色遮瑕遮盖\n【原理】：当然这个原理如同你要粉刷一面有颜色的墙，直接刷白色你会发现底色会透过白色显现出来的颜色并不会是理想的全白。于是你需要先修色，也就是用其他颜色抵掉原来的颜色，之后再涂上你要的白色，才会有理想效果。\n视频内图十大眼部遮瑕产品：（用这类产品或许第三步就直接略掉好了，二、三都合成一步喽）每个产品细节不展开和翻译 另作下一篇推文介绍哈！记得关注哦！[得意]\n1. Urban Decay 24/7 Concealer Pencil\n2. IT Cosmetics Bye Bye Under Eye（我喜欢啊我喜欢💕）\n3. Make Up For Ever Full Cover Concealer\n4. Smashbox High Definition Concealer\n5. Laura Mercier High Coverage Concealer\n6. Smashbox Camera Ready BB Cream Eyes\n7. Amazing Cosmetics Amazing Concealer\n8. CoverGirl TruBlend Fixstick Concealer\n9. Dermablend Quick Fix Concealer\n10. NYX Dark Circle Concealer\n第三步：遮瑕覆盖\n你可以用你的粉底、遮瑕盘、遮瑕膏、遮瑕液、遮瑕棒…………只要是你想要的肤色🏼即可，用按压式覆盖在修色的上。轻薄！轻薄！轻薄！请掌握好用量。[喜欢]\n很多仙女用比粉底亮一号的遮瑕液来做这步，其实就是为了眼下眼周是需要提亮突出轮廓的，所以这一步也可以选择遮盖与提亮同时实现。\n⚠️：眼下遮瑕提亮请以倒三角形来覆盖，面部会立体呈现。\ntarte遮瑕液、、kat von D的lock it遮瑕液、的粉条、Anastasia的粉条、MAC遮瑕液、urban decay的Naked skin………很多产品都很适合这步。（黑眼圈不严重的修饰都可以省略，直接到第三步使用这些产品即可）\n#如何选择遮瑕膏的颜色[话题]#\n第四步：定妆散粉、蜜粉\n用散粉、蜜粉在眼周清扫是妆容落定。也能使眼周肌肤看起来哑光细腻。这一步是确保之前遮的都没问题。我用的散粉\n对于合适的散粉太多啦 不赘述 （回头发个专门说十几款散粉哒）[活力]\n第五步：高光提亮\n高光加强眼周效果，日常建议大家用一些自然效果的高光。视频里我用了Tony Moly的混合高光，相对比较适合上班。我最喜欢的是hourglass的上色修容高光盘，妈啊 那颜色简直无与伦比的高级。我爱高光这个大家都知道，我就喜欢高光盘 。Anastasia的高光盘都能召集开会啦！视频里是ABH* nicole guerriero的glow kit闪瞎眼那种 （以后再出个高光大集合推荐）高光可以营造水光肌的效果，看起来皮肤会很好。当然打的位置也很重要，轻微扫，别太多会吓着人[装酷]\n\n\n\n\n\n买不着的买这个👉\nPS.使用液体或膏状高光滴仙女们 请在定妆前使用高光，最后清扫定妆粉。\n对于黑眼圈其实要聊我能聊出一个合辑呢，继续下次分享去黑眼圈的小技巧到眼周保养。[喜欢]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/800785472119fd77ea5bc0877bf8124fb35dd789_v1_ln',
    'video_id': '59019f1ab46c5d552230ded0',
    'title': '🎊迪士尼迷们的福利！🏰迪士尼最新玩法🏖',
    'video_tag_list': '迪士尼;上海迪士尼住宿指南',
    'content': '陪伴才是最长情的告白\n🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾\n如果你的未来我无法参与更多，那你的童年我一定不能错过！一段新奇的旅程，一次难忘的经历，一段美好的童年记忆，一堂丰富多彩的校外辅导课，disney will give you more……\n🎡🎡🎡🎡🎢🎢🎢🎢🎢🏰🏰🏰🏰🏰\n迪士尼专属邮轮+迪士尼主题乐园＋迪士尼园区特色酒店＋迪士尼私人小岛…\n玩迪士尼，我们是#认真的#！\n🎊🎊🎊🎊🎊🎊🎉🎉🎉🎉🎉🎉🎀🎀🎀🎀🎀🎀\n北京出发路经墨西哥，大开曼，雅买加奥兰多更多精彩地，为期12天的迪士尼豪华游轮幻想号\n请打开脑洞跟我们一起探索迪士尼！#我是短发控[话题]##上海迪士尼游玩攻略[话题]##上海迪士尼住宿指南[话题]##一听就爱上的英文歌单[话题]##肉食动物最爱的美食[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/a22fc9fb-f7fe244-a1c6-048a660f2bee_compress_L1',
    'video_id': '5901a5b9a9b2ed5f94789dff',
    'title': '春风十里，不如野餐一次【曼达小馆】',
    'video_tag_list': '',
    'content': '#用视频记录美食[话题]##野餐带什么[话题]#\n最近天气真是太好了，各种各样叫不出名的花花开得正旺，心心念念了一个冬天的春游终于可以提上日程了，所以我赶紧挑了个好天气，准备三两美食，就和我的小伙伴出来春游了！不过在曝光我的私房春游菜谱之前，还是有必要和你们通报一下我都玩了什么让你们知（xiàn）道（mù）一下的。\n不得不说工作日出来春游还是挺爽的，有种承包了整座公园的感觉，走在路上，还能撞见出来春游的萌萌的小学生，感觉自己也一下回到了童年。不过到了放风筝的时候，就有点尴尬了，小黄鸭怎么也飞不起来......本来想给你们看一下春日里我放荡不羁的一面，那现在这样，你们假装看一下我放风筝就好了......\n春光这么好，食物也不能输啊！所以我准备了野餐必备的猪排三明治和配色媲美花花的鲜虾意面沙拉，还有以前节目里做过的紫菜包饭（后台回复关键词“紫菜包饭”，可以查看图文菜谱），不吃饱怎么有力气玩（làng）呢！裹着脆脆面包屑的鲜嫩猪肉，再配上新鲜的蔬菜和抹着美乃滋的吐司，一本满足！还有吃起来酸爽的意面沙拉，里面满是虾仁、番茄、甜椒、牛油果、芝士、橄榄，吃起来比春天更精彩！\n▊  猪排三明治\n- 食 材 -\n猪排300g、吐司4片、生菜4片、面粉50g、美乃滋2大勺、猪排酱2大勺、黄油2大勺、芥末酱1大勺、卷心菜100g、胡萝卜50g、鸡蛋1个、黑胡椒、盐\n1.猪排切断筋膜用刀背敲打，撒上盐和胡椒腌10分钟，筛一层面粉，薄薄裹上一层蛋液，再粘一层面包屑，下油锅炸至表面金黄，捞出放凉\n2.取两片吐司，一片先抹软化的黄油再抹美乃滋，另一片先抹黄油再抹黄芥末酱\n3.吐司片上放生菜、卷心菜丝、胡萝卜丝、炸猪排和猪排酱，再放一些卷心菜丝、胡萝卜丝和生菜，将另一片吐司盖上去\n4.保鲜膜包好三明治，固定形状后从中间切开，放入餐盒\n- Tips -\n1.猪排外面包裹的一圈白色筋膜一定要切断，不然加热后猪排会卷起来；\n2.炸猪排的面包屑最好是颗粒较大的，炸出来会比较脆，如果不想在家自己做，也可以直接买现成的；\n3.猪排过蛋液和面包屑的时候，记得保持一只手过湿的蛋液、一只手过干的面包屑，这样操作不会那么乱；\n4.吐司切不切边看个人喜好，但一定都要抹黄油，增添味道的同时可以防止食材里的水分渗出弄湿三明治；\n5.吐司上抹的酱料可以选你们喜欢的，我抹辛辣的芥末酱是为了缓解猪排的油腻；\n▊  鲜虾意面沙拉\n- 食 材 -\n樱桃番茄100g、意面100g、虾仁150g、马苏里拉奶酪100g、白酒醋2大勺、橄榄油4大勺、黑橄榄50g、欧芹一小把、蒜头一瓣、牛油果1/2个、黄甜椒1/2个、柠檬一个、芥末酱1小勺、盐、糖、黑胡椒\n1.虾仁开背，开水中煮2分钟，捞出后放冰水降温\n2.开水加盐煮意面至9.5成熟捞出，趁热加入橄榄油拌匀，小番茄切半、甜椒切块，加入意面，牛油果切块后先加柠檬汁拌匀，再加入意面\n3.柠檬汁、白酒醋、橄榄油、蒜蓉、芥末酱、糖、盐、黑胡椒放入杯子，盖上盖子摇匀，做成油醋汁\n4.虾仁、马苏里拉芝士、橄榄加入意面，淋上油醋汁，拌匀后撒上欧芹碎，盖上保鲜膜，放冰箱冷藏一夜\n- Tips -\n1. 我做意面沙拉时用的是螺旋状的意面，你们也可以用那种短短的通心粉；\n2. 做沙拉的意面不能煮到全熟，煮到9.5成熟就可以捞出来了，趁热马上加橄榄油拌匀，可以防止粘连；\n3. 牛油果切好后不能直接放进意面沙拉，容易氧化，用柠檬汁拌一下可以防止变色；\n4. 油醋汁中的酸性汁可以全部用柠檬汁，也可以用柠檬汁和白/红酒醋的混合，味道会更丰富；\n5. 拌意面沙拉的油醋汁最好稍咸一点，因为沙拉里的食材没有经过调味，酱汁拌进沙拉隔夜再吃，可以让食材吸收酱汁的味道；\n6. 我做沙拉用的是小球状的马苏里拉芝士，换成车达奶酪或者是那种大块状的马苏里拉芝士也可以。\n｡◕‿◕｡学做更多美食'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljZKE3t8nEwU201mFoBz61PS6Y10_compress_L1',
    'video_id': '5901b1e2d1d3b94c24788da3',
    'title': '如何用家里最普通的衣架，让裤子不滑落、不产生折痕',
    'video_tag_list': '',
    'content': '家里用衣架挂裤子经常会滑落，有些面料还容易产生折痕，今天分享一下挂裤子的小技巧[萌萌哒R][萌萌哒R]之前发完某拍就把原视频删了，结果害的我还得去某拍再下载带水印的版本，100%是我原创哦[偷笑R][偷笑R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhlOZYeT-cMR1luAmcv1tRYgj-VG_compress_L1',
    'video_id': '5901c041d1d3b90293788db2',
    'title': '关于猫咪尴尬期的科普',
    'video_tag_list': '',
    'content': '猫咪的尴尬期,你了解吗？\n尴尬期是什么？\n尴尬期是指猫咪因为正常生长的原因变得暂时偏离了本品种应有的比例、协调感和美感，变得不好看的一个时期，所以我们叫它尴尬期。 尴尬期基本出现在大概3月龄至到6、7月龄，个体差距会有长有短，有早有晚，偶尔有少数猫猫成长的过程中一直保持本品种应有的比例、协调感和美感，那么这样的猫猫就可以说尴尬期也很漂亮，也可以说没有尴尬期。\n尴尬期的特点和表现\n出现尴尬期的原因是正常的生长特点导致的，尴尬期指的是幼猫身体快速生长的同时因为各组织结构生长速度不同而导致幼猫暂时失去本品种正确的身体比例、均衡感和美感（比如脸变长，是因为头骨会首先明显的纵向生长，导致了脸变长，然后才有明显的横向（宽度）生长和额段变化，脸的宽度才逐渐显现，尴尬期结束后，脸的长度和宽度，恢复到正常的比例）并伴随换毛，纹路变淡（换掉胎毛）等现象的正常表现。期间的表现比如感觉猫猫变瘦（但重量不会减）、脸变长、身体比例不够协调、被毛稀少颜色黯沉。\n尴尬期家长需要做的就是等待和提供足够的营养食物。使用专业的幼猫猫粮，这里我推荐法产皇家的幼猫猫粮，购买营养丰富的主食罐头和主食冻干，也可以喂生肉哦，还有晒够太阳，补充鱼油营养膏这些就好啦！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ln7a1F7z-KwuscKGfCSczWt5ZllI_compress_L1',
    'video_id': '5901d56fd1d3b95fbba0a4aa',
    'title': '关爱油皮代表：Nina姐姐好物推荐',
    'video_tag_list': '',
    'content': '神奇的洁面棒and收缩毛孔神器！还有油皮的亲妈：BECCA妆前乳！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqcNAZ8-4wx5egZjPGvNgNVK1Zdn_compress_L1',
    'video_id': '5901d7fbd1d3b967c1788da7',
    'title': '鼻影教程终于出来了！',
    'video_tag_list': '简单易学的鼻影画法',
    'content': '最近更新了画眉教程，请一定多多收藏！谢谢！\n#简单易学的鼻影画法[话题]# #五分钟妆容挑战[话题]# #日常妆容打卡[话题]#\n我终于有了第一支视频，是大家期待已久的鼻影画法。\n看前有几点提醒：\n🌟鼻影对鼻子的精致有一定的作用，但是不能神化它。还是要靠p图的，但是一定会让你不一样的。\n🌟请手动戳视频前后对比，化的时候可能没感觉，但对比一下还是蛮大的。\n🌟相机吃妆，现实鼻影会更加明显。\n🌟第一次做视频，不接受批评，只接受鼓励和建议，谢谢。\n有人希望我做眉毛教程，我是只有半截眉毛的无眉星人，可能会吓到大家，有人愿意看么？那就举手吧。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lo4XvKd7z7kuNdV7e5vBut95FIwE_compress_L1',
    'video_id': '5901d92e14de412313e528b5',
    'title': '本期话题：你的唇色和哪首歌最配？',
    'video_tag_list': '你的唇色和哪首歌最配？',
    'content': '#你的唇色和哪首歌最配？[话题]#\n👉有没有一种唇色让你涂上就想哼歌？\n👉有没有一首歌让你听了只想涂某种唇色？\n如果你是化妆必听歌的人，就赶紧po出来分享吧！[少女心]\n【如何发笔记】\n1⃣️拍一段30s左右的唇膏试色视频，并配上你觉得最合适的背景乐～\n2⃣️你可以在后期加上音乐 or 拍的时候就放着音乐同期收音！\n3⃣️加上话题标签#你的唇色和哪首歌最配？[话题]#\n【如何加话题】\n1⃣️在文字输入页面有 ＃井号键，按下去！输入关键词，找到话题活动，点击即可参与。\n2⃣️成功参与话题的文字会变成蓝色哦：#你的唇色和哪首歌最配？[话题]#\n美妆薯期待大家的小视频哦～\nps：视频功能已全线开放。\npps：视频来自@草一直很青'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FuTxru7RFr4U-mToEPIiVc7ZwczF_compress_L1',
    'video_id': '59020da614de411e29c9924e',
    'title': '哈哈哈哈哈哈保证你没见过的纯素颜（掉粉视频）',
    'video_tag_list': '',
    'content': '男票平常不让我化妆说喜欢我素颜的样子。\n我自己是觉得素颜太可爱了不符合我性格所以爱化妆[鄙视R]。\n大家就笑一笑吧也别损我了啊！连眉毛都没了啊哈哈哈哈哈哈哈我看着都想笑啊哈哈哈哈哈哈哈哈哈哈。\n厕所拍的🙄️\n这个视频可以清走一波非真爱粉了[再见R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpRD0tWQQFIsE396FKzep7C4_sFj_compress_L1',
    'video_id': '59021676d2c8a57210dc6991',
    'title': '无需注册VSCO，一样也能修大片【视频教程】',
    'video_tag_list': '',
    'content': '之前发过一期VSCO基础调色攻略，有小仙女反映说怎么样都注册不好，其实VSCO不注册只是不能使用全滤镜，但它的调整工具还是能用的，而且我觉得非常好用。有时候照片选不好一款适合的滤镜，直接调参倒是很令人满意。\n今天就以视频的形式讲一下如何在【不注册】的情况下，依然使用VSCO进行调色修图。前半段废话比较多，可以拉到【32秒】开始教程，视频最后部分有修图前后的对比图。希望这支视频对你有所帮助❤\n🍊这是我第一次录视频，表达水平和画质呈现不是很好，但是真的有用心在做，试了很多次，有什么不到位的地方还请多多包涵～\n附：调整参数\n曝光+1.8 | 对比度+1.4 | 清晰度+1.5 | 锐化+1.2 | 饱和度+1.0 | 色温-1.2 | 色调+1.0 | 褪色+1.7\n还有小仙女问VSCO是否能调粉色调照片，回答是肯定的，找机会下次出教程吧~\n🔸🔸🔸🔸🔸🔸🔸🔸\nP.S 关于修图的功课我建立了一个【拍照修图】的专辑，有我自己的，也有收藏别人的，欢迎关注，一起学习！\n不知道视频的形式你还满意咯？\n欢迎给我留言提意见，感谢[飞吻R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/707347077917e2e2ff0e3643e524cc9bf7377a9e_r',
    'video_id': '5902aff514de416d06e528ac',
    'title': '土豆这样做好吃又好看，制作非常简便快捷',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n土豆饱腹感强，营养含量丰富。富含维生素B1、B2、B6和泛酸等B族维生素及大量的优质纤维素等。\n另外,土豆是非常好的高钾低钠食品，很适合水肿型肥胖者食用，加上其钾含量丰富，所以还具有瘦腿的功效。\n★★★★★\n创意指数\n神农架小土豆\n▼\n神农架小土豆\n·视频音乐·\nLucky Stroke - Good Day\n·食材·\n小土豆、青椒、红椒、洋葱\n葱、生抽、十三香、孜然\n糖、辣椒粉、盐\n1.土豆放入沸水中，煮至变熟\n2.捞出过冷水\n3.姜土豆去皮，备用\n4.洋葱切丁、青、红椒切丁、切葱花备用\n5.热锅内倒入橄榄油\n6.倒入土豆，将土豆煎炒至两面发黄\n7.倒入洋葱丁炒出香味\n8.倒入2茶匙十三香、1茶匙辣椒粉\n9.迅速炒匀后倒入青、红椒丁清炒\n10.锅内倒入1茶匙盐、1勺生抽、2茶匙糖、少许清水\n11.大火煸炒收干汁水，关火撒入葱花拌匀\n12.盛盘后撒入适量孜然即可\n13.这样做的土豆绝对让孩子们爱上它~！\n#人人都爱土豆料理[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liPpYJ2jZjOAqhADhGGI2Vw4TFKI_compress_L1',
    'video_id': '5902e175d1d3b935746b78ce',
    'title': '广州四季酒店99层天吧',
    'video_tag_list': '',
    'content': '慕名而来\n优点：吧台设计很好看\n靠窗户边的位置很舒适\n卫生间设计很好看\n没有了 因为我之前如果柏悦酒店的悦吧感觉还是柏悦比较好吧\n跟柏悦相比  酒吧太小了  有点吵  外国人很多  要等位才轮到靠玻璃边的  没有露天的座位 东西一般般的  下次会去柏悦 个人观点'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/b7f83e7fbc62719636f4a2f7b5f24f7667ccf035_v1_ln',
    'video_id': '5902e2f6d1d3b91a9fe26354',
    'title': '广州柏悦酒店70层悦吧',
    'video_tag_list': '',
    'content': '优点：环境很舒适  酒吧设计很棒 座位也很好\n外面还有露天的座位  站在外面吹吹风看看夜景真的是超级棒了～\n柏悦跟司四季比 我比较喜欢柏悦 虽然比四季低几层 但是环境比四季好很多～  里面的炸辣椒圈也好吃哈哈还有鸡肉薯条[飞吻R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lunZekhTJ42i5qYeGcori5gkIBPI_compress_L1',
    'video_id': '5902ee93d1d3b96b35e2637f',
    'title': '海风狂吹',
    'video_tag_list': '',
    'content': '午后海边狂风大作，不怕，迎着风继续我的爱好！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/5ed8ee04ac9d266c4dc46f5a05e0e60f36e321f7_v1_ln',
    'video_id': '5902fdb37fc5b8300fe12f5e',
    'title': '上东穆坞茶园采制正宗西湖龙井茶~我们给你拍回来啦！@杭州',
    'video_tag_list': '用视频记录旅行;杭州',
    'content': '#用视频记录旅行[话题]#\n第一次拍这种视频晃啊晃啊晃的，但是上茶山采茶制茶的过程都记录给大家啦！\n对于这次去东穆坞村采制正宗西湖龙井茶，写了PO文，大家可以翻翻前几天发的文章，里面对于一些“科普性”的小知识大家可以看那边哦~\n这次拍摄的茶园是 @禅茶香 家的，她爷爷奶奶依然忙碌于茶园，感兴趣的童鞋们可以直接cue她。\nPS.剪片就是imove，求推荐更好用丰富的剪片软件~~谢谢各位大神！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/80b588a04b397455505e63ec21bd47d5e96651c2_r_ln',
    'video_id': '590324ebb46c5d62a73ac154',
    'title': '快速减脂瘦身、成就蜜桃臀、马甲线 到底要怎么练？',
    'video_tag_list': '见人不如健身',
    'content': '#必须要安利的健身动作[话题]#\n最近两天好多宝宝问“到底怎么减脂？怎么练？练些啥？怎么练肌肉？怎么练翘臀？……\n这些问题都好大、没法用一句话回答[叹气R][叹气R][叹气R]\n说看了笔记后觉得很科学很仔细很全面、决定要练起来，可是还是一脸迷茫、不知道怎么开始！\n这个对于之前不怎么接触健身的人来说、确实是会无从下手～\n没事，不要着急、文章可以慢慢看、动作可以慢慢学、不管多厉害的大神也都是一点一滴的积累、无数的汗水和学习才能成就自己想要的好身材～健身真的没有捷径可走、也绝不辜负你、付出多少就会回报多少！\n有太多的东西想跟大家分享、可是还是得有先后顺序、有的人想要减脂动作、有的人想知道有氧怎么做最好、有的要减肚子、有的要练力量、有的要大翘臀、有的要挺拔的背部、有的要核心训练、有的要解决肩颈不适、有的要普拉提等等…\n今天就做个调查和投票、上面这些、想要我优先更新的在下面留言、我会根据大家投票的结果按顺序分享训练视频等～ 欢迎大家围观讨论！\n今天录的这个是一套很简单很短的初级减脂计划～\n募集到全身上下大小肌肉、核心腹部、稳定性、心肺等\n动作讲解：\n最前面垫子上的动作是属于普拉提的核心激活的、\n注意腹部全程收紧\n建议训练前都可以做两组、先稳定了核心、后面所有的动作才能保证不变形、不代偿、不出错！\n接着做成动态的登山跑、热身、提高体温和心率！\n也可以侧面提膝激活下侧腹\n（激活热身的动作每侧15-20次、每一侧都得做、平板支撑30秒-60秒一组、登山跑45秒一组 ）做两组\n后面接着的深蹲：\n保持核心收紧、膝盖和脚尖必须在一个方向、膝盖尽量在脚尖以内活动、蹲到大腿与地面接近平行即可、能力强的可以全蹲到膝盖以下！吸气下蹲、呼气起来\n15-20个/组 3-6组\n俯卧撑：\n女生可以直接做跪姿的版本、肩，髋、膝要在一条线上\n收腹收屁股\n胸部往地面的方向走、呼气胸大肌和肱三头肌用力把身体撑起来～ 吸气下去 呼气起来\n15-20个/组 3-6组\n附身划船：\n手上的负重可以换成别的东西、杠铃、哑铃、球、弹力带等都可以、也可以空手/\n手划向肚脐处、拉起来的时候主动往后缩肩胛骨、\n全程收紧腹部\n吸气下放、呼气拉起\n15-20个/组 3-6组\n～～请忽略我的大背、因为练力量很久、而且负重较大、所以背部肌肉相对还算发达、加上现阶段体脂很高、加上角度问题、会显得很壮实、希望不要吓到宝宝们[害羞R][害羞R][害羞R][害羞R][害羞R]\n波比跳：\n公认的最减脂的动作！\n按照视频对着做就行、老规矩、收核心、脚尖冲前、不要外八字脚！20个/组  3-6组\n战术绳：\n跟波比跳一个级别的减脂利器！\n需要全身肌肉的共同稳定配合发力、\n有很多种玩法、今天先分享这一个\n30秒/组 3-6组\n#见人不如健身[话题]##健身是把整容刀[话题]##科学减脂食谱[话题]##健身靠装备[话题]##健身穿什么[话题]##厉害了我的健身房[话题]##举铁P.K.瑜伽[话题]#\n#必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fj7TdEIQ44V49AUi78zEKATbxJyQ_compress_L1',
    'video_id': '5903252014de41726351c1f7',
    'title': '夏日搭配',
    'video_tag_list': '',
    'content': '帽子是巴黎世家 选了深咖色 白色黑色戴的人太多了 并且咖色复古显肤白 很喜欢 蓝白条纹衬衣是小众品牌 巴黎买手店购入。鞋子是jaquemus 很钟爱的法国九零后设计师品牌 编织球包perrinparis 短裤是多年前的zara 为了避免走光搭配在衬衣里面😺'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpJpTEYeDHIEtk7sfod7-q_V33i4_compress_L1',
    'video_id': '590364f0d2c8a50b3c26ce09',
    'title': '细软榻护发造型第二波，醒发水升级了升级了升级了',
    'video_tag_list': '拯救细软发大作战;沙宣',
    'content': '之前发过拯救细软发质的视频大家都略喜欢的样子，里面有出现过的沙宣醒发水升级了，包装是好看了些，然后顺带我就入了它们这个新系列。\n这次给到我惊艳的是弹力素，质地rio轻薄一点都不生硬，具体的看视频吧[得意]#拯救细软发大作战[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/806a20b181e033ce7bbc2baf6d8326a294bb40c4_r_ln',
    'video_id': '59040049d2c8a5543b26ce10',
    'title': '新手指南 眼影怎么画',
    'video_tag_list': '跟着视频画眼影',
    'content': '有博主分享过这两种画法 这也是我日常画眼妆的方法\n搭配好颜色 晕染自然边界处是这两种画法的要求\n💕三字型画法\n示范眼影：hilikaX懒蛋蛋（韩货不建议购买）\n颜色由浅到深 依次渐小着色面积\n一字：眼部打底 或采用日常淡色系眼影可以一个颜色出门\n二字：根据自己的眉眼距确定范围 越靠近睫毛颜色越深\n边界晕染干净 从睫毛根部向外晕染\n三字：可以用眼线色画眼线 或者珠光色提亮\n💕川字形画法\n示范眼影：smash box 色号 ablaze\n由前往后 眼线变化 一般中间色最前 头尾颜色深\n可用两个颜色 分别分布在眼睛前后1/2的位置\n或者分布在2/3和1/3的位置 属于边界以及中间颜色过渡自然\n💕希望大家喜欢这个视频 欢迎点赞收藏关注\n有问题可以留言 最近不知道要拍什么 也没入手新的\n有啥想看的可以留言给我 比❤️\n#跟着视频画眼影[话题]#\n#眼影如何晕染[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luDMHxwBGgfocYYsIR0CA394tTGA_compress_L1',
    'video_id': '59041afab46c5d20283ac153',
    'title': '哼！这么可爱你妈知道吗！皮，皮，皮，肯德基皮卡丘！脸红啦！',
    'video_tag_list': 'KFC',
    'content': '肯爷爷家就是来用这个骗玩具的啊皮卡丘\n[笑哭R][笑哭R][笑哭R][笑哭R][笑哭R][笑哭R][笑哭R][笑哭R][笑哭R][笑哭R]\n萌死了啊！\n萌啊！\n皮，皮，皮，皮卡丘！\n帅气和娇羞皮卡丘碰在一起，女孩子就会脸红呦[害羞R][害羞R][害羞R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmEHd3D8Zt2rJa-VUVSpVPqU-ilF_compress_L1',
    'video_id': '59046344b46c5d5d120fd432',
    'title': '只有这样才能腾出更多空间买新牛仔裤',
    'video_tag_list': '',
    'content': '家里牛仔裤太多，今天教大家如何把它们收纳起来以便我们有借口买更多[偷笑R][偷笑R][害羞R][害羞R][飞吻R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhb6OH5XH3TqjCfU3K2eJXBDbA-k_compress_L1',
    'video_id': '59048beeb46c5d0ffb0fd435',
    'title': '4.29 | 加送短视频，看看动态的我！',
    'video_tag_list': '',
    'content': '🗣hi，老铁们～在外面玩呢吧？在家无聊呢吧？不如跟我一起看看我出去玩儿的视频吧，就想应个景，节日快乐哦,love u all ❤️'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/1a8b6980-e74b839-91a6-b4ae4bee4974?sign=d889d354a9642f9771d28ccb990b21fe&t=65fb06d4',
    'video_id': '5905640a7fc5b819cb3ed9af',
    'title': '30分钟HIIT搏击燃脂｜训练前后的饮食吃对了事半功倍',
    'video_tag_list': '8周变身比基尼女神;8周变身比基尼女神',
    'content': '#8周变身比基尼女神[话题]#空腹训练能够燃烧更多热量？运动后吃饭容易长胖？果真如此还是这些仅仅是没有科学依据的谣言？健身前后是否该吃东西？吃什么？怎么吃？本期视频Giselle和Weiya将和大家分享训练前后用餐的小窍门，在对的时间吃对的东西，让你训练事半功倍！此外，五一小长假别偷懒，在家跟着大G一起搏击HIIT练起来，刷脂刷到没朋友！记得训练完了打卡@fit4life ，并加标签#8周变身比基尼女神[话题]#\n疑问1: 空腹做运动能够燃烧更多热量？\n错。试验证明，不管是否空腹，同样训练燃烧的热量是一样的。对这句话的正确理解是，空腹做有氧运动，因为体内没有糖原可以燃烧，于是身体会直接通过燃烧脂肪供能。但是，你之后吃完东西，摄入的糖又会转化成脂肪。除非你吃的东西热量小于你健身消耗的热量，但是这样你变瘦也不是因为空腹做运动，而是你的热量消耗大于摄入。\n反而，当空腹训练的时候，身体除了依靠脂肪供能，也会分解部分肌肉。所以长期空腹训练，还可能造成肌肉流失，降低基代，真的是得不偿失。\n此外，在进行力量训练的时候我们需要快速供能（“咣”的一下子举起来），也就是燃烧糖原的无氧功能。而燃烧脂肪是非常慢的有氧供能（脂肪要先转化成糖再转化成能量），是来不及支持我们举铁时的爆发力的。我们饿着肚子举铁的时候经常会感觉到没劲儿，就是因为身体里没有快速供能的糖。\n所以健身真的不要空腹，尤其是做力量训练。建议大家在训练之前1个小时补充复杂碳水（比如红薯、燕麦、全麦面包等），以及适量蛋白质（鸡蛋、坚果、酸奶等）。\n疑问2: 运动完之后吃东西更容易长胖？\n错。之前视频里有讲过，我们的体重变化完全取决于蓄水池的进水量和出水量，当进水量大于出水量（吃的比消耗的热量多），体重上涨；出水量大于进水量（消耗的比吃的热量多），体重减轻。所以说运动完吃东西更容易长胖是不对的。\n反而，由于运动中我们消耗了身体里所有的糖原，如果在之后不及时补充糖和蛋白质，身体可能就要依靠分解肌肉来供能了。\n实验证明，在运动后30-60分钟内补充足量蛋白质和少量复杂碳水是最好的。所以如果训练后用餐，比较好的选择有全麦三明治，沙拉加份肉，中餐的话蒸煮类的瘦肉，清淡的蔬菜，搭配粗粮都是不错的选择。如果来不及吃饭，那就喝一杯蛋白粉或者吃个蛋白棒吧。\n上个周末Giselle和Weiya被请去拳赛当ringcard girl，4个小时一直站在最前面看各种K.O.激动到不行，所以本周的快速燃脂HIIT课程里也加入了搏击的元素。五一小长假到了，就算你不能来参加在fit4life实体店的变身比基尼女神集训营，在家也不能偷懒，这套动作加上家庭作业（keep HIIT活力）每天都要打卡哦！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luDEY1GPD8OKZeXdkK5TdxlftNsG_compress_L1',
    'video_id': '59057f75d1d3b95ac3abed3e',
    'title': '迪拜哈利法塔灯光秀视频',
    'video_tag_list': '迪拜;用视频记录旅行',
    'content': '哈利法塔灯光秀由 yusuke murakami 和 tangent 完成的灯光艺术装置，在世界最高建筑的哈利法塔外立面展出，为大家带了一段从地球中心到宇宙的探索旅程。整个过程，开始于地球中心的熔岩，通过矿物层、深海、沙滩、建筑物、山脉到宇宙天空的层次变化，体现“提升”主题。\n太美太魔幻\n😍😍\n可惜当时离得太近，又没有带Gopro 手机拍的有点遗憾\n下次再去一定带好装备好好记录下来～\n#最爱旅行地[话题]##用视频记录旅行[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lndEtazAsg1xn9FoePTSxXLhv4CH_compress_L1',
    'video_id': '5905a851b46c5d6fe60fd435',
    'title': '穿搭心得分享#Rita聊天室#穿搭',
    'video_tag_list': '每日穿搭',
    'content': '来更新Rita聊天室的视频啦 更新完再粗门玩：）\n今天视频主要讲穿搭心得 希望有帮助啦\n#每日穿搭[话题]##微胖显瘦巧穿搭[话题]##小个子显高穿搭[话题]##170cm女生穿搭[话题]#\n但小红书只能传5分钟[哭惹R]\n视频其余部分的在 微博：Ritatawang\n记得点赞么么哒：）'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqtJGDDb4K9uyatuj2kSTorTafIb_compress_L1',
    'video_id': '5905df5114de41245cca0e4e',
    'title': '舔爪爪~布偶猫香菇',
    'video_tag_list': '',
    'content': '爪爪好不好吃？🌝'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lv2Ea51ISDvynl9p--8VjPkMhKvM_compress_L1',
    'video_id': '5906607ed1d3b95809abed3c',
    'title': '亲子游泳',
    'video_tag_list': '',
    'content': '婴儿天生就会游泳。这是在天津龙格亲子游泳馆，教练在让大人托着宝宝的肩膀练习。\n😘宝宝一放到水上，身子就自动漂起来，平漂在水面上。\n😉教练说，有47天的宝宝游泳的。\n😜训练四节课后，就可以让宝宝潜水了，宝宝一出生就会潜水，有自动闭气反射，在六个月以后渐渐消退。\n☺我家宝宝第一次下水太紧张，手脚绷得直直的。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FsyF1CG6q7f7upo5gSD6IDC2N4rv_compress_L1',
    'video_id': '590662be14de41692851c1f2',
    'title': '五一度假好去处，云海仙境旅游处女地',
    'video_tag_list': '',
    'content': '基隆山云海，位于江西赣州市寻乌县，海拔一千四百多米，属于亚热带地区，常年湿润气候，生态宜居，未开发，无飞机火车，只能通汽车，想去得找当地人引路。全国脐橙之乡，赣南脐橙优质产区。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/158b895871c87856d9fb9f366ca277c473f23a0d_v1_ln',
    'video_id': '5906970d14de415568ca0e4c',
    'title': '自制Jagerbomb',
    'video_tag_list': '家里必备的酒杯',
    'content': '昨儿买了些酒回来自己玩，先弄了个简单又好喝的Jagerbomb，只需要Jagermeister和红牛就可以啦～\n杯子是宜家的杯子，量也刚刚好～\n#家里必备的酒杯[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/9e99ebe5-6c95649-83fa-f08bc6491a04?sign=071c97b35758b6bfbdcd878273586617&t=65fb06d4',
    'video_id': '5906b24f7fc5b8416192f6f2',
    'title': '我的近况+购物分享  Dior |  Christian Louboutin | Agent Provocateur | Sep',
    'video_tag_list': '',
    'content': '我要毕业啦！下学期要去我的Dream School西北大学Kellogg商学院读研究生，好开心，希望把这个快乐分享给你们！嘻嘻~这支视频给你们分享我最近买的东西，答应你们的TF试色我下期就做！\n*提到的商品*\n1. Dior 塔罗牌丝巾 Moon\n2. 墨镜 店里买的 发票上写的是 ORIGINS2 1EDT4/TU\n3. Christian Louboutin 红底鞋 Pigalle Pumps\n4. Agent Provocateur Classic Dressing Gown Pink\n*Sephora*\n5. BENEFIT COSMETICS Cheek Parade\n6. SEPHORA FAVORITES Power of the Petal\n7. VISEART Theory Palette\n8. VISEART Eyeshadow Palette\n*Miibox*\n9. 日本资生堂高端银座系列THE GINZA 贵妇天然蚕丝化妆棉 粉色 60枚\n10. 日本DUP假睫毛胶 黑色\n11. Dolly Wink #9'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/26e1a40f35d84ed50c3b7dd11b987382bb93fbde?sign=dacfbb134b433b6a84ad2458d20155d5&t=65fb06d4',
    'video_id': '5906f097b46c5d136e0fd433',
    'title': '不用老师也可以在家学钢琴了',
    'video_tag_list': '升级88键重锤考级自学神器智能专业成人儿童电子钢琴PX-770 优雅白+琴凳礼包',
    'content': '入手的电子钢琴the one，省去了昂贵的钢琴课的费用😁，在家边看ipad，边弹就可以，4000元，搞定，一部手机的价格，挺好滴😛\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/01e24807932027c001837003803120dad5_259.mp4',
    'video_id': '5907350ad2c8a5539604822c',
    'title': '松下卷发棒视频评测版本',
    'video_tag_list': '拯救细软发大作战',
    'content': '之前发过的这个卷发棒图文版本，这次撸个视频给大家看[抠鼻]#拯救细软发大作战[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgfHFM-99YnozvMpIJk3ggMHNBmI_compress_L1',
    'video_id': '59075a2ad2c8a5722a26ce0e',
    'title': '【Adora试色】Huda beauty迪拜的哑光唇彩',
    'video_tag_list': '冷门色号口红试色;Huda Beauty',
    'content': '这是一波视频试色来自迪拜滴火遍全球的Huda beauty 的Liquid matte minis哑光液体mini装的试色#唇妆试色报告[话题]##冷门色号口红试色[话题]##豆沙色口红试色[话题]#喜欢欧美风的仙女请不要错过哦！huda beauty家的唇彩💄地区不踩雷 好选择👌\nps.脸肿各位凑合看哈[腹黑]\n颜色顺序是Pink edition、Nude edition、Red edition\n📢：那些天天视频底下问我什么唇彩💄的妹纸快粗来[惊恐R]\n[得意]其实这系列有四个色系，深棕色系我木有po就给仙女们奉上个人感觉比较日常的色系萌喽！\n选mini套主要是因为mini色真心为消费者考虑啊！不像其他品牌净把不好卖的奇怪色混在套装里让人觉得鸡肋，huda beauty的mini里包含着比如pink系里的明星色Icon、trophy wife、gossip gurl（颜色很日常而且显得灰常洋气 还不挑皮肤）[喜欢]\n还有nude系里推荐bombshell和venus是那种涂上秒变lily Maymac的颜色哈哈哈哈[少女心]\n最让我惊艳的red系里heartbreaker特别显白的大红色和很显气质的material girl哈哈捡到宝\nhuda beauty的唇彩味道很好闻像巧克力🍫 也不是特别浓的香，个人感觉味道适中。made in Italy竟然在意大利🇮🇹制造可见迪拜人民就是壕啊[抠鼻]\n虽然是哑光液体唇彩💄滋润度适中比Lime Crime要滋润一些，颜色也没那么重口，都很恰到好处，[害怕]摸着心❤️说实话。\n视频结尾是那一套大盒里十几支装，原谅我的嘴累了，想看试色可以留言我看情况而定哈。[喜欢]宝宝我嘴巴👄也挺不容易的[石化]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvuqgcGon3rAv-wCANqqKiqMuxFJ_compress_L1',
    'video_id': '590761d814de416536ca0e4b',
    'title': '竟然可以发视频啦',
    'video_tag_list': '',
    'content': '1M Hyojin编舞\ncover by Cady\n·\n竟然可以发视频了诶……HaHHHa\n那就来一支大爱的boys……\n爱了一年的舞终于学完拍完了\n谢谢cady老师圆梦\n都不知道有多坎坷……\n前后经历了：学的当天睡过头—拍的前一天摔了一跤—拍的路上车被撞了。\n虽然不及原版，但比想象中好很多！\n音乐是后期配的，有点延迟？'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llxkHm5tTl_laOeKlhWnccPtrTHR_compress_L1',
    'video_id': '5907ed79d2c8a5376d04823a',
    'title': '花10块钱买根棍子，家里就多出无数储物空间（1/2）',
    'video_tag_list': '',
    'content': '这次的视频超过5分钟了，小红书系统限制只能发5分钟以内的，所以切成两段发啦[吧唧R][得意R][害羞R]这是第一部，后面还有第二部\n希望视频里介绍清楚啦[偷笑R][偷笑R][偷笑R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lj9BFF3TiVKWHmz0dOMtpLCMd7CW_compress_L1',
    'video_id': '5907ee6ed2c8a56a8726ce08',
    'title': '花10块钱买根棍子，家里就多出无数储物空间（2/2）',
    'video_tag_list': '',
    'content': '这期视频超过5分钟啦，所以分两期发，这是视频后半部[偷笑R][偷笑R][偷笑R][萌萌哒R]\n#视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmgql8l_dL_481BxFNujRAxEJe_v_compress_L1',
    'video_id': '5907f600b46c5d13a40fd433',
    'title': '【Le Petit Chef】3D法餐🍽',
    'video_tag_list': '',
    'content': '推荐一处好玩的3D法餐！\n三道式～\n原理就是利用投影放小视频\n每道菜前都有一个呆萌小厨师下厨小故事\n小厨师的配音像小黄人！！！\n我手机上视频只能做10s的\n就放了三段好玩的哈哈\n菜式还算经典 但是食材摆盘但没啥大惊喜～\n图个新鲜 好玩😁\n📍浦东香格里拉翡翠36餐厅\n🎫Rmb650/pp\n每天中午1场 晚上2场'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FkYkuTj21hAjZ4Af9So-uvXmq_ee',
    'video_id': '5907f91314de417f8a51c1fa',
    'title': '最喜欢杀年猪时做自家卤',
    'video_tag_list': '周末吃啥;成都',
    'content': '新鲜哦！咕嘟咕嘟，流口水😪😢，做法前面有介绍😂😂\n#周末吃啥[话题]# #今天吃什么[话题]# '
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg9NVOPD_BdsBauL-iIlP4ElBYW7_compress_L1',
    'video_id': '5907fc5dd1d3b9645cabed39',
    'title': '没有螃蟹的赛螃蟹，孙红雷最爱吃的菜！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n赛螃蟹是一道传统特色名菜，口感滑嫩，营养丰富，味似蟹肉，老少皆宜。\n此菜虾蛋软嫩滑爽味鲜赛蟹肉，不是螃蟹，胜似蟹味，故名“赛螃蟹”。\n★★★★★\n创意指数\n赛螃蟹\n▼\n赛螃蟹\n·视频音乐·\nChina - m\n·食材·\n鲜虾仁、扇贝、咸蛋黄、鸡蛋\n胡萝卜、姜、料酒、糖、陈醋、盐\n1.蛋清蛋黄分离\n2.虾肉剁碎\n3.扇贝肉剁碎\n4.倒入料酒拌匀\n5.倒入蛋清中加入一茶匙盐搅拌均匀\n6.鸭蛋黄碾碎倒入鸡蛋黄中\n7.搓入生姜末、胡萝卜泥\n8.搅拌至粘稠备用\n9.热油锅倒入蛋白\n10.炒至嫩滑盛出备用\n11.油锅倒入蛋黄\n12.清炒至出油脂倒入蛋白\n13.炒至均匀即可出锅\n14.倒入一茶匙姜末、陈醋一勺、糖1.5茶匙拌匀\n15.淋上调料汁\n16.软嫩爽滑味鲜赛蟹肉，“不是螃蟹，胜似螃蟹”'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgNg_aPxDHhFKpwAP9TB-SiBr-p5_compress_L1',
    'video_id': '590813a314de4177406fddfc',
    'title': 'USJ哈利波特魔法世界',
    'video_tag_list': '',
    'content': '这次去环球影城买了7项express票，把热门的想坐的项目都刷完了，超满足！在霍格莫德村从白天呆到日落，哈利波特脑残粉好开心😍回头再发战利品！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/lugOzAMHIE40qD4AWlFiEGQF2cAj?sign=e65f708d3328b04528eff14888afaa25&t=65fb06d4',
    'video_id': '59082ad9b46c5d5d75aab19e',
    'title': '美胸笔记出炉🌼针对胸部（下垂外扩飞机场）✈️',
    'video_tag_list': '必须要安利的健身动作',
    'content': '#必须要安利的健身动作[话题]#\n答应过出美胸视频，前几天太忙啦。录了好久一直没腾出时间整理出笔记给你们😂给你们两个动作的文字解析和功效，配合着视频看👀应该会很清晰了😉（还有就是在我之前发过的笔记里，评论下方打广告的产品，都不是我用过的，买不买妹子们自行选择，因为我用过，对我而言有效的产品，基本上我都会发笔记告诉大家，但是还是那句我有效不代表100%的妹子用过都可以有效果，所以因人而异自行选择）：\n首先，视频中的第一个动作🌷：\n仰卧飞鸟（名字有点low，但是效果是很好的😂）\n准备姿势：选择软的垫子或者在床上，仰卧，屈腿90°，腹部收紧保持身体的稳定，手持哑铃或者选择其他小重量的重物\n开始动作：双手张开几乎平行于垫子但不接触，手臂不要完全伸直，吐气双手往中间靠拢\n结束动作：手腕的位置始终保持在乳头的正上方，吸气还原。\n过程中要想着是胸部正在往中间挤压发力而不是单靠手臂的力量\n这个动作能防止胸部外扩，让胸部聚拢并且挺拔（母乳期可以练）\n跪姿平地俯卧撑\n准备姿势：同样选择软垫子至于膝盖下方，选择俯卧位，膝盖着地，屈膝，大腿与地面的夹脚控制在30°-50°的范围之内，臀部腹部同时收紧保持躯干的稳定，不要塌腰，双手张开略比肩宽，大臂与身体的夹角保持在45°左右，眼睛朝正下方，手臂不要完全伸直\n开始动作：先吸气不动，吐气身体跟着向下，手臂不要向外张开。\n结束动作：到达最低的位置之后吐气，手臂向上伸直，身体跟着缓慢的向上还原。\n这个动作能让胸部防止下垂。\n✔️做完这两组运动后要放松可以促进血液循环，可选择拉伸动作。例如：（双手向上贴墙壁，双脚垂直地面分开。与肩同款，眼睛看向墙壁方向，往下压）保持在可承受范围之内。这个动作也可以很好疏通乳腺的😛之前产后恢复瑜伽课的老师教过我😛。\nPS：平常可以多选择精油类的美胸产品，出浴后🛀进行胸部打圈式顺时针按摩！⚠️（母乳期可以选择针对促进乳汁分泌的手法，这个详细可以百度，或者咨询月子中心，因为我本身喂养期乳汁分泌足够，只需要用四只手指轻轻按压结节出即可，所以详细的按摩手法我没有特别了解，☺但是精油尽量避免‼️）⚠️非母乳期的按摩方法是（百度搬运工）：\n一、整个乳房的按摩\n1．使用与需要按摩的乳房相反方向的手掌，从下方往上推。（10次左右）2．从乳房的外侧向乳房内侧，注意避开乳晕进行画圆的动作。（10次左右）\n二、乳头的按摩\n1．  用手指的指尖部分压住乳晕的圆圈部位，将乳头拉出。（5-6次左右）2．用手指水平地推，伸展乳晕部位。（5-6次左右）\n三、保持胸部优美曲线的按摩\n1．  从乳房下部开始，以打圈的手势，左右一同进行按摩。（10次左右）2．从胸部上方开始到颈部，以向上托起肌肉的手势按摩。（10次左右）\n看见评论有说动作太初级意义不大，我想解释一下：因为我之前的笔记看评论很多人说没时间去健身房 ，所以给到的动作都是属于平常在家 比较简单常能做到的动作 我是觉得运动是一个持之以恒的东西，姿势动作专业的话 其实长久坚持会有一定效果的，毕竟我的教练也很专业，都是得过奖而且也是有一定水准的。不会说推荐一些毫无意义的动作分享给大家☺～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ccf0275b9819e7529343012f1f9cb7ff7b278736_r_ln',
    'video_id': '590844d1a9b2ed6255d73dd5',
    'title': '涨姿势了，原来这样也可以，从此切菜不再有粘住刀面的烦恼！',
    'video_tag_list': '',
    'content': '切蔬菜或者切肉类，遇到食材接二连三的粘住刀面的情况总是很难受，不断的清除黏在刀面上的食材也很费时间。\n这样的小烦恼就来交给喵招吧！只要用上一根小牙签，居然全都能搞定~超实用，以后再也不怕食材粘住刀啦！ #视频教你生活小窍门\n#视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhipayMAFZJ2_j_sfaEHuI71flGj_compress_L1',
    'video_id': '59089a9bd2c8a5594373dadf',
    'title': '四个半月长牙了',
    'video_tag_list': '',
    'content': 'Cherry小公主在四个半月给麻麻一个大惊喜，冒出两颗小白牙，一早上我就看她在那吐泡泡吃手，一直在那扣扣，我说看看是不是要长牙痒痒，扒开嘴，长牙了！！！\n于是各种咬咬胶给她买起来了，出门最方便最喜欢的还是这个可么可多的，软软的可能咬起来舒服吧。'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/4538dc67-1b8eced-8bc0-8f9e6bb6ca20?sign=6b7d98d9a13fac6ab45a0a2d728d2300&t=65fb06d4',
    'video_id': '590933ba7fc5b86f20b88980',
    'title': 'wi化妆视频|夏日都市妆容+发型',
    'video_tag_list': '跟着视频画眼影;乔治阿玛尼;LB 鲜奶油防水眼线笔;ZOEVA;花王 Kao 碧柔Biore防晒霜SPF50',
    'content': '终于又出视频啦~这次的妆容我个人感觉属于比较清爽系的，毕竟夏天了嘛，冬天不爱用的阿玛尼滴管最近天天拿出来用，好用的不得了，遮盖力又不错，质地又轻薄，这瓶快用光了，看来我要继续入一瓶才行啊~\nLB的眼线笔最近越用越喜欢，上色度堪比之前一直用的爱丽小屋，一直以为我的最爱是爱丽小屋，想不到有新爱了！LB 鲜奶油防水眼线笔\n新人的zoeva眼影南瓜盘，喜欢的不得了~颜色虽然比较适合秋冬，但毕竟新入手，就算夏天也要画一画才对得起自己。#ZOEVA\n对了，夏天防晒很重要，最近一直用碧柔这款防晒霜，保湿不油腻，看来整个夏天我要多囤几瓶才行啊！花王 Kao 碧柔Biore防晒霜SPF50\n好吧 一起看视频吧~还有我每日的头发内扣打理方法哦~\n#跟着视频画眼影#视频教你画底妆#乔治阿玛尼'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.com/FjaBtcXLUl8prDp7JGfKpErdRsqf_compress_L1',
    'video_id': '590954bd14de411e0a55cbfa',
    'title': '云海奇观',
    'video_tag_list': '',
    'content': '坐标江西寻乌项山'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/9195466f5d9e3fc66e62b090e252ef648bc9efda_r_ln',
    'video_id': '590982e9a9b2ed63ced73dcf',
    'title': '如何彻底清洗衣物上的口红渍',
    'video_tag_list': '',
    'content': '抹上口红总是性感动人，但是粘到衣物上就不可爱了哟~\n今天喵酱带来了专业口红清洗小妙招，不用太费力，轻松搓洗就能让衣服焕然一新咯。#视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/4b0725fe-1b7f543-bd9f-edbc78251bcc?sign=5786ea013d426f6bd3e58bdaa9b6d773&t=65fb06d4',
    'video_id': '590996c4a9b2ed62f1d73dd1',
    'title': '五一我们干啥去了？网红的欺骗餐+弹力带全身塑形训练',
    'video_tag_list': '8周变身比基尼女神;8周变身比基尼女神',
    'content': '#8周变身比基尼女神Weiya和giselle五一没闲着，比基尼女神特训营带大家十八班武艺练了两天；然后踏踏实实地吃了欺！骗！餐！弹力带是weiya和giselle健身包里不可或缺的工具，它对于塑造紧致小巧的肌肉线条很有帮助，而且体积小，便于携带；出差或者出游，都可以随时随地练起来。这套全身塑形的动作可以高效的锻炼到全身上下肢的肌肉，快找块空地，一起练起来吧。\n用具：一条弹力带（带把手或者不带都可以，重量的话，我用的是15磅，你也可以选择10磅的）\n时长：所有动作重复2遍，大概20分钟左右\n动作一：深蹲+三头屈伸 - 20次\n动作二：请安弓箭步+侧举 - 每侧20次\n动作三：弓箭步+划船 - 20次\n动作四：深蹲+颈后下拉 - 20次\n动作五：驴踢 - 每侧20次\n动作六：仰卧单腿上举 - 每侧20次\n整套动作重复2次，训练就结束啦\n请持续关注我们，八周挑战，5月继续!每天运动打卡#8周变身比基尼女神并@fit4life，八周之后惊喜大礼等着你！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lr10JsQn21Y_Qjf4bu77Hthiewnh_compress_L1',
    'video_id': '5909d322b46c5d498955a928',
    'title': '米兔+费雪床铃，让宝宝自己玩',
    'video_tag_list': '',
    'content': '我绝对是个懒妈妈，懒妈妈就要有让宝宝睡在小床上自己玩的方法。一个讲故事的米兔加一个费雪的旋转床铃，足够吸引宝宝玩上好一阵了。另外，米兔的发光耳朵实在是太可爱了！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/e656f844988e6f39e5452b73f4f9e8e03d9029ea_v1_ln',
    'video_id': '5909d40dd1d3b97304f175b0',
    'title': '我的哄娃神器4moms电动摇篮',
    'video_tag_list': '神器摇篮解放妈妈双手',
    'content': '即将在我家退役的电动摇篮，最后来一段影片纪念吧。最喜欢下午的时光把宝宝这样放在摇篮里，一边摇一边晒太阳。我家宝宝5个月，已经随时要从摇篮里越狱了😂#神器摇篮解放妈妈双手[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsbQ_Cr9mTlBeEc6nb4F5Xr_UIu5_compress_L1',
    'video_id': '590a0b24d1d3b969a1c9910f',
    'title': '【视频】NRC👍国家级教练传授的🏃跑步拉伸动作！',
    'video_tag_list': '跑步的乐趣',
    'content': '这个套简单的拉伸动作是我在Nike Running Club学习到的，授课教练都是国家级教练，专业性就无需质疑了。希望大家可以通过视频非常直观的学习到拉伸动作。❤️\n这个动作是跑前跑后均适用的，我们在NRC训练的步骤是\n1、慢速跑15mins热身，慢速很重要哦！不要急特别是温度不高时。\n2、就是这一套拉伸动作，由于视频时间有限我没有保持很久。自己在心中默默数30秒，身体两侧部位都要做哦。\n一共有5个动作，拉伸不同的部位\n1⃣️大腿后侧拉伸 先上下浮动，保持膝盖伸直，做到自己的即点即可 不要过度勉强哦，最后极限保持30秒\n2⃣️小腿后侧拉伸 ，脚尖回勾，后侧的脚和前侧的脚要保持平行状态\n3⃣️大腿内侧拉伸，用手肘使劲抵开大腿，利用外力打卡大腿内侧，拉伸\n4⃣️大腿内侧、后侧、侧腰拉伸，一条腿伸直脚尖回勾，一条腿弯曲向外展，手触摸反向脚尖，注意不要扭伤！不够柔软或者肌肉过度紧绷都容易拉伤，so 先适应性来回摆动，再到极限停留30mins\n5⃣️大腿前侧拉伸：这个姿势常见，重点是是否标准，注意两膝盖并拢，腰背挺直，千万别前倾，甚至可以用双手把腿向后拉更高\n其实还有一些加强版的拉伸动作我会再录一次视频。不过宝宝们还说先从基础做起哦！么么哒👄\n#见人不如健身[话题]##厉害了我的健身房[话题]##跑步的乐趣[话题]#\n#肌肉拉伸教程[话题]##肌肉拉伸视频[话题]##必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsXSZsWKyEBz3kCge6edNkgrCP1Y_compress_L1',
    'video_id': '590a8dd6d2c8a5382f440718',
    'title': '不二之选#超实用空调毯&手感软爆的北极熊抱枕（1/2）',
    'video_tag_list': '',
    'content': '自己超级喜欢的Liv Heart【超实用空调毯&手感软爆的北极熊抱枕】，在日本&中国都卖得超级好\n视频只能发5分钟，只能切断啦，后半段见下条视频～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ca0310e9b84b55397ed668d3b25331339b6b0179_r_ln',
    'video_id': '590a9df014de4160ad5aea27',
    'title': '史上最详细的饭团做法，为了孩子收藏吧！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n饭团在日本深受人们的喜爱，是日本人外出野餐以及午餐便当的首选食物。\n若是你自己亲手来做一份为自己量身打造的健康饭团，你一定会感受到一份温馨。\n★★★★★\n创意指数\n虾仁饭团\n▼\n虾仁饭团\n·视频音乐·\nChina、X - Vip Mix\n·食材·\n鲜虾、三丁\n米饭、黑胡椒、盐\n1.鲜虾过水变色捞出\n2.剥去外壳\n3.倒入1勺橄榄油、1茶匙黑胡椒、少许盐\n4.拌匀备用\n5.热油锅倒入三丁炒软\n6.倒入米饭后迅速炒散\n7.加入一茶匙盐、1茶匙黑胡椒\n8.大火翻炒至均匀，盛盘备用\n9.抓一把炒饭将虾仁包裹起来\n10.有了这个再也不怕小孩不吃饭啦~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/e6187ba828980e61339d865587c02124f4f4b6e9_v1_ln',
    'video_id': '590ae568a9b2ed37eda54bf7',
    'title': '还在买超市那些香蕉干？教你三步轻松自制香甜0负担香蕉干',
    'video_tag_list': '',
    'content': '女生们总是零食不离嘴，可是快到了夏天，想吃香甜的零食又担心发胖怎么办？\n今天喵招教大家自己在家，只要三步，也能做出超好吃0负担的香蕉干哟~\n#水果的有趣吃法[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/a5f5ec7537b2b5b0555dbc3c57692d61f7cf2a54_r',
    'video_id': '590ae67f7fc5b84ca845e76d',
    'title': '零失手微波炉快手红枣糕！',
    'video_tag_list': '',
    'content': '#罐头小厨# 微波炉快手红枣糕！想有无数种食物能让你越吃越瘦，可吃完又瘦又美的你肯定没见过~红枣燕麦一出手，健康美丽全都有~\n#叮！零失手微波炉食谱[话题]##下午茶必备小糕点[话题]##烘焙能手[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/968bb70f-8893b2c-a477-70892a7f3a32?sign=a402e77f5062de966ec90d78f23b74c5&t=65fb06d4',
    'video_id': '590b267834609473142778a6',
    'title': '健康饮食里的隐形卡路里｜自制希腊酸奶｜超虐燃脂',
    'video_tag_list': '8周变身比基尼女神',
    'content': '#8周变身比基尼女神[话题]#你有没有这种感觉，自己明明吃的很健康，但就是不见瘦，到底哪里出了问题？超市里的“低脂”和“高营养”的食品，热量就真的低么？本期giselle和weiya带你一一揭露那些所谓“健康”食品里暗藏的隐形卡路里。还有听说5月份fit4life的比基尼燃脂课程再创强度新高，一节课下来爆刷500大卡不是问题。不在北京不能来上课？没关系，本期quick burn我们精选了最经典的几个动作，让你在家一样练起来！8周挑战进行到第三周，你瘦了多少？快关同名公众平台Fit4Life健身与美食，并在微博上@fit4life 和我们分享吧！\n最后应大家要求，粽子节小长假（5月28日、29日）比基尼女神训练营现在开始招募啦，这次的主题是马甲线＋蜜桃臀，上次没有报上的同学这次要抓紧咯！\n那些隐藏在“健康食品”标签背后的卡路里…\n果汁\n超市里的大部分果汁都含有很高的添加糖，少数几款“纯天然，无添加蔗糖”的果汁，如果你仔细看配料表，就会发现这些都是用浓缩果浆调制出来的，而浓缩果浆中本来就含有大量的糖。\n此外，及时是鲜榨果汁，在制作过程中，水果中本身含有的营养和纤维也会大量流失，最后只剩下一杯有甜味的水，所以千万不要把果汁当做水果的替代品。\n如果觉得喝水太无聊，那就来一瓶苏打水吧，在这个炎炎夏日，还有什么比这更解渴的？\n早餐麦片\n超市里琳琅满目的早餐麦片，尤其是那些口感丰富添加了各种干果的即食麦片， 它们打着“低脂”“降血脂”“高纤维”的标签，让你以为自己吃的很健康，殊不知在不察觉中已经吃进去好几十克的糖。\n建议大家在选购麦片时，去买那种没有任何添加的天然燕麦。天然燕麦含有丰富的维生素和膳食纤维，饱腹感超级强，翻看往期视频有各种燕麦的做法哦！\n酸奶\n市场上琳琅满目的酸奶产品，打着各种“0脂肪”和“益生菌”的旗号，给大家一个误区，以为“低脂”就等同于“低热量”。其实如果仔细阅读食品成分表或者营养表，你会发现，这些所谓的健康酸奶，热量却一点也不比正常酸奶来的低。因为商家在制作“低脂”酸奶的同时，往往会在里面加入大量的糖以保证口味，更不要提那些我们都叫不上名字的食品添加剂了。\n建议大家像我们一样买一个酸奶机，自己制作完全无添加的酸奶。如果喜欢浓郁的口感，那就不要嫌麻烦，多添一道工序，滤掉乳清，自己做美味的希腊酸奶吧！（做法见视频哦）\nfit4life实体店的比基尼塑形和燃脂课程由两位网红阿姨亲自设计和教授，是店里最受欢迎的课程。从试营业到现在两个月，已经有无数姑娘看到了身材的明显改变。燃脂课的动作每个月更新，为了让散落在祖国乃至世界各地的你们也能体验到我们的“用心良苦”，本期视频精选了6个动作，让你在家也可以跟着一起“受虐”哦！\n动作一：波比跳＋箭步跳 （x10）\n动作二：平板撑＋转体 （x两边算一次30）\n动作三： 开合深蹲跳 （x20\t）\n动作四：内外平板跳＋“蜘蛛”俯卧撑 （x10）\n动作五：俯卧撑＋摸肩 （x10）\n动作六：箭步跳至高抬腿 （x每侧10）\n动作之间不休息，全部做完休息30-60秒，重复三遍\n家庭作业：\nkeep HIIT适应性训练 1次\n本期视频训练 1-2次\n8周挑战第四期“蜜桃臀”训练1-2次'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltMdm-7UEPN6h84ZQkvTU-WTsIoK_compress_L1',
    'video_id': '590bd99ed1d3b9756e31fa87',
    'title': '如何用拳头大小的mini细缝收纳100件杂物？（1/2）',
    'video_tag_list': '',
    'content': '因为拍的角度太刁钻了，所有有一些手持相机的镜头有些晃，大家见谅呀～视频后半部见下一条～\n#收纳神器[话题]#\n#买了不后悔的家居神器[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lp_i3pO9KQZ4MQTpU_sCZiuqRRYP_compress_L1',
    'video_id': '590bda11b46c5d5b7ec27092',
    'title': '如何用拳头大小的mini细缝收纳100件杂物？（2/2）',
    'video_tag_list': '',
    'content': '接上部视频～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvWoChU-lIktUFjCh1cK0AKOY-4X_compress_L1',
    'video_id': '590be839b46c5d1d91db1954',
    'title': '豆爷的➕餐：腌笃鲜😎———我有一个坏妈妈',
    'video_tag_list': '小红书萌娃大赛',
    'content': '我错过了什么！！竟然我也可以发小视频！！！\n#小红书萌娃大赛[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lj_HePgoEsbjA4Pexdldrpqc7HAY_compress_L1',
    'video_id': '590be9b1d1d3b9463831fa7c',
    'title': '豆爷怒吃草泥马———我有一个小气的妈妈',
    'video_tag_list': '小红书萌娃大赛',
    'content': '这是红豆的阿如爸爸从遥远的马丘比丘带回来的新鲜草泥马\n然而我给红豆玩了玩\n她表示出了又爱又恨的样子…\n豆豆这只草泥马很贵的啊豆豆………\n#小红书萌娃大赛[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/f413e9efb51aa841925a72d491065fb4261f3aa8_r_ln',
    'video_id': '590beae4d2c8a542c39312dc',
    'title': '0失败超滑溜的日式茶碗蒸，宝宝老人都爱吃！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n茶碗蒸（ちゃわんむし），日式蒸蛋，日本风味小吃的一种。茶碗是日文汉字，即茶杯的意思，茶碗蒸听上去花头花脑，其实就是日式炖鸡蛋。\n在日本茶碗蒸名气很响，是日本料理中女人和孩子最喜欢吃的菜肴之一。它是一款体现主妇手感和美术才能的浪漫作品，在家里做也简单。\n★★★★★\n创意指数\n茶碗蒸\n▼\n茶碗蒸\n·视频音乐·\nTrace Bundy - Lullaby on Three\n·食材·\n鸡蛋、鲜虾仁、玉米、香菇\n柴鱼高汤、昆布酱油、味淋、葱、清水\n1.鲜虾仁过水变色捞出\n2.打入3个鸡蛋\n3.倒入一勺昆布酱油、一勺味淋、150ml柴鱼高汤、50ml清水\n4.搅拌均匀备用\n5.过筛去除杂质\n6.倒入茶碗蒸移入蒸锅，中火蒸8分钟\n7.香菇切片备用\n8.打开锅放入香菇片、虾仁、玉米粒\n9.关盖转小火蒸5分钟\n10.最后撒上葱花点缀\n11.好看又好吃的茶碗蒸就完成啦~！\n#周末家常菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/e757e54f-974d7c6-88ed-2ba76cbff81a?sign=9d28bb128e6eaf25c7f18c34a3dec006&t=65fb06d4',
    'video_id': '590bf1467fc5b853e8d20c22',
    'title': '打造马甲线的腰腹核心中级训练',
    'video_tag_list': '',
    'content': '这套中级训练动作开始有一点难度了，跟着坚持下来你会明显感觉到腹部在燃烧，小红书的小伙伴们，马甲线小蛮腰正在向你招手！赶快跟着火辣健身练起来吧！#必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llPEQIU2Eh_J_WnDuVKtvtucqshB_compress_L1',
    'video_id': '590c568e14de4167507851fe',
    'title': '刚出炉的会动的蛋挞！',
    'video_tag_list': '蛋挞在家这样做',
    'content': '蛋挞什么时候最可爱？\n我以为、刚出炉的时候，蛋挞一鼓一鼓、噗噜噗噜，炒鸡可爱啊！\n#蛋挞在家这样做[话题]##在家做甜品[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lp2MuwK-yKsDeirhiwNXm982PJ3T_compress_L1',
    'video_id': '590ca189b46c5d0ae35c8cb0',
    'title': '【Adora妆容视频】逆龄欧美妆在此',
    'video_tag_list': '嗨爆音乐节的妆容',
    'content': '前几天po滴#嗨爆音乐节的妆容[话题]#在此视频部分呈上，使用全部产品如下：\n眉毛\n打底 farsali的unicon essence\n粉底 \n遮瑕 tarte 海洋系列遮瑕液\nit cosmetics byebye undereye黑眼圈遮瑕\n修容\n散粉 塑颜光彩蜜粉\n眼影huda beauty eyeshadow platte\n眼线笔\n高光glow kit\n唇彩tarte 夏季新款 festival\n刷子tarte unicon brush'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/713c08d6547c9eb59aa9857220f479aed71f6a40_v1_ln',
    'video_id': '590d3aa4a9b2ed1b755612d4',
    'title': '自制运动饮料，非常适合正在健身或运动减肥的小伙伴们 - 视频教程',
    'video_tag_list': '',
    'content': '今天我来分享一款自制运动饮料的做法，制作非常简单，能快速补充运动中流失的水份和微量元素，非常适合那些近期正在健身或运动减肥的小伙伴们。\n你可以根据自己的喜好来选择水果的口味，最好选用柑橘类水果，因为富含维生素C和钾元素。\n我们在运动的时候会流失很多水份和微量元素，只喝水是很难快速补充回来的，所以需要运动饮料让身体快速恢复，避免出现脱水乏力等现象。\n我分享的这款自制运动饮料能让你及时补充水份，以及钠、钾、钙、镁等微量元素，以后不用买加了防腐剂香精等添加剂的运动饮料啦！\n记得喝前摇一摇哦。\n#适合夏天的饮料[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liYe1Hmr4vffjNHHBQryrHAdq00E_compress_L1',
    'video_id': '590d47a7d2c8a50d5ec86598',
    'title': '东京超酷airbnb-表参道房车',
    'video_tag_list': '酒店控or民宿控;酒店控or民宿控',
    'content': '在东京的两天住在南青山Commune 2nd里的房车，空间不大，设施齐全，出门就是美食美酒和南青山表参道的繁华～特别棒～具体介绍看之前的长笔记哦，预定在airbnb上搜caravan tokyo就行啦！价格差不多是1300一晚，性价比不算特别高，不过体验很好！东京的住宿比较贵，普通酒店也要上千啦，所以不如来点不一样的。#设计感超强的民宿[话题]##最美民宿[话题]##酒店控or民宿控[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lndviy05jCJDIDsMmV-TPn2_rZ6Z_compress_L1',
    'video_id': '590e750ed2c8a578cc302111',
    'title': '任人蹂躏的小胖猫',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '哈哈哈哈哈哈昨天带我家福虎去打疫苗，医生一摸她肚子，说 ：“哎哟喂小肚腩都出来了。是…有点胖了”哈哈哈哈哈哈哈才四个月就四斤了简直福猪，脸还堪比柴犬，可以捏捏捏捏，真是太可爱了[得意][得意][得意]#我家宠物最萌的瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FhmwtrAnJOBXrv2o2WgbSooRUzZk_compress_L1',
    'video_id': '590ef07d14de416191718c42',
    'title': '哈哈哈哈😄😄😄⛳⛳健身餐吃得好有力气💪💪',
    'video_tag_list': '成都;周末去运动',
    'content': '这是我用TaylorMade M1 XT6S杆身干出来的，工坊模拟器测落点244码，距离265码。💪💪👏👏\n #周末去运动[话题]##健身靠装备[话题]# #高尔夫[话题]#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lmwBWMcsoufDQefutrL-_9s5gwU7_compress_L1',
    'video_id': '590eff4814de412d11718c3d',
    'title': '带大家逛逛英国大型宠物展🐶第一次编辑视频，多多支持喔😘',
    'video_tag_list': '我和宠物的日常;英国;伦敦',
    'content': '这个活动是英国最大的宠物展，在伦敦ExCeL展览中心，除了平常看到的猫猫狗狗，还将有机会看到其它各种各样的动物。6号/7号两天的宠物展，里面最吸引人的应该就是神奇的宠物表演，包括rabbit show jumping（兔子马术），duck herding dogs（牧羊犬赶鸭子），birds of prey display（鸟猎食表演）和Super Dogs Live超级狗狗们的现场表演。里面有狗，猫，鼠，兔，爬行动物，小马，鱼，鸡, 羊驼或龙猫，这里除了表演秀，还有对动物教育性的讲解或者展示，还有个特别市场，卖一些跟宠物有关的用品。\n我拍了20分钟的视频，最后剪辑到5分多才能上传到小红书，心在滴血呀😂😂但是大致内容我都拍到了，大家先感受下啦♥️\n#我和宠物的日常[话题]##我家宠物最萌的瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luAgjjtGfqg2aEBTEg_oHd1wpryp_compress_L1',
    'video_id': '590fe896d2c8a5264bc07e46',
    'title': '#ELLEMAN 时装编辑为你推荐！',
    'video_tag_list': '高田贤三;D二次方;冰岛;一周T恤不重样',
    'content': 'ELLEMAN X 第五系 | 不穿得好看，怎对得起春色如许？\n这次特别邀请了 ELLEMAN 的时装编辑 沈洁涯 Sherry Shen为男士们进行推荐搭配。\n━━━━━\n搭配信息:\n单词印花简约T恤_DSQUARED2       ¥1780\n纯色牛仔豹纹领夹克_KENZO     \t¥3780\n细格花纹拉链休闲裤_ICEBERG  \t¥2790\n(以上单品均可在 App:第五系 中购买)\n“不费力的搭配”是目前时尚界最为崇尚时髦宗旨。本套着装搭配选取了多条当下最时髦的元素，均能体现不过分用力就能时髦指数翻倍的“不费力”精神。这是一套适合大多数场合的着装。一周七天都可以穿着它出门。\n—— Sherry Shen\n#男人这样穿才型[话题]##每日穿搭[话题]##约会必胜装[话题]# @小红叔  @穿搭薯 #一周T恤不重样[话题]##我爱牛仔元素[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/7ead98bfc424330760eab322ade5c0bc95dad740_v1_ln',
    'video_id': '590fec6ca9b2ed4a2364884d',
    'title': '电熨斗的4种高能用法！',
    'video_tag_list': '',
    'content': '#夹脑计划#电熨斗的4种高能用法！用来烫衣服简直大材小用，夹脑计划带你解锁电熨斗的4种高能用法，电熨斗我们走，你就是居家小能手～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lin6bN9lTij3jfI-dPQ9ZHmBY4tU_compress_L1',
    'video_id': '590ff3bbd1d3b93f6b68e7ed',
    'title': '自己的尿布自己背🤣Cathkidston的宝宝印花双肩背包',
    'video_tag_list': '凯茜·绮丝敦;凯茜·绮丝敦 Cath Kidston 女士印花双肩包;宝宝日常穿搭指南',
    'content': '大王们自由的灵魂不喜欢被防走失包所束缚 所以之前买的带牵绳的都进冷宫了 他俩比较喜欢cathkidston的印花双肩包 容量感人 平时出去他们都是自己背着水壶和一两张尿布 帮妈妈减轻一点负担😂\n我是在实体店买的 打折的时候RMB150一只 天猫有旗舰店大家自行搜索😈\n优点是表面采用了防水的材质 比较抗造 而且夏天的时候也不会吸汗 脏了湿布擦一下就干净了 最重要的还是颜值高 车车啊花花啊款式图案很丰富 宝宝肯定会喜欢😎 有大人同款的（小红书里也有 链接在下）背上街萌萌哒 回头率↑↑↑👫\n\n#宝宝早教这么做[话题]##宝宝日常穿搭指南[话题]##宝宝穿搭打卡[话题]##夏日包包[话题]##出街最爱的包包[话题]##千元以下的好包包[话题]##随身包包大搜查[话题]##母婴好物大推荐[话题]#\n@薯宝宝'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/920056c2-7d196f7-93a2-4da02bec686b?sign=29fa349b56e55b03cac16a19dcb39a3c&t=65fb06d4',
    'video_id': '59102016a9b2ed3d5568bf80',
    'title': '王者荣耀玩腻了？试试乐高实用新玩法',
    'video_tag_list': '',
    'content': '#夹脑计划#乐高实用新玩法！小积木大能量，玩法其实很多样，从今天开始你的生活被乐高承包啦~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llYL5sGP3MoXcAZcz_Iic302jgfo_compress_L1',
    'video_id': '59105c6fb46c5d1a7edec89e',
    'title': '办公室的这个小东西，居然能解决你30%的收纳烦恼',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lovvVyUwmzfvVcTgrVe59JCMiELX_compress_L1',
    'video_id': '59105c9ad2c8a53e5d93e48c',
    'title': '宝宝吃柠檬',
    'video_tag_list': '',
    'content': '妹妹你这个表情也是赢了全场😂😂我做水果茶剩下的柠檬自己就拿起来吃了！\n# 萌娃最爱   # 宝宝辅食食谱   # 吃货小分队   # 节后瘦身必吃TA   # 大爱水果季   # 自制水果茶\n#萌娃吃播视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnwusXosqtPGhj-GdLo7wyRFHEVr_compress_L1',
    'video_id': '59109050d2c8a538079e0594',
    'title': '香港 攻略 美食 美景 🇭🇰',
    'video_tag_list': '',
    'content': '这是视频版，看我笔记里面有图文版哦😊☺'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loertF8qcyNiTqE4Z5FRCqvQRh5l_compress_L1',
    'video_id': '591112d0d1d3b947adce304e',
    'title': '0基础初学爵士舞',
    'video_tag_list': '',
    'content': '这段话献给所有女孩子\n[飞吻R]一直都认为会跳舞的女孩很有魅力  很羡慕的\n但是因为家庭的原因 从小都没有上过什么培训班\n后来因为想学就去报了培训班  每天坚持基本动作听节拍练舞\n没几天就爱上了跳舞哈哈\n跳舞能使人心情变好  现在都好后悔失恋没去跳舞  不然早就康复啦\n跳舞心态很重要   一定要喜欢跳舞才能学会跳舞  因为跳的时候是不能分心 要保持好心情[得意R][得意R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lv0MmREyxHq5Kbd-gTySq8zphpeO_compress_L1',
    'video_id': '59121cf2b46c5d1dd84dafb8',
    'title': 'Jenny厨房之卤牛肉牛筋牛尾（内附步骤）——超香且入口即化',
    'video_tag_list': '用视频记录美食',
    'content': '因为夜晚拍摄，视频可能颜色深一点，但是已经获得老曹好评，比上次更好吃[笑哭R]好吧。我尝了一点，嘴巴到现在还粘粘的，真的很好吃。\n视频中间有几十秒黑屏[惊恐R]我也不知道咋回事，不要换台，要接着看[色色R]\n这次我把肉煮的烂一点，因为考虑到Jimmy喜欢吃这种，我也爱这种，家里大人更喜欢吃有嚼劲的，所以时间亲们要控制好。\n下面说重点\n食材：[飞吻R]牛腱（带牛筋），牛尾中断，牛筋，葱，生姜，花椒，八角，香叶，桂皮，茴香，辣椒，白芷，陈皮，山楂，百里香（新鲜的），枸杞。\n[得意R]料酒，生抽，老抽，冰糖，醋，鸡精，盐。\n步骤：\n[害羞R]首先准备食材后，沸水一锅，把牛筋牛尾牛腱过水再洗净\n[得意R]把所有材料放进高压锅，用大火烧，等煮沸后尝一下味道，然后决定是否需要加某种调料（我放入了新鲜的百里香，可以去腥味，味道也很好，可以tb买盆栽，很便宜，可以顺便把迷迭香也给买了）\n[飞吻R]盖上高压锅，小火煮，大约3小时，可以关火准备开锅啦！\n就是这么简单！\n如果想要多煮一点，隔天吃或者放冰箱之类的，不要放在放多的卤水里，因为这样颜色会越发深并且会越来越咸，所以要酌情考虑。\n像我煮的基本就两天吃完，所以我会把肉放在一半高度的卤水里，等室温之后裹上保鲜膜放入冰箱冷藏即可。\n[萌萌哒R]这个时候的牛筋q弹，入口即化，太好吃！牛尾炒鸡香，一点腥味都没有。\n另外\n卤好之后的这些可以做\n卤牛肉饭\n卤牛肉面\n卤水拼盘\n冷吃热吃\n想怎么吃就怎么吃\n上班族回来做完可以吃几天不会腻，只要你会方法变样，营养美味，rio简单哈！同样小孩子会hin中意！\n❤\n我不是专业选手，请勿喷，欢迎提意见。\n#美食才是人生主角[话题]##爱上我的厨房[话题]##我的私房菜[话题]#\n#用视频记录美食[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lo_sUxqETKJM74il7Kad5CEvm7EX_compress_L1',
    'video_id': '59121f7614de410b46ed2cd6',
    'title': '',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '#我和宠物的日常[话题]##我家宠物最萌的瞬间[话题]##吸猫[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lszdL3h-z594j8EGn846g1nF50xw_compress_L1',
    'video_id': '5912698dd2c8a504846b4057',
    'title': 'Olly的日常 - 5M',
    'video_tag_list': '',
    'content': '奥利小哥哥五个月啦🌟\n黑黑胖胖茁壮成长中🤣'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lidxMLZN_5JELEAs5COROLDXt1qG_compress_L1',
    'video_id': '59127658d1d3b91f0af53fad',
    'title': '笑到抽筋的《银河护卫队2》',
    'video_tag_list': 'Funko 树精格鲁特手办',
    'content': '全程承包萌点的小Groot～不剧透了～大家自己去看吧～科科～😉😉\n梗概是：星爵终于解开了身世之谜&银河护卫队的又一次团建（觉得自己概括能力简直爆表！）💃🏻💃🏻💃🏻\n外行看热闹的我觉得场面还是很大的～特效什么的没毛病～看3D版本也不会头晕眼花～还是值回票价的～🎉🎉🎉虽然超级英雄类电影一般情节都是硬伤，但这部有萌点有泪点，这点对于我来说就够啦！😋😋很合格的爆米花🍿️电影🎬！\n祝大家都看到好看的电影～💖💖 @娱乐薯\n#银河护卫队2[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lv6S5fMydQYxfyfoIgeP78ektePz_compress_L1',
    'video_id': '5912c5ac14de412edaed2cdc',
    'title': '3个月零27天，坐着高铁去西安啦！',
    'video_tag_list': '',
    'content': '下午4个半小时的车程正适合花森\n因为他是下午睡两个小时，傍晚再睡半小时的宝宝'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/9456903789cda536d537e35d71cd7d9f138328e9_v1_ln',
    'video_id': '5912e506a9b2ed6eb1260891',
    'title': '教你基本的西餐礼仪，如何正确优雅的吃西餐',
    'video_tag_list': '',
    'content': '享用西餐时却不知道西餐礼仪？拿着刀叉对着餐盘胡乱挥舞的话，会像个原始人。在宴会、餐厅或者较为正式的场合，你需要学会正确而优雅地使用刀叉！\n今天喵招教大家欧式的简单西餐礼仪，希望能帮助到大家哟~#视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmKNqKbGoDoCCGbOkiTSiPpvxLIW_compress_L1',
    'video_id': '5913d26fd1d3b93a1a6ee5d8',
    'title': '丢不掉这件东西，看再多收纳方法都白搭',
    'video_tag_list': '',
    'content': '为啥看了别人的收纳，还是无从下手？那些抱怨自己衣柜太小的看这里～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgLRuyfROwHvtrMKvEkCyUL231CK_compress_L1',
    'video_id': '5913eeb4d1d3b96a737fc3c6',
    'title': '入夏午后的惬意',
    'video_tag_list': '',
    'content': '一群英短，惬意的午后，我们互相陪伴，有辛苦但是快乐更多，这才是生活嘛[飞吻R]'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/59e5b868-794320f-ab56-4882302cc90b?sign=c1e1164537185197b0f48647c84bafb0&t=65fb06d4',
    'video_id': '5913f59a7fc5b82c56e5e19e',
    'title': '脂肪到底该不该吃？｜为啥我一减肥就不来姨妈了？',
    'video_tag_list': '8周变身比基尼女神;8周变身比基尼女神',
    'content': '#8周变身比基尼女神[话题]#为什么我一减肥就容易不来姨妈？Weiya和Giselle经历过一样的事情，在最开始减肥的时候只吃水煮菜胡萝卜和水果，然后几周下来姨妈不来了，皮肤也变得松弛粗糙没光泽…这一切，原来是因为我们脂肪吃得太少了！脂肪对女生太重要了，吃不够”健康脂肪“，吃再多的橙子也无法补充维生素；而且姨妈会变得超级不准！不吃脂肪还会让我们的皮肤变得粗糙松弛，新陈代谢也会降低。。。但是吃多了脂肪又怕胖，该怎么办？快看本期视频Weiya和Giselle是如何轻松把”健康脂肪“融入每日食谱的。\n比基尼女神八周挑战继续，更多的训练和饮食干货，请关注我们的同名全平台\nfit4life健身与美食！每天运动打卡#8周变身比基尼女神[话题]#并 @fit4life, 八周之后惊喜大礼送给你！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/c16684ffc0bd07d4df8f00512894233e58774f79_r_ln',
    'video_id': '5913fb587fc5b849a445dd37',
    'title': '马甲线入门训练指南',
    'video_tag_list': '',
    'content': '想要马甲线小蛮腰？你得好好练练腰腹核心了，这是一套初级训练动作，难度不大，每个人都可以尝试。更丰富更完整的训练计划欢迎下载「火辣健身app」，或者微信关注「火辣健身」。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkbGkzDy-Y4ez2jJBNI6Cgyy8P9V_compress_L1',
    'video_id': '5913fd32d2c8a56349729fa9',
    'title': 'smashbox metallic眼影盘',
    'video_tag_list': '新手最容易上手的眼影盘',
    'content': '朋友推荐入手的，也是youtube美妆博主tati很喜欢的一盘。不是这个系列里最热门的色号，颜色有点骗冷，很闪～好上色也不怎么飞粉～～感觉可以用它画出不同的妆～～包装很有趣#眼妆测评[话题]##新手最容易上手的眼影盘[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llhuGtgoxoLgYzPSKzPoqNBcF6yZ_compress_L1',
    'video_id': '591400fc14de410f4f6af819',
    'title': '某个两面派和nunu分零食🙄',
    'video_tag_list': '',
    'content': '人前人后完全是两幅面孔🙄真应该跟着他爸好好接受再教育🌚'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luuL6GIeE8tt5tIBPRpyeoNAhJj9_compress_L1',
    'video_id': '591402d2b46c5d41be4d11b7',
    'title': '爱马仕展览video',
    'video_tag_list': '',
    'content': '拍了一些视频做了剪辑给大家\n笔芯❤️ @薯管家'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loKN443BDB-165J7PZ95IY4VY1wv_compress_L1',
    'video_id': '59141051d2c8a51fd6599644',
    'title': '哥哥实力演绎最爱零食~嘉宝Garber切达奶酪玉米泡芙条',
    'video_tag_list': '嘉宝;萌娃最爱',
    'content': '金牛座最爱什么？吃吃吃！所以老天送给我一个能吃能睡的小🐷哥。而哥哥目前最爱的零食就是嘉宝的奶酪芝士条，这应该是很多小宝宝的挚爱吧～\n我查了配料（妈妈职业病），主要成分是谷物粉、谷物油、奶酪调味粉、淋磷酸三钙（一种安全的钙强化剂）和维E，所没有不该有的添加剂，但每7g含50mg的钠，妈妈们还是要控制小宝宝的摄入量。\n我们家是从10个月左右开始引入零食的，虽然零食还是要控制为妙，但宝宝开心满足的小胖脸更让我神魂颠倒[色色R]（还是要控制）～嘉宝的其他产品像星星泡芙啊车轮饼啊都很好，但我家还是最爱这一款，我也很爱吃，经常在车上跟他们一起吃，所以这款是家中常备，童叟无欺[吧唧R]。\n每次光盆了都超级不舍，我让哥哥把空罐子扔到垃圾桶去，他扔了好几遍都没成功，扔之前还要猛吸几口，看看商标牢牢的把它镌刻在心中，“嗯，下次还是你哦”，哈哈哈[笑哭R]。\n#宝宝辅食食谱[话题]##萌娃最爱[话题]##零食发现家[话题]##小红书萌娃大赛[话题]#\n@薯宝宝'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/f3114412-1286192-a07c-d4b9b2972bd7?sign=666c0640cc181fa561e73a2aa005af4e&t=65fb06d4',
    'video_id': '5914105a7fc5b8546545dd37',
    'title': '不面试个100多家公司，你根本听不懂HR的这些话~',
    'video_tag_list': '',
    'content': '弹性工作待遇高\n发展前景大大滴好\n还觉得是好话你可就大错特错啦\n只做傻白甜，迟早被坑又被骗\n帅无敌教你解锁职场谜语\n再也不怕掉坑里~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fqoo90oFB8ar62M-NkLRKv_Hqyb8_compress_L1',
    'video_id': '5914425014de4139216af81e',
    'title': '再来一段兄妹情深版的～嘉宝切达奶酪玉米泡芙条 Yummy😋',
    'video_tag_list': '小红书萌娃大赛;嘉宝',
    'content': '上条笔记哥哥的馋样儿大家看够了吗 再来一条兄妹互喂版的 如果一只能这么相亲相爱就好了😝\n#宝宝早教这么做[话题]##萌娃最爱[话题]##小红书萌娃大赛[话题]##零食发现家[话题]#\n@薯宝宝'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqGsYmPHoZ37VdljwgW2H4a0p21T_compress_L1',
    'video_id': '59147d7db46c5d0ba962a24d',
    'title': '猫也会做梦哒',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '猫真的会做梦，不信看视频，小尾巴摇的，估计梦到吃好吃的罐头了😂#我家宠物最萌的瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhz3rN_NM0YM2ZPL9BVeeTYX3qcH_compress_L1',
    'video_id': '5914aaca14de416d706af81c',
    'title': '#桃花眼妆怎么化#视频—资深堂眼影pk403，樱花美过桃花',
    'video_tag_list': '',
    'content': '今天分享的是比桃花妆还更清纯的樱花妆🌸\n整段视频因为太长就直接剪成了眼妆部分的节选\n资深堂pk403三色的各种用法都有详细的示范讲解\n浅樱花色的各种用法就是妆容➕分的关键\n一点点的不同就变成了点睛之处\n也许你不知道，\n用在鼻子上，耳朵上，嘴唇线上，和嘴唇上\n出来的效果简直是意想不到\n超美的偏光色\n上到脸上对的位置可以让脸部皮肤和轮廓更加的柔和\n面部色彩也可以更加的灵动\n一样的产品不一样的用法可以让同样的妆容出来更不一样的效果\n快上车吧\n邱哥带你变成彩妆大神\n善于利用你手中的化妆品\n打造出更美的效果\n用到极致，什么妆你都会化了。\n#桃花妆眼影教程[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lu2maKBSadltMrUwFQjcQnP0s26c_compress_L1',
    'video_id': '5915094bd2c8a55d37729fb3',
    'title': '一秒变腹肌大法',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkcRpIZEB104PaIUHwaIg2wJN54R_compress_L1',
    'video_id': '5915250bb46c5d593d62a247',
    'title': '最近大家问的比较多的船袜、连裤袜的叠法都在了',
    'video_tag_list': '',
    'content': '最近问的比较多的船袜、连裤袜，还有如何分辨颜色相近的T恤，我的建议和方法都在这了。以后想多出这样的小问题集锦，大家可以多交流哦[吧唧R][吧唧R]其他的等我慢慢拍吧[偷笑R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkDy0vgwLPaXsksoRrDVIBS7Z2Bk_compress_L1',
    'video_id': '591528a6d2c8a5450e599634',
    'title': '超薄pizza来了',
    'video_tag_list': '',
    'content': '棒约翰0.1比萨来啦！多了一个更爱Pizza的理由～超薄饼底香脆可口，浓香芝士回味无穷，这个夏天你一定不能错过的美味，真的好好吃，大家可以去尝尝哈'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loKfEbXxqCpZDra6HWBMURsZgAit_compress_L1',
    'video_id': '5915806bd1d3b9463982d82d',
    'title': '笼养还是散养，这是一个问题',
    'video_tag_list': '我和宠物的日常',
    'content': '笼养还是散养，这真的是一个值得思考的问题！\n好多猫友问我，到底是笼养还是散养，我可以不经考虑的告诉你～散养，散养永远是最佳的养猫方式，换一个观念，把你关笼子里，你会快乐吗？\n我家面积不大，现在房价可以说是很贵，但是我还是保证了母猫完全散养，公猫只有晚上的时候才会放在笼子里（因为我的猫没有绝育，而且家里面积确实不大，我也有苦衷），但我白天猫全都是散养的！散养的猫是快乐的，自由的，每天跳跳跑跑，四肢也是健壮的，肌肉线条也很明显（英短确实胖胖的可爱，但是品相好并不是和胖挂钩，肥胖只会给猫咪带来负担,严重引发健康问题）\n对于宠物家庭，没有打算让猫咪生育，并且适龄绝育了的情况下，可以完全散养，猫不会闻到异性的气味而发情乱尿打架，这些情况基本可以避免。有时候猫也孤单，有个猫互相陪伴，是很好的选择。\n有的猫友说，不关着会掉毛，我家也会掉毛，既然考虑养猫了，又付诸行动了，就要提前考虑好这一问题，而不是等养了，发现hold不住了，这是很不负责任的表现。换毛季掉毛完全可以解决，勤洗澡勤梳梳，用较高级较专业的宠物香波可以缓解，实在不行剃了毛穿上衣服，这些都是解决办法！\n所以哦，不要问我散养好，还是笼养好，因为你已经知道答案了，猫是喜欢舒服享受的动物，不喜欢被束缚，当然偶尔也要束缚一下。cat fancy并不是养殖场的概念，所以哦，无论是作为宠物还是服役做种猫，请给他提供一个好的环境，因为她们的世界里只有你#我和宠物的日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Frlu6QNNodMGXcUuPbwSTkceQAkJ_compress_L1',
    'video_id': '5915a13fb46c5d3578c84be7',
    'title': '减轻劳动负担的桌面吸尘刷头',
    'video_tag_list': '',
    'content': '谁都不是天生爱干活，顺手的劳动工具绝对能减轻很多负担[赞R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FshiIgYbPy1f6ZTDy-a_mzxxrRDU_compress_L1',
    'video_id': '591661b714de414d61b77aad',
    'title': '超凶！',
    'video_tag_list': '',
    'content': '哈哈哈 每天被小家伙逗乐'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/854x480/vcodec/libx264/pgc/78d1e3fc-16af62c-8ab6-5ca4962909be?sign=6e2ecc4f8aaa9a49cd36a2e55ce4997c&t=65fb06d4',
    'video_id': '591668b534609452553dbf6b',
    'title': '10支Tom Ford热门口红 | 无滤镜试色',
    'video_tag_list': '最显白的口红',
    'content': '好久不见！好想你们呀！\n我终于忙完期末考试啦~这个视频是10支sephora八折购入的Tom Ford口红试色，色号都写在视频里啦吼吼~\n我的暑假马上就正式开始了！立flag：这个暑假做一个高产的博主！\n如果有什么想看的主题别忘了留言告诉我哦~\n#人民的唇色[话题]##最显白的口红[话题]##最显白的口红[话题]##最滋润的口红[话题]##黄皮最爱的口红[话题]##素颜最适合的口红[话题]##欧美系口红推荐[话题]##豆沙色口红试色[话题]##春夏最爱的清新口红[话题]##无滤镜口红试色[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llRm3h2XK9dTjl-DnksmwaZIC39J_compress_L1',
    'video_id': '59168996d2c8a50a4614f09d',
    'title': '大巨蟹老师下课之乱舞哈哈哈哈——克罗心➕J brand',
    'video_tag_list': '爱马仕;克罗心;J Brand',
    'content': '我就是爱克罗心！！！！！！！\n身上是m号哈！\n第一次买m，以前都是s号，不同上身效果❤\n短裤J brand，也是死忠粉！\n25码哦！\n下课依然很high！\n今天教学生们唱英文歌嘞！\n❤❤❤\n拖鞋\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lheKzANpZ2Vqq0pi2UaYiCGHmFW1_compress_L1',
    'video_id': '59168d2ed2c8a5181814f098',
    'title': '＃我和宠物的日常#呆萌比格汪',
    'video_tag_list': '我和宠物的日常',
    'content': '视频第一弹送给我的宝贝儿子十一郎～几个小绝活拿出来遛一遛～小崽子看见吃的那两眼的光芒呦！我是一天不逗他就觉得心里空落落的😛\n#我家宠物最萌的瞬间[话题]##我和宠物的日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fm7WHHECkupLSpUqSiV-LO6BhCUT_compress_L1',
    'video_id': '59169e9314de417ac4b77ab4',
    'title': '美美的户外婚礼',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FnchDdTIGbpLl28YWhjShMiFCzJX_compress_L1',
    'video_id': '5916a0afd1d3b92edbca1e22',
    'title': '这家店的出品有点可爱',
    'video_tag_list': '',
    'content': '想看探店的深圳童鞋举个手！\n低于30人我就懒得发啦～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lj_paLWyPzA83zwZOX2iMxoNpDe5_compress_L1',
    'video_id': '5916cb00b46c5d6f4d4566a4',
    'title': '宠物小精灵',
    'video_tag_list': '',
    'content': '现在都学会看电视了😂😂'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/720x404/vcodec/libx264/pgc/22fc819a-844b8bd-adf1-8ea956b48a3d?sign=6519d75a02553d12b08cfc45560e9df1&t=65fb06d4',
    'video_id': '5916f3e87fc5b84594709a93',
    'title': '和陌生男银一起跳了个飞机……',
    'video_tag_list': '',
    'content': '自从能发视频后~一发不可收拾！以前的视频全都翻出来咔咔咔！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lq2J69ZJxIm1x2y5Dwc6HEVLAzrW_compress_L1',
    'video_id': '59172958d2c8a536b114f09e',
    'title': '母亲节亲手为麻麻插一个花篮是不是够有诚意',
    'video_tag_list': '',
    'content': '明天就是母亲节了，一直不知道该送妈妈什么礼物，今天带妈妈去小伙伴的花店参加花艺课，亲手为妈妈插了美美的花篮，希望所有的妈妈都能像鲜花一样永远美丽，希望妈妈慢一点变老，慢一点，再慢一点…'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/85ba5ca26a107fb8854153e294dcf675e2617f04_r',
    'video_id': '5917d45cd1d3b95213ca1e24',
    'title': '一条丝巾的6种时髦系法',
    'video_tag_list': '我的丝巾这么玩',
    'content': '#我的丝巾这么玩[话题]##每日穿搭[话题]#\n优雅的小方巾不止能系在脖子上！编头发，系包包......一条丝巾也能玩出不同可能性！\nLook 1 单结系法\n划重点：方巾尾巴要藏好\nLook 2 可爱蝴蝶结\n划重点：蝴蝶结要随意松散\nLook 3 童子军系法\n划重点：一长一短才俏皮\nLook 4 复古头戴法\n划重点：在耳侧打结，露出刘海\nLook 5 三角领巾系法\n划重点：绕成细绳再打结\nLook 6 名媛绑手柄法\n划重点：结头朝下，手柄要绑紧'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgvs4DorNhjCbrzxo03RNNNjsb-S_compress_L1',
    'video_id': '5917d8dfb46c5d5bae4566b6',
    'title': '厚重衣物收纳法（1/3）',
    'video_tag_list': '',
    'content': '夏天来啦，是时候把厚厚的衣服收起来啦，好多人问的羽绒服、厚毛衣、被子等整理方法都在这里了，尽量详细了，还有啥没拍到的可以参考同类衣服的收纳方法，或者留言给我吧。厚重的衣物本来就占地方，通过合理的方法能尽量利用空间。\n由于系统只能发5分钟，而这次视频内容较长，所以分三次发，这是第一部～'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lutHymzEy7-_2rmqNc-fTVrggSGa_compress_L1',
    'video_id': '5917d9aed2c8a50c9a14f09a',
    'title': '厚重衣物收纳法（2/3）',
    'video_tag_list': '',
    'content': '夏天来啦，是时候把厚厚的衣服收起来啦，好多人问的羽绒服、厚毛衣、被子等整理方法都在这里了，尽量详细了，还有啥没拍到的可以参考同类衣服的收纳方法，或者留言给我吧。厚重的衣物本来就占地方，通过合理的方法能尽量利用空间。\n由于系统只能发5分钟，而这次视频内容较长，所以分三次发，这是第二部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmf7fVNWHwt2cO88X9U85PDm6CRq_compress_L1',
    'video_id': '5917daa0d1d3b9640cca1e21',
    'title': '厚重衣物收纳法（3/3）',
    'video_tag_list': '',
    'content': '夏天来啦，是时候把厚厚的衣服收起来啦，好多人问的羽绒服、厚毛衣、被子等整理方法都在这里了，尽量详细了，还有啥没拍到的可以参考同类衣服的收纳方法，或者留言给我吧。厚重的衣物本来就占地方，通过合理的方法能尽量利用空间。\n由于系统只能发5分钟，而这次视频内容较长，所以分三次发，这是第三部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/6ab46e51b209723d2bbaae7d22f3b37e468777e5_r_ln',
    'video_id': '5917f3b0d2c8a5541a14f099',
    'title': '吃太好要锻炼，不然要长嘎嘎😂😂',
    'video_tag_list': '成都;高尔夫',
    'content': '腰扯到后恢复练习，不发力，感觉好呀！A杆距离打够了⛳⛳😂😂\n #拍照低头族[话题]# #高尔夫[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltm74vBjWmqdrLMDl-MKHK8zB8qX_compress_L1',
    'video_id': '59183660d1d3b977139634ea',
    'title': '【小视频】Piloxing激情团课💪',
    'video_tag_list': '见人不如健身',
    'content': '激情和美丽运动时一个也不能少。\n决定即日起去锻炼的时候都要适当注意形象😅#见人不如健身[话题]#\n健身的时候看到好身材+好造型自己心情都会好很多呐。\n😡没有丑只有懒！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/c112ac3d-5ef744e-89b0-c1a86e00cb42?sign=54e95877b7f2e8726b811733f77c25a7&t=65fb06d4',
    'video_id': '5918405fa9b2ed4b5ed9b5f1',
    'title': '“网红”身材死角大公开｜健身能不能拯救我的水桶腰',
    'video_tag_list': '8周变身比基尼女神',
    'content': '#8周变身比基尼女神[话题]#你是不是很困惑，为啥明星和健身网红们一个个都360度无死角，而自己无论吃的多克制，练的多刻苦，也还是有很多身材缺点无法改变？其实你在荧幕和社交媒体上看到那些所谓完美的形象，都是从几百次拍摄几千张照片中甄选出来的 。今天giselle和weiya就将自己的身材缺陷大公开，和你们分享那些即使健身也很难改变的身材痛点，和她们的健身心路历程以及这些年来身材的变化。健身不能改变一切，但是可以让我们达到自己最好的状态。8周挑战第四周， let’s work hard to become the better self! 记的关注我们的同名同姓全平台 fit4life健身与美食，每天打卡@fit4life'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljcf1lWFwwf22gnegti6MOjA1Akp_compress_L1',
    'video_id': '5918602fd1d3b97a9aca1e1b',
    'title': '超实用的减脂瘦肚子训练动作！核心腹部训练动作（上）',
    'video_tag_list': '见人不如健身',
    'content': '#必须要安利的健身动作[话题]#\n最近忙的有点过分、以至于没时间好好训练、快要胖成🐷🐷、当然也没时间给大家分享干货笔记[叹气R][叹气R][叹气R]\n之前答应大家要分享减脂腹部训练视频的～\n认真坚持做、燃脂瘦肚子效果都很好滴～\n今天趁着有点空闲、开始恢复了一下核心腹部训练～\n也给大家录了两套腹部动作（这套是上部分、适合初学者、核心力量相对不那么好的宝宝们！下部分是适合有一点训练基地和核心力量的宝宝们！）\n动作注意要点直接写在视频中了～\n有疑问的可以给我留言、我会抽空回复大家！\n腹部训练大家可以放在做有氧运动前、大概半小时左右就可以、接着再去做有氧能帮助有氧过程中身体更稳定、发力更准确、减少肌肉发力不对导致的关节疼痛！\n如果是大肌群的力量训练的话、也可以把腹部放在大肌群训练后～\n#健身是把整容刀[话题]##健身靠装备[话题]##见人不如健身[话题]##厉害了我的健身房[话题]##健身穿什么[话题]##在家徒手如何健身[话题]##高效腰腹燃脂计划[话题]##必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fm-BW_zENC4co8kA3XpkQ5naVIui_compress_L1',
    'video_id': '59186087b46c5d59e90a89e5',
    'title': 'My👧🏻Girl',
    'video_tag_list': '妈妈我最爱你',
    'content': '#妈妈我最爱你[话题]##我的母亲节[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lp2tKX7-LuQnNF79m65X7MVz0fpL_compress_L1',
    'video_id': '591862cc14de4102ceb77ab4',
    'title': '超实用的减脂瘦肚子训练动作！核心腹部训练动作（下）',
    'video_tag_list': '见人不如健身',
    'content': '#必须要安利的健身动作[话题]#\n最近忙的有点过分、以至于没时间好好训练、快要胖成🐷🐷、当然也没时间给大家分享干货笔记[叹气R][叹气R][叹气R]\n之前答应大家要分享减脂腹部训练视频的～\n认真坚持做、燃脂瘦肚子效果都很好滴～\n今天趁着有点空闲、开始恢复了一下核心腹部训练～\n也给大家录了两套腹部动作（这套是上部分、适合初学者、核心力量相对不那么好的宝宝们！下部分是适合有一点训练基地和核心力量的宝宝们！）\n动作注意要点直接写在视频中了～\n有疑问的可以给我留言、我会抽空回复大家！\n腹部训练大家可以放在做有氧运动前、大概半小时左右就可以、接着再去做有氧能帮助有氧过程中身体更稳定、发力更准确、减少肌肉发力不对导致的关节疼痛！\n如果是大肌群的力量训练的话、也可以把腹部放在大肌群训练后～\n#健身是把整容刀[话题]##健身穿什么[话题]##见人不如健身[话题]##健身靠装备[话题]##厉害了我的健身房[话题]##在家徒手如何健身[话题]##高效腰腹燃脂计划[话题]##我为瘦身打卡[话题]##必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loFGMxn5zd92l1516jVnhGqtO46K_compress_L1',
    'video_id': '59187495b46c5d11924566b7',
    'title': '好书推荐📖把卢浮宫搬回家🏺',
    'video_tag_list': '我的睡前书单',
    'content': '这是我买过最大的书！超值得收藏！\n打开一座只为您开放的博物馆\n卢浮宫太大藏品太多，走到脚断都很难逛完\n但有了这本书，你就可以把卢浮宫搬回家慢慢看！\n仔细看！从不同角度看！\n@娱乐薯 @视频薯 看我看我🙋🏻🙋🏻\n（视频加快以后声音太好笑了😂）\n历时10年、30种文字发行、卢浮宫5任馆长联合编辑\n8开超巨幅呈现\n打开一座365天只为您一个人开放的卢浮宫\n我觉得本书出版社总经理 徐洁民说的实在是太好了！！⬇️⬇️⬇️\n“以往数次参观卢浮宫，每每由达鲁楼梯拾级而上，我都只顾仰望萨莫特拉斯的胜利女神，无暇欣赏勒菲埃尔的巅峰之作--优雅的穹顶结构和椭圆形洞窗，想来不免遗憾。然而日复一日，在《蒙娜丽莎》和《岩间圣母》之间，在爱神阿佛洛狄忒的注视下，无数参观者面对眼前的美好或无暇驻足，或茫然无知，错过的美好又何止如此。有了这本呈现历代工匠和艺术大师细腻心思的著作，哪怕此生与卢浮宫无一面之缘，断也会少一些执拗的牵念。”\n总之呢，《卢浮宫》是一本全面介绍卢浮宫历史、文化、建筑变革以及传世藏品来历的精美图文书。非常值得收藏！！！\n💰价格：\n原价998，我趁当当做活动特价然后200减100的时候买的，只要384！！！超划算！！\n#晒晒我的书房[话题]##我的私藏书单[话题]##我的睡前书单[话题]##读书打卡[话题]##在读的一本书[话题]##偏爱纸质书[话题]#\n我改名字不叫厄齐尔的老婆啦 现在的我是山贼夫人！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltE3SWF2M7FH6K5nexO-sDK6Vy1K_compress_L1',
    'video_id': '5919352514de415547edf626',
    'title': '这样做的“宫保鸡丁”简单美味，99%的人都学会了',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n这是一道川菜中的保留家常菜，由鸡丁、干辣椒、花生米等炒制而成。由于其入口鲜辣，鸡肉的鲜嫩配合花生的香脆，深受大众喜欢。\n红而不辣、辣而不猛、香辣味浓、肉质滑脆。由于其入口鲜辣，鸡肉的鲜嫩配合花生的香脆。\n★★★★★\n创意指数\n宫保鸡丁\n▼\n宫保鸡丁\n·视频音乐·\n徐梦圆 - China Dance\n·食材·\n鸡肉、鸡蛋、大葱、青椒\n小米椒、蒜、花生\n清汤、豆瓣酱、老抽、料酒\n糖、香油、陈醋、盐\n1.鸡肉切条再改刀切丁\n2.倒入蛋清、1勺料酒、1茶匙淀粉、1茶匙糖、少许盐拌匀\n3.再淋少许油拌匀，腌制15分钟\n4.取一小碗清汤，倒入1勺料酒、半勺老抽、1茶匙糖，拌匀备用\n5.热锅冷油下鸡丁\n6.炒至熟透，将炒熟的鸡丁盛出备用\n7.大葱切段，蒜切末，青椒切圈\n8.油锅下干辣椒、大葱段、青椒段爆香\n9.加入豆瓣酱、蒜泥继续煸炒\n10.等豆瓣酱呛香溢出时，倒入兑好的调料汁\n11.加入一点水淀粉勾芡\n12.最后倒入鸡丁翻炒，直到酱汁完全裹住鸡丁\n13.再淋入少许醋，撒一把去衣熟花生米\n14.淋上一点香油\n15.关火盛出即可\n16.美味的家常版宫保鸡丁就上桌啦~！\n小贴士\n1.这道菜全程要大火，煸炒鸡丁不能久，久了就会老。\n#超级下饭的家常菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/cf868a99-d8fceea-a532-6e99033d4af3?sign=4347e2e22502e74fdfbd3615cd5ea199&t=65fb06d4',
    'video_id': '59194f907fc5b82a3b383800',
    'title': '表白成功率低到可怕？桌上摆了它你再试下！',
    'video_tag_list': '',
    'content': '照明只能靠灯光\n但温馨浪漫还得数烛光\n废旧铁罐变烛台\n随意镂空DIY\n一罐烛光表爱意\n自制浪漫才叫温馨\n材料\n铁桶 / 蜡烛 / 图片\n步骤\n①用G字钳固定铁桶\n②用透明胶把图案粘在铁桶上\n③用电钻沿着图案轮廓开孔\n④揭除图案\n⑤放入点燃的蜡烛\n⑥镂空铁艺烛台就完成了~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/2918a87b9a7a53935c9eddb4bc1626b157bc46f6_r_ln',
    'video_id': '591960f3a9b2ed268fe0a3ce',
    'title': '教你如何正确收纳耳机！再也不用担心耳机线打结了',
    'video_tag_list': '视频教你生活小窍门',
    'content': '很多人总会感叹耳机线易缠绕，每次用之前都需要把乱缠成一团的耳机方便解开，如果遇到没有耐心的耳机主还有可能面临着被扯断的命运。那么，今天喵酱就来教大家简单轻松又便于收纳的耳机线收纳法，再手残也不怕哟~   #视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/720x404/vcodec/libx264/pgc/145f8814-80e1e1a-8691-ff8f1efaab24?sign=3f2048becf814b4362898a14a7e281fe&t=65fb06d4',
    'video_id': '591972007fc5b83b84ed525a',
    'title': '服！我服！这TM就是一出大戏！',
    'video_tag_list': '',
    'content': '7分钟看完琼瑶作（死）了一辈子的人生大戏'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luAswxAB65FsdpaMvKLJMAhD9ts1_compress_L1',
    'video_id': '59197d7114de41235dedf624',
    'title': '我的除螨心得',
    'video_tag_list': '',
    'content': '大家都超感兴趣的除螨喷雾来了！一只螨虫一夏天就能繁殖一亿只[骷髅]绝不能坐视不管[加油]这次推荐的是UYEKI除螨喷雾中功能最全、口碑最好的白色升级款[求关注]感兴趣的进围脖哦'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/6bde4a2a-d0fc406-b247-31855b19283e_compress_L1',
    'video_id': '591995f3a9b2ed3cb8431551',
    'title': '雅诗兰黛持妆无暇气垫粉底',
    'video_tag_list': '',
    'content': '雅诗兰黛持妆气垫气垫\nSPF50/PA+++\n最近陆陆续续用了好多欧美系的气垫粉底\n雅诗兰黛DW的持妆气垫应该算是当中遮瑕度最高的\n这款气垫有超强遮瑕力和持久控油\n非常适合油皮、混油皮和瑕疵皮\n中性和干性皮无需散粉就能持妆8小时\n修饰黑眼圈、痘印等瑕疵\n持妆一整天，近看都是美美哒\n实现持久无瑕少女颜\n如果特别严重的瑕疵还可以叠加持妆无瑕气垫粉妆棒\n这款更加滋润保湿\n单独用也很好，叠在气垫上遮瑕度加倍\n附上气垫使用小Tips: 轻轻沾，轻轻拍\n官网说的有道理，少量遮瑕力已经很气强\n如果沾粉太多或下手太重容易让妆感变厚重\n局部可以少量多次叠加增加遮瑕效果\n听说，现在专柜还有“一盒双芯”的限量套装哦~~一起相约拔草吧！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loMG77NA9WvUDLw-Vdl18w_afF05_compress_L1',
    'video_id': '5919d1bed1d3b95b4a154e3b',
    'title': '手把手教你如何梳蜈蚣辫',
    'video_tag_list': '',
    'content': '小蛙心血来潮录了两次视频～\n大家不要嫌弃我吖～\n这个是第二次录～但是整个感觉就是新手～\n然后～然后～然后😂😂😂\n其实还蛮好玩的诶～\n也能发现很多自己说话不好的习惯～譬如“啧”哈哈哈哈\n其实我一直是一个爱捣鼓头发的人～\n从小就喜欢帮别人梳头发～嘻嘻～\n我发现我一开始讲话是温柔的～\n然后声音越来越粗越来越粗哈哈哈～\n还有宝宝们不要催我染头发啦～\n今天有人问我是不是没时间染头发😂😂😂\n真的是不准备染了～凑合看看～下次剪了就好啦～\n希望以后有机会多录视频给大家看囖～\n喜欢的话给我点赞哟～\n爱你萌～\n如果效果不好～咱就删了～自己留着看哈哈哈哈～\n效果好的话我再放第一次录的视频～晚上录的～光不好～是丸子头视频啦～'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/640x360/vcodec/libx264/pgc/dfb50c83-e9998c2-9764-9c86e91c49cf?sign=6a231fea1d28dfbb8c2301ead2efb816&t=65fb06d4',
    'video_id': '591a5a85a9b2ed3784d0708a',
    'title': '不撕逼的《花少3》，就没有收视率啦？',
    'video_tag_list': '',
    'content': '花少=撕逼？但比撕逼更糟心的是，市面上的国产综艺几乎全是抄的'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/7a0aac45-4886692-b7fb-d78e6a1a3825?sign=a5914949c7dae32d9b2cea95977be8f7&t=65fb06d4',
    'video_id': '591a7120a9b2ed1fd4d07093',
    'title': '有小肚子？收腹减脂这套动作全搞定！',
    'video_tag_list': '',
    'content': '腹愁者们，夏天来了，肚子上的游泳圈和小肉肉还没有减掉？那就来做这套腹部训练动作吧，收腹减脂全靠它！更丰富更完整的训练计划欢迎下载「火辣健身app」，或者微信关注「火辣健身」。#健身# #减肥# #瘦肚子##必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/49ddb43b-cbd14c6-b71e-4fbeec7c098a?sign=53218a262db6149dc74d1ac3e130699d&t=65fb06d4',
    'video_id': '591a73087fc5b86996d217c8',
    'title': '拉伸能瘦腿么？肌肉腿怎么破？实用腿部拉伸视频',
    'video_tag_list': '8周变身比基尼女神',
    'content': '#8周变身比基尼女神[话题]#关于拉伸与”瘦腿“的关系，误区多如牛毛。从直观感觉，拉伸可以让肌肉线条变得纤长，可是事实，可能会让你吃惊。本期视频让weiya与giselle为你揭开拉伸与”瘦小腿“和”瘦大腿“的关系。视频后半段实用腿部拉伸动作，可以作为你的每天拉伸routine哦！八周挑战我们继续，请持续关注（下期视频是臀腿训练哦）同名全平台：fit4life健身与美食。'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/ljvCDBA1OwWSZEhBE6ZnO-xtZd9D_compress_L1',
    'video_id': '591a73e2d2c8a5658614ffc7',
    'title': '一道美味的蒜蓉粉丝蒸丝瓜，爽滑清口正是夏天滋味！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n丝瓜有凉血解毒、除热利肠之效，对于女性来说，丝瓜还含有防止皮肤老化的维生素B1，多吃能护肤除斑，使皮肤洁白细嫩。\n粉丝有良好的附味性，它能吸收各种鲜美汤料的味道，再加上粉丝本身的柔润嫩滑，更加爽口宜人，凉拌更佳。\n★★★★★\n创意指数\n蒜蓉粉丝蒸丝瓜\n▼\n蒜蓉粉丝蒸丝瓜\n·视频音乐·\nBlake Shelton - Do You Remember\n·食材·\n丝瓜、粉丝、剁辣椒\n高汤、老抽、蒸鱼豉油、蒜、盐\n1.丝瓜洗净去皮\n2.去掉根蒂\n3.切成合适的长短的段备用\n4.粉丝放热水浸泡至发软\n5.大蒜切末\n6.烧热锅，放入适量猪油化开\n7.炒匀盛出\n8.倒入少许盐搅拌\n9.倒入半勺老抽、半勺蒸鱼豉油、适量高汤，搅拌均匀\n10.泡软的粉丝放入盘中，倒入味水后姜粉丝扒匀\n11.将丝瓜段摆入盘中\n12.将熬好的剁辣椒盖在丝瓜上\n13.移入蒸锅，大火蒸5分钟即可\n14.用心做人人都可以是大厨~！\n小贴士\n1.盘底铺满粉丝，将丝瓜和调味的汁水统统吸入粉丝中，使其滋味更加浓郁。\n2.丝瓜易熟，大约蒸5分钟即可。'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lm0qsS_Bdm0DbhXdfO18YDiH0MDr_compress_L1',
    'video_id': '591abbf8b46c5d6439b7ab25',
    'title': '今天,我带你来了！周杰伦结婚教堂+伦敦+约克 英国婚纱摄影篇',
    'video_tag_list': '',
    'content': '今天， 我带你来了！之前教堂求婚成功， 这次带着女主拍摄了伦敦许多场景和约克场景，以及周董结婚的教堂。感谢客人的支持！也期望后边几组客人的教堂婚礼顺利完成， 大家先来围观花絮视频吧！\n本次拍摄经过了三天， 分别是求婚 外景伦敦 加 约克 和周杰伦教堂。\n其实， 拍摄视频和照片不太一样， 有时候为了2-3秒镜头可能要花很久时间去完成，如果要拍成不是花絮，而是有剧本的话， 难度就更加大啦^^\n不过 我们也在努力进步中， 过不了多久VM 就会推出带剧本的微电影和大家相见啦^^\n有问题的朋友留言就好啦'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/a95db19f379c35ad13b3f032da5ffeaaf6c37885_r',
    'video_id': '591ac70a346094755d9ce9c4',
    'title': '教你2种内裤的折叠收纳法',
    'video_tag_list': '',
    'content': '很多人都会来问喵酱关于内衣的收纳，今天喵酱来教大家两种内裤的不同折叠收纳法。\n无论是出门旅行，还是衣柜收纳，都能优雅的随机应变哟٩(•౪•٩)♡'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsmp1AtBEvfDMqNWLE9FvCTRRd5y_compress_L1',
    'video_id': '591add05d1d3b9017bb2ee3e',
    'title': '柯基宝宝成天就知道闹腾哈哈哈哈',
    'video_tag_list': '',
    'content': '一条只专心看电视的短腿柯基😂😂'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loCf3gsgdQA4w5jnF2ZvsEmH1n0L_compress_L1',
    'video_id': '591af6a5b46c5d0a6a97fa89',
    'title': '',
    'video_tag_list': '最显白的口红;香奈儿',
    'content': '喵王唇妆试色测评14款香奈儿RougeGloss唇彩上脸视频\n这是一个极其失败的唇妆视频🙈喵王随便录着玩儿的哈。。喵王还是比较适应文本形式的那种常规介绍！这个就是随便儿看看吧。。😂\n就是手机翻转过来的那种，都懂苹果手机是特别变形特别不好使那种，像素啊～分辨率呀～色差呐～反正各种不好。。我就是糙录一下，大致的一个色儿是那样滴。。。😳\n喵王就是不太喜欢录视频，首先人长的也不是特别好看，再一个就是我设备也不好，还有就是我也不会编辑修片啥的。。欧洲这边一直都特别昏沉阴暗的天儿，采光也不是很好，也没边角料的设备。。加上喵王平时就是光写测评都不是特别有时间。。就是酱子。。。喵王基本不录视频，就是纯描绘写作测评这种。。。以后有功夫有能耐的吧。。\n好！好！我们来简单说下这个2017年的香奶奶家Rouge CoCo Gloss玻璃唇彩～～～超级美昂，不显唇纹护唇啥的。。喵王之后会好好写一篇试色测评跟之前一样那种。。发视频的我就不太想写什么了，我之后会像往常测评类笔记📒细致描绘的😁😁😁\n喵王一共就1⃣️4⃣️个色儿哈，都挺不错的，凑乎看吧基本的上脸效果。。录的非常糙和失败哈。。🙈看个大概就行了～～[偷笑R]还有视频里的喵王也没化特别艳丽的妆主要为了衬托唇色饱和度，还有就是白天没什么时间，就是晚上已经带妆十个小时了录的时候，晚上十一二点那样，比较疲惫不堪，本来长得也很疲惫🌚\n最后就是里面录的十四个色号都是一天录的，中间的有的色号之间喵王喝了些水吃些东西瞎忙活啥的，回来接着录下一个色号光线就调的可能有些小差距，不是很影响唇彩本身颜色哈😁😁😁理解下，设备环境不好，我瞎录的。。\n谢谢观看～ByeBye～之后上细致试色测评笔记版[飞吻R]\n#我的口红日记[话题]##最显白的口红[话题]##日常口红[话题]##我的口红不挑皮[话题]##显白口红[话题]##人不红靠口红[话题]##黄皮最爱的口红[话题]##素颜最适合的口红[话题]##秋冬必备口红[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsCIEWj8u3e24fWr-HT4ahkM5qgw_compress_L1',
    'video_id': '591b1dcfd1d3b941fbfc9a53',
    'title': '换季收纳大法，妈妈再也不用担心我衣服乱糟糟了',
    'video_tag_list': '收纳小诀窍',
    'content': '大衣收纳\ntips：大衣不易折叠，用防尘罩将大衣罩住挂起来。\n羽绒服收纳\ntips：衣袖两侧向内折三分之一，向上卷并用帽子包住羽绒服。\nT恤收纳\ntips：衣袖两侧向内折三分之一，将袖子整理好，对折两次即可。\n衬衫收纳\ntips：将一本杂志放在衬衫背后，沿着杂志边缘折好。\n背心收纳\ntips：两侧向内折三分之一，折叠几次形成小方块。\n连帽衫收纳\ntips：衣袖两侧向内折三分之一，帽子由外向里翻折。\n裤子收纳\ntips：折叠多次形成小方块。\n#收纳小诀窍[话题]##我的衣橱秘密[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhtoUlmfcRYUWV9yG5oIIrRhP-Se_compress_L1',
    'video_id': '591b98e7b46c5d50c897fa7a',
    'title': '小灯泡养成记！',
    'video_tag_list': 'SK-II;SK-II 肌因光蕴环采钻白精华露;春季防晒必备',
    'content': '哈哈哈夏天最重要的任务就是白成小灯泡💡\n今天跟大家分享我自己很喜欢的两款美白产品哦～\n\n\n#美白洗面奶推荐[话题]#\n#春季防晒必备[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/87d6361f3c554f43f40e2ab3ac2dd2ba7f7ff5dd_r_ln',
    'video_id': '591ba8e1b46c5d7af78425c7',
    'title': '虾仁炒蛋这样做绝对好吃，清香四溢一点都不醒！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n虾仁肉质松软，易消化，虾肉中含有丰富的镁，能很好的保护心血管系统，减少血液中的胆固醇含量，防止动脉硬化。\n鸡蛋就更不用说了，含有大量的维生素和矿物质及优质蛋白质，是人类最好的营养来源之一。\n★★★★★\n创意指数\n虾仁炒蛋\n▼\n虾仁炒蛋\n·视频音乐·\n岸部眞明 - RIJN de smile\n·食材·\n鸡蛋、姜、虾仁\n胡椒粉、料酒\n葱花、淀粉、盐\n1.取少许蛋清倒入碗中备用\n2.倒入1勺料酒、1茶匙胡椒粉、1茶匙淀粉、少许姜末\n3.倒入少许蛋清，拌匀，腌制10分钟\n4.油锅倒入腌制后的虾仁，炒熟盛出\n5.将鸡蛋液倒入炒好的虾仁中\n6.倒入少许葱花、盐拌匀\n7.热锅冷油倒入鸡蛋液\n8.蛋液微微凝固后关火\n9.用余温炒匀盛出\n10.回家来一份一人食，照顾自己的胃\n小贴士\n\u200b\n1.虾仁：虾忌与某些水果同吃。\n2.鸡蛋：与鹅肉同食损伤脾胃'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/a20049223dae5bef6442946ba11be46fa0d94d55_r',
    'video_id': '591beefcd1d3b938d4fc9a4e',
    'title': '翘臀必看👉🏻【蜜桃臀养成手册】9大招式拥有翘臀不是梦！',
    'video_tag_list': '见人不如健身',
    'content': '[得意R][得意R]视频来咯~~\n上次发了关于练翘臀的文字笔记之后，大家墙裂要求大魔王出个视频教程，昨晚在GYM训练赶紧让宋先森帮忙录了一个。还没练出翘臀的小仙女们快看这里👆🏻👆🏻\n---------------------------❤️--------------------------\n✨动作要点✨\n前面7个动作都是自重训练，只需要一张瑜伽垫，不限场地，随时随地都能练！\n每个动作做5次之后再快速震动5次，每边连续做5组！一定要做完一边再换另外一边哦~所有动作要一气呵成，中间不能休息，保你做下来酸爽无比！\n后面2个是可以在GYM借助器械练的动作，每个动作15次为一组，一共做6组，组间休息30s。\n⚠️这里要特别说明一下Hip Abdoctor这个器械的正确✅打开方式👇🏻\n双手扶在前面的杆子上，臀部向下坐，但要保持悬空不能坐在凳子上，把臀部送出去(类似于撅起屁股的感觉)，腹部收紧，臀部发力慢慢打开到最大角度感受臀部肌肉收缩，停顿1s再慢慢收回。注意整个过程都要慢哦！\n关于练臀动作的详细文字教程，大魔王在之前的一篇笔记中有做过介绍，感兴趣的小仙女可以去翻看之前的笔记哈~\n✨训练频率✨\n臀属于大肌群，为了让身体在每次健身训练后都能有更好的恢复和生长，最好让两次大肌群训练间隔72小时左右。所以针对臀部的训练最好是每3天安排一次，不要每天练哦！\n---------------------------❤️--------------------------\n五月已经过半，夏天还会远吗？小仙女们不要再犹豫啦！赶在夏天到来之前，和大魔王一起练出傲人蜜桃翘臀吧💪🏻💪🏻\n最后，大魔王想要感谢小仙女们对健身的热爱和关注，大家的点赞和鼓励也激励着我想要变成更好的自己！[害羞R][害羞R]我会继续跟大家分享更多的健身方法和经验，让我们一起变瘦变美变身美少女！\n大家有任何问题或者想看什么内容都欢迎留言给我噢"😘\n🎵视频背景音乐🎵Never Win - Fischerspooner\n@小红叔  @视频薯\n#厉害了我的健身房[话题]##见人不如健身[话题]##在家徒手如何健身[话题]##臀部塑形视频[话题]##健身器械的正确使用方式[话题]##练出翘翘蜜桃臀[话题]##我为瘦身打卡[话题]##周末去运动[话题]##必须要安利的健身动作[话题]##健身是把整容刀[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/b1d0978b9b588517a8771583f3c6a1feb4b13793_v1',
    'video_id': '591bef82d1d3b93c21b2ee4d',
    'title': '巴塞罗那，一家宫殿般的酒店',
    'video_tag_list': 'Fenty by Puma;Tony Bianco;巴塞罗那',
    'content': '卫衣+长裙\n尖头踝靴\n酒店实在太美，忍不住给自己加上一点点女人味😜\n🌹'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpTpWtZq_TavV85H_8HnfVWRxIdv_compress_L1',
    'video_id': '591bf8e4d1d3b95821fc9a4b',
    'title': '几块钱的衣架选不对，会让你买衣服花的几个亿都浪费掉（1/3）',
    'video_tag_list': '',
    'content': '没有夸张哦，因为衣架你毁掉的衣服还少嘛[哭惹R][哭惹R][害羞R]大家要看的衣架视频终于来喽[偷笑R][偷笑R][萌萌哒R]\n因为小红书系统限制，只能发5分钟以内的，后半部分内容见下部视频～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luPSt5oM5k6jbZgRD1TaaMYTuj-2_compress_L1',
    'video_id': '591bfa6ad2c8a50e36b96a7f',
    'title': '几块钱的衣架选不对，会让你买衣服花的几个亿都浪费掉（3/3）',
    'video_tag_list': '',
    'content': '没有夸张哦，因为衣架你毁掉的衣服还少嘛[哭惹R][哭惹R][害羞R]大家要看的衣架视频终于来喽[偷笑R][偷笑R][萌萌哒R]\n因为小红书系统限制，只能发5分钟以内的，这是第三部分～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/92ced58722afd8569cd0411edfbdc749827e8f1d_v1_ln',
    'video_id': '591c0c95a9b2ed6e1cd1adfa',
    'title': '如何辨别好坏鸡蛋？教你这一招再也不担心吃到坏鸡蛋了',
    'video_tag_list': '视频教你生活小窍门',
    'content': '鸡蛋在我们平日的生活中非常的常见，而买鸡蛋这件事很多时候我们并没有太多的注意。如果买回来放得比较久了，我们应该如何判断鸡蛋是否还能吃呢？\n今天喵招就来教大家一招辨别鸡蛋的好坏！\n#视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/abf06bc2-10195b1-a859-c888be3beb91?sign=741a59c61f59cbd5ffa29a2cf5770824&t=65fb06d4',
    'video_id': '591c1b477fc5b842f42400f4',
    'title': '肠胃不好自带音效？一招教你化解放屁烦恼',
    'video_tag_list': '',
    'content': '肠胃不好，尴尬不少\n如何掩盖最重要\n帅无敌教你轻松化解肠胃音效'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lniNIGiRJHSEOfR4EGilCUS_5GEV_compress_L1',
    'video_id': '591c1f11d1d3b950ecb2ee40',
    'title': '减肥瘦身～最简单有效瘦腰方法视频版',
    'video_tag_list': '',
    'content': '宝宝们不知道笔记描述\n我录视频了！\n每组做1到2分钟，时间久效果佳\n早晚都做，每次做5组！1周见效！\n只要你动作对！一周你就能看到腰腹瘦下来！甚至有马甲线'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/db9f1cda9abf96d8f23ed8a7d6ca4ff935864402_r_ln',
    'video_id': '591c2c9bb46c5d6bb18425c7',
    'title': '我有家啦 ！🐶',
    'video_tag_list': '',
    'content': '听说男主人心仪我很久了\n今天主人带我回家啦\n我35天大啦\n希望大家喜欢我噢✌️\n我是只有着超美淡蓝色眼球的烟灰红阿拉斯加哟💕'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/47f43bd9-ce137cf-a1ad-43a965a0fb33?sign=12257e933aa7cbde07782456cf89f750&t=65fb06d4',
    'video_id': '591c380f7fc5b85a3c2400f2',
    'title': '蜜桃臀周（1）：如何练臀又圆又翘',
    'video_tag_list': '8周变身比基尼女神',
    'content': '大家都说练臀，但是你知道练臀究竟练的是哪块肌肉么？为什么你深蹲了半天屁股不疼腿疼？哪些训练是最好的臀部训练？如何才能避免训练受伤？没时间去健身房在家怎么练翘臀？本周是8周挑战的第五周，我们决定将本周全部贡献给我们的蜜桃臀。 以上问题我们会分三期视频给大家详细讲解。如果喜欢我们的内容那一定要关注我们的同名平台 fit4life健身与美食。想要翘臀，那就从一周两次臀腿日开始吧！记的打卡@fit4life, 并加标签#8周变身比基尼女神[话题]# 哦！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkWjhgDsW6m-gRzYCz-5UEcxfWBe_compress_L1',
    'video_id': '591c4cb214de4127096167ac',
    'title': '智障少女吃榴莲',
    'video_tag_list': '',
    'content': '好喜欢吃榴莲啊～～～大家都喜欢吃榴莲么？！\n真的好好吃啊！哈哈哈～\n祝大家都吃到好吃的水果！笔芯～💖💖'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/b01fcac15944f388b2b20c4874de791e8560db60_v1_ln',
    'video_id': '591c5c75d1d3b90b94b2ee45',
    'title': '背部力量训练、告别圆肩驼背穿衣无形！附送增肌细节干货！',
    'video_tag_list': '见人不如健身',
    'content': '#必须要安利的健身动作[话题]#\n昨天欠你们的背部力量训练视频～\n今天补上、因为目前我也在恢复性训练、所以背部是分开训练、今天主要以下拉类动作为主、主要发展背部的宽度！\n背阔肌很大、在背部呈倒三角形、想要练就好看有力的背部、宽度 厚度 肩袖 下背部都得全面发展！\n今天顺便送上增肌的一些细节讲解！正在增肌的拿走不谢[得意R][得意R][得意R][得意R][得意R][得意R][得意R][得意R]\n增肌注意细节：\n胸肌\n如果胸肌紧凑 面积小# 主要原因是练后不进行拉伸 卧推的握距长期较窄\n胸肌上部薄弱#说明上胸练的不够 长期卧推下落到比较低的位置\n内侧薄弱#说明夹胸类的动作做的比较少 或者是不做略窄距的卧推\n如果下胸比较差的话# 说明下胸训练频率过低 杠铃杆下放的位置长期过度靠上\n多做双轨迹的动作可以改善两边不均匀的肌肉\n胸肌面积大 厚度不足# 是因为卧推握距长期过宽\n如果一个人正面宽 肩部较窄是因为#（1，先天锁骨较短 2，三角肌欠发达）\n*在训练胸部的时候经常会碰到肱三头肌和三角肌等协同肌先于胸肌疲劳 导致无法对胸部进行更好的刺激，此时不妨把孤立的夹胸类动作安排在卧推，双杠臂屈伸等大重量的复合动作之前，预先刺激胸肌 使其疲劳，再用大重量的复合动作对胸部进行轰击\n背阔肌\n背部宽度不够说明#（1，宽距的下拉做的太少  2，宽距的引体向上做的太少  ）\n背阔肌过短的原因#是不做或者少做窄距的下拉\n背阔肌厚度不够的原因是#（1，各种划船类的动作做的太少）\n背中部（斜方肌中下）薄弱的原因#是肩带缩回的动作不做或很少做\n背下部腰部两侧（竖脊肌）薄弱的原因是#不做或者很少做挺身 屈腿硬拉等动作\n训练原则\n以周为循环的训练 最少一周要保证一天休息\n休息日后的第一天应该练最欠缺的部位\n每个循环的第一天练大肌肉群（胸 背 腿 选其一） 先训练大肌肉群再练小肌肉群\n不要把三头放在胸的前一天练 不要把二头放在背的前一天练 不要把三角肌放在练胸的前一天练  尽量遵循训练强度的强弱交替\n训练间歇时间为30s~90s之间 休息超过三分钟代表训练终止\n大肌肉群恢复需要72小时 小肌肉群需要48小时\n单次训练中总组数不要超过24组  大肌肉群3～6个动作 小肌肉群2～4个动作（3～4组）\n一个训练部位中 永远把最好嘴基础的动作放在最前面做\n#健身穿什么[话题]##健身靠装备[话题]##厉害了我的健身房[话题]##见人不如健身[话题]##健身是把整容刀[话题]##在家徒手如何健身[话题]##健身器械教学视频[话题]##必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FlwlIxqEwZFPqAQxtRbMVt2xJG_g',
    'video_id': '591c73dcb46c5d338e8425ca',
    'title': '喵星人也能乖乖洗澡澡',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '英短MOlly已经四岁多啦，在四年的岁月里最让我宽心的就是它每次洗澡都乖乖的，呆萌，不吵不闹[飞吻R]一个月就能给她洗一次，洗玩毛摸起来更蓬松，像个毛绒玩具[飞吻R]\n#我和宠物的日常[话题]##我家宠物最萌的瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FuwuyDwJyth64HOgM-QuuDNaoibF_compress_L1',
    'video_id': '591c83ecd1d3b97f1db2ee3f',
    'title': '卡节拍的喵哦，你们有嘛、hhh',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '#我和宠物的日常[话题]##我家宠物最萌的瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpX1A9SQ9Kvv0yfUuKFW5xwBIYTa_compress_L1',
    'video_id': '591d0c96d1d3b91d97b2ee3c',
    'title': '料理达人教你用菠萝入菜，分分钟征服你的味蕾！',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/30a2a92d-ca96d32-ace1-d481edd14bf7?sign=f86cbe2504dcef61ad04d6a4929aade1&t=65fb06d4',
    'video_id': '591d10c3346094292ad009e4',
    'title': '女生版腹肌撕裂者，练出马甲线就靠它！',
    'video_tag_list': '',
    'content': '鼎鼎大名的腹肌撕裂者你应该听过，但是因为难度太大令很多人望而却步，这套比较适合女生的腹肌撕裂者，想练出马甲线的你一定要试试。更丰富更完整的训练计划欢迎下载「火辣健身app」，或者微信关注「火辣健身」。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/c76371631d8de186fdd9c40a85de1887dc167e88_r_ln',
    'video_id': '591d4a68a9b2ed778d468d36',
    'title': '520表白神助攻：蓝莓慕斯镜面蛋糕 - 视频教程',
    'video_tag_list': '',
    'content': '今天我来分享一款蓝莓慕斯镜面蛋糕的做法，不仅外观看上去高大上，甚至都可以自拍了，而且口感绵软，入口即化，蓝莓果味十足，保证你吃了还想吃。\n冰冰凉凉的口感，最适合炎热的夏天了。\n520表白成功全靠它了！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lohfr6J3PasxL-NNVUPEQXGiXG6z_compress_L1',
    'video_id': '591d68fcb46c5d49f24f8139',
    'title': '绝了！水果竟然还能这么吃，不光惊艳，还能瘦身养颜',
    'video_tag_list': '',
    'content': '教你在家自制香芒火龙果暮雪，好吃还瘦身养颜！\n#用水果做甜品#大爱水果季'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/6f50735a6837efe977e604db1312d63e39fd5128_v1_ln',
    'video_id': '591d82ab7fc5b8600f55aaa1',
    'title': '10个小技能，彻底改变你的生活现状，还等什么，赶紧收藏！',
    'video_tag_list': '视频教你生活小窍门',
    'content': '最全喵招生活小技能大盘点，教你10个生活必备小技能，彻底改变你的生活现状，还在等什么？赶紧Get√起来吧！ #视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lockY3YajvYciRMrdMYlDAJ-LTV__compress_L1',
    'video_id': '591daab6b46c5d159755a6b3',
    'title': '如何打包行李能让行李箱大两倍，而且永远翻不乱？（1/3）',
    'video_tag_list': '',
    'content': '由于系统限制只能发5分钟以内，后半部分见下部视频～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loO-tpnIYoh5XxDdJcC6Gaknqguu_compress_L1',
    'video_id': '591dac0414de4109b03c23b4',
    'title': '如何打包行李能让行李箱大两倍，而且永远翻不乱？（2/3）',
    'video_tag_list': '',
    'content': '系统限制只能发5分钟以内，后半部分见下部视频～'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lvDU1WfI-5bLFuB3VlbtJKfnyHVp_compress_L1',
    'video_id': '591dadc914de410e51c2c06e',
    'title': '如何打包行李能让行李箱大两倍，而且永远翻不乱？（3/3）',
    'video_tag_list': '',
    'content': '系统限制只能发5分钟以内，这是最后一部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgH-H27lMsgDUTJ84EAO0wtmqhBZ_compress_L1',
    'video_id': '591e442bd2c8a5262be11f8d',
    'title': '拍黄瓜好吃的秘籍，看一遍就懂！天热也有好胃口',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n拍黄瓜是道家常凉菜，主料是黄瓜，用各种调料拌制而成。清凉爽口，适合夏季食用。\n夏天天气炎热，没胃口吃饭，可以试试做这道菜，不用开火，就可以做一道下饭菜，很是值得推荐哈。\n★★★★★\n创意指数\n拍黄瓜\n▼\n拍黄瓜\n·视频音乐·\n岸部眞明 - Heartstrings\n·食材·\n黄瓜、小米椒\n葱、姜、蒜\n蒸鱼豉油、香醋、香油、盐\n1.黄瓜洗净，去头尾\n2.用刀将黄瓜拍裂\n3.将拍裂的黄瓜切成小段\n4.将黄瓜块用盐腌制5分钟\n5.将腌制出来的黄瓜汁倒掉\n6.姜蒜切米，小米椒切段，葱切花\n7.倒入一勺蒸鱼豉油、半勺香醋、半勺香油、适量姜蒜末\n8.混合均匀\n9.撒上葱花、辣椒段\n10.淋上热油\n11.这才是夏天的味道~！\n小贴士\n1.黄瓜用刀拍裂，自然开裂的黄瓜比直接切段的黄瓜更容易入味\n2.黄瓜段用盐先腌制，可以将多余的黄瓜汁排出，使黄瓜更加清脆\n#超Easy的凉拌菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fs76KsIKhJTQmDwLL-ahwnHE2SEX_compress_L1',
    'video_id': '591e4ba8b46c5d4f4b4f812f',
    'title': '＃上海＃世上本没有美蛙鱼头，有了＿＿＿，才有了美蛙鱼头。',
    'video_tag_list': '',
    'content': '没排过哥老官，就不是真正的吃货[吧唧R]'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lokbjFrPjx_IdmiaTVeyo6ma-Usu_compress_L1',
    'video_id': '591e6ac8d2c8a50da0e11f8f',
    'title': '假裝在度假⛱️',
    'video_tag_list': '',
    'content': '#优雅的露背穿搭[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/45689d01-8024b1b-ac85-5a8c9ec39967?sign=0215772bd6caf5b54a70264aa35b222f&t=65fb06d4',
    'video_id': '591e8d0a34609467c61751a0',
    'title': '【近期购物分享 - Burberry、CPB、黛珂、Jo Malone等一大波好东东】',
    'video_tag_list': "悦木之源 ORIGINS 泥娃娃活性碳面膜;科颜氏 Kiehl's 集焕白均衡亮肤淡斑精华液;资生堂 Shiseido 新透白美肌美容精华;黛珂 COSME DECORTE 天然植物软肌牛油果乳液;资生堂 Shiseido 安耐晒防晒霜金瓶;美宝莲;雪花秀 Sulwhasoo 莹彩腮红;肌肤之钥;肌肤之钥 clé de Peau Beauté 蔷薇口红/唇膏;博柏利;祖·玛珑 Jo Malone London 香水;我的护肤日常",
    'content': "duang duang duang~一大波购物分享来啦！\n最近苏妹儿又入了hin多好东东，包括护肤、彩妆、指甲油、还有香水，刚兴趣的小伙伴快来看吧！\n✔️Products Mentioned/都有点啥：\n1️⃣Origins悦木之源泥娃娃面膜\n2️⃣Kiehl's美白淡斑精华\n3️⃣Shiseido/资生堂新透白美肌集光祛斑精华液\n4️⃣黛珂牛油果乳液\n5️⃣资生堂安耐晒大金瓶防晒霜\n6️⃣美宝莲黑金气垫\n7️⃣雪花秀腮红 02号\n8️⃣CPB蔷薇唇膏 307\n9️⃣Burberry指甲油 No.299 黑色\n1️⃣0️⃣Jo Malone蓝风铃香水\n.\n你们近期都买了些什么呢？欢迎留言区跟我讨论哦😘\n#我的彩妆测评[话题]##我的护肤日常[话题]##闻香高手在民间[话题]#"
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/ljZbtfNK26FT3iWJ5qhb_RBuAq5Q_compress_L1',
    'video_id': '591e9beed2c8a514e9520cb1',
    'title': '🎬视频话题：必须要安利的健身动作',
    'video_tag_list': '必须要安利的健身动作',
    'content': '#必须要安利的健身动作[话题]#\n健身路上总有几个动作炒鸡爱！无论是练马甲线、练蜜桃臀、练腿练背，照着这样做才能事半功倍。\n周五又到啦！又是该去健身房的时间。不如拍支视频安利其他红薯你最爱的健身动作吧！\n👉动作不用拍太多，针对一个部位就好啦。\n👉有什么动作要点，记得在视频或文字里指出来哦～\n👉别忘了打上话题标签，发笔记的时候戳表情符号右边的#，在话题库里搜索“必须要安利的健身动作”，看到了就戳～\n视频来自 @的欢-gladys  @Miss米牙小姐Mia  @xuelove723  @Doreamon_M'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnF83ojntvWroBnDnboHVocCl2KE_compress_L1',
    'video_id': '591ea18f14de4140d0f29197',
    'title': '🌿CSMulti-穿搭',
    'video_tag_list': '每日穿搭',
    'content': '#每日穿搭[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lt7qypJTs9NO5ZjA1wbg5u_KERyw_compress_L1',
    'video_id': '591eafd5d1d3b912d8a91370',
    'title': '马尔代夫的海水有魔力',
    'video_tag_list': '',
    'content': '☀️'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpPBHj1Cbx1xg66pS9rMYr13sTpb_compress_L1',
    'video_id': '591ed19bd1d3b979b3a9136c',
    'title': '减肥健身～腿粗和小腹突出！假胯宽，盆骨前',
    'video_tag_list': '',
    'content': '先看视频～体态调整篇！\n视频限制长度'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/deeb4ffd-e430f79-aa30-868191ef98eb?sign=ec7ae7f4440e59d2d3105dd39d13ff0d&t=65fb06d4',
    'video_id': '591ed8967fc5b819dd2685d7',
    'title': '本期话题 | 爆笑！让你的男票给你的彩妆视频配个音！',
    'video_tag_list': '',
    'content': '#直男解说化妆视频\n又到一年虐狗节，今年我们不如来玩些好玩的，让你的男票/男朋友给你的化妆视频配音。\n👉🏻他到底能不能认出你的彩妆品？\n👉🏻他眼里你平时涂涂抹抹都在干嘛？\n美妆薯期待你们爆笑的作品哦！\n【如何发笔记】\n️1、拍一支彩妆视频\n2️、让你的男票给你后期配音\n️3、加上话题标签#直男解说化妆视频\n【如何给笔记加话题】\n️1、在文字输入页面有 ＃井号键，按下去！输入关键词直男，找到话题活动，点击即可参与。\n️2、成功参与话题的文字会变成蓝色哦：#直男解说化妆视频\n封面视频来自： @kim'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/01e2480e9422b25a01837003803a26ec96_259.mp4',
    'video_id': '591ef3c8d2c8a57c7a074070',
    'title': '家有萌🐶，我的宝宝！',
    'video_tag_list': '',
    'content': '第一个视频给我家东哥，今年七岁了，我是他姐姐。\n我妈一说姐姐他就歪着脑袋到处找我！太可爱了！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpo6HUK4H1ubaRcWnPHdQ9O6Bc0C_compress_L1',
    'video_id': '591f0f84d1d3b93512a9136c',
    'title': '珍爱生命 远离吸猫',
    'video_tag_list': '',
    'content': '这只猫叫皮皮 公司附近一家设计公司养的喵\n有天早上我上班看它被关在门外估计是一个晚上了\n可怜兮兮的就陪她玩了一会儿\n然后就\n吸猫上瘾了\n珍爱生命 远离吸猫\n离开皮皮的第一个半天 想她\n我要去搜猫棒了 拜拜'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lo3MpMEARwclHcBaULqxNbA4KFuy_compress_L1',
    'video_id': '591f18f8d1d3b94eb0a91373',
    'title': '周末扒舞时间',
    'video_tag_list': '',
    'content': '跳跳更健康'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/e5c99223-f561a0e-975e-f29bc2677bdc_compress_L1',
    'video_id': '591ff8847fc5b848092685d7',
    'title': '那些错误的民间护肤传说',
    'video_tag_list': '',
    'content': '“冷热水交替洗脸缩毛孔？柠檬片敷脸能美白？敷黄瓜片能补水？正确的护肤顺序是水乳霜精华吗？不要再被那些传说的民间美容秘方坑了！快来看看＃变美你不知道的100件事＃，跟着大大美酱科学变美！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvlI7Xrd_GPuIMfhiAwP1Gj3OJo8_compress_L1',
    'video_id': '5920579ab46c5d0b1f4a8ab9',
    'title': '一个内衣🐶的520',
    'video_tag_list': '',
    'content': '刚刚剪完出炉的新品视频\n美的自己想找个黑暗又安静的角落看完\n无可言说的感动\nBgm M83 Wait\n歌词 | send your dreams where nobody hides\n不能够更贴切地描述关于这件事情的意义'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgFVZl-t49ok_hFDyXz2cLduR8Fn_compress_L1',
    'video_id': '59210566d2c8a57c56520cb1',
    'title': '如何收纳让人头疼的帽衫、衬衫等不规则衣物？（1/2）',
    'video_tag_list': '',
    'content': '上次说的小问题集锦系列哦，这期视频集中回答下[偷笑R]留言私信没精力一一回复，对不起大家喽，我会尽量把问的比较多的问题拍成小集锦，所以，有问题多多给我留言吧[吧唧R][飞吻R]\n由于系统限制只能发5分钟，后半部分内容见下部视频～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltPWu-U9J_ZnEt4IA6sovn33RMNd_compress_L1',
    'video_id': '592105f914de4107d9391cbe',
    'title': '如何收纳让人头疼的帽衫、衬衫等不规则衣物？（2/2）',
    'video_tag_list': '',
    'content': '上次说的小问题集锦系列哦，这期视频集中回答下[偷笑R]留言私信没精力一一回复，对不起大家喽，我会尽量把问的比较多的问题拍成小集锦，所以，有问题多多给我留言吧[吧唧R][飞吻R]\n由于系统限制只能发5分钟，这是后半部～'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/6899588f-639da4c-8cdd-019bbd3d480f?sign=c9bdb196ea20ddcbb6553f10630c014b&t=65fb06d4',
    'video_id': '59211d223460946c690734b9',
    'title': '蜜桃臀周（2）你的深蹲到底有没有练到屁股？|新手深蹲指南',
    'video_tag_list': '8周变身比基尼女神',
    'content': '#8周变身比基尼女神[话题]#为何所有的健身网红都疯狂的练习深蹲？又为何健身大牛说至少要1-2年才能做出正确的深蹲？今天Weiya与Giselle就和你聊聊深蹲 - 一个练出美腿翘臀必不可少，但又高风险的动作。新手如何练出pro一般的深蹲？我们会犯哪些常见错误？又如何矫正？视频末一个简单的方法，让你少走弯路，早日练出翘臀与美腿。八周挑战的“蜜桃臀”周，快在夏天来临之前给自己一个穿热裤炫耀的理由！欢迎关注我们视频首发的全平台：fit4life健身与美食！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lugF1xUjltcls8BSK1BA3blZR3BR_compress_L1',
    'video_id': '5921204bd1d3b971222bdfa9',
    'title': '',
    'video_tag_list': '',
    'content': '【徒手家庭健身9个动作】一起塑形细腰长腿大胸就是你\n无器械在家健身，只需一张沙发➕你，视频和大家分享，在家无器械健身，一起动起来😍\n【徒手训练】利用自身的重量，不借助器械☺训练全身肌肉力量，达到减脂塑形。\n【8个动作】助你：瘦手臂、还能胸变大😘背部变好看，塑形减脂，保持平衡。\n【道具】一张沙发or 椅子\n【训练量】一周练3次 ，每个动作12-15个，一共4组，每【tips】如果觉得动作有难度，可以选在平地完成，瑜伽垫上也可以 同理哦\n💕女生记得穿专业运动bra再运动，防震。对胸部保护好。组休息30-60秒\n－－－动作 动作 动作 －－\n🌟【上斜侧腹支撑抬腿】瘦腿＋侧腹＋手臂\n告别手臂拜拜肉，累累的动作\n左右两边各手脚单边支撑，一边腿向上抬。用屁股带动腿发力\n要点：收紧核心，保持稳定，不用太快。\n感受：臀部腹部左右侧腹有拉伸感觉 手臂借力\n数量：左右各 15*4\n这个动作有难度，可以在平地做，瑜伽垫上 图4\n🌟【上斜俯卧撑】练胸部＋瘦手臂\n上次练胸的教程，也写到这个动作，练胸好动作\n借助沙发or椅子，踮起双脚，身体呈一条直线做俯卧撑\n要点：挺胸直腰部，和俯卧撑同理\n感受：胸部下侧有拉伸感 后臂有轻微收缩感\n数量：15*4\n🌟【上斜动态平板】侧腹部塑形＋瘦手臂\n两腿左右快速跑起来\n第二天有点酸，塑形好动作\n同上斜俯卧撑，增加难度，两腿向上向内，交替轮流跑。\n要点：收紧核心，保持身体稳定。\n感受：腹部紧绷，肩 手臂 发力，侧腹有紧绷感。\n数量：15*4\n🌟【仰卧屈膝后撑】瘦手臂后侧＋练肩部 图5\n喜欢瘦腿的宝贝们的爱\n🌟【腿高位俯卧撑】瘦手臂＋练胸胸\n考验手臂力量，瘦手臂ing，记得戴运动bra再做。\n数量：12*4（按照自己的承受可以调整）\n🌟【腿高位支撑 左右平移】练腹部＋瘦手臂\n全身一起动，消耗脂肪，塑形长肌肉\n🌟【腿高位 平板左右转体】练左右侧腹＋手臂塑形\n考验腹部核心力量，进阶动作\n.【拉伸拉伸拉伸拉伸拉伸】\n腿部 手臂 记得拉一拉，让肌肉舒缓\n每个动作15-20秒\n－－－－－每次花20分钟，养成好习惯－－－－－\n👉【有氧＋力量训练结合】更好的有减肥塑形效果\n具体详细的笔记 图片教程，在我上上上篇笔记中有😊😍还可看我的 健身笔记专辑哦！\n一起来试试吧，还想看什么教程攻略可用给我留言'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/c9d97585-9c122a4-a21d-cc8132dbe8d1?sign=39b627638ceaee0b659dfb64fcd45a0c&t=65fb06d4',
    'video_id': '5921b9fd7fc5b81f7b2685d5',
    'title': '季度爱用品 | 春2017 | 3月4月5月',
    'video_tag_list': '适合湿敷的化妆水',
    'content': '久等了！我的第一个爱用品视频终于来啦！这几天我不是在参加自己的毕业典礼，就是在参加同学的毕业典礼：D 争取下周开始开启假期高产模式！这是我最近爱用的护肤品化妆品好用的好吃的~如果你们有什么想让我尝试的产品可以留言告诉我哦！\n按照视频出现先后顺序\n1. Wet n Wild Photo Focus™ Foundation # nude ivory 买了之后就用到停不下来！服帖、用了之后妆效很好、不脱妆，重点是太白菜了才5美金！完全值得尝试！\n2. Giorgio Armani Beauty Lip Magnet Liquid Lipstick #504 西柚红很显气色，黄皮友好，不沾杯。\n3. Natasha Denona Star Eyeshadow Palette 无敌的雾面粉质和亮色显色度，色彩搭配也很喜欢，无法不喜欢！\n4. NARS NARSissist Unfiltered Cheek Palette 这个腮红盘有6个非常好看的颜色，设计适合生活里每件小事都愿意自己拿个主意的人（围笑。我每天化妆一打开，然后选喜欢的腮红感觉好开心~颜色也美，可日常可夸张，性价比也很高！\n5. Fresh Soy Cleanser 黄瓜味，太好闻了，温和洗的干净而不干~\n6. Timesless vitamin b5 serum 适合学生党和年轻女孩的精华液，成分很简单，有初期抗老的作用，春天过敏季必备的产品，使用起来真的是秒速吸收！补水效果超好，已经回购了~\n7. muji 化妆棉 晨间快速3-5分钟湿敷适合使用，湿敷均匀不浪费化妆水。\n8. Ginza 化妆棉 在Miibox这个网站买的 软软绵绵，锁水性和颜值我都能给满分！\n9. Origins Dr. Andrew Weil For Origins™ Mega-Mushroom Skin Relief Soothing Treatment Lotion 湿敷最爱的化妆水之一，镇定痘痘有急救的功能，适合痘痘皮和敏感肌湿敷使用。\n10. Organic Bulgarian White Rose Water by Alteya Organics 保加利亚的玫瑰精油品牌出的白玫瑰纯露，太好用了，性价比超高，大牌化妆水的平价替代品。\n11. Origins High Potency Night-A-Mins™ Mineral-Enriched Renewal Cream 适合学生党和年轻女孩的晚霜，立竿见影第二题皮肤细细滑滑，无限空瓶！\n12. belif The True Cream Moisturizing Bomb 太水了太滋润了！第一次尝试这个品牌，好感度超高的！啫喱状也很适合春夏使用。\n13. OLEHENRIKSEN Power Bright™ 3-Step Professional Brightening System 面膜3部曲，磨砂、美白和提亮，其中第二步有有25%的VC，用起来有点刺痛感，但是很好用，第二天皮肤会明显变细变滑变软。\n14. Parfum MDCI Rose De Siwa Eau de Parfum 我在luckyscent这个洛杉矶买手店收的！我最爱的沙龙香之一，颜值真的无敌了，香味也是特别的美国+荔枝，每次我用都会被别人问香水的牌子，千真万确！深度香水控可以种草了哈哈。\n15. Goody QuikStyle Paddle Brush 拯救懒癌的吸水毛巾刷子，谁用谁知道！\n16. Kerastase Nutritive Lait Vital 沙龙洗发店里用得专业护发素，发膜也很好，防止头发干枯受损，也是我回购的一个产品。\n17. Dream Water Natural Sleep Aid, GABA, MELATONIN\n18. Good Day Chocolate - Milk Chocolate with Pharmaceutical Grade Nutraceuticals for Sleep 这两个都是褪黑素的食品，适合和我一样睡眠质量不好的小伙伴~\n#最显白的口红[话题]##最适合春夏的眼影[话题]##我的护发秘籍[话题]##适合湿敷的化妆水[话题]##精华深度测评[话题]##性价比高的保湿精华[话题]##热门面霜测评[话题]##学生党最爱的化妆水[话题]##平价好用的洗面奶[话题]##美白精华推荐[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkHGgWByxUOEifM6tdMoTJ3PKJ5C_compress_L1',
    'video_id': '59224993d2c8a55d8e520cb1',
    'title': '照着这个方子做，新手也能做出大厨的美味！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n红烧猪蹄是很家常的菜肴之一，也是食肉一组不可抵挡的美味。 猪蹄含有丰富的胶原蛋白质，脂肪含量也比肥肉低，并且不含胆固醇。\n对防治皮肤干瘪起皱、增强皮肤弹性和韧性，对延缓衰老和促进儿童生长发育具有功效。 红烧是最简单的做法，也是每个厨房新手一定要学会的美味之一哦！\n★★★★★\n创意指数\n红烧猪蹄\n▼\n红烧猪蹄\n·视频音乐·\nJonny Diaz - Love Like You Loved\n·食材·\n猪蹄、啤酒、花椒、八角\n葱、姜、干辣椒、香叶\n生抽、老抽、糖、盐\n1.葱切花、姜切片备用\n2.水中倒入花椒放入猪蹄，中火煮40分钟，沥干备用\n3.油锅倒入姜片、香叶、八角爆香\n4.爆香后倒入猪蹄\n5.倒入干辣椒、1勺生抽、1勺老抽、1茶匙糖，炒匀\n6.倒入啤酒没过猪蹄\n7.大火转小火焖煮20分钟\n8.撒入少许盐，炒匀收汁盛出\n9.撒上葱花\n10.美味下酒菜就上桌啦~！\n小贴士\n1.猪蹄要用冷水焯烫，才能把猪蹄中的血水煮出来，然后再过凉水处理掉上面的猪毛，这样猪蹄烧出来口感才好。\n#跟着视频学做菜[话题]##超级下饭的家常菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lp4R7tB2YHwfweWkxmEeyM9zk2vM_compress_L1',
    'video_id': '59224ea914de412d45f29197',
    'title': '',
    'video_tag_list': '我和宠物的日常',
    'content': '日常吸猫🐈\n自己的尾巴敲好玩[萌萌哒R][萌萌哒R][萌萌哒R]\n#我和宠物的日常[话题]##随手拍宠物[话题]##我家宠物最萌的瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luInYi3BzdLeTPxCqTWTRhLl7qGX_compress_L1',
    'video_id': '5922746cb46c5d6bc5edc6a8',
    'title': 'TF白管03试色again——我就是TF脑残粉啊！',
    'video_tag_list': 'Amanda Uprichard;克罗心',
    'content': 'TF脑残粉来啦——\n白管03号，太适合这个季节啊！我今天就用了一下ginza防晒隔离就赶紧去教育局办事儿了。皮肤有一点点点偏黄，用这个颜色无比显白，但是我觉得太黑太黄的妹子不要尝试。\n反正我就是爱TF啊，什么颜色都好看啊！只要有她，其他啥啥牌子都可以走开[笑哭R]\n粉嫩粉嫩的颜色，一点都不干！显色好！一切口红具备的优点她都有！颜值还高！\n大白我的大白啊！\n裙子是去年买的\n手环跟项链是\n很多妹子问之前一些视频的背景音乐\n我是一个音乐发烧友\n早前做过很长时间的国内国外音乐节目的电台DJ，我喜欢买CD，不喜欢用蓝牙听歌，所以我家里还有车上有许多cd盘……下一次可以拍一下[笑哭R]\n这次音乐的背景是the chainsmokers的新专辑memories do not open里的第一首和第三首歌，推荐bloodstream'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/3e56f95d3561929e59b03ebbee7fcc83ce397a70_r',
    'video_id': '59227a2f7fc5b83ebe2685d7',
    'title': '视频薯说：“这是一条甜死个人的海岛旅行记录。”',
    'video_tag_list': '',
    'content': "这里是视频薯的频道【小红书上不为人知又超好看的vlog】\n对，很长的名字，我知道。\n视频薯我在这里给大家介绍我书上那些好看的vlog。\n[吧唧R]\n🎬What's Vlog？\nVlog的意思是“视频博客”，来源于bolg（博客）。任何人都可以拍摄一支任何主题Vlog来记录和分析你的生活。\n🎬今日Vlogger： @Ohmykrisss #我的海岛游攻略[话题]##用视频记录旅行[话题]#"
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/18314f74-d411003-bb5c-2ea04d90bb82?sign=8411ba6a36865516a7b886ef48632333&t=65fb06d4',
    'video_id': '59227c087fc5b87bf9ef34d3',
    'title': '平凡料理－不一定好吃的普通食物',
    'video_tag_list': '',
    'content': "🎬外国人眼中的中国食物长什么样？做出来好吃吗？\n🎬What's Vlog？\nVlog的意思是“视频博客”，来源于bolg（博客）。任何人都可以拍摄一支任何主题Vlog来记录和分析你的生活。\n🎬今日Vlogger：  @cbvivi #用视频记录美食[话题]##平凡料理[话题]#\n（戳一下他的名字查看更多视频）"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lk2AYuerGIT3lQNMmOQy5hUzvjsI_compress_L1',
    'video_id': '5922a7bc14de4135a7391cbc',
    'title': '视频卸妆—Bifesta曼丹卸妆纸巾😏敲好用📌',
    'video_tag_list': '卸妆测评',
    'content': '强烈安利！\n懒人必备！为了证明好用我都视频卸妆了[扶墙R]也是拼了\n日本原产🇯🇵的东西不得不说很好用...\n一点都不刺激 我带着美瞳擦眼也不会难受糊眼什么的\n而且很方便 出门带着～之前用过屈臣氏的..很不好用\n所以一直对卸妆纸巾望而却步。但是这款真的打开新世界大门了～\n我自己是在某东的旗舰店买的 建议大家找靠谱的地方买～\n千万不要买到假的....\n现在夏天用卸妆湿巾擦胳膊擦腿卸除防晒霜也很方便\n最后～卸妆很重要！！大家一定要重视！闭口爆痘很多时候都是因为卸妆不彻底～\n#卸妆测评[话题]##平价好用卸妆[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg66FrwnivlBHZW8jFHTamCCJC_a',
    'video_id': '5922e669b46c5d2c774a8ac2',
    'title': '新生儿不会被宠坏',
    'video_tag_list': '宝宝早教这么做',
    'content': '婴儿期：开始种下亲密基因\n新生儿不会被宠坏\n六个月以下的婴儿无法控制自己的行为，自我安慰能力也极其有限，完全依赖成人。经常被拥抱和安抚的婴儿哭得更少，更信任他人，也更独立。\n六个月以后的孩子腹肌强壮到可以自己坐在小床上的时候，才可以让他入睡前哭闹一会。之前在孩子哭闹的时候他需要被摇晃或拥抱。\n孩子不需要电视或者玩具卡片，他需要的是你。\n一些有效的方法\n反复模仿宝宝的声音，会让他有自信和自尊。\n多种触觉游戏，培养孩子的感知。\n通过动作和歌唱让孩子和你一起做运动。\n在和孩子互动时一直说话，解释你在做的事，开始情感启蒙，用语言描述出孩子的情绪状态。\n2-3岁，建立亲密关系的关键时期\n学会设定限度\n仅有情感引导是不够的，家长必须对孩子设定限度，让他们知道什么事情可以做，什么事情绝对不可以做。\n原则是：温柔但是有边界。\n父母可以解释为什么可以或者为什么不可以，能讲道理的\u200d\u200d父\u200d\u200d母更能让孩子信服。\n孩子需要自信心\n给孩子一些自己决策的空间，不要否定他所有的要求。\n打屁股会让孩子缺乏自信，今后在学校表现更糟；而且等于鼓励孩子使用暴力；也会伤害孩子的自尊心。\n用情感引导的方法处理孩子的情绪\n让自己的视线和孩子齐平，进行充分的眼神交流，问他认为自己做的是对还是错；\n如果孩子没有平静下来或者停止错误行为，带他到一个“安静区”或“思考区”，与他一同坐下来。记住，你不是在惩罚他；\n抱着孩子，说出他的感受，表示你理解他的感受，这样有助于他平静下来；\n平静下来之后，问孩子“这是怎么回事？”“哪里做得不对了？”孩子不明白的话你可以解释给他听；\n问问孩子“下次你会怎么做？”如果他不知道，告诉他怎么做才是恰当的；\n感谢孩子帮你想出了解决方法；\n让孩子设想一下“下次又犯了同样的错误会发生什么事情？”告诉孩子，你可以帮助他改正，但你不会容忍不适当的行为。\n通过情感引导而不是赞扬的方法\n简单地告诉孩子你真棒，对孩子是没有帮助的，因为孩子不知道为什么棒，甚至会觉得“棒”很廉价。\n情感引导的方法是更加关注孩子自己的感受，让他知道这件事本身的乐趣和意义。\n家长不是评判他的裁判，而是一个真心的交流对象。“你一定可以的”、“你还可以更好”这样的话会让孩子更加失去兴趣，因为这简直就是责怪。\n正确的方法比如：\n“你现在的这种感觉就叫做成就感，怎么样，很开心吧！”\n“你刚才的表现叫做有毅力，有毅力是很重要的哦！”\n“你这件艺术作品真漂亮，我可以收藏它吗？”“你现在有什么感觉呢？”\n与4-7岁的孩子保持亲密关系\n当孩子难过的时候\n允许孩子难过，每个人都需要宣泄悲伤的通道，不要因为孩子情绪激动而生气；\n允许孩子哭泣，哭泣是悲痛的一个步骤，会有助于孩子的恢复。不要期待孩子任何时候都勇敢坚强；\n同情孩子，让他知道你也会有难过的\u200d\u200d时候，倾听孩子的心声；\n鼓励\u200d\u200d孩子用语言或图画来表达情感，做好一些特殊的心理准备，比如孩子会出现一些行为上的退步；\n关键是让孩子明白悲伤和表达悲伤都是正常的，而且任何时候你都会帮助他。\n培养良好的社交习惯\n孩子是父母的复印件，所以你要先做好社交的示范；\n培养孩子尊重他人的隐私，先要解释什么叫隐私，为什么要尊重隐私；\n教会孩子如何道歉，但不要强迫他们不真诚地道歉；\n让孩子知道抱怨无法让你明白他的需要，教会他如何正确地表达，在他停止抱怨的时候对他表示感谢；\n游戏当中要学会保护别的孩子，不专横。\n孩子害羞的时候\n播下种子：在体验新鲜事物之前帮孩子做好心理准备；\n同情：耐心听孩子诉说，你可以说“有时候我也在刚开始的时候觉得不好意思”；\n和孩子进行角色扮演游戏，预演和陌生人的见面；\n不给孩子贴上害羞的标签，可以说“我知道你不喜欢被别人盯着看”；\n给孩子示范社交生活的乐趣；\n要有耐心；\n鼓励孩子和成年人交流时进行眼神交流；\n永远不要强迫孩子变得活泼外向，也不要逼着他和人交流。\n孩子说谎的时候\n向孩子解释现实和幻想的区别；\n明确界定真话和假话。\n#儿童节送什么[话题]##宝宝早教这么做[话题]##宝宝穿搭打卡[话题]#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/FozfwglQdJEOgk4fEc9RVV0dKb_c_compress_L1',
    'video_id': '5922f437d1d3b96fe62bdfb6',
    'title': '寻梦爪哇 印象印尼行',
    'video_tag_list': '用视频记录旅行',
    'content': '😄消失了一个礼拜 其实是去印尼旅行啦 视频是用另一个手机录的 有点模糊[哭惹R]\n上海🔜雅加达🔜日惹🔜梭罗🔜广州🔜无锡 七天七飞游三地 每天不足五小时的睡眠💤别提多幸苦啦 有累有甜 从婆罗浮屠到bromo火山🌋都留下了深刻的印象 虽说火山之行天气不佳 没有看清全景 留下些许遗憾 但日后一定还会来到这个美丽的热带地区 亲自爬上火山顶端看日出🌄去到人人向往的巴厘岛 龙目岛……\n这个小视频录于日惹街头 是不是很吸引你呢[吧唧R]\n补足元气 后续报道游记 吃吃喝喝 购物分享  买买买的日常😄\n从浦东日上免税店到泰国素万那普机场王权免税店再到雅加达最大的两个商场grand Indonesia   central park最划算最值得入的东西\n#看山看海住酒店[话题]##最爱旅行地[话题]##我的小众旅行攻略[话题]##用视频记录旅行[话题]##东南亚旅行攻略[话题]##日上免税值得买的护肤品[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/b14b48b8-16c68bb-87dd-d696bb720a63_compress_L1',
    'video_id': '59230ee07fc5b85a1eef34d3',
    'title': '一个混油痘皮的夜间护肤步骤',
    'video_tag_list': '夜间护肤步骤大公开;SK-II;赫莲娜 HELENA RUBINSTEIN 夜间超膜精华;SK-II 神仙水2017樱花限定套装;茵芙莎;欧缇丽 CAUDALIE 葡萄籽臻美亮白精华液;柏佰 Bye Bye Blemish 瞬间祛痘精华',
    'content': '一个混油皮肤的夜间护肤步骤，基本上就是：二次清洁、化妆水、眼霜、肌底液、精华、乳液、急救。我个人选择产品的原则非常肤浅，味道好闻＋吸收快就好。这里有sk2晶莹露、sk2神仙水、hr极致之美眼霜、hr夜间精华、欧缇丽美白精华、ipsa乳液还有bye bye blesh的祛痘精华。这里有好多都是我回购又回购的单品，希望能帮到肤质相似的宝宝嗷嗷嗷～#护肤步骤# #夜间护肤##我的护肤日常[话题]##夜间护肤步骤大公开[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/40b3dbd57e40684d1b1e5dedb85fc4b87fa7a42e_r',
    'video_id': '59238c8814de413a56f29197',
    'title': '白灼芦笋到底有多好吃？秘诀就在这酱汁里！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n芦笋这个东西，据说有极高的营养价值。以前不是很常见，如今也算是普通了，只是与其他品种的蔬菜相比，价格还是蛮贵的。\n今儿上道最简单的白灼芦笋——将芦笋修切整齐，入沸水中大火汆烫，浇上最常见的蒸鱼豉油或鲜味酱油，再点缀上几片小红椒，就是一道清新爽口的家常小菜——\n★★★★★\n创意指数\n白灼芦笋\n▼\n白灼芦笋\n·视频音乐·\nDotan - Daydreamer\n·食材·\n芦笋、大葱、小米椒\n蚝油、蒸鱼豉油、糖、盐\n1.芦笋洗净去皮\n2.倒入1勺蚝油、1勺蒸鱼豉油、1茶匙糖、搅拌均匀备用\n3.沸水中加入适量盐\n4.放入芦笋煮30秒\n5.捞出过冷水沥干备用\n6.大葱斜切入刀\n7.冷水浸泡沥干备用\n8.小米椒斜切入刀备用\n9.摆好造型，倒入调料汁\n10.淋上热油即可\n11.健康又美味的白灼芦笋就上桌啦\n小贴士\n1.汆烫芦笋时掌握：宽水、大火、快汆，水中加盐、出锅后过凉，都是为了保持芦笋的鲜绿和脆嫩。\n2.浇汁时，也可以将调料汁直接浇在芦笋上，再浇上热油。\n#好吃的素菜这么做[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/fec490e0-0126f72-b3ae-e08743d1caa6?sign=6206a934f90198d8e5086380108fda82&t=65fb06d4',
    'video_id': '592390113460944efa0734b6',
    'title': '【5月爱用品分享 - Tom Ford，Fresh，Benefit，Bobbi Brown等】',
    'video_tag_list': '馥蕾诗 FRESH 澄糖亮采磨砂面膜;The Beautools FacePump微电流超导美容仪 TBFP-01W;芭比波朗 Bobbi Brown 舒盈平衡粉妆条;汤姆·福特 TOM FORD 完美无痕粉底液;贝玲妃 Benefit 蒲公英婴儿粉红胭脂水凝露;魅可;馥蕾诗;贝玲妃;美容仪体验报告',
    'content': '今天的视频主题呐，是我滴5月爱用品分享，其实之前我一直在录【每月爱用品】这个主题，但是这段时间懒癌有点严重就搁浅了几个月，以后会坚持做每月爱用品的，欢迎大家监督💪\n✔️Products mentioned/都有点啥：\n1️⃣Fresh黄糖磨砂面膜 - 温和祛角质，好用没的说😉\n2️⃣The Beautools Facepump超导美容仪 - 导入，提拉，紧致肌肤的全能型选手，个头也很小随身携带超方便✌️\n3️⃣Bobbi Brown粉妆条，色号0.75 Ivory - 真的没想到这么好用\n4️⃣Tom Ford圆管粉底液，色号01 Cream - 属于各方面发挥很稳定的粉底液，没有特别突出的优缺点，一不小心就用空瓶了，可见确实好用呀😁\n5️⃣Benefit贝玲妃蒲公英液体腮红 - baby pink 嫩嫩的婴儿粉，涂上自然又提起色，非常适合夏天使用哦！\n6️⃣MAC棒棒糖唇釉，色号11 Last Minute - 超美的枚红色，涂上显白up up，之前有分享过试色图文，感兴趣的小伙伴可以往前翻哈！\n.\n以上，希望你们喜欢❤️\n#我的护肤日常[话题]##我最爱的彩妆品牌[话题]##入门级彩妆[话题]##美容仪体验报告[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/1a0a5f64-c16d12f-9138-09af3a82b9ae?sign=e153e0cb10b0416b9411566826e6887f&t=65fb06d4',
    'video_id': '5923a3c77fc5b84b0d2685d9',
    'title': '夏季轻薄底妆+不脱妆的小技巧，快来get',
    'video_tag_list': '',
    'content': '一般想要底妆不脱妆，特别是对于出油的人来说，先用一个妆前打底产品很重要，比如~可以选择苏菲娜的妆前控油产品，可以只用在控油的位置~很多人直接用了防晒就上底妆，油皮也不会用一个控油产品，所以才间接导致了底妆暗沉和快速脱妆的问题。\n对于底妆部分，我个人是觉得，夏季要换持久型的粉底液了，如果还在用滋润款，脱妆是必然，我用下来是觉得露华浓24小时不脱妆粉底液，雅诗兰黛DW的不错，但是！！！这些不脱妆的粉底液通常会有一个毛病，会相对厚重一些，所以我觉得即使是油皮，也用喷湿的海绵蛋上妆更好一些，第一是可以相对的把粉底液的油脂吸附一些出来，但是又不会吃粉，第二就是能够让底妆轻薄一些，而且用量不需要太多，层层叠加的方法效果会更好一些！\n定妆在夏季很重要，想要轻薄就用刷子，然后采用局部定妆的方法就好啦！！！\n欢迎评论区讨论！\n#不脱妆的必胜法宝[话题]##油皮最爱的底妆推荐[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrOIImaBPAJtWeOUJ5CyAWZmwxLH_compress_L1',
    'video_id': '5923c087d1d3b968072bdfa7',
    'title': 'maje16年春夏民族风连体裤露肩露肩＋GGDB小脏鞋',
    'video_tag_list': '',
    'content': '这条连体裤去年买的，一次没有穿过，今年他们家也出了一字肩的连体裤，而且带褶皱公主风的，也超级美丽，都是高腰收的设计，所以很显瘦。我比较爱maje，然后又适合我的预算，还没有买得起大牌的裙装[笑哭R]maje我都穿一码，身高168，体重今天是109，不确保明天会不会超过，哈哈哈哈哈哈哈，我要控制成106，是我的目标[再见R]\n我也是GGDB的脑残粉，今天穿的是小黑尾，平时37.5的脚，买都是买38码，喜欢稍微大一点，这样才不用动手拖鞋……也不用系鞋带……一伸脚，顶多弯个腰拔一下就好了……太适合我这种懒人了[害羞R]\n祝大家天天美美的，好心情❤'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/55f0cf43165b8eb21d849718a3883ab46a8dd0ef_r_ln',
    'video_id': '5923c32714de415860f29196',
    'title': '设计不合理的衣柜真的就没办法好好利用吗？（1/3）',
    'video_tag_list': '',
    'content': '家里的大深柜、太深/太浅的悬挂区、衣柜死角怎么合理利用？收纳工具到底怎么选？还有我做衣柜的一点经验教训都在这里喽[飞吻R][飞吻R]\n由于系统限制只能发5分钟，这期内容拆成3部，这是第一部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lorICMes2NQMLONvOd0fhWxrpCKA_compress_L1',
    'video_id': '5923c42914de415b49f2919a',
    'title': '设计不合理的衣柜真的就没办法好好利用吗？（2/3）',
    'video_tag_list': '',
    'content': '家里的大深柜、太深/太浅的悬挂区、衣柜死角怎么合理利用？收纳工具到底怎么选？还有我做衣柜的一点经验教训都在这里喽[飞吻R][飞吻R]\n由于系统限制只能发5分钟，这期内容拆成3部，这是第二部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/6d079c998f494841d99208ffcfcdd7a9ecb57068_v1_ln',
    'video_id': '5923c4a2d1d3b97293a9136f',
    'title': '设计不合理的衣柜真的就没办法好好利用吗？（3/3）',
    'video_tag_list': '',
    'content': '家里的大深柜、太深/太浅的悬挂区、衣柜死角怎么合理利用？收纳工具到底怎么选？还有我做衣柜的一点经验教训都在这里喽[飞吻R][飞吻R]\n由于系统限制只能发5分钟，这期内容拆成3部，这是第三部～\n#视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvkOri9ecFGCP4LUSXTtSml7he2V_compress_L1',
    'video_id': '5923d487d1d3b924ad2bdfa9',
    'title': '🎠Olly的日常小视频 -5M14D',
    'video_tag_list': '',
    'content': '亲子瑜伽是什么 可以吃吗？\n反正我有手指吃 你们爱怎么折腾我都行!'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/cd3a3e6a98d053a40024d111d41f4899894cf8be_v1_ln',
    'video_id': '5923d6ea7fc5b848eeef34da',
    'title': '百元以下！热门防晒霜测评，你一定用得到~',
    'video_tag_list': '',
    'content': '从左到右→ 娜丽丝，悦诗风吟，碧柔，近江兄弟红色，近江兄弟蓝色，曼秀雷敦，妮维雅，露得清， 凯伊秀，一共9款。\n#学生党爱用平价防晒[话题]##出门必备防晒喷雾[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/a62048e5-389846a-8cda-6dab4b83a879?sign=854d5ae75fa6d54e60b9044fb401adab&t=65fb06d4',
    'video_id': '59240477a9b2ed53e0bd781d',
    'title': '香辣干锅土豆片',
    'video_tag_list': '',
    'content': '香辣干锅土豆片，不用油煎也很好吃。再加上孜然，我能配着这道菜啃一根板凳腿儿。\n#人人都爱土豆料理[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lo_3VjOR327YaoMcgVqpYGGibnI6_compress_L1',
    'video_id': '59240799d2c8a50a3e520cb3',
    'title': '新手指南 底妆步骤及产品选择',
    'video_tag_list': '完美底妆这样画',
    'content': '有妹子经常会问到底妆的问题 在这里统一给大家回答一下虽然网上也有一些功课 我在这里就全部给大家说了 全部的看法都来自于我自己做的功课和经验总结\n也欢迎大家多多交流\n💕上妆步骤：\n基础护肤👉🏻防晒👉🏻妆前乳/隔离👉🏻粉底👉🏻散粉\n💕产品区别及选择（所有产品均为举例 不是推荐 是否好用自行尝试或者功课 仅针对用途而言 不讨论效果）\n💋防晒：防晒属于护肤的步骤 这一步一定不能少\n比较清爽的 比如sofina小蓝花\n比较油腻的 比如 安耐晒的小银瓶\n比较水润的 比如 妮维雅和碧柔\n推荐产品：安耐晒 sofina 资生堂\n💋妆前乳/隔离\n这两个东西是一样的 二者选其一就好\n根据自己的肤质以及所需要的妆感妆效来选择 以下举例：\n💄水润保湿 防止浮粉：娇兰金箔 espoir珍珠妆前乳 玛丽黛佳红参妆前乳（这种妆前乳类型推荐 油皮干皮都可以）\n💄油润款 底妆更服帖：VE面霜 embryolisse保湿妆前隔离乳（但可能会脱妆比较快 太滋润也会出现搓泥 注意用量）\n💄控油款 ：sofina控油妆前乳（注意太干的皮肤可能会起皮）\n💄修正肤色款：兰芝隔离。makeup forever妆前乳（个人觉得效果一般 可以考虑调色盘试的遮瑕）\n💄平滑毛孔：benefit 反恐精英（但据说含硅 长期使用对皮肤有伤害）\n💄提亮 增加光泽度：vdl贝壳提亮液 covermark提亮妆前乳（我觉得这类基本没啥用 可以考虑混在粉底液里）\n💄美白类： za隔离（我妈挚爱款 擦上就很白 没啥遮瑕度 可以和粉底调色）\n推荐产品：Laura mecier 妆前乳 rmk cpb\n💋粉底液/粉霜/粉膏/气垫/粉条/粉饼\n这些产品有各自的特点 具体产品请大家自行功课 使用感及色号问题 也请大家做功课或者购入分装\n💄控油遮瑕度高类：雅诗兰黛 double wear（可以配合控油妆前乳和控油散粉使用）\n💄滋润类：bobbibrown 虫草粉底液 rmk圆管粉底液（滋润度不够 可以混合滋润的面霜妆前或者精油）\n💄哑光妆效：ysl羽毛粉底液 Dior恒久凝脂粉饼（一般哑光妆效底妆偏干 粉饼挺干 我一般补妆用）\n💄奶油肌妆效：suqqu粉霜（这个一直长草 就是贵 另外听说易暗沉？）\n💄哑光慕斯妆效：Dior恒久凝脂粉底液 tater粘土粉底液 美宝莲新品气垫（个人觉得Dior色号不够白 粘土妆效到后面就不是特别精致了 美宝莲挺好 性价比超高 有兴趣可以看我之前的测评）\n💄光泽肌妆效：雪花秀气垫 hera气垫（个人感觉 脱妆快 易暗沉 遮瑕一般 非要对比 雪花秀比hera好用 但比不上luna粉霜）\n💄特别水润清薄类：makeup forever水粉霜 江原道粉底液（muf的水粉霜是挚爱 新款没用过 偏爱高遮瑕度的妹子可能很讨厌 江原道的还在磨合 不知道为什么 浮粉卡粉的现象很严重 不应该是一个水润底妆该出现的问题）\n💋一般来说 遮瑕度高的妆感会重一些 太过有光泽感 太滋润的更易脱妆 气垫类持久力相对较差\n个人建议 不要依靠粉底遮住全部瑕疵 若有很多很严重瑕疵需要遮住 可以借助于遮瑕产品\n💋散粉/蜜粉饼/蜜粉\n基本上都是起到一个定妆的作用 基本没颜色没遮瑕度\n💄控油款：nars蜜粉饼 makeup forever hd蜜粉/蜜粉饼（这几款都是网红产品 没有尝试过但好评满满）\n💄提亮润色类：elegance蜜粉饼 Givenchy四宫格散粉（这两个也是没有尝试过 四宫格散粉好像也有焦柔效果）\n💄磨皮焦柔类：Laura mecier 散粉（这个功能大部分定妆产品都能做到）\n💄干皮适用类：Charlotte tilbury蜜粉饼（这块口碑很好 也在我的草单上）\n💄不改变底妆妆效类：rcma transparent powder（还有一个no-colour powder 不改变妆效的应该是透明的那个）\n以上为基本的底妆步骤 关于遮瑕产品也有很多功课可以做 以后再补充吧\n总之 明确自己的肤质所需要的妆效 最好可以靠柜或者购入分装试用 以及 不要过度追求底妆的持久和高遮瑕 最好四五个小时悄悄抽空补个妆 妆面干净 也能让自己心情变好\n希望大家都能找到自己的真爱底妆产品\n欢迎点赞收藏留言关注 比❤️\n#完美底妆这样画'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luBadTn4JA2ZbRC02pV1BPbfHsOR_compress_L1',
    'video_id': '59243b0614de4133d8f29196',
    'title': '超详细修眉画眉教程',
    'video_tag_list': '',
    'content': '浓眉星人看过来！\n超详细的修眉+画眉视频！！😜\n#实用的修眉小技巧[话题]##简单易上手的画眉方法[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luxnYBgB5OndbgzFYtRv2Gc_kkrd_compress_L1',
    'video_id': '59243b94b46c5d68154a8aba',
    'title': '空瓶记2⃣️3⃣️',
    'video_tag_list': '空瓶记;加拿大',
    'content': '如题！\n终于剪出来了[笑哭R][笑哭R][笑哭R]\n祝小仙女们食用愉快！[得意]\n#空瓶记[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FqyqUeRx-9ND-OBEZbTovF2HwWIQ_compress_L1',
    'video_id': '59245969b46c5d3a00847be0',
    'title': '最近发质回春啦💆',
    'video_tag_list': '我的护发秘籍',
    'content': '近期会发一个护发心得篇\n🍠们想看啥都可以告诉我[喜欢]\n比如是洗发水、烫染还是卷发教程（我基本现在都是自己夹头发）\n问的多的我会在心得里解答～\n#我的护发秘籍[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/91b091d98ba70f676253b272b8a550bd12c3cfea_r_ln',
    'video_id': '5924e5e4d1d3b95b073e722c',
    'title': '教你用13种调味料，做一道艳惊四座的土豆料理！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n土豆虽然不是什么山珍海味，但是它的营养价值却是很高的，各种维生素、膳食纤维等物质可以大大满足我们身体的需要，适合大部分人食用。\n每天坚持吃一点土豆，对身体是极好的。土豆丝的做法也是很简单的，每个人都会做出不同的味道，只要是自己喜欢的就是最好的美味。\n★★★★★\n创意指数\n十三香土豆片\n▼\n十三香土豆片\n·视频音乐·\nLauren Aquilina - Time To Say Goodbye\n·食材·\n土豆、圆葱、姜片\n葱花、香叶、草果、白蔻\n八角、干辣椒、花椒、辣椒粉\n白芝麻、花生酱、糖、盐\n1.土豆洗净去皮\n2.切成均匀薄片\n3.放入冷水中泡去淀粉\n4.炒锅放入干辣椒、花椒、草果、香叶、白蔻、八角、小火炒至断生盛出\n5.放入研磨机打成粉末\n6.将调味粉倒入碗中，加入1勺辣椒粉、1勺白芝麻、适量的盐搅拌均匀\n7.热油锅倒入圆葱片、姜片，炒香后，打出不要\n8.将葱姜油倒入辣椒碗中搅拌均匀备用\n9.取一个空碗倒入适量花生酱、1茶匙糖、适量清水搅拌均匀备用\n10.浸泡后的土豆片沥干水分，放入沸水中氽熟，快速捞起，放久则不脆\n11.淋上料理汁拌匀\n12.最好撒上葱花即可享用\n小贴士\n1.调至辣椒粉时盐可以适量多放些，口清则少放些\n2.土豆过水时尽量时间少些，以免影响口感\n#人人都爱土豆料理[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmOYphmgIIOT2yg_528oN6UD7ei0_compress_L1',
    'video_id': '5924e74dd2c8a56835c13fd2',
    'title': '精致小耳坠✔️',
    'video_tag_list': '精致的小耳坠',
    'content': '给大家推荐一些便宜好用的饰品～\n今年开始对耳饰的选择就两个字：夸！张！\n哈哈哈哈哈哈～也不知道为什么～偏爱夸张的耳饰～\n可能显得脸比较小？\n1⃣️是我的最爱～很像窗帘布有木有～哈哈～但是超好搭配～每一块蕾丝下面都有一粒小水钻～细节满分～这款名字叫海边沙滩仙女款～没错～戴上就是仙女儿～\n2⃣️这款很神奇～为什么我不停摇头呢（其实每一副我都在摇头哈哈哈哈～因为立方体是炫彩色～并非固定角度下的“绿色”～会有其他颜色出现～小巧精致又特别～\n3⃣️一定不陌生～之前穿搭有出现过～我是爱心控～任何爱心形状的东西我都会觉得很可爱～蕾丝爱心更爱金色～百搭款～有点小女人～\n4⃣️最近爱少女心～看到粉色迈不开步～大气水晶珠花～一秒变温柔～参加party首选款～质感hin好～头发梳上去戴特别美～\n5⃣️这款被我称为夜店款～哈哈哈哈～为啥呢～那天画了个红唇戴上这款我就跟我朋友说：妈呀～这节奏是去夜店的啊～她点头赞同～噗噗噗～其实有点民族风囖～\n6⃣️最近很流行这种个性夸张的长款耳环～我选择镂空五角星⭐️（最好看！！走起路来～耳环跟着随风摇摆～之后穿搭也会配到这一款～超美\n7⃣️又是一款五角星耳环（谁刚刚说是爱心控的～谁！！！这不是打自己脸嘛～那个～我也是五角星控啊～哈哈哈啊哈哈哈～大圆圈里面镂空五角星～特别～\n8⃣️925银水晶冰花～有木有冰清玉洁的感觉哈哈哈～这形容词也是够了（其实想破脑袋～也是小巧精致款～\n9⃣️大圆圈就不用我介绍了～欧美百搭款～最近看到好多人戴大圆圈啊～果然也是我喜欢的类型～\n1⃣️0⃣️两边不对称耳钉～一边为爱心💗另一边为水滴💧闪闪的简单可爱～日常可佩戴～\n店名：Dreamwa～\n如果大家喜欢～以后可以多给大家拍耳环视频啦啦啦啦～\n#精致的小耳坠[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fsi2tRvLbc9jeBibj5qs_5q7X6iJ_compress_L1',
    'video_id': '5924f5c0d2c8a50984c13fd9',
    'title': '这香菇、不、包子好假！',
    'video_tag_list': '美食才是人生主角',
    'content': '早饭吃了个假包子！长得像香菇，其实是包子！\n#美食才是人生主角[话题]##全球美食跟我走[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/e630fa73-497ac31-bbb3-1f85b4225a90?sign=a7c8a474b13414ba8076f90953951618&t=65fb06d4',
    'video_id': '5925280fa9b2ed43dc39834d',
    'title': '超现代厨具',
    'video_tag_list': '',
    'content': '试问谁不想拥有这样一套科技感十足的厨具呢'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/7b9d7a02-8024e4b-8ed1-caa44dc70b5b?sign=7681cd8ecb62be72e1a2ca07a86c4144&t=65fb06d4',
    'video_id': '592547a57fc5b81905a0ee3b',
    'title': '自从加了父母微信，更加相信自己是充话费送的...',
    'video_tag_list': '',
    'content': '加父母微信是什么体验\n发朋友圈不敢随随便便\n养生知识堪比电商诈骗\n时不时还被被朋友圈鸡汤净化心灵一百遍~'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/dd56f8e4-8a7ce6d-9221-beade9da48ff?sign=d748a4e47c517a08c2fba34fc6b09258&t=65fb06d4',
    'video_id': '592557727fc5b8623f2a9056',
    'title': '需不需要卸妆？200元左右防晒霜评测，看敏感肌适合哪款？',
    'video_tag_list': '',
    'content': '从左往右→Fancl，理肤泉，雅漾，雪肌精，ipsa，索菲娜，怡丽丝尔，兰芝，安耐晒~\n#学生党爱用平价防晒[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnlBvvvASN1EYaIrBxGXvIcXlU8T_compress_L1',
    'video_id': '59255edd14de417f38692871',
    'title': '今日话题：视频记录下厨',
    'video_tag_list': '',
    'content': '对于爱下厨的人来说，一天里最幸福的时刻莫过于在厨房里消磨创作。❤️\n从打开冰箱开始构思今晚做什么菜，到切菜洗菜准备食材，再到磨刀霍霍、大开油锅，每一步都有它独特的乐趣。生活薯今天就期待大家来#视频记录下厨[话题]#\n如果你是亲自下厨，也许可以拍摄这些片段：\n-\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 打开冰箱，介绍一下里面有什么食材；\n-\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 拍摄做菜时的关键步骤，解说一下怎么做；\n-\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 美食出炉时，热气腾腾诱人的样子；\n如果在家下厨做饭的是你家人，你可以拍摄：\n-\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 大秀刀功的切菜瞬间；\n-          技艺娴熟的包点心手法；\n-          大厨下厨时认真的样子\n……\n视频片段来自小红薯@Xuanananananan @小吃货羚羊 @天空zz @cbvivi @小兔纸乐乐'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgtcJZzibeNA4SWmBDgZP-FgbWpi_compress_L1',
    'video_id': '59261cebd2c8a520e4d21a35',
    'title': '香气十足的百香果柠檬果酱简单制作',
    'video_tag_list': 'Bormioli Rocco波米欧利.罗克 四季玻璃密封罐 双耳款 300ml 2只装;水果甜品在家做',
    'content': '#视频记录下厨[话题]#\n百香果柠檬果酱\n用料：百香果   3个\n柠檬       1个\n冰糖       70克（我口味偏甜喜欢偏酸的可以少放10克）\n✨先将百香果切开，用小勺挖出放入锅中\n✨🍋切块挤出柠檬汁（这里我只用汁不用皮有些配方会加柠檬皮看各人口味决定）\n✨加入冰糖开小火煮，煮的时候用勺经常去搅拌，防止粘锅，看到变到浓稠后就关火\n✨最后将果酱装入果酱瓶～完成制作[赞R]\n✨果酱瓶我是买的是波米欧利.罗克的300ml装感觉有点大了，应该150ml的就可以了，🤦\u200d♂️所以我今天又在小红书下单了150ml的果酱瓶\n✨今天做的果酱呢是为了后面即将出来的美食做的准备，敬请关注\n\n#大爱水果季[话题]##水果的有趣吃法[话题]##水果甜品在家做[话题]#\n#最爱吃的水果[话题]##吃货小分队[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqoV_aZDcS9bVt6f0ybjToxxqK0S_compress_L1',
    'video_id': '59264db214de41255b905dcf',
    'title': '0厨艺也能轻松搞定的甜点——木瓜牛奶冻',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n很简单的两样东西，竟能做出这么漂亮的甜点，家里有客人的时候端出来绝对为你赚足面子，更关键的是绝对的零厨艺也能轻松搞定。\n冰冰凉凉的木瓜牛奶冻，香甜的木瓜醇香的牛奶冻，炎热的夏天，把这份冰爽的美味端上餐桌。\n★★★★★\n创意指数\n木瓜牛奶冻\n▼\n木瓜牛奶冻\n·视频音乐·\nMindy Gledhill - California\n·食材·\n木瓜、牛奶\n吉利丁片、糖\n1.吉利丁片用冷水泡软\n2.锅中倒入200g牛奶\n3.倒入30g白糖\n4.大火烧开\n5.将泡软的吉利丁片放入热牛奶中\n6.搅拌至融化，放凉备用\n7.木瓜洗净，沿1/4处切开\n8.用勺子将木瓜籽挖去\n9.将放凉的牛奶倒入木瓜中\n10.盖上瓜盖，放入冰箱冷藏3小时\n11.将木瓜对半切开\n12.接着再对半切开，再改刀切成小块\n13.摆盘即可开动！\n小贴士\n1.木瓜去籽时，内壁也要轻轻刮干净，切出来的冻会很整齐\n2.热牛奶时大部分会出现奶皮，滤去即可\n#在家做甜品[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fq5lAIKilI_0aqhPxF8CvvbEHXpV_compress_L1',
    'video_id': '59268b2ad1d3b962046c2554',
    'title': '一言不合就抱起女儿在优衣库尬舞',
    'video_tag_list': '爸爸带娃记',
    'content': '#爸爸带娃记[话题]#\n当时我在结账\n扭头一看\n这边随着优衣库动感的BGM\n已经跳起来了😂\n相比妈妈带娃的套路\n不得不说爸爸带娃还是花招多🙂'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpWC-KHWvMk3YlZ5T0lgGJXAAHeU_compress_L1',
    'video_id': '5926a48ed2c8a5192d326968',
    'title': '不后悔的包包收纳法你错过了几条（1/2）',
    'video_tag_list': '',
    'content': '#收纳小诀窍[话题]#\n包包系列来了哦👛👛花几个亿买了太多包，你的收纳方法会损害包包吗？着急出门却总是找不到想用的那一个？或者常常忘记小包塞进了哪个大包里？\n系统限制只能发5分钟，分上下两部发，这是第一部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmUbOzn2LtdRBrklcLOhLSgKkKSX_compress_L1',
    'video_id': '5926a60cd2c8a51d66326968',
    'title': '不后悔的包包收纳法你错过了几条？（2/2）',
    'video_tag_list': '',
    'content': '#收纳小诀窍[话题]#\n包包系列来了哦👛👛花几个亿买了太多包，你的收纳方法会损害包包吗？着急出门却总是找不到想用的那一个？或者常常忘记小包塞进了哪个大包里？\n系统限制只能发5分钟，分上下两部发，这是第二部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgX_UQ_VXQkDs4NwaPSqmdmoQiFV_compress_L1',
    'video_id': '5926dafbb46c5d3fad081691',
    'title': '大巨蟹老师下课就靠逗逼跳来调节心情—Chanel气垫好用啊啊',
    'video_tag_list': '',
    'content': '今天用了新款Chanel气垫哈\n果真是一个字！润润润润润！\n还有一个字！好好好好好！\n我用的是n20，觉得很好，很自然，荷兰只有12号色，就是粉色一白，然后就是20号色啦，没有10号哎！20色我觉得妥妥的！\n衣服裤子我下一篇帖子讲！\n音乐我下下下一篇日志再分享！\n今儿一天打包了40多个袋子的东西……上了3个小时课……累死……但是只要可以瘦！啥都可以忍！\n❤'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lisWQLg02G11zXDz1yEmz7FUQOvP_compress_L1',
    'video_id': '5927654bb46c5d30a6d280be',
    'title': 'wi化妆视频|烈日逛街妆',
    'video_tag_list': '跟着视频画眼影;芭比波朗;乔治阿玛尼;KIKO',
    'content': '新视频出炉~\n最近特别喜欢这种超级干净的妆容，大夏天都无压力感 夏天最怕脱妆，我的皮肤只出油不脱妆，平时用吸油面纸吸下，粉饼按两下就可以了。\n最近好喜欢用#canmake#粉饼做定妆，皮肤质感超好，可能用它也是我不容易花脸的理由\n夏天用#armani阿玛尼#大师粉底液太厚了，混点#YSL#超模粉底液进去刚刚好。\nCPB的防晒隔离我准备入手正装了，我觉得不错不错。质地还是很喜欢的，刚上脸有点腻一回就会被吸收，很滋润呢！\n大家喜欢这款妆容就继续看视频吧~\n#跟着视频画眼影[话题]#\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/6af89a03893df4f764d9453ad73421c478bde661_r_ln',
    'video_id': '59278313b46c5d4e9ad280d2',
    'title': '这道菜打破你对苦瓜的印象，让你从此爱上它！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n老辈人世世代代传承下来的生活经验都是很有科学根据的。俗话说：“夏日吃‘苦’，甚似进补”。\n夏季暑盛湿重大多数人的心火比较旺，吃一点降心火的“苦”菜（苦味的蔬菜一般偏凉性）会比较好。\n★★★★★\n创意指数\n苦瓜炒咸蛋黄\n▼\n苦瓜炒咸蛋黄\n·视频音乐·\n·食材·\n苦瓜、咸蛋黄\n葱、盐\n1.放入适量咸蛋黄碾碎\n2.倒入碗中备用\n3.葱切花\n4.苦瓜洗净，切出两头\n5.苦瓜切半\n6.用勺子刮去内瓤\n7.切成薄片备用\n8.锅中撒入1茶匙盐\n9.水开后倒入苦瓜略汆后捞出过冷水滤干备用\n10.热油锅倒入咸蛋黄\n11.炒至变软倒入苦瓜片\n12.清炒炒至咸蛋黄完全包裹住苦瓜，撒少许盐调味，炒匀盛出\n13.最好撒上少许葱花点缀即可\n小贴士\n1.我喜欢咸蛋黄是颗粒状的，所以不会碾得很细。你可以随自己喜欢调整。\n2.炒蛋黄时加少许料酒可以起到去腥的作用。（选用）'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lv9A5J-x468UZ-NjrfO5o1OTyKXq_compress_L1',
    'video_id': '59278cccd1d3b96d52839a56',
    'title': '罚站，抖不停🐶',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '#我和宠物的日常[话题]##我家宠物最萌的瞬间[话题]#\n做了错事，被罚站，在窗帘上尿尿！！\n我家狗子的必杀技是：装可怜！！！！\n看他一副可怜巴巴的样子，还不停地抖😔谁忍心罚他很久，这招屡试不爽😢\n我觉得他就是个🐶精！汪星人星球来的...\n视频里的声音是我妈的，天生大嗓门，吓到大家不好意思😂'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/cba1a578-adb48d8-ad1d-618b4a443afa?sign=a450dcef4d7cd7504c2bd5130070b89f&t=65fb06d4',
    'video_id': '5927a0427fc5b85f43cd7f6d',
    'title': '五月包包购物分享',
    'video_tag_list': '',
    'content': '以后大多笔记可能会用视频的方式跟大家分享\n感觉视频更直观 也更能让你们看到产品实物的样子 无ps 无美颜\n嘻嘻\n先跟大家讲讲我这个月买的三个包\n1.Wconcept Comme.R Fillette Mini Yellow\n2.SANTA ANNA MINI BLACK\n3.Celine Box #冰川蓝\n#购物分享 #包包购物分享'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/90bdf19c-293d1ea-b3c0-9eb0d3b89b11?sign=1f3fe992cba3cd8ea82c188bb613dc75&t=65fb06d4',
    'video_id': '5927b2c37fc5b84f09cd7f6c',
    'title': '在家就能做的蜜桃臀训练',
    'video_tag_list': '8周变身比基尼女神',
    'content': '#8周变身比基尼女神[话题]#千呼万唤始出来，你们要的在家也能做的#练出翘翘蜜桃臀[话题]#来啦！之前反复强调肌肉训练效果的两个重要因素：阻力和运动幅度。在家运动幅度完全可以保证，但是阻力肯定比健身房稍逊一筹啦，所以建议大家去买一套不同重量的弹力带和哑铃哦。八周变身比基尼女神第五周，蜜桃臀周结束啦。希望我们的三期视频（臀肌组成和黄金臀部训练、细说深蹲、以及家庭臀肌训练）可以帮助大家从此走上练臀的不归路哦！记得关注我们的视频首发同名平台 fit4life健身与美食，并按时打卡@fit4life 哦'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/56be25faba59dff351cc81e63f1588f195504dd7_v1_ln',
    'video_id': '5927bf577fc5b80684cd7f6f',
    'title': '这些美爆了的3D果冻花居然是一根吸管做出来的',
    'video_tag_list': '',
    'content': '今天我来分享一款3D果冻花的做法，外观非常漂亮，晶莹剔透的果冻里盛开出一朵朵立体的花，简直就像艺术品一样，不光可以吃，还可以观赏。\n口味和造型都由你决定，拿来送人一定可以惊艳到对方。\n无论是脱模前还是脱模后都相当吸引眼球，如果要做来卖，摆在冷藏柜里绝对吸睛，携带也方便，直接连盒子拿，也不用担心把造型弄坏了，如果是堂吃可以在上桌前脱模摆盘即可。\n你还可以发挥自己的艺术天份，把吸管剪成不同的形状来做出不同造型的花朵。\n赶紧行动起来吧！\n#在家做甜品[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/852x480/vcodec/libx264/pgc/723e5b00-1e0d74e-ba46-eeb32fb56ab6?sign=dbb87f8feba1f6942feab1baf22b6c07&t=65fb06d4',
    'video_id': '5927c5617fc5b82595cd7f6d',
    'title': '年度彩妆爱用品榜单上篇| 防晒、底妆和腮红',
    'video_tag_list': '适合黄皮用的腮红;适合黄皮用的腮红',
    'content': '#我的彩妆测评[话题]##囤防晒[话题]##底妆评测看视频[话题]##适合黄皮用的腮红[话题]#\n防晒：🌟\n首先是防晒这两支是我近期最爱用的防晒霜，都很适合干皮使用，作为妆前打底效果也是刚刚的！[飞吻R]\n1️⃣Tatcha毛孔隐形防晒霜[得意R]\n这个品牌很受Youtube上的美妆达人们推崇，虽然价格稍微贵妇点但口碑超级好[赞R]，比较适合熟龄肌和干性皮肤使用。\n它开宗明义就叫pore perfecting sunscreen，具有毛孔隐形的功效，质地在我用过的防晒霜中算是很特别的，擦上去之后滋润得来又不会让你油光满面，显得皮肤特别细腻，也会让后续的底妆更加服帖，跟某些单擦会显得厚重的粉底搭配起来简直有化腐朽为神奇的功效。加上SPF35的防晒指数和防UVA的功能，日常使用是完全足够的，可谓除了贵点没其他缺点了。[扶墙R]\n2️⃣资深堂ELIXIR弹力保湿防晒霜[得意R]\n这款具有保湿功能的防晒乳我已经用到第二只了，SPF30的防晒指数同样是适合日常使用的。[飞吻R]\n它涂上去是轻薄的乳液质感，擦上之后有种自然润泽的效果，肤感舒适不会泛或拔干，在干燥的冬天和春天都很适合[飞吻R]，就像是一个带有防晒功能的保湿隔离乳。\n以上两款价位稍高，如果你还是学生党的话可以用这支我也推荐过N次的碧柔小白防晒霜，SPF50的防晒指数性价比也超高\n底妆：🌟\n1️⃣兰蔻气垫CC霜[得意R]\n底妆我还是喜欢这个安利了无数次的兰蔻的气垫CC霜[汗颜R]，因为用它来上底妆真的是很轻薄、服帖，皮肤会变得滋润又有光泽[害羞R]。虽然以前介绍过的一些其它底妆产品也能达到类似的效果，但都需要配合海绵蛋蛋来使用，每次都要洗真是太麻烦，相比起来气垫粉底要方便太多，更适合赶时间（懒）的人。[偷笑R]\n2️⃣Armani无痕遮瑕膏（2号）[得意R]\n因为兰蔻气垫CC的妆感比较自然清透，如果有痘印之类的瑕疵我会搭配这款Armani的遮瑕膏使用。最近下巴的地方有一些生理痘印，用这款遮瑕膏之后在镜头上基本是看不出痘印的。\n3️⃣嘉娜宝2016天使蜜粉饼[得意R]\n嘉娜宝每年都会推出限量的天使蜜粉系列[飞吻R]，我这盒去年你们在去年的化妆视频里就见过了，这么大一罐蜜粉硬生生被用到铁皮的状态，就知道我有多喜欢了[笑哭R]。\n但是需要吐槽的一点是它的盒子太大了[笑哭R]，只能放家里使用。外盒的塑料质感略显廉价，不知道为毛那么多人吹嘘它包装美轮美奂啊。。。[哭惹R]吐完槽还是不得不承认粉质确实很好，用它做定妆会有种磨皮柔焦的感觉，即使凑近看也无可挑剔，跟兰蔻CC搭配起来用会让人上瘾的感觉。\n腮红部分：\n1️⃣Laduree蛋蛋腮红膏[得意R]\n蛋蛋腮红已经是我回购的第三个了，它质感好、上妆方便，擦上去的颜色很自然，持久度在膏状腮红中也算高的，长相更是招人爱[飞吻R]。不过用多了总想换个别的试试，这次就重点介绍我最近发现的一款平价好用的腮红。[赞R]\n2️⃣Milani浮雕玫瑰花瓣腮红[得意R]\n这款腮红便宜大碗长得也好看，我最推荐的是11号色Blossomtime Rose，也被很多美妆博主称作是平价版的高潮色。[害羞R]它是蜜桃色带有一点金色的偏光[赞R]，扫在脸上之就像运动之后自然散发的好气色，还隐约闪着光泽，所以擦了这款之后在苹果肌都不用打高光了。[害羞R]\n作为资深手残星人[扶墙R]，我刷很多粉状腮红都容易失手搞成猴屁股[哭惹R]，但用这块就算反复刷个两三次也还是很自然。有件奇怪的事情是很多朋友看了视频之后去做功课，然后问这个腮红是不是会有臭臭的怪味道[笑哭R]，但我拿出自己那块使劲凑近鼻子闻也并没什么异味啊？[叹气R]\n上集部分就暂时介绍这么多了，下集还有更多好用的彩妆品介绍，敬请期待哦'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/45a6dff8-8c655d2-9733-5bb2804af840?sign=0b7f60ce94c570431d3ed5b496a6ab57&t=65fb06d4',
    'video_id': '5927c6377fc5b82bd20d6225',
    'title': '试问谁不想拥有这项云技能',
    'video_tag_list': '',
    'content': '试问谁不想拥有这项云技能？专治懒、手残！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/10fd2c96-98143b0-9e3b-1d84d95b5920?sign=ef94e701b376cb2e2a458c5d75ae1937&t=65fb06d4',
    'video_id': '5927cf947fc5b8596acd7f6f',
    'title': 'DIY猫咪凉席卷！身为铲屎官的你是时候挺身而出了！',
    'video_tag_list': '',
    'content': '打败本喵的不是天真，是天真热\n如此火热的天气，\n高冷喵星人也hold不住！\n材料\n橡胶圈 / 腰带 / 凉席 / 热熔胶\n步骤\n①\n准备数个橡胶环\n②\n数个腰带\n③\n一张凉席\n④\n在凉席上涂上热熔胶\n⑤\n将橡胶环固定在凉席上\n⑥\n用多个橡胶环固定\n⑦\n再铺上一层凉席\n⑧\n用腰带捆绑装饰\n⑨\n猫咪凉席卷就完成啦～'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/58573478-095d73d-a179-c397168ef904?sign=b589c1f652571a820a6fd92c5f3417b7&t=65fb06d4',
    'video_id': '5927dd887fc5b82484cd7f6c',
    'title': '下血本！“贵妇”防晒霜解析！这些防晒贵在哪？',
    'video_tag_list': '',
    'content': '从左往右的品牌:\n科颜氏，雅顿橘灿，兰嘉丝汀，碧欧泉，娇兰，兰蔻，娇韵诗，黛珂，SKII，CPB'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/5668b98c8b58b0ba3a056ea5f70974e015edcc91_v1_ln',
    'video_id': '5927e4c1d2c8a566abf49d5b',
    'title': '内双、肿眼泡必看！！超详细眼妆教程',
    'video_tag_list': '日月晶采;日月晶采  Lunasol 魅惑净化巧克力四色眼影;眼妆每日打卡',
    'content': '有许多妹纸和我的眼睛差不多，不是完美的大双眼皮\n而是眼头内双、眼睑肿\n遇到这样的眼睛，可能不知道怎样去画一个日常眼妆\n这条视频就是手把手教和我一样眼睛的妹纸画一个眼妆\n用到的妆品中，强烈向大家安利lunasol\n日月晶采巧克力02号色眼影\n这盘眼影集珠光，哑光，卧蚕，眼线色于一体\n非常非常实用～\n#内双如何画眼妆[话题]##跟着视频画眼影[话题]##日常眼妆怎么画[话题]##眼妆每日打卡[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/24d8ca4c-01a18e0-81ba-758fc59f8938?sign=84b92af412d3554f2cc7c1e580b1b5e5&t=65fb06d4',
    'video_id': '5927eff07fc5b87f980d6224',
    'title': '夏天到了该多补水？可是喝水多又容易出眼袋！怎么破！',
    'video_tag_list': '',
    'content': '别人眼底是卧蚕，而我只有烦人的眼袋！是不是因为晚上睡前喝水太多导致的？为什么会有眼袋？有了眼袋该怎么办！跟着大大美酱告别眼袋科学变美！视频最后还有本期奖品价值299元的ysl唇釉送出哦，快来看看吧！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/4f3c7ccb-4ce2dd6-a5ba-99a3a2cd9929?sign=9c8f7bc5147c819115966cb0ffd02df4&t=65fb06d4',
    'video_id': '5927f1f37fc5b805990d6229',
    'title': '4款防晒喷雾评测！大公开！',
    'video_tag_list': 'RAFRA;防晒也能很清爽',
    'content': '#防晒也能很清爽[话题]##学生党平价防晒[话题]##我的彩妆测评[话题]#\n今天给大家带来的是4款防晒喷雾的评测\n👉RAFRA防晒喷雾\n产地：日本 容量：100g  RMB:89\n本身非常温和，在皮肤状态不好的时候也是可以使用的\n👉CIPE水晶防晒喷雾\n产地：韩国 容量：150ml  RMB：69左右\n这款的话也是娜扎同款，性价比也是非常的高，然后上脸也是比较清透的\n👉安耐晒防晒喷雾\n产地：日本 容量：60g RMB：149左右\n这款不用说，大家都知道，主打怎么晒都不怕，都晒不黑\n👉AJUSTE防晒喷雾\n产地：日本 容量：200g RMB：89左右\n200g大容量，还是防蚊的，不需要卸妆\nNO.1 细密程度\n结果：Rafra＞Ajuste＞安耐晒＞水晶\nNO.2 喷雾的味道\n水晶防晒喷雾：味道较冲，升级版空气清新剂\nRafra防晒喷雾：橙子清香味\n安耐晒防晒喷雾：花香味\nAjuste防晒喷雾：无色无味\nNO.3 清爽度\nRafra＞Ajuste＞水晶＞安耐晒\nNO.4防水防汗度\n几乎差不多~\nNO.5 保湿度\n水晶＞Rafra＞Ajuste＞安耐晒\nNO.6防晒度测试结果\n三个小时的话几乎看不出大差别~\n但是从防晒指数来说水晶是最差的\n水晶＜Rafra=安耐晒=Ajuste'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/17880283f69bd86be1da8f3c213334db2be3c595_r_ln',
    'video_id': '592824f37fc5b80cf591ab40',
    'title': '仅需2种材料！教你自制棉花糖冰激凌',
    'video_tag_list': '',
    'content': '女生们在夏天最爱吃的莫过于甜甜的冰激凌啦~其实你大可不必顶着烈日出门买冰激凌。\n今天喵酱就来教大家在家也能做的棉花糖口味的冰激凌，原材料居然只要两种，赶紧一起学起来吧！#视频教你生活小窍门[话题]##自制完美冰淇淋[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/7a660f29-21c3625-884c-fdbe06ea3be9_compress_L1',
    'video_id': '592838577fc5b861e391ab42',
    'title': '原来你是这样的卡姿兰大眼睛！',
    'video_tag_list': '如何画眼妆让眼睛变大;卡姿兰',
    'content': '这次是真点卡姿兰大眼睛啦！之前帮卡姿兰拍了一组照片，有幸得到他们首席化妆师帮我化妆，结果简直了，第一次知道我的睫毛居然能那么屌爆！此处绝对不是广告，我只是一个自来水，and我也好期待我拍的这组照片啊啊啊啊啊（记得把我修瘦一些……#如何画眼妆让眼睛变大[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkbfYUC0vqu5HaMXW7lRa15nc_T6_compress_L1',
    'video_id': '592867c9b46c5d129627813a',
    'title': '',
    'video_tag_list': '我和宠物的日常',
    'content': '日常 | 自从我家加菲迷上了ipad！哈哈哈哈哈哈哈哈哈哈\n————————标题分割线————————\n😳在小红书发现的几个猫游戏，我家加菲就独宠paw me（对，游戏就是这个名字）。每次给它玩 要是盯着它的话它就一脸傲娇，不理不睬，我一转身走开它自己就玩疯了🤣🤣🤣哪来那么傲娇！！😑😑有时候我手机玩游戏它也凑过来看🤷🏻\u200d♀️🤷🏻\u200d♀️🤷🏻\u200d♀️对方永远不知道他的队友是人还是只猫~🤦🏻\u200d♀️\n注：iOS11及以上的系统无法运行paw me（好像现在App Store也搜不到了）'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lszJIHOMDctj29aDEm0WBMa70XKy_compress_L1',
    'video_id': '5928bab8d2c8a504d6a5ada2',
    'title': '看完让我饭都吃不下的🎬',
    'video_tag_list': '异星觉醒',
    'content': '#异星觉醒[话题]#\n这部电影是我近年来看得最吓人的电影，全程20分钟左右还是比较温馨的，大家在感受着生命的奇迹，20分钟后就看到人类为之骄傲的卡尔文有多吓人，怪物开始不停地杀人～充满了血腥场面，胆小的我基本不敢正眼看～\n怪物有点像🐙，所以我最近不会吃🐙了太恶心，这部电影对于我冲击还是比较厉害的，我看完晚饭都吃不下，只能吃点素菜\n电影的结尾更是吓人，怪物来地球了，遇到一帮愚昧的人还去准备开门～有时好奇心会害死人也是有道理的……'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lm28z5F21GFzX2Bus_DxPL1_PCUF_compress_L1',
    'video_id': '5928c7c514de413a6fe25030',
    'title': '小红书四周岁生日在即，来为队长录生日祝福吧！🎊',
    'video_tag_list': '小红书生日快乐;小红书生日快乐',
    'content': '🎂#小红书生日快乐[话题]#🎉🎉🎉🎉\n6月6日是小红书的4岁生日了[喜欢]，很荣幸那么多的小红薯们陪伴我们一路成长，感谢大家一直以来对我们的喜欢、支持和信赖[得意]。\n趁着这个机会，大家一起来录一段视频，祝小红书生日快乐吧~（顺便给队长表个白吧～）[飞吻R]\n记得打上#小红书生日快乐[话题]#，这样队长才能看得到你们的祝福呢！[萌萌哒R]队长会选出一些幸运小红薯送福利哟！[赞R]\n爱你们哟~啾咪[喜欢]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fr1Ro7ri96_zKtl68HHtoh18Cfg0_compress_L1',
    'video_id': '5928c7cbd2c8a5436e476e7f',
    'title': '',
    'video_tag_list': '法国;旅行;带着小红书去旅行',
    'content': '埃菲尔铁塔闪灯\n\n#旅行[话题]#\n#带着小红书去旅行[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/ljjfa4MvPFm0aDeeBfCKD7SoBtBd_compress_L1',
    'video_id': '5928cff5d1d3b93945526718',
    'title': '#小红书生日祝福#第一次用视频表白！',
    'video_tag_list': '小红书生日快乐',
    'content': '#小红书生日快乐[话题]#\n听说6.6号小红书要过生日啦~所以用我的第一个视频笔记来表白小红书，笔芯💕\n玩小红书快两年了吧，现在什么东西都喜欢看看小红书上的笔记，化妆品啊，穿搭呀，旅游攻略呀等等，什么方面的笔记都有，真是棒！\n种草的东西在小红书上下单也是超方便，不用担心买到假货，价格也实惠，买东西hin放心~\n通过小红书这个平台呢，也认识了很多特别特别可爱的新朋友~\n同时呢，也非常非常感谢那些喜欢我，关注我的小红薯们！蟹蟹你们的支持！\n最后，祝小红书以后越来越好，走的越来越远！\n生日快乐呀！😁😁😁\n（第一次拍视频好害羞啊啊啊，长这么丑，我哪敢素颜出镜，本来想磨个皮，可是一用美拍，下巴就变这么尖了，我也没办法，摊手....T_T)\n发出去感觉要掉粉的节奏，但还是要表白小红书哈哈哈~[飞吻R] [飞吻R]\n北鼻，你们别喷我呀。嗯，我玻璃心[害羞R]'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lrF2UJmidX2qbyvr-yYPvP33k6X8_compress_L1',
    'video_id': '5928d38514de4158bbe25031',
    'title': '端午节除了吃粽子以外，我就爱吃这道面扇子！',
    'video_tag_list': '',
    'content': "★★★★★\n小圆食记\nMenu\n端午节是我们中华民族的传统节日，很多人都知道在端午节应该吃粽子，那么除了粽子还能吃些什么呢？\n甘肃省民勤县一带，端午节这天都蒸“面扇子”。就是最好的美味。今天小圆稍作改变来一道煎面扇！\n★★★★★\n创意指数\n面扇子\n▼\n面扇子\n·视频音乐·\nGeorge Winston - The Snowman's Music Box Dance\n·食材·\n面粉、鸡蛋、黄瓜、胡萝卜\n葱、胡椒粉、芝麻油、盐、清水\n1.黄瓜洗净切半\n2.一半切成条，一半切片备用\n3.胡萝卜洗净切片备用\n4.葱切段备用\n5.倒入200g面粉、1个鸡蛋、1茶匙盐、1茶匙胡椒粉、1茶匙盐\n6.加入适量清水拌匀\n7.调至粘稠后放入葱段拌匀\n8.取空碗倒入1勺辣椒粉、1勺生抽、1勺醋、1茶匙芝麻油拌匀\n9.热锅冷油，倒入面糊\n10.中火煎至面饼边缘变脆，翻面\n11.中火煎至面饼两面金黄后，撇油出锅\n12.面饼切半再等分切成三角形\n13.切去尖角作为面扇上部\n14.切去底部作为面扇底部\n15.摆成扇子造型后，淋上酱汁即可\n小贴士\n1.面糊倒入油锅时用面铲整理边缘，这样煎出来的会比较圆"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnSp-9aQ8vdQCZxapePiQtjWlzxK_compress_L1',
    'video_id': '5928dab2b46c5d4dfa747fef',
    'title': '小红书周年庆6666666666666',
    'video_tag_list': '小红书生日快乐',
    'content': '#小红书生日快乐[话题]#\n这个记性不好的又很多戏的玛丽也来祝贺小红书4岁生日快乐啦🎂\n已经来了小红书400多天，发了快200条笔记，认识了数不清的小美人儿，还买到了很多人一辈子都不会有那么多的化妆品（都是泪[害怕]\n这不仅仅是一个种草的平台，大家都很认真的分享生活，分享漂亮，分享欢乐。\n（那么走心不是我的风格啊！）\n希望每个女孩子的手机里都会有这一本小红书，这里有买不尽的好东西，种不尽的草，当然最关键的，还是有我啦[得意][得意][得意]\n视频后面循例有彩猫，我觉得我越来越丧心病狂了'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkVBtRRmXF4Ven_Gs5Dgk-FXFZCi_compress_L1',
    'video_id': '5928e4d3d2c8a50e5ea5ada0',
    'title': '小红书6.6生日快乐！送上一段视频祝福嘿嘿🎂❤️',
    'video_tag_list': '小红书生日快乐;LRENE工作室 一字露肩松紧带荷叶边衬衫',
    'content': '#小红书生日快乐[话题]#\n本来想6.6发的祝福视频 忍不住今天就发上来啦哈哈[讨厌]\n去年三月份下载的小红书app，至今已经400多天啦！以前觉得小红书就如同《百科全书》一般的存在，想知道什么好用、什么好吃、去哪儿玩好都会打开小红书搜一搜。\n也很喜欢在小红书上分享心得，每当自己的笔记能被小红薯们赞同一起讨论的时候，都有一种小小的成就感哈哈～也因为小红书认识到了许多可爱的女孩纸！从线上发展到线下的感觉太美好啦！[喜欢][喜欢][喜欢]\n最后祝小红书宝宝生日快乐！快高长大越来越棒！笔芯！😘🎂❤️❤️❤️\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsDO_pRJU8AgANvoYQZDXxSDQOJ3_compress_L1',
    'video_id': '5928f79ad2c8a5420fa5ada0',
    'title': '给大家献上一段夏日热舞 BangBangBang',
    'video_tag_list': '小红书萌娃大赛',
    'content': '可能是Bigbang的最小粉丝\n最后被爸爸玩哭了哈哈哈哈\nPS：最后一下子哭了的原因是因为时间到了饿了想喝奶，放下来喂奶之后马上就不哭了并不是不舒服什么的啦。手臂也没有磨红，是因为红色衣服光线的反射噢。😂谢谢大家关心！\n#爸爸带娃记[话题]##小红书萌娃大赛[话题]##萌娃最爱[话题]#\n@薯宝宝'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/ls3fN4ZH09UlKadWdYoef647ThuS_compress_L1',
    'video_id': '59291460b46c5d7347fa7ae9',
    'title': '毛球杀手！皮皮！',
    'video_tag_list': '猫奴必备猫玩具',
    'content': '超萌的皮皮～～～\n买了逗猫棒来逗她～\n今天是毛毛球的逗猫棒～\n哈哈哈\n皮皮一定是爱我的\n#猫奴必备猫玩具[话题]##我和宠物的日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/60d32ed0-454448f-89b7-8ca3516f68e1?sign=b4998130ea074a2099a10e442e1c3321&t=65fb06d4',
    'video_id': '5929185a7fc5b8552e1ae3e2',
    'title': '美味香辣蟹',
    'video_tag_list': '',
    'content': '#在家做海鲜[话题]#\n一道连葱姜都好吃到不舍得放过的香辣蟹，香、辣、鲜、脆，味道鲜美，营养丰富。唯一缺点，浪费米饭！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/266d36705c6f7ac3b63c64800ea69a0aada33ab2_r',
    'video_id': '59291c2e7fc5b869dd6e1e1f',
    'title': '端午节DIY：提神又驱蚊的艾叶香囊',
    'video_tag_list': '就爱DIY',
    'content': '端午节来了，来和喵酱一起做一个可爱小巧的传统艾草小香囊吧！ps：佩戴在身边，可以起到防暑驱蚊、提神醒脑的效果哟~ #就爱DIY[话题]# #视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lizZ7L0KPwzQMR0RcMhSHnpojQuH_compress_L1',
    'video_id': '592933b5d1d3b9698cd6900d',
    'title': 'Q弹的西米和蓝莓会摩擦出什么美味呢？',
    'video_tag_list': '',
    'content': '西米不可以直接水洗，要先用油和糖讲西米拌匀，用以隔离部分水，再用水慢慢浸润西米泡一会，使其慢慢把水吸收膨胀起来，再包粽子。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/9b7c58357205382b130bff5a728e52fbec43c389_v1_ln',
    'video_id': '59294ce4d1d3b93555d7d7e2',
    'title': '小红书生日快乐🤗',
    'video_tag_list': '小红书生日快乐',
    'content': '#小红书生日快乐[话题]#\n小红书6.6生日快乐，加入小红书半年时间，写了很多笔记，也种了无限的草，这是一个超级好的平台，感觉想知道什么时尚讯息都可以在这里查到！\n好吧，视频内容很干，有点害羞，其实只是想顺便来卖个萌[萌萌哒R]\n祝小红书年年有今日，岁岁有今朝[赞R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fj6cHE-OW2RYOtLzfsXaqImDlV36_compress_L1',
    'video_id': '592966bed1d3b906d2d7d7df',
    'title': 'Nia 来啦 Joy of your movement',
    'video_tag_list': '舞蹈表演视频',
    'content': 'Nia New moon session today❤️ it was so much fun dance with you! Keep Renewing and move your Steps of joy till next Tuesday 😋\n每周二，周四 等着你\n#舞蹈表演视频[话题]##小红书生日快乐[话题]##见人不如健身[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmcjfqbMPu6fIyzsW4-H_6EnvGEj_compress_L1',
    'video_id': '59297572d1d3b934d4d7d7de',
    'title': '近期心头好|miumiu玛丽珍鞋',
    'video_tag_list': '缪缪;换季必备鞋',
    'content': '夏天该告别一下黑白灰，尝试着给自己添置一点颜色啦！\nmiumiu这款玛丽珍鞋，我选了裸粉色，不俗，很大方好看。\n不偏码。不过皮质偏硬，又加上是长款，比较适合长脚或者正常的脚，胖的话可能挤不进去。\n穿脱方便，不仅很配各种夏天的小裙子，牛仔裤通勤打扮也没有问题。\n另外，这防尘袋也太美了点！桃粉色，miumiu真的是超级少女心。\n价格：5800\n#鞋控の日常[话题]##一线鞋星[话题]##上班穿什么鞋[话题]##换季必备鞋[话题]##你晒太阳我晒鞋[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ac0c909cddcd3e2b323619ca8c7c0e00fbe975c4_r_ln',
    'video_id': '5929781f7fc5b838786e1e1b',
    'title': '不放糖也很美味的健康水晶粽，在宿舍不开火也能做',
    'video_tag_list': '',
    'content': '在宿舍不开火也可以做粽子吃吗？不放糖也可以做出香甜美味的水晶粽吗？叔这次脑洞大开教你们一个改良版粽子做法，简单、健康、高颜值还很美味。所有食材和工具都能轻松在网上买到，一起过个快乐有粽子吃的端午节吧。\n食材：绿西米适量、台农芒果一颗、椰青一个\n辅料：粽叶、棉绳、橄榄油\n#粽子大作战[话题]##甜粽党[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lmeriL2pHStyC6YFwbzHWxLbPu-d_compress_L1',
    'video_id': '59298ca8d1d3b978bfd7d7de',
    'title': '短发夏季头发蓬松心得分享#Rita聊天室#头发蓬松',
    'video_tag_list': '拯救头发油腻的好东西;Tangle Angel',
    'content': '嘻嘻来分享视频啦～\n果然头发洗一下好很多 昨天还要好一点 今天已经睡过一觉起来没有你们蓬松啦，就来教大家如果夏天头发蓬松不踏～\n因为真的夏天头皮容易烤焦头发就很容易变踏\n梳子是：Tangle Tamer Ultra\n洗发水是： Lee Stafford （Big Fat Healthy Hair）\n烫完头发以后洗过就自然很多啦 ～～ 本来还伤心了两天觉得头发被剪坏了哈哈\n希望对你们有帮助啦：）还有就是吹头发时候不要太热风，会加速头皮出油的热风，所以还是慢慢吹 风速小一点温和一些～\n#拯救头发油腻的好东西[话题]##我是短发控[话题]##保持短发造型的好东西[话题]##我的护发秘籍[话题]#\n记得点赞么么哒😘😘😘'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnDNncoiU24QNGm_Xa9eGyb2xy7N',
    'video_id': '5929a59b14de410bfa17daaf',
    'title': '#半丸子头教程分享第二弹#这次再不会我要去哭一哭系列',
    'video_tag_list': '',
    'content': '😄好久没有录视频\n之前的半丸子头教程\n大家还喜欢嘛？\n超多妹子给我点赞鼓掌叫好\n在此由衷感谢大家！😆\n但是还是有些妹子没有办法梳\n原因有以下几点\n1:发量问题\n2:头发长短问题\n3:我的教法问题（一定是我的方法没有更全面更深入😅）\n所以这次这个方法.\n应该百试百灵！一见倾心…🌚岔开话题了…\n总之！再不会的话…我要去哭一哭系列了！\n哈哈！由于感冒咳嗽\n声音略磁性…\n还请大家多多包涵\n谢谢大家！'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/FqeVVrdygITPkufNHflcF0CT3T2-_compress_L1',
    'video_id': '592a236eb46c5d6774849853',
    'title': '家有小白猫🐱领养代替购买',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '我家猫咪已经养了7年多，是我大三的时候从流浪动物所领养回来的，那时候它才3个月大。\n它一直是很谨慎的性格，到新家总要躲起来两三天去适应。它是那种安安静静的陪伴型，不黏人但很懂我，会在我不高兴的时候过来陪陪我，在我出差回来之后喵喵叫问我去哪了。\n其实现在很多流浪动物都很好看，性格也很好，不一定养宠物非要追求品种，和谈恋爱一样，只要看对眼了就是一辈子的家人。\n#我和宠物的日常[话题]##我家宠物最萌的瞬间[话题]##家有小主[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhZgtXTvEFAdH_ShfOqVkuPejTIo_compress_L1',
    'video_id': '592a25b5b46c5d6b72849855',
    'title': '猫咪在睡午觉✨',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '#我家宠物最萌的瞬间[话题]##我和宠物的日常[话题]#\n在咖啡店门口一只真正睡午觉的🐈\n这个睡姿真惹人喜爱'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lmnnTc7pD1gchX7ZQNe17Q8LoqiP_compress_L1',
    'video_id': '592a2f70b46c5d07e7fa7aeb',
    'title': '晒后修复期的一些可选产品',
    'video_tag_list': '高田贤三;雪花秀;希思黎;馥蕾诗;雪花秀 Sulwhasoo 清润舒缓面膜;希思黎 sisley 花香保湿面膜;馥蕾诗 FRESH 红茶抗皱紧致修护面膜;敏感肌适用的面膜',
    'content': '#晒后修复靠什么？[话题]#\n晒后皮肤会非常敏感，所以选择全步骤产品都要相对温和。\n[色色R]\n1.Kenzo Lotus洁面泡泡\n非常温和的一款洁面泡泡 泡泡十分绵密 清洁力适中 洗掉后肤感很好 会有微微水润的感觉 不干 算是小众洁面了\n[得意R]\n2.雪花秀清润舒缓面膜\n啫喱质地 涂在脸上会有冰爽感 面部舒缓效果还不错 也有一定补水功能 镇静肌肤\n\n[飞吻R]\n3.Sisley花香补水面膜\n啫喱质地 淡淡花香味道很好 主打速效3分钟补水功能 涂完面部非常水润 补水效果好 价格稍高\n\n[偷笑R]\n4.Fresh红茶紧致修护面膜\n土豆泥质地 膏体细腻冰凉 涂开面部有冰爽感 镇静肌肤效果不错 紧致功能暂未感受到\n\n[吧唧R]po主肤质情况：混合，曾痘肌，广东\n#美白面膜大作战[话题]##拯救敏感肌[话题]##敏感肌适用的面膜[话题]##敏感肌洁面利器[话题]##我的护肤日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/87b44b35-68b502e-ad1a-98bb9f4be8db?sign=89764e3a60af38201fba450a521b0913&t=65fb06d4',
    'video_id': '592a4edd7fc5b875566e1e18',
    'title': '【本周萌娃】只有亲爸才这么带娃',
    'video_tag_list': '爸爸带娃记',
    'content': '哈喽艾瑞巴蒂！来认识一下今天出镜的萌娃轰轰和她的爹地轰爸~来自话题#爸爸带娃记[话题]#\n轰的妈咪 @kiki🍜kismine 说：“轰爸是个操心的爸爸。轰一有点什么问题，他就到处问当了妈妈的朋友，以至于有个妈妈直接把他拉进了妈妈群。（笑）轰轰也是个爱笑的宝宝，冲着陌生人也笑，自己跟自己玩儿都能莫名咯咯笑。带娃的生活还蛮乐在其中的。”\n戳 @kiki🍜kismine 的主页，可以看到更多轰轰的日常哟~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FnxE1AuB9pF4b6gLOg5733lwzkV1_compress_L1',
    'video_id': '592a554014de41217b810251',
    'title': '祝小红书生日快乐🎂🎂🎂🎂🎂，',
    'video_tag_list': '小红书生日快乐;天津',
    'content': '#小红书生日快乐[话题]#\n认识小红书一年多了，在这里开阔了眼界，找到了自己的新天地，会一直陪小红书走下去哦😁😁😁😁\n#亲子游攻略[话题]#\n宝宝在家也可以游泳哈，省的去外面了。外面的水质不敢保证，在家里，想怎么游就怎么游，就是浴缸有点浅就是😂\n宝宝第一天还不怎么适应，第二天完全自己游咯，胆子大了。\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpl993y9shWpi2QdHnGtScGZxtcC_compress_L1',
    'video_id': '592a7149d2c8a527d4580a1f',
    'title': '萌萌的噼里啪啦玩具书',
    'video_tag_list': '视频推荐玩具',
    'content': '宝宝5个月大的时候\n除了黑白卡还有那些基础卡片外\n想给她买点书培养培养兴趣\n然后就被小红书种草了\n这款噼里啪啦玩具书很有意思\n买来给宝宝看的，她看着一半不看了\n我却停不下来[笑哭R][笑哭R]\n一口气全看完了\n真的很好看耶\n做工精细，配色也很美丽\n现在宝宝6个月大了，开始对它们感兴趣\n看着看着就笑，也有特别喜欢的那一页\n还会想吃\n虽然现在对她来说还是玩具\n但毕竟看书的兴趣是从小培养的嘛[叹气R]\n真心喜欢这款书哦\n#宝宝育儿书选择[话题]##有料立体书[话题]##新款宝宝玩具[话题]#\n#视频推荐玩具[话题]##视频绘本打卡[话题]#\n#我的私藏书单[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqaTyuSIiOefNKxMoLbKaFFTkRMl_compress_L1',
    'video_id': '592a731614de417776810249',
    'title': '自制抹茶冰淇淋，无需中途搅拌，完全无冰渣。',
    'video_tag_list': '夏天就要吃冰',
    'content': '#夏天就要吃冰[话题]#抹茶可以不放，滴两滴香草精，或者换成可可粉就是巧克力味了。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhZJddeKPD5A0CpsDRCgC57v7Jtv_compress_L1',
    'video_id': '592a73dbb46c5d4615849854',
    'title': '嗨玩芽庄-就这么霸气你敢吃吗',
    'video_tag_list': '',
    'content': '芽庄海边的一家烧烤自助，门口转着烤鳄鱼🐊，还有一些烤海鲜，人均60rmb，不过我只是路过……给你们看个新鲜\n\n#最爱旅行地[话题]#\n#带着小红书去旅行[话题]#\n#我的小众旅行攻略[话题]#\n#旅行必逛夜市[话题]#\n#旅行必吃的小吃打卡[话题]#\n#东南亚旅行攻略[话题]#\n#吃货小分队[话题]#\n#漂洋过海来吃你[话题]#\n#越南游攻略[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhdKXbPHTkkEUV1-huBZtPvRHuSa_compress_L1',
    'video_id': '592a7af3d1d3b948b9a7ea1e',
    'title': '4⃣️岁的小红书生日快乐🎉',
    'video_tag_list': '小红书生日快乐',
    'content': '嗨皮啵丝带 土 友 ～\n祝你生日快乐～\n赛腻粗卡哈密达～\n#小红书生日快乐[话题]#\n一年前开始接触小红书，慢慢分享自己的心得和妆容，也遇到了许多志同道合的人，是一种幸运也是一种学习👍\n最感谢的还是一直支持我的小伙伴们！\n❤️'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/37170c846c7d099925c24851c3af4a0989a98b5c_r_ln',
    'video_id': '592a7bdfd2c8a54629ad6397',
    'title': '少女心| mk mercer 粉白拼色',
    'video_tag_list': 'Michael Kors;MK明星同款包',
    'content': '这只包是我买来送给闺蜜的毕业礼物，不浮夸不low、实用好看，我觉得是送女孩子毕业礼物的好选择。\n这款mercer最出名的就是杨幂的墨绿色啦，不过我觉得太容易撞包，而这只粉白拼色是新颜色，我觉得一样很好看，目前我还没在路上看过别人背哟。\n❤️小号尺寸也还蛮好装东西的，不过只有中间是有拉链，两侧建议放杂物了，不然不是特别安全。大号的话真的很大，比较适合通勤装的时候搭配。\n❤️可以手拎也可以背肩带，但我觉得这个肩带真的好长！看起来有点拖沓，较小的女生适合手拎。\n❤️荔枝皮，蛮耐脏，不过也要看是什么颜色了。如果比较随意粗心的女生更建议选深色系。浅色系还是需要比较好的保护。\n❤️价格1800，美国入。美国和韩国应该比较便宜，香港我之前看到是3000港币。\n#MK明星同款包[话题]##夏日包包[话题]##出街最爱的包包[话题]##我的包从没撞过款[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/d233165f720e10274ab3ac72a092f46da850d329_r',
    'video_id': '592a99cfd1d3b927f6f0a983',
    'title': '瘦腿减脂不可忽视的肌肉筋膜放松！泡沫轴肌肉放松动作分享～',
    'video_tag_list': '肌肉拉伸教程',
    'content': '#见人不如健身[话题]##健身是把整容刀[话题]##必须要安利的健身动作[话题]##泡沫轴使用教程[话题]##全身减脂教学视频[话题]##高效瘦腿攻略[话题]##肌肉拉伸教程[话题]##10斤减肥小目标[话题]##健身靠装备[话题]##好看好穿健身裤[话题]#\n健身不能只练不吃！\n训练不能光练不放松！\n肌肉需要我们先简单粗暴再温柔相待[害羞R][害羞R][害羞R]\n特别是腿臀部大肌肉、练完一定一定要拉伸和放松\n我们的肌纤维是有弹性的、训练的时候肌纤维收缩变短、训练后需要我们帮它拉回到原来的长度它才能变得有弹性并且好看～不然肌肉长期处于紧张和变短的状态、第一是肌肉形态不好看、看着僵硬、第二是容易受伤、肌肉过于紧张会导致关节偏离中立位从而压力加大导致受伤、关节炎症等～\n肌筋膜如果紧张不光是有可能会有以上的问题、还会导致力量训练的时候找不到发力感、充血不敏感、阻碍血液循环等～\n特别是下肢、肌肉面积大，长期训练或者不训练都会僵硬、血液循环不畅、也会很大程度上影响你的减脂或者增肌效果！\n有的时候你的腿一直不瘦不是你练得不够、而是你放松得不够[叹气R][叹气R][叹气R][叹气R]\n所以泡沫轴肌筋膜放松也可以放在训练前、对需要训练的目标肌肉进行几分钟的松解、松完再去举铁、发力感会特别棒[赞R][赞R][赞R][赞R][赞R]\n不管你是爱健身爱举铁的猛妹子还是每天久坐经常肩颈不适的上班族菇凉、或者你是常常腰酸背痛的全职宝妈… 都很有必要拥有一个筋膜放松泡沫轴噢😯\n举铁后、徒步后、爬山后、跑步后、骑行后（总之就是各种有氧无氧运动后）都可以拿出泡沫轴全身滚一遍！\n每个部位3-5分钟、坚持一段时间你会发现自己明显没那么僵硬、也能做个软妹子啦！举铁的时候肌肉泵感好强好强的[得意R][得意R][得意R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljVQ9dDvl6PsRS4F47grLnnqznwH_compress_L1',
    'video_id': '592a9aded1d3b90eacf0a989',
    'title': '🎊❤️小红书4周岁生日快乐❤️🎊',
    'video_tag_list': '小红书生日快乐',
    'content': '哈哈请允许我带上我家豆芽一起卖萌祝小红书生日快乐，另一只拉布拉多太重了抱不动………\n从15年开始用小红书，到现在基本天天都在用哈哈哈哈，一直在种草跟被种草的道路上，而且用起来好方便，想找什么都会来小红书搜一搜\n另外😳还认识了很多有趣可爱美美的小仙女，我超喜欢大美女哈哈哈哈\nAnyway、祝小红书宝宝\n🌟HAPPY BIRTHDAT🌟越来越棒！\n#小红书生日快乐[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llHW2fbZblP7dw-YoHBWt2yLBMYT_compress_L1',
    'video_id': '592aa74514de4165f2564df6',
    'title': '拔草古北粒粒堡——12月龄里的宝贝们免费玩～',
    'video_tag_list': '宝宝日常穿搭指南',
    'content': '#小红书萌娃大赛[话题]#\n#宝宝日常穿搭指南[话题]#\n地点：粒粒堡亲子餐厅上海古北店\n人物：犯困的小红豆\n12个月龄里的宝宝是免费玩两小时的哦～超时30rmb/小时～\n里面的牛肉披萨和薯条推荐哦～带宝宝去是个不错的地方～\n办1岁生日宴应该会考虑这里～蛮赞的～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljLKRvsH8L9D_K4PtVq3N5RKPu3__compress_L1',
    'video_id': '592ad83ad2c8a542164a465f',
    'title': '猫咪怎么洗澡，知识帖！',
    'video_tag_list': '我和宠物的日常',
    'content': '没想到这么乖吧，哈哈哈哈哈哈😄，可能我养了一只假猫，乖的不像话😂😂😂😂😂\n首先要准备好洗澡的东西！水温要42度，准备浴液并且稀释好，准备吸水毛巾，还有吹水机也要调好状态！\n下面步骤哦：\n第一步，剪指甲，避免剪出血！\n第二步，掏耳朵，用棉签蘸上专业的洗耳液，清洁耳朵，力度要轻！\n第三步，擦眼镜，推荐用化妆棉蘸上隐形眼镜护理液沾湿眼眶，再轻轻擦！\n第三步，打湿猫咪毛发，水温要正好，手法要轻，慢慢打湿，并且轻微按摩，直至全部湿透。\n第四步，涂浴液，看你们用哪几种浴液了，一般也就一种吧（我要用三四种，哈哈哈哈），涂上稀释好的浴液，轻柔按摩起泡，三分钟左右，记住要顺着毛发的方向按摩！\n第五步，冲洗，先冲干净，大约五分钟，然后再泡一下，彻底洗干净，不能有浴液泡沫残留，要不然毛吹的再好也是趴趴的！\n第五步，吸水干斤吸掉水分，然后大致擦干就可以吹毛了。\n第六步，吹水机吹干，要控制好温度还有风力，过热过猛猫都不会舒服。还有就是吹头和毛发的距离，适当调控，同时吹的方向记住不能倒着吹太伤毛，一定要顺着吹，才能吹出纹理的感觉！\n第七步，吹干之后，要注意回潮情况，再次烘干，就是微风慢慢烘干，直至干透！\n就是这些啦，当然这些前提是猫咪很配合的情况下，不配合的话还是去设备及环境好一点的宠物店，请专业的宠物美容师帮助清洗！#我和宠物的日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lisIEDGh_b000dcO4rbZRmpImeib_compress_L1',
    'video_id': '592add3eb46c5d6dd614d021',
    'title': '欢乐颂里不同阶层应该怎么理财！精辟',
    'video_tag_list': '你是欢乐颂里的谁;天津',
    'content': '欢乐颂已经上映了一段时间了，简单而贴近大城市真实生活的剧情，反映出了事业与爱情之间的诸多问题。剧中五个新时代女性来着不同的背景，反映了不同的生活观念和价值观念，同时也代表了社会不同阶级的生活状况。今天，小编带您聊聊，根据所处不同的经济阶段，新一代小仙女们应该如何理财呢？\n>>>>邱莹莹\n普通应届毕业生\n参考因素：\n年龄：24岁\n工作：咖啡店员工\n收入：4000元/月+绩效\n阶级：低收入人群\n财富指数：★★☆☆☆\n邱莹莹本身没有过硬的背景和好文凭，各方面条件都很一般，但是自带一往无前的勇气以及赚钱的欲望，毕业一年已经能够独立自主，承担自己的生活花销。在未来的日子里，可以相信她凭借自己的努力，邱莹莹能够在每月绩效上咸鱼翻身！\n投资建议：职场新人一定要养成记账的好习惯，并强迫自己好好储蓄，有了一定存款之后，可以投入一些收益较低但稳定收益的货币基金型理财，存取更加灵活。\n关关\n参考因素：\n年龄：23岁\n工作：证券公司正式员工\n收入：7000-10000元/月+年终奖\n阶级：小康\n财富指数：★★★☆☆\n同为刚入社会的小新人，关关家境良好，父母都是国企领导，在这种家庭中可以很容易地过上有编制的小康生活，然而不安分的心使得她来到上海拼搏。在上一部中和邱莹莹一样都是低收入群体，但转正之后收入立马得到了提高，身处金融行业大牌券商的她，又在努力攻读MBA，事业处于上升期，但在这一阶段中，理财时间较少，不可能实时关注自己的投资。\n投资建议：外表看就非常保守的关关，不太适合去选择高风险的高收益产品，可以使用基金定投等方式进行理财，这也非常适合忙碌的工薪一族，而随着财富的逐渐积累，可以开始关注一些风险较高但收益同样可观的高收益产品。\n樊胜美\n>>>>\n职场白骨精\n参考因素：\n年龄：31岁\n工作：高级理财顾问\n收入：8000-15000元/月+绩效\n阶级：中产阶级下层\n财富指数：★★☆☆☆\n第一步作为外企资深HR的樊胜美第二部果断转型成为了一名高级理财顾问，学霸兼具高情商的樊姐转行后事业一定迎来新高峰。樊姐对于高品质生活的追求以及家庭的索取让她一直挣扎在贫困线上，在缺乏足够的理财意识情况下很可能会带来严重的后果。幸运的是，她转行做理财顾问之后这一方面的意识将得到加强，相信她在未来一定会有更好的“财缘”。\n投资建议：开源节流是樊胜美必须做到的一件重要事项，同时家庭责任的明确也能够减轻身上的负担。樊胜美的工作环境以及自身条件可以开始学习一些技术性的理财知识，做好资产分配，逐渐学习一些高收益的投资产品（比如外汇、股票），这些工具可以更快的提高她的投资知识，更好的辅助她与客户沟通，同时加快她翻身的速度！\n安迪\n参考因素：\n年龄：32岁\n工作：上市公司CFO\n收入：100,000-150,000元/月+分红\n阶级：富人\n财富指数：★★★★★\n安迪简直就是大都市金领的典型代表，良好的学历文凭，拥有过人的智商以及情商，出色的商业敏感度。投行背景的安迪对数字极其敏感，对金融产品也十分熟悉。\n投资建议：安迪优秀的个人能力可以使她合理的追求更高收益的产品。同时根据自己的实际情况，可以对自身资产进行有效调配，各类保本型、稳健型理财也可划入自身的理财规划当中。\n曲筱筱\n>>>>\n24K真·富二代\n参考因素：\n年龄：25岁\n工作：民营企业总经理\n收入：100,000-500,000元（营运利润）\n阶级：富人\n财富指数：★★★★★\n富二代，家庭资产10亿级，200万创业资金\n曲筱绡是一个令人羡慕的富二代，第一部的稳准狠的商业作风为她大赚一笔。在第二部的剧情中，民营企业的痛点—资金周转不灵，这一部中可能她要更多的依靠自己了。但凭借自身的优势—人脉、能力、经验，东山再起想必也是指日可待。\n投资建议：曲妖精家族资产丰厚，是标准的高净值人士，从运营风险上来看，应当增加海外资产的配置。此外，自身资产的保值增值也是非常重要的，私募、信托等投资公司非常适合曲筱绡的实际情况，同时，还应当关注流动性方面的要求，尽量选择变现能力高且快的投资品种以确保资金的正常周转。\n不难发现，从职场小白到资产丰厚的标准高净值人士，都是需要规划投资理财生涯。当然，以上分析建议绝不是标准答案，投资理财还需专业机构量身提供个性化服务更科学。\n#欢乐颂2[话题]##你是欢乐颂里的谁[话题]##小红书生日快乐[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkowmaAQu_Q6R1ZxKHOXGWs2KpkK_compress_L1',
    'video_id': '592af24bd1d3b91b2da7ea2b',
    'title': '猫奴必入之PAUL&JOE 15周年限量猫咪彩妆礼盒试色',
    'video_tag_list': 'PAUL & JOE;春夏最爱的清新口红',
    'content': '这款是我在淘宝新入的彩妆礼盒，超级超级美，如果不是为了做试色，根本舍不得用…\n这组PAUL&JOE 15周年猫咪彩妆组，经典的西洋菊外纸盒包覆，单是开盒就有很明显的经典PAUL&JOE 香氛，然后里面就只有放了2个东西，一个是化妆箱，一个则是化妆包。\n单是那盒收纳箱，就真的有点过分美，单是摆在化妆台上都是一个很美好的装饰品。[飞吻R]\n还有一个猫咪造型的化妆包，非棉质而是尼龙材质，清洁上还算方便，整个化妆包就是以一种萌猫的脸去设计，还有两隻可爱的猫耳朵。\n收纳箱里面所含的一支猫猫唇膏、猫咪眼影蜡笔、猫咪彩妆盒，特别要提的是，那收纳盒的抽屉拉把，还是作成金色猫猫脸，萌萌的很可爱。\n这次的PAUL&JOE 15周年猫咪彩妆组一个大重点就是这支猫咪口红，除了是经典款的猫咪头造型外，这一次还戴上了帽子，是一种帅气的可爱。（这个造型其实在2012年春妆就已经出现过了，这一次可以说是再一次復刻。） 外面的口红盒也都是插画的猫咪图腾，里面转头也是猫咪的样子，不过同样的，这支猫咪口红，你真要从正面来擦也实在很捨不得，大多还是只能从它的后脑勺开始使用。\n这支猫咪唇膏是比较温润的珊瑚蜜桃橘色，刚好是春夏推出，也是比较适合春夏的活力色调，反正切记，从它的后脑勺开始擦，才不会毁坏掉整个唇膏的本体。\n猫咪蜡笔眼彩共有6色，全都是做成猫咪静坐的样子。共有6个顏色，包括天空蓝、大地咖啡色、莓果红、香槟金、纯粹黑以及甜美粉。（就是不太好上色啊…[扶墙R]）\n纯铁制的眼影盒中，一次可以放三颗猫猫蜡笔眼影，里面附有一支双头PAUL&JOE眼影棒可以使用。\n#我的彩妆测评[话题]##最适合春夏的眼影[话题]##跟着视频画眼影[话题]##创意彩妆试色[话题]##唇妆试色报告[话题]##唇妆试色报告[话题]##我的口红不挑皮[话题]##最显白的口红[话题]##春夏最爱的清新口红[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/b01de495b9976d2b17973f19f9c5501a25b4012d_v1_ln',
    'video_id': '592af83514de4176bfc46318',
    'title': '周末教舞时间，超有活力的舞蹈good time',
    'video_tag_list': '',
    'content': '赞够多才有动力出分解啊，每周末行程都是满满的，明天早上要拍外景了，lui～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/2e47ef56cabcfe80ef7445c90295954f13be9270_r_ln',
    'video_id': '592b74f17fc5b83655a729cb',
    'title': '3分钟营养早餐「港式火腿西多士」',
    'video_tag_list': '',
    'content': '休息日的清晨，没什么比一份香喷喷热乎乎的早餐更能增添元气啦！\n记得蛋液里要加一点盐！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhZLmbNkgPLEJnW9xdyRJpwOhPmL_compress_L1',
    'video_id': '592b8cf3d2c8a50c22ad639e',
    'title': '堆积的软布包、购物袋如何整理？',
    'video_tag_list': '',
    'content': '这期结尾补充了超实用的“衣柜整理技巧”，告诉你如何改善柜门总摩擦衣服，以及超快速断舍离衣物的方法，你们在问的鞋子、厨卫收纳后续都会有，别着急一个个来哦[萌萌哒R]\n#衣物收纳小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkcwuPodjOyVc_0cWcQzE5STUP-e_compress_L1',
    'video_id': '592bb9f8d1d3b90b78f0a987',
    'title': '祝小红书6.6生日快乐！',
    'video_tag_list': '小红书生日快乐',
    'content': '马上要到六月六号小红书的生日啦！祝小红书4周岁生日快乐～越来越好，越来越红！\n希望以后我们多多互动，一起分享美好的生活。[飞吻R]#小红书生日快乐[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/FiXfnFifYcQ-QOLElCtAsp0wYpBP?sign=f7ac34cd189867c83bde39c655e4d806&t=65fb06d4',
    'video_id': '592be970d1d3b91bdbf0a985',
    'title': '端午节快乐～',
    'video_tag_list': '端午小长假',
    'content': '大家都撸猫撸狗，我来撸只大公鸡！哈哈哈！看它享受的样子哟[偷笑R]\n#端午小长假[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/f944d140362d4271c3a8505a4b4cec789d1ab368_r_ln',
    'video_id': '592bf4d0d2c8a52dc14a4660',
    'title': '满满少女心的草莓冻🍓',
    'video_tag_list': '最拿手的草莓食谱',
    'content': 'cr：迷迭香\n来自一个美食精品原创博主，周一到周五每天一天美食原创视频，2分钟就可学会。\n材料：4个草莓🍓、冷水、吉利丁片5g、热水、蜂蜜5g\n@生活薯 #水果的有趣吃法[话题]##最拿手的草莓食谱[话题]##大爱水果季[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgPt9uLKXkzRLaZeHWp-mk-NoN-I_compress_L1',
    'video_id': '592bf555b46c5d742914d026',
    'title': '🐨超级撞大运——活蹦乱跳的考拉🐨',
    'video_tag_list': '',
    'content': '🐨这两天都在🌊大洋路（The Great Ocean Road）耍，路上的景点之一大奥特维森林公园（Great Otway Nation Park）路边的🌲上就能看见野生考拉。结果大发我撞大运，不仅看见没在睡的，还见到了迷茫过马路的。哈哈哈哈哈，真的太可爱了。我刚发现它救援组织就来了，效率超高。好可爱哦，想抱抱它。[飞吻R][飞吻R][飞吻R]'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/FhCqnwp5cAWJGYRb9eTMI8EB1hOg_compress_L1',
    'video_id': '592c03edb46c5d22879e44fb',
    'title': '仙气十足的日本最新夜光贝壳美甲🐚不要太仙喔～',
    'video_tag_list': '亮片美甲惹人爱',
    'content': '超梦幻的款式诶，看得我心花怒放[色色R]～超级仙的款式～\n由于要体现夜光效果所以拍摄光线很暗哦～实物超美的！[赞R]\n还是我最爱的美甲店！现在去就能做！广州哦！[得意R]\n🐚🐚🐚\n店铺名：The Grand Nail\n地址就在马场西门旁边～\n她家是需要预约的，wx或者电话都可以～\n她家最近还从日本带了好多贴纸和饰品，还有新的果冻色和猫眼色！都炒鸡正！！\n过几天准备去体验一把棕色睫毛～听说接了之后看起来会很温柔哦～\n正好端午来做一发～夏天就要美美哒～\n#少女心美甲[话题]##亮片美甲惹人爱[话题]##春夏美甲配色[话题]##端午小长假[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsUySquCYCYOYAW2cEx3Ywp_Qxqc_compress_L1',
    'video_id': '592c05df14de4139d4564e08',
    'title': '我是文化薯啦哈哈哈哈—高兴就唱老黄的歌哈哈哈—r13短裤神了',
    'video_tag_list': '',
    'content': '今天一看！\n我去！\n我是文化薯了！\n好有文化的赶脚啊！\n哈哈哈哈哈哈哈！\n我爱ed sheeran哦！老黄啊！每张专辑必买——长的跟大黄🐻一样可爱❤\n裤子是r13，前面做旧破洞，后面却很长。一点不会走光。腿长瞬间一米八！\n我也爱小红书❤\n我要吐槽一下！我的血型是o没错！可是我也太招蚊子了！真的！我简直是每到一个地方的蚊子测试仪，但凡有蚊子，我就会第一个被咬！[扶墙R][扶墙R][扶墙R][扶墙R][扶墙R][扶墙R]真的是！啊啊啊啊啊啊啊！这么多年来都这样！夏天真是怕了蚊子啊！[扶墙R][扶墙R][扶墙R][扶墙R]'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/ls21JFIwp31KCsRi0k2Kr42yhLQs_compress_L1',
    'video_id': '592c220814de4142db564dee',
    'title': '看着我的小螃蟹',
    'video_tag_list': '',
    'content': '今天在东营抓到的小朋友，很活泼，爱举着钳子哈哈哈'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FlHzaw8gKxh-He5v6pGerhJWYFK0_compress_L1',
    'video_id': '592c253bd2c8a533454a465e',
    'title': '夜晚的小美丽 干了这杯“银河”',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lvndtegbuqER6dp5tEZwba-GsXwN_compress_L1',
    'video_id': '592c2f61d1d3b96eb4f0a987',
    'title': 'TRANSINO 敏感皮也能安心美白',
    'video_tag_list': '',
    'content': '谁说transino只有内服的美白丸出名？他们的敏感皮美白产品也很诱人啊！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lt25h_N5W0jpBCTDVO6nSjPsuRuS',
    'video_id': '592c3039b46c5d1e6b9e44fa',
    'title': '卷发教程 对 就是你们等很久的 快给我小心❤️',
    'video_tag_list': '',
    'content': '之前说好的卷发教程 来了 你们快鼓励我一下 给我小心心和收藏 喜欢妆容的我也会发妆面教程的\n卷发棒 淘宝搜 反正我这个是随便买的 50块\n然后里面有说技法 就是最前面的一定要外卷 然后一外一内的卷 才会自然好看\n卷发之前要涂抹精油哦 我白天洗头后用了好多护发素和精油 精油就是欧莱雅那个 很便宜滴 我有朋友和我说牛油果当发膜效果特别好 那我那么爱吃牛油果 怎么舍得用它敷头发呢😊'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltjloWzcOQnP4qFmE-pevt_vcJ9Z',
    'video_id': '592c3e5cd2c8a574d0ad6394',
    'title': '绘本看世界‖长大以后想做什么？',
    'video_tag_list': '周岁宝宝可读的绘本',
    'content': '看到这个话题#在绘本里看世界 ，又忍不住想参加@薯宝宝\n宝宝，么么哒～\n实际上这本绘本大概要两岁左右的宝宝才能够熟练掌握的吧，我这囤货的本领从自己身上又蔓延到小瓜子身上啦，嘤嘤嘤\n这本书最大的特别就是集触觉视觉听觉于一体，不仅可以了解职业以及职业内容，还可以自己动手学习到每个职业装，每套衣服还配以相关的声音。\n比如，我给男娃娃配了一套警服，在右边就可以找到警察的枪声。\n整本书的知识点由点到面，很详备，等小瓜子同学开始有认知能力以后再使用啦～\n#一起读绘本\n#视频绘本打卡\n#周岁宝宝可读的绘本'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llbVCKZpPxql7rzN62Ano8ezgAnk_compress_L1',
    'video_id': '592c406014de411868c4631f',
    'title': '爵士舞good time外景拍摄剪辑完成！',
    'video_tag_list': '',
    'content': '生命不息，舞动不止！\n本职职业之外的业余爱好，\n但是也要做出成绩！\n无论何时也不忘宣传家乡！\n望你们的生活不止眼前的苟且，还有诗远方！\n跟这群志同道合的人在一起，才是青春张扬！\n不论何年龄段，也要享受每一段人生精彩！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luT4kmETMr2jRcqtrAsZZmu-PxDm_compress_L1',
    'video_id': '592cd9cdd2c8a513abad638e',
    'title': '指尖陀螺，传说中的减压神器，我用来打牌时招唤大怪～',
    'video_tag_list': '视频推荐玩具',
    'content': '#端午小长假[话题]#几天被安利的，然后我就在地铁上玩high了😂\n我突然get到这个点了，然而路人应该把我当自闭症少女，远远🉐️观望我，好吧，深井冰的世界你们不懂😿\n指尖陀螺号称减压神器，也就号称啦，就是不自觉的拿在手里想转转，这个稳定性一般，要换指估计不可能，马上新货要到手了，嘿嘿[害羞R]\n后来我们去打牌，我就把这个放在桌上转啊转，真的有点招大小怪，以前打牌与怪无缘😂\n话说有人说这是老头子玩的，我不服！[扶墙R]\n#家有玩具大推荐[话题]##视频推荐玩具[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhgBJQ3dd7c2fhQER2AM6S7BSgAd_compress_L1',
    'video_id': '592d0bd3b46c5d78bb14d029',
    'title': '小蜗牛在吃西瓜🍉',
    'video_tag_list': '',
    'content': '🍉🍉🍉引来了小蜗牛'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/c513241f-7838865-9971-f38d71b07a12?sign=46b9ad527d8ffe026f0b15b4a6d322bf&t=65fb06d4',
    'video_id': '592d0f967fc5b856eb66df02',
    'title': '如何高逼格撸串！撸的不是串儿，是腔调！',
    'video_tag_list': '',
    'content': '#无敌来啦#大金链子小手表，一天三顿小烧烤。别小看街边撸串，逼格高起来也挺唬人！撸串系研究生毕业的帅无敌今天教你撸个串如何逼格高到心无杂念~'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/fdcb1a09-7e838d8-9db2-0aabf1ef8bdc?sign=c515209b2c524c7f7733114ad3bbeabe&t=65fb06d4',
    'video_id': '592d26407fc5b83620a7295c',
    'title': '穿吊带好看的肩臂训练|为什么你健身不瘦反而变得“虎背熊腰”',
    'video_tag_list': '8周变身比基尼女神',
    'content': '#8周变身比基尼女神夏天到了， 网红们终于可以将皮肤晒成发亮的小麦色，然后穿着牛仔热裤和吊带美美的出门了。可是比起洋装长裙，热裤和吊带对我们的身材要求却高出许多。大象腿、塌瘪的臀部，肚子上的“游泳圈”，以及松弛的手臂都变得无处可藏。上周我们将整个三期视频都贡献给了蜜桃臀，本周让我们一起雕刻好看的肩臂线条，最后我们会在下周视频里带大家练出马甲线。8周健身小白变身比基尼女神第六周，最好看的吊带肩臂，你准备好了么？'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lsIjtJC6gOom0VnWDgq7q7HYD58G_compress_L1',
    'video_id': '592d2f27d1d3b9648fa7ea21',
    'title': '柠檬水？才不是柠檬🍋加水那么简单！',
    'video_tag_list': '柠檬的巧妙做法',
    'content': 'cr美食台\n让你绝对改观的柠檬水制作方式！\n让你清爽一夏🍋～\n😘\n#假期宅在家[话题]#\n#柠檬的巧妙做法[话题]#\n#春天喝什么果汁[话题]#\n@生活薯'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhenn8x6g2VDeFivgGf-07MeQSic_compress_L1',
    'video_id': '592d487b14de4104d4c46327',
    'title': '5.29我的婚礼我的火烈鸟预告片',
    'video_tag_list': '我独一无二的婚礼',
    'content': '#我独一无二的婚礼[话题]#\n5.29我的婚礼，已经剪辑出预告片，好期待成品。先和大家分享一下。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrqdQAxFhLDoarxcpq49SGMRiGWE_compress_L1',
    'video_id': '592d4883d2c8a53556ad6399',
    'title': '耶里夏丽好好吃！羊肉串真棒！',
    'video_tag_list': '地道的新疆菜餐馆',
    'content': 'qiao好吃的！棒棒哒！会出一期图文的！就是等不急了一定要先告诉你们一声真的很好吃哦！\n我先撸两串，以后再说！\n祝大家都吃到好吃的烤串，么么哒～\n#地道的新疆菜餐馆[话题]#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lqtB1PS03N-ND1SUls22ylRWs5zR_compress_L1',
    'video_id': '592d6032d1d3b92751f0a9a3',
    'title': '祝小红书生日快乐！大巨蟹英语老师送来祝福啦！还有一点小提议嘿',
    'video_tag_list': '小红书生日快乐;汤姆·福特;嘉娜宝 Kanebo Twany极致粉霜 SPF23 PA++',
    'content': '#小红书生日快乐[话题]##小红书生日快乐[话题]##小红书生日快乐[话题]#金桃子眼影 07夹心 \n一直想着录这样一个视频，昨儿今儿上了整天的课，到下课的时候才想起来，拉学生一起来拍视频[得意R]我的学生年龄跨越度很大，从二年级到高中，到成人，都有哦，主要是预备国际高中，初中，小学的学生，还有要出国或者移民的孩子或成人。今天最后一课是四年级的课，所以就拉了他们中的一些人。感谢[飞吻R]\n还有我的小小曹[色色R]没错，就是我儿砸[害羞R]他已经上中班啦！但是个头很高[偷笑R]\n自从有了小红书，就相当男人有了王者荣耀[害羞R]每天早晨起来必看，每天必刷，真的很开心，我上次去上海还真的见了小红书里的宝宝，当时很紧张，感觉和当年那种网友见面一样，哈哈哈哈，还很不好意思。很开心分享一些美的东西，也同时学到了许多东西。\n有这样一个app，可以kill time，可以作为每天都要美美的motivation，可以学习更多的搭配，关注到更多的新品，真是赞。\n用了小红书之后，身边好多人都开始用了，我的朋友，客户，学生，家长等等，都开始用啦！真好！\n这次提了两个小提议，仅供参考！\n谢谢小红书app，让我们可以更美！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltHZZZC2G-qTLGZK7_cfe2l9j2dp_compress_L1',
    'video_id': '592d6a56d2c8a51588ad6391',
    'title': '🎂祝小红书生日快乐🎊🎉',
    'video_tag_list': '小红书生日快乐;欧时力 ochirly V领镂空水溶绣花无袖连衣裙',
    'content': '6.6 小红书就要4⃣️岁啦！[得意]\n祝小红书生日快乐！[装酷]\n虽然来到小红书才两个月，但是已经感受到了这里无比的魅力和🍠们的无限热情。\n愿与你一同成长～🤘🏻\n这是我第一个有声音的视频哟[讨厌] 和你想象中的一样嘛。（镜头前我的声音有点尴尬）\n（一定要看到最后哈哈哈哈[偷笑R]有惊喜）\n衣服也还是👉[偷笑R] 正好能给你们看细节嘎嘎嘎\n然后请忽略那个“今天是六月六号”[腹黑] 我………我等不及了还不行吗[讨厌]\n@视频薯\n#小红书生日快乐[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/854x480/vcodec/libx264/pgc/5c84e2aa-99b341f-9d41-979f0bf3d89e?sign=b36f07da48c3655c9eefa3e2629dc0d0&t=65fb06d4',
    'video_id': '592d7ad77fc5b8758fa72959',
    'title': '干货 | 科普 | 美国爱马仕配货指南 | 配多少 配什么 | 0.3:1 拿包经验分享',
    'video_tag_list': '爱马仕;出街最爱的包包',
    'content': '这次和大家谈一谈爱马仕的“潜规则”——配货。爱马仕最出名的包有两款，Birkin和Kelly（不讨论Constance，我的sales曾经和我说我如果想拿Constance不用配货，但我不喜欢，就没拿），我在美国华盛顿的店里拿过2个birkin和一个kelly，平均下来配货比例都是0.3：1左右，三个包加起来包以外的消费是1万美金左右。\n*注意：先统一概念，在这篇文章和视频里，配货包括所有买包之前的消费和买包当天的消费*\n在视频当中，我总结少配货拿包最重要的几个经验，也推荐了作为配货很值的几个产品（美国配货是算皮具的）。\n接下来我说一下我拿3个包的具体过程。\n我的3个包分别是在12月（2个铂金包）和4月（1个凯丽包）拿到的。\n我在12月拿了2个包因为我有两个账号，分别大约3000美金的消费记录。\n在视频中我展示的几个推荐作为配货的产品，包括1个护照夹、1个本子、1个twilly丝巾、1双平底鞋、1个kelly钱包、1个腰带都是我在6月-12月之间买的，另外我还买了1条小丝巾、1个卡包、2个twilly（共3条），1个本子（共两本），和3个香水的香皂。一共是大约$7000，最后拿了两个birkin。一个是Cuivre 红铜色 Togo 30 银扣；一个是 Trench 风衣米 Togo 35 银扣 （太大转给朋友了）。4月我在拿kelly之前只买了一个鸵鸟皮的小钱包，$4000左右，当时是有国内的朋友托我买的，结账的时候我的sales就问我有没有什么想要的包，两周后我就接到电话说到了一个kelly 28 黑色 Togo 银扣。\n划重点！！！（因为我觉得这条经验因人而异我就没在视频里说）\n因为我家和店离得很近，我所有的配货基本上都是分开买的。也就是说，多次地去买价格低的单品，是减少配货的办法。我当时去了很多次，和sales混熟了，和店里的其他店员、店长也都认识了。他们知道我想拿包，就给了我3个名额，还有教我开两个账号买东西的办法。和sales多说说话，聊聊天，就能更快，更少配货地拿到包。\n最后我想说：拿包是一个修行，一定要有耐心，平常心地等待~\n不要因为想急着拿包就丧心病狂地买一堆自己不喜欢的东西。\n和sales多建立关系，多沟通，会有更好的效果~\n如果你们在美国华盛顿周围，我推荐我的sales，叫Ashley，是个黑人小姐姐，人很好~\n#夏日包包[话题]##出街最爱的包包[话题]##春夏百搭包包[话题]# @视频薯  @穿搭薯'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltAWq_pw3uK1YyWOXNFKG5ERjheC_compress_L1',
    'video_id': '592e097b14de412e1b564df6',
    'title': '',
    'video_tag_list': '健身器械教学视频',
    'content': '【美背秘籍】5个动作塑造性感背部，美背轻松Get✔️\n所谓“新手练胸，老手练背”，大魔王在初进健身房时曾问过教练女孩纸为什么要练背呢？因为我们都不想变成虎背熊腰啊，相信很多小仙女也会有同样的疑惑。\n教练告诉我说健身房里流行着一句顺口溜“练胸不练背，含胸又驼背！”长期坐在电脑前的小仙女们可能多少会有点含胸驼背的毛病，通过加强背部的训练不仅可以减掉肩胛骨的赘肉，还可以很好地矫正身姿。更重要的是，没有宽美背，怎么能凸显小蛮腰？\n视频中给大家介绍了5个最基础、最有效的背部训练动作，小仙女们赶快和大魔王一起来Get性感美背吧~\nFOLLOW ME [得意R][得意R]  #背部塑形视频[话题]#\n-------------------------❤️-----------------------\n🌟跑步热身🌟\n无论做什么训练，热身都是必不可少的！在健身房里可以借助跑步机或椭圆机来进行，一般10-15分钟，微微出汗即可。\n🌟辅助引体向上🌟\n10-15个/组 x 4组；组间休息60秒\n说到练背第一个想到的动作应该就是引体向上了吧，但是对于大部分小仙女而言，我们的上肢力量并不足以支撑我们独立完成引体向上的训练，这时候就可以借助引体向上辅助架来进行。\n做引体向上的时候要注意【挺胸】在向上拉的过程中要时刻保持挺胸，尽量挺！同时肩胛骨收紧，并收紧核心。整个过程要缓慢进行，无论上拉还是下放都不要太快哦！有能力的小仙女还可以在顶峰做3-5秒的停顿，这样会更好地刺激到背部肌肉。\n🌟宽握高位下拉🌟\n10-15个/组 x 4组；组间休息60秒\n高位下拉是最好的练背动作之一，但找不到正确发力方式往往会导致背阔肌还没酸，手臂先酸。做这个动作的时候要保持挺胸，肩部下沉，双肘打开，不要耸肩。整个运动过程中肩胛骨应该是灵活的，向下拉时，先收下肩胛骨，再收背阔肌，感受背部发力，尽量不要用到手臂二头的力量；在上放的时候手臂肘部不应该是崩直锁住的，而是要留有些许自然的曲度，同时向上送肩胛骨。如果肩胛骨固定了不动，那么拉和收就会借用很多胳膊的力量，背部肌肉就得不到很好的锻炼啦！\n拉下和放回的过程要匀速，不要太快，注意肌肉的控制，使用的重量逐渐的递增，不要一次性上太大的重量哦！当重量增加到一定程度握力不够时，可以借助握力带进行训练。\n🌟器械划船🌟\n10-15个/组 x 4组；组间休息60秒\n之所以叫做“划船”其实就是在强调【划】的动作！这个动作轨迹应该是有一个自然的划的弧度，而不是直前直后地拉！\n为了能够更好的刺激背阔肌，做划船的动作时要记得挺胸！使劲儿挺胸‼️(其实所有背部训练动作都要建立在挺胸的基础上)向后“划”时收紧肩胛骨，手肘尽量往身体方向收，背阔肌收紧，想象用背部把它向身体后方拉，拉到最顶峰处停顿1-2秒，感觉背部肌肉在向中间挤压。千万不要耸肩！耸肩靠的是斜方肌来完成最顶端的收缩，就刺激不到背阔肌啦！回放的时候最好要一个往前送的动作，向前送一下肩胛骨。回放过程不要太快，注意控制。\n🌟反向蝴蝶夹胸🌟\n10-15个/组 x 4组；组间休息60秒\n这是一个训练三角肌后束的动作，我一般会放在练背日一起训练。动作全程手肘保持微屈，肘关节不要锁死，手臂在水平面上移动，顶峰收缩，要尽量控制离心收缩的过程，延长肌肉做功的时间。\n需要注意的是⚠️与其他练背的动作不同，这个动作不要挺胸加紧肩胛骨！肩胛骨应保持【打开】这样斜方肌就很难借力，从而可以更好地练到三角肌后束。\n🌟山羊挺身🌟\n15-20个/组 x 6组；组间休息60秒\n这个动作可以很好地锻炼到下背部肌肉，髋部以下紧靠在器械靠垫上，双脚用力踏实脚踏板，双腿蹬直。肩膀打开，挺胸抬头，头部保持中立，负重的话将哑铃片紧贴在胸前，若不负重双手可抱在胸前或捏住耳朵。下背部发力将上身抬起，保持腰背挺直，核心收紧，抬直至腿部与身体处于同一条直线上，稍作停留，再缓慢下放至起始位置。整个过程中保持均匀呼吸，起身时呼气，下放时吸气。 \u200b\n-------------------------❤️-----------------------\n今天视频中介绍的所有动作都是需要在GYM中借助器械做的训练，喜欢不要忘记点赞收藏哦！\n大魔王后续还会出一篇适合在家做的背部运动，欢迎小仙女们继续关注呦[飞吻R][飞吻R]\n露背的季节到啦，小仙女们都准备好了嘛？\n记得将背部训练添加到日常训练计划中去哦！有问题留言给我哟~[萌萌哒R][萌萌哒R]\n🎵视频背景音乐🎵PDD - 徐梦圆\n@小红叔  @视频薯\n#必须要安利的健身动作[话题]##见人不如健身[话题]#\n#厉害了我的健身房[话题]##健身是把整容刀[话题]#\n#健身器械教学视频[话题]##健身器械的正确使用方式[话题]#\n#运动风不能停[话题]##我为瘦身打卡[话题]##10斤减肥小目标[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgl5oRd8UddHiFsl6x-VEwPonNHc_compress_L1',
    'video_id': '592e158db46c5d655f14d023',
    'title': '可可麻薯夹心软欧做法',
    'video_tag_list': '每日早餐打卡',
    'content': '#每日早餐打卡[话题]#\n可可软欧的做法\n材料：\n1⃣️高筋粉 220g\n2⃣️全麦粉 50g\n3⃣️可可粉 15g\n4⃣️盐 3g\n5⃣️糖 30g\n6⃣️高活性酵母 3g\n7⃣️全蛋液 1个\n8⃣️水 125g\n9⃣️黄油 30g\n🔟内馅：核桃仁、蔓越莓干、葡萄干、红豆沙、麻薯\n步骤：\n1⃣️将所有材料除黄油外搅拌均匀混合揉成面团，加入黄油揉至扩展阶段，发酵至两倍大。（在这里我想说没有面包机厨师机的童鞋经常反应手揉面团很粘手，按配比根本揉不成光滑的面团，不用着急，我揉也是这样的😂，你就在盆里多揉揉面团，粘的满手都是也别管它，扔盆里发酵好就不粘手了，好吧，你说我不专业我也认了，反正我这样做出来的照样松软😂）\n2⃣️发酵的同时可以制作麻薯，步骤如下\n3⃣️发酵好的面团均匀分成三份，案板上撒上干粉，取一块排气擀成长方形，加入三分之一的麻薯，抹上红豆沙，撒上核桃仁、葡萄干、蔓越莓干等（按各自喜好添加，卷起来收紧收口，一定要收紧口哦，不然麻薯受热会爆出来）。依次做好三个面团，卷好定型后发酵至两倍大，撒上干粉，表面割成你想要的形状。\n4⃣️烤箱预热180°，预热好后放入烤箱烤20分钟，我习惯性在烤的过程中加盖锡纸，避免上色太深，你们随意。趁热家人就消灭了一整个✌️，密封保存哦，长时间保存可以放冰箱冷冻，吃前回温烤3-5分钟。\n麻薯夹心做法\n材料：\n1⃣️水磨糯米粉 70g\n2⃣️玉米淀粉 20g\n3⃣️糖 30g\n4⃣️牛奶 120g\n5⃣️黄油 10g\n步骤：\n将水磨糯米粉、玉米淀粉、糖和牛奶混合搅拌均匀，加入黄油，入锅蒸20分钟，出锅后搅拌成团，放凉盖保鲜膜备用'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/854x480/vcodec/libx264/pgc/5863a63a-9d58f3f-b308-90ab39310b81?sign=19a984ff2105058dd5b64e800929b156&t=65fb06d4',
    'video_id': '592e1e477fc5b82868a7295f',
    'title': '新手装备 | 我给中学生妹妹买了什么化妆品？| Makeup Beginner Set',
    'video_tag_list': '适合新手的眉笔',
    'content': '大仙女小仙女儿童节快乐！收到一些留言和私信让我推荐我认为最适合新手的产品，这次我给我初三的妹妹买一整套化妆品，都是我新手时期的真爱/回购过/现在超爱用的产品~\n提到的产品（按照视频中出现的先后顺序）：\n1. 眼影刷店铺名 雨潼彩妆\n2. 植村秀 睫毛夹\n3. 美妆蛋 beautyblender nude\n4. 妆底 Smashbox Iconic Photo Finish Foundation Primer\n5. 粉底 wet n wild Photo Focus Foundation #nude ivory\n6. 遮瑕 wet n wild Photo Focus Concealer #light ivory\n7. 腮红修容盘 Benefit Cosmetics Cheek Parade\n8. 鼻影 KEVYN AUCOIN The Contour Duo On The Go\n9. 蜜粉 Laura Mercier Translucent Loose Setting Powder\n10. 眼影 Viseart Theory Palette\n11. 眼线 Stay All Day® Waterproof Liquid Eye Liner\n12. 睫毛膏 Benefit Cosmetics Roller Lash Curling & Lifting Mascara\n13. 眉笔 Benefit Cosmetics Goof Proof Brow Pencil Easy Shape & Fill\n14. 口红 Dior Addict Lip Glow Color Reviver Balm\n15. 口红 TOM FORD Clutch-Size Lip Balm #02\n#适合新手的眉笔[话题]##新手必备化妆刷[话题]##新手最容易上手的眼影盘[话题]##平价好用的底妆产品[话题]##平价好用的单色眼影[话题]##平价VS贵价彩妆测评[话题]##最适合春夏的眼影[话题]##最滋润的口红[话题]##适合黄皮用的腮红[话题]##六一儿童节[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ls7uWVykKH9WeVlfzHU2znYrQ3nd_compress_L1',
    'video_id': '592e28d1b46c5d1c4a9e44fb',
    'title': '又被卡在缝里',
    'video_tag_list': '',
    'content': '不长记性 明明已经被卡住好几次了 还一定要去钻洗衣机缝'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lpvXihX3Y-LK3iXjtupsxQuKIj1a_compress_L1',
    'video_id': '592e2de0d1d3b974e9f0a983',
    'title': '61儿童节童趣妆容',
    'video_tag_list': '减龄妆的小秘诀',
    'content': '一年一度的装嫩盛事怎么能少得了我呢\n产品:\n兰欧媞妆前 荷拉气垫 傲蝶散粉 眼影 口红 睫毛膏 腮红均为多多小屋#减龄妆的小秘诀[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/01b613e3-14857d8-9178-cdbf431a0af6?sign=8c83bc48edf4b72a30b0981debae7309&t=65fb06d4',
    'video_id': '592e2e28a9b2ed2105f99068',
    'title': '【我的护发秘籍 之 工具篇】',
    'video_tag_list': '谭木匠;米歇尔 名仕 Michel mercier 意大利原木顺发梳;我的护发秘籍',
    'content': '✔️之前跟大家分享过一次我用来护发和造型的产品，这次再来一期护发工具的分享，主角是两把梳子，一把是来自谭木匠的木质黑牛角梳，一把是来自以色列的Michel Mercier魔法梳。\n✔️两把梳子各有各的特点和长处，解决的头发问题也很有针对性。\n1️⃣传统的单排宽齿梳，材质木头➕黑牛角，功能疏通经络，养发亮发。\n缺点：梳头发的时候有拉扯感，容易梳不通、或发尾产生断发。\n2️⃣Michel Mercier：跟一把大刷子一样，428个梳齿儿，粗细、高低和分布都不同，这个设计能够让梳头发的压力减小到普通梳子的1/10，还获得了国际专利。所以用它梳头发几乎没有拉扯感，也不会断发，非常适合发尾干、头发爱打结的小伙伴。\n✔️如我所说，这两把梳子的功能区分很明显，牛角梳长期使用能够养发亮发，魔法梳能够有效防止打结和断发，小伙伴们根据自己的需求来选择吧！我最近是超爱用这个魔法梳，有它在手，顺滑我有😎\n#我的护发秘籍[话题]##提升幸福感的家居小物[话题]##拯救细软发大作战[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/d771b0ab-9d391df-88df-44b4cd22baec?sign=a0b198d440cbc0c60ac7fd48b364d68f&t=65fb06d4',
    'video_id': '592e3a01a9b2ed5740f99068',
    'title': '毕业面试妆！这是毕业生们都需要get到的妆容！',
    'video_tag_list': '最适合面试的妆容',
    'content': 'HI~又是一年毕业季，来不及惆怅就要进入面试状态啦！\n应付面试除了需要专业素质高，当然也需要有一个好的妆面，让面试官们能够看到清新自然的你。\n面试妆容的要点就是自然大方，切忌不能浓妆艳抹，衣着也要得体一些，看起来有新人的态度却又自信满满！\n编了这么多。。。真是编不下去了！！！看视频吧！！！\n#又到一年毕业季[话题]#\n#毕业季妆容[话题]#\n#面试该化什么妆？[话题]#\n#上班look不无聊[话题]#\n#最适合面试的妆容[话题]#\n#日常妆容打卡[话题]#\n#日常眼妆怎么画[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkIVxFGgDxeoIUbBEHR0G-0mMysz_compress_L1',
    'video_id': '592e421714de415148564dee',
    'title': '大厨教你用转圈刀法，做一道超级美味的蓑衣茄子',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n茄子是夏日的当季蔬菜，也是一年中茄子最好吃的时节，爱吃茄子的人很多，至少我认为，茄子是蔬菜中最好吃的，木有之一。\n茄子菜好吃，但是费油太多了，这是因为茄子过油后才能更软烂、更容易入味，今天的这道蓑衣茄子，做法特殊，用油少、放少许肉，更入味，是夏天餐桌不可多得的美食。\n★★★★★\n创意指数\n蓑衣茄子\n▼\n蓑衣茄子\n·视频音乐·\nThomas Greenberg - The Right Path\n·食材·\n茄子、肉末、二荆条、小米椒\n姜、蒜、葱、高汤\n老抽、豆瓣酱、蚝油、糖、陈醋、盐\n1.茄子洗净，正面垂直入刀，不要切断\n2.翻面成45°入刀，不要切断\n3.移入蒸锅蒸至变色出锅备用\n4.热锅冷油，下肉末\n5.肉末变色后，倒入姜蒜末炒香\n6.倒入二荆条、小米椒、半勺豆瓣酱\n7.炒出红油后倒入蒸好的茄子\n8.倒入高汤拔匀\n9.倒入1勺老抽、1茶匙糖、1茶匙耗油、适量盐、少许陈醋，大火汁水收匀装盘\n10.最后撒上葱花即可上桌~！\n小贴士\n1.切蓑衣刀时千万不要切断茄子，入刀要均匀\n2.新手可以用筷子放在茄子前后，辅助入刀，这样就不会被断\n#周末家常菜[话题]##茄子的做法[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/10fee4ae-5c7c73b-ad4b-24a08fd138c0?sign=d842cdad12236d14fc95b5bcdbd20026&t=65fb06d4',
    'video_id': '592e6e7b7fc5b83e7a66df03',
    'title': '实话实说，这些事让你尿湿过几层床单？',
    'video_tag_list': '',
    'content': '小小年纪怎么能没有烦恼\n童年的阴影依旧在萦绕\n最好的朋友变成妈妈的菜这件事\n至今还让帅无敌想起来就心惊肉跳！'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/f73413a5-11852f4-8963-329532bd8bf8?sign=bd888f9fdc6a645ee2aea16f8181d058&t=65fb06d4',
    'video_id': '592e71b17fc5b85689a72959',
    'title': '越苦的咖啡越提神？',
    'video_tag_list': '',
    'content': '你们也是那么想的吗？咖啡那些不能不说的小秘密！\n#不喝咖啡会死星人[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/36fbfebd206550e9c17ce8825cd7126958830602_v1_ln',
    'video_id': '592e7da6b46c5d0ad06e4874',
    'title': '【视频试色】3CE新品气垫腮红视频开装试色',
    'video_tag_list': '白皮最显气色的腮红推荐;3CE 持久水嫩果汁气垫腮红',
    'content': '#元气少女必备腮红[话题]##白皮最显气色的腮红推荐[话题]#\nstylenada旗下的少女品牌3concepteyes\n简称3CE最金出了新品气垫腮红\n果汁水润显色滋润 （她家模特小姐姐的气色妆容真是太美了）\n一共6个颜色 其中包括：5个腮红1一个修容\n#pink 粉色\n#peach桃色\n#coral 珊瑚色\n#girlsh red红色\n#mandarine橘色\n#soft brown 柔棕色（修容）\n使用感受：都为液体气垫没有那么粘稠\n不会担心使用上去有叠粉的厚重感\n很好吸收\n粉扑也很软密度很厚'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/f16d38b321ca907e4cb8132e9c03eb5618abf50b_v1_ln',
    'video_id': '592e8bb87fc5b8533e144dd0',
    'title': '工作日的下午，看这个好解压~',
    'video_tag_list': '用视频记录旅行',
    'content': '【水母疗法】：水母游动的姿势可以帮助人转移注意力。假如眼前的工作让你心烦紧张，你可以通过观察水母，让眼睛及身体其他部位适时地获得松弛，从而缓解压力。\n这支视频的作者是@PNK-PIC，来自话题#用视频记录旅行[话题]#，这是香港海洋公园的水母哦。\n话说有人来告诉视频薯这是什么水母吗~\n你们有什么解压视频，不如也发上来@视频薯[吧唧R][吧唧R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/c00953b4db75e6d5e0a9f2d4ef8711f44ceae683_v1',
    'video_id': '592e8f71a9b2ed2056230f95',
    'title': '超可爱兔兔毛巾折叠法',
    'video_tag_list': '',
    'content': '儿童节到啦，还是宝宝（？）的我们不如来找些有♂趣又可爱的事情做吧~今天喵酱就来教各位超可爱的兔兔造型的毛巾折叠方法哟~てへぺろ(´>ω∂`)☆  #视频教你生活小窍门[话题]#\n#六一儿童节[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/592e9db2b46c5d62ce6e4875_compress_L1',
    'video_id': '592e9db2b46c5d62ce6e4875',
    'title': '🎈小红书生日快乐🎈',
    'video_tag_list': '小红书;小红书生日快乐',
    'content': '#小红书生日快乐[话题]#\n祝小红书4岁生日快乐！！！[萌萌哒R]\n转眼加入小红书已经两个月啦～\n期待以后在这里继续跟小红薯们分享点点滴滴❤️'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llSTS9pbw1Tc8xsh6VKNM3fBy8E9_compress_L1',
    'video_id': '592eab22d1d3b97351403be5',
    'title': 'kelly 28 开箱',
    'video_tag_list': '爱马仕',
    'content': '新加坡买的 要配货\n等我拍了照片再慢慢道来\n总之的确很lucky'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/ltXv1hO19bOIxAa6sireALlOqHe9_compress_L1',
    'video_id': '592eff70d2c8a55922981f14',
    'title': '中国家庭的宿命：为什么心累，总来自最亲的人？',
    'video_tag_list': '天津;北京;北京周末做什么',
    'content': '文︱艾明雅\n01\n你最大的挫败感什么时候？\n一个29岁的姑娘，在深圳，独自买车买房。相亲无果，恋爱未知，那段时间每天工作十二个小时“感觉整个脑子都烧坏了”。回家发现两个老人发脾气，要闹着回老家，原因就是下午有个姑姑给她打电话说介绍对象，她委婉拒绝了。\n父母几乎是愤怒了：“你还要挑到什么时候？”然后从挑剔她的长相，到她的人生观，一整夜。终于再次爆发争吵。她在电话里泣不成声对我说：“作为一个员工，我每天都要面临无数KPI考核，可为什么我回到家，依然还要被打分，被指责，我真的只是希望那一刻，他们作为我最亲的人哪怕唯心说一句闺女你不要着急，即使一辈子不嫁人爸妈也等你回家。\n比起优秀的自己，这个时代每个年轻女孩子，更大的幸福感和安全感，一定来自“被爱的自己”。\n可是，这样坚强勇敢独立，值得赞赏的姑娘，却在冰火都市里流泪。\n“我不怕千头万绪的工作压垮我，我只怕累倒想要一个拥抱的时候，你们作为我最亲的人，用世俗的标准说我不值得。”\n02\n这些年，我听多了太多哀婉的故事，那些明明长相姣好，温柔上进的女孩子，自带令人遗憾的不自信，始终无法救赎的自卑，都来自于在生命的最初没有被温柔而首肯地对待过。\n父亲指责，母亲挑剔，哪怕是以爱之名，都给了这孩子最大的恐惧：原来尘世残酷如此，原来我要考到第一名，我要变成三好学生，我要25岁嫁人，30岁生龙凤胎，才使得我的父母好好爱我。\n这心智模式直接又使得太多的女孩子长大后在爱情里不自觉成为一种“讨好型恋爱选手”，她们永远在为那个其貌不扬平淡无奇的男人端茶倒水，在试图成为一个五星女友，优质妻子，因为潜意识里她觉得，只有这样，她才值得被爱。\n她的心智模式让她养成这样的行为模式：一定是因为我好好做了某件事获得了某种“灿烂，辉煌，美丽”的身份，我才被爱；而不是因为，我哪怕工作平平，大龄未嫁，却依然正直，勤奋，善良，就值得被爱。\n曾经有人问我说，该不该刻意提前让孩子去直面一些现实世界的残酷。\n我拼命摇头：请爱他，拼命爱他，在是非明朗的范围里给他最多的爱，而不是考核，而不是见识什么残酷。对一个中国孩子而言，这个世界上最大的残酷，永远不来自他遇到多少事业上的艰辛，也不来源于她恋爱失败了多少次，那残酷一定是他被这世俗逼到墙角的时候，家人亦变成“对错警察”，连同世俗标准一起审判他。\n那一刻，他将知道，什么叫“你生了我，却弃我于荒野”，对他而言，那才是人生最心碎的残酷。\n所以你说，中国的孩子们，还有必要提前知道什么是世界的残酷？\n03\n你说，中国人爱孩子吗？明显是爱的。可是中国的家庭关系，可能坐拥这个世界上最令人不解的表达方式。\n“我”明明是你唯一的儿子，你明明对我赋予厚望，鼓励我的方式就是：就凭你这个败家样子，以后我就给你买个小三轮车，你就在你校门口捡一辈子垃圾。\n“我”明明是你最亲的女儿，可是在你眼里，我胸平，腿粗，牙齿不整齐，永远不讲卫生把头发掉在地上，这就是你眼中的我。\n这样的“我”，择偶的时候，你就觉得我“就凭你这样差不多就得了”，你觉得我挑剔对门葱油饼大叔的独生子，“他家拆迁分了两套房啊”，你永远觉得任何一个和我来相亲的人，最后没成都是因为我太挑，我太作，我吓跑了人。\n那姑娘说，她人生最大挫败感，在23岁的时候有个青年才俊追求她，她妈妈居然吓坏了，“就你这样，他看上你哪一点？以后一定会出轨。”\n原来你永远觉得别人的孩子比“我”好。\n而且，如果“我”没符合那标准，我如果成为不结婚，不嫁人，独一无二的人，只要我表现得和别人不一样，还会给你“丢脸”了。\n虽然亲情，是这个世界上最能给予一个人安全感的情感，可是在中国人这里，畸形演变成任何关系都能凌驾这段关系之上——你不结婚，你考得差，你大龄未嫁，你离婚，都让他们丢脸了。亲情永远让步于面子与规则。\n《倾城之恋》里的白流苏，婆家呆不了，娘家留不住，“一个女人，再好些，得不着异性的爱，也就得不着同性的尊重”——岂止，连血脉亲情都得不到了。\n因为不合规则。\n可是家人啊，什么是亲情，什么是爱。爱就是去他的规则。在这个闭环里，你给我的爱来自无条件的支持，360度全方位的理解，面对世俗的一致对外，生命本身的舐犊情深；绝不来自我要“长得好，考得好，工作好，嫁得好。”\n你爱我，没有理由，没有原因，这样，我才能觉得你是我的亲人。\n04\n那我就是天生就这么迷之自信的吗？\n不是，是因为我妈妈永远支持我，她支持我成为在课上照镜子的那个，支持我成为大学里第一个染头发的那个，支持我成为高中时候打五个耳洞的那个。我捡垃圾还是当作家，我都是她的最爱。\n在生命的最初，我就知道了，不管我怎样我妈都爱着我。全世界挑剔我，指责我，或者嘲讽我，都没有关系，还有妈妈，我就能够幸福快乐地生活下去。\n这力量，最后就变成此生最大安全感。温柔而有力量的安全感；反之，它就会成为一个人最大的伤痛和不信任感。而太多人发现，她最大的痛苦来自，她曾那样被伤害过，却用那同样方式，又施予了她身边的人。那一刻，善有了轮回，恶也有了。\n生而为人，修爱，或是修恶，那是我们各自要走的路。但我依然希望，我点了这盏灯给你，终有一天，你原谅曾经被“糟糕”对待过——毕竟，他亦是第一次当你的父亲或是母亲。\n那个被母亲说“你哪一点配得上青年才俊”的姑娘说，十年之后，她自己做了母亲，才知道为什么是亲人最质疑自己——\n因为你是血脉，是复刻，他们在你身上，看到了他们自己的美丽和强大，也看到了自己的虚弱与哀愁。他们害怕，是自己的弱传递给你，害怕你克服不了那基因里的弱。因为他们自己此生没能克服他们就不相信你可以。\n他们害怕是你高看自己，忽略了那弱，看不清自己，却试图打开更美的潘多拉盒子受到伤害。所以他们不相信你能嫁给更好的人，不相信一个小女子瘦弱的身躯能够撑起一家公司，不相信你一个人在冰火都市也可以过得很好——\n所以他们永远想给你一种保底的生活。而却不知道，当你试图高飞，他们只想给你一个笼子的时候，你的心就开始累了。\n怎么办？\n你是大人了。你得告诉他，展示出，你的力量很大。因为，你可以给予那力量给你的孩子和你的爱人。在你决定割裂过去，给予的那一刻，你就获得了救赎。\n你和他们并不一样。当你开始接受并敢于这一点，你就会发现，你的力量来了。我们从联结，到分离，再到原谅。\n这就是中国家庭的宿命。\n完\n#小红书生日快乐[话题]##宝宝早教这么做[话题]##不花钱早教[话题]##北京周末做什么[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqZfIjWRqCvPMTcs_1FC9zB8RreO_compress_L1',
    'video_id': '592f75cfd2c8a50ded44e886',
    'title': '柯基 · 不高兴的胖基👇🏼还会斜眼儿看人',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '上上周末出去玩 放朋友家两天 把朋友家嚯嚯了一通...被我朋友栓起来 又委屈了 一脸不高兴 还斜眼看我朋友😂我当时隔着屏幕 都感觉到了百利的怨气哈哈哈哈哈哈哈\n#我家宠物最萌的瞬间[话题]##我家宠物最萌的瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/cc64470d70662fe86a96ff61a57d14ae5230a270_v1_ln',
    'video_id': '592f79add1d3b962fedaa80b',
    'title': '成本只有5元的菜，却做出了米其林餐厅的感觉',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n秋葵是一种一年生草本植物，也叫黄秋葵、咖啡黄葵，俗名羊角豆、潺茄。果荚脆嫩多汁，滑润不腻，香味独特。\n老豆腐洁白明亮、嫩而不松，卤清而不淡，油香而不腻；食之香气扑鼻，有肉味而不腥，有辣味而不呛。\n★★★★★\n创意指数\n豆腐秋葵\n▼\n豆腐秋葵\n·视频音乐·\nGontiti - 朝\n·食材·\n老豆腐、红椒、秋葵\n生抽、香油、姜\n1.豆腐洗净，稍许厚切备用\n2.焯水后捞出备用\n3.秋葵洗净，切切去头部后切半\n4.利用之前的沸水，焯水捞出备用\n5.红椒切圈\n6.姜切末\n7.取空碗倒入一勺姜末，淋上热橄榄油\n8.倒入1勺生抽、1茶匙香油拌匀\n9.摆出造型\n10.淋上酱汁即可\n11.用这道菜去征服你的家人吧~！\n小贴士\n1.喜欢嫩滑口感的朋友，豆腐可以选用韧豆腐\n2.这道菜建议现做现吃不宜久放\n#跟着视频学做菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/3c2c5ad1-7c1fa60-b691-658f580cea33?sign=1f29064b63f08fe080426220f0518553&t=65fb06d4',
    'video_id': '592f7cec7fc5b80ec130ee6f',
    'title': '熬夜急救妆！最适合小长假之后的你！',
    'video_tag_list': '熬夜后怎么急救？',
    'content': '👋👋👋国际惯例先自报家门哦~\n23岁~坐标在武汉哦~干性敏感肌，所以如果你跟我差不多！别忘记关注我哈哈求关注啦！🙌🙌🙌\n小长假玩的开开心心，第二天上班发现自己的肤色超级无敌暗沉！[扶墙R][扶墙R][扶墙R]\n只想赶紧画一个熬夜急救妆来分享给大家~把好气色画出来！\n也提醒大家一定要少熬夜，因为熬夜闭口痘痘真的一起来！哭瞎了！\n以下这些常见的因为熬夜出现的上妆困扰，视频都有帮助大家解决哦~\n👉STEP1：👈熬夜肌肤暗沉，肤色不均越来越明显怎么办！\n一般紫色的隔离霜就是起到修正作用的，我觉得可以先用一个紫色的隔离霜来修正一下暗沉的肌肤，再来画底妆效果会更加好一些哦~紫色隔离霜一定要少量，不然会泛白！\n👉STEP2：👈熬夜肌肤出油太多上妆浮粉怎么办！\n建议先好好的洁面一下，让脸部处于一种清爽状态之后，用一个类似于苏菲娜的控油妆前产品，点涂在出油多的位置就好啦~这样能够让妆容持久一些，也很好的控制住了油腻的尴尬哦~\n👉STEP3：用了妆前还是觉得底妆暗沉的快怎么办！！！👈\n如果手边会有一瓶提亮液就好啦~用提亮液+粉底液混合的方式，不仅可以让粉底液变的更加的亮泽一些，也能够让底妆更滋润，减少卡粉尴尬，这样混合的方法能够让底妆暗沉的速度变慢！当然，后续加一个有提亮肤色效果的粉饼效果更好哦~\n👉STEP4：底妆卡粉，又想定妆怎么办？👈\n其实定妆喷雾这种神器的存在，给干皮和肌肤状态不佳的人解决了太多问题啦！喷一下，自然干就好了！居然还会有妹子问我黏不黏，我就问一句，你喷水在脸上会黏吗~必然不会的呀！所以一般自然干掉就好~当然，如果想要底妆更加服帖一点，也可以喷过之后用海绵蛋或者粉扑采用按压的方式就好！\n👉STEP5：熬夜之后两眼无神！👈\n除了靠画眼线来解决两眼无神的囧况，其实画一个有眉峰的眉毛也是必要的呀~眉峰不用太突出，稍微画出来一点，能够让人看起来精神很多呀！\n👉STEP6：熬夜后肌肤泛红，底妆都遮不住怎么办！👈\n紫色腮红的存在就是专门针对泛红肌肤，和紫色隔离是一个道理，可以起到修正肤色的效果，既能修饰红血丝，也能够让脸部看起来粉嫩一点。\n👉STEP7：熬夜之后肌肤暗沉，原本白皮变黄皮！唇膏怎么选！👈\n橙色是任何肤色的人都能hold的住的哦~所以选橙色的唇膏提亮气色是绝对不会错的！记住是橙色不是橘色哦~然后用这个颜色，也能让人白一度，衬肤色！还能点亮心情！\n好啦~大家记得戳视频哦~\n#熬夜后怎么急救？[话题]#\n#熬夜神器[话题]#\n#日常妆容打卡[话题]#\n#日常眼妆怎么画[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/d23df2d0779a89b5301e442ecb3613e3a3d1e8cd_r_ln',
    'video_id': '592f8cbcb46c5d7bc8495c03',
    'title': 'USJ小黄人爆米花桶会说话哦',
    'video_tag_list': '萌你一脸血的卡通周边',
    'content': '#萌你一脸血的卡通周边[话题]##六一儿童节[话题]#拍出Bob来卖个萌～在大阪环球影城排了半天队才买到的，会说话的bob爆米花桶～～超级可爱，工作人员也都好可爱，看到我一路背着都会开心地喊minion！还和我击掌哈哈～每次到主题乐园都觉得自己还是个孩子[少女心] #小黄人[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/d517b211-fc46a1c-b61e-74ba11488adb?sign=47ae2926c385bb3853485fd75786806c&t=65fb06d4',
    'video_id': '592f90ed7fc5b87c2b30ee6a',
    'title': '家庭训练神器「哑铃」的使用指南',
    'video_tag_list': '',
    'content': '一个小工具就能搞定健身？那非哑铃莫属，这最经典的健身工具。只要方法用的对，让你的健身训练事半功倍！#健身# #减肥# #哑铃# #哑铃杠铃教学视频[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/5639a4ee-9e8a9ae-b842-77bf6f722980?sign=3520af2fab5ff3780e63fd43a801ce08&t=65fb06d4',
    'video_id': '592f910e7fc5b878cca09b6d',
    'title': '这是一个可以下饭的小视频',
    'video_tag_list': '',
    'content': '这是一只萌萌哒非洲迷你刺猬~来自话题#我与宠物的日常，它的主人是@💓小妮子🎀\n看到一身的刺你就避之不及？相信视频薯，这会是你生活中遇到的最与众不同的宠物，走进它你就会发现防御的外表下，其实住着的是一个分分钟戳萌点的小妖精😉\n与普通的野生刺猬不同，非洲迷你刺猬的体型较小，成年后也不过手掌大小，重要的是它们身上也没有野生刺猬那样的体味，饲养环境得当也不会招惹寄生虫。不过它胆子非常小哦，一旦受到惊吓就会缩成一个刺求， 是一种十分可爱，但是也脆弱需要坚硬的外壳的的小动物~'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x272/vcodec/libx264/pgc/221c281d-d7caad6-a8f0-929ee267e879?sign=6533587a87852dc581ea0c2a5f1d4922&t=65fb06d4',
    'video_id': '592fa1aba9b2ed286ec71403',
    'title': '玩儿起来欲罢不能的迷你娃娃机',
    'video_tag_list': '谁是吊娃娃大神',
    'content': '谁说长大了就不能有童心？这个迷你娃娃机一被@林大哈_58FD612E 带回家就成了大小老少抢着玩儿的对象~而且一玩儿就可以玩儿超久，过足抓娃娃的隐！\n来自话题#谁是吊娃娃大神[话题]# #六一儿童节[话题]#\n你是怎样保持童心？拍视频@视频薯 吧！~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/56504d73e86cbdcd58ef5afb59917c6ae92350f4_v1_ln',
    'video_id': '592fa8c87fc5b8751da09b6e',
    'title': '给孩子做份爱心厚蛋烧，不放任何调料也能很美味',
    'video_tag_list': '',
    'content': '首先祝各位小伙伴六一儿童节快乐哈！\n今天的节日礼物是这份「爱心厚蛋烧」\n一份不放任何调料也能很美味的亲子营养餐…\n适合一周岁以上的所有大小朋友…\n而且制作方法也比较简单快手…\n减肥塑形的朋友也能拿来当代餐哦…\n#六一儿童节[话题]##鸡蛋的巧妙做法[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/31bc0d86-c01654a-abcc-4b99c6ba093d?sign=6f2edf1584bb8a61921b4ecef8491fbb&t=65fb06d4',
    'video_id': '592fa923a9b2ed53e773f87c',
    'title': '新手必看！眼影画法大全｜从单色眼影到五色眼影的画法套路',
    'video_tag_list': '',
    'content': '新手必看的一期视频啊 很多人都说不会画眼影\n这个视频很实用啊 所以大家千万不要错过啦\n我分享一下我自己画眼影的套路\n从单色眼影到五色眼影 每种眼影介绍了两种画法\n其实学会前三种基本上所有的眼影都可以用同样的套路来画\n最重要的就是晕染！！！\n基本上学会了所有眼影都能掌握啦～\n视频中提到的产品：\nkiko单色眼影 ＃137\nnars双色眼影 ＃吉隆坡\njcat三色眼影 ＃104\nvisee四色眼影 #or-6\ncanmake五色眼影 ＃07\nbgm：let me love you——Justin Bieber\n口红：Dior变色润唇膏＃001 叠加 得鲜双头气垫口红 ＃rd01'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loJUhupEgLWXzHJxAh36FBsD3U0u_compress_L1',
    'video_id': '592fb9bdb46c5d7bb745435c',
    'title': '有颜值的星空果冻😋',
    'video_tag_list': '网红美食我来推',
    'content': '一直对星空果冻情有独钟～\n颜值高味道好\n刚好看到一个比较简单的教程\n教你怎么制作星空果冻～\n大人小孩都爱吃～\n😋😋😋\n@生活薯\n#六一儿童节[话题]#\n#网红美食我来推[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/5f3e8b55325bd50117069e3ea7d803ad67128dff?sign=7169b4e6248f79e23c3b5a4fb87036d7&t=65fb06d4',
    'video_id': '592fde2a14de41645eb41ab4',
    'title': '婴儿排气操 超级简单被动操教程视频',
    'video_tag_list': '',
    'content': '适合腹胀气 肠道蠕动差的宝宝\n对于几天没拉便便的宝宝也有效果\n我家宝宝一个月的时候\n每天早晚至少做一次 所以基本上没有因为腹胀气哭闹过\n朋友们的宝宝做完半小时内会拉臭臭或者放臭屁\n不过大家节奏可以慢一些啊 我是为了让大家迅速的看完动作 小婴儿如果肌张力比较高 更需要慢慢的轻柔一点做曲膝动作\n新生儿适用～～～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/84cad409188f60f3bcaad203696e95ff84f5a425_r_ln',
    'video_id': '592fe422d2c8a533c6965605',
    'title': '🏋🏻\u200d♀️如何使用健身房的龙门架？(含视频)',
    'video_tag_list': '必须要安利的健身动作',
    'content': '常去健身房的小伙伴有些时候是不是会对一些器材有些困惑，不知道该如何使用？今天我就给大家演示一下该如何使用龙门架。\n龙门架是很好的训练方式，有着N种的训练方法。这次先给大家示范4个上肢练习的动作，希望可以帮助到大家。[萌萌哒R]\n视频的前几秒会简单的介绍龙门架。紧接着就是4个动作训练。\n---开始---\n在练之前首先要选好握把，这次我们使用的是短三角形的握把。选好握把后扣到挂钩上面，然后调节高度。\n1. Kneeling press\n⚠️：双膝着地，握把调到胸部位置，双手推出去再进来，腹部要收紧，整个过程中都应该感受到阻力。脚尖着地，立起来，不要脚背着地。练这个动作的时候要感觉到腹部很累\n1. Hammer row\n⚠️：单膝着地，握把调到胸部位置，仔细看动作的第一部分是夹紧肩胛骨，再来用胳膊拉。右手的话就是左腿跪在前面。左手的话就是右腿跪在前面。后面的脚不要脚背着地，要脚尖立起来。这个动作是练背部的力量。\n1. Kneeling overhead lean\n⚠️：双膝着地，握把调到比头高一头的位置，双手手臂上举，形成菱形。身体往内侧倾，这个动作练的是侧腹的力量。\n1. Side plank pull\n⚠️：握把调到脚踝以上的位置。一侧胳膊侧撑，上面的腿踩在地板上，用另一侧胳膊来拉。这个动作可以练习到平衡，腹部以及肩膀。\n每个人的重量都不一样，自己试一下，找到自己适合的重量。每个动作左右两边各8次。每个项目各做4组。\n---结束---\n想看更多健身视频的话就点击我主页，里面有一些视频可以供大家练习。如果还有什么问题的话，就在底下留言吧。最近我视频会发的比较频繁一些，希望大家继续关注我 [害羞R]\n#必须要安利的健身动作[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/01e2480472200bfb01837003801ba13f25_259.mp4',
    'video_id': '592fedefd1d3b9406ac6396b',
    'title': '儿童节最好的礼物#绘本推荐#我们的身体#',
    'video_tag_list': '在绘本里看世界',
    'content': '#视频绘本打卡[话题]#\n我在视频里都介绍的很详细了呢。这本《我们的身体》真的炒鸡炒鸡棒，非常详细的讲了我们如何出生到长大，吃饭，消化，生病，及男孩女孩的身体特征等等，最后两页没有录，感觉男孩女孩的生理特征妈妈们可以叙述的更好呢。\n灰常值得入的一本绘本，生动，有意思，宝宝在羊水里成长，书本里真的有水在动，宝宝在妈妈的阴道里出来，头先来到世界上。书本里含蓄又直接真实的表达！这是孩子们需要的书本，直接能让他们接受的事实！！许多妈妈不懂如何表达，这本书讲的就非常棒了呢！\n@薯宝宝 #一起读绘本[话题]##六一儿童节[话题]#\n#视频绘本打卡[话题]##在绘本里看世界[话题]#\n#幼儿教育必读绘本[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/li_obgI5mg6pXO0R-FJ-2wchxo08_compress_L1',
    'video_id': '5930213fb46c5d1707454367',
    'title': '无眉星人画眉教程——和半永久说拜拜',
    'video_tag_list': '简单易上手的画眉方法',
    'content': '大家期待已久的画眉教程终于出来了～\n画眉还是熟练功了啦，我其实已经熟练到平常不画框的，但是为了学习方便视频里我画了。其实真正的大神都是用液体眉笔画纹路的呢，我暂时还不敢尝试。\n#小红书生日快乐[话题]# #六一儿童节[话题]# 今天是六一，所以BGM就选了我最喜欢都柯南啦，同时将此片献给小红书的生日。\n眉笔是植村秀#适合新手的眉笔[话题]#，眉粉是Kate #自然又显色的眉粉[话题]#\n#眼妆每日打卡[话题]# #日常妆容打卡[话题]# #简单易上手的画眉方法[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqdYB4ULEBmFQ7ln2HS0JToZcg18_compress_L1',
    'video_id': '59306227d1d3b9140ec63968',
    'title': '宝宝是男孩子😂',
    'video_tag_list': '给宝宝的mini情书',
    'content': '宝贝7个月了，很爱笑。我想记录他每天的笑脸。\n#小红书萌娃大赛[话题]##给宝宝的mini情书[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrXkhCZeGAFWVlXu4m6_91phfjsU_compress_L1',
    'video_id': '5930900414de4152f5b41aae',
    'title': '我们胖基可会找靠山了哈哈哈',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '你让我下去？我不下去.......\n好吧好吧我这就下去.....嘿嘿逗你的我就不下去\n我在妈妈怀里 我委屈.....你看妈妈都没说让我下去\n你不管我了？太好了 开心\n#我和宠物的日常[话题]##我家宠物最萌的瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/197cf173-4db5989-b706-5dac574b7a9e?sign=db624509ad61f86828aa76b2d919d3a0&t=65fb06d4',
    'video_id': '5930d1017fc5b84fe804b6d4',
    'title': '晒后修复靠什么！别等晒伤了再急救！',
    'video_tag_list': '晒后修复靠什么？',
    'content': 'HI~暴晒的季节，除了需要做好防晒工作，当然还需要做好晒后修复工作啦！\n所以来跟大家分享一下我的晒后修复的一些小秘诀吧！\n敲黑板：一定要记得涂防晒，哪怕你是在室内！也一定要记得防晒，隔离不等于防晒哦~任何有防晒系数的底妆产品也不能等同于防晒哦~\nSTEP1：先用一个带有镇定效果的芦荟胶来舒缓和镇定肌肤，可以迅速的先减轻泛红的情况！\nSTEP2：晒后的肌肤其实是非常非常缺水的！所以在确保肌肤已经舒缓过了的情况下，可以适当的通过湿敷的方法来给肌肤进行一些水分的补充~比如用温和的喷雾或者纯露，来给肌肤进行湿敷！能够在短时间内减少肌肤的紧绷感！\nSTEP3：晒后短时间内敷美白面膜，是能够达到控制肌肤变黑的效果的，前提是要确定这款面膜确实是有美白效果的。如果你是一个有斑的妹纸~不妨试试看，在敷面膜之前，把淡斑精华在脸上打底，涂一些在颧骨或者是容易长斑的位置，再来敷面膜，能够达到事半功倍的效果哦~\n如果还有什么晒后修复的方法，在评论区相互种草分享哦~\n感谢观看！\n#晒后修复靠什么？[话题]#\n#我的护肤日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhB-i_pOngtmXwtQ7tYVjQlF0ZJY_compress_L1',
    'video_id': '5930e214b46c5d17b7454378',
    'title': '《这些整理鞋柜的方法 每一条都实用》（1/3）',
    'video_tag_list': '',
    'content': '作为家门口或玄关最重要的存在，鞋柜只有摆放整洁才会让进出门心情都变得好起来。视频里介绍了合理利用鞋柜的方法，每一条都实用易操作。\n系统限制5分钟，分三部发，这是第一部'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fo4mQtDjiyAXkHOP4JkXXoK17uWw_compress_L1',
    'video_id': '5930e4f6d1d3b92d61cbfc3f',
    'title': '三木布偶家新伙伴～小三山',
    'video_tag_list': '',
    'content': '这谁家小娃娃这么可爱😘'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnJPL31abZYznowk5kYy7L4iffDC_compress_L1',
    'video_id': '5930f5d2b46c5d5a28eb65fc',
    'title': '《这些整理鞋柜的方法 每一条都实用》（2/3）',
    'video_tag_list': '',
    'content': '作为家门口或玄关最重要的存在，鞋柜只有摆放整洁才会让进出门心情都变得好起来。视频里介绍了合理利用鞋柜的方法，每一条都实用易操作。\n系统限制5分钟，分三部发，这是第二部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg_eZAVoQGgx2HCN2TeVNzW_0mmN_compress_L1',
    'video_id': '5930f685b46c5d6a9ad18bd5',
    'title': '《这些整理鞋柜的方法 每一条都实用》（3/3）',
    'video_tag_list': '',
    'content': '作为家门口或玄关最重要的存在，鞋柜只有摆放整洁才会让进出门心情都变得好起来。视频里介绍了合理利用鞋柜的方法，每一条都实用易操作。\n系统限制5分钟，分三部发，这是最后一部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/pgc/8eaaddad-6a4c1b6-b834-d69b7f72b84e_compress_L1',
    'video_id': '59310576a9b2ed6084b3c84e',
    'title': '中法混血宝宝竟然也能把古诗词背的溜溜的！',
    'video_tag_list': '小红书萌娃大赛;小红书萌娃大赛',
    'content': '中法混血的杰杰宝宝已经2岁七个月啦，这是宝宝的国学第一课哦~\n念起古诗词来也是超级可爱的！！\n小红薯们听得出宝宝念的是哪几首古诗吗~\n#小红书萌娃大赛[话题]#\n#萌娃最爱[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljv2johgznoj_R0cpbOcKPZr2nmM_compress_L1',
    'video_id': '5931091d14de412d5bd73403',
    'title': '韩舞爵士舞  分享',
    'video_tag_list': '',
    'content': '我自己一直上韩舞爵士课  经常在APP 上看跳舞学习，目前只会一些基本的动作，没办法自己太笨啦～这个视频是最常见的韩舞啦～学完这支舞跳起来就美美哒[得意R]有想学舞蹈的妹子可以点赞收藏～我会发布更多舞蹈视频的[害羞R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/34512f20fa884aa799550379a3d60f78d6c0fbcb_r',
    'video_id': '59310a4cb46c5d2684d18bd2',
    'title': '女孩子变美需要的一些步骤👧快去护肤化妆吧',
    'video_tag_list': '',
    'content': '最经典的一句话，只有懒女人，没有丑女人。变美运气都会变好，还有什么理由不化妆呢？'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ll2SpaR-5acVZ5T6_KV-O0bHEqx__compress_L1',
    'video_id': '59310c5cd1d3b9260155e0da',
    'title': '韭黄炒蛋这样搭配好看又好吃，1分钟就能学会哦！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n韭黄也称“韭芽”、“黄韭芽”、“黄韭”，俗称“韭菜白”，为韭菜经软化栽培变黄的产品。\n韭菜隔绝光线，完全在黑暗中生长，因无阳光供给，不能产生光合作用，合成叶绿素，就会变成黄色，称之为“韭黄”。\n★★★★★\n创意指数\n韭黄炒鸡蛋\n▼\n韭黄炒鸡蛋\n·视频音乐·\nLex Vandyke - How Deep Is Your Love\n·食材·\n韭黄、鸡蛋、圣女果、盐\n1.韭黄洗净切段备用\n2.圣女果切成4小瓣备用\n3.鸡蛋打入碗中，打散备用\n4.鸡蛋炒散备用\n5.热锅冷油倒入韭黄\n6.炒出香味后放入1茶匙盐调味\n7.倒入鸡蛋\n8.倒入圣女果炒匀盛出\n9.简单又美味的快手菜就完成啦\n小贴士\n1.韭黄比较嫩，不宜炒太久，否则会出汤\n#跟着视频学做菜[话题]# #快手菜大挑战[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnDSZ3Jpb_ZH62TVH2C75xVcn6bF_compress_L1',
    'video_id': '59310fc0d2c8a5525345848f',
    'title': '这段爵士特别适合零基础学员学习',
    'video_tag_list': '',
    'content': "这段爵士舞特别适合零基础的学员学习，歌曲：You don't know me"
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/c266817d-9b2d2ce-8ce7-60ae166c2b02?sign=93f6a3816fba3402b92b9dcdacbeacdb&t=65fb06d4',
    'video_id': '59311bf0a9b2ed624bb327d2',
    'title': '夏日猫咪护理全攻略，原来食疗这招对猫主子也管用',
    'video_tag_list': '',
    'content': '夏天一到\n主子们的便秘、脱毛、绝育后遗症又来光顾了\n想当五星铲屎官\n除了给猫咪最全面的呵护\n你还可以给主子们换个猫粮试试\n幸福生活从吃开始\n猫咪轻松度夏就看这里～\n①\n夏季肠道问题\n【基础解决方法】如厕后喷洒除臭剂\n【深度解决方法】喂食皇家肠道舒适型成猫猫粮\n②\n夏季脱毛问题\n【基础解决方法】定期梳理毛发\n【深度解决方法】喂食皇家去毛球成猫猫粮\n③\n绝育术后护理\n【基础解决方法】喂食营养膏等补充营养\n【深度解决方法】喂食皇家绝育呵护成猫猫粮'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqxr_A0U31tg9Kqw2yoZ3AyAttCI_compress_L1',
    'video_id': '593126bbd1d3b97306bd0261',
    'title': '迟来的六一视频～',
    'video_tag_list': '宝宝日常穿搭指南',
    'content': '家附近有一个适合遛娃的码头 人少景美天气好 就算再多烦恼 有大王们的笑治愈我 怕啥尼[吧唧R] 当然啦 他们发威的时候我也只能自愈啦[笑哭R]\n#宝宝穿搭打卡[话题]##宝宝早教这么做[话题]##宝宝日常穿搭指南[话题]##小红书萌娃大赛[话题]#\n@薯宝宝  @视频薯'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/47b20e69-d0d225c-8757-30855bc5f8cc?sign=8a6a85c0ce988fff51e695ba6a117a25&t=65fb06d4',
    'video_id': '5931410634609441147cd5d3',
    'title': '拯救小糙手！如何在家做手部保湿护理',
    'video_tag_list': '',
    'content': '女生们学习工作劳累一天，手部的皮肤也一起疲惫，产生粗糙细纹。这时如果能享受一次专业的手部护理那就完美了。喵酱今天教大家，睡前只要5个步骤，在家也能轻松拥有专业的手部保湿护理哟~再也不用担心小糙手啦~#视频教你生活小窍门'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/e57a8d75c81cc15762bc8613811ce62ca8d89ad7_r_ln',
    'video_id': '5931463a7fc5b827ec3260c4',
    'title': '这么简单的自制水果软糖你有什么借口不做？',
    'video_tag_list': '',
    'content': '#水果的有趣吃法[话题]##DIY美味小零食[话题]#\n今天我来分享一款水果软糖的做法，食材和制作都非常简单，口感Q弹，一点也不硬，冰冰凉凉的特别好吃，而且想吃什么口味就做什么口味，只要换果汁就行。\n这回手残党都没有借口不做了，小朋友们都可以自己动手做糖吃了。\n我这次尝试做了三种口味，用了三种不同口味的果汁，紫色的用的是紫葡萄汁，橙色的用的是胡萝卜汁，黄色的用的是橙汁。\n如果你用吉利丁片做的话，用同样克重的量，只要先用冰水泡10分钟，然后捞出来拧干后加到温果汁里搅拌至完全融化即可，食谱里的80克饮用水就不需要了。'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/3eff0a6f-1ef81dc-bd64-29a04ed418f8?sign=c05f70024abc26047c4291bf014f73d9&t=65fb06d4',
    'video_id': '593146607fc5b8385e3260c2',
    'title': '🎂🎂小红书4⃣️岁啦！生日快乐',
    'video_tag_list': '',
    'content': '#小红书生日快乐\n让我们一起手拉手愉快的买买买！🎁  🎁\n感谢小红书让我们相遇😍  😍\n以后Nina姐姐会给大家分享更多的好物噢～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lgsjsDNWVOpC7LtBYRMKNHCf2XLJ_compress_L1',
    'video_id': '59314a8114de415f44d733f9',
    'title': '🐧超可爱的小东西——企鹅呆萌日常🐧',
    'video_tag_list': '带着小红书去旅行',
    'content': '🐧今天去悉尼水族馆看见了超呆的海牛和企鹅，还拍到小企鹅滑倒的一瞬间，笑死我了，也就看了几十遍吧。哈哈哈哈哈哈哈哈[萌萌哒R][萌萌哒R][萌萌哒R]\n#带着小红书去旅行[话题]#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/ltylJRVtdsUVtrFtF3K3OZaF7o0__compress_L1',
    'video_id': '59314d08d1d3b94ec055e0e3',
    'title': '三木三木三山三山',
    'video_tag_list': '',
    'content': '来我家的毛孩子都特别的享福，这只小基基名字叫Sunshine，和哥哥Summer都是三字辈儿的😑简称就叫三木三山啦😆\n总会有那么一只汪能让你一见钟情，想都不想就冲动的抱回家啦～会一直分享傻小子成长史给喜欢我们的朋友们哒😘'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/bd384421-4e43e95-823d-f08c06184a9c?sign=d6adaa1eb28097bf3390dc46d6b7cdd6&t=65fb06d4',
    'video_id': '59315a5e7fc5b8307a2ef4ee',
    'title': '穿吊带为何不好看|圆肩驼背怎么破？',
    'video_tag_list': '',
    'content': '“圆肩驼背”真的是颜值杀手，不管怎么瘦，只要圆肩驼背还是显得虎背熊腰没气质。圆肩驼背的成因很多，但是除了骨骼形态，90%以上的体态问题都可以后天矫正，Weiya自己就亲身经历过这些！快看本期超级实用干货视频，从理论到实践，让我们一起怒怼这个颜值“痛点”吧！八周挑战第七周，小仙女们加油！#手臂如何塑形[话题]##8周变身比基尼女神[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ll868qehVLjdWMvXcp3YRq4peZh6_compress_L1',
    'video_id': '59315b3dd2c8a51de735ab04',
    'title': '香菇来玩躲猫猫~闷儿',
    'video_tag_list': '',
    'content': '香菇比较爱玩的一个游戏~虽然我们是跟她玩的，但也经常被他突然跑出来吓一跳[笑哭R]'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/c8ead81a-1bf91a7-aba0-f0b81996598a?sign=f3ab007a32516ac9e7c66fe090cc7ed1&t=65fb06d4',
    'video_id': '59316abda9b2ed342b96de1a',
    'title': '这个宝宝的座驾超厉害！',
    'video_tag_list': '',
    'content': '#宝宝座驾我选TA[话题]# 中，来自薯妈@Warmwarm 的贡献\n她的宝宝Ariel的座驾居然是....\n一只\n苏卡达陆龟！！！\n@薯宝宝只想说，\n好。拉。风。。。\n❤ 各位薯妈，你见过最拉风/最实用/最意想不到/的宝宝座驾又是什么呢？\n写个【评论】告诉宝宝吧！~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmCwicuHX1RQemmbZR6E1R3JBmb3_compress_L1',
    'video_id': '59317d6db46c5d6517526137',
    'title': '🍠来首弹唱祝福小红书生日快乐！',
    'video_tag_list': '小红书生日快乐',
    'content': '#小红书生日快乐[话题]#\n小红书，祝你生日快乐～🎂\n第一次露声希望大家不要见笑，说的有点啰嗦，但都是真心话！\n希望小红书越办越好，下一个4年、10年、40年希望还能一起陪伴～\n爱你哟❤️'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lk0oPdGo8_vCzbrbQVqLp2B0fMDz_compress_L1',
    'video_id': '59322454b46c5d3656526136',
    'title': '丨适合新手的一个日常欧美妆容丨',
    'video_tag_list': '',
    'content': '稍微改良了一下所以可以当做很日常的妆来看 另外也比较适合新手\n雅诗兰黛的DW粉底液简直是油皮亲妈 持妆力惊人 录完视频出去拍照了一天也没有脱 最近状态不好 这款粉底的遮瑕力度也不错 我的色号是36 比较自然偏黄\n眼影用的是全哑光的大地色来叠加 眼头和眉骨的白色可以让眉眼看起来更干净\n口红也是雅诗兰黛  色号520 特别美特别正的一个颜色 而且很滋润\n喜欢的话给我点赞评论吧~ 有想要看的视频也可以给我留言 么么哒爱你们\n#日常妆容打卡[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fm1-RBZZUrY9dXF3tUvRVFRMFFDB_compress_L1',
    'video_id': '593234cbd2c8a55d57d9a596',
    'title': '我们家有一个偷u盘的小偷🐱',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '#我家宠物最萌的瞬间[话题]#你这样捣乱我怎么做毕设啊小坏蛋[叹气R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FrWOrRC4dbfW77zZ-QMBrIVO8ZW5_compress_L1',
    'video_id': '59323fdeb46c5d04c04bca14',
    'title': '十秒改变造型',
    'video_tag_list': '年度最佳造型',
    'content': '#拯救头发油腻的好东西[话题]##年度最佳造型[话题]#十秒就能改变自己 ，你还在等什么[飞吻R]现在发型师真的越来越会做头发啦[害羞R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fgx1Hv9l0I2TMJBMIxrCELc4eOLG_compress_L1',
    'video_id': '593260d6d2c8a55677e297d3',
    'title': '周末啦来挤眉弄眼😘😘',
    'video_tag_list': '',
    'content': '😘😘😘😘\n这一两个星期一直在你们的赞美中度过，我做梦都在笑。\n哈哈哈，爱你们。\n这几天深圳真的是超级热，每天都是三十几度，刚好这几天又在外头忙。😭所以你们看到视频里的我头发都汗湿了😂\n上篇分享你们问的最多的是卧蚕和头发是怎么卷的。\n我想再发一篇详细分享眼妆的，其实说起化妆我有点惭愧的，我化妆很简单，用的产品也很少，我是个看不惯自己化浓妆的人😂\n所以我会给你分享一些小技巧，最近有点忙，所以等我缓缓先吧😘\n还有头发，那个弧度是我卷了个丸子头放下来后形成的弧度。哈哈，你们也可以试试，想持久一点可以用吹风机吹吹再放下来。（先用热风吹再用冷风吹）\n[吧唧R][吧唧R][吧唧R][吧唧R]\n周末你们都在干嘛，有吃什么好吃的吗[色色R][色色R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmGAVUhuXMfBr7n4vW54jzN_Ge0U_compress_L1',
    'video_id': '5932854314de416c07793ae8',
    'title': '这 哈喇子流的 我的短腿🐔呀',
    'video_tag_list': '',
    'content': '我在吃🍒她就盯着看 一开始我没留意 后来我一转头看她……我惊呆了😂😂😂'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/6ac23ae3-7a93382-8a0c-8496e923da27?sign=73f34f958b99dfcbd553ad0404dde9a4&t=65fb06d4',
    'video_id': '593290d07fc5b847fb01c126',
    'title': '🎓要高考了，大学里的坑都是哪些专业？',
    'video_tag_list': '',
    'content': '#高考加油[话题]#\n一年一度的高考又要来啦！~视频薯这次采访了一下小红书的大嘎们大学都是什么专业。哪些专业让他们又爱又恨？到底该不该选这些专业？红书的学长学姐们亲身讲述自己的校园经历~\n同时，视频薯为即将高考的小红薯发起#高考加油，大嘎也来讲讲自己的校园生活，为他们加加油吧！\n如何参与话题活动：\n在发笔记的输入框上方，看到#就戳~搜索#高考加油 ，点击之后就能为小红薯加油打气啦！\n发布视频后别忘了@视频薯 哟！视频薯会去翻牌子哒！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/locCwFkWpmVELCTmk70EcOwGgktx_compress_L1',
    'video_id': '5932b258d2c8a52fede297d2',
    'title': '你想不到的润唇膏还有这6大妙用',
    'video_tag_list': '秋冬必备润唇膏;悦诗风吟',
    'content': '人手一支的润唇膏，还有什么其他妙用呢？一起来get把！\n妙用1 随身卸妆好物\n妙用2 搞定上妆卡粉\n妙用3 指甲倒刺\n妙用4 巧取戒指\n妙用5高跟鞋磨脚救急\n妙用6 擦鞋子\n放一下自己拍摄负责的视频新栏目，生活技能GET，希望大家喜欢~视频里面用的是insfree的润唇膏[吧唧R]\n#秋冬必备润唇膏[话题]##视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fn13xiqbrC0lK0FfI5OcoDVqpNVL_compress_L1',
    'video_id': '5932b8f414de410296f5d5cc',
    'title': '小红书6.6生日快乐！🎉🎉🎁💕🎈',
    'video_tag_list': '小红书生日快乐',
    'content': '本来是想让小奶油抱着宗主录一段的，毕竟结缘于小红书就是因为她，可惜小家伙完全不配合，一抱上宗主就去扯掉宗主的披风😓😓而且还不肯看镜头，无奈只好让宗主独自庆生了😁😁\n非常感谢小红书，让我可以记录小奶油的成长，向各位宝妈宝爸学习育儿经验，见识了更广阔的世界，祝愿小红书未来的发展越来越好哦❤❤😘😘\n@薯宝宝 #小红书生日快乐[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/ll-D2br5tf-cu3oy9SVRWK5kYKy2_compress_L1',
    'video_id': '5932cca6d1d3b971b5c8fefb',
    'title': '韩舞爵士  IU❤palette❤李知恩',
    'video_tag_list': '舞蹈表演视频;舞蹈表演视频;韩国',
    'content': '#舞蹈# 🎨#iu palette#🎨 我特别喜欢IU，可惜有舞蹈的歌不多，这次看到1M工作室的版本，♥️很喜欢这种随性的风格。分享给大家。#舞蹈表演视频[话题]##舞蹈表演视频[话题]##韩国品牌种草会[话题]##10斤减肥小目标[话题]##减肥是女人一生的事业[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lvHPUE8lmxbcz7yL_BQ1mDZunQ8j_compress_L1',
    'video_id': '59338fc6b46c5d2d032bc387',
    'title': '萌炸的奥利奥小狗狗——点点',
    'video_tag_list': '我和宠物的日常',
    'content': '出门又比平时晚了，又要让小伙伴等了🌚🌚\n谁让小狗狗那么萌！🐶\n在小区里碰到的～主人老伯伯说才2个月大！叫点点～😍😍😍\n超萌啊！肉乎乎毛茸茸的一坨～\n靠在我身边～还翻肚子给我摸了！肯定超喜欢我吧，科科～😊😊😊\n点点你真的萌炸了！\n#我和宠物的日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrRHT8g-Pzp4FMVNEuMYwsuVPvLw_compress_L1',
    'video_id': '5933ea78d1d3b946d6a8d118',
    'title': '夏季懒人健身心得体会#Rita聊天室#懒人健身#锻炼',
    'video_tag_list': '见人不如健身',
    'content': '来更新视频啦\n最近吃得很愉快 胖得很实在\n现在我是身高168 体重105[腹黑][石化][震惊L]\n争取瘦到100斤[装酷][装酷]\n我平时最爱就是吃 基本上吃得很爽快，一顿两个披萨，一顿一个全家桶什么的。\n平时在家会做Keep，之后会专门写一篇懒人练Keep的文章哈哈！有些时候会去健身房跑半小时～\n所以我不是健身狂魔 就针对懒人健身出一个心得体会啦～\n💡视频如果没声音是因为手机总开关声音键没打开～\n希望对你们有帮助！夏天一起瘦起来吧[装酷][装酷][装酷]\n#见人不如健身[话题]##零基础健身房入门[话题]#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/a93b4d9472b06e2318065e06ab522296e5b66873_v1_ln',
    'video_id': '5933fb227fc5b8349f0e6dee',
    'title': '论香蕉的循环利用！被玩儿坏的宝宝，还是萌萌哒~',
    'video_tag_list': '',
    'content': 'Q：吃完香蕉剩下的香蕉皮怎么办？\nA：可以拿来给萌娃做个香蕉帽，做个香蕉比基尼和香蕉小内内呀~！\n来自薯妈@Summer\ue305迎迎，不知道这个薯宝长大后看到这个视频会是啥表情？\nhiahia~反正本宝宝最后是被宝贝的的笑容萌化啦~\n⭐️今晚咱们就来聊一聊：\n红薯地的麻麻们都做过什么坑娃黑娃以及把娃玩儿坏的事情呐？~~~\n写评论跟@薯宝宝 和薯妈们分享吧~~\n当然啦，光靠评论说不清的麻麻们，更欢迎PO出图文和视频笔记哟～也更能萌倒@薯宝宝 和薯妈们吧！！~~~\n❤小提示~\n麻麻们晒娃时要将宝宝的隐私部位挡住哦~不要晒宝贝们的裸照吼！~'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/ljxLsZ1NCIeBELJ3eyYLsq-TuN4s_compress_L1',
    'video_id': '593405fc14de4129cc9f91b8',
    'title': '韩舞爵士舞 #IU李智恩&GD 权志龙palette#',
    'video_tag_list': '',
    'content': '大家多点赞收藏关注  我就会出慢动作教程啦～\n#舞蹈# 🎨#iu palette#🎨 我特别喜欢IU，可惜有舞蹈的歌不多，这次看到1M工作室的版本，就学了，♥️很喜欢这种随性的风格。#iu#\n这个舞蹈是非常基本的基础动作～点赞收藏就会出教程啦～想学的赶紧动动你的小手[飞吻R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FkvwpwXjuPVkB6vcfdE2C_ryOHG8',
    'video_id': '59340889d2c8a53c5cef7707',
    'title': '肚皮舞 对着镜子练正骆驼',
    'video_tag_list': '',
    'content': ''
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FqAf6l6H_JkP6rswaIaLDxsxlNKZ_compress_L1',
    'video_id': '59340cae14de4141430154fa',
    'title': 'HEFANG 热情西西里岛系列 火烈鸟耳环💐',
    'video_tag_list': 'ins上最火爆的小众配饰',
    'content': '超美的小众饰品潮牌HeFang～\n其实也不算小众了，自从周冬雨等明星戴火了就超多人开始追～\n这对满钻火烈鸟超级灵动～\n她家饰品精致又不天价，超爱～\n#首饰就要blingbling[话题]##配饰就要这么戴[话题]##国内明星同款配饰[话题]##ins上最火爆的小众配饰[话题]##晒晒我的购物车[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fg9OuZR0sqtKDzMoi11NAlQF4i52_compress_L1',
    'video_id': '59341179d2c8a54e90998971',
    'title': '小红薯们快来看#我们相爱吧❤️！',
    'video_tag_list': '',
    'content': '他是🐆还是🐱？嘻嘻嘻 今晚揭晓哦!\n端好🍿️🍭🍦准备看电视吧～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg6LavETj92we7rNyAj54Yf9kvyt_compress_L1',
    'video_id': '59341841b46c5d29b6fe4f20',
    'title': '拍摄了一部小视频，祝福小红书四周岁生日快乐！🎂🎁🎉',
    'video_tag_list': '小红书生日快乐;小红书',
    'content': '过两天就要到6月6日啦！拍摄了一部小红书生日视频小短片，刚剪辑好就赶紧发上来啦，哈哈。😜\n去年10月份的时候入驻了小红书，从分享泰国游记开始，再到分享健身穿搭美妆心得，一发不可收拾的爱上了小红书。\n正如视频中写的“女生想要变美很简单，只需要看一本书就够了！”啊哈哈哈哈，没错，那就是小红书。在小红书里可以学习到各种穿搭，美妆，护肤知识，长草好用的单品，也可以参考其他小红薯的种草笔记。在我心目中小红书就是一本神奇的百科全书，但比百科全书更好玩儿，更有意思，哈哈。\n通过小红书，我也认识了一群可爱的小红薯，大家成为了好朋友，哈哈哈，超开心的！还有每当小红薯们给我留言点赞，都很感动，也给了我继续写笔记的动力。\n最后呢，祝福小红书生日快乐，越来越好，所有的小红薯们越来越美丽哟！么么哒～😘😘😘#小红书生日快乐[话题]##生日派对这么穿[话题]##带着小红书去旅行[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lrjdHm11IeK07pRPtAKgzLv9GvWO_compress_L1',
    'video_id': '593424f2d1d3b904388c6d12',
    'title': '解决腰粗最简单粗暴有效的方法！（超实用训练视频分享）',
    'video_tag_list': '健身器械教学视频',
    'content': '腰粗？\n基因不好？\n体脂率低依旧摆脱不了直筒腰？\n不想控制饮食也不想痛苦的练腹和有氧？\n还有救吗？\n真的有奇招？\n[偷笑R][偷笑R][偷笑R][偷笑R][偷笑R][偷笑R][偷笑R][偷笑R][偷笑R][偷笑R][偷笑R][偷笑R][偷笑R][偷笑R][偷笑R][偷笑R][偷笑R]\n[鄙视R][鄙视R][鄙视R][鄙视R][鄙视R][鄙视R][鄙视R][鄙视R][鄙视R][鄙视R][鄙视R][鄙视R][鄙视R][鄙视R][鄙视R][鄙视R][鄙视R]\n[生气R][生气R][生气R][生气R][生气R][生气R][生气R][生气R][生气R][生气R][生气R][生气R][生气R][生气R][生气R][生气R][生气R]\n抱着侥幸心理点进来的宝宝要打屁股[抓狂R][抓狂R]自己面壁去\n不想控制调整好饮食搭配也不想做有氧运动 也不愿意练腹有想要小蛮腰和迷人曲线？\n不是调戏宝宝们～\n办法还真的有～\n最简单粗暴有效的方法就是—\n把背练大!\n不是开玩笑\n讲真的\n这个办法很奏效！\n决定人气质和穿衣是否有型的最主要的部位其实是背部！尤其是女生、你再瘦再高挑如果圆肩驼背头前引的话、真的是穿什么都差点感觉！\n今天不讲上交叉综合症体态的问题和理论知识（之前都具体讲过）、只分享我今天的背部训练视频！看再多理论都不如行动起来～\n今天的背部训练视频针对有一定训练基础的健身宝宝们～ 想要变的挺拔有型的可以直接开始练起来了\n动作视频里有写、重量和组数因人而异、自己根据自己的能力调整！女生塑形可以15-20RM/组 每个动作3-4组/ 男生增肌的话 6-12RM/组 每个动作3-4组\n训练视频是我个人觉得好用的动作和健身心得、只代表我的个人想法、没有绝对～大家可以去尝试、觉得好的可以直接拿去用、有不明白的可以留言我[得意R][得意R][得意R]\n#背部塑形视频[话题]##举铁P.K.瑜伽[话题]##见人不如健身[话题]##健身是把整容刀[话题]##10斤减肥小目标[话题]##厉害了我的健身房[话题]##必须要安利的健身动作[话题]##健身器械教学视频[话题]##小红书生日快乐[话题]##健身靠装备[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/7c647f21-4faac08-a624-f4b43e48d892?sign=d05b8eb90ce00f682e9418f8dcd1e042&t=65fb06d4',
    'video_id': '5934b2d27fc5b8303d0e6def',
    'title': 'WI美妆视频|气质红唇妆',
    'video_tag_list': '',
    'content': "难得拍一个带感的气质妆容，一直太清新有点无聊，配上红唇改头换貌，大家一起来看吧~\n防晒：CPB防晒隔离乳\n遮瑕：Make up forever 五色遮瑕膏、IPSA遮瑕膏\n底妆：Bobbi brown胶囊气垫4号色\n定妆：Canmake粉饼MB色\n眉笔：玻儿不期而遇眉1号\n眼影：Wet n Wild335色\n眼线：I'M meme眼线液笔\n假睫毛:淳子老师7号\n睫毛膏：熊野职人浓密款\n腮红：Canmake腮红2号色\n修容：Ponyeffect4色修容\n高光：BobbiBrown高光Pinkglow\n唇膏：阿玛尼400色\n#化妆视频##跟着视频画眼影#\n#唇膏#"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loglZ7mEf-GqLqjMOUrqr0w_ROZ__compress_L1',
    'video_id': '5934badfd1d3b9411cea58e2',
    'title': '【视频教程】刷子眉笔染眉膏 超清楚的画眉教程 麻瓜版',
    'video_tag_list': '适合新手的眉笔',
    'content': '这次再有人跟我说不会画，我真的没办法了…\n为了你萌，我昨晚学剪视频学到了三点钟…\n终于生下来这个孩子…\n用品视频里都有，步骤也有，我自认为还是比较明了的，祝仙女们都长出眉毛，我先睡了…\n呼呼呼[瞌睡][瞌睡][瞌睡]～\n#简单易上手的画眉方法[话题]##回购一生的眉笔[话题]##适合新手的眉笔[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/111b2874-3b2e38d-b052-e5a63abe591b?sign=64bf6c4fbf6d63fd6fede8eaa9adb555&t=65fb06d4',
    'video_id': '5934bfb67fc5b87d9b6c3751',
    'title': '适合夏季的开架底妆！超持久！干皮油皮都有介绍哦~',
    'video_tag_list': '轻薄底妆如何画;苏菲娜;苏菲娜 SOFINA 控油瓷效防晒隔离妆前乳;露华浓;露华浓 Revlon 24小时持久不脱色粉底液;封面女郎;封面女郎 Covergirl Ready Set Gorgeous Foundation无油清透粉底液;Canmake;Canmake 棉花糖控油粉饼 SPF26',
    'content': 'HI！这个视频是分享适合夏季使用的底妆产品哦~从粉底倒定妆产品都有，干皮油皮的都有推荐，快点夸我贴心吧！\n其实最近很多人都在问我夏季适合什么底妆，其实这个跟个人肤质有关系，因为一个人的肌肤的持妆度跟肤质有关系也跟个人有关系~所以呢，还是希望大家可以找点分装神马的试试看再做决定。\n👉油皮控油妆前乳：苏菲娜控油妆前乳👈\n这个绝对是油皮亲妈！✌如果说夏季你用什么都油腻用什么都脱妆的话，一定要试试看这款妆前乳，涂改液的质地，推开之后非常轻薄！把它涂在出油很厉害的位置就好了，后续直接去用底妆控油效果非常好哦！\n\n\n👉干皮/油皮/混合肤质：露华浓24小时不脱妆粉底液👈\n这款是非常贴心的设计，你们在购买的时候会发现有适合不同肤质使用的，都是不脱妆的设计，但是有针对干皮和油皮，所以根据自己的肤质去挑选就好了。这款最大的特点就是持久，不过不少人说有假面感，但是我觉得呢，这个跟上妆手法有关系，欧美底妆大多数有厚重感，所以最好是少量多次的叠加，不要一次性上很多底妆，湿润的海绵蛋上妆效果会更好！切记少量多次哦~这瓶对于我来说持妆大概可以到8到10小时~不过我也是个不容易脱妆的人~这瓶也是兰蔻24小时持妆粉底液的替代品哦~\n\n\n👉油皮亲妈粉底液：covergirl封面女孩粉底液👈\n这个粉底液是无油型的，所以讲真非常适合油皮来用，质感有点奇妙，但是用起来真的觉得脸上超级无敌的丝滑！有时候不得不佩服开架品牌！做的真心很好。这个是乳霜的质地，其实可以直接用手来上妆了！！！很哑光的感觉！！！不过干皮真的不要来尝试，会哭泣！\n\n\n👉各种肤质只要你皮肤好：CANMAKE棉花糖粉饼👈\n这个我之前的粉饼合集也写过一次，反正只要是皮肤状态好，用这个真的有一种磨皮之后的效果，超级无敌美啊！但是肌肤状态不好可能会卡粉，所以如果你皮肤好，无论是什么肤质，用这个都很好！\n\n\n👉沙漠干皮适合：Tonymoly保湿定妆喷雾👈\n如果说沙漠皮到了夏季还是很干，用不了粉状的底妆产品，不如试试看这个定妆喷雾，喷一下就能够很好的达到定妆效果，而且能够让肌肤看起来有光泽感。如果觉得底妆不够服帖，用这个喷一下之后再用粉扑按压一下就好啦~总之这个绝对是干皮的救星！！！\n希望这个视频能够帮到大家呀~\n评论区请和谐的相互种草！\n谢谢观看！\n#我最爱的平价彩妆品牌[话题]#\n#平价好用的底妆产品[话题]#\n#完美底妆这样画[话题]#\n#轻薄底妆如何画[话题]#\n#夏日缤纷妆容色[话题]#\n#粉底持久度大比拼[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/854x480/vcodec/libx264/pgc/1b6ae78d-1bd747a-9217-7cb55af75b22?sign=f5b68dec197b9e824fba6e5c0152b093&t=65fb06d4',
    'video_id': '5934c0457fc5b834ee0e6dec',
    'title': '我要变学霸 | 一个月GMAT从580到720经验分享 | 10 Tips',
    'video_tag_list': '',
    'content': 'GMAT是美国、英国等国家的商学院研究生入学考试。这支视频是一个全新的主题“我要变学霸”，我想给大家分享我的学习经验，接下来我准备做的3个学习相关的主题（在视频开始的时候说啦）如果有什么别的想看的也可以留言告诉我！\n10个Tips：设定一个很高的目标；安排足够的准备时间；留出至少一周的全职考前突击；看论坛；不要盲目跟风 根据你自己最有效的学习方式去选择资料；单词是一切的基础；OG是最重要最重要最重要的复习资料；做一遍OG后半裸考一次 感受考场氛围和题量；运动和体力的训练；毅力和信念\n祝备考的小伙伴考试顺利，早日达到你的目标！！！\n@视频薯  @生活薯  @薯博士'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lhKgLprOGM5I_S3MnQQgjtVAlHn7_compress_L1',
    'video_id': '5934cea9b46c5d268ffe4f16',
    'title': '福建人太会吃了，番茄蛋汤也能做出山珍海味！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n海葵，我们这边叫它是海础子，它散开像一朵花很漂亮，它是一种无脊椎没有骨骼的动物生长在岩石活珊瑚上。\n海葵很鲜很有营养，很喜欢吃这个东西， 有人说吃它还能治疗痔疮呢，当然这是土方子，不过听说还真有吃好了的呢。\n★★★★★\n创意指数\n海葵鸡蛋汤\n▼\n海葵鸡蛋汤\n·视频音乐·\n伍々慧 - 約束の海\n·食材·\n海葵、番茄、芹菜、洋葱\n葱、鸡蛋、料酒\n胡椒粉、糖、盐、醋\n1.海葵切半备用\n2.撒入少许盐，用手抓匀\n3.腌制10分钟后，过清水用手洗去表面粘膜\n4.鸡蛋打匀备用\n5.西红柿切块、洋葱切丝、芹菜切段、葱切段\n6.热油锅炒香辣椒、洋葱\n7.倒入一碗热水\n8.倒入适量盐、1勺料酒、1茶匙糖、少许醋\n9.倒入西红柿煮沸，再倒入鸡蛋液\n10.勾芡拔匀\n11.倒入芹菜段、葱段提香\n12.倒入切好的海葵，煮至沸腾关火盛出\n13.撒上少许胡椒粉即可享用~！\n小贴士\n1.海葵要用盐腌制去腥味\n2.腌制后的海葵用清水洗净去除粘膜\n3.喜欢吃喝汤的朋友，当汤煮沸时倒入鸡蛋液顺时针搅拌，蛋液就会融入汤中\n#我的煲汤秘籍[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/2563853081318ad75d42ab34528b6359841f4274_v1_ln',
    'video_id': '5934d171b46c5d2c11fe4f1a',
    'title': '前段时间特别火的凉凉，动作简单大家都可以学',
    'video_tag_list': '',
    'content': '不是专业科班出身，跳的比较接地气，动作简单没有技巧，大家可以学习学习。有些动作借用了大师的，勿喷'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/d536d71b8a9b4415daf3a4b37812b997ccddac94_v1_ln',
    'video_id': '5934de9214de410a63015501',
    'title': '希望看完视频我们还是好朋友😃',
    'video_tag_list': '',
    'content': '突然翻出来这个视频，是想效仿哪吒头出个教程，一不小心走偏了 🌝🌝'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/01e248089c2036d4018370037feed56e28_259.mp4',
    'video_id': '5934df6f14de4109609f91b6',
    'title': '天空之镜',
    'video_tag_list': '用视频记录旅行',
    'content': '世界上真的有这样一个地方，放眼望去你根本分不清哪里是天哪里是地。\n视频来自 @潇2⃣️妹💓 ，她参与了话题#用视频记录旅行[话题]#\n有机智的小红薯认出这是哪里吗？'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lvIZ5bdR09IVuS35pU79-aCJxMAL_compress_L1',
    'video_id': '5934ea2bd2c8a50c191e749e',
    'title': '【视频】视频教你画上镜底妆 遮瑕粉底修容高光一步到位',
    'video_tag_list': '视频教你画底妆;NYX 遮瑕3C修容盘;Tarte;RCMA;Hourglass;Hourglass  腮红高光五色限量面部盘',
    'content': '#视频教你画底妆[话题]##完美底妆这样画[话题]#   @视频薯\n最流行的完美轮廓清晰底妆大法在此⬇️\n之前视频发过：《修容遮瑕到底怎么用》\n《黑眼圈到底怎么遮》\n《眼周干燥怎样上妆》\n等关于底妆类的视频。很多仙女问底妆的步骤先后。今天把整个顺序排列录制出来。方便大家学习。[喜欢]\n步骤：\n1⃣️遮瑕修颜\n2⃣️粉底\n3⃣️局部遮瑕提亮 tarte海洋森林系列 遮瑕液\n4⃣️散粉定妆 \n5⃣️修容（粉质修容）\n6⃣️高光（粉质高光）\ntip：若使用膏妆或液体质地 修容和高光，在完成修容 高光后再进行散粉定妆。避免妆面斑驳。\n-----------------------------------------------------------\n我：热爱色彩小魔人，偏爱欧美妆。\n我：拒绝乌合盲从，拒绝用奢侈彰显品味。\n我：我相信用心学习，就是掌握各种美的诀窍最佳途径。\n我：希望世界上每一个女孩都首先接纳本来的自己，热情拥抱变化的到来。用你的眼界、思维、创造力、和热情享受让自己越来越好的过程。生活需要有态度，美也要感受内心。\nAdora都会把我长期（辛勤的成果）搜集来的新奇好物推荐出来给各位仙女们一起变美[喜欢]\n【本人禀着三条】：\n1优质！优质！优质！不买最贵，只买最好！\n2新奇！新概念、新设计、新潮流的个性主张\n3我们关心性价比！荷包是自己的[活力]价格要配得上品质才像话。也会分享给大家最实惠的购买方式-----------'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/5baeb0f2-d93564f-8d9b-eb93f84578cb?sign=6e8919466ab400d8579a6110ab8e345e&t=65fb06d4',
    'video_id': '593506777fc5b81f25b032e9',
    'title': '夏日驱蚊产品强势攻略！',
    'video_tag_list': '',
    'content': '有了这些，小妖精们再也不怕被蚊虫叮咬啦！\n#驱蚊大作战[话题]##我的驱蚊神器[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ae81ae8867c1c9b8915b686c0f82a15af84a0f81_v1_ln',
    'video_id': '59351caa7fc5b8136bb032ed',
    'title': '免烤奥利奥芝士蛋糕，不需要烤箱，简单几步就可以做好',
    'video_tag_list': '',
    'content': '今天我来分享一款免烤奥利奥芝士蛋糕的做法，不需要烤箱，简单几步就可以做好，食材也不复杂，而且还很好吃呢！\n做好的芝士蛋糕可以放在冰箱的保鲜层冷藏保存，想吃的时候直接从冰箱里拿出来就可以吃，口感不甜不腻，冰冰凉凉的感觉，特别适合即将到来的夏天享用。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/e871a3e28ff3470ab91e80f72bdeea1b51ae679c_r',
    'video_id': '593535ad7fc5b86dd51eadc9',
    'title': '冰激凌冻的太硬舀不起来怎么办？学会一招，轻松享受美食！',
    'video_tag_list': '',
    'content': '夏天喜欢吃冰激凌，在冰箱里囤积了好多。时间放久了，冰激凌杯的表面冻上了一层霜，被冻的硬邦邦，很难快速享受到美味怎么办呢？ 这次喵招教大家只要事先做一步，就能防止冰激凌被冻过硬咯！#视频教你生活小窍门'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/e4764446-2c59798-98f5-a188aa9668da?sign=5d92fd6f968c24899af5cd3164d4d0be&t=65fb06d4',
    'video_id': '59353e687fc5b86dd31eadcd',
    'title': '关于减肚子的谎言，科学和终极建议|史上最良心的减肚子视频',
    'video_tag_list': '',
    'content': '这期我们终于要说说如何“减肚子上的肥肉”了，这是大家最关心的话题，也是误区最多的。什么动作能减肚子上的肥肉？等等，如果我告诉你，肚子上的肉练卷腹或者平板是减不下去的呢？如果我还告诉你，就算完全不练腹部，做到视频里的这件事，你也会轻松拥有平坦的小腹呢？快来看看Weiya与Giselle为你揭开关于减肚子的谎言，科学和终极建议吧！想看视频首发？请一定关注我们的同名全平台“fit4life健身玉美食“哦！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lk39Zvs5nFr3PdVOWdbGdpFwHtWd_compress_L1',
    'video_id': '59355953b46c5d28742493d2',
    'title': '帮妈做家务的乖大王(o^^o)',
    'video_tag_list': '宝宝早教这么做',
    'content': '最近迷上了收纳 我家衣帽间的衣柜设计不太合理 买了塑料抽屉回家改善一下 立马变出双倍空间来[赞R]\n宝宝看到我擦柜子 也帮着一起擦 安逸啊[得意R]养了两个小童工 为娘可以歇一会儿了[萌萌哒R]\n#小红书萌娃大赛[话题]##小红书生日快乐[话题]##收纳神器[话题]##我是收纳狂[话题]##宝宝早教这么做[话题]##宝宝穿搭打卡[话题]##宝宝日常穿搭指南[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljSl0p9ExkewvFf-8qHJ-QgjT96X_compress_L1',
    'video_id': '59356407d2c8a5517057fbac',
    'title': '三木木家',
    'video_tag_list': '',
    'content': '小儿子三山，和两个大哥哥一起拍了室内写真，期待精修赶紧出来，we are big family😘\n几小只拍照的配合程度也真是让麻麻欣慰。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liHmvAHBtDJJ4d6TxTlzu3WFu-4W_compress_L1',
    'video_id': '5935655e14de410de9726858',
    'title': '歌王献唱🎤',
    'video_tag_list': '小红书生日快乐;森永制果  儿童加钙小馒头',
    'content': '我携二傻子来祝小红书生日快乐啦🎂\n感谢在这里遇到的好物，感谢喜欢我家老大老二和小三小四的你们😊\n我有一张30元薯券，打算换成小胖最爱的小馒头和你们分享😜老规矩，点赞或评论的粉丝里选一个😌\n#小红书生日快乐[话题]#\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnH31ZLx0dFAnGcWtzaZJ8tQKZvz_compress_L1',
    'video_id': '59357f1d14de4150c072685e',
    'title': '咖喱咖喱~送给大家~',
    'video_tag_list': '',
    'content': '😘😘😘'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhbZl1HgseYA5GyPHIwdR8RBcX4p_compress_L1',
    'video_id': '59357f2a14de41564d91dc16',
    'title': '',
    'video_tag_list': '生日蛋糕晒一晒',
    'content': '#生日蛋糕晒一晒[话题]#没错这就是蛋糕！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmVtwmIdy7oXIn9kRCvvi7z6aOsI_compress_L1',
    'video_id': '59357f7ad2c8a51a95e1d8fc',
    'title': '就是蛋糕！',
    'video_tag_list': '',
    'content': '没错这就是蛋糕！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llH0Jpo4wF86YjIeDIehwdKjI8OJ_compress_L1',
    'video_id': '5935c6de14de412b15726872',
    'title': '三木木家',
    'video_tag_list': '',
    'content': '熬夜做蛋糕，今天有三个小朋友过生日，家里的三个宝宝也跟着搓了一整个蛋糕，凌晨吃蛋糕是不是太幸福了呀😜'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fu84K2cUHjWSJjOgdeNIxvFwc-8M_compress_L1',
    'video_id': '59360212d1d3b920529e6970',
    'title': '[6•6周年庆大促]全世界都在刷小红书',
    'video_tag_list': '',
    'content': 'Hello world!\n小红书周年庆正式拉开帷幕啦！🎊🎊\n你们的购物车都填满了吗？视频里是全球刷小红书的动态哦～视频薯也是看得心潮澎湃[色色R][色色R]\n[赞R]红薯们都打算抢点啥呢？快点在评论里告诉视频薯吧！\n#小红书生日快乐[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/lldZ9lW07nVIKJ977sTgRISHpz7t?sign=4a0bbca9a32fd0a453ac87a449cfdbd6&t=65fb06d4',
    'video_id': '593605ae14de414d22726859',
    'title': '一分钟贴底教程',
    'video_tag_list': '就爱DIY',
    'content': '@Bunny95 小公主买了新鞋叫我帮她贴底，顺便录个视频分享给大家。\n真皮鞋底不耐磨，所以一般都需要贴底，自己动手还是挺简单。3M鞋底磨网上都有的卖，搜一搜就有了。\n话不多说直接看视频吧。\n#就爱DIY[话题]#\n#鞋控の日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lj1SDh3TFW00G31YK5Xtvt0hR6Ff_compress_L1',
    'video_id': '5936293bd2c8a5407a57fbc1',
    'title': '这样做的土豆片太好吃了，连老外都赞不绝口！',
    'video_tag_list': '麻辣土豆片',
    'content': '★★★★★\n小圆食记\nMenu\n一道普通的家常菜，搬到大饭店里，价格也开始水涨船高！\n一碗牛肉炒饭在外面能卖到好几十元，何况一盘孜然土豆片了！暴力啊!\n★★★★★\n创意指数\n孜然土豆片\n▼\n孜然土豆片\n·视频音乐·\n徐梦圆 - China-O\n·食材·\n土豆、孜然、辣椒粉\n白芝麻、葱、豆瓣酱\n老抽、盐、清水\n1.土豆洗净去皮\n2.切成同等厚薄片备用\n3.热锅冷油下豆瓣酱\n4.豆瓣酱炒出红油后，倒入土豆片炒匀\n5.倒入少许清水，防止土豆片粘锅\n6.撒入适量盐、老抽，翻炒片刻\n7.撒入适量辣椒粉、孜然、白芝麻\n8.大火炒匀盛出\n9.撒上葱花即可上桌~！\n小贴士\n1.炒土豆片时，加少许清水防止粘锅\n#麻辣土豆片[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/c4f8d1a38ad7b1a420d2f00221d1723234263e64?sign=57132111c4258f4e832a013ebe4068d7&t=65fb06d4',
    'video_id': '59363ec614de4168b872685c',
    'title': '幸福感小家电🌸催眠加湿器MUJI无印良品香薰灯',
    'video_tag_list': 'Florihana 超声波香薰灯;无印良品 MUJI 超声波香薰灯精油套装',
    'content': '让生活更美好的小家电\n这款无印良品的香薰灯应该很多人推荐过了。\n\n我放小视频就是推荐给大家看看他有多催眠😂下面详细讲\n1️⃣加湿功能\n因为这款是中号，加湿范围很小，作用不算太大。但是我出门旅游出差都会带着他，因为第二天要化妆的话皮肤太干燥就比较麻烦，住酒店的时候放在床头加湿还是会起到一定效果。体积小，也很容易就可以收在行李箱里。\n2️⃣香薰功能\n用MUJI的自带精油味道很棒，淡香不刺鼻，有多种味道功效选择。不过我是那种比起味道，环境更影响睡眠的人。助眠味道没什么体会，不过味道确实让人心情好。屋子里也都香香的，特别适合女孩子。\n3️⃣小夜灯\n因为比较怕黑，关灯晚上会睡不着。不关灯又太亮了刺眼睡不着，所以小夜灯很必要。MUJI的这款夜灯有两个等级的亮度，光线非常催眠哈哈，也很舒服。推荐~\n[萌萌哒R]如果被我安利了，记得点个赞哦。\n\n幸福感爆棚的家电 宿舍专用小家电'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/cc03c489-a9d61e3-9964-5ab933fe486a?sign=11ce6978f6c2235201022b08c1c01432&t=65fb06d4',
    'video_id': '59364d327fc5b84dd0df7027',
    'title': '金枪鱼披萨，味道鲜美，馅料十足',
    'video_tag_list': '',
    'content': '今天我来分享一款金枪鱼披萨的做法，我做了六小一大，大的大人们吃，小的给孩子吃再好不过了。\n烤好的金枪鱼披萨味道鲜美，馅料十足，而且小披萨小巧玲珑，外观非常可爱，小朋友们一定很喜欢，还非常适合外出携带。\n#跟着视频学做菜[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/adb1439666a7ca913eb924aa5031e7131edf25f3_r_ln',
    'video_id': '59365d307fc5b84a0cdf7096',
    'title': '简单易学的编发教程，还怕做不了小仙女？',
    'video_tag_list': '',
    'content': '日渐时尚潮流化的当下\n爱美的女生们\n怎能允许自己做个土妞呢？\n只是如何打理头发才会时尚更显年轻呢？\n一直换发型，担心头发受损\n编发既可以满足换发型的心\n又不会伤到头发\n跟着我学起来~\n今天要教大家的就非常简单易学\n不用担心早上不够时间打理头发\n5分钟搞定蓬头乱发\n今天就由我来教大家编头发~\n编发所需用件\n皮筋，发夹，梳子\n1.第一款:\n先用一根小皮筋\n把头顶上的一部分头发扎成一个马尾\n在扎的地方挖一个小洞\n然后把我们的马尾塞进去\n2.第二款:\n跟第一款造型一样的步骤\n我们的第二个马尾\n也是扎在第一个马尾的上面\n但是呢\n要与第一个马尾保持一段距离\n以此类推\n最后我们在第三个马尾处\n用一根皮筋把它全部扎起来就可以了\n3.第三款:\n先在头顶处扎一个马尾\n扎马尾的时候长刘海可以作为自己装饰门面\n尤其是笑得多的姑娘们\n不用担心笑起来颧骨突出啦\n在这里呢教给大家一个小妙招\n我们可以用两根发夹\n在我们绑马尾的地方固定一下\n以此类推\n我们将中间部分的头发\n紧挨着放在之前的马尾上面扎起来\n跟上面一样在中间挖一个小洞\n把我们的马尾塞进去就完成了\n4.第四款\n跟第三款一样先扎一个马尾\n用一根皮筋在马尾3/1处固定一下\n再在中间挖一个小洞\n把我们的马尾塞进去\n以此类推\n最后随意的搭配一个发箍就可以啦~\n5.第五款：\n先将头发疏通\n把头发全部放在肩部的一边\n随意的分成3股\n变成3个小辫子\n再将3个小辫子编成大辫子\n最后用皮筋固定住就完成啦\n6.第六款:\n接着第五款的编发把辫子卷起来\n卷成一个短发的造型\n最后用发夹把它固定住就完成啦\n7.第七款：\n现在头顶处抓一小撮头发\n用皮筋把它绑成一个丸子头\n抓松一些就完成啦~\n这次教学的编发是不是灰常简单？\n都学会了嘛？'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsadPyMDD5xMnT1-Tb2zlro5Uoxi_compress_L1',
    'video_id': '59365f11d2c8a5599ae1d8fe',
    'title': '必听歌曲♬ 《我的一个道姑朋友》一首很好听的古风歌曲~',
    'video_tag_list': '',
    'content': '弹唱:趣弹音乐羊可爱  uncle周'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/1809532e-062af45-b121-72b5d43e9a7f?sign=4e9c3c3f79a5785b8924eb77decb4619&t=65fb06d4',
    'video_id': '593667347fc5b825e41eaddc',
    'title': '迪丽热巴仿妆！你们看看像不像~',
    'video_tag_list': '创意仿妆秀',
    'content': '#创意仿妆秀[话题]##明星仿妆我最像[话题]#\n1.皇后薏仁水\n2.heynature水珠亮泽啫喱打底\n3.banila primer blur妆前珠光乳\n4.美宝莲fit me粉底液\n5.美宝莲fit me遮瑕液笔\n6.爱丽小屋play101双头修容棒\n7.dior散粉\n8.canmake眼影#11\n9.tonymoly 眼线膏笔\n10.大创Daiso肉色双眼皮贴\n11.dolly wink假睫毛\n12.miche bloomin双头眉笔\n13.heelaa炫彩口红#02\n当当当就这样完成了，仙女们有没有感觉到像胖迪呢？\n视频，纯属娱乐，不喜勿喷哈~~'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/640x360/vcodec/libx264/pgc/ffdd5422-da945d7-9210-ff9eecc749ee?sign=081163ec04de1ee1638f301e6588e7fd&t=65fb06d4',
    'video_id': '59366d667fc5b81270df702c',
    'title': '一个人毁掉一部戏，说的正是他',
    'video_tag_list': '',
    'content': '姥姥姥爷们好呀，这里是前女友吐槽小剧场，泥石流颁奖典礼转播现在开始啦。\n让我们来一起见证，在历史的洪流中，有哪些演员们创造出一批批经典角色，以一己之力，毁了一部作品的口碑、收视率，甚至剧情走向。'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/16ead1e7-e2463f5-a63c-008af2c0da2b?sign=6c0087468a6078b41e20b914436d2f23&t=65fb06d4',
    'video_id': '5936708c7fc5b839661eae59',
    'title': '夏天是个藏不住肉的季节，教你几招甩掉拜拜肉！',
    'video_tag_list': '',
    'content': '如果你经常使用火辣健身App进行训练，那么你一定记得训练视频中穿着红色紧身裤的美女教练，她叫冉冉。今天她换了一身衣服，来和你分享一组训练手臂的动作，帮你消除拜拜肉，打造紧致美臂！更丰富更完整的训练计划欢迎下载「火辣健身app」，或者微信关注「火辣健身」。#练出马甲线#减肥##健身##拜拜肉#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsBlKT-2lJ1GP5BOEL4rY3mV4oSI_compress_L1',
    'video_id': '59367e6ad1d3b919ba489a4b',
    'title': '我最爱的首饰  Apm Monaco',
    'video_tag_list': '首饰就要blingbling;apm MONACO',
    'content': '#首饰就要blingbling[话题]#真的超喜欢它家的 当代设计风格，还带着一丝优雅的摩洛哥气息 ～  apm 真的特别适合女生 ，款式多  风格齐全，任何场合的首饰都能选到， 好看 不失优雅 也不会掉档次，关键 性价比还高～ 哈哈 推荐\n[笑哭R]由于专柜不卖样品，我选的尾戒 正在向我奔波的路上…\n购于：上海 芮欧百货  三楼 Apm Monaco 专柜\n#首饰就要blingbling[话题]##耳钉[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/76f1829348ef0e1077717093ada9324fce1ba48e_r_ln',
    'video_id': '59367ea8d1d3b919ba489a4d',
    'title': 'Happy birthday to 小红书——王智',
    'video_tag_list': '小红书生日快乐',
    'content': 'hi all～很开心能在小红书生日这一天加入到这个大家庭当中❤️祝小红书越来越红📕最近在广州拍摄新的电影🎬刚收工回到酒店🌼先和大家打个招呼🤗希望各位小红薯们常来玩哟💋💋#小红书生日快乐[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsjBIW1hMNQdZOzXp3JjW7Sv7Lap_compress_L1',
    'video_id': '59368930d1d3b93652489a59',
    'title': '【 你的剃毛刀长大了吗？ 】',
    'video_tag_list': '雅萌;雅萌 YA-MAN 剃脱两用激光脱毛仪 STA-189P;脱毛好物排行榜',
    'content': '脱毛仪的视频来啦～\n先跟大家交代一下我的肤质状况，因为我皮肤比较敏感而且又很怕痛，所以对于身体脱毛的话，我非常不喜欢用脱毛膏以及蜜蜡脱毛。\n我个人比较喜欢用剃毛刀，因为它很方便嘛。\n前前后后也买过不少剃毛刀，所以今天就来讲讲我目前手头上有的一些产品。\n首先就是最基础的这种脱毛刀，但是这种算是还不错的，因为它上面有一块小肥皂，这个就可以在脱毛的过程中稍微有一些润滑的效果，但是也微乎其微，它是一袋里有三把，小肥皂用完就需要换一个的类型。\n这个一开始也是能满足我的要求的，但是后来换掉它的原因就是它真的非常容易刮破肌肤，而且它刀头很小嘛，特别麻烦。\n我就换了这个比较安全的电动剃毛器。这个刀头外面有一层安全网，真的不会伤害肌肤。\n但是特别特别容易坏，它是更换电池的设计，我记得就用过一个月吧，他就完全没办法再启动了。\n所以我后来还是换回了脱毛刀。\n这个应该是现在市面上最为普遍的一种剃毛刀了，跟刚刚这个比起来，刀头外面有一大圈肥皂，我用这个真的没刮破过肌肤，而且也不需要再借助沐浴露，我觉得应该算是剃毛刀当中特别方便的产品了。\n但是上面的这三种剃毛刀都有一个通病，就是维持时间很短，基本上过两天就需要重新脱毛，而且摸起来会有刺刺的感觉。\n所以我后来就开始买家用脱毛仪。\n我之前其实也有用过另一个牌子的脱毛仪，因为我妈觉得特别好用，所以她就拿走了。\n然后我自己就重新买了yaman的脱毛仪。\n选这个牌子因为他家美容仪做的非常专业嘛，还有一个很重要的原因就是这部仪器带有剃毛刀功能。\n📎\n它特别贴心的是有三种护理头。\n其实一开始使用这个脱毛仪也是心里有些害怕的，因为我之前去医院做过脱唇毛嘛，可能机器强度太大，所以过程真的蛮痛的。\n我算是痛感很强的人了，但是用这部机器真的不痛，就很适合自己在家使用。\n这款仪器是彩光脱毛的方式，它的光波深入毛囊之后可以去除黑色素。\n有嫩肤效果，所以不用担心去除毛发之后这块皮肤会变得有些暗沉。\n使毛发再生长的速度变慢，而且会越来越稀少，长期使用可以达到一个持久脱毛的效果。\n我是连用10天再停用4天，这样一直坚持下去使用的。\n📎\n具体使用方法看视频以及单独发的图文笔记吧。\n\n\n#美容仪体验报告[话题]##脱毛好物排行榜[话题]#\n#身体护理全靠TA[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lt1juu150dbXAtMdYJbvwvCCDiFi_compress_L1',
    'video_id': '59368c99d2c8a55c869eadb6',
    'title': '一条只知道奔跑的短腿柯基',
    'video_tag_list': '',
    'content': '一门心思只知道奔跑的胖柯基😂😂'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/4fd2e403ba10a1690b35852b04f70d68708dff5d_v1_ln',
    'video_id': '5936a1a6b46c5d38082d029f',
    'title': '关于我的短发打理心得✔️ 蓬松自然易学简单快速!',
    'video_tag_list': '',
    'content': '你们好呀 今天给你们带来我的短发打理方法 之前有些人问我我的头发是怎么打理的 其实真的很简单 除了剪发 我很少去理发店吹头发洗头什么的 全都是自己来的  快看 哈哈哈哈 今天就这么随意发啦 下次出美妆的 我会用相机好好剪完分享给你们 爱你们哟[飞吻R]\n[飞吻R][飞吻R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llGNxkWxg1Np87QPIo_jQlx_wV8g_compress_L1',
    'video_id': '5936cb7c14de417b1fdb3f83',
    'title': '宠物篇～隔壁老王家的布偶猫🐱布偶届的一股清泉，真面目曝光～',
    'video_tag_list': '我家宠物最萌的瞬间',
    'content': '布偶脾气好得要命，随便抱随便撸不生气，\n和其他猫比起来还是比较亲人的～\n洗澡被吹风机吓死，死死抱住杆子默默流泪都不会去抓人😘\n但此胖砸懒🉐️要命，只会因为肉干奔跑🙄️，\n偶尔对逗猫棒有兴趣，\n看到最后哦，露出狰狞面目了😂\n#我和宠物的日常[话题]##我家宠物最萌的瞬间[话题]##猫奴必备猫玩具[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lp3qCkK3xiBeLXjSO6Vtwv-R2COJ_compress_L1',
    'video_id': '5936dd68d1d3b92d8d71ac5c',
    'title': '猫咪🐈被扔N件衣服竟然不跑开还如此淡定！我惊呆了',
    'video_tag_list': '小红书生日快乐',
    'content': '#我和宠物的日常[话题]#每天换着法子把住子玩坏😀家里有主子的大家可以试试哦！\n对啦 米牙 协家里两位喵主子祝福小红书 生日快乐！今天买了好多东西价格很棒！品质更无需要怀疑✌️\n#小红书生日快乐[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/a5fe41b778b82594d602aa7a33fe123854d73bf3_r_ln',
    'video_id': '59375c6a14de41123c505379',
    'title': '徒手健身| 不靠健身器材也能练出好身材',
    'video_tag_list': '见人不如健身',
    'content': '文字版写在这里啦！\n一、后交叉步蹲起\n瘦大腿和臀部\n建议做4到6组，每组交替20次。\n注意事项：\n上身挺直，腰部收紧，重心要在前腿，站起来的时候要把支撑侧臀部收紧。\n二，俄罗斯转体\n瘦腹部\n初练者建议先徒手做两周左右，之后一手呐一个矿泉水瓶，每次做40次左右就可以了。\n注意事项：\n把背挺直，身体后倾大概45度，腹部收紧。\n三，平板支撑\n瘦腹部\n初练者建议做静态，有训练基础的可以做动态，做三十秒休三十秒，一共四到六组。\n注意事项：\n腹部收紧，臀部收紧，身体呈平板状态，腰部不要下沉。\n四，肘对膝➕高抬腿（不前面难度大）\n全身减脂，提高心肺功能\n肘对膝每侧各做十次➕十五秒高抬腿，每次做4-6组，每组中间休息1分钟\n注意事项：\n肘对膝，腿部尽量后伸，保持身体直立，腹部收紧。起身时身体保持稳定，尽量抬高膝盖找肘，呼气。\n高抬腿，速度要快，大腿尽量抬高，保持匀速呼吸。\n好啦！今天就讲这些吧！\n【衣服：kisskissyaya】\n#健身靠装备[话题]##见人不如健身[话题]##健身是把整容刀[话题]##健身穿什么[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg3DX2OxgdhCQOhEi3Cah8RQaCLD_compress_L1',
    'video_id': '59376bd3d1d3b9631d489a4a',
    'title': 'momax摩米士手机麦克风',
    'video_tag_list': '摩米士 momax mini手机录音麦克风',
    'content': '[飞吻R]哈喽，大家好，我是momax小摩，手机视频直播、短视频越来越🔥，momax顺势推出了可以满足常规手机录音需求的便携式麦克风。\n如果对手机自带麦克风效果不满意，或者在没有充足预算购买专业级录音机的情况下，使用智能手机+便携式麦克风当录音机也是非常不错的选择[赞R]。\nmomax便携式麦克风为驻极体电容麦克风，全金属机身，采用镀金处理的3.5mm四段式接头，机身主体长约6.8cm，重量仅14g，整体感觉迷你小巧，像是一支口红，带在身上不会感觉到有负担，它不需要电池，也不用app，将麦克风插入手机的耳机接口，在录音/拍摄视频时就可以直接使用啦。[飞吻R]\n当采用其进行录音时，便携式麦克风的心型指向可以过滤绝大部分不需要的背景噪声，从而获得不错的拾音效果，搭配有一个黑色的防喷海绵套，即使在户外，也能取得较好的防风效果。[赞R][赞R][赞R]\n对于常用手机进行录音/视频拍摄的各位小红薯，可以随身携带一支，随时能将小红薯的手机变成一支心型指向麦。😊\n'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lmgXA-gBIDuWV7z4WI6atQLAFi-x_compress_L1',
    'video_id': '593773c1d2c8a51d669eadc8',
    'title': '夏日消暑好物🏖dimo小风扇',
    'video_tag_list': '夏天必备小风扇',
    'content': '夏天太热啦！出门必备一个快速降温的小风扇～\n这款超可爱的便携式小风扇，嫩粉、鹅黄、深蓝三个颜色每个都超级美～超级小清新的颜色～还送了一堆超级可爱的贴纸供diy～配色太美啦！\n一共3档风速可任意调节，平放着或者拿着都可以，吹风声音很小但风力强大，降温速度超快！～这个是充电的哦，2500毫安的电池～充电90分钟续航10小时～\n然后这个品牌的售后也做得很不错，一年内机器有问题，直接换新！换新！换新！\n#夏日消暑用什么[话题]##夏天必备小风扇[话题]##提升幸福感的家居小物[话题]##防暑给力的电风扇[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkGFru2Tz4YW1SpYmV3TYJpumqwl_compress_L1',
    'video_id': '593778a6d2c8a546a61cbfae',
    'title': '高考来临食欲不佳怎么办，这碗面瞬间让你精神百倍！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n橄榄菜：性平;味甘、酸、微涩;入肺、胃经。 【功效主治】消肿利咽，生津解毒。\n我也经历了高考其实不用把高考看的那么的紧张饮食方面建议就想平时那样饮食，只是多注意下饮食平衡就行。\n★★★★★\n创意指数\n橄榄菜拌面\n▼\n橄榄菜拌面\n·视频音乐·\nOwl City - Vanilla Twilight\n·食材·\n肉末、橄榄菜、小米椒、四季豆\n挂面、葱、姜、料酒\n生抽、蚝油、盐\n1.四季豆洗净，摘取两头去茎\n2.四季豆切成小粒\n3.沸水下锅焯水后，捞出泡入冰水沥干备用\n4.肉末倒入1勺料酒，1茶匙盐拌匀\n5.热锅冷油下姜末\n6.炒香后依次倒入肉末，四季豆粒，小米椒，橄榄菜清炒\n7.倒入一勺生抽，1茶匙耗油炒匀盛出\n8.油锅下葱段\n9.沥出葱油盛盘备用\n10.葱油加入1勺生抽拌匀\n11.沸水煮熟挂面\n12.碗底倒入1大勺葱油，将煮好的挂面捞入碗中\n13.铺满浇头，少许香葱\n14.吃的时候从碗底拌开即可\n小贴士\n1.四季豆焯水后入冰水口感会变脆\n2.煮挂面时用筷子不停拌开，防止粘底\n#面条的花式做法[话题]##复习迎考吃什么[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/4ccaa424-fe0c87c-8aa5-5a80807be856?sign=a55a1bf79d635b81a205dfdb0ae56666&t=65fb06d4',
    'video_id': '59377f207fc5b81ea25557f0',
    'title': '20%的宝宝会“留级”？ 产科医生帮你“跳级”毕业',
    'video_tag_list': '',
    'content': '预产期到了，但不是每一个妈妈都会生宝宝的，有些妈妈到了39周、40周还是完全没有动静。不光是妈妈着急，其他家里人也跟着着急。今天的视频就是来和大家探讨一下预产期到了，宝宝还没有出生，我们该怎么办？\n预产期的计算：一般情况下是根据末次月经的第一天开始算起，月份减3，日子加7，即减3加7的概念。（比如2017年4月15日是末次月经第一天，预产期大概在2018年1月22日）而从预产期40周开始，正算和倒算会差1到3天的时间。这个数字并不是非常精确的数字，因为孩子并不是40周整才出生的。\n在37周到40周预产期之间，大约有75％的宝宝会分娩发动，剩下的一部分人会发生早产，中国的早产率大约在8％~10％，过了40周之后还没有发动的大概有20％。\n到了预产期还没有发动，还没有正常的宫缩，大家都很着急要怎么办。这个时候就需要知道催产的概念了。哪些条件决定了妈妈催产的时间，这些都是需要医生去评估的。\n催产的时机大致分为两种，一种是预产期40周，一种是41周左右。而对于有并发症的妈妈，比如糖尿病的妈妈，或者高血压、甲状腺功能减退等等的妈妈，催产的时间是不同的。如果并发症很厉害，血糖血压控制不好，医生可能提到39周，如果十分严重，可能还会提到35周左右。\n总结：预产期并不是精确的的概念，到了预产期没有生产的妈妈也不要着急，记得# 听医生的话 ，天使宝宝注定是会降临人间的。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/07dd8388c9f5beac954c4e9268aa2bd9fb1e09d8_r',
    'video_id': '593795dea9b2ed3eb3b99eb2',
    'title': 'PVC管清凉躺椅！体会下什么叫躺赢的夏天吧',
    'video_tag_list': '',
    'content': '站着不如坐着，坐着不如躺着！\n罐头哥送你夏日幸福感up的终极法宝\n打造专属人体工程学躺椅\n椅面弧度全按身材定\nPVC管组装起来超容易\n还能清凉的就像抱着冰\n给我一把，我能一整天不起床\n材料\n木板 / PVC管 / 木漆\n步骤\n①按照模板标记切割线\n②沿标记线切割木板\n③打磨木板边缘\n④用圆规标记裁切线\n⑤用曲线锯切割木板\n⑥木板上漆\n⑦切割并打磨等距PVC管\n⑧组装躺椅\n⑨PVC管清凉躺椅就完成了~'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/640x360/vcodec/libx264/pgc/e158bc1d-0107887-b4a2-108817ae2b89?sign=f902ebc17977b2591c4fc353960d40c3&t=65fb06d4',
    'video_id': '593796357fc5b819b1b80003',
    'title': 'KATE骨干眼影两种画法！内双双眼皮日常妆都能HOLD住~',
    'video_tag_list': '日常眼妆怎么画;凯婷;凯婷  KATE 骨干重塑眼影',
    'content': 'HI大家好啊~\n我相信很多妹纸都喜欢用KATE骨干眼影！\n因为配色非常的简单好上手，日常通勤或者假日派对都能够用上！\n所以其实对于新手来说，我觉得你人生该拥有的第一块眼影就是KATE骨干啦！\nKATE骨干眼影颜色日常，粉质比较细腻，而且有一块是全部哑光的，非常适合眼睛容易肿的妹子来用！至于这块眼影的画法当然不止我说的两种，只不过我这两种都非常的常规而已！\n第一种就是层层叠加的方法啦~一层一层颜色逐渐变深。\n第二种就是眼头眼尾小三角晕染的方法。\n当然，最近看我日常妆分享的会发现，我现在也会用深色来当做眼线，拯救画眼线手抖！\n希望这个视频对于不会画眼影的你们有帮助！\n我会继续出这种视频来造福大家的~\n不要忘记点赞哦~\n谢谢观看！\n#新手最容易上手的眼影盘[话题]#\n#四色眼影盘怎么画[话题]#\n#平价好用的单色眼影[话题]#\n#日常妆容打卡[话题]#\n#日常眼妆怎么画[话题]#\n\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lncCGHERXFN_8vOVPPvhcsBKrchS_compress_L1',
    'video_id': '5937a36db46c5d7ea52d02b8',
    'title': '其实，你也可以将生活拍成电影的',
    'video_tag_list': '摩米士 momax 精英手机三脚架',
    'content': '2010年 YouTube邀请全世界的网民用摄像机记录下2010年7月24日这一天的生活状态，据称，最后他们收到8万个视频，总时长约为4500个小时。后来电影制作人将这些影像素材剪辑制作成一部长达90分钟的纪录片，并命名为《同一天的生活》。\n相信好多人都看过电影、纪录片，但是有没有想过自己来拍一场呢？\n也许你的生活本来就是一部电影，导演、编剧、演员是你，灯光、后期是自然和城市，你的每一个动作和眼神都是一张张胶片。\n摩米士微电影，视频全长5分钟。\n（把发热的脸颊\n埋在柔软的积雪里一般\n想那么恋爱一下看看----石川啄木）\n--------------\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnGpn6W6Tky7Yf_SMM5NMSKikInC_compress_L1',
    'video_id': '5937b6f2b46c5d3d4d0bbb93',
    'title': '关于车内整理 最简便的方法&最实用的工具（1/3）',
    'video_tag_list': '',
    'content': '刚好要出趟门，就趁机拍一下车内吧～有很多好用的必备工具推荐[得意R]这期结尾有个小小彩蛋哦[偷笑R]\n系统限制只能发5分钟，本期内容分三部发，这是第一部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lmsO9SHrK0Avm4O1LjWSd771iAJp_compress_L1',
    'video_id': '5937b82cd2c8a56a6990c316',
    'title': '关于车内整理 最简便的方法&最实用的工具（2/3）',
    'video_tag_list': '',
    'content': '刚好要出趟门，就趁机拍一下车内吧～有很多好用的必备工具推荐[得意R]这期结尾有个小小彩蛋哦[偷笑R]\n系统限制只能发5分钟，本期内容分三部发，这是第二部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvodCT46Kkcgyh80uSUDo10c1z04_compress_L1',
    'video_id': '5937b8d8d1d3b923410a4ea9',
    'title': '关于车内整理 最简便的方法&最实用的工具（3/3）',
    'video_tag_list': '',
    'content': '刚好要出趟门，就趁机拍一下车内吧～有很多好用的必备工具推荐[得意R]这期结尾有个小小彩蛋哦[偷笑R]\n系统限制只能发5分钟，本期内容分三部发，这是第三部～'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/lsadPyMDD5xMnT1-Tb2zlro5Uoxi_compress_L1',
    'video_id': '5937c85ad2c8a5195cd6cde0',
    'title': '我的一个道姑朋友♬ 超好听的古风尤克里里弹唱',
    'video_tag_list': '66好物抢晒单',
    'content': '做个小调查♬ 大家知道尤克里里吗？😁😁😁😁#我是歌薯[话题]##古风歌[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/c62721f6-1839066-bc77-84a33690c9c3?sign=b76dda31331f5cf267c7a99f12f9b62f&t=65fb06d4',
    'video_id': '5937cfb2a9b2ed745e4dc1ef',
    'title': '教你10秒快速打领带',
    'video_tag_list': '',
    'content': '打领带不是谁都会打的哟~很多男士都觉得打领带是件很麻烦的事。\n今天喵酱就教大家一招，居然只要10秒钟之内就能打好领带。顺手也可以为你心爱的ta打一次领带吧！  #视频教你生活小窍门\n#视频教你生活小窍门[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lnwmvg0Kf75_j_uicptqRqssUTRF_compress_L1',
    'video_id': '5937dac4b46c5d1b59f3643c',
    'title': '【 近期最爱的打理头发神器 】',
    'video_tag_list': '拯救细软发大作战',
    'content': '跟大家分享一个我近期最喜欢的头发打理工具。\nDafni黛弗妮美发梳/靓发梳。\n特别适合像我这样的懒人。\n随便梳一梳卷发就可以变直发，秒杀夹板～\n#拯救细软发大作战[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lj3ZBY2FzYsGz3yVGkerWf0iuJHj_compress_L1',
    'video_id': '5937db6bb46c5d24c60bbb8b',
    'title': '☀️雅诗兰黛Double Wear持妆粉底液12小时测评',
    'video_tag_list': '雅诗兰黛;雅诗兰黛 Estee Lauder Double Wear无暇亲肤持妆粉底液;雅诗兰黛 Estee Lauder 气垫粉底棒;夏日不脱妆小秘诀',
    'content': '天气越来越热啦~\n傍晚下班刚要去嗨看到早上化的美美的妆脱得面目全非真的是要哭惹\n这次借着去参加婚礼的机会在南方海边30度+的高温和潮湿环境下\n叫板传说中的“油皮亲妈”雅诗兰黛持妆粉底液！\n带妆12小时，无散粉无补妆\n更有现场泼水挑战！也是很拼呢…\n油皮亲妈的鼎鼎大名早就如雷贯耳了\n虽然自己就是中性皮，但炎炎夏日还是很需要持状效果好的粉底\n尤其出席重要场合的时候必须一直保持状态\n这款粉底液的质地不厚重，用海绵蛋很容易拍开\n我用的色号是1W1暖调一白，刚刚好\n中高度遮瑕力非常够用，暗沉和小瑕疵基本一层就都盖住了\n但不会妆感厚重面具感\n防水力也是一流，我想我知道去游泳该用什么粉底了\n持妆效果更是名不虚传\n我在视频里实测12小时中间没补妆\n真的保持得非常好，但晚上也不花\n虽然持久但并不会不好卸哦\n卸妆油轻轻松松就卸掉了不会干燥不适\n30ml 390元的定价\n无论与同类专柜粉底液还是雅诗兰黛其他底妆产品相比\n性价比都非常高，可以说是良心定价\n用量也不费，这么好的效果真的非常值得入手夏日常备\n现在专柜购买还赠送泵头哦～\n#脱妆算我输##夏日不脱妆小秘诀[话题]#\n\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lheGCfvLDwd26G3gJkdqSv9Kzasa_compress_L1',
    'video_id': '5937e605d1d3b9558ccb03f5',
    'title': '居然还藏钥匙🌚',
    'video_tag_list': '',
    'content': '眼看着香菇就一屁股卧在了车钥匙上面…不嫌咯吗😂\n再说，你是准备给我再孵个车钥匙出来🌚？'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/5c7e42fa-fa46cb4-98b7-1da47ced7b5e?sign=f9751a84f9653130db0a9af3e3de146e&t=65fb06d4',
    'video_id': '5937ec0d7fc5b82a4e24e98e',
    'title': '彩虹蛋白饼干，外形可爱，口感入口即化',
    'video_tag_list': '',
    'content': '今天我来分享一款彩虹蛋白饼干的做法，外形可爱，口感入口即化，而且还可以用来装饰滴落蛋糕或翻糖蛋糕哦！\n做好的蛋白饼干是很怕水的，完全冷却后的蛋白饼干要尽快密封储存，因为空气中的水份会很快使它变软影响口感。\n#自己动手做饼干[话题]##跟着视频学烘焙[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/4f2973b935c273859cf8b92594bea3bb7210e91e_r_ln',
    'video_id': '5937ecd0d1d3b965400a4e89',
    'title': '除了衣服鞋子包包，Gucci的饰品也超美哦～',
    'video_tag_list': '古驰;首饰就要blingbling',
    'content': '今年Gucci在饰品上也下功夫啦！彩钻系列超级美！！\nGucci现在真的是从头美到脚，今年出的首饰和钥匙链等等都运用了彩色的元素，显得无比绚烂～\n同样美的还有老虎头系列和蜜蜂系列～\n不过这类大牌出的时装首饰一般材质都很普通，就是戴戴样子的，像chanel啊dior这类也都一样，耳钉也不便宜，2000-4000豆油，有的更贵～\n真的想买金饰移步卡地亚tiffany宝格丽这些珠宝店～或者有钱任性去chanel和dior高定咯～\n#首饰就要blingbling[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhj_0kgV3V2g3F7roeAfu9_YdpMS_compress_L1',
    'video_id': '59381d3814de413214ffd547',
    'title': '日常清新妆快速变夜店妆',
    'video_tag_list': '斩男妆这样画',
    'content': '画好一个清新日常妆上班，突然被约晚上去浪怎么办？\nGet！！\n用到的化妆品：\n日常妆\n隔离：Armani\n粉底液：Armani\n遮瑕膏：ipsa\n散粉：植村秀\n眉粉：KATE\n染眉膏：Kiss me\n眼影：梦妆\n睫毛膏：Lancôme\n卧蚕：Pony\n腮红：canmake\n染唇液：too cool for school\n夜店妆\n眼影盘／眼线笔／眼线膏：美宝莲\n眼影笔：爱丽小屋\n唇彩蜡笔：美宝莲\n衣服\nWEIVSTUDIO\n#斩男妆这样画[话题]##日常妆容打卡[话题]##日常眼妆怎么画[话题]##嗨爆音乐节的妆容[话题]##夜店派对女王妆教程[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liejIupp-ARHoWq628GxpuRF-_ag_compress_L1',
    'video_id': '5938297bb46c5d7c990bbb8b',
    'title': '一条用视频才能拍出美的裙子，法式复古style也可以很俏皮',
    'video_tag_list': '小清新复古穿搭',
    'content': '本来是用相机拍穿搭的，但这条裙子的裙摆真的太太太好看了！！！忍不住一直转圈，哈哈哈，所以用视频记录下。\n我很少会穿连衣裙，但这条真的是最近大爱的！气质的格纹+优雅的蕾丝原本裙子就已经很美啦！我自己玩儿了一把混搭，加了个腰封，戴上复古的草帽，脱下高跟鞋穿上了平底鞋，哈哈。欢快的跳起来了。\n对啦，你们猜猜看我一边跳一边在唱什么歌呢？😁😁😁\n#每日穿搭[话题]##170cm女生穿搭[话题]##小清新复古穿搭[话题]##大气欧美风[话题]# @穿搭薯  @小红叔'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Fic4ZfXdJA-A3Pm1MCpSj1vYGDnQ_compress_L1',
    'video_id': '5938a2ccb46c5d2f2cf36433',
    'title': '👀',
    'video_tag_list': '跟着视频画眼影',
    'content': '去拍照的时候\n开始还美滋滋觉得自己脸好小哦\n脸好瘦哦\n相机拍出来也是瘦瘦的好看哦[少女心]\n结果闪光灯+单反\n分分钟一块大饼🤦🏻\u200d♀️\n忍不住哭出声来\n是时候好好减肥了\n#跟着视频画眼影[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/3158f467-efac70c-b37f-29b4682ef874?sign=034a1263175229998b311f615736ca8f&t=65fb06d4',
    'video_id': '5938c533a9b2ed744f4dc1ef',
    'title': '3 个臀腿训练动作，跟着美女教练一起学',
    'video_tag_list': '',
    'content': '火辣健身教练「冉冉」又来了，今天她将教给你3个简单又有效的动作，让你的臀腿训练事半功倍，赶快准备一把椅子和一块瑜伽垫，跟着冉冉练起来吧！更丰富更完整的训练计划欢迎下载「火辣健身app」，或者微信关注「火辣健身」。#练出马甲线#减肥##健身##瘦腿#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/852x480/vcodec/libx264/pgc/5567ee1a-a64be37-abc7-cc9434b638f2?sign=9db06517e02289b125b0ec969bd99b1f&t=65fb06d4',
    'video_id': '5938c6ef3460946f3699b425',
    'title': '曼谷攻略| 好吃好喝又好买的城市，还便宜！',
    'video_tag_list': '曼谷;泰国游美食指南',
    'content': '#泰国游美食指南[话题]#\n曼谷我算是非常熟悉的[得意R]，所以到了这边就像地头蛇一样带着姑娘们到处吃吃喝喝买买买[害羞R]，第一次来的Cherry表示以前觉得泰国是挺落后的地方，好像除了看人妖表演就没别的了，跟着我逛了之后才发现原来好洋气捏！[赞R]\n🌟🌟🌟关于酒店❤️\n曼谷的酒店超级多而且便宜[色色R]，如何选择主要看你的诉求是什么。像我们还是以拍照工作为主的Business Trip[飞吻R]，所以那些装修老气色调暗沉的直接看图片就排除了，最后选择了位于Thong Lo区的Grande Centre Point Sukhumvit 55。\n这家酒店是2016年才开业的，所以装修明亮简洁大气，蓝白金色调为主的大堂尤其漂亮~~[飞吻R]\n因为我们有四个人，就订了一间Two-bedroom studio，有两卧+两卫+一客厅，总共面积110平方米，位于视野开阔的21楼上，住起来感觉很宽敞。而且这边是有点偏酒店式公寓的感觉，客厅里有个小橱柜，里面炉灶、厨具和餐具一应俱全，非常适合一大家子人来住。。。关键是它的价格相当美好，住这么多人一晚上才1700人民币左右，在五星酒店中算是相当亲民了。[赞R]\n这家酒店的早餐也很丰盛[害羞R]，每天早上都有不同浇头的泰式汤面或河粉供应，各种各样的冷热菜和点心也很多。我最喜欢的是它提供的无糖超浓豆浆，旁边放着薏仁、糖冬瓜、椰果、雅塔子等配料随便加，又健康又好喝，我每天早上都要整两碗这个，再吃两碗河粉才罢休。[笑哭R]\n总体来说这家酒店是性价比很高的[赞R]，只是location不算很中心。Tong Lo区在曼谷是日本人的聚集地（所以酒店也有冲pp的马桶），很多时尚餐厅和酒吧，但并不是游客爱去观光的地方。好在曼谷的轻轨还是很发达的，酒店每隔20分钟就有班车接送住客去轻轨站，不怕交通麻烦一点的可以考虑。\n而如果你来曼谷主要是想吃吃喝喝，体验一下当地潮人的生活，Tong Lo区会是不错的选择，附近就有个美食聚集的网红商场，我们等一下会讲到。\n🌟🌟🌟关于美食❤️\n吃货们来到曼谷绝对会流连忘返，因为好吃的真是太！多！了！无论是西式还是泰式还是融合式都有让人眼花缭乱的选择，而且这边的餐厅环境好、食物素质高，普遍来说比上海同等餐厅便宜一半左右，让我们回来以后觉得吃什么都好贵啊。。。\nAgain因为时间有限，我就精选了几家带着姑娘们冲去大开杀戒，就是你们在视频里看到那些哈：\n1️⃣The Commons\n地址：Soi Thonglor 17 Klongton Nue, Wattana, Bangkok\n这就是我前面提到那个酒店附近的网红商场，藏在一条僻静的小巷子里，主打垂直商场+绿色环保社区的概念。所谓垂直商场指的是它纵向层层叠叠半露天的结构，每一层都设有台阶、坡道和休息平台，环绕着绿树成荫的中庭，打造出一个城市花园的感觉~\n这里无论是白天还是夜晚气氛都非常妙，里面主要集中了大大小小的餐厅和酒吧，光看环境就很吸引人了。\n我们刚到曼谷的第一晚就冲过来报道，一楼是个开放式的food market，有卖酒的和各类小吃，好多衣着光鲜的白领貌似下班之后在这里喝一杯放松，让人忍不住想要加入。\n这边的menu都做成一本小清新杂志的样子，上面好多令人吞口水的菜式，主打意式融合一点泰式风格。我这个人的毛病就是只要饿着肚子点菜就会往死里点，搞出丧心病狂的一大桌。。。\n还好它家分量都不算很大，而且每一道菜都很刺激味蕾，第一道沙拉端上来就把我征服了。它是很嫩的豆子切成细条，配上清爽的油醋汁和羊奶芝士，再加上泰国盛产的新鲜香草，吃起来清脆爽口停不下来的节奏。\n2️⃣karmakamet Diner\n地址：30/1 Soi Matheenivet, Sukhumvit 24, Bangkok\n另一个“又好吃又好买又适合拍照”的地方就是这家餐厅，我手里捧的彩色棉花糖是每桌必点的网红单品，不过环顾四周大家都只用来当拍照道具而已，没几个人真的吃它。\n当然店里好吃的菜也是有的，比如青酱牛肉丸表面一层都煎得脆脆的，羊肉酱pasta也很香，它们自家品牌的house wine品质也不错，算是一家随便吃吃也不会出错的餐厅。不过当天我们的注意力主要在别的地方，以至于都没认真给食物拍照。\n3️⃣Nara（多间分店）\n这家餐厅我在两年前的曼谷美食攻略中就写过，当时它就被评为最好的泰国餐厅之一，现在好像更红了，几乎每家大商场里都有分店，几乎每个攻略里都会被提到。\n这次我们去的是位于新商场Central Embassy五楼的分店，这个商场本身比较高档人流也少，餐厅也不会像其他分店那样大排长龙，想试试Nara就来这家吧。\n它的招牌菜依然是咖喱蟹，比起新加坡那种过分甜腻辣椒蟹来，我更喜欢这种泰式口味的，外面那层酱非常香，好像除了咖喱还混着蟹黄的味道在里面，吃得人赞不绝口。\n泰式生腌虾也还是记忆中那样美好，除了食材本身够新鲜，酱汁的调味也层次丰富，酸辣中带点微甜，充满了混合香草的滋味，涂在鲜嫩的虾肉上吃真是太棒了！\n除了海鲜之外，这道不起眼的丝瓜苗是我的最爱，因为平时很难吃到。新鲜丝瓜苗口感又脆又嫩，用酸辣酱汁凉拌吃起来超过瘾的。回上海我只有在一间叫做“一坐一忘”的云南餐厅吃到过，是从云南空运过来的，有时候去晚了就吃不到，或者运气不好吃到很老的，这么嫩的丝瓜苗一定要在泰国抓紧多吃点啊！\n除了这三家重点介绍之外，其它好吃的选择也真是太多了，有时候在商场里随便找家餐厅吃吃也不会踩雷。\n🌸🌸🌸🌸🌸\n像有一天我们在Siam Center里逛累了，就上楼找了家吃濑尿虾的专门店，连店名都不记得了，但对那里的美味印象深刻。平时冬阴功吃得多，但用濑尿虾来做的还是第一回遇到，汤底辣得超够劲的，让我们边猛灌冰凉椰子水边停不下来地往嘴里送。\n吃完出来又遇到一个烤饼的小摊位，好多穿着制服的学生在这里又是排队又是拍照的，让我们认定肯定又是网红美食，于是也加入了队伍。戴小帽子的眼镜蜀黍耐心细致地一份份烤出来，看到我们拍照还配合地转过来微笑，相当nice。\n别看小煎饼本人黑乎乎的，那是因为加入了竹炭粉，实际上它口感松软很像迷你版的蛋烘糕（四川人懂的），只不过里面是流心芝士馅的，略带咸味吃起来一点都不腻，一口干掉一个毫无压力，如果大家遇到这个摊位别忘了试试啊~\n🌟🌟🌟关于购物❤️\n购物方面曼谷当然比不上东京，因为气候炎热也不适合在外面压马路逛小店什么的，不过几大商场还是很好逛的。尤其是这里的商场经常会更换不同主题的装置艺术，就算是不爱买东西的人，光看看也觉得很有意思。\n除了那些到处都能见到的国际品牌，很多商场里都有的本土设计师专柜也蛮有意思的。虽然他们在服装设计方面很多时候天马行空，不太穿得出去，但在店面布置上总是充满新意，让人眼前一亮，也是拍照的好去处。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/88f3da0dbdb4fc41c6b99d94e056825f9cc84be6_r_ln',
    'video_id': '5938c74cd2c8a5308d90c301',
    'title': '薯片与色拉的完美搭配，吃一片为高考减减压！',
    'video_tag_list': '',
    'content': '★★★★★\n小圆食记\nMenu\n高考的日子里，除了要保证考生以最佳的状态认真复习、迎接考试外，如何让考生吃得好、吃得科学、保障考生的营养供给也成了家长们最关心的话题。\n★★★★★\n创意指数\n薯片色拉\n▼\n薯片色拉\n·视频音乐·\n徐梦圆 - Run - 纯音乐版\n·食材·\n苦菊、薯片、大虾\n牛油果、芒果、圣女果\n柠檬、酸奶\n1.煮一锅开水，放入l少量柠檬片放入大虾煮熟，并捞出备用\n2.虾肉切丁\n3.芒果对半切开，在果肉部分划十字斜刀\n4.切好后从芒果皮中心往上顶起成芒果花状，拿刀沿果皮边缘切下果肉备用\n5.圣女果切4小瓣\n6.苦菊洗净切段备用\n7.牛油果切半去核，果肉部分切竖刀\n8.用勺沿果皮边缘挖出果肉，并切丁备用\n9.将食材一同放入碗中\n10.取适量酸奶拌匀\n11.将沙拉置于薯片之上，便可以享用啦~！\n小贴士\n1.煮大虾时放入适量柠檬片可以去腥'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/640x360/vcodec/libx264/pgc/074f0404-c8075a1-8e30-dfb10fa22a6b?sign=4cd7c281bbdaed9a900099f363cea66d&t=65fb06d4',
    'video_id': '5938ca177fc5b8303d24e97e',
    'title': '学生党福利！军训最适合用的防晒霜top5！必收藏哦~',
    'video_tag_list': '清爽不黏腻的防晒霜;防晒也能很清爽',
    'content': 'HI~大家好我是小斤斤呀~\n话说高考即将结束啦~相信各位考生们都是充满笑意的离开考场，都会金榜题名~一直会长远考虑的我表示！浪两个月就要军训了！又是一场灾难！所以防晒工作必须做的足足的才行呀~\n所以今天分享的就是军训适合的防晒霜测评啦~\n当然，如果你学车的话这些也是可以用的上的哦~\n#防晒也能很清爽[话题]#\n#学生党爱用平价防晒[话题]#\n#清爽不黏腻的防晒霜[话题]#\n#我最爱的平价彩妆品牌[话题]#\n#痘痘肌适用防晒产品[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lj3NYwoLi-jPYYXTXXh4e-75ivoC_compress_L1',
    'video_id': '5938cadb14de41163fa9c57b',
    'title': '喜欢你超好听的歌♬ 我喜欢上你时的内心活动',
    'video_tag_list': '气垫BB霜大测评',
    'content': '曲谱在微信公众号趣弹音乐哦~想要学习的小伙伴可以联系我哦~#我是歌薯[话题]#'
  },
  {
    'video_url': 'https://sns-video-bd.xhscdn.com/lixj84NoisRGdM0a8DkWbSDTHU9y_compress_L1',
    'video_id': '5938dcced1d3b9339b0a4e98',
    'title': '第一次在家给她🛀一只胖柯基',
    'video_tag_list': '',
    'content': '第一次在家给她🛀，第一次让她上床，第一次让她在垫子上玩，第一次舔脚上瘾😂😂'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/1c9d372b-c812af7-a37c-d8bcfedcd8b1?sign=1f7d2a1fe8c0ec8239cca49f48c32486&t=65fb06d4',
    'video_id': '5938e13c7fc5b85f7c505147',
    'title': '另类毕业照，就说你爱不爱吧~',
    'video_tag_list': '',
    'content': '又到一年毕业季，毕业照可是重头戏\n微笑抛帽剪刀手，pose套路年年有~\n然而是学霸or学渣\n一个姿势其实就会轻松暴露~'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/FqgaSXD9zm-zM349fS5DX1vIE7dn?sign=3777e4a21c7f972bc74652dae45fb00b&t=65fb06d4',
    'video_id': '59390e5ad1d3b9510b88aaa2',
    'title': '肚皮舞 八字胯练习',
    'video_tag_list': '',
    'content': '今天礼拜四了 离周末不远啦😄'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/loJ4vooinkNLklM3Hm60YxeFTQ-a_compress_L1',
    'video_id': '5939178bd1d3b96be788aaa6',
    'title': '第一次🤝这么配合',
    'video_tag_list': '',
    'content': '丸子用了一天的时间学会了握手，趴下……\n可她怎么就学不会定点上厕所呢😂'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvTgErdhDR_3UMbVKa5-JtwZ7ggv_compress_L1',
    'video_id': '5939186cb46c5d10c26437da',
    'title': '快上🚗☄️——3分钟学会【夏日出街妆】',
    'video_tag_list': '夏日缤纷妆容色',
    'content': '今天分享一个比较简单日常的橘色系妆容给大家哟\n（就是上次我鲁卸妆视频时的那个妆容）因为很多宝宝说好看想要学 所以就出啦～传上来以后好像有点模糊 不是很显色～忧桑...\n这次用到的东东我都在视频里打出来啦\n都是我平时很喜欢用的～\n录视频太激动结果..[汗颜R]眉毛部分没录上，睫毛膏直接忘了！哈哈哈哈哈 大家见谅～\n最后\n有啥问题可以问我哟～\n#日常妆容打卡[话题]##夏日缤纷妆容色[话题]##跟着视频画眼影[话题]# @美妆薯'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FsLoefvfG-6qKQk3DfmIksLxqwOK_compress_L1',
    'video_id': '5939310dd1d3b924f365b774',
    'title': '【本周萌娃】我要开特斯拉！',
    'video_tag_list': '小红书萌娃大赛',
    'content': '哈喽艾瑞巴蒂！又到了【本周萌娃】的时间！～[吧唧R]\n今日的萌娃账号是小男孩ET和加菲猫胖子Fatty🐱的呆萌组合 @ETandFATTY ，来自#小红书萌娃大赛[话题]#\nET的日常就是卖萌、跟Fatty抢🍤、穿成时尚小Icon出门。ET的麻麻陈公子笑称两小只是西瓜太郎和猫咪老师，感情超好～[萌萌哒R]视频薯也是被他们的日常萌的不要不要的，超级治愈[飞吻R]\n你家也有萌娃？拍出来@视频薯 吧！下周的萌娃之星可能就是你家宝宝哦～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/9a42e290f7852b2b178ed9ab932cb09afd238d59_v1',
    'video_id': '593936ecd1d3b9060e65b766',
    'title': '一分钟日系风格卷发',
    'video_tag_list': '我是长发控',
    'content': '一个卷发棒就可以做出来的发型～做好之后的效果也是很自然温柔[萌萌哒R]\n不同发长的小红薯可以戳#我是短发控[话题]##我是长发控[话题]#\n你平时怎么折腾头发？可以拍出来@视频薯 哟[偷笑R]～\n（视频来自@seiichirookawakami ）'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FnGvWUuhRNV_V7FPI7olhsSDPEmq_compress_L1',
    'video_id': '5939449f14de416983ded88a',
    'title': '布偶猫香菇🐱馋猫日常',
    'video_tag_list': '',
    'content': '拿点吃的一逗就出来了~[偷笑R]\n当然这个巧克力的冰棍并没有给他吃，就是给她看了看[得意R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ligwxk4NGK2-PjzgMBNg_-5fv3hh_compress_L1',
    'video_id': '59395235d2c8a51b0887a076',
    'title': '',
    'video_tag_list': '随手拍宠物',
    'content': '第一次见到氢气球的cookie🎈\ncookie第一次见到氢气球 有点害怕又有点好奇[笑哭R]\n后来就开始躺着玩啦哈哈哈[笑哭R]\n#我家宠物最萌的瞬间[话题]##随手拍宠物[话题]##我和宠物的日常[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llXwgqbkeeUsiGO-huVPwveY41AN_compress_L1',
    'video_id': '59396abc14de415181ded895',
    'title': '3种眉形画法！卡姿兰三角立体画眉笔，什么眉形都能hold住',
    'video_tag_list': '适合新手的眉笔;卡姿兰',
    'content': '好久不更新视频的玛丽已忘记了拍视频的技能，导致这次光线极度不可控，差点变成非洲人[无语L]\n话入正题，今天这个视频全是干货，一直说不会画眉不知道自己适合哪个眉形的仙女可以耐心耐心看完。另外！画眉不是灵光一闪就可以技能满点，一定要好好练习OK？\n今天用的产品是卡姿兰三角立体画眉笔，一盒抵到爆，最适合练手，我用的01号色。\n另外仙女们还想看什么视频just告诉我，毫无灵感的玛丽非常捉急[害怕]#适合新手的眉笔[话题]##简单易上手的画眉方法[话题]#'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/FqIhCj4o4swCcBSDIYlo20M1DWbt_compress_L1',
    'video_id': '59396fac14de4164ec9e93bc',
    'title': '我的宝贝',
    'video_tag_list': '给宝宝的mini情书',
    'content': '干啥呢，嘴巴吧唧吧唧的,其实啥都没有。😂😂😂\n#小红书萌娃大赛[话题]##给宝宝的mini情书[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkUcXgPY4RgOfnk_ZjyRjQR5BPXV_compress_L1',
    'video_id': '59397dbdb46c5d238a75adbf',
    'title': '美瞳+眼妆搭配',
    'video_tag_list': '眼妆测评',
    'content': '昨天po的那款眼妆，还有之前发的TF02的图文稿子，有宝宝留言给我想看视频，所以出了这条视频～\n是一个很闪亮✨的眼妆搭配一款非常漂亮的美瞳\n希望小红薯们喜欢\n#眼妆测评[话题]##眼妆每日打卡[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ltFb9mtODyBU3hVNlbN2FNgwlfpP_compress_L1',
    'video_id': '59397e7cb46c5d1ec475adcb',
    'title': '三木三山',
    'video_tag_list': '',
    'content': '我这俩儿子，天天都是戏………'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lpGJklkWeW7aANP37HUM7hEmaNp1_compress_L1',
    'video_id': '5939eb51d1d3b9679c88aaa5',
    'title': '毛里求斯旅行视频',
    'video_tag_list': '',
    'content': '一直不知道小红书还能发视频，那我以后可要泛滥了，舞蹈视频一堆堆的，等着我吧。😊'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/57bb0e717debdce39d1cd7c660040dc89a4db0a8_r_ln',
    'video_id': '5939ecc114de4141b3ded888',
    'title': '舞蹈视频watch me work',
    'video_tag_list': '',
    'content': '啦啦啦，能发视频好开心啊，喜欢就关注我吧，以后会经常有舞蹈视频哦！这是我的学员们学了4个月的时候演出视频，棒棒哒！😉'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lkkQyfczAH1fsdZCI5cR14Xle87W_compress_L1',
    'video_id': '593a0df7d1d3b9532c65b748',
    'title': '【 近期爱用眉笔 | 卡姿兰三角立体画眉笔 】',
    'video_tag_list': '卡姿兰;适合新手的眉笔',
    'content': '一直有宝宝在我发妆容的时候问眉毛怎么画，所以今天就特意发个视频来讲一讲。\n使用的产品就是最近出远门的时候无意间买的眉部套盒，但我没想到居然会这么平价好用，真是无可挑剔了。\n今天画的就是我平时最常画的弯弯眉，会显得人更温柔有亲和力。\n具体的画法看视频吧～\n\n#适合新手的眉笔[话题]##回购一生的眉笔[话题]##自然又显色的眉粉[话题]#\n#实用的修眉小技巧[话题]##我的彩妆测评[话题]##平价双头眉笔测评[话题]#\n#我最爱的彩妆品牌[话题]##我最爱的平价彩妆品牌[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/dbcb4a47367a645761c62642e52b08a7da1839da_v1',
    'video_id': '593a196c14de41310eded8a7',
    'title': '视频版本--超实用马甲线教程！坚持做一个月练出马甲线！💪',
    'video_tag_list': '练出马甲线',
    'content': '之前的马甲线教程笔记大家有木有跟着做呢？\n今天来更新视频版本啦！哈哈\n挥洒汗水的时刻，就是你努力的见证！💪\n时间在你身上刻画了努力的痕迹。\n一套动作在家就可以完成，\n每天坚持练习，再结合有氧运动，控制饮食。\n相信我，一个月后马甲线会属于你！加油！\n更多减肥健身笔记记得关注我的专辑➡️【听雨健身分享】哈，么么哒，希望我们都可以做自己的马甲线女王！✌️️✌️️✌️️#健身靠装备[话题]##见人不如健身[话题]##练出马甲线[话题]##厉害了我的健身房[话题]##减肥是女人一生的事业[话题]# @小红叔'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lll_bAGZKJ65k1CH2PoRtHBli5Bg_compress_L1',
    'video_id': '593a33f2b46c5d19c675adb4',
    'title': '2017.2@瑞士🇨🇭瑞吉山RIGI🚠下来时日落美景～',
    'video_tag_list': '瑞士旅游',
    'content': '地球🌍不爆炸 旅游👟不停歇\n世界🌟那么大 我想❤️去看看\n春节(14天）去了奥地利🇦🇹,德国🇩🇪,瑞士🇨🇭，法国🇫🇷\n坐的是战斗民族俄罗斯航空，Moscow转机，保留曲目，落地鼓掌👏\n奥地利🇦🇹停留了4天～萨尔茨堡，哈尔施塔特小镇主推～\n德国🇩🇪是为了到Konstanz退税，然后到Munich住一天，前后不到24小时就离开了～\n瑞士🇨🇭～停留8天，一个个地点分析，会耗尽元神伐😂\n法国🇫🇷其实到的是依云小镇😂，也算是法国到此一游～\nQ：交通费如何？\nA：贵，奥地利德国买的的是4日欧铁通票，仅限铁路，城市有一日通票可以买，瑞士买的八天连续通票swiss pass，铁路、船、公交车、地铁都可以坐，除了部分登山缆车需要买票但可以打折.\nQ：吃如何？\nA：写过一篇关于物价的可以去翻，欧洲还可以，瑞士贵➕味道一般，我们基本超市购物解决饭，自己弄过火锅，饺子，蛋饼，当然少不了🍜这些冬天比较合胃口～\nQ：英文不好自由行怎么办？\nA：相信我，你们的英语一定比我好！\nQ：欧洲难民现在多，治安如何？\nA：没有碰到小偷，弄个小背包，贵重物品放前面，不要让小偷觉得有机会，诱发人家犯罪😂\nQ：有什么app推荐？\nA：OBB（欧铁）SBB（瑞士铁路）google map ，有道翻译，Coop（瑞士超市定位），Meteoswiss（瑞士天气）\nQ：冬天几点天黑？几点商店关门？\nA：4点半左右就要黑了，630左右关门，包括有些便利店\nQ：退税怎么退？\nA：奥地利德国买的东西是不能在瑞士退税的，所以我们找了德国瑞士边境火车站konstanz退税，夜长梦多还是拿了现金\nQ：旅途中遇到最大的困难？\nA：拎箱子拖箱子😂冬天防滑路上铺了很多碎石，拖箱子比较费力，所以火车站离酒店尽量近，火车站上下火车时有好心人帮你提箱子，但大部分时候要靠自己。\n～～～～～～～～～～我是分割线～～～～～～～～～～\n🌟🌟🌟🌟🌟用swiss pass全程免费🌟🌟🌟🌟🌟\n位于卢塞恩的瑞吉山（Mr Rigi）真的美到炸，是到瑞士的第一个景点，以下是去Mr Rigi的路线，这样既可以坐登山小火车，又可以下来坐缆车🚠，缆车下来可以顺便兜瑞士十大最美小镇之一的韦吉斯Weggis小镇（另一篇攻略已写）给大家参考～\n上山：Luzern游船到Vitznau(1小时）坐红色登山列车到RIGI KULM山顶\n下山：徒步or电梯到RIGI Kaltbad,坐缆车🚠到Weggis，坐船回Luzern～\n这段视频就是缆车下来时候正好碰到日落，很美，下面就是韦吉斯小镇～\n瑞士🇨🇭的攻略已经每个地方都详细展开写过了，有兴趣可以去翻，几乎要飜到最底部了😂～\n#最爱旅行地[话题]##欧洲旅行攻略[话题]##带着小红书去旅行[话题]##我的小众旅行攻略[话题]##边走边拍[话题]##天空[话题]##瑞士旅游[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljpdz8RUx4MZXOPzyNa__x6i0Fjb_compress_L1',
    'video_id': '593a37acb46c5d2d6c6437ec',
    'title': '专治夏天没胃口，超清爽凉面',
    'video_tag_list': '周末吃啥',
    'content': '#周末吃啥[话题]##吃货小分队[话题]#\n不知道大家有没有和我一样\n一到天热的时候，就什么都不想吃\n以前超级爱的鸡腿啊，火锅啊，\n统统提不起味口来\n但是要给我来一碗清爽的凉面\n我能一口扒完~\n食材\n面：适量\n姜：一小块\n辣椒油：花生、芝麻、辣椒面、花椒\n调味汁：生抽、醋、蒜泥、辣椒油\n做法\n1.    姜切末，加适量冷水泡姜水。\n2.    拌辣椒油，将炒好的花生碎、芝麻、辣椒面、花椒放到一个碗里，倒入热至80-90度的菜籽油。边倒边搅拌。\n3.    开水下面条，熟了捞出过冷水后立即再捞出，加1-2勺橄榄油，拌匀放凉。\n4.    做拌面的调料，生抽、醋、蒜泥、和拌好的辣椒油按1：1：1：1的比例拌好。\n5.    凉好的面条加入适量姜汁，加入第4步拌好的调料，拌匀即可。\nUU小TIPS\n1、炒花生碎的方法能用火炒，也能用烤箱烤：a、炒：将花生放到食品袋内，用擀面杖压碎。\nb、烤：直接把花生放到烤盘里，用可以放进烤盘的擀面杖擀碎花生，放入无预热烤箱内，180度烤15分钟。（时间供参考，具体时间根据烤箱定哦。）\n2、辣椒油里一定要多加花生碎，超好吃。喜欢吃辣的人就多加点辣椒。\n3、关于用油，用菜籽油炸辣椒油是因为菜籽油比较香，拌面时加入橄榄油是因为橄榄油属于可生食油。以上两种油都可以替换成其它油。\n4、加点芝麻酱也超级好吃哦~芝麻酱可以用芝麻油或者温水拌开再加到面里。'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/45d4206e-95c443a-8712-b18a46735878?sign=9f9414e5add61729898e6fbb8599b695&t=65fb06d4',
    'video_id': '593a3d387fc5b854c07b18fb',
    'title': '黄金马甲线动作 | 小腰围和线条感秘诀',
    'video_tag_list': '',
    'content': '很早之前我就有个疑惑，为什么臀部会越练越大，而腰会越练越细呢？真的好天真。如果用不正确的方法去去训练腹肌，不练成水桶腰才怪呢。所以今天视频和大家分享练出线条感又保持超小号腰围的训练安排和方法，以及weiya和Giselle最喜欢的腹肌训练，快戳视频！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/Frm039F7GWGTBZMVDwuU6-_l8AyW_compress_L1',
    'video_id': '593a3dbb14de410ebc9e93c7',
    'title': '教你做美甲：在家也能diy的清新美甲💅',
    'video_tag_list': '亲手晒美甲',
    'content': '超级简单的美甲花式～bling bling+黑白配，看上去很清爽，适合夏天装扮😊\n自己DIY的指甲油我一般会选可剥的，没几天可以用手剥掉，随心情变换花式，特色适合我这种善变女森～\n有想学美甲的妹纸，可以直接拿图来找，会选合适的出视频教程😉\n废话不多说，直接看视频，精华都在视频里👉\n@美妆薯 #少女心美甲[话题]##我们就爱纯色美甲[话题]##春夏美甲配色[话题]##亲手晒美甲[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvXZNQyyifj576Tk5xNQRIVmFYL1_compress_L1',
    'video_id': '593a44c4d2c8a51b1f87a06d',
    'title': '嗯哼~♬ 不一样的《郭源潮》',
    'video_tag_list': '一周7天口红不重样',
    'content': '完整的视频可以偷偷的在【趣弹音乐】微信公众号拿到哦~记住要偷偷的😁😁😁'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ll5MzZJeHy0AvA2fFfCkouHLwvq1_compress_L1',
    'video_id': '593a4560d2c8a51afb652f47',
    'title': '三木三山',
    'video_tag_list': '',
    'content': '今日北京温度38度（可能不止啊）趁着麻麻在休假，自打办了游泳卡，每周都来游一次，多游泳对关节保健有好处，身心都健康😜'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/290445f1-f33a97f-a792-e593c3b2c950?sign=aeec60fe21e4ca04edd2fb8c578e4bcf&t=65fb06d4',
    'video_id': '593a52847fc5b834797b18ef',
    'title': '家庭版麻辣小龙虾',
    'video_tag_list': '',
    'content': '麻辣小龙虾，所需调料略多，但都是超容易买到的。这种7钱左右的龙虾我这边本地市场价23一斤，准备买5斤吃到爽！\n#我爱小龙虾[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lu0oNh9ACLX2vA80fvvDpwxOwk_o_compress_L1',
    'video_id': '593a5512d1d3b927e388aaa2',
    'title': '【最新资讯】未来手机标配的Type-C 是何方神圣?',
    'video_tag_list': '科技拯救世界;爱科技',
    'content': '最近两年，手机技术有了突飞猛进的发展，处理器性能提高了不止一倍，手机摄影上各厂商也从开始拼像素到纷纷从单摄像头转为使用双摄镜头。除此之外，还有一项改进引人注目，那就是Type-C接口在手机上慢慢普及。[吧唧R]\n究竟什么是Type-C？它和Micro USB有何不同？为什么大家都说它是USB接口的划时代产品。今天小摩就跟大家聊一聊Type-C 。\n话说Type-C接口慢慢崭露头角也是近2年的事情，尤其是最近三星、小米、华为、一加发布的旗舰手机几乎全都采用了Type-C的接口，就连最新款MacBook都放弃了使用多年的磁吸式接口改用了Type-C，苹果下半年推出的iPhone是否采用Type-C规格仍是众说纷云，但足以可见Type-C的火爆程度。\nType-c又叫 USB-C，现在我们一起通过视频来认识下吧[飞吻R]\n#科技拯救世界[话题]#'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/4d929378-2fd134f-a96d-b588f20a19b9?sign=2d08befb54e27162f60673ef48267a0d&t=65fb06d4',
    'video_id': '593a57cc7fc5b85b467b18e6',
    'title': '巧克力慕斯，十几分钟就可以轻松搞定',
    'video_tag_list': '',
    'content': '今天我来分享一款巧克力慕斯的做法，十几分钟就可以轻松搞定，用它来招待客人也倍儿有面子。\n做好的巧克力慕斯可以放进冰箱的保鲜层冷藏保存，想吃的时候直接从冰箱里拿出来就可以吃，口感丝滑细腻，入口即化，当然你也可以用它来做蛋糕。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/49f6d12df45c1662c96b5d37d9a07fba91f8ef29_r_ln',
    'video_id': '593a58897fc5b85b0ac39a9b',
    'title': '花蛤意大利面 - 视频教程 - 美善品食谱',
    'video_tag_list': '',
    'content': '#简单美味的意大利面[话题]##跟着视频学做菜[话题]#\n今天我来分享一款花蛤意大利面的做法，用美善品来做特别方便，一气呵成。\n做好的花蛤意大利面鲜味十足，满屋飘香，保证你吃了还想吃。\n无论你身在何处，即使你在出租房、宿舍或者出门旅游，只要有个插座的地方，你就能无油烟地做出各种营养丰盛的大餐。\n我目前和大家分享的只是美善品的冰山一角，以后我会继续分享更多美善品能做的美食。'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/93f6ee7a-0ab749b-b78d-e2a2efcb2972?sign=6016e6ab17ea94ecc66cd531cbbc1d34&t=65fb06d4',
    'video_id': '593a5f437fc5b85e42c39aa3',
    'title': '无敌外卖侠！给你送餐的小哥其实都有另一个隐藏身份',
    'video_tag_list': '',
    'content': '凉快的办公室里陪伴你的只有饥饿感\n可外卖小哥却在酷暑中为生活跑订单\n风雨无阻使命必达，这种事不是超人能做到吗~'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhxTMBzY8F01b-sBuN-tgFWNt6q2_compress_L1',
    'video_id': '593a69d9d1d3b94bc565b767',
    'title': '【Adora视频】教你不同脸型上挑眉画法',
    'video_tag_list': '给眉毛穿一层雨衣;伊蒂之屋;Anastasia Dipbrow Pomade超持久眉膏',
    'content': '#简单易上手的画眉方法[话题]##给眉毛穿一层雨衣[话题]#\n各式眉毛大法看过来，貌似还木有博主po欧美风眉毛的画法 我来填空[喜欢]\nins、youtube博主的眉毛和欧美流行的中性风都有一个特别明显的眉毛特征[活力]上挑眉 大战一字韩式半永久后 我要大肆宣扬一下我日常的眉毛画法。\n就算是上挑眉，各种脸型也有不同的眉型画法。总的来说眉毛的型是需要根据脸型来进行配合，目的从视觉上起到协调美化的效果的。所以也就是不存在，所有人都适合韩式半永久，不存在所有人都适合三角眉………要依据自己的脸型来选择眉型。\n采用的眉毛位置衡量法也是依据自己眼睛和鼻尖位置距离来衡量的。\n不妨试试这种欧美风，换个新自己。欧美妆容从眉毛开始。\n作用产品：的透明啫喱眉胶 眉毛雨衣 眉毛打底\n\n和12号眉刷'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lv8TmN2sZDPVUBCWkg8-toKiNs-V_compress_L1',
    'video_id': '593a80e3d1d3b9292f65b74f',
    'title': '英短柯基日常',
    'video_tag_list': '我和宠物的日常',
    'content': '只要lulu上我旁边坐着 百利一定要赶紧过来 不仅要趴我身上 还要把猫咪赶走🙄百利好坏的....\n#我和宠物的日常[话题]##我家宠物最萌的瞬间[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/2b7afb488dfd3b12608d4461e6a1a9175bb14d30_r_ln',
    'video_id': '593a8b24b46c5d14df75ada7',
    'title': '夏天最爽口的搭配——皮蛋拌黄瓜',
    'video_tag_list': '',
    'content': "★★★★★\n小圆食记\nMenu\n黄瓜含有胡萝卜素。抗坏血酸及其他对人体有益的矿物质，硫胺素、核黄素的含量高于番茄。不仅含有较高的营养价值，而且有许多药用价值和美 容作用。\n松花蛋较鸭蛋含更多矿物质，脂肪和总热量却稍有下降，它能刺激消化器官，增进食欲，促进营养的消化吸收，中和胃酸，清凉，降压。\n★★★★★\n创意指数\n皮蛋拌黄瓜\n▼\n皮蛋拌黄瓜\n·视频音乐·\nP!nk - I Don't Believe You\n·食材·\n黄瓜、皮蛋\n小米椒、蒜\n生抽、醋、糖\n1.黄瓜洗净，切去两头\n2.用刀柄拍碎黄瓜\n3.切成小块备用\n4.皮蛋去壳，切成4瓣备用\n5.摆出喜欢的造型备用\n6.蒜切末，小米椒切圈备用\n7.取一空碗倒入蒜末，小米椒圈，淋上热油拌匀\n8.倒入一勺生抽、一勺醋、一茶匙糖拌匀\n9.淋上即可\n10.夏天的最爱，简单又美味~！\n小贴士\n1.皮蛋切半后光滑面朝上入刀，切出的皮蛋光滑整洁\n#超Easy的凉拌菜[话题]#"
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/40d447ea8ad47fdb8e19f46c77adf6f9f966f8c3_r_ln',
    'video_id': '593a8e3fb46c5d1d4a6437f1',
    'title': 'May J舞蹈改编•Supterstar',
    'video_tag_list': '舞蹈教学视频',
    'content': '哈喽艾瑞巴蒂！周五到了，来热舞一曲吧～\n今天的舞蹈视频来自@胖子沫er要减肥 ：“拿花球是因为要在篮球场跳。其实还是不加花球好看，有时间再拍个不加花球的吧～”\n可以戳她参加的#舞蹈表演视频[话题]##舞蹈教学视频[话题]#观看更多舞蹈哦，拍了视频别忘了@视频薯[吧唧R]'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/9ff4ad4f-c6d4456-9993-80ab0a339be1?sign=f1889926b2beb3be3e33d992eabea253&t=65fb06d4',
    'video_id': '593a9b927fc5b81ea37b18f3',
    'title': '收藏！揭秘网红PS大法！（完整版）',
    'video_tag_list': '',
    'content': '#好用App推荐 #PS教程\n用到的app有：VSCO(滤镜）、facetune(修脸）、Spring（增高减肥）、PhotoGrid(加白边+拼图）\n之前只能发5分钟的，现在可以发完整版啦，看过的可以直接拉到5分01秒哦！'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liYd6O6D1K27wgmFDlSTxqb7JJuF_compress_L1',
    'video_id': '593aa34ad1d3b975f965b754',
    'title': '三木三山',
    'video_tag_list': '',
    'content': '我有两个好儿子，相互遛够，麻麻根本不用操心[偷笑R]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lil3N1NaCjIUB05TL0KDO7KGlXrA_compress_L1',
    'video_id': '593aabb3b46c5d719375ad9f',
    'title': '你的节操呢？？？',
    'video_tag_list': '给宝宝的mini情书',
    'content': '你是有多委屈呀？哭成这样😢，不知道的人还以为我虐待你了😒。为了吃到苹果🍎，你真是死劲力气了😒😒😒#小红书萌娃大赛[话题]##给宝宝的mini情书[话题]##我家宝宝超搞笑[话题]##戏精宝宝[话题]# @薯宝宝  @薯宝宝  @薯宝宝'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lr9vD4o2jvBCK8TXk2l28T8tyTua_compress_L1',
    'video_id': '593b6720d2c8a5163087a063',
    'title': '',
    'video_tag_list': '手机摄影好用利器;摩米士 momax 精英手机三脚架',
    'content': '一台手机、一个三脚架，差不多就实现了一个抽象主播的网红梦想。\n#手机摄影好用利器[话题]#\n'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/d809b7ce35eed935d6a2c77978aaf86fa7e483aa_r_ln',
    'video_id': '593b705514de4179f99e93c5',
    'title': '宝宝游戏',
    'video_tag_list': '宝宝早教这么做',
    'content': '会玩还是爸爸啊😘\ntb上随便买买彩色胶带粘起来就玩了😂不比游乐场差啊😱有没有😎\n#宝宝早教这么做[话题]# #新款宝宝玩具[话题]# #宝宝游戏区这么搭[话题]#\n#爸爸带娃记[话题]#   @薯宝宝'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/270x480/vcodec/libx264/pgc/6b519120-a731491-a94c-5fb9c913b897?sign=3b4e4b47a1e900c2255c00de272f8a57&t=65fb06d4',
    'video_id': '593b72aea9b2ed5676cfa0e7',
    'title': '周末早教在家做,快来教娃读首诗~~',
    'video_tag_list': '为你读诗;为你读诗',
    'content': '宝宝，你的平翘舌有时候分得很清楚，有时候分得不清楚，是咋回事儿呀~?[偷笑R] [偷笑R] [偷笑R]\n（吼吼吼~~~不过敲可爱哒！！！~~~[飞吻R] [飞吻R] [飞吻R] ）\n红薯地有多少薯宝会说话啦？\n只能不流畅地说几个词？\n还是能毫不费劲儿的沟通交流啦？\n没关系~~~\n都欢迎麻麻们上传#为你读诗[话题]# 视频笔记哦~\n记录下宝宝成长的每一步~~~[赞R] [赞R] [赞R]\n顺便看看，红薯地里到底有多少小学霸！！\n❤参与方式超简单吼！\n→ 1. 录下宝宝读诗的小视频~\n从【儿歌】到【古诗】，从【中文】到【英文】，哪怕只是【绘本小片段】或是【美文短句】~\n只要是宝宝会的“诗”，读也好，背也好！~\n快来和小红薯们分享宝宝成长的小喜悦！！~\n→ 2. 用文字写下宝宝读的是什么——有时候小宝宝难免口齿不太清楚，可以帮大家更好的GET哟~\n如果能顺便记录你的语言启蒙经验、育儿经验，还能得到更多薯妈的赞和收藏哦~~\n→3.一定一定一定！！ 记得在笔记中加上话题标签#为你读诗[话题]# ，并@薯宝宝 哈~~~\n❤❤还不得空录视频的麻麻们，先在评论里留言你家宝宝会的诗，当作报名吧！！\n本宝宝等着看一大堆萌娃的小视频和萌萌哒小奶音吼~~~[偷笑R] [偷笑R] [吧唧R] [吧唧R] [萌萌哒R] [萌萌哒R] 愉快周末，顺手录视频吧！~~！\n视频来自@迷你Michael'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/03dad87e9a699bfa18b5d6b600911f825cb9e137_v1_ln',
    'video_id': '593b82a57fc5b852b87b18e6',
    'title': '玩转网红盘canmake砍妹14秋冬眼影盘｜我最常画的三种画法',
    'video_tag_list': '',
    'content': '这个眼影盘之前答应分享画法 嗯我知道很久了\n所以今天来还flag了\n这三种画法都是我自己比较常用的画法\n可能有点浓？但是我自己觉得还挺好看的～\n悄悄地说一句这三个画法其实都挺像的哈哈哈哈\n#眼影画法大搜罗[话题]##眼影如何晕染[话题]##跟着视频画眼影[话题]##新手最容易上手的眼影盘[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lk67qCPvPAI9s7REOC8KRexhfpwq_compress_L1',
    'video_id': '593b861f14de4134e39e93b9',
    'title': '猫的自动贩售机笔下的猫🐱，已经可以从眼妆届改行了',
    'video_tag_list': '',
    'content': 'Long time no see！[喜欢]\n感觉发这篇笔记应该会有很多小伙伴认不出我……但是没办法呀，相机去修了好几天，也怪想你们哒，佳能那边告诉我起码要一周，只能先拿存货来发一发。\n上次分享了一些平时的小作品～有小红薯说想看过程，就录了一次，第一次录视频太紧张了[石化]画的不是很好…总是看我的手有没有出画，但好歹也比较完整！！！大家就凑合看吧！[活力]\n相机还没拿回来之前只能暂时分享一些除了眼妆以外的小东西，例如我的日常干嘛呀呀，穿搭呀，平时用的刷具什么的也有薯想看，趁这段时间慢慢充实一下笔记吧～\n视频是高速，其实画了四十多分钟，这样看起来比较爽，大家爽才是真的爽[活力][活力][活力]'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/li1lxg4No4mBsG8Qvg1rgHJnf5oy_compress_L1',
    'video_id': '593b969214de41625aded88d',
    'title': '宝爸和小情人的约会',
    'video_tag_list': '宝宝如何学游泳',
    'content': '#宝宝如何学游泳[话题]##儿童节送什么[话题]##爸爸带娃记[话题]# 送给宝宝一节亲子游泳🏊体验课  @薯宝宝\n我家小可爱特别喜欢水 平时洗澡游泳都不怕 自己拍水踢水玩 经常弄麻麻一身水[笑哭R] 考虑了很久 又和宝爸敲定了时间 送给宝宝一节亲子游泳体验课 整个过程宝宝都很放松 爸爸一只手托着宝宝就可以漂在水里 完全不怕 还尝试了一小段潜水 宝宝棒极了 没呛水也没哭 好勇敢 相信这次亲子游泳会是宝宝和爸爸一段非常甜蜜的回忆 拍了好多视频 可惜一次只能上传一个[叹气R]\n友情提示：宝宝8个月前有闭气反射 想尝试的爸妈尽量趁宝宝还小时去 另外40分钟的课宝宝和爸爸的体力消耗都蛮大的 挑宝宝状态好的时间游 宝妈体力不好的 就把这样的体力活交给爸爸吧 在旁边看也是很幸福的[偷笑R]\n坐标：苏州吴中万达金街艾贝瑞亲子游泳馆'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/f4ee85e4fc237bea79d60f1b2a0262cc7497e3ef_v1_ln',
    'video_id': '593b9d617fc5b87b4ec39a9e',
    'title': '做翻糖蛋糕从它开始：蜂蜜版翻糖膏',
    'video_tag_list': '',
    'content': '#烘焙大神的蛋糕食谱[话题]##烘焙能手[话题]##翻糖蛋糕[话题]#\n今天我来分享一款蜂蜜版翻糖膏的做法，不仅比买来的工业翻糖要好吃，而且食材和制作都非常简单，有了它就可以给各种蛋糕做出美美的装饰了！\n自制翻糖膏因为没有防腐剂，它的保质期没有工业翻糖膏长，密封储存一般可以保存1个月左右。\n时间越长，它会变得越硬，使用前揉软就会更费劲，花更长时间，所以不建议一次性做太多，做好后第二天使用效果最佳。\n翻糖膏的用处很广泛，可以用它来装饰各种蛋糕和饼干，这次我就用它来装饰纸杯蛋糕，做出我们每天都在用的Emoji表情造型。\n如需下载Emoji表情纸杯翻糖蛋糕模板，请在公众号聊天窗口回复：\n表情纸杯蛋糕\n即可免费获得下载地址。\n除了蜂蜜版翻糖膏，我还用到了可可味纸杯蛋糕和美式奶油霜。配方和制作方法我之前都已经分享过。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lksYNnWJt_b-evq1tl9fBKi1pTsZ_compress_L1',
    'video_id': '593b9d6fd1d3b9049788aaa8',
    'title': '超燃《未闻花名ed》♬ 女生必听版正片在中间哦',
    'video_tag_list': '66好物抢晒单',
    'content': '未闻花名是一首动漫的主题曲，讲述了一个唯美忧伤的故事~听的时候可以准备纸巾~( ๑ŏ ﹏ ŏ๑ )\n#我是歌薯[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/e661ba9a0544e587273e7b69115a70b1a6298844_v1_ln',
    'video_id': '593b9e3a7fc5b8204bc39aa2',
    'title': '0脂肪冰淇淋，只用3种食材，5分钟轻松搞定',
    'video_tag_list': '',
    'content': '今天我来分享一款0脂肪冰淇淋的做法，只用到了3种食材，5分钟轻松搞定，夏天可以敞开怀吃冰淇淋了！\n我这次用的是可可粉来做巧克力味的，你也可以做成其他口味的，比如放抹茶粉来做抹茶味的。\n#自制完美冰淇淋[话题]##夏日消暑吃什么[话题]##在家做甜品[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lg8fXAOymn1xjDtuqtx-t0pKKLpZ_compress_L1',
    'video_id': '593ba17dd1d3b904a965b755',
    'title': '小兔子和小猪#为你讲故事#一周11#',
    'video_tag_list': '为你读诗',
    'content': '一周11个月的大宝贝从在麻麻肚子里就听我讲故事，一周十语言爆发期后开始说了很多很多词语，只要我讲过一遍的故事或古诗或儿歌，她都能接上去后面的2-3-4个字。\n如何让孩子快速学会讲故事，古诗，儿歌？\n首先打动孩子的是你读起来抑扬顿挫的语调，这是直接吸引宝宝会否认真听你讲。\n其次是声情并茂的讲述，当你特别有感情和表情的去跟孩子讲这个故事，或古诗或儿歌，怎么能不吸引他们呢？\n最后能让孩子快速的记下来，并用他们的小嘴说出来的是，你适当的配合动作，当这个动作与这个动词在他们脑海中连接在一起时，很快词语就能从她们嘴里脱口而出。\n平时我家大宝在我讲故事时，会与我一起做动作和讲故事；这个视频是我刚生完二宝第一天的时候，没有办法蹦蹦跳跳，大宝只能根据我的声音给我回馈。如若我做动作，她会站起来跟我一起表演这个故事。\n这个故事的名字叫：小兔子和小猪\n小兔子，住木屋。\n有个邻居叫小猪。\n兔子夜里睡不着，\n都怪小猪打呼噜。\n这天，小猪回老家。\n兔子夜里却呜呜哭。\n你猜，兔子为什么哭？\n原来是想听小猪打呼噜。\n如果麻麻们感兴趣，等我出月子可以录个完整的声情并茂带动作的视频。😂😂\n#为你读诗[话题]# @薯宝宝 #一起读绘本[话题]##宝宝小才艺[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/li74NQpuMvgqA4N_5vpSiBzcIFb9_compress_L1',
    'video_id': '593ba939b46c5d2fae75ada4',
    'title': '跟着视频塑形手臂👉🏻瘦手臂动作示范，天鹅臂告别蝴碟袖',
    'video_tag_list': '无器械锻炼视频',
    'content': '结合上一篇:瘦手臂塑形笔记，录制视频。get有线条曲线的手臂塑形动作😘在家和寝室也能做。\n🌟🌟【手臂塑形减脂 的几大入手方面】🌟🌟\n【紧质有线条的手臂】＝有氧减脂＋器械 小哑铃等塑形＋合理饮食＋显瘦穿搭\n1.【体脂高，赘肉多的宝宝】＝多有氧减脂＋器械塑形＋合理饮食＋坚持\n2【体脂满意，手臂塑形为主】＝少有氧＋多器械塑形＋好的饮食＋坚持\n🌟🌟🌟【瘦手臂动作 安利】🌟🌟🌟\n手臂肌肉是小肌肉群，在平时锻炼健身时候，都会带到。\n道具准备：\n一对小哑铃 重量：2～5kg\n👉🏻【手臂塑形搭配选择】可以组合搭配在你那天要训练的部位一起➕配合有氧训练\n紧质的手臂】＝有氧减脂＋器械 小哑铃等塑形＋合理饮食＋显瘦穿搭\n1.【坐姿哑铃颈后臂屈伸】\n告别后臂肉肉，塑形。\n要点；双腿分开与臀部同宽，两手握住一个哑铃，用手臂后侧肌肉乏力，上举哑铃，然后再缓慢地弯曲手臂。\n感受：后臂有明显收缩、拉伸感。做的时候另一只手可以扶住手臂上次，帮助感受大臂肌肉收缩发力。\n数量：15*4\n2【哑铃向上抬】简单的动作 注意节奏\n3.【下拉划船】在家可以借助弹力带哦\n4【变式动态俯卧撑 】 交替手臂支撑，还 可以练到核心肚子！持续1分钟\n🌟🌟总结：🌟🌟🌟\n手臂肌肉是小肌肉群，在平时锻炼健身时候，都会带到。\n【减去手臂脂肪的捷径】＝多有氧减脂\n【体脂高，瘦手臂】＝多有氧减脂＋器械塑形＋合理饮食＋坚持\n【体脂低，手臂塑形】＝少有氧＋多器械塑形＋好的饮食＋坚持\n下期想看什么？都可以留言 留言～[得意]\n#健身靠装备[话题]##手臂如何塑形[话题]##手臂塑形视频[话题]##健身是把整容刀[话题]##好用家庭健身器械[话题]##在家徒手如何健身[话题]##必须要安利的健身动作[话题]##科学减脂食谱[话题]##减肥是女人一生的事业[话题]##无器械锻炼视频[话题]#\n@小红叔'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lsjc16sPe3-jbou9prxjbTLEuRXE_compress_L1',
    'video_id': '593bcefad1d3b9188265b744',
    'title': '三木三山',
    'video_tag_list': '',
    'content': '我就说，家里这俩儿子天天都是戏，三木啊，装一个迎接主人回家的孤寡残疾狗合适么……🙈🙉🙊快给我滚下来！😂'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/luxrEudT5Yv7U3eLV2Qp4lXFrWtH_compress_L1',
    'video_id': '593bd6f5b46c5d31bd6437da',
    'title': '男朋友猜化妆品之唇膏篇',
    'video_tag_list': '',
    'content': '录完之后我问他为什么猜canmake200元，jill stuart50元，他说canmake上面有日本字，他觉得日本的东西好像贵一些，然后说jill stuart做工太廉价，看着就便宜，哈哈哈，直男的思想😂'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/ljqmvRa2KEuGqv2BrMR5mhMQ4Qix_compress_L1',
    'video_id': '593be9e1b46c5d64f96437e0',
    'title': '街舞',
    'video_tag_list': '',
    'content': 'A舞库 编舞byGirin 《post to me》这个舞蹈超帅'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/FiFa8dDNQdl3irc9cSXrIAgOhQ26_compress_L1',
    'video_id': '593bea8614de415171ded88c',
    'title': '裸照公布啦🎊',
    'video_tag_list': '小红书萌娃大赛',
    'content': '谢谢大家这么喜欢😍他，我就曝光他沐浴后的模样。他自己害羞😳得不好意思啦。\n#小红书萌娃大赛[话题]##给宝宝的mini情书[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/b3dd0d06e1a6b75fc727bab6ececf7d6d0d7d9c4_v1_ln',
    'video_id': '593c15e7d1d3b971b965b747',
    'title': '瑜伽球训练！在家徒手健身也能瘦全身（跟圆肩驼背说拜拜！）',
    'video_tag_list': '见人不如健身',
    'content': '今天分享一套相对简单实用的瑜伽球训练！激活-训练-拉伸 腹部 背部 臀部 腿部都有～\n一套动作在家在宿舍练全身～\n大家按顺序做就行～\n因为之前有很多学生党宝宝吐苦水说没时间和条件去健身房训练,想要在家也能练的教程、所以就有了今天这套不用去健身房也能瘦全身紧全身的训练视频！\n只用买一个瑜伽球、一块小小的场地就可以练起来啦[赞R][赞R][赞R][赞R]\n瑜伽球按照自己的身高买（正规的健身球一般都是按身高来分大小号的）\n视频里的动作顺序是：\n核心激活（增强身体稳定性）\n核心腹部训练（练马甲线 改善骨盆前倾 缓解腰酸背痛）\n臀部激活训练（翘臀 缓解腰痛 改善骨盆前倾 帮助臀部肌肉发力）\n背部 肩袖肌群激活训练（改善圆肩驼背头前引  缓解肩颈不适 加强背部肌肉力量）\n下肢力量 腿臀部训练（翘臀 加强大腿肌肉力量 改善骨盆前倾 缓解腰痛 减少膝盖受伤风险）\n下肢力量及后背力量（改善上下交叉综合症的不适 加强大腿肌肉臀部肌肉力量 提高整体运动表现）\n臀部及大腿后侧训练（后侧链比较重要的两大肌群  改善骨盆前倾 翘臀 加强下肢力量 提高运动表现）\n以上动作都可以15-25次/组 做3-4组\n最后是全身上下的拉伸动作（比训练更重要的环节 不可忽略）\n拉伸动作从下肢到上肢 正面 侧面 都有 大家跟着视频做就行、每个动作保持15-25秒、每天做一做 不仅很舒服 觉得整个人都被拉开了长高了一样！特别是圆肩驼背和骨盆前倾平时身体僵硬的宝宝、坚持做真的会有收获！\n这些动作看着简单 但是其实要做好了还是会很累的！\n动作相对都较安全、没有跑跳等冲击力大的容易伤关节的动作、都是控制型动作、大家可以放心的练起来！\n为了让更多没办法去健身房或者经常出差在外的宝宝也能好好练起来、我最近会优先分享可以在家在宿舍在酒店也能练的小工具的训练方法！弹力带、麦管球、弹力圈、TRX等…\n最后友情提示一下正在心急减肥的宝宝～\n很多视频里的高效减脂训练动作、部分动作真的对关节的冲击力很大、对于关节不稳定、核心不会收紧的健身小白来说、带来的伤害是你们无法想象的、因为看似一样的动作、有的人健身五年、有的人健身2个月、做出来的效果是完全不一样的！所以不建议盲目的跟随和尝试、毕竟每个人的运动表现、身体差异都是参差不齐的、找适合自己的动作最重要！减脂也好、增肌也好、塑形也好、安全才是第一位！\n#举铁P.K.瑜伽[话题]##如何改善驼背的塑形[话题]##见人不如健身[话题]##健身是把整容刀[话题]##在家徒手如何健身[话题]##必须要安利的健身动作[话题]##健身靠装备[话题]##10斤减肥小目标[话题]##全身减脂教学视频[话题]##厉害了我的健身房[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lguUr-eACfJy3qr2qEgYIUWazCaH_compress_L1',
    'video_id': '593c1677d2c8a50f2a87a07a',
    'title': '这样的求婚，我服！',
    'video_tag_list': '感人求婚现场',
    'content': '#感人求婚现场[话题]# #520说爱你[话题]# 520那天我们舞蹈室是要搞活动的，然后就到步行街，前面一个快闪鬼步（学员只学了1个月），然后中间一个假人游戏（所有人不动），之后有一支舞蹈samsara然后快闪结束。大波哥在假人后竟然跟摄影师商量好跟我求婚，我不知道我还着急最后一支舞，为什么学生都没上来，我就跑去急急忙忙放音乐，后来学生告诉我，我回头看天上的条幅，我有点懵。哈哈，所谓一跪一跪又一跪，终于抱得美人归（虽然视频上的我好丑）\n几个问题：\n1、事后大波哥扫花瓣扫了半个小时\n2、我喊话筒是因为人太多，他声音好小我听不见\n3、为什么我没穿美美哒，哭。\n4、第一个音乐faded，第二首音乐我忘了，第三首samsara，还有一首告白气球，还有一首boy，自己对去吧。\n5、看完赶紧点赞！😉'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/90f2ac6ba24e05b7abb5e72368198737fc0d44c0_r_ln',
    'video_id': '593c29b4d1d3b928a365b744',
    'title': '6.10薛之谦上海演唱会，看完回来激动得睡不着！',
    'video_tag_list': '去听一场演唱会',
    'content': '#去听一场演唱会[话题]#\n没有买黄牛票，自己在大麦上原价抢到的票，觉得自己运气真是好到爆棚！\n内场观众席惊现沈梦辰，戚薇，王啸坤。嘉宾张靓颖，合唱暧昧。上海滩名嘴朱桢，助阵演舞台剧，上海不愧是主场，各种上海话乱开～气氛超级嗨！\n这是我看过的，最真实，最有趣，最有灵魂的一场演唱会。\n短片中老薛对曾经懵懂的自己，说谢谢你。\n谢幕时对观众深鞠一躬，他说承蒙关照。\n你值得所有的欢呼和掌声，你真的很棒，歌手薛之谦。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lr7GOejTFIuD-l2Q7maBZb89GBfQ_compress_L1',
    'video_id': '593cac59d1d3b9306688aaa3',
    'title': '这个小动作，帮你快速收好床笠、连衣裙（1/2）',
    'video_tag_list': '',
    'content': 'Polo 衫和吊带的整理方法也都在这里了\n其他空间的收纳陆续都会有，别急哦[笑哭R]\n这期视频分两部发，这是第一部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lvgkLY6b_x-RP1oCPSQggBnYdZS-_compress_L1',
    'video_id': '593cad7014de4161b6ded896',
    'title': '这个小动作，帮你快速收好床笠、连衣裙（2/2）',
    'video_tag_list': '',
    'content': 'Polo 衫和吊带的整理方法也都在这里了\n其他空间的收纳陆续都会有，别急哦[笑哭R]\n这期视频分两部发，这是第二部～'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lqmuwFD7LvHFohxkMIsROPArpcHs_compress_L1',
    'video_id': '593cad97b46c5d064e75ad9b',
    'title': '不去健身房在家里也可以减脂的运动-跳绳',
    'video_tag_list': '跳绳教学视频',
    'content': '【跳绳减脂】\n不想去健身房，不想每天起早去室外跑步有氧的的妹纸，就在家跳跳绳吧，跳绳也能让你让你减脂塑形哦。\n热身运动后：\n第一循环：跳绳一分钟+自重深蹲30个\n第二循环：跳绳一分钟+自重剪步30个\n第一和第二作为一组，可以做三组。\n一周3-4次多种形式的有氧训练，对于心肺运动和减脂都有很好效果。\n有氧前建议服用支链氨基酸，防止肌肉在有氧中流失过多。\n有氧有很多好处，但是平时也不要忽略了力量训练！\n运动后记得拉伸哦！\n#低强度有氧燃脂技巧[话题]##跳绳教学视频[话题]##全身减脂教学视频[话题]##大体重减脂分享[话题]##减肥是女人一生的事业[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/61062260a50e87854ba8402904abcc9ccb7870f9_r',
    'video_id': '593cb0137fc5b858977b18ff',
    'title': '【教你用两种工具画眼线 - 单眼皮/内双眼线画法教学】',
    'video_tag_list': '芭比波朗 Bobbi Brown 流云眼线膏;得鲜;单眼皮如何画眼妆',
    'content': '✔️苏妹儿的新一轮教学视频又来啦！继上次的画眉教程，这次是手把手教你如何画眼线！✌️\n我就是传说中的内双，离远看单眼皮😄相信很多小伙伴跟我一样，觉得单眼皮眼妆、眼线都好难画，那今天就来教大家如何画眼线能使眼镜又大又有神，还不会显臃肿。\n✨既然是功能帖，那必须来点儿硬货👍！左右眼我使用了不同工具来画：\n1️⃣左眼：眼线液笔 黑色\n2️⃣右眼：眼线胶/膏➕眼线刷\n✔️敲个黑板儿！虽然我是内双，但今天的眼线教程不止适用于单眼皮，双眼皮、三眼皮的小伙伴也都适合的哈！是一款比较日常，单纯顺着自己眼型进行一个眼尾拉长的、整体偏细的眼线，如果大家喜欢这个主题，我会继续出不同主题和画法的【眼线教学】，包括cat eye/ 猫眼，上扬、下垂、无辜眼等画法😏\n另外，如果大家有什么想看的主题也可以留言告诉我哦！\n.\n以上，你们学会了嘛？😉   @视频薯\n#眼线到底怎么画[话题]##新手也能用的易上手眼线笔[话题]##单眼皮如何画眼妆[话题]##眼妆每日打卡[话题]##入门级彩妆[话题]##我的彩妆测评[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/6d4edffa51a0092b6c6933a7fde5c1590bc920cf_r_ln',
    'video_id': '593cb817b46c5d1fb375adaa',
    'title': '6.10薛之谦上海演唱会（视频版）',
    'video_tag_list': '去听一场演唱会',
    'content': '#去听一场演唱会[话题]#\n做了个视频合集。其实完整是8分17秒。小红书只能裁其中的5分钟，想找的话根据水印去小影app找吧😂\n这是我看过的最真实，最有趣，最有灵魂的一场演唱会。薛之谦很认真。\n最后短片中老薛对曾经的自己说谢谢你，一直坚持没有放弃。\n谢幕时对观众深鞠一躬，他说：我回来了，承蒙关照。\n你值得所有欢呼和掌声，你真的很棒，歌手薛之谦。'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/llxDhFuBqrmYby7nslhqHIoINBF0_compress_L1',
    'video_id': '593cce8f14de4148399e93ca',
    'title': '布偶傻布偶',
    'video_tag_list': '',
    'content': '一大早把布偶提溜出来洗澡，布偶说：老子这是没来得及尿的晨尿，不是被吓尿了！😂😂😂'
  },
  {
    'video_url': 'https://sns-video-hw.xhscdn.net/ltRkBlD0vhzLkEf-cG1JXr73v_jL_compress_L1',
    'video_id': '593cd365d2c8a54c57652f37',
    'title': '只想安静做个美男子👼🏻',
    'video_tag_list': '',
    'content': '👼🏻萌宝：7⃣️个月半月啦🎊\n首先，谢谢大家点赞👍，这么喜欢我的儿子👼🏻，当妈的特别高兴😊，所以特地代表大家，对儿子👦一顿猛亲😘，哈哈😄。\n他👼🏻的一举一动、一颦一笑，每次都可以把我的心❤️融化，所以在这里，我想跟大家一起分享他的成长、他的快乐！🤗\n#小红书萌娃大赛[话题]# #给宝宝的mini情书[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/d70b57c334a7bd73bc4b843082355baa4498c45b_v1_ln',
    'video_id': '593d01a17fc5b836607b18ec',
    'title': '提拉米苏千层蛋糕，饿了困了来一块',
    'video_tag_list': '提拉米苏',
    'content': '#提拉米苏[话题]# 今天我来分享一款提拉米苏千层蛋糕的做法，它是提拉米苏和千层蛋糕的完美结合，享受蛋糕的同时还能提神，有了它再也不用喝苦咖啡了。\n冷藏好的提拉米苏千层蛋糕，口感冰冰的，奶油一点也不腻，饿了困了来一块，既顶饿还解困，一举两得。\n#烘焙能手[话题]##烘焙大神的蛋糕食谱[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/d51579a7cf947025f3eb5c8746234dbb883d5dd8_r_ln',
    'video_id': '593d03647fc5b84423c39aa3',
    'title': '美到舍不得吃的彩虹千层蛋糕-不用烤箱',
    'video_tag_list': '吃一道彩虹',
    'content': '今天我来分享一款彩虹千层蛋糕的做法，色彩缤纷，非常漂亮，味道也很美味，女孩子们一定很喜欢。\n当然你也可以用这个配方来做原色的千层蛋糕，无需调色了。\n另外如果你不打算做成彩虹的颜色，决定做素色的话，你也可以把其中的一部分低筋面粉替换成可可粉做成巧克力味的，薄饼就是咖啡色的。\n或者是替换成抹茶粉，做成抹茶味的，薄饼就是绿色的了。\n如果是做原色的千层蛋糕，填充除了可以用打发的奶油之外，你也可以用别的食材，比如用巧克力酱。\n你甚至都可以尝试用紫薯泥来给千层蛋糕做填充。\n#吃一道彩虹[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/lhxqJKeDaAaFJAhwk7fmr2XUC_kV_compress_L1',
    'video_id': '593d106db46c5d16bb6437e4',
    'title': '几款中长发造型分享',
    'video_tag_list': '年度最佳造型',
    'content': '厌倦了直发？快来看看中长发还可以做哪些造型～\n超简单省时哦！\n#最爱的女人味元素[话题]##年度最佳造型[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/liD_0ctEmwn4tTA8ukQoETa4CcqB_compress_L1',
    'video_id': '593d341fd1d3b9503b88aaa0',
    'title': '穿串儿神器哪家强',
    'video_tag_list': '美食才是人生主角',
    'content': '看完视频就知道了有多好使，肉摆上去，盖上盖子，夹住肉，签子一插就OK了，注意最好买我这种铁签子，我这个是配着烤串锅一起买的，大家也可以自己淘一下\n#厨房神器[话题]#\n#美食才是人生主角[话题]#\n#亲测好用的小厨具[话题]#'
  },
  {
    'video_url': 'https://sns-video-al.xhscdn.com/7d1a8b1072b42f51770f6e4600d673f97960ff32_v1',
    'video_id': '593d3cb6b46c5d12b36437e2',
    'title': '看完《神奇女侠》种草Gal，男盆友视角下的她那么甜～',
    'video_tag_list': '明星;神奇女侠',
    'content': '#做个侧脸女神[话题]##神奇女侠[话题]#\n看完《神奇女侠》，一直在吐槽Gal Dadot饰演的傻白甜女王，但是她的身材颜值双双上线，也是实力圈粉啊！\n这段视频是以男朋友视角看Gal Gadot的一天，也是甜到没sei了～相较于神奇女侠里没有bug的她，反而更喜欢现实里的她～😛'
  },
  {
    'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/2383f520-f5c6d92-a742-7b87a46e1af0?sign=d831062e5eebba89296097be16f39e12&t=65fb06d4',
    'video_id': '593d5bf77fc5b82a837b18e8',
    'title': '有了这个自制酸奶酱，三明治怎么吃都不胖',
    'video_tag_list': '',
    'content': '#早餐就爱三明治[话题]#\n很多饭友问我有没有适合减肥吃的三明治，毕竟吐司夹肉类本身热量就不低了，再涂上高热高脂的蛋黄酱或沙拉酱，确实容易超标。叔今天就教大家做一款低卡酸奶酱，很好的融合并提升了水浸金枪鱼的口感，成就一道335大卡且营养全面均衡的美味三明治。\n食材：水浸金枪鱼罐头固体部分取80克、全麦吐司两片约75克、小黄瓜1根修整后约70克、番茄取三薄片约60克、自制低卡酸奶酱约60克。\n酸奶酱材料：希腊酸奶40克、橄榄油3克、白醋5毫升、泰国鱼露10毫升、白胡椒粉2克。'
  }
]
])


class ClsRequest(BaseModel):
    title: str = Field(..., description="视频标题", example="这个蜜桃味唇油可爱到我心里了 有被惊喜到")
    content: str = Field(..., description="视频文字内容",
                         example="唇油;唇蜜;变色唇膏;水光唇釉;美妆好物;apieu;apieu唇油")


class GetDataRequest(BaseModel):
    start_time: str = Field(None, description="大于该时间的数据，不传全量", example="2024-04-02 11:27:26")
