from data_analiser import DataAnaliser
from args_parser import createParser


if __name__ == '__main__':

    parser = createParser()
    namespace = parser.parse_args()
    result = DataAnaliser(namespace)
    result.script()