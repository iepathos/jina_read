#!/usr/bin/env python3
import requests
import os
import sys
import re
from urllib.parse import urlparse
from dotenv import load_dotenv

def sanitize_filename(url):
    # Remove any protocol prefix (http://, https://, etc.)
    url = re.sub(r'^https?://', '', url)
    # Replace all slashes and other unsafe characters with underscores
    sanitized = re.sub(r'[\\/*?:"<>|]', '_', url)
    # Remove any leading/trailing spaces or dots
    sanitized = sanitized.strip('. ')
    return sanitized

def fetch_and_save_markdown(links):
    # Load environment variables from .env file if it exists
    load_dotenv()
    
    # Get token from environment variable
    token = os.getenv('JINA_TOKEN')
    if not token:
        print("Warning: JINA_TOKEN not found in environment or .env file", file=sys.stderr)
        return

    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    output_dir = "markdown_outputs"
    os.makedirs(output_dir, exist_ok=True)
    
    base_url = "https://r.jina.ai/"
    
    for link in links:
        link = link.strip()
        if not link:  # Skip empty lines
            continue
            
        # Create safe filename from the link
        safe_filename = sanitize_filename(link)
        filename = f"{safe_filename}.md"
        filepath = os.path.join(output_dir, filename)
        
        # Skip if file already exists
        if os.path.exists(filepath):
            print(f"Skipping {link} - file already exists: {filename}")
            continue
            
        try:
            # Updated to include headers
            response = requests.get(f"{base_url}{link}", headers=headers)
            response.raise_for_status()
            
            # Save the markdown content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(response.text)
                
            print(f"Successfully saved markdown for {link} as {filename}")
            
        except requests.RequestException as e:
            print(f"Error fetching {link}: {str(e)}", file=sys.stderr)
        except IOError as e:
            print(f"Error saving file for {link}: {str(e)}", file=sys.stderr)

if __name__ == "__main__":
    links = sys.stdin.readlines()
    fetch_and_save_markdown(links) 