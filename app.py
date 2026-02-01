import streamlit as st
import json
from utilty import call_llm, critique_response
from tools import search_web
from tooldefiniton import tools_available

available_functions = {
    "search_web": search_web
}

st.set_page_config(page_title="Deep Research Agent", page_icon="🕵️‍♂️")

st.title("🕵️‍♂️ Deep Research Agent")
st.markdown("Ask a complex question and watch the agent plan, search, and critique itself.")

query = st.text_input("Enter your research query:", placeholder="e.g. What is the latest news on Palki Sharma?")

if st.button("Start Research") and query:
    
    messages = [{"role": "user", "content": query}]
    
    result_container = st.empty()
    
    with st.status("🤖 Agent is working...", expanded=True) as status:
        
        st.write("🧠 Planning initial steps...")
        response = call_llm(messages, tools_available)
        tool_calls = response.choices[0].message.tool_calls

        while True:
            
            while tool_calls:
                messages.append(response.choices[0].message)
                
                for tool_call in tool_calls:
                    func_name = tool_call.function.name
                    args = json.loads(tool_call.function.arguments)
                    
                    st.write(f"🔍 **Searching:** {args.get('query', 'Checking web...')}")
                    
                    function_response = available_functions[func_name](**args)
                    
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(function_response)
                    })
                
                response = call_llm(messages, tools_available)
                tool_calls = response.choices[0].message.tool_calls

            draft_answer = response.choices[0].message.content
            st.write("👨‍🏫 **Critic:** Reviewing the draft answer...")
            
            critique = critique_response(query, draft_answer)
            
            if "STATUS: APPROVED" in critique:
                st.write("✅ **Critic:** Approved!")
                status.update(label="Research Complete!", state="complete", expanded=False)
                break
            else:
                st.write("❌ **Critic:** Rejected. Asking for revisions...")
                messages.append({
                    "role": "user", 
                    "content": f"Please fix the following issues:\n{critique}"
                })
                
                response = call_llm(messages, tools_available)
                tool_calls = response.choices[0].message.tool_calls

    st.subheader("Final Report")
    st.markdown(response.choices[0].message.content)