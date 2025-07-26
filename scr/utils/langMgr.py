from tokenize import generate_tokens, COMMENT, untokenize
from io import StringIO

def RemoveComments(context):
    tokens = generate_tokens(StringIO(context).readline)
    filtered_tokens = (
        token for token in tokens
        if token.type != COMMENT
    )
    return untokenize(filtered_tokens)