import fire
import os

# additional function
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

# tests
def test_on_dev_activity_in_manifest(path):
    print("test_on_dev_activity_in_manifest" + " path=" + path)
    manifest_files = find_all("AndroidManifest.xml", path)
    print(manifest_files)

# main function
def start_scan(path):
    print("Scanning started at path: " + path)

    # tests
    test_on_dev_activity_in_manifest(path)

    print("Scanning finished.")

if __name__ == '__main__':
  fire.Fire(start_scan)
