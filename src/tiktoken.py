import tiktoken

def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    # encoding = tiktoken.get_encoding("o200k_base")
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

print(num_tokens_from_string("Hello, world!", "gpt-4.1-mini"))