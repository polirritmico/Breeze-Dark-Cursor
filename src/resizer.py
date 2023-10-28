#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

PATH = "config/"


def main():
    files = os.listdir(PATH)
    files.sort()
    target_proportions = [1, 1.34, 1.5, 2, 2.67, 4]
    for file in files:
        output_file = []
        with open(PATH + file, "r") as stream:
            raw_data = stream.read().split("\n")
        base_data = raw_data[0].split(" ")
        if len(base_data) == 4:
            for proportion in target_proportions:
                new_line = []
                for i in range(3):
                    new_value = int(int(base_data[i]) * proportion)
                    new_line.append(str(new_value))
                new_line.append(base_data[3])
                output_file.append(" ".join(new_line))
        elif len(base_data) == 5:
            # get all base proportion (x1) lines
            base_size = base_data[0]
            base_data = []
            for current_line in raw_data:
                current_line = current_line.split(" ")
                if current_line[0] != base_size:
                    break
                base_data.append(current_line)
            for proportion in target_proportions:
                for line in base_data:
                    new_line = []
                    for i in range(3):
                        new_value = int(int(line[i]) * proportion)
                        new_line.append(str(new_value))
                    new_line.append(line[3])
                    new_line.append(line[4])
                    output_file.append(" ".join(new_line))
        else:
            raise NotImplementedError("Expecting 4 or 5 parameters per line")

        output_file = "\n".join(output_file) + "\n"
        with open(PATH + file, "w", encoding="ascii") as stream:
            stream.write(output_file)

    return 0


if __name__ == "__main__":
    main()
