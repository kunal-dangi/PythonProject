import requests as rq

parameters = {
    "amount": 10,
    "type": "boolean"
}


response = rq.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]



# question = data["results"][0]["question"]
# answer = data["results"][0]["correct_answer"]
# print(question, answer)
#
# dictionary = {
#     "question": question,
#     "answer": answer
# }
# print(dictionary)