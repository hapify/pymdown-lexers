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
            (r'<<(\?\?|\?|@|if|elseif|for)', token.Operator, 'condition'),  # Condition opening
            (r'<<(\@|\?\?|\?|endif|else|endfor)>>', token.Operator),  # Condition closing
            (r'<<([a-zA-Z_.]+)\s+([a-zA-Z_-]+)>>', token.String),  # Name interpolation
            (r' |\t', token.Whitespace),
            (r'.', token.Text)
        ],
        'condition': [
            (r'(\d)+', token.Number),  # Operator number
            (r'(\/|\*|\+|\-|\bor\b|\band\b|\bnot\b|\borNot\b|\bandNot\b)', token.Keyword),  # Condition keywords
            (r'(\(|\)|\.)', token.Punctuation),  # Common syntax
            (r'>>', token.Operator),  # Operator closing
            (r' |\t', token.Whitespace),
            (r'.', token.Name)
        ]
    }
