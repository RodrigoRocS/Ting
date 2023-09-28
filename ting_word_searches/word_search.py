def exists_word(word, instance):
    results = []

    for i in range(len(instance)):
        file_info = instance.search(i)
        file_name = file_info["nome_do_arquivo"]
        lines = file_info["linhas_do_arquivo"]
        occurrences = []

        for line_number, line in enumerate(lines, start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_number})

        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return results


def search_by_word(word, instance):
    results = []

    for i in range(len(instance)):
        file_info = instance.search(i)
        lines = file_info["linhas_do_arquivo"]
        occurrences = []

        for line_number, line_content in enumerate(lines, start=1):
            if word.lower() in line_content.lower():
                occurrences.append({
                    "linha": line_number, "conteudo": line_content
                    })

        if occurrences:
            result = {
                "palavra": word,
                "arquivo": file_info["nome_do_arquivo"],
                "ocorrencias": occurrences
            }
            results.append(result)

    return results
