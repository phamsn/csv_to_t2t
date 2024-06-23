# CSV to Time2Track
---

Project for creating activities in Time2Track from a csv file.

The python script will open up the Time2Track webpage, log in with
the provided credentials, and start adding activities as if you were
to click on the webpage yourself

run `./csv_to_t2t.py --help` for some more details

## CSV Format
---

- The CSV file should follow the usual CSV file format.
- Values from the CSV file will be input into the web page fields as-is.
- For the assessments column, values should be in the following format:

```
<assessment name 1>,<adult administered 1>,<adult report 1>,<adult research 1>,<child administered 1>,<child report 1>,<child research 1>,...,<assessment name N>,<adult administered N>,<adult report N>,<adult research N>,<child administered N>,<child report N>,<child research N>
```

see [sample.csv](./sample.csv) for working csv example
