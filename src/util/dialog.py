LINE_COL_LIMIT = 45


def break_dialog_lines(dialog):
    lines = []
    for line in dialog.split('\n'):
        if len(line) > LINE_COL_LIMIT:
            limited_line = []
            for word in line.split(' '):
                if len(' '.join(limited_line)) + len(word) > LINE_COL_LIMIT:
                    lines.append(' '.join(limited_line))
                    limited_line = []
                limited_line.append(word)
            lines.append(' '.join(limited_line))
        else:
            lines.append(line)

    return lines