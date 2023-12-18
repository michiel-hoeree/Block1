

def pretty_print(dictionary):
    for level in dictionary:
        if type(dictionary[level]) == list:
            for child in dictionary[level]:
                pretty_print(child)
        else:
            tabs = int(dictionary[level][6]) * "\t"
            print(f"{tabs}{dictionary[level]}")


folder_hierarchy = {
    "name": "level 1 directory",
    "children": [
        {
            "name": "level 2 directory A",
            "children": [
                {
                    "name": "level 3 directory A1",
                    "children": []
                },
                {
                    "name": "level 3 directory A2",
                    "children": []
                }
                ]
        },
        {
            "name": "level 2 directory B",
            "children": [
                {
                    "name": "level 3 directory B1",
                    "children": []
                }
                ]
        },
        {
            "name": "level 2 directory C",
            "children": [
                {
                    "name": "level 3 directory C1",
                    "children": []
                },
                {
                    "name": "level 3 directory C2",
                    "children": []
                },
                {
                    "name": "level 3 directory C3",
                    "children": []
                }
                ]
        }
]
}

pretty_print(folder_hierarchy)