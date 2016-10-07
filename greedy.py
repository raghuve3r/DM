from utils_greedy import *
from Tree import *


def float_or_str(s):
    try:
        return float(s)
    except ValueError:
        return str(s)


# Convert all the marked string to (0,1,2,etc)
def get_marked_values(mark):
    mark_val = {}
    for key in mark:
        mark[key] = list(set(mark[key]))
        size_key = len(mark[key])
        mark_val[key] = dict(zip(mark[key], [i for i in range(size_key)]))
    return mark_val


# Use all the marked data to convert string to int of 0,1,2..
def convert_data_mark(mark_val, my_data, mark):
    for record in my_data:
        for key in record:
            if key in mark.keys():
                #  change value of string to 0,1,2,etc
                val = record[key]
                record[key] = mark_val[key][val]
    return my_data


def data_pop(lines, attr):
    my_data = list()
    mark = {}
    for line in lines:
        i = dict(zip(attr, [str(j.strip()) for j in line.split(",")]))
        my_data.append(i)
    for i in my_data:
        dict_data = i
        for key in dict_data:
            # Convert each data to either float or string
            dict_data[key] = float_or_str(dict_data[key])
            # If an attribute is just string, mark the attribute & Values
            if type(dict_data[key]) == type("String"):
                if not key in mark.keys():
                    mark[key] = list()
                mark[key].append(dict_data[key])
    mark_val = get_marked_values(mark)
    my_data = convert_data_mark(mark_val, my_data, mark)
    return my_data


def get_data(filename):
    input_file = open(filename, "r")
    lines = []
    attr = input_file.readline().split(",")
    for line in input_file.readlines():
        lines.append(line.strip())
    return data_pop(lines, attr), attr


def classification_data(example, tree):
    if isinstance(tree, (float,int)):
        return tree
    else:
        attr = tree.keys()[0]
        j = example[attr]
        if j in tree[attr].keys():
            t = tree[attr][example[attr]]
        else:
            return tree
        return classification_data(example, t)


def classify_tree(tree, copy_data):
    classify = []
    for i in copy_data:
        classify.append(classification_data(i, tree))
    return classify


def decision_tree(data, target, attributes, split):
    data = data[:]
    target_values = [i[target] for i in data]
    if not data or len(attributes) - 1 <= 0:
        # Get the most values as the node in the base case and return as the leaf node
        class_val = most_values(target, data)
        return Node(class_val, target)
    elif len(target_values) == target_values.count(target_values[0]):
        # If all values in the list are the same then return that as a leaf node.
        return Node(target_values[0], target)
    else:
        best_attribute = get_best(data, attributes, target, split)
        med = get_median(data, best_attribute)
        large_records = get_greater_examples(data, best_attribute, med)
        small_records = get_lesser_examples(data, best_attribute, med)
        # get examples and call them both
        # Create a Node.
        k = [a for a in attributes if a != best_attribute]
        root = Node(med, best_attribute)
        root.dict = data
        root.left = decision_tree(small_records, target, k, split)
        root.right = decision_tree(large_records, target, k, split)
    return root


def check_test_data(root, value, target):
    if root.left is None and root.right is None:
        if root.data == value[target]:
            return True
        else:
            return False
    elif value[root.label] > root.data:
        return check_test_data(root.right, value, target)
    else:
        return check_test_data(root.left, value, target)


def one_fold(inp_data, start, end, attr, split, pos):
    inp_data = inp_data[:]
    test_data = inp_data[start:end]
    train_data = [item for item in inp_data if item not in test_data]
    root = Tree()
    root = decision_tree(train_data, attr[pos], attr, split)
    correct = 0
    for value in test_data:
        if check_test_data(root, value, attr[pos]):
            correct += 1
    return (correct * 100) / len(test_data)


def run_code(filename):
    inp_data, attr = get_data(filename)
    item = int(len(inp_data) * 0.1)
    mean_accuracy = 0
    split = 1
    split = input("Choose INFO GAIN 1, GINI 0: ")
    pos = -1
    pos = input("Enter the attribute position to be used: ")
    for i in range(0, 10):
        end = len(inp_data) - item * i
        start = end - item
        mean_accuracy += one_fold(inp_data, start, end, attr, split, pos)
    print "Percentage of Accuracy for: ", filename, " : ", float(mean_accuracy/10)


if __name__ == "__main__":
    filename = ["iris.data", "wine.data"]
    for i in filename:
        run_code(i)
