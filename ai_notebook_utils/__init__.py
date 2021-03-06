import requests
import base64
import json
import numpy as np

submission_token: str = None
TOKEN_API_ENDPOINT = "https://ai.science"
SUBMISSION_API_ENDPOINT = "https://api.ai.science/v1/notebook-submissions"


def score_answer(question_id: str, answer):
    """Sends student submission to retrieve bonus materials."""
    if ensure_token():
        global submission_token
        if not submission_token:
            print("No valid token available. Skipping submission.")
        else:
            answer64 = base64.b64encode(
                answer.astype(np.float32)).decode("ascii")
            url = f'{SUBMISSION_API_ENDPOINT}'
            payload = {
                'answer64': answer64,
                'questionId': question_id,
                'token': submission_token
            }
            result = requests.post(
                url,
                data=json.dumps(payload),
            )
            try:
                print("Submission result: ", result.json()['body'])
            except:
                print("Something went wrong. Please contact admin@ai.science.")
            return None


def ensure_token():
    global submission_token
    if submission_token is None:
        print(
            "To submit your answer, " +
            f"log in to {TOKEN_API_ENDPOINT}/my-notebook-token and paste your personal token here: ")
        token_entered = input()
        if token_entered:
            token_validation_url = f'{TOKEN_API_ENDPOINT}/api/v1/notebook-tokens/{token_entered}'
            res = requests.get(token_validation_url)
            if res.status_code == 200:
                submission_token = token_entered
                return True
        print("You need to enter a valid token to contine.")
        return False
    return True
