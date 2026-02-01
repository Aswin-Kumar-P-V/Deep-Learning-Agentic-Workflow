from utilty import call_llm, critique_response
import json
from tools import search_web
from tooldefiniton import tools_available

available_functions = {
    "search_web" : search_web
}

user_query = input("Enter your query:")
messages = [
        {"role" : "user", "content" : user_query}
    ]
response = call_llm(messages, tools_available)

tool_calls = response.choices[0].message.tool_calls

while True:
    while tool_calls:
        messages.append(response.choices[0].message)
        for tool_call in tool_calls:
            tool_call_id = tool_call.id
            tool_call_function_name = tool_call.function.name
            tool_call_arguments = json.loads(tool_call.function.arguments)

            print(f"Agent Decided to call function {tool_call_function_name} with prameter {tool_call_arguments}")

            function_response = available_functions[tool_call_function_name](**tool_call_arguments)

            messages.append({
                "role" : "tool",
                "tool_call_id" : tool_call_id,
                "content" : str(function_response)
            })
        response = call_llm(messages, tools_available)
        tool_calls = response.choices[0].message.tool_calls

    critique_response_returned = critique_response(user_query, response.choices[0].message.content)
    if "STATUS: APPROVED" in critique_response_returned:
        print(f"Critique Response : {critique_response_returned}")
        print(f"Final response: {response.choices[0].message.content}")
        break
    else:
        print(f"Critique Response : {critique_response_returned}")
        messages.append({
            "role" : "user",
            "content" : critique_response_returned
        })

        response =  call_llm(messages, tools_available)
        tool_calls =  response.choices[0].message.tool_calls