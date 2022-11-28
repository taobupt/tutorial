# ------------把包含石油的行保存下来--------------
def read_file(file_path):
    with open(file_path) as f:
        return f.read()


def write_file(file_path, context):
    with open(file_path, 'w') as f:
        f.write(context)


def find_keys_words_and_save(input_file_name, keyword, output_file_name):
    input_str = read_file(input_file_name)
    keyword_lines = []
    for line in input_str.split('\n'):
        if keyword in line:
            keyword_lines.append(line)
    context = '\n'.join(keyword_lines)
    write_file(output_file_name, context)


def main():
    resource_dir, extension = 'examples/', 'txt'
    input_file_name = resource_dir + '.'.join(['news', extension])
    keyword = '石油'
    output_file_name = resource_dir + '.'.join([keyword, extension])
    find_keys_words_and_save(input_file_name, keyword, output_file_name)


if __name__ == '__main__':
    main()
