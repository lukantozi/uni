import argparse, json, os, random
from datetime import datetime

DEFAULT_ORDER = [
    "bubble_sort",
    "insertion_sort",
    "merge_sort",
    "quick_sort_3way",
    "stack",
    "binary_search",
]

def load_topics(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def pick_variant(rng, variants):
    return rng.choice(variants)

def section(topic_name, basic, variant, tests):
    lines = []
    lines.append(f"#{topic_name}")
    lines.append(f"#- BASIC: {basic}")
    lines.append(f"#- +1: {variant}")
    if tests:
        lines.append("TESTS = " + json.dumps(tests, ensure_ascii=False))
    lines.append("")  # blank line between topics
    return "\n".join(lines)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--topics", default="topics.json")
    p.add_argument("--out", default="drills")
    p.add_argument("--seed", type=int, default=None)  # reproducible picks across PC/laptop
    p.add_argument("--name", default=None)            # optional filename override
    p.add_argument("--shuffle", action="store_true")  # optional: randomize topic order
    args = p.parse_args()

    db = load_topics(args.topics)

    order = [t for t in DEFAULT_ORDER if t in db]
    # include any extra topics that exist in json but not in default list
    for t in db.keys():
        if t not in order:
            order.append(t)

    rng = random.Random(args.seed)

    if args.shuffle:
        rng.shuffle(order)

    os.makedirs(args.out, exist_ok=True)

    stamp = datetime.now().strftime("%Y-%m-%d")
    if args.name:
        filename = args.name if args.name.endswith(".py") else args.name + ".py"
    else:
        filename = f"{stamp}__daily_drill.py"

    path = os.path.join(args.out, filename)

    lines = []
    lines.append("# Daily drill: implement BASIC + 1 variant per topic (no sorted()).")
    lines.append("")

    for topic in order:
        info = db[topic]
        basic = info["basic"]
        variant = pick_variant(rng, info["variants"])
        tests = info.get("tests", {})
        lines.append(section(topic, basic, variant, tests))

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(path)

if __name__ == "__main__":
    main()
