tools_available = [
    {
        "type": "function",
        "function": {
            "name": "search_web",       
            "description": "Allows to search web for relevant information", 
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {    
                        "type": "string",
                        "description": "The topic or question to search for on the web"
                    }
                },
                "required": ["query"] 
            }
        }
    }
]
