# study-lang-family

学习 LangChain、LangGraph、LangSmith 的代码与笔记。

## 环境

| 项 | 值 |
| --- | --- |
| Python | 3.13 |
| 环境管理 | conda，环境名 `langchain1.2` |
| langchain | 1.2.12（core 1.2.18） |
| langgraph | 1.1.2 |
| langsmith | 0.14.14 |
| 模型 | deepseek-flash（DeepSeek）；qwen3.8-flash / qwen3-vl-plus（阿里云百炼，OpenAI 兼容接口） |

## 目录

```
01-langchain/     LangChain 主体
02-langgraph/     LangGraph
03-langsmith/     LangSmith
projects/         实战项目
docs/             环境搭建、API 速查
```

每章文件平铺，文件名带章节号：

```
ch02-model.ipynb
ch03-message.ipynb
images/
```

## 笔记

| 文件 | 内容 |
| --- | --- |
| [ch02-model.ipynb](01-langchain/ch02-model.ipynb) | 模型创建、参数、invoke 与三种输入格式 |
| [ch02-profile-initparams-config.ipynb](01-langchain/ch02-profile-initparams-config.ipynb) | 模型 profile、完整初始化参数、model_kwargs、extra_body、config |
| [ch03-message.ipynb](01-langchain/ch03-message.ipynb) | 消息类型与格式、对话历史管理与优化、多轮机器人、content_blocks |
| [ch04-prompt_templates.ipynb](01-langchain/ch04-prompt_templates.ipynb) | 提示词模板：实例化方式、调用方式、初始化参数类型、消息占位符、可复用模板库 |
| [ch05-tools.ipynb](01-langchain/ch05-tools.ipynb) | 工具调用：直接调用与 bind_tools、消息流转、convert_to_openai_tool、@tool 装饰器、parse_docstring、args_schema（Pydantic / JSON Schema） |
| [ch06-structured-Output.ipynb](01-langchain/ch06-structured-Output.ipynb) | 结构化输出：四种 Schema 方式对比、Pydantic 模型与 Field、SecretStr、Optional 默认值、枚举与 Literal、列表提取、嵌套结构 |
| [ch07-Agent.ipynb](01-langchain/ch07-Agent.ipynb) | 智能体：create_agent 参数、绑定工具与重试、结构化输出（ProviderStrategy / ToolStrategy / AutoStrategy）、handle_errors 错误处理、流式输出、多工具 CLI 助手实战 |
| [langsmith-test.ipynb](03-langsmith/langsmith-test.ipynb) | LangSmith 接入与监控指标 |

## 进度

| 章节 | 内容 | 状态 |
| --- | --- | --- |
| 01 | LangChain 1.2 概述 | 完成 |
| 02 | 模型的创建与调用 | 完成 |
| 03 | 消息 | 完成 |
| 04 | 提示词模板 | 完成 |
| 05 | Tools | 完成 |
| 06 | 结构化输出 | 完成 |
| 07 | 智能体 | 完成 |
| 08 | 中间件 | 待学 |
| 09 | 上下文与记忆 | 待学 |
| 10 | RAG | 待学 |

另有 [03-langsmith/](03-langsmith) 记录 LangSmith 接入与监控，进行中。

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
