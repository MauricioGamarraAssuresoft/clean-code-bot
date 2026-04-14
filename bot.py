import os
import click
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def refactor_code(dirty_code):
    """
    Implements Chain of Thought (CoT) to analyze and refactor code.
    """
    prompt_cot = f"""
    Analyze the following code step by step:
    1. ANALYZE: Identify which SOLID principles are being violated.
    2. PLAN: Design a better structure and logical flow.
    3. REFACTOR: Rewrite the optimized code with professional documentation (Docstrings/JSDoc).

    Original Code:
    {dirty_code}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert Senior Developer specialized in Clean Code and SOLID principles."},
            {"role": "user", "content": prompt_cot}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

@click.command()
@click.argument('file_path')
def main(file_path):
    """CLI Tool to clean and refactor code automatically."""
    if not os.path.exists(file_path):
        click.echo(f"Error: File '{file_path}' not found.")
        return

    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        click.echo("Processing... the AI is thinking.")
        result = refactor_code(content)
        
        # Save the result to a new file
        output_file = f"clean_{os.path.basename(file_path)}"
        with open(output_file, "w") as f:
            f.write(result)
        
        click.echo(f"Done! Check the refactored file: {output_file}")
    
    except Exception as e:
        click.echo(f"An error occurred: {e}")

if __name__ == "__main__":
    main()