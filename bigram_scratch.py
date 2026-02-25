import random
import string

def build_bigram_model(text):
    """
    Build a bigram character-level probability model.
    Returns a nested dict: {prev_char: {next_char: probability}}
    """
    # Step 1: Count all adjacent pairs
    counts = {}
    for i in range(len(text) - 1):
        prev, next_char = text[i], text[i + 1]
        if prev not in counts:
            counts[prev] = {}
        counts[prev][next_char] = counts[prev].get(next_char, 0) + 1

    # Step 2: Convert counts to probabilities
    model = {}
    for prev, next_counts in counts.items():
        total = sum(next_counts.values())
        model[prev] = {nc: cnt / total for nc, cnt in next_counts.items()}
    return model

def sample_next_char(model, prev_char):
    """
    Sample the next character given `prev_char` using weighted random choice.
    """
    if prev_char not in model or not model[prev_char]:
        # Fallback: return random printable ASCII char
        return random.choice(string.printable)
    
    choices = list(model[prev_char].keys())
    weights = list(model[prev_char].values())
    return random.choices(choices, weights=weights)[0]

def generate_text(model, start='h', length=50):
    """
    Generate `length` characters starting from `start`.
    """
    result = [start]
    current = start
    for _ in range(length - 1):
        next_char = sample_next_char(model, current)
        result.append(next_char)
        current = next_char
    return ''.join(result)

# Example usage (uncomment to run)
if __name__ == '__main__':
    # Tiny training text
    train_text = "hello world hello hello"
    
    # Build model
    m = build_bigram_model(train_text)
    
    # Print some probabilities
    print("P('e'|'h') =", m.get('h', {}).get('e', 0))
    print("P('l'|'l') =", m.get('l', {}).get('l', 0))
    
    # Generate
    print("\nGenerated:", generate_text(m, start='h', length=20))

# ✅ 验证示例：展示前 3 个最高概率预测
for ch in ['h', 't', 'a']:
    probs = m.get(ch, {})
    top3 = sorted(probs.items(), key=lambda x: x[1], reverse=True)[:3]
    print(f"P(*|'{ch}') top3: {top3}")
