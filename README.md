# ConversationManager

A lightweight conversational interface that connects to the **Together AI** API (and optionally OpenAI) to simulate a chat system using the **Meta Llama 3.3** model.

---

## 🧩 Features

* Uses **Together API** to generate chat completions with `meta-llama/Llama-3.3-708-Instruct-Turbo-Free`;
* Implements a **token budget** system to control conversation memory;
* Tracks **total tokens used** per session;
* Supports **system prompts** for personality configuration;
* Provides a **command-line chat interface**.

---

## 🧰 Requirements

```bash
pip install openai together tiktoken
```

---

## 🔑 Environment Variables

You’ll need a valid API key for Together AI.

Set it in your environment:

**Mac/Linux:**

```bash
export TOGETHER_API_KEY="your_api_key_here"
```

**Windows (PowerShell):**

```bash
$env:TOGETHER_API_KEY="your_api_key_here"
```

---

## 🚀 How to Run

1. Save the file as `conversation_manager.py`
2. Run the script from your terminal:

   ```bash
   python conversation_manager.py
   ```
3. Start chatting!
   Type messages and get snarky responses from your AI assistant.
   To quit, type `exit` or `quit`.

---

## 🧠 How It Works

1. **Initialization:**
   Creates a `ConversationManager` instance with a system prompt and token settings.
2. **Message Handling:**
   Keeps track of user and assistant messages while enforcing a token limit.
3. **Token Counting:**
   Uses `tiktoken` to count tokens and manage message pruning.
4. **Chat:**
   Sends the conversation to Together AI’s `chat.completions.create()` endpoint and receives a generated reply.

---

## 💬 Example Session

```
You: How are you today?
Assistant: Oh, wonderful. Another question. Just what I needed.
Current tokens: 48
```

