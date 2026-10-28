# 常用 API 速查

## 初始化模型

```python
# 方式一：厂商专用类，参数提示最全
from langchain_deepseek import ChatDeepSeek
llm = ChatDeepSeek(model="deepseek-flash")

# 方式二：通用工厂，换厂商只改字符串
from langchain.chat_models import init_chat_model
llm = init_chat_model("deepseek:deepseek-flash")
```

`model="厂商:模型名"` 是 `model` + `model_provider` 的合并写法，只在 `init_chat_model` 里有效。两种写法不要混用，同时传 `model_provider` 时前缀不会被解析。

依赖已装好的 key 时无需再传 `api_key`。

## 调用

```python
llm.invoke("你好")                          # 一次性返回 AIMessage
for chunk in llm.stream("你好"):            # 流式
    print(chunk.text, end="", flush=True)
llm.batch(["问题1", "问题2"])               # 批量
```

## 消息

```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

messages = [
    SystemMessage("你是一名计算机老师"),
    HumanMessage("介绍一下字典树"),
    AIMessage("上一轮的回答"),
    HumanMessage("我刚才问了什么"),
]
llm.invoke(messages)

# 字典形式等价写法
[{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]
```

模型返回的 `AIMessage` 可以直接 `append` 回消息列表，比转成字典更安全（保留 tool_calls 等结构化信息）。

## 常用参数

| 参数 | 作用 |
| --- | --- |
| `temperature` | 随机性，0 最稳定 |
| `max_tokens` | 回复长度上限 |
| `timeout` | 请求超时（秒） |
| `max_retries` | 失败重试次数 |

## 返回值

```python
response.content            # 文本内容
response.text               # 纯文本，content 为列表时自动抽取
response.response_metadata  # token 用量、模型名等
response.tool_calls         # 工具调用请求
```

## 流式累加

```python
full = None
for chunk in llm.stream("..."):
    full = chunk if full is None else full + chunk
print(full.content)
```

`AIMessageChunk` 支持相加，累加结果是完整消息。初始值用 `None`，不要用空字符串。

## IDE 跳源码

| 场景 | PyCharm | VS Code |
| --- | --- | --- |
| 跳定义 | `Ctrl+B` 或 `Ctrl+单击` | `F12` |
| 预览源码 | `Ctrl+Shift+I` | `Alt+F12` |
| 看参数文档 | `Ctrl+Q` | `Ctrl+K Ctrl+I` |

Jupyter 里：`类名?` 看签名与文档，`类名??` 看源码，光标在括号内按 `Shift+Tab` 看参数。
