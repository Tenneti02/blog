import openai

openai.api_key = 'skey'  # Use environment variables instead

def generate_blog(paragraph_topic):
    response = openai.Completion.create(  # Corrected method
        model='gpt-3.5-turbo-instruct',
        prompt='Write a paragraph about the following topic: ' + paragraph_topic,
        max_tokens=400,
        temperature=0.3
    )

    retrieve_blog = response['choices'][0]['text'].strip()  # Fixed key access

    return retrieve_blog

print(generate_blog('Why NYC is better than your city.'))
