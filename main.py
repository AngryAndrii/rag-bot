def load_chunks(path) -> list:
    with open(path, encoding="utf-8") as f:
        text = f.read()
        splitted_text = text.split('\n\n')
        res = [p.strip() for p in splitted_text if p.strip()]
        print(res)
        return res


if __name__ == "__main__":
    load_chunks("text.txt")