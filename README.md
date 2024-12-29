# AI-chat-interface-for-DataSpell
A project task for JetBrains internship that involves creating a chat interface for data transformations.

# Instructions:
1. Go into LLM -> api_key.txt
   Here you should paste your OpenAI API key. It will not work if you don't put in your own key.
2. Put the dataset you want to use into the "data" folder (You can also use one of the two existing datasets)
3. run "main.py".
   Here you will be prompted to give your file name (include extension).
   Once you input your dataset, you can give it commands to execute. Currently only 3 transformations are supported (filter, select column, sort).

# Experimental
If you want to have a bit more fun, try the experimental feature. Here the llm will dynamically create the transformation code that it will perform, thus allowing you to have virtually unlimited ways to perfrom transformations. However,this is risky as the generated code can be problematic. 
If you want to test this out, repeat instructions from 1 to 3 but instead of "main.py" run "main_experimental.py"

Have fun :)
