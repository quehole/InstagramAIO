# Instagram Automation Discord Bot

This Discord bot automates interactions with Instagram such as following users, liking posts, and commenting on posts. It uses the Instagram API and performs actions based on commands issued in a Discord server.

## Features

- **Follow Users**: Automatically follow specified users on Instagram.
- **Unfollow Users**: Automatically unfollow specified users on Instagram.
- **Like Posts**: Automatically like posts on Instagram.
- **Comment on Posts**: Automatically comment on posts on Instagram.
- **Role-Based Access**: Commands can be restricted based on user roles.
- **Channel-Based Commands**: Commands can be restricted to specific channels.

## Requirements

- Python 3.8 or higher
- `discord.py` library
- `requests` library
- `colorama` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/quehole/InstagramAIO.git
    cd InstagramAIO
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Create a `config.json` file in the root directory of the project with the following structure:

    ```json
    {
        "Config": {
            "token": "YOUR_DISCORD_BOT_TOKEN",
            "prefix": "!",
            "color": "#3498db",
            "bot_channel": CHANNEL_ID_1,
            "mod_channel": CHANNEL_ID_2,
            "default_role_id": ROLE_ID_1,
            "premium_role_id": ROLE_ID_2
        }
    }
    ```

    Replace `YOUR_DISCORD_BOT_TOKEN`, `CHANNEL_ID_1`, `CHANNEL_ID_2`, `ROLE_ID_1`, and `ROLE_ID_2` with your actual values.

4. Create a `cookies.txt` file in the root directory and add your Instagram session cookies (one per line).

5. Run the bot:

    ```sh
    python main.py
    ```

## Commands

- `!follow <username>`: Follow an Instagram user. Restricted to channels with the ID specified in `bot_channel` and users with the `default_role_id` role.
- `!unfollow <username>`: Unfollow an Instagram user. Restricted to channels with the ID specified in `bot_channel` and users with the `default_role_id` role.
- `!like <post_id>`: Like an Instagram post. Restricted to channels with the ID specified in `bot_channel` and users with the `default_role_id` role.
- `!comment <post_id> <message>`: Comment on an Instagram post. Restricted to channels with the ID specified in `bot_channel` and users with the `default_role_id` role.
- `!follow_all <usernames>`: Follow multiple Instagram users. Restricted to channels with the ID specified in `mod_channel` and users with the `premium_role_id` role.
- `!unfollow_all <usernames>`: Unfollow multiple Instagram users. Restricted to channels with the ID specified in `mod_channel` and users with the `premium_role_id` role.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This bot is for educational purposes only. Use it responsibly and in accordance with Instagram's terms of service. The authors are not responsible for any misuse of the bot or any potential consequences.

## Contact

For any issues or suggestions, please open an issue on the [GitHub repository](https://github.com/quehole/InstagramAIO/issues).
