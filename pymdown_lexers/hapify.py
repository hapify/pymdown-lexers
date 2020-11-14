"""Pygments lexer for Hapify Syntax."""
from pygments.lexer import RegexLexer
from pygments import token

__all__ = ("HapifyLexer",)


class HapifyLexer(RegexLexer):
    """Simple lexer for Hapify Syntax."""

    name = 'Hapify'
    aliases = ['hapify', 'hpf']
    filenames = ['*.hpf']
    mimetypes = ['text/hapify']

    tokens = {
        'root': [
            (r'<<(\?|if|else|elseif|endif)([^>]*?)>>', token.Keyword),  # Condition
            (r'<<(\@|for|endfor)([^>]*?)>>', token.Keyword),  # Iteration
            (r'<<<(.*)>>>', token.Escape),  # Evaluate
            (r'<<#(.*)>>', token.Comment),  # Comments
            (r'<<=(.*)>>', token.String),  # Interpolation
            (r'<<([a-zA-Z_.]+)\s+([a-zA-Z_]+)>>', token.String),  # Name interpolation
            (r' |\t', token.Whitespace),
            (r'.', token.Text)
        ]
    }
