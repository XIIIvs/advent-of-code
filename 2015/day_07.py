import re

PATTERN = re.compile(r"([0-9a-zA-Z ]+) -> ([a-z]+)")
NOT_PATTERN = re.compile(r"^NOT ([a-z]+)$")
INPUT_PATTERN = re.compile(r"^([a-z0-9]+)$")
TWO_INPUT_PATTERN = re.compile(r"^([0-9a-z]+) ([A-Z]+) ([a-z0-9]+)$")

LOGIC_GATES_OUTPUTS = dict()
LOGIC_GATE_KEYS_TO_PROCESS = set()

PART_2 = True

class KeyOrValue:
    def __init__(self, key_or_value: str):
        self.key: str = None
        self.value: int = None

        if key_or_value.isnumeric():
            self.value = int(key_or_value)
        else:
            self.key = key_or_value

    def get(self) -> int:
        if self.value is not None:
            return self.value
        else:
            return LOGIC_GATES_OUTPUTS[self.key].value

    def __repr__(self):
        return f"<K: {self.key}>" if self.key is not None else f"<V: {self.value}>"


class Gate:
    def __init__(self, name, value=None, operation=None):
        self.name = name
        self.value = value
        self.operation = operation

    def __repr__(self):
        return f"Gate [{self.name}] {self.operation}"


class Same:
    def __init__(self, input_a):
        self.a = KeyOrValue(input_a)

    def process(self):
        a = self.a.get()
        if a is not None:
            return a
        return None

    def __repr__(self):
        return f"SAME {self.a}"


class Not:
    def __init__(self, input_a):
        self.a = KeyOrValue(input_a)

    def process(self):
        a = self.a.get()
        if a is not None:
            return ~a
        return None

    def __repr__(self):
        return f"NOT {self.a}"


class And:
    def __init__(self, input_a, input_b):
        self.a = KeyOrValue(input_a)
        self.b = KeyOrValue(input_b)

    def process(self):
        a = self.a.get()
        b = self.b.get()
        if a is not None and b is not None:
            return a & b
        return None

    def __repr__(self):
        return f"{self.a} AND {self.b}"


class Or:
    def __init__(self, input_a, input_b):
        self.a = KeyOrValue(input_a)
        self.b = KeyOrValue(input_b)

    def process(self):
        a = self.a.get()
        b = self.b.get()
        if a is not None and b is not None:
            return a ^ b
        return None

    def __repr__(self):
        return f"{self.a} OR {self.b}"


class RShift:
    def __init__(self, input_a, input_b):
        self.a = KeyOrValue(input_a)
        self.b = KeyOrValue(input_b)

    def process(self):
        a = self.a.get()
        b = self.b.get()
        if a is not None and b is not None:
            return a >> b
        return None

    def __repr__(self):
        return f"{self.a} RSHIFT {self.b}"


class LShift:
    def __init__(self, input_a, input_b):
        self.a = KeyOrValue(input_a)
        self.b = KeyOrValue(input_b)

    def process(self):
        a = self.a.get()
        b = self.b.get()
        if a is not None and b is not None:
            return a << b
        return None

    def __repr__(self):
        return f"{self.a} LSHIFT {self.b}"


with open("07_input", "r") as file_input:
    for line in file_input:
        match = PATTERN.match(line.strip())
        if match is not None:
            operation_string = match.group(1)
            output = match.group(2)

            if PART_2 and output == 'b':
                LOGIC_GATES_OUTPUTS[output] = Gate(output, value=46065)
                continue

            not_match = NOT_PATTERN.match(operation_string)
            input_match = INPUT_PATTERN.match(operation_string)
            two_input_match = TWO_INPUT_PATTERN.match(operation_string)

            if input_match is not None:
                value_string = input_match.group(1)
                if value_string.isnumeric():
                    int_value = int(value_string)
                    LOGIC_GATES_OUTPUTS[output] = Gate(output, value=int_value)
                else:
                    LOGIC_GATES_OUTPUTS[output] = Gate(output, operation=Same(value_string))
                    LOGIC_GATE_KEYS_TO_PROCESS.add(output)

            elif not_match is not None:
                value_string = not_match.group(1)
                LOGIC_GATES_OUTPUTS[output] = Gate(output, operation=Not(value_string))
                LOGIC_GATE_KEYS_TO_PROCESS.add(output)

            elif two_input_match is not None:
                input_one_string = two_input_match.group(1)
                operation_type_string = two_input_match.group(2)
                input_two_string = two_input_match.group(3)

                operation = None
                if operation_type_string == "RSHIFT":
                    operation = RShift(input_one_string, input_two_string)
                elif operation_type_string == "LSHIFT":
                    operation = LShift(input_one_string, input_two_string)
                elif operation_type_string == "AND":
                    operation = And(input_one_string, input_two_string)
                elif operation_type_string == "OR":
                    operation = Or(input_one_string, input_two_string)
                else:
                    print(f"Operation {operation_type_string} is not defined")
                LOGIC_GATES_OUTPUTS[output] = Gate(output, operation=operation)
                LOGIC_GATE_KEYS_TO_PROCESS.add(output)
            else:
                print(f"Line [{line.strip()}] operation `{operation_string}` not match")

while len(LOGIC_GATE_KEYS_TO_PROCESS) > 0:
    to_process_collection = list(LOGIC_GATE_KEYS_TO_PROCESS)
    for key_to_process in to_process_collection:
        gate = LOGIC_GATES_OUTPUTS[key_to_process]
        result = gate.operation.process()
        if result is not None:
            gate.value = result
            LOGIC_GATE_KEYS_TO_PROCESS.remove(key_to_process)

print(f"Part {2 if PART_2 else 1} - wire `a` input: {LOGIC_GATES_OUTPUTS['a'].value}")
