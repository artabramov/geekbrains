class Dept:
    def __init__(self, name):
        self.name = name
        self.devices = {}

    def append(self, device):
        self.devices[device.id] = device

    def transfer(self, device, dept):
        dept.append(self.devices[device.id])
        self.exclude(device)

    def exclude(self, device):
        self.devices.pop(device.id)

    @property
    def total_cost(self):
        return sum([self.devices[id].cost for id in self.devices])

    def __str__(self):
        return ''.join([self.devices[id].params for id in self.devices])


class Technics:
    def __init__(self, id, name, cost=0):
        self.id = Technics._validate(id, int)
        self.name = Technics._validate(name, str)
        self.cost = Technics._validate(cost, int)

    @staticmethod
    def _validate(value, value_type):
        if not isinstance(value, value_type):
            raise ValueError(f'value {value} must be an instance of {value_type}')
        return value

    @property
    def params(self):
        return f'id: {self.id}, name: {self.name}, cost: {self.cost}, '


class Printer(Technics):
    def __init__(self, id, name, is_color, print_type, cost=0):
        super().__init__(id, name, cost)
        self.is_color = Technics._validate(is_color, bool)
        self.print_type = Technics._validate(print_type, str)

    @property
    def params(self):
        return super().params + f'is color: {self.is_color}, print type: {self.print_type}\n'


class Scanner(Technics):
    def __init__(self, id, name, resolution, cost=0):
        super().__init__(id, name, cost)
        self.resolution = Technics._validate(resolution, str)

    @property
    def params(self):
        return super().params + f'resolution: {str(self.resolution)}\n'


class Copier(Technics):

    def __init__(self, id, name, is_color, print_type, resolution, cost=0):
        super().__init__(id, name, cost)
        self.is_color = Technics._validate(is_color, bool)
        self.print_type = Technics._validate(print_type, str)
        self.resolution = Technics._validate(resolution, str)

    @property
    def params(self):
        return super().params + \
               f'is color: {self.is_color}, print type: {self.print_type}, resolution: {str(self.resolution)}\n'


if __name__ == '__main__':
    printer_1 = Printer(1975243205, 'HP LaserJet Pro M15w', False, 'laser', 8690)
    printer_2 = Printer(10782150, 'Epson L120', True, 'stream', 10990)
    scanner_1 = Scanner(225699269, 'Canon CanoScan LiDE 300', '2400x2400', 5690)
    copier_1 = Copier(11154747, 'Xerox WorkCentre 3025BI', False, 'laser', '600x600', 14390)

    it_dept = Dept('IT department')
    it_dept.append(printer_1)
    it_dept.append(printer_2)
    it_dept.append(scanner_1)
    it_dept.append(copier_1)

    sales_dept = Dept('Sales department')
    it_dept.transfer(printer_2, sales_dept)

    print(f'{it_dept.name} (total {it_dept.total_cost}):', it_dept, sep='\n', end='\n\n')
    print(f'{sales_dept.name} (total {sales_dept.total_cost}):', sales_dept, sep='\n', end='\n\n')
