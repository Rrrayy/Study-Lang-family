# 环境搭建

## 1. 创建环境

```bash
conda create -n langchain1.2 python=3.12 -y
conda activate langchain1.2
pip install -r requirements.txt
```

## 2. 配置密钥

复制模板，填入自己的 key：

```bash
cp .env.example .env
```

`.env`：

```
DEEPSEEK_API_KEY=sk-xxxxxxxx
DEEPSEEK_BASE_URL=https://api.deepseek.com
```

在 notebook 里加载：

```python
from dotenv import load_dotenv
load_dotenv(override=True)
```

`override=True` 的作用：`.env` 的值强制覆盖系统里已有的同名环境变量。默认不覆盖，改了文件却不生效时就是这里的原因。改完 `.env` 记得重启内核，已创建的对象不会自动更新。

## 3. 验证

```python
from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(model="deepseek-flash")
print(llm.invoke("你好").content)
```

## 4. 查看账号可用模型

模型名以服务端返回为准，不要凭记忆写：

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)
print([m.id for m in client.models.list()])
```

---

# 踩坑记录

## 1. `.env` 变量名拼错

`DEEPSEEK_API__KEY`（双下划线）与 `DEEPSEEK_API_KEY` 是两个不同的变量，读错只会拿到 `None`。

```python
ValueError: If using default api base, DEEPSEEK_API_KEY must be set.
```

最省事的做法是干脆不手动读：`load_dotenv()` 之后直接 `ChatDeepSeek(model="deepseek-flash")`，key 由模型类自己从环境变量取。

## 2. `api_base` 与 `base_url` 不通用

| 类 | 正确参数 |
| --- | --- |
| `ChatDeepSeek` | `api_base` |
| `ChatOpenAI` | `base_url` |

给 `ChatDeepSeek` 传 `base_url` 不会报错，会被静默忽略；给 `ChatOpenAI` 传 `api_base` 则会被塞进请求参数，报：

```
TypeError: Completions.create() got an unexpected keyword argument 'api_base'
```

## 3. 两类报错其实是同一个病因

`api_base` 为默认值时，缺 key 报友好的 `ValueError`；`api_base` 被改成非默认值后，这段检查被跳过，问题延后到创建 OpenAI 客户端时才炸成 `OpenAIError`。所以"改了个参数，报错反而更奇怪"往往是同一个错误换了个位置冒出来。

## 4. `role` 拼写固定

```python
ValueError: Unexpected message type: 'assitant'.
```

合法值只有 `system`、`user`/`human`、`assistant`/`ai`、`tool`。用消息对象（`SystemMessage` 等）可以让 IDE 提前发现拼写问题。

## 5. 读懂 AttributeError

```
'list' object has no attribute 'invoke'
```

读法：点号左边那个对象是 list，它没有 invoke 方法。排查时往左看，`print(type(x))` 一句定位。常见原因是把消息列表当成了模型对象。

## 6. `print` 流式输出

```python
for chunk in model.stream("..."):
    print(chunk.text, end="", flush=True)
```

`end=""` 避免每片换行，`flush=True` 避免缓冲区攒批导致"最后一次性刷出"。`chunk.text` 是属性不是方法，会自动从结构化 content 里抽取纯文本。
