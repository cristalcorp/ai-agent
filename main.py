import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    #print("Hello from ai-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    try:
        _, user_prompt = sys.argv
    except ValueError:
        print("Error: Missing 1 argument. You need to provide a prompt")
        sys.exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )


    #content = client.models.generate_content(model="gemini-2.0-flash-001", contents=user_prompt)
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
