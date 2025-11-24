import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    #print("Hello from ai-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    #try:
    #    _, user_prompt = sys.argv
    #except ValueError:
    #    print("Error: Missing 1 argument. You need to provide a prompt")
    #    sys.exit(1)

    parser = argparse.ArgumentParser(
        description="This is an ai-agent script, made using Boot.dev, thank you Boot.dev, you rock"
    )

    parser.add_argument(
        "prompt",
        type=str,
        help="The prompt you should send to the llm"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Display User Prompt, Prompt Tokens and Response Tokens"
    )

    args = parser.parse_args()


    messages = [
        types.Content(role="user", parts=[types.Part(text=args.prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )


    #content = client.models.generate_content(model="gemini-2.0-flash-001", contents=user_prompt)
    print(response.text)
    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
