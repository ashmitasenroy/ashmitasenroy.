import feedparser
import re

RSS_URL = "https://dev.to/feed/ashmitasenroy"

def fetch_blog_posts():
    print(f"Fetching posts from: {RSS_URL}") 
    feed = feedparser.parse(RSS_URL)
    print(f"Found {len(feed.entries)} posts in the feed.") 
    posts = []
    # Get the 5 latest posts
    for entry in feed.entries[:5]:
        print(f"  - Adding post: {entry.title}") # <-- DEBUG LINE
        posts.append(f"* [{entry.title}]({entry.link})")
    return "\n".join(posts)

def update_readme(new_content):
    try:
        with open("README.md", "r") as f:
            readme_content = f.read()

        # Use regex to find and replace the content between the markers
        # The 's' flag allows '.' to match newline characters
        updated_content = re.sub(
            r"(?s)(<!--BLOG-POST-LIST:START-->)(.*)(<!--BLOG-POST-LIST:END-->)",
            f"\\1\n{new_content}\n\\3",
            readme_content
        )

        with open("README.md", "w") as f:
            f.write(updated_content)
        print("README.md updated successfully.")

    except FileNotFoundError:
        print("Error: README.md not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    latest_posts_markdown = fetch_blog_posts()
    print("--- Generated Markdown ---") # <-- DEBUG LINE
    print(latest_posts_markdown) # <-- DEBUG LINE
    print("--------------------------") # <-- DEBUG LINE
    update_readme(latest_posts_markdown)
