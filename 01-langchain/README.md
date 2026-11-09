# LangChain

文件平铺在本目录，文件名带章节号。

## 已有文件

| 文件 | 内容 |
| --- | --- |
| [ch02-model.ipynb](ch02-model.ipynb) | 模型创建、参数、invoke 与三种输入格式 |
| [ch02-profile-initparams-config.ipynb](ch02-profile-initparams-config.ipynb) | 模型 profile、完整初始化参数、model_kwargs、extra_body、config |
| [ch03-message.ipynb](ch03-message.ipynb) | 消息类型与格式、对话历史管理与优化、多轮机器人、content_blocks |
| [ch04-prompt_templates.ipynb](ch04-prompt_templates.ipynb) | 提示词模板：实例化方式、调用方式、初始化参数类型、消息占位符、可复用模板库 |
| [ch05-tools.ipynb](ch05-tools.ipynb) | 工具调用：直接调用与 bind_tools、消息流转、不用 @tool 的定义方式、convert_to_openai_tool、@tool 装饰器 |

## 规划（按课件一级节）

| 章 | 文件 |
| --- | --- |
| 05 | `ch05.1-tool-def.ipynb` → `ch05.2-tool-decorator.ipynb` → `ch05.3-tool-practice.ipynb` |
| 06 | `ch06.1-structured-output.ipynb` → `ch06.2-structured-output-extra.ipynb` |
| 07 | `ch07.1-agent-basics.ipynb` → `ch07.2-agent-tools.ipynb` → `ch07.3-agent-advanced.ipynb` → `ch07.4-agent-project.ipynb` |
| 08 | 按课件一级节切文件 |
| 09 | `ch09.1-short-term-memory.ipynb` → `ch09.2-long-term-memory.ipynb` |
| 10 | 按课件一级节切文件 |

## 约定

- 换章新建 `chNN-主题.ipynb`；章内切到课件的一级节新建 `chNN.M-主题.ipynb`
- 理论/概述节不单独建文件，写进该章 `chNN-note.md` 或并进下一个文件
- 同一节里的小实验继续用当前文件
- 截图统一放 `images/`，笔记引用 `images/xxx.png`
- 某章文件超过四个时，可收进 `chNN-主题/` 目录（目前仅 ch07 预留）
