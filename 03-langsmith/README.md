# LangSmith

调用链追踪、数据集与评测。

## 环境变量

在本地 `.env` 中启用（模板见根目录 `.env.example`）：

```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=lsv2_xxxxxxxx
LANGCHAIN_PROJECT=study-lang-family
```

注意这里的 key 是 LangSmith 平台的 key，与 `DEEPSEEK_API_KEY` 不同。开启追踪后，所有调用会自动上报到对应 Project。
