# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
Creates updated_drivers.rst which includes import names for each module.
"""

if __name__ == '__main__':
    with open('docs/drivers.rst', 'r') as drivers_rst:
        with open("updated_drivers.rst", "w") as updated_drivers_rst:
            lines = drivers_rst.readlines()

            for line in lines:

                if "<https://docs.circuitpython.org/" in line:
                    docs_url = line.split("<")[1].split(">")[0]
                    #print(docs_url)

                    short_name = line.split("https://docs.circuitpython.org/projects/")[1].split("/en/latest/")[0]
                    insert_index = line.index("<") - 1
                    #print(f"adafruit_{short_name} | {insert_index}")

                    modified = line[:insert_index] + f" (adafruit_{short_name})" + line[insert_index:]
                    #print(modified)
                    updated_drivers_rst.write(modified)
                else:
                    updated_drivers_rst.write(line)
