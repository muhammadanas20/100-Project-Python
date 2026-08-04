import sys        # System-specific parameters and functions (used to exit the script early on errors)
import requests   # HTTP library used to send requests and download web page data
from bs4 import BeautifulSoup  # HTML parsing library used to extract specific data tags

# 1. Get user input and clean up whitespace at the edges
user_input = input("Wikipedia article title: ").strip()

# 2. Format the title into a proper Wikipedia page slug
# Split the input string into individual words by any whitespace, capitalize each word, 
# and join them back together with underscores. This perfectly handles single or multiple spaces.
slug = "_".join(word.capitalize() for word in user_input.split())

# 3. Construct the destination web address using a Python f-string
url = f"https://wikipedia.org/wiki/{slug}"

# 4. Set a custom User-Agent identity string so Wikipedia knows who is making the request
headers = {"User-Agent": "ClassroomPythonProject/1.0 (contact: student@example.com)"}

# 5. Begin a try-except structure to gracefully trap internet or server errors without crashing
try:
    # Send a GET request to the constructed URL with our headers and a 10-second timeout limit
    response = requests.get(url, headers=headers, timeout=10)
    
    # Check the server response; raises an HTTPError exception automatically if the status is not 200 OK
    response.raise_for_status()

except requests.exceptions.HTTPError as e:
    # If an HTTP error happens, isolate 404 (Not Found) errors to give a clean message to the user
    if response.status_code == 404:
        print(f"\n❌ Error: The article '{user_input}' does not exist on Wikipedia.")
    else:
        print(f"\n❌ HTTP Error occurred: {e}")
    sys.exit(1)

except requests.exceptions.RequestException as e:
    # Capture any other network issues like DNS failures, loss of internet, or connection dropouts
    print(f"\n❌ Connection error: {e}")
    sys.exit(1)

# 6. Parse the raw HTML text string downloaded from the response using the standard 'html.parser' engine
soup = BeautifulSoup(response.text, "html.parser")

# 7. Find the primary heading tag (<h1>) on the page, extract its clean text, and print it as a title
print("\n📝 " + soup.find("h1").get_text(strip=True))

# 8. Use CSS selectors to target <p> tags nested directly inside the '.mw-parser-output' main body block.
paragraphs = [p.get_text() for p in soup.select(".mw-parser-output > p")]

# 9. Filter out any empty paragraph blocks (e.g., hidden formatting spaces or layout linebreaks)
valid_paragraphs = [p.strip() for p in paragraphs if p.strip()]

# 10. Check if we successfully gathered any text blocks from our structural matching loop
if valid_paragraphs:
    # Slice the list to extract just the first 3 string matches and loop through them
    for paragraph in valid_paragraphs[:3]:
        # Print each text paragraph on a fresh line separated by a blank spacing block
        print("\n" + paragraph)
else:
    # Error message if the page loaded successfully but has a unique structure missing standard paragraph containers
    print("\n⚠️ No structural paragraph content found in the main body of this article.")
