# OCR_ElectricityMeter
基于`text_renderer`库，针对电表图像，制作OCR文本图像模拟数据集

# 环境安装
- `Anaconda`:推荐使用该工具进行环境管理，百度搜索安装教程即可。如果不想使用也可以不安装
- `Python3.7`
- `opencv-contrib-python3.4.2.17`

# 代码目录
- `data`：
    - `bd`:存放背景照片
    - `chars`:存放字典txt，注意，这里的字典里面不能有`blank`
    - `corpus`:语料库-文本txt，`chn`模式中有相应代码会从中随机提取定长字符串
    - `fonts`:字体文件
    - `fonts_list`:字体文件路径
    - `list_corpus`:列表语料库-文本txt，`list`模式中有相应代码从中随机提取一行字符串
- `config`:`default.yaml`文件会配置相关文本生产方式，支持旋转、模糊等数据增强
- `output`:默认图片保存路径
- `imgs`:存放展示效果图片
- `gists`:几何变换等相关代码
- `libs`:代码基础工具库
- `textrenderer`:核心代码
    - `corpus`:
        - `chn_corpus.py`:读取语料库文件，将其拼接为一个长字符串，然后随机提取一定长度的字符串
        - `list_corpus.py`:定义读取字符串列表中的一行字符串
- `tools`:
    - `check_font.py`:检查字体
- `dict_make`:字典文件生成代码
- `elec_data_make`:电表相关数据生成
- `label_index_make`:标签修正，将字符标签改为基于字典索引的标签，按比例划分训练集和测试集

# 使用教程
以`list`模式为例，给定一个语料库，每行是希望生成的字符串，每次从中随机提取一行生成文本图像，并给出对应文字标签。
- **更改配置**：在`parse_args.py`文件中更改对应选项，语料库文件、字典、图像数量、大小、模式等
- **更改数据增强方式**：在`config/default.yaml`文件中更改对应数据增强方式和效果
- **运行**:运行`main.py`文件代码，会在给定目录中生成图像和对应标签。

# 参考
- https://github.com/Sanster/text_renderer
如有侵权，务必告知
