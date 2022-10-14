import json, os.path


def Read(Point):
    Path = "Data/Config.json"

    if (os.path.exists(Path)):
        File = open(Path, "r")
        Data = json.loads(File.read())
        File.close()

        return Data[Point]

    else:
        print(f"БД '{Path}' не найдена...")