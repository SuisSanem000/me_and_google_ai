https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them

Tokens are sub-word chunks — roughly 4 characters or ¾ of a word each. Common rules of thumb: 100 tokens ≈ 75 words, 1,500 words ≈ 2,048 tokens. Non-English text tends to use more tokens per character (e.g. Spanish uses ~2× the tokens per char vs English), making API usage pricier for those languages.

Token context matters: the same word gets a different token ID depending on capitalization and position in a sentence (e.g. "red", "Red" mid-sentence, and "Red" at sentence start are three distinct tokens).

Two practical tips:
- Don't end prompts with a trailing space — it degrades output quality because the tokenizer already bakes trailing spaces into tokens.
- Use `logit_bias` to boost or suppress specific tokens in completions (values from -100 to +100, where -100 effectively bans a token).

The article also mentions legacy limits (2,048 tokens shared between prompt + completion) and links to an interactive tokenizer tool — both fairly outdated given current models.