## API 报文说明

本 API 通过字符串和软件模块的 C++ 代码进行通信。字符串即输入输出的报文，其格式定义如下：



### 推断模块输入报文

```txt
[
    {
        "imaging": "II_shoulder_3#102",               # 图片ID（命名规则参见以下链接）
        "product": "default",                         # 类别名称（默认是 default）
        "image_share_path": "ShareMem_Name_1_1"       # 图片在共享内存中的映射名
        "image_w": 4096,                              # 图片宽度
        "image_h": 3000,                              # 图片高度
        "image_c": 1,                                 # 图片通道数
        "image_size": 12288000                        # 图片在共享内存中所占字节数
    },
    {
        "imaging": "II_tip_1#102",                    # 图片ID（命名规则参见以下链接）
        "product": "default",                         # 类别名称（默认是 default）
        "image_share_path": "ShareMem_Name_1_1"       # 图片在共享内存中的映射名
        "image_w": 4096,                              # 图片宽度
        "image_h": 3000,                              # 图片高度
        "image_c": 1,                                 # 图片通道数
        "image_size": 12288000                        # 图片在共享内存中所占字节数
    },
    ...
]
```

**NOTE**：图片ID ``imaging`` 的命名规则参照：[【金山文档】 原始数据命名规则](https://kdocs.cn/fl/srYFoeqda)



### 推断模块输出报文

```txt
[
    # 第一张图检测结果（结果按输入图片顺序输出）
    {
        "exception_info": null,          # 检测期间发生的异常，是个字符串；无异常时显示 null
        "imaging": "II_shoulder_3#102",  # 图片ID，和输入图片的 imaging 变量一致
        "product": "default",            # 产品名称，和输入图片的 product 变量一致
        "defects": [
            # 第一个缺陷
            {
                "defect_type": "starving",   # 缺陷类型（所有缺陷类别的集合待定）
                "defect_x": 29,              # 缺陷左上角x轴坐标
                "defect_y": 162,             # 缺陷左上角y轴坐标
                "defect_w": 199,             # 缺陷宽度
                "defect_h": 10,              # 缺陷长度
                "attributes": {...}          # 缺陷特征，内容待定
            },
            ...
        ],
        "debug_info": {...}  # 算法 debug 信息，内容待定
    }
]
```



## 使用说明

我们用类来封装连个模块。废话不多说，程序员喜欢直接上代码：

```python
from pipeline import build_pipline

# 初始化推断模块
pipeline = build_pipline(gpu_id=0)  # gpu_id = -1 时使用cpu； debug = True 保存从共享内存图片； action = False 总是输出OK结果

# 根据输入报文进行推断
input_string = 'blah blah ...'
output_string = pipeline.infer(input_string)
```

一个立马可运行的代码是主文件夹的`demo.py`，建议先试试看 （前提是先按下面的安装说明安配置好算法环境）。



## 安装说明

Pipeline API 的代码通过 gitlab 管理，代码以外的大文件都用 dvc 工具管理，通过其它通信渠道保持更新。加载代码需要从 gitlab 克隆代码仓库：

```shell
git clone git@192.168.10.30:Algorithm4/Programs/Bearing/pipeline.git
sh setup.sh
```
