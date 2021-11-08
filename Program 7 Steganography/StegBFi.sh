#!/bin/sh
#!/usr/bin/python3
#!/usr/bin/env python
python3 Steg.py -r -B -o1 -i1 -w > 1.jpg
python3 Steg.py -r -B -o1 -i2 -w > 2.jpg
python3 Steg.py -r -B -o1 -i4 -w > 3.jpg
python3 Steg.py -r -B -o1 -i8 -w > 4.jpg
python3 Steg.py -r -B -o1 -i16 -w > 5.jpg
python3 Steg.py -r -B -o1 -i32 -w > 6.jpg
python3 Steg.py -r -B -o1 -i64 -w > 7.jpg
python3 Steg.py -r -B -o1 -i128 -w > 8.jpg
python3 Steg.py -r -B -o1 -i256 -w > 9.jpg
python3 Steg.py -r -B -o1 -i512 -w > 10.jpg
python3 Steg.py -r -B -o1 -i1024 -w > 11.jpg
python3 Steg.py -r -B -o1 -i2048 -w > 12.jpg
python3 Steg.py -r -B -o1 -i4096 -w > 13.jpg
python3 Steg.py -r -B -o1 -i8192 -w > 14.jpg
python3 Steg.py -r -B -o1 -i16384 -w > 15.jpg
python3 Steg.py -r -B -o1 -i32768 -w > 16.jpg

