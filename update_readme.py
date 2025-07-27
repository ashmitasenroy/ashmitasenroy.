import feedparser
import re

# IMPORTANT: This is your dev.to RSS feed URL.
RSS_URL = "https://dev.to/feed/ashmitasenroy" # Please chnage this line while working on yours

def fetch_blog_posts():
    feed = feedparser.parse(RSS_URL)
    posts = []
    # Get the 5 latest posts
    for entry in feed.entries[:5]:
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
    update_readme(latest_posts_markdown)
