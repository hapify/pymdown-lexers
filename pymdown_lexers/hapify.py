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
            (r'<<<([^>]+)>>>', token.Comment),  # Evaluate
            (r'<<#([^>]+)>>', token.Comment),  # Comments
            (r'<<=([^>]+)>>', token.String),  # Interpolation
            (r'<<([a-zA-Z_.]+)\s+([a-zA-Z_-]+)>>', token.String), # Name interpolation
            (r'<<(\?\?|\?|@|if|elseif|for)(\d+)?\s', token.Operator),  # Condition opening
            (r'<<(\@|\?\?|\?|endif|else|endfor)>>', token.Operator),  # Condition closing
            (r'>>', token.Operator),  # Operator closing
            (r'(\/|\*|\+|\-|\bor\b|\band\b|\bnot\b|\borNot\b|\bandNot\b)', token.Keyword),  # Condition keywords
            (r' |\t', token.Whitespace),
            (r'.', token.Text)
        ]
    }
