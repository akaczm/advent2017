import re
from collections import Counter
from anytree import Node, RenderTree, ContStyle

REGEX_STR = r"(?P<name>^\w+) \((?P<weight>\d+)\)(?P<arrow> ->)?(?(arrow) (?P<children>.+\w+)$)"

def parse_input():
    outputlist = []
    p = re.compile(REGEX_STR)
    with open('input.txt') as items:
        for line in items:
            match = p.match(line)
            outputlist.append(match.groupdict())
    return outputlist

def build_tree():
    item_list = parse_input()
    treedict = {}
    for item in item_list:
        try: 
            parent = treedict[item['name']]
            parent.weight = item['weight']
        except KeyError:
            treedict[item['name']] = Node(item['name'])
            parent = treedict[item['name']]
            parent.weight = item['weight']
        
        if item['children'] is None:
            pass
        else:
            children = item['children']
            children = list(map(str.strip, children.split(',')))
            for child in children:
                try:
                    childnode = treedict[child]
                    childnode.parent = parent
                except KeyError:
                    treedict[child] = Node(child, parent=parent)
    return treedict

def calculate_weight(nodetree, weight=0):
    if nodetree.is_leaf:
        nodetree.sumweight = int(nodetree.weight)
    weight = int(nodetree.weight)
    for leg in nodetree.descendants:
        weight += int(leg.weight)
    nodetree.sumweight = weight
    for child in nodetree.children:
        calculate_weight(child)
    return nodetree

def check_equal(iterator):
   return len(set(iterator)) <= 1

def most_common(lst):
    data = Counter(lst)
    return max(lst, key=data.get)

def compare_weights(nodetree, parent=None, prev=True, **kwargs):
    weights = []
    if nodetree.is_leaf:
        pass
    for child in nodetree.children:
        weights.append(child.sumweight)
    if check_equal(weights) and prev is False:
        # now I know this object is the problem
        diff = nodetree.sumweight - most_common(kwargs['prevweights'])
        return int(nodetree.weight) - diff
    else:
        counter = Counter(weights)
        odd_weight = weights.index(min(counter, key=counter.get))
        odd_child = nodetree.children[odd_weight]
        return compare_weights(odd_child, nodetree, prev=False, prevweights=weights)
    
        
tree = calculate_weight(build_tree()['mwzaxaj'])
print(compare_weights(tree))