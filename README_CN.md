# Zelda3 中文版

基于 [snesrev/zelda3](https://github.com/snesrev/zelda3) 的《塞尔达传说：众神的三角力量》C 语言重制版，新增完整中文支持。

## 特性

- 397 条对话全部翻译为简体中文
- 使用 [Ark Pixel 12px](https://github.com/TakWolf/ark-pixel-font) 像素字体（SIL OFL 开源协议），复古风格完美契合
- 蓝色描边 + 白色主体的双色字体，与原版英文字体风格一致
- 1118 个 CJK 汉字，通过转义前缀编码，兼容原有文本系统
- 支持 Mac 和 Nintendo Switch 双平台

## 截图

（待添加）

## 构建步骤

### 前置条件

- 美版 ROM 文件 `zelda3.sfc`（SHA256: `66871d66be19ad2c34c927d6b14cd8eb6fc3181965b6e517cb361f7316009cfb`）
- Python 3 + Pillow 库：`pip install pillow`
- SDL2：`brew install sdl2`（macOS）

### Mac 构建

```bash
# 1. 将 ROM 放到项目根目录
cp your_rom.sfc zelda3.sfc

# 2. 生成中文字体
python3 tools/generate_font_cn.py

# 3. 提取资源并生成中文资源包
cd assets && python3 restool.py --extract-from-rom --languages cn
cd ..

# 4. 编译
make

# 5. 配置语言（编辑 zelda3.ini，设置 Language = cn）
# 6. 运行
./zelda3
```

### Nintendo Switch 构建

需要先安装 [DevKitPro](https://devkitpro.org/wiki/Getting_Started)。

```bash
# 安装 Switch 开发工具
sudo dkp-pacman -S switch-dev switch-sdl2 switch-tools

# 设置环境变量
export DEVKITPRO=/opt/devkitpro
export DEVKITA64=$DEVKITPRO/devkitA64
export PATH=$DEVKITPRO/tools/bin:$DEVKITPRO/devkitA64/bin:$PATH

# 清除 Mac 编译产物（避免 VPATH 冲突）
make clean_obj

# 编译 Switch 版本
cd src/platform/switch
make clean && make -j$(sysctl -n hw.ncpu)
# 输出：zelda3.nro
```

### Switch 部署

将以下文件复制到 Switch SD 卡的 `/switch/zelda3/` 目录：

| 文件 | 来源 |
|------|------|
| `zelda3.nro` | `src/platform/switch/zelda3.nro` |
| `zelda3_assets.dat` | 项目根目录 |
| `zelda3.sfc` | 你的 ROM 文件 |
| `zelda3.ini` | 项目根目录（设置 `Language = cn`） |

建议在 `zelda3.ini` 中设置 `ExtendedAspectRatio = 16:9` 以适配 Switch 屏幕。

通过 Homebrew Launcher 启动即可。

## 技术实现

### 文本编码

采用 EU 风格的"new"编码格式：
- 字节 0x00-0x6E：111 个单字节字符（95 个 US 字母 + 16 个中文标点）
- 字节 0x6F-0x73：转义前缀，后跟 1 字节 → CJK 字符索引（容量 1280 > 实际 1118）
- 0x7F：消息结束，0x80-0x87：控制命令（与 EU 相同）

### 字体渲染

- CJK 字符使用 16x16 像素，以 4 个 8x8 SNES 2BPP tile 存储
- 像素值 1 = 蓝色描边（SNES 调色板颜色 1），像素值 2 = 白色主体（颜色 2）
- `dialogue_flags` 第 2 位（值 4）= 中文模式
- VWF（Variable Width Font）渲染，宽度上限 13px，每行约 12 个汉字

### 修改的文件

| 文件 | 说明 |
|------|------|
| `assets/text_compression.py` | LangCN 类，CJK 转义编码 |
| `assets/sprite_sheets.py` | 16x16 中文字体编码，宽度表 |
| `assets/compile_resources.py` | CN 语言标志位 |
| `src/messaging.c` | 中文文本解码 + VWF 渲染 |
| `src/messaging.h` | 函数声明 |
| `src/platform/switch/Makefile` | Switch 交叉编译路径修复 |

### 新增的文件

| 文件 | 说明 |
|------|------|
| `tools/generate_font_cn.py` | 中文字体生成器（含描边） |
| `tables/dialogue_cn.txt` | 397 条中文对话翻译 |
| `tables/font_cn.png` | 中文位图字体（1134 字符） |
| `tables/ark-pixel-12px-zh_cn.otf` | Ark Pixel 像素字体 |
| `tables/FONT_LICENSE` | 字体 SIL OFL 许可证 |

## 许可证

本项目遵循 MIT 许可证，与原 zelda3 项目一致。

中文字体使用 [Ark Pixel](https://github.com/TakWolf/ark-pixel-font)，遵循 SIL Open Font License 1.1。

中文翻译由 AI 生成。
