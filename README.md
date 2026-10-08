# NexaBot — Rule-Based AI Chatbot

NexaBot is a simple Python-based rule-driven chatbot. It responds to predefined
user inputs using conditional logic and a structured knowledge base.

## Features

- Greeting and conversation responses
- 5+ predefined intents
- Input sanitization for spaces and letter case
- Rule-based `if/elif` decision making
- Dictionary-based knowledge base
- Fallback response for unknown input
- Continuous conversation loop
- Clean exit commands: `bye`, `goodbye`, `exit`, `quit`

## Project Structure

```text
decodelabs_tasks/
├── README.md
└── task1_nexabot/
    ├── chatbot.py
    └── README.md
```

## Run

Make sure Python 3 is installed, then run:

```bash
python task1_nexabot/chatbot.py
```

## Example

```text
You: hello
NexaBot: Hello! 👋 I'm NexaBot. How can I help you?

You: what is your name
NexaBot: I'm NexaBot, a rule-based AI chatbot.

You: bye
NexaBot: Goodbye! Have a great day! 👋
```

## Project Context

This project was created as my implementation of an introductory rule-based
AI chatbot assignment. The implementation focuses on control flow, decision
making, input handling, and basic AI concepts.
