# from tabulate import tabulate
from pandas import DataFrame

class TruckTable:

    def __init__(self):
        self.dates = []

    def _add_truck(self, date, truck, income, fuel, maintenance):
        for _list in self.dates:
            # "Unpack" the dates object
            date_i = _list[0]
            truck_i = _list[1]

            # Shouldn't be true, but just in case
            if date == date_i and truck == truck_i:
                return

        self.dates.append([date, truck, income, fuel, maintenance])

    def update_truck(self, date, truck, income=0, fuel=0, maintenance=0):
        if len(self.dates) > 0:
            # Search the table for the corresponding date and truck:
            for _list in self.dates:
                # "Unpack" the dates object
                date_i = _list[0]
                truck_i = _list[1]
                income_i = _list[2]
                fuel_i = _list[3]
                maintenance_i = _list[4]

                # If date-truck pair is already in the table:
                if date == date_i and truck == truck_i:
                    # Update the entry by adding the new values
                    self.dates[self.dates.index(_list)] = ( [
                        date,
                        truck,
                        income + income_i,
                        fuel + fuel_i,
                        maintenance + maintenance_i
                        ] )
                    return

        # If date-truck pair is not already in the table:
        self._add_truck(date, truck, income, fuel, maintenance)


    def tabulate(self):
        data = []
        header = ["", ""]

        def align_to_date(n, element_1, element_2, element_3):
            list_1 = [element_1, element_2]
            list_2 = ["" for i in range(n-1)]
            list_3 = [element_3]

            return list_1 + list_2 + list_3

        for _list in self.dates:
            # "Unpack" the dates object
            date_i = _list[0]
            truck_i = _list[1]
            income_i = _list[2]
            fuel_i = _list[3]
            maintenance_i = _list[4]

            # Format the data
            if date_i not in header:
                header.append(date_i)

            align = len(header) - 2

            data.append(align_to_date(align, truck_i, "Income:", "{}".format(income_i)))
            data.append(align_to_date(align, "",      "Fuel:", "{}".format(fuel_i)))
            data.append(align_to_date(align, "",      "Maintenance:", "{}".format(maintenance_i)))

            # TODO: Collapse entries for the same truck on different dates into
            # a single row

        # tabulated_data = tabulate(data, header, tablefmt="simple")
        tabulated_data = DataFrame(data, columns=header)
        return(tabulated_data)