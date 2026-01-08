SYSTEM_PROMPT = """
You are an expert summarizer.
Given any text, provide a clear, concise,
and accurate summary in 2-3 sentences.
"""


def clean_tags(text: str, start: str, end: str) -> str:
    start_p = text.find(start)
    while start_p >= 0:
        end_p = text.find(end, start_p)
        if end_p >= 0:
            end_p += len(end)
            text = text[:start_p] + text[end_p:]
        start_p = text.find(start)
    return text


def run(inputs: dict) -> dict:
    text = inputs.get("text", "")
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": text},
    ]
    summary = ""
    try:

        from ollama import chat

        response = chat(model="qwen3:1.7b", messages=messages)
        summary = response.message.content
        summary = clean_tags(summary, start="<think>", end="</think>")

    except Exception as e:
        print(e)

    return {"summary": summary}


if __name__ == "__main__":
    NORTHERN_LIGHTS = """
    There are times when the night sky glows with bands of color. The bands may
    begin as cloud shapes and then spread into a great arc across the entire sky. They
    may fall in folds like a curtain drawn across the heavens. The lights usually grow
    brighter, then suddenly dim. During this time the sky glows with pale yellow, pink,
    green, violet, blue, and red. These lights are called the Aurora Borealis. Some
    people call them the Northern Lights. Scientists have been watching them for
    hundreds of years. They are not quite sure what causes them. In ancient times
    people were afraid of the Lights. They imagined that they saw fiery dragons in the
    sky. Some even concluded that the heavens were on fire
    """

    inp = {"text": NORTHERN_LIGHTS}
    out = run(inp)
    print(out)
