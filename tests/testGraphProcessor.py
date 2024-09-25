import unittest

from GraphProcessor import GraphProcessor


class TestGraphProcessor(unittest.TestCase):

    def test_process_rules(self):
        NV, NE = 8, 8
        edges = [(1, 2), (2, 4), (3, 4), (4, 5), (6, 5), (5, 7), (7, 6), (7, 8)]
        rules = [
            "0.1", "2", "0.2", "min e 2 e 3", "min e 4 e 5", "0.5", "0.3", "e 8",
            "v 1", "* v 2 e 1", "v 3", "v 4", "* v 6 e 7", "v 5", "v 7", "v 7"
        ]

        expected_attributes = [
            0.1, 2.0, 0.2, 0.2, 0.15, 0.5, 0.3, 0.3, 0.1, 0.2, 0.2, 0.2, 0.15, 0.15, 0.3, 0.3
        ]

        processor = GraphProcessor(NV, NE, edges, rules)
        result = processor.process_rules()

        self.assertEqual(result, expected_attributes)

    def test_read_input(self):
        input_data = "8 8\n\n1 2\n2 4\n3 4\n4 5\n6 5\n5 7\n7 6\n7 8\n\n" \
                     "0.1\n2\n0.2\nmin e 2 e 3\nmin e 4 e 5\n0.5\n0.3\n" \
                     "e 8\nv 1\n* v 2 e 1\nv 3\nv 4\n* v 6 e 7\nv 5\nv 7\nv 7\n"

        with open('input_test.txt', 'w') as f:
            f.write(input_data)

        NV, NE, edges, rules = GraphProcessor.read_input('input_test.txt')

        self.assertEqual(NV, 8)
        self.assertEqual(NE, 8)
        self.assertEqual(edges, [(1, 2), (2, 4), (3, 4), (4, 5), (6, 5), (5, 7), (7, 6), (7, 8)])
        self.assertEqual(rules, [
            "0.1", "2", "0.2", "min e 2 e 3", "min e 4 e 5", "0.5", "0.3", "e 8",
            "v 1", "* v 2 e 1", "v 3", "v 4", "* v 6 e 7", "v 5", "v 7", "v 7"
        ])


if __name__ == '__main__':
    unittest.main()
