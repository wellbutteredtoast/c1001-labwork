#Given a quote it generates the output as desired.

#The following quote is by John F. Kennedy, with some leading 
#and trailing spaces added.
quote = "   Man is still the most extraordinary computer of all.     "

# Print quote & length
print(quote)
print(f"Length of quote: {len(quote)}\n")

# Print quote without leading spaces & length
lstripped_quote = quote.lstrip()
print(f"{lstripped_quote}")
print(f"Length of quote: {len(lstripped_quote)}\n")

# Print quote with all whitespaces leading and trailing stripped
print(f"{quote.strip()}")
stripped_quote = quote.strip()
print(f"Length of quote: {len(stripped_quote)}\n")

# Append John F. Kennedy to end of quote.
appended_quote = quote.strip() + " - John F. Kennedy"
print(f"{appended_quote}\n")

#List of words from quote
word_list = quote.split()
print(f"{word_list}\n")