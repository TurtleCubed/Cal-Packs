
class ImageReader:
    @staticmethod
    def text_to_array(file_name):
        file = open("DinoImages/" + file_name, "r")
        file_text = file.read()
        rows = int(file_text[0:file_text.find(" ")])
        file_text = file_text[file_text.find(" ") + 1:]
        cols = int(file_text[0:file_text.find("\n")])
        file_text = file_text[file_text.find("\n") + 1:]

        array = [[0 for x in range(cols)] for y in range(rows)]

        print(rows, cols)
        print(len(array[0]), len(array))

        list_of_rows = file_text.split("\n")

        for i in range(len(list_of_rows)):
            for j in range(len(list_of_rows[i])):
                array[i][j] = int(list_of_rows[i][j])

        for i in range(len(array)):
            for j in range(len(array[0])):
                print(array[i][j], end='')
            print('')

        return array




