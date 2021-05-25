# JDMemberCloseLinks

本项目旨在使用京东cookie一键生成所有退会链接

本项目大部分代码基于 https://github.com/yqchilde/JDMemberCloseAccount （MIT协议开源）

## 使用方法

1. 克隆到本地

    ```shell
    git clone https://github.com/hyzaw/JDMemberCloseLinks.git
    ```

2. 安装所需要的依赖包


    ```shell

    pip install -r requirements.txt 
    或 
    pip3 install -r requirements.txt

    ```
    当网速很慢式可以考虑，先添加pip的清华源后，再执行上述命令
    ```
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    或
    pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    ```

3. 运行程序

    ```shell

    python main.py
    或
    python3 main.py
    ```

## 注意
   由于，脚本运行时需要连接到京东，需要国内ip连接。使用代理时如果出现闪退或报错，请尝试关闭代理软件！
