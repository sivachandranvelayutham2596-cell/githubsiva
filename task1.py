from openai import openai

client =openai(api_key ='need to paste key link')
response =client.response.create(model='gpt4o mini',
input ="tell me about madurai")
print(response.output_text)
