 You can test this plugin by inputting the link 'https://ukr-books-chatgpt-plugin.illia56.repl.co' into the field ![image](https://github.com/Illia-the-coder/Ukr-Books-ChatGPT-Plugin/assets/101904816/9d246a23-969a-44f8-9f2a-422928b6cbe4). Here are the instructions for setting up the plugin:
 
# Ukr-Books-ChatGPT-Plugin Quickstart
Get the Ukr-Books-ChatGPT-Plugin up and running in less than 5 minutes using Python. This plugin is meant to work with the [ChatGPT plugins documentation](https://platform.openai.com/docs/plugins). If you do not have plugin developer access yet, you can sign up to the waitlist by going to https://openai.com/waitlist/plugins.
 
## Setting up Locally
To install the required packages for this plugin, run the following command:
```bash
pip install -r requirements.txt
```
To run the plugin, enter the following command:
```bash
python main.py
```
Once the local server is running, follow these steps:
1. Go to https://chat.openai.com.
2. In the Model dropdown, select "Plugins" (if you don't see it there, you don't have access yet).
3. Choose "Plugin store"
4. Select "Develop your own plugin"
5. Enter `localhost:5003` as this is the URL the server is running on locally, then click "Find manifest file".
 
The plugin should now be installed and enabled! You can start with a question like "Tell me about this Ukrainian book" and then try asking more detailed questions about it!
 
## Setting up Remotely
Here are the instructions for setting up the plugin remotely:
 
### Cloudflare Workers
[Instructions for setting up with Cloudflare Workers]
 
### Code Sandbox
[Instructions for setting up with Code Sandbox]
 
### Replit
[Instructions for setting up with Replit]
 
## Getting Help
If you run into any issues or have questions about building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).
