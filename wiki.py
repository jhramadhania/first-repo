import wikipedia # pyright: ignore[reportMissingImports]

phrase = "Python (programming language)"
print(wikipedia.summary(phrase))

print(wikipedia.search('Barack'))
print(wikipedia.suggest("Barak Obama"))