from ddgs import DDGS

def search_web(query):
    '''
    This tool allows to search web for relevant information
    '''
    ddgs = DDGS()
    result = ddgs.text(query, region="wt-wt", safesearch='off', timelimit='y', max_results=3)
    return result 