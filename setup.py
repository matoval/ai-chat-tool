from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.8'
DESCRIPTION = 'AI-Chat-Tool is a tool that brings ChatGPT to the command line'
LONG_DESCRIPTION = '# AI-Chat-Tool\nAI-Chat-Tool is a tool that brings ChatGPT to the command line.\n\nTo use this tool you will need a ChatGPT api key.\n\n### Options\n- **--api-key**\n    - (required) ChatGPT api key to use to access ChatGPT.\n- **--file**\n    - (optional) File to write ChatGPT response to.\n- **--max-tokens**\n    - (optional) The maximum number of tokens to generate in the completion.\n- **--temperature**\n    - (optional) What sampling temperature to use.\n\n### Example\n- Use AI-Chat-Tool to create a Python function that checks for even numbers\n\n**CLI**\n```\npython -m ai-chat-tool --api-key=$CHATGPTKEY --file=test.py --max-tokens=2000\n```\n```\nWhat can I do for you today?: Can you create a pyhton function that checks for even numbers?\nText written to test.py\n```\n \n \nFile created by AI-Chat-Tool \n**test.py**\n```python\ndef check_even(number):\n    if number % 2 == 0:\n        return True\n    else:\n        return False\n```'

# Setting up
setup(
    name="ai-chat-tool",
    version=VERSION,
    author="matoval (Matthew Sandoval)",
    author_email="<matovalcode@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['click', 'requests'],
    keywords=['chatgpt', 'ai', 'chat'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
