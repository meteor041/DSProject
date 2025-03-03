import { useState } from 'react';
import axios from 'axios';

function APIClient() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const callAPI = async () => {
    try {
      setLoading(true);
      // 发送 POST 请求到后端
      const res = await axios.post('http://localhost:8000/api/deepseek', {
        prompt: input,
        max_tokens: 300
      });
      // 假设后端返回的数据结构是 { choices: [{ text: "..." }] }

      if (res.data.choices && res.data.choices.length > 0) {
      setResponse(res.data.choices[0].message.content);
    } else {
      setResponse(JSON.stringify(res, null, 2));
    }
    } catch (error) {
      console.error('API调用失败:', error);
      setResponse('API调用失败，请检查控制台日志。');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>DeepSeek API 调用示例</h1>
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="请输入您的提示"
        rows={5}
        cols={50}
      />
      <br />
      <button onClick={callAPI} disabled={loading}>
        {loading ? '生成中...' : '提交'}
      </button>
      <div className="response-area">
        <h2>响应结果：</h2>
        <pre>{response}</pre>
      </div>
    </div>
  );
}

export default APIClient;