# LLM Jailbreak Robustness Evaluation

This repository contains the code, datasets, and experiments for my research on evaluating the robustness of open-weight Large Language Models (LLMs) against jailbreak attacks.

The study benchmarks multiple instruction-tuned models using the JailbreakBench dataset and compares their responses to different jailbreak attack methods across various categories of harmful behaviors.

## Models

- Llama 3.1 8B Instruct
- Qwen 2.5 7B Instruct
- Gemma 3

## Attack Methods

- GCG
- JBC
- DSN

## Project Structure (essential)

```
prompts/
    dsn.json
    gcg.json
    jbc.json

main.py
requirements.txt
```

## Workflow

1. Generate a standardized prompt dataset from JailbreakBench artifacts.
2. Run the prompts on each model.
3. Store model responses.
4. Evaluate each response for jailbreak success.
5. Analyze results by attack method and harm category.

## Status

🚧 Work in progress.