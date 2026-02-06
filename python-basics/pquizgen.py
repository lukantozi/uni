import argparse
import json
import os
import random
from datetime import datetime

def load_questions(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def flatten_questions(db):
    """Extract all questions from nested gate/layer structure."""
    all_questions = []
    for gate_name, gate_data in db.items():
        if gate_name == "gate_0_setup":
            continue  # skip setup gate (no quiz questions)
        
        for layer_name, layer_data in gate_data.items():
            if "questions" in layer_data:
                for q_obj in layer_data["questions"]:
                    all_questions.append({
                        "gate": gate_name,
                        "layer": layer_name,
                        "q": q_obj["q"],
                        "a": q_obj["a"]
                    })
    return all_questions

def filter_by_gates(questions, gate_list):
    """Keep only questions from specified gates."""
    if not gate_list:
        return questions
    return [q for q in questions if any(gate in q["gate"] for gate in gate_list)]

def format_quiz(questions):
    """Format questions as Markdown."""
    lines = []
    lines.append("# Python Quiz\n")
    lines.append(f"**{len(questions)} questions** | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append("---\n")
    
    for i, q in enumerate(questions, 1):
        lines.append(f"## Q{i} `{q['gate']}` / `{q['layer']}`\n")
        lines.append("```python")
        lines.append(q["q"])
        lines.append("```\n")
    
    lines.append("---\n")
    lines.append("## Answers\n")
    
    for i, q in enumerate(questions, 1):
        lines.append(f"**Q{i}:** `{q['a']}`  ")
    
    return "\n".join(lines) + "\n"

def main():
    p = argparse.ArgumentParser(description="Generate Python quiz from question bank")
    p.add_argument("--questions", default="python_questions.json", help="Path to questions JSON")
    p.add_argument("--out", default="drills", help="Output directory")
    p.add_argument("--count", type=int, default=10, help="Number of questions (default: 10)")
    p.add_argument("--gates", nargs="+", help="Filter by gate keywords (e.g., 'strings' 'lists')")
    p.add_argument("--list", action="store_true", help="List available gates")
    p.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")
    p.add_argument("--name", default=None, help="Custom filename (default: date-based)")
    args = p.parse_args()

    db = load_questions(args.questions)

    if args.list:
        print("Available gates:")
        for gate_name in db.keys():
            if gate_name != "gate_0_setup":
                print(f"  - {gate_name}")
        return

    all_q = flatten_questions(db)
    
    if args.gates:
        all_q = filter_by_gates(all_q, args.gates)
        if not all_q:
            print(f"No questions found for gates: {args.gates}")
            return
    
    if len(all_q) < args.count:
        print(f"Warning: only {len(all_q)} questions available, using all of them")
        args.count = len(all_q)

    rng = random.Random(args.seed)
    selected = rng.sample(all_q, args.count)

    os.makedirs(args.out, exist_ok=True)

    stamp = datetime.now().strftime("%Y-%m-%d")
    if args.name:
        filename = args.name if args.name.endswith(".md") else args.name + ".md"
    else:
        filename = f"{stamp}__quiz_{args.count}q.md"

    path = os.path.join(args.out, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(format_quiz(selected))

    print(path)

if __name__ == "__main__":
    main()
