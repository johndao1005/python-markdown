# Replacements tell us were to insert tags with the font and colors given
def search_re(pattern, text, offset):
    matches = []
    text = text.splitlines()
    for i, line in enumerate(text):
        for match in re.finditer(pattern, line):
             matches.append(
                (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end() - offset}")
            )
    return matches