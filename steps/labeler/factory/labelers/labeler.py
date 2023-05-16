import constants

class Labeler():
    def __init__(self) -> None:
        self.arch_styles = {}

    def save_label(self, filepath, label, language):
        with open(f"{constants.labels_output}/{language}-labels.csv", 'a') as labels:
            labels.write(f'{label},{filepath}\n')
            labels.flush()
            # check if string present in a file

    def calculate_label(self, file_path: str):
        results = {}
        all_found_keys = []
        maxi_score = 0
        maxi_key = ''
        for arch_key in self.arch_styles:
            all_found = True
            score = 0
            for term in self.arch_styles[arch_key]:
                found = self.search_str(file_path, term)
                if found: score += 1
                all_found = all_found and found
            if all_found: all_found_keys.append(arch_key)
            results[arch_key] = score
            if maxi_score <= score: maxi_key = arch_key
        if len(all_found_keys) > 0:
            maxi_score = 0
            maxi_key = ''
            for key in all_found_keys:
                if len(self.arch_styles[key]) >= maxi_score:
                    maxi_key = key
        return results, all_found_keys, maxi_key

    def search_str(self, file_path, word):
        with open(file_path, 'r') as file:
            # read all content of a file
            try:
                content = file.read()
                if word in content:
                    return True
                else:
                    return False
            except Exception as e:
                print("error reading file", file, e)
                return False


    def get_label(self, file_path, file, language):
        pass
