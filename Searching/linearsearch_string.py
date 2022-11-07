def linearsearch_string(input, target):
    if len(input) == 0:
        return False
    for i in input:
        if i == target:
            return True
    return False

def main():
    name = "vibhavari"
    target = 'i'

    result = linearsearch_string(name, target)
    if result == False:
        print("Element not found")
    else:
        print("Element found at position: {}".format(result))


if __name__ == "__main__":
        main()