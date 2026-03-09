#!/usr/bin/env python3
"""Generate font_cn.png for zelda3 Chinese language support.

Creates a bitmap font image with 16x16 pixel CJK characters arranged in a grid.
The image uses palette mode with 4 colors (matching 2BPP SNES format):
  0 = transparent, 1 = color1, 2 = color2, 3 = color3

Layout:
  - 32 characters per row
  - First 112 entries: Latin/symbol characters (from US font, reused in encode_font_cn)
  - Remaining entries: 1118 CJK characters at 16x16

This script only generates the CJK portion. The US font portion is handled
by encode_font_cn() which reads from the existing US font.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'assets'))

from PIL import Image, ImageFont, ImageDraw

# The sorted CJK characters from dialogue_cn.txt
CJK_CHARS = list(
  '一七万三上下不与专且世东丢两个中丰临为主丽举久么义之乎乐也书买乱了予争事于亏互井亚些亡交产亮亲人什仇今仍从仔他付代令以们件价任份仿企伏伐休众优伙会伟传伤伴伸似但位住佐体何佛作你使供侬便保信倒候借值假做停健偷储像儿允充先光克免兔入全公六共关兴兵其具兹内再冒冰冲冷冻准减凝几凭凶出击刃分切划列则创利别刮到制刺刻前剑剧剩副劈力办功加务动助励劲劳势勇勉勾匙匠升午半单卖南卜占卡卢卦卫印危即厄厅历厚原去又及友双反发取受变口古另叨只叫召可右吃各合吉吊同名后向吗吞否吧听启吱吵吸吹呀呃告员呢呣周呱呼命和咒咔咕咳咻品哇哈响哟哥哦哪哼唠唤唯商啊啦喂喜喝嗝嗯嘛嘟嘿噜器噬囚四回因团围国图土圣在地场坏块坚坠坦型埋城堂堡塔塘塞墓墙增壁士声处备复外多够大天太夫失头夺奇奏奖套女她好如姆始姿婆子字存孙学孩它守安完官定宜宝实宠客室宫害家容寄密寒对寻封射将小少尔尝就尼尽局层居展属山岩巢工左巧巨差己已布师希带帮常干平年并幸广庄庆应底店座庭康建开弃弄式弓引弟张弥弱弹强当形影彻往征待很徊律得徘御德徽心必忘忙快怀态怎怕思怪总恐恢恭息恶情惊惑惜惠惫想惹意感愧愿慧慰憾懂懦戏成我或战房所扇手才打扔托扛扭扯扰找承技把抓投抚抢护报抱抵担拉拔拖招拜拥择拯拾拿持指按挑挖挡挥捕换捣据掉掘探接控推掩掷描提揭搜搞搬携摧摸撞擅操攀攒支收改攻放故敌救教敢散数整文斗料断斯新方旁旅旋族无既旧早时明易映是晕晚晨普晶智暖暗暴曦曲更曾替最月有朋服望期木未本机杀杆村杖束条来松林枚果枝架某查标树样根格桩梭棋棒森棵楼概模横次欢欲欺歉止正此步武死殿毁每比毛氏民气水永求池汪沉沙没河治沼沿泉泊法注泰泽洒洞活派流浪海消涌涡深混清游湖湛滚满漆漠漩漫潜澈激瀑灌火灭灯灵灾炎炸点炼烂烈烦热焰然照熬燃爆爪爱父爽片牌牢物牵特犯狂独猩献猴王玛玩环现珍珠球理瓦瓶甚甜生用由甲界留疑疲病痛登白百的皮益盖盗盛目直相盼盾看真眠眩眼着睛睡瞄瞌矗知石砍破砸确碍碎碑示礼祈祝神祭祷禁福离种科秒秘积称移稀稍穆穴空穿突窝立站竟章笛第笼等答策简算管箭箱篷类粉精糊糟系索紧繁红约级纪纳纵线细终经绑结绕给绝统继绩续绿缉缩缺罐网罩罪置美群老者而耗聊联聚肉股肯胖胜能脉脚脸腿臂自至致舒舞色节花英荡荣药获莽菇萨落蒙蓄蓝蔽蕴藏蘑虫蛋蛰蜂蜜血行衣表被裂装裔西要见观视觉角解触言计认让议记讲讶许论设访证识诉试诚话该语误说请诺读谁调谋谎谓谢负贤败贪购贵费贼资赏赐赚赢赫走赶起趁越趣足跑跟路跳踢蹦蹼身躲轻辈辉输边达过迎运近还这进远连述迷追退送逃选途通逛逝造遇遍道遗遭避那邦邪部都配酷释里重量金针钥钩钱铁铠铲银铺链锁错锤键锻镖镜长门闪闭问闯闲间闻阴阵阿附陈降院除险陪陶随隐难雄集雨雾需震非靠面靴音顶顺须顾预领颗题颜风飞饰香马驱骑骗骚骨骷髅高鬼魂魔鱼鲁鸟麻黄黑鼾齐龟'
)

# CN punctuation characters (positions 96-111 in the alphabet)
CN_PUNCT = ['，', '。', '！', '？', '…', '：', '、', '—', '（', '）', '《', '》', '\u201c', '\u201d', '\u2018', '\u2019']

CHARS_PER_ROW = 32
CELL_SIZE = 16
FONT_PATH_DEFAULT = '/System/Library/Fonts/STHeiti Medium.ttc'
FONT_SIZE_DEFAULT = 12

# Ark Pixel 12px - pixel-perfect bitmap font for retro games (SIL OFL license)
FONT_PATH_PIXEL = os.path.join(os.path.dirname(__file__), '..', 'tables', 'ark-pixel-12px-zh_cn.otf')
FONT_SIZE_PIXEL = 12


def generate_font_cn(output_path):
  """Generate the CJK font image.

  The image contains CN punctuation (16 chars) + CJK chars (1118) = 1134 chars total.
  These map to alphabet positions 96-111 (punct) and CJK indices 0-1117.
  """
  all_chars = CN_PUNCT + CJK_CHARS
  num_chars = len(all_chars)
  num_rows = (num_chars + CHARS_PER_ROW - 1) // CHARS_PER_ROW

  img_w = CHARS_PER_ROW * CELL_SIZE
  img_h = num_rows * CELL_SIZE

  # Create grayscale image, render, then threshold to 1-bit
  img = Image.new('L', (img_w, img_h), 0)
  draw = ImageDraw.Draw(img)

  # Use pixel font if available, fall back to system font
  if os.path.exists(FONT_PATH_PIXEL):
    font = ImageFont.truetype(FONT_PATH_PIXEL, FONT_SIZE_PIXEL)
    print(f'Using pixel font: {FONT_PATH_PIXEL}')
  else:
    font = ImageFont.truetype(FONT_PATH_DEFAULT, FONT_SIZE_DEFAULT)
    print(f'Using system font: {FONT_PATH_DEFAULT}')

  for i, ch in enumerate(all_chars):
    col = i % CHARS_PER_ROW
    row = i // CHARS_PER_ROW
    x = col * CELL_SIZE
    y = row * CELL_SIZE

    # Get bounding box to center the character
    bbox = font.getbbox(ch)
    char_w = bbox[2] - bbox[0]
    char_h = bbox[3] - bbox[1]

    # Center horizontally, align to top with small offset
    dx = (CELL_SIZE - char_w) // 2 - bbox[0]
    dy = (CELL_SIZE - char_h) // 2 - bbox[1]

    draw.text((x + dx, y + dy), ch, fill=255, font=font)

  # Threshold to binary body mask, then dilate to create outline
  pixels = img.load()

  # Step 1: Create binary body mask
  body = [[pixels[px, py] > 80 for px in range(img_w)] for py in range(img_h)]

  # Step 2: Dilate body by 1 pixel to get outline region
  dilated = [[False] * img_w for _ in range(img_h)]
  for py in range(img_h):
    for px in range(img_w):
      if body[py][px]:
        for dy in range(-1, 2):
          for dx in range(-1, 2):
            ny, nx = py + dy, px + dx
            if 0 <= ny < img_h and 0 <= nx < img_w:
              dilated[ny][nx] = True

  # Step 3: Assign colors — body=2 (white), outline only=1 (blue)
  palette_img = Image.new('P', (img_w, img_h))
  palette_pixels = palette_img.load()

  for py in range(img_h):
    for px in range(img_w):
      if body[py][px]:
        palette_pixels[px, py] = 2  # White body
      elif dilated[py][px]:
        palette_pixels[px, py] = 1  # Blue outline
      else:
        palette_pixels[px, py] = 0  # Transparent

  # Set a simple palette (similar to existing font PNGs)
  pal = [0] * 768
  # Color 0: transparent (background gray)
  pal[0], pal[1], pal[2] = 192, 192, 192
  # Color 1: light
  pal[3], pal[4], pal[5] = 128, 128, 128
  # Color 2: medium
  pal[6], pal[7], pal[8] = 64, 64, 64
  # Color 3: full
  pal[9], pal[10], pal[11] = 0, 0, 0
  palette_img.putpalette(pal)

  palette_img.save(output_path)
  print(f'Generated {output_path}: {img_w}x{img_h}, {num_chars} characters ({len(CN_PUNCT)} punct + {len(CJK_CHARS)} CJK)')


if __name__ == '__main__':
  output = os.path.join(os.path.dirname(__file__), '..', 'tables', 'font_cn.png')
  if len(sys.argv) > 1:
    output = sys.argv[1]
  generate_font_cn(output)
