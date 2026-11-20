# test_env.py —— LangGraph 环境验证脚本（来自课程 00-环境配置.md 第 8 节）

print("环境验证开始")
print("=" * 40)

# 1. Python 版本
import sys
print(f"Python 版本: {sys.version.split()[0]}")

# 2. 关键包
from importlib.metadata import version as pkg_version
print(f"LangGraph 版本: {pkg_version('langgraph')}")

import langchain_core
print(f"LangChain Core 版本: {langchain_core.__version__}")

import pydantic
print(f"Pydantic 版本: {pydantic.__version__}")

# 3. .env 加载
from dotenv import load_dotenv
import os
load_dotenv(override=True)

deepseek_key = os.getenv("DEEPSEEK_API_KEY")
if deepseek_key:
    print(f"DeepSeek API Key 已配置: {deepseek_key[:8]}...{deepseek_key[-4:]}")
else:
    print("⚠️  未检测到 DEEPSEEK_API_KEY，请在 .env 文件中配置")

# 4. 模型调用测试
if deepseek_key:
    from langchain_deepseek import ChatDeepSeek
    model = ChatDeepSeek(model="deepseek-v4-flash")
    response = model.invoke("回复'一切正常'四个字，不要其他内容")
    print(f"模型调用测试: {response.content}")
else:
    print("⚠️  跳过模型调用测试（缺少 API Key）")

print("=" * 40)
print("环境验证完成")
print("=" * 40)
