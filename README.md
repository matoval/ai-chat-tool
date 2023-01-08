# AI-Chat-Tool 
AI-Chat-Tool is a tool that brings ChatGPT to the command line.

To use this tool you will need a ChatGPT api key.

### Options
- **--api-key**
    - (required) ChatGPT api key to use to access ChatGPT.
- **--file**
    - (optional) File to write ChatGPT response to.
- **--max-tokens**
    - (optional) The maximum number of tokens to generate in the completion.
- **--temperature**
    - (optional) What sampling temperature to use.
    
### Example
- Use AI-Chat-Tool to create a Python function that checks for even numbers

**CLI**
```
python -m ai-chat-tool --api-key=$CHATGPTKEY --file=test.py --max-tokens=2000
```
```
What can I do for you today?: Can you create a pyhton function that checks for even numbers?
Text written to test.py
```
\
\
File created by AI-Chat-Tool\
**test.py**
```python
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
```
