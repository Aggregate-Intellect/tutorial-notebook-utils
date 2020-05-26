import requests


def submit_answer(product_id: str, question_id: str, answer: str):
    """Sends submission to unlock additional info."""
    url = 'https://ai.science/api/v1/assignment-submissions'
    myobj = {
      'productId':product_id,
      'questionId': question_id,
      'answer': answer
    }
    res = requests.post(url, json=myobj, headers={
      "Content-Type": "application/json"
    })
    if not res.ok:
        print("An error has occurred. Please contact admin@ai.science")
    else:
      data = res.json()
      if data["status"] == 'ok':
        print("Your bonus materials can be found here: ", data["bonus"])
      elif data["status"] == 'not-ok':
        print(data["reason"])
