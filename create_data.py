import json

system_content = "あなたはしんぶんぶんという20歳の学生エンジニアです"

tweet_json = open("tweets.json", "r")
tweet_obj = json.load(tweet_json)

for tweet in tweet_obj:
    tweet_text = tweet["tweet"]["full_text"]
    if ("RT" in tweet_text) or ("http" in tweet_text) or ("@" in tweet_text):
        continue
    dataset_file = open("dataset.jsonl", "a")
    write_data = {
        "messages": [
            {"role": "system", "content": system_content},
            {"role": "assistant", "content": tweet_text},
        ]
    }
    dataset_file.write(json.dumps(write_data, ensure_ascii=False) + "\n")
