# study-lang-family

跟随尚硅谷课程学习 LangChain、LangGraph、LangSmith 的代码与笔记。

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
01-langchain/     LangChain 主体：模型、消息、提示词、链、RAG、Agent
02-langgraph/     LangGraph：状态图、多智能体
03-langsmith/     LangSmith：追踪与评测
projects/         综合实战项目
docs/             环境搭建、API 速查
```

每节课一个文件夹，代码、笔记、截图放在一起：

```
ch01-model-init/
├── 01-model-init.ipynb
├── note.md
└── images/
```

## 进度

| 章节 | 内容 | 状态 |
| --- | --- | --- |
| ch01 | 模型初始化、invoke、温度与长度参数 | 完成 |
| ch02 | 消息类型、多轮对话 | 完成 |
| ch03 | 提示词模板 | 待学 |
| ch04 | 输出解析 | 待学 |
| ch05 | 链与 LCEL | 待学 |
| ch06 | RAG | 待学 |
| ch07 | Agent 与工具 | 待学 |

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
- 提交信息带章节号：`ch02: 补充消息类型笔记`
- 提交前清除 notebook 输出：

```bash
pip install nbstripout
nbstripout --install
```

## 笔记索引

- [环境搭建与踩坑记录](docs/setup.md)
- [常用 API 速查](docs/cheatsheet.md)
