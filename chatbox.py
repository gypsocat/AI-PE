import requests
import json

API_KEY = "SFt9ar49JYTDD05saTsQkjRN"
SECRET_KEY = "ACf6xrdFpcdEtu9JKdhZVIyOOB5l1OVo"

def make_prompt(prompt_file, data_file):
    with open(prompt_file, 'r', encoding='utf-8') as f:
        prompt = f.read()
    with open(data_file, 'r', encoding='utf-8') as f:
        data = f.read()
    return prompt + data

def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

def main():

    prompt_file = "./prompt_t.txt"
    data_file = "./user_input.txt"
    prompt = make_prompt(prompt_file, data_file)
    print(prompt)

    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-3.5-128k?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.8,
        "top_p": 0.8,
        "penalty_score": 1,
        "disable_search": False,
        "enable_citation": False,
        "response_format": "text"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    result_value = data.get('result')

    with open('./tmp_text/chatbox.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(result_value)

    print("done")

if __name__ == '__main__':
    main()