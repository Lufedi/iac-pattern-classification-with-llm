import json

with open("../dataset/test.jsonl") as f:
    with open("saved_models/predictions.txt") as p:
        f_lines = f.readlines()
        p_lines = p.readlines()
        print(len(f_lines), len(p_lines))
        matches = 0
        assert len(f_lines) == len(p_lines)
        for i in range(len(f_lines)):
            json_line = json.loads(f_lines[i].strip())
            p_val = p_lines[i].strip()
            j_val = str(json_line['label'])
            if p_val == j_val: matches = matches + 1

        print("matches: ", matches)
        print("total: ", len(f_lines))
        print("accuracry :", (matches * 100)/ (len(f_lines)))
