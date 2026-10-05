from gemini_query import get_embed

def load_chunks(path) -> list:
    with open(path, encoding="utf-8") as f:
        text = f.read()
        splitted_text = text.split('\n\n')
        res = [p.strip() for p in splitted_text if p.strip()]
        return res

def get_one_chunk_embedded():
    first_chunk = load_chunks("text.txt")[0]
    result = get_embed(first_chunk)
    return result


if __name__ == "__main__":
    print(get_one_chunk_embedded())