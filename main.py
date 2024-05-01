'''
This python project creates a Discord chat bot by leveraging both OpenAI and Discord API endpoints.
'''

# ---- LIBRARIES ----
# Import necessary libaries
from openai import OpenAI
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

# ---- CLASSES ----
# Create a class named, "BingBot" to be used to create an instance of a discord bot
class BingBot(discord.Client):
    # Override the on_ready function
    async def on_ready(self):
        print("We have logged in as {0.user}".format(self))

    # Override the on_message function
    async def on_message(self, message):
        # If statement to ignore messages from the bot itself
        if message.author == self.user:
            return
        else:
            # Generate a response using the message content as the prompt
            response = generate_response(message.content)

            # Send the response to the same channel that the message was received in.
            await message.channel.send(response)


# ---- FUNCTIONS ----
# Create a function to make API requests to OpenAI. Read more here: https://platform.openai.com/docs/api-reference/chat
def generate_response(prompt):

    client = OpenAI() # Create a custom OpenAI class named, "client"

    # Create a variable to store completions.
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful Chat bot."},
            {"role": "user", "content": prompt}
            ]
    )

    message = completion.choices[0].message
    return message.content

# Create the main function. This is where you run functions from.
def main():

    # Prints the text in quotation marks to show that this code is running.
    print("Running...")

    # Load environment variable
    load_dotenv()

    # Initialize openai client object, in the next line we assign the API key to this object.
    client = OpenAI()

    # Initialize the API keys from environment
    client.api_key = os.getenv("OPENAI_API_KEY")
    discord_api_key = os.getenv("DISCORD_API_KEY")

    # Run the webserver.
    keep_alive()

    # Create an instance of the bot with all intents enabled
    botclient = BingBot(intents=discord.Intents.all()) # This is creating an instance of the class (object) we defined earlier, named "botclient".

    # Run the bot with the token
    botclient.run(discord_api_key)

# Run the main function if "main.py" is executed directly.
if __name__ == "__main__":
    main()