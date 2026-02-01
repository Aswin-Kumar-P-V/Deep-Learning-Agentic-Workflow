from clients import openai_client


def call_llm(messages, tools = None):
    return openai_client.chat.completions.create(
        model = "gpt-5",
        messages= messages,
        tools= tools
    )

def critique_response(user_query, draft_answer):
    prompt = f"""
    Act as a helpful peer reviewer. Your goal is to ensure the answer is accurate and helpful, but do not be overly pedantic.

    User Query: {user_query}
    Draft Answer: {draft_answer}

    ### Evaluation Criteria
    1. RELEVANCE: Does the answer address the main part of the user's question?
    2. ACCURACY: Does the information seem reasonable based on the context?
    
    ### Decision Rules
    - If the answer is helpful and covers the main points -> STATUS: APPROVED
    - If the answer is completely wrong, irrelevant, or missing the core answer -> STATUS: REJECTED

    ### Your Output Format
    STATUS: [APPROVED | REJECTED]
    FEEDBACK: [Brief feedback. If REJECTED, state exactly what one thing to search for next.]
    """
    
    messages = [
        {"role" : "system", "content" : prompt}
    ]

    return call_llm(messages).choices[0].message.content