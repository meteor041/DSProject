from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from fastapi.middleware.cors import CORSMiddleware

# 创建 FastAPI 实例
app = FastAPI()

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 允许的前端地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义请求体模型
class Query(BaseModel):
    prompt: str
    max_tokens: int = 300

# DeepSeek API 的 URL 和 API 密钥
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
API_KEY = os.getenv("REACT_APP_DEEPSEEK_API_KEY")  # 从环境变量中读取 API 密钥

# 定义 API 路由
@app.post("/api/deepseek")
async def deepseek_api(query: Query):
    try:
        # 调用 DeepSeek 官方 API
        deepseek_response = requests.post(
            DEEPSEEK_API_URL,
            headers={"Authorization": f"Bearer sk-b3b97a6399e04c50953f5dd37753627c"},
            json={
                "messages": [{"role": "user", "content": query.prompt}],
                "model": "deepseek-chat",
                "max_tokens": query.max_tokens
            }
        )
        # 返回 DeepSeek 的响应
        return deepseek_response.json()
    except Exception as e:
        # 如果出错，返回 500 错误
        raise HTTPException(status_code=500, detail=str(e))

# 运行命令：uvicorn main:app --reload