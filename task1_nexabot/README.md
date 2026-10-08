# NexaBot — Rule-Based AI Chatbot

## Overview

NexaBot is a lightweight rule-based chatbot developed in Python. It does not
use machine learning, an external API, or an LLM. Instead, it uses explicit
programming rules to decide how to respond to user input.

## How It Works

```text
User Input
    ↓
Input Sanitization
    ↓
Exit Check
    ↓
Knowledge Base / Rules
    ↓
Matching Response
    ↓
Fallback if No Match
    ↓
Continue Conversation
```

## Main Components

### 1. Input Sanitization
The chatbot converts input to lowercase, removes leading/trailing whitespace,
and normalizes repeated spaces. This makes matching more reliable.

### 2. Knowledge Base
A Python dictionary stores predefined intents and their responses.

### 3. Decision Logic
`if` conditions check exit commands and useful variations. Exact known inputs
are looked up in the knowledge base.

### 4. Continuous Loop
The chatbot keeps accepting messages until the user enters an exit command.

### 5. Fallback
If no rule matches, NexaBot gives a helpful default response instead of
crashing.

## Supported Examples

- `hello`
- `hi`
- `hey`
- `how are you`
- `what is your name`
- `who are you`
- `help`
- `thanks`
- `thank you`
- `bye`
- `goodbye`
- `exit`
- `quit`

## Requirements

- Python 3.x
- No external packages required

## Run

```bash
python chatbot.py
```

## Author

**Zahid Ali**
