# LangGraph

状态图、节点与边、多智能体编排。

学习开始后按 `chNN-主题` 建立子目录（或单文件），本文件同步维护章节表。

## 环境

独立于 `01-langchain` 使用的 `langchain1.2` 环境，互不影响：

| 项 | 值 |
| --- | --- |
| conda 环境名 | `langgraph` |
| Python | 3.13.18 |
| 依赖来源 | 课程 `2.资料/requirements_full.txt`（含 jupyter 与 langgraph-cli），2026-11-20 安装 |
| pip 镜像 | 清华源（全局配置） |

常用命令：

```bash
conda activate langgraph          # 命令行进入环境
jupyter notebook                  # 本目录下启动笔记
```

PyCharm 使用方式：**单独打开本目录作为项目根**（File → Open → 选择 `02-langgraph`），
解释器选 Conda 环境 `langgraph`（Settings → Python Interpreter → Add → Conda → Existing）。
`.idea/` 已被仓库根 `.gitignore` 排除，不会入库。

## .env

本目录下已放置 `.env`（与根目录同源，含 `DEEPSEEK_API_KEY` 等），
`load_dotenv(override=True)` 直接可用；该文件已被 `.gitignore` 排除。

## 章节

| 文件 | 内容 | 状态 |
| --- | --- | --- |
| test_env.py | 环境验证脚本（Python / 依赖版本 / .env / 模型调用） | 就绪 |
