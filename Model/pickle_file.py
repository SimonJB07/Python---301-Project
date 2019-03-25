from Model.set_up_class import SetUp


class PickleHandler(object):
    def __init__(self):
        pass

    def __str__(self):
        return "Test"


def get_file_to_pickle():
    file = SetUp.uml_list
    return file


if __name__ == "__main__":
    import pickle
    # test1 = Tes()
    # files need to be opened as binary files
    with open('data.pickle', 'wb') as f:
        # pickle.dump(for_function(), f)
        # pickle.dump(test1, f)
        pickle.dump(PickleHandler, f)
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
    # print(id(test1))
    # print(id(data))
    # print(test1 == data)
    print(data)
    test1 = data()
    print(test1)
    print(get_file_to_pickle())
