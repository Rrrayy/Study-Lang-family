# study-lang-family

学习 LangChain、LangGraph、LangSmith 的代码与笔记。

## 环境

| 项 | 值 |
| --- | --- |
| Python | 3.13 |
| 环境管理 | conda，环境名 `langchain1.2` |
| langchain | 1.2.12 |
| langchain-deepseek | 1.0.1 |
| 模型 | deepseek-flash（DeepSeek） |

## 目录

```
01-langchain/     LangChain 主体
02-langgraph/     LangGraph
03-langsmith/     LangSmith 深入用法
projects/         实战项目
docs/             环境搭建、API 速查
```

每节一个文件夹，代码、笔记、截图放在一起：

```
ch02-model-init/
├── 02-model-init.ipynb
├── note.md
└── images/
```

## 进度

| 章节 | 内容 | 状态 |
| --- | --- | --- |
| 01 | LangChain 1.2 概述 | 完成 |
| 02 | 模型的创建与调用 | 完成 |
| 03 | LangSmith 基本使用 | 待学 |
| 04 | 消息与提示词模板 | 进行中 |
| 05 | Tools | 待学 |
| 06 | 结构化输出 | 待学 |
| 07 | 智能体 | 待学 |
| 08 | 中间件 | 待学 |
| 09 | 上下文与记忆 | 待学 |
| 10 | RAG | 待学 |

## 快速开始

```bash
git clone https://github.com/Rrrayy/Study-Lang-family.git
cd Study-Lang-family

conda create -n langchain1.2 python=3.13 -y
conda activate langchain1.2
pip install -r requirements.txt

cp .env.example .env        # 填入自己的 DEEPSEEK_API_KEY
```

## 约定

- `.env` 不入库，密钥只留在本地
- 目录命名 `chNN-主题`，NN 为章节号
- 提交信息带章节号：`ch04: 补充消息类型笔记`
- 提交前清除 notebook 输出：`pip install nbstripout && nbstripout --install`

## 笔记索引

- [环境搭建与踩坑记录](docs/setup.md)
- [常用 API 速查](docs/cheatsheet.md)
