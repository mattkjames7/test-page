from update_readme import splitPageSections,splitTableSection,updateTable,parseTable


jsondata = """
{
    "date": 20230119,
    "tests": "pass",
    "packages": {
        "ubuntu-22.04": {
            "x86_64": "https://dhfsudhfuodhfo",
            "arm64": "https://dhfsudhfuodasfdasfo"
        },
        "ubuntu-24.04": {
            "x86_64": "https://dhfsudhfuodhfo",
            "arm64": "https://dhfsudhfuodasfdasfo"
        },
        "fedora-41": {
            "x86_64": "https://dhfsudhfuodhfo"
        }
    }
}"""

def testReadFile():
    fname = "README.md"


    beforeSection,tableSection,afterSection = splitPageSections(fname,"memgraph")

    print("######### before #########")
    print("\n".join(beforeSection))


    print("######### table #########")
    print("\n".join(tableSection))


    print("######### after #########")
    print("\n".join(afterSection))


def testReadTable():
    fname = "README.md"


    beforeSection,tableSection,afterSection = splitPageSections(fname,"memgraph")

    beforeTable,tableLines,afterTable = splitTableSection(tableSection)

    print("######### before #########")
    print("\n".join(beforeTable))


    print("######### table #########")
    print("\n".join(tableLines))


    print("######### after #########")
    print("\n".join(afterTable))


def testParsing():

    fname = "README.md"


    beforeSection,tableSection,afterSection = splitPageSections(fname,"memgraph")

    beforeTable,tableLines,afterTable = splitTableSection(tableSection)   

    tabledata = parseTable(tableLines)
    print(tabledata)

def testInsert():

    updateTable("memgraph",8,jsondata)