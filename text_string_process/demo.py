"""把包含石油的行保存下来"""


def read_file(file_path):
    """
    read data from file_path
    """
    with open(file_path, encoding="utf-8") as f:
        return f.read()


def write_file(file_path, context):
    """
    write the context to the file_path
    """
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(context)


def find_keys_words_and_save(input_file_name, keyword, output_file_name):
    """
    find all text lines from input_file which contains the keyword
    and store into the output file
    """
    input_str = read_file(input_file_name)
    keyword_lines = []
    for line in input_str.split('\n'):
        if keyword in line:
            keyword_lines.append(line)
    context = '\n'.join(keyword_lines)
    write_file(output_file_name, context)


def main():
    """
    main function to find all lines which contains keyword 石油
    """
    resource_dir, extension = 'examples/', 'txt'
    input_file_name = resource_dir + '.'.join(['news', extension])
    keyword = '石油'
    output_file_name = resource_dir + '.'.join([keyword, extension])
    find_keys_words_and_save(input_file_name, keyword, output_file_name)


if __name__ == '__main__':
    main()
