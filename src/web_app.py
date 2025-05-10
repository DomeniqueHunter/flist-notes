from flask import Flask, render_template
import flist
import config

app:Flask = Flask(__name__)
flist.login.login(config.USER, config.PASSWORD)

conversations = flist.notes.Conversations(conversation_root_path=config.CONVERSATIONS_PATH)
nav_items = conversations.keys()

@app.route('/<page>')
def page(page: str) -> str:
    # Define content for each page dynamically
    
    bottom_contents: dict[str, str] = {
        "home": "<p>Here is some additional content for the Home page's bottom section.</p>"
    }

    # If the page exists in the dictionary, pass its content to the template
    content: str = conversations.get_conv(page).html()
    conversations.save()
    
    return render_template('index.html', nav_items=nav_items, content=content, bottom_content=bottom_contents.get(page, ""))


@app.route('/')
def index() -> str:
    return render_template('index.html', nav_items=nav_items, content="main page")


def main() -> None:
    app.run(debug=True)


if __name__ == '__main__':
    main()
