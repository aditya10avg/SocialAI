import openai

# Function to get API key securely
def get_openai_api_key():
    # Ideally, the API key should be stored in an environment variable or config file for security
    return "your-openai-api-key"

# Function to generate the post
def generate_post(content, platform):
    prompt = ""

    if platform == "tweet":
        prompt = f"Convert the following text into a viral, concise, engaging tweet:\n\n{content}"
    elif platform == "linkedin":
        prompt = f"Convert the following text into a professional LinkedIn post that is engaging and suitable for a business audience:\n\n{content}"
    elif platform == "medium":
        prompt = f"Convert the following text into a detailed, informative, and engaging Medium post:\n\n{content}"
    else:
        return "Invalid platform choice. Please choose either 'tweet', 'linkedin', or 'medium'."

    try:
        # Request to OpenAI GPT-3 API to generate the post
        openai.api_key = get_openai_api_key()
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use the most appropriate model for your use case
            prompt=prompt,
            max_tokens=300  # Adjust this based on how long you want the output to be
        )

        return response.choices[0].text.strip()
    
    except Exception as e:
        return f"Error: {str(e)}"

# Main code to interact with the user
def main():
    # Get the input from the user
    content = input("Enter your random and unorganized write-up: ")

    # Ask the user which platform post they want
    platform = input("What type of post would you like to create? (tweet, linkedin, medium): ").lower()

    # Generate and display the post
    result = generate_post(content, platform)
    print("\nGenerated Post:\n")
    print(result)

if __name__ == "__main__":
    main()

#The next step is to integrate it to ui and add some functionalities like updating the current write up into linkedin one or tweet or medium blog. 