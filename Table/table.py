class ItemTable(dict):
    def __init__(self, keys, values):
        super().__init__()
        try:
            for i in range(len(keys)):
                self[keys[i]] = values[i]

        except IndexError:
            pass

    def show_table(self):
        m_keys = max(len(key) for key in list(self.keys()))
        m_value = max(len(key) for key in list(self.values())[0])
        max_length = m_keys if m_keys > m_value else m_value
        if max_length%2 != 0: max_length+=1

        for key in list(self.keys()):
            print(key.title().center(max_length), end="|")

        print('')
        for i in range(len(list(self.values())[0])):
            for item in list(self.values()):
                print(str(item[i]).center(max_length), end="|")
            print('')
    
    def add_line(self, new_values):
        try:
            for i in range(len(new_values)):
                self[list(self.keys())[i]].append(new_values[i])
            
        except Exception as exception:
            return exception

    def rem_line(self, index):
        try:
            for key in list(self.keys()):
                del self[key][index]

        except IndexError:
            return "IndexError: given index its out of the range"

    def add_column(self, column_name, new_values):
        total_len = 0
        for i in range(len(list(self.values()))):
            total_len += len(list(self.values())[i])
        
        if len(new_values) > (total_len/len(list(self.values()))):
            return "LengthError: more values were given than needed"
        
        elif len(new_values) < (total_len/len(list(self.values()))):
            return "LengthError: less values were given than needed"
        
        else:
            self[column_name] = new_values
            
    def rem_column(self, column_name):
        try:
            del self[column_name]

        except KeyError:
            return f"KeyError: key '{column_name}' does not exists"

    def verify_column_isnumber(self, column):
        for item in column:
            try:
                int(item)

            except:
                 return False
            
        else:
            return True
            
    def sum_all_columns(self):
        sum = 0
        for item in list(self.values()):
            isnumm = self.verify_column_isnumber(item)

            for value in item:
                if isnumm:
                    sum += float(value)

        return sum

    def mean_all_columns(self):
        sum = 0
        count =0
        for item in list(self.values()):
            isnumm = self.verify_column_isnumber(item)

            for value in item:
                if isnumm:
                    sum += float(value)
                    count += 1
                    
        return f"{(sum/count):.2f}"

    def filter_line(self, cond_func):
        return_table = {column: [] for column in self.keys()}
        
        num_lines = len(next(iter(self.values())))
        
        for i in range(num_lines):
            line = {column: self[column][i] for column in self.keys()}
            
            if cond_func(line):
                for column in self.keys():
                    return_table[column].append(line[column])
        
        return return_table
    
def csv_reader(csv_path):
    with open(csv_path, "r", encoding="utf-8-sig") as csv:
        list1 = csv.read().split("\n")
        keys = list1.pop(0).split(",")
        p_values = []
        values = [[] for x in range(len(keys))]

        for i in range(len(list1)):
            p_values.append(list1[i].split(","))
            
        for j in range(len(p_values[0])):
            for item in p_values:
                try:
                    values[j].append(item[j])
                except: pass

        csv.close()

    return (keys, values)
