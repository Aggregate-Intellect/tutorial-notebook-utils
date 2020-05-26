import requests


def submit_notebooks(product_id: str, answer: str):
    """Sends student submission to retrieve bonus materials."""
    url = 'https://ai.science/api/v1/notebook-submissions'
    myobj = {
        'answer': answer
    }
    bonus = requests.post(url, data=myobj)
    print("Your bonus materials can be found here: ", bonus)
