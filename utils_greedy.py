import math


def most_values(target, data):
    values = [i[target] for i in data]
    high_freq = 0
    most_freq = None
    values = unique(values)
    for value in values:
        if values.count(value) > high_freq:
            most_freq = value
            high_freq = values.count(value)
    return most_freq


def unique(values):
    uniq_values = []
    for i in values:
        if uniq_values.count(i) <= 0:
            uniq_values.append(i)

    return uniq_values


def mean_best(values):
    return sum(values) / len(values)


def get_best(data, attributes, target, split):
    data = data[:]
    best = 0.0
    best_attribute = None

    for a in attributes:
        gain = calculate(data, a, target, split)
        if gain >= best and a != target:
            best = gain
            best_attribute = a

    return best_attribute


def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    else:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0


def get_median(data, best_attribute):
    data = data[:]
    return median([i[best_attribute] for i in data])


def get_values(data, best_attribute):
    data = data[:]
    return unique([i[best_attribute] for i in data])


def get_examples(data, best_attribute, value):
    data = data[:]
    result = []
    if data:
        ex = data.pop()
        if ex[best_attribute] == value:
            result.append(ex)
            result.extend(get_examples(data, best_attribute, value))
            return result
        else:
            result.extend(get_examples(data, best_attribute, value))
            return result
    else:
        return result


def get_greater_examples(data, best_attribute, value):
    data = data[:]
    result = []
    if data:
        ex = data.pop()
        if ex[best_attribute] > value:
            result.append(ex)
            result.extend(get_greater_examples(data, best_attribute, value))
            return result
        else:
            result.extend(get_greater_examples(data, best_attribute, value))
            return result
    else:
        return result


def get_lesser_examples(data, best_attribute, value):
    data = data[:]
    result = []
    if data:
        ex = data.pop()
        if ex[best_attribute] <= value:
            result.append(ex)
            result.extend(get_lesser_examples(data, best_attribute, value))
            return result
        else:
            result.extend(get_lesser_examples(data, best_attribute, value))
            return result
    else:
        return result


def calculate(data, attribute, target, split):
    if split == 1:
        return info_gain(data, attribute, target)
    else:
        return gini(data, attribute, target)


def gini(data, attribute, target):
    freq = get_attribute_data(data, attribute)
    children_gini = 0.0
    total = sum(freq.values())
    for i in freq.keys():
        prob = freq[i] / total
        children_data = [j for j in data if j[attribute] == i]
        children_gini += prob * gini_coeff(children_data, target)

    result = 1 - children_gini
    return result


def gini_coeff(children_data, target):
    freq = get_attribute_data(children_data, target)
    value = 0.0
    for i in freq.values():
        value += (i/len(children_data)) * (i/len(children_data))

    return value


def info_gain(data, attribute, target):
    freq = get_attribute_data(data, attribute)
    children_entropy = 0.0
    total = sum(freq.values())
    for i in freq.keys():
        prob = freq[i] / total
        children_data = [j for j in data if j[attribute] == i]
        children_entropy += prob * entropy(children_data, target)

    result = entropy(data, target) - children_entropy
    return result


def entropy(data, target):
    freq = get_attribute_data(data, target)
    entrop = 0.0
    for i in freq.values():
        entrop += (-i/len(data)) * math.log(i/len(data), 2)

    return entrop


def get_attribute_data(data, attribute):
    freq = {}
    for i in data:
        if i[attribute] in freq.keys():
            freq[i[attribute]] += 1.0
        else:
            freq[i[attribute]] = 1.0
    return freq
