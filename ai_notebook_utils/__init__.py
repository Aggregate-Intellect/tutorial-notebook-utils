import requests

submission_token: str = None
ENDPOINT = "https://ai.science"


def score_answer(question_id: str, answer):
    """Sends student submission to retrieve bonus materials."""
    ensure_token()
    global submission_token
    if not submission_token:
        print("No valid token available. Skipping submission.")
    else:
        url = f'{ENDPOINT}/api/v1/notebook-submissions'
        myobj = {
            'answer': answer,
            'questionId': question_id
        }
        result = requests.post(
            url,
            data=myobj,
            headers={'Authorization', f'Bearer {submission_token}'}
        )
        print("Submission result: ", result)


def ensure_token():
    global submission_token
    if submission_token is None:
        print(
            "To submit your answer, " +
            f"log in to {ENDPOINT}/my-notebook-token and paste your personal token here: ")
        token_entered = input()
        if token_entered:
            token_validation_url = f'{ENDPOINT}/api/v1/notebook-tokens/{token_entered}'
            res = requests.get(token_validation_url)
            if res.status_code == 200:
                submission_token = token_entered
                return True
    print("You need to enter a valid token to contine.")
    return False
