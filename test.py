print("===== Testing Python environment =====")

# LangChain
try:
    import langchain
    import langchain_core
    print("✅ langchain")
    print("✅ langchain-core")
except Exception as e:
    print("❌ LangChain:", e)


# OpenAI
try:
    import openai
    import langchain_openai
    print("✅ openai")
    print("✅ langchain-openai")
except Exception as e:
    print("❌ OpenAI:", e)


# Anthropic
try:
    import langchain_anthropic
    print("✅ langchain-anthropic")
except Exception as e:
    print("❌ Anthropic:", e)


# Google Gemini
try:
    import langchain_google_genai
    print("✅ langchain-google-genai")
except Exception as e:
    print("❌ Google Gemini:", e)


# Hugging Face
try:
    import langchain_huggingface
    import transformers
    import huggingface_hub

    print("✅ langchain-huggingface")
    print("✅ transformers")
    print("✅ huggingface-hub")
except Exception as e:
    print("❌ Hugging Face:", e)


# PyTorch
try:
    import torch
    print("✅ torch")
    print("   PyTorch version:", torch.__version__)
    print("   CUDA available:", torch.cuda.is_available())
except Exception as e:
    print("❌ PyTorch:", e)


# Environment variables
try:
    from dotenv import load_dotenv
    print("✅ python-dotenv")
except Exception as e:
    print("❌ python-dotenv:", e)


# ML utilities
try:
    import numpy
    import sklearn

    print("✅ numpy")
    print("✅ scikit-learn")
except Exception as e:
    print("❌ ML utilities:", e)


print("\n===== Testing completed =====")