import os, sys
from dotenv import load_dotenv
from google import genai



def main():
    #print("Hello from ai-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    try:
        _, arg = sys.argv
    except ValueError:
        print("Error: Missing 1 argument. You need to provide a prompt")
        sys.exit(1)

    content = client.models.generate_content(model="gemini-2.0-flash-001", contents=sys.argv[1])
    print(content.text)
    print(f"Prompt tokens: {content.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {content.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
