# LLM Projects:

## 1. ConversationManager

A lightweight conversational interface that connects to the **Together AI** API (and optionally OpenAI) to simulate a chat system using the **Meta Llama 3.3** model.

* Uses **Together API** to generate chat completions with `meta-llama/Llama-3.3-708-Instruct-Turbo-Free`;
* Implements a **token budget** system to control conversation memory;
* Tracks **total tokens used** per session;
* Supports **system prompts** for personality configuration;
* Provides a **command-line chat interface**.

## 2. AI Translator English-Hindi

This project implements an **AI-powered neural machine translation (NMT)** system that translates text from **English → Hindi** using the **Helsinki-NLP/opus-mt-en-hi** model (Transformer-based) from Hugging Face. The system is fine-tuned and evaluated using the **IIT Bombay English–Hindi Parallel Corpus**.
