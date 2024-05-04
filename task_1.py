def underscore_to_camelcase(name):
    words = name.split('_')
    camelcase_name = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camelcase_name

input_name = input("Enter the name in the format underscore: ")
camelcase_name = underscore_to_camelcase(input_name)
print("Name in the format CamelCase:", camelcase_name)